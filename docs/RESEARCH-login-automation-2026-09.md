# Login-Automation Research — Sep 2026 (dependency kam karne ka plan)

5-agent research, vendor docs se verify (04-09-2026). Sawal: kya koi aur
LLM/agent signup/login karke humein "READY" handoff de sakta hai, ~$100/mo?

## Grok bot — seedha jawab: NAHI (by design)

Grok Bot (xAI, beta Aug-26, SuperGrok $30/mo mein bundled) persistent cloud
computer hai, par **xAI ne khud design kiya hai ki password, passkey, 2FA,
CAPTCHA, payment — sab pe wo human ko control HAND KAR DETA hai** (remote
screen pe aap type karte ho). Matlab: human hatata nahi, sirf human ka kaam
Grok ki screen pe shift hota hai — upar se ek shared cloud computer mein
saare logins, koi Sheet-handoff API nahi, beta reliability, datacenter-IP
ban risk. **Is kaam ke liye nahi hai.** (xAI ka developer Agents API bhi
nahi — wo search/code/MCP hai, browser-login kar hi nahi sakta.)

## Hermes bot — technically HAAN, par DIY power tool

"Hermes bot" = **Nous Research Hermes Agent** (open-source MIT, Feb-26;
self-hosted daemon/desktop). Ye poora signup→verify→login loop ATTEMPT kar
sakta hai (accessibility-tree browsing, form fill, apne Chrome profile ke
logins inherit karna), software free + Nous Portal $20–100/mo credits —
budget mein fit. **Par**: koi success guarantee nahi, kisi technical bande
ko install/configure/per-site-debug karna padega, aur chhoti directories pe
achhi-khaasi failures expect karo. (Sirf "Hermes model" = bina haath ka
dimaag — browser nahi chala sakta.)

## Jo genuinely ye kaam karte hain (ranked)

| Tool | Login/verify capability | $100 mein | Verdict |
|---|---|---|---|
| **Skyvern** | Best-in-class: write-only credential vault, TOTP auto, **email/SMS verification code API se push** (hamara system agency inbox padh ke code POST kare) | Cloud 2FA-tier $149 😕 → **self-host free** (+$20–60 LLM/VPS) ya Hobby $29 (verify human) | **#1 pick** |
| **browser-use cloud** | Login + signup; **native Gmail integration verification codes padhti hai**; domain-scoped credential placeholders (LLM values kabhi nahi dekhta) | True pay-as-you-go — 10-site batch = kuch dollars | **#2 / budget pick** |
| **Airtop** | Login + profiles; **Live View**: CAPTCHA aaye to team member usi browser mein 30-sec assist kare | $89/mo Professional | Best human-in-loop UX |
| Browserbase + Stagehand | DIY scripts + persistent contexts — stable 10-site list pe sabse repeatable | $20–99/mo | Build-not-buy (main scripts likh sakta hoon) |
| MS Copilot Studio | **Ekmatra big-lab jo stored-credentials login officially bless karta hai** (Azure Key Vault) | ~$0.05–0.15/step credits | Enterprise-flavored option |
| Anchor Browser | Credential-security pick | $50/mo+ | Agar dar "startup ke DB mein password" hai |
| Hyperbrowser | stealth/CAPTCHA-positioning — galat fit | — | ❌ skip |

## Risk reality (honest numbers)

- **Email-verify** directories pe near-universal hai — inbox-access wale
  agent se automatable ✅. **CAPTCHA/SMS** unmeasured-but-meaningful minority
  — **human hi rahega** (hum bypass nahi karte/karwate): expect **2–4 of 10
  sites pe ab bhi human assist**.
- **ToS**: Crunchbase, G2, IndiaMART ke ToS automated access explicitly
  prohibit karte hain (primary pages se verify); pakde gaye to account
  termination — IndiaMART pe permanent re-enrollment ban. **In big platforms
  pe signup+login 100% HUMAN hi rakho.** Chhoti directories pe worst case =
  listing reject — wahan automation OK.
- Anthropic/OpenAI/Google policies bhi bot-prohibiting sites pe automated
  account-creation ke against hain — isliye **SIGNUP step pe human
  watch/approval rakho** (Airtop Live View jaisa), automation ka sweet spot
  = login/session-refresh + email-confirm-link + form-fill.
- **Credentials**: vault mein (1Password/Bitwarden — Browserbase ke saath
  "agentic autofill" hai jisme LLM password kabhi nahi dekhta), har site ka
  unique password, `agents+site@` aliases. Prompt mein password KABHI nahi.
  Aur mujhe (Claude) kabhi nahi.

## Recommended architecture ($100/mo ke andar, sab verified)

```
Sheet (Dispatch): AWAITING_LOGIN
  → n8n (self-host free / €24 cloud): PENDING row uthao → agent trigger
  → Agent (browser-use PAYG ya self-hosted Skyvern): login/signup attempt
      - email code: agents@fameninja inbox se
      - TOTP: vault se auto
  → webhook wapas n8n → Sheet:
      ✅ READY            → Claude Code fill+submit karta hai (hamara flow)
      🙋 NEEDS_HUMAN      → team ko live-view URL (30-sec CAPTCHA assist)
      ❌ FAILED           → human queue, purana tarika
```
Cost: n8n $0 + browser-use ~$10–30 actual usage (ya Skyvern self-host
~$20–60) = **$100 ke andar aaraam se.** Hamara status machine already
compatible hai (AWAITING_LOGIN → READY).

## Meri (Claude) red lines — unchanged

Main khud credentials/OTP/CAPTCHA handle nahi karunga; passwords mujhe
kabhi mat dena — wo agent-platform ke vault mein rahenge. Mera kaam READY
ke BAAD shuru hota hai (fill → submit → sheet → QA). Realistic net gain:
human ka per-site kaam signup+login se ghat kar sirf CAPTCHA-assists +
big-platform logins reh jayega — dependency ~60–80% kam.

## Pilot plan (jab bologe)

1. `agents@fameninja.com` inbox + vault setup (team)
2. browser-use cloud pe $15 free credit se 5 chhoti directories
   (freelistingindia-class) ka login+verify pilot — success rate KHUD napo,
   vendor benchmarks pe bharosa nahi
3. n8n spine + Sheet statuses wire karo
4. Numbers achhe → Skyvern self-host evaluate for scale
