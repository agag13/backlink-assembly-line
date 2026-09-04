# DECISION: Login-automation — browser-use direct (no n8n), Hermes abhi nahi

Deep-dive 04-09-2026 (3 agents, vendor docs + GitHub issues + practitioner
reports verify). Detail: RESEARCH-login-automation-2026-09.md.

## Hermes Agent ka seedha jawab

- **Desktop app = galat mode "bina user ke" ke liye.** Wo sirf UI client
  hai — laptop on + awake chahiye; koi cloud relay nahi. Unattended ke liye
  headless gateway chahiye (`hermes gateway install` / Docker) kisi
  always-on Linux machine pe.
- **Andar Grok-jaisa cloud computer NAHI hai** — apna local Chromium chalata
  hai (accessibility-tree se). "Real Profile Browsing" = aapke Chrome
  profile ki cookie-copy — matlab us machine pe pehle se logged-in profile
  chahiye. VPS pe naya IP → directories datacenter-IP block karti hain
  (unka open issue #102731, unsolved). Best host hota office ki always-on
  machine, VPS nahi.
- **CAPTCHA pe stall** ho jaata hai aur human-handoff feature abhi bana hi
  nahi (#12667, Apr-26 se open). Password vault nahi (chmod-600 files).
  **Koi credible signup case study nahi mili** — jo "98% success" articles
  hain wo fabricated SEO slop nikle. 241k★ hai par 39k open issues, weekly
  babysitting.
- Pricing: **$50 ka tier exist nahi karta** ($0/$20/$100/$200). $20 Plus +
  apni API key chal jaata. Par abhi ke liye: **NAHI.**

## Winner: browser-use cloud, DIRECT API — Claude Code khud orchestrator

n8n ki zaroorat hi nahi: main seedha REST API call karta hoon
(`POST /api/v2/tasks`, poll, Sheet update). Sab verified:

- **Profiles** = ek baar login → cookies saved → har agla task logged-in
  khulta hai (per-client profile)
- **Secrets kabhi LLM ko nahi dikhte** (placeholders + allowedDomains);
  **1Password vault integration (`opVaultId`)** — passwords vault se
  seedha browser-use tak, **Claude ke context mein kabhi nahi** (ye
  mandatory config hai, best practice bhi aur meri red line bhi)
- **Email-verify**: browser-use ka native inbox/Gmail integration poora
  loop khud karta hai — agency listings ke liye `agents@fameninja.com`
  scoped access UNKO do (mujhe nahi)
- **CAPTCHA aaya** → session ka `liveUrl` = shareable interactive link →
  team member ko WhatsApp/Telegram pe paste → 30-sec manual solve → agent
  resume. No bypass.
- **structuredOutput** JSON → main READY/NEEDS_HUMAN/FAILED seedha Dispatch
  mein likhta hoon
- **Cost: ~$8–12/month** for ~40 signup/login tasks ($0.01/task +
  $0.006/step + $0.02/browser-hr). **$15 free credit se pilot muft.**

⚠️ **Ek mandatory config**: Browser Use Cloud ke stealth browsers default
mein CAPTCHA-solving bundle karte hain — **wo OFF/avoid karna hai** (hamara
rule: CAPTCHA = human, hamesha). Unke bina bhi chhoti directories pe kaam
chalega; jahan CAPTCHA aaye wahan liveUrl-takeover.

## Boundaries (unchanged)

- Crunchbase/G2/IndiaMART-class: **100% human** (ToS, account-ban risk)
- Expect **2–4 of 10** sites pe phir bhi human assist (CAPTCHA/SMS)
- Claude kabhi passwords nahi dekhega/bhejega — vault→browser-use direct

## Pilot ladder (directly-use plan)

1. Ankush: cloud.browser-use.com account (Google login se $15 credit) +
   API key; 1Password vault mein 5 chhoti directories ke unique passwords;
   agents@ inbox (ya unka built-in inbox sirf test ke liye)
2. Claude: profile create → 5 smallest directories pe signup+login tasks
   (vault-referenced secrets, allowedDomains, structuredOutput) → Sheet
   statuses + success-rate report
3. Numbers dekh ke scale: profiles sab clients ke, READY rows pe main
   fill+submit — poora loop
4. Sirf agar self-host/always-on ki zid ho baad mein → Hermes gateway
   office machine pe revisit
