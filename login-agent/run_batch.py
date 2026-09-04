#!/usr/bin/env python3
"""
Login-agent runner (open-source browser-use, self-hosted).

TEAM chalati hai ye script (signup/login = human-approved step):
    ./.venv/bin/python run_batch.py signup   # tasks.json ke sites pe account banao
    ./.venv/bin/python run_batch.py login    # existing accounts ki sessions refresh karo

Rules (hard-coded philosophy):
- CAPTCHA aaye to agent ruk jayega — browser HEADED khulta hai, wahi pe
  KHUD solve karo, agent aage badh jayega. Koi bypass nahi.
- Passwords .env mein (git mein kabhi nahi) — LLM ko sirf placeholder
  dikhta hai (browser-use sensitive_data), value type-time pe inject hoti hai.
- Har site ka apna Chrome profile (profiles/<site>/) — ek baar login,
  cookies hamesha saved. Claude Code baad mein READY sites pe fill+submit
  karta hai.
- Result reports/<timestamp>.json mein — Claude ise padh ke Sheet update
  karta hai.
"""
import asyncio, json, os, re, sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

HERE = Path(__file__).parent
load_dotenv(HERE / ".env")

from browser_use import Agent, BrowserProfile  # noqa: E402


def make_llm():
    if os.getenv("OPENROUTER_API_KEY"):
        from browser_use.llm.openrouter.chat import ChatOpenRouter
        model = os.getenv("OPENROUTER_MODEL", "google/gemini-2.5-flash")
        return ChatOpenRouter(model=model, api_key=os.environ["OPENROUTER_API_KEY"])
    if os.getenv("GOOGLE_API_KEY"):
        from browser_use.llm.google.chat import ChatGoogle
        return ChatGoogle(model=os.getenv("GOOGLE_MODEL", "gemini-flash-latest"))
    sys.exit("ERROR: .env mein OPENROUTER_API_KEY ya GOOGLE_API_KEY daalo (README dekho)")


def env_key(site: str) -> str:
    return "PASS_" + re.sub(r"[^A-Z0-9]", "_", site.upper())


SIGNUP_TASK = """Go to {url} . Create a new account (sign up) with email x_email and password x_password.
Business context: this is for the agency's own business listing account on this directory.
If the site asks name/company, use: {display_name}.
If an email verification screen appears, say so in your final answer and stop (a human/system will verify).
If a CAPTCHA appears, WAIT — a human will solve it in this browser window, then continue.
NEVER pay for anything, never accept paid plans. When done (or blocked), report exactly one of:
STATUS=READY (logged in, account usable) | STATUS=EMAIL_VERIFY_PENDING | STATUS=CAPTCHA_WAITED_TIMEOUT | STATUS=FAILED <reason>"""

LOGIN_TASK = """Go to {url} and log in with email x_email and password x_password.
If already logged in (cookies), just confirm. If CAPTCHA appears, WAIT for a human to solve it here.
Report exactly one of: STATUS=READY | STATUS=CAPTCHA_WAITED_TIMEOUT | STATUS=FAILED <reason>"""


async def run_site(site: dict, mode: str, llm, email: str) -> dict:
    name = site["site"]
    password = os.getenv(env_key(name))
    if not password:
        return {"site": name, "status": "SKIPPED", "reason": f".env mein {env_key(name)} nahi hai"}
    profile = BrowserProfile(user_data_dir=str(HERE / "profiles" / name), headless=False)
    template = SIGNUP_TASK if mode == "signup" else LOGIN_TASK
    task = template.format(url=site["url"], display_name=site.get("display_name", "FameNinja"))
    agent = Agent(
        task=task,
        llm=llm,
        browser_profile=profile,
        sensitive_data={"x_email": email, "x_password": password},
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
    llm = make_llm()
    results = []
    for site in sites:  # sequential — headed browser, human paas mein
        print(f"\n=== {mode.upper()}: {site['site']} ===")
        r = await run_site(site, mode, llm, email)
        print(" ->", r["status"], r.get("reason", ""))
        results.append(r)
    out = HERE / "reports" / f"{mode}-{datetime.now().strftime('%Y%m%d-%H%M')}.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(results, indent=2))
    print(f"\nReport: {out}\nAb Claude Code ko bolo: 'login-agent report padh ke Sheet update karo'")


if __name__ == "__main__":
    asyncio.run(main())
