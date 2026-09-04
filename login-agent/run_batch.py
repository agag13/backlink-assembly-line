#!/usr/bin/env python3
"""
Login-agent runner (open-source browser-use, self-hosted). v2 — pilot-1 fixes:
- sensitive_data ab DOMAIN-SCOPED hai (sirf usi site pe inject ho sakta hai)
- fallback LLM (primary JSON-glitch kare to dusra sambhal leta hai)
- CAPTCHA pe agent ab 2.5 min tak WAIT karta hai (human solve kare)
- username rule: lowercase fallback jab site format reject kare

TEAM chalati hai:
    ./.venv/bin/python run_batch.py signup
    ./.venv/bin/python run_batch.py login
"""
import asyncio, json, os, re, sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

from dotenv import load_dotenv

HERE = Path(__file__).parent
load_dotenv(HERE / ".env")

from browser_use import Agent, BrowserProfile  # noqa: E402


def make_llms():
    """(primary, fallback) — dono OpenRouter se."""
    from browser_use.llm.openrouter.chat import ChatOpenRouter
    key = os.getenv("OPENROUTER_API_KEY") or sys.exit("ERROR: .env mein OPENROUTER_API_KEY daalo")
    primary = ChatOpenRouter(model=os.getenv("OPENROUTER_MODEL", "google/gemini-2.5-flash"), api_key=key)
    fb_model = os.getenv("OPENROUTER_FALLBACK_MODEL", "openai/gpt-5.6-luna")
    fallback = ChatOpenRouter(model=fb_model, api_key=key)
    return primary, fallback


def env_key(site: str) -> str:
    return "PASS_" + re.sub(r"[^A-Z0-9]", "_", site.upper())


COMMON_RULES = """
USERNAME RULE: if the site asks for a username (or rejects 'FameNinja'), use a
lowercase username like 'fameninja' plus 2-3 digits (e.g. fameninja77). Display
name / company stays: {display_name}.
CAPTCHA RULE: if a CAPTCHA / reCAPTCHA / verification checkbox appears or the
site says a captcha response is missing, DO NOT give up: use the wait action
for 15 seconds, then re-check, repeating up to 10 times (a human is sitting at
this browser and will solve it). Only after ~10 waits report
STATUS=CAPTCHA_WAITED_TIMEOUT.
PASSWORD RULE: if the site rejects the password policy, report
STATUS=FAILED password-policy <what it wants> — do not invent a different password.
PATIENCE: you have 40 steps; slow pages need wait+retry, never declare a time
limit yourself. NEVER pay, never accept paid plans, never accept marketing
subscriptions."""

SIGNUP_TASK = """Go to {url} . Create a new account (sign up) with email x_email and password x_password.
Business context: agency's own business listing account on this directory.
{rules}
If an email verification screen/notice appears after signup, report STATUS=EMAIL_VERIFY_PENDING.
When done (or blocked), report exactly one of:
STATUS=READY | STATUS=EMAIL_VERIFY_PENDING | STATUS=CAPTCHA_WAITED_TIMEOUT | STATUS=FAILED <reason>"""

LOGIN_TASK = """Go to {url} and log in with email x_email and password x_password.
If already logged in (cookies), just confirm.
{rules}
Report exactly one of: STATUS=READY | STATUS=CAPTCHA_WAITED_TIMEOUT | STATUS=FAILED <reason>"""


def root_domain(url: str) -> str:
    host = urlparse(url).netloc.lower()
    return host[4:] if host.startswith("www.") else host


async def run_site(site: dict, mode: str, llms, email: str) -> dict:
    name = site["site"]
    password = os.getenv(env_key(name))
    if not password:
        return {"site": name, "status": "SKIPPED", "reason": f".env mein {env_key(name)} nahi hai"}
    profile = BrowserProfile(user_data_dir=str(HERE / "profiles" / name), headless=False)
    rules = COMMON_RULES.format(display_name=site.get("display_name", "FameNinja"))
    template = SIGNUP_TASK if mode == "signup" else LOGIN_TASK
    task = template.format(url=site["url"], rules=rules)
    dom = root_domain(site["url"])
    scoped_secrets = {f"https://*.{dom}": {"x_email": email, "x_password": password},
                      f"https://{dom}": {"x_email": email, "x_password": password}}
    primary, fallback = llms
    agent = Agent(
        task=task,
        llm=primary,
        fallback_llm=fallback,
        browser_profile=profile,
        sensitive_data=scoped_secrets,
    )
    try:
        history = await agent.run(max_steps=40)
        final = (history.final_result() or "").strip()
    except Exception as e:  # noqa: BLE001
        return {"site": name, "status": "ERROR", "reason": str(e)[:300]}
    m = re.search(r"STATUS=(\w+)", final)
    return {"site": name, "status": m.group(1) if m else "UNKNOWN", "detail": final[:500]}


async def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "login"
    assert mode in ("signup", "login"), "usage: run_batch.py signup|login"
    email = os.getenv("AGENT_EMAIL") or sys.exit("ERROR: .env mein AGENT_EMAIL daalo")
    sites = json.loads((HERE / "tasks.json").read_text())
    llms = make_llms()
    results = []
    for site in sites:
        print(f"\n=== {mode.upper()}: {site['site']} ===")
        r = await run_site(site, mode, llms, email)
        print(" ->", r["status"], r.get("reason", ""))
        results.append(r)
    out = HERE / "reports" / f"{mode}-{datetime.now().strftime('%Y%m%d-%H%M')}.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(results, indent=2))
    print(f"\nReport: {out}\nAb Claude Code ko bolo: 'report padh ke Sheet update karo'")


if __name__ == "__main__":
    asyncio.run(main())
