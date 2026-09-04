# Login Agent (self-hosted, open-source browser-use)

Signup/login ka semi-auto worker — AAPKI machine pe chalta hai (asli India
IP = kam blocks), CAPTCHA-solving koi nahi (CAPTCHA aaye to khuli browser
window mein KHUD solve karo, agent aage badhega), passwords sirf local
`.env` mein (git ignored, Claude kabhi nahi dekhta).

## Setup (5 min, ek baar)

1. `./setup.sh`
2. `.env` bharo: LLM key (OpenRouter pe $10 daalo — 40 signups ≈ $2-8/mahina)
   + `AGENT_EMAIL` + har site ka unique password
3. `tasks.json` mein sites (example copy ho jaata hai)

## Roz ka use

- Naye accounts (TEAM chalaye, apni marzi se): `./.venv/bin/python run_batch.py signup`
- Sessions refresh: `./.venv/bin/python run_batch.py login`
- Browser samne khulega — CAPTCHA/OTP aap karo, baaki agent.
- Report `reports/*.json` mein banti hai → Claude Code ko bolo:
  **"login-agent report padh ke Sheet update karo"** → READY sites pe wo
  fill+submit shuru kar dega.

## Rules

- Crunchbase / G2 / IndiaMART class sites is agent se KABHI nahi (ToS) —
  wo tasks.json mein mat daalo.
- Email verify aaye to status EMAIL_VERIFY_PENDING aata hai — inbox se
  aap verify karo (ya baad mein hum agents@ inbox ka auto-verify jodenge).
- Ek site ek profile (`profiles/<site>/`) — machine badli to profiles
  folder bhi le jao.
