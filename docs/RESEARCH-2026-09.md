# Upgrade Research — Sep 2026

17-agent research run (Playwright vs extension · agent email · market repos ·
playbook patterns). Har repo ki activity/stars 04-09-2026 ko verify hui hai.

## 1. Playwright vs Chrome extension — verdict: HYBRID (do lanes)

**Playwright kya ADD karta hai (extension nahi kar sakta):**
1. **Login-once persistent auth** — human ek baar login kare, session
   (storageState/persistent profile) file mein save; baad mein headless,
   kisi bhi machine pe, baar-baar reuse. Roz ka login khatam.
2. **True parallelism** — 5–10 sites ek saath fill (isolated contexts),
   abhi ek tab ek waqt.
3. **Codegen replay** — site ka flow ek baar record → deterministic script
   → har agle client pe near-zero-token replay (sirf naya NAP variable).
4. **Official Claude Code integration** — `microsoft/playwright-mcp`
   (36.8k★, v0.0.80 Sep 2026) ya `@playwright/cli` (13.1k★).

**Extension kahan BEHTAR rahega:** G2/Crunchbase class sites — DataDome/
Akamai/Cloudflare bot-detection (G2 = 9/10 difficulty) automated browsers ko
pakadti hai; human ka REAL Chrome profile (asli fingerprint/cookies/history)
sabse safe hai. Plus instant human OTP/CAPTCHA handoff.

**Recommended architecture — Site DB mein `Lane` tier:**
- **Lane A (extension)**: protected/high-value sites (G2, Crunchbase,
  Trustpilot, Justdial) — abhi wala flow, human ke real Chrome mein.
- **Lane B (Playwright)**: chhoti directories ka long tail — per-site
  codegen script + per-client storageState + Patchright (4.3k★, undetected
  fork, upstream ke saath lockstep) touchy sites ke liye; markdown playbook
  fallback jab script toote.
- **Bridge option**: Playwright MCP ka `--extension` mode (Chrome Web Store
  ~100k users) — Playwright tooling human ke REAL logged-in Chrome ke andar.
  Lane A ko bhi scriptable banata hai. Pilot-worthy.

## 2. Agent email — verdict: agents@fameninja.com (apna domain)

Deciding factor = **domain reputation**: temp-mail/disposable domains
directory sites ki blocklists (e.g. disposable-email-domains list) mein hain
— REJECT. Apne domain pe inbox best:

| Option | Kya hai | Cost | Verdict |
|---|---|---|---|
| **Google Workspace user `agents@fameninja.com`** + plus-addressing (`agents+justdial@`) | Team+AI shared inbox; Gmail toolkit (Composio — already connected) se AI READ-ONLY padhe | ~$7/mo | ✅ RECOMMENDED — fastest |
| **AgentMail** (YC S25, $6M seed) | Agent-native inboxes on custom subdomain, webhooks + MCP | free → $20/mo | 🟡 pilot alongside |
| MailSlurp / SendGrid Inbound / Postmark | programmable inboxes | pricier/DIY | backup |
| Temp-mail APIs | disposable | — | ❌ listings years tak verifiable rehni chahiye |

**Policy line (unchanged):** account creation, password, OTP-SUBMIT human ke
paas hi. AI inbox PADH ke code/link team ko surface karega. Ek exception
research ne confirm ki: **plain "confirm your email" links** idempotent hote
hain (corporate scanners bhi click karte hain) — wo AI safely khol sakta
hai; **magic-login links** OTP-equivalent hain → human only.

## 3. Site playbooks — hamara design validated + upgrades

Poora industry same pattern pe converge hua: **pehla run mehenga (agent) →
artifact save → replay deterministic (3–5x speed, ~70–80% cost saving) →
page badle to agent-mode se self-heal.** Research (Agent Workflow Memory,
ICML 2025): natural-language procedural memory se hi success +24.6%/+51.1%
(Mind2Web/WebArena). Hamara `playbooks/<domain>.md` design sahi hai; do
upgrades adopt kiye:
- Field-mapping table mein **selector hints** column (accelerator, hard
  dependency nahi — live page ke against validate karo).
- **2 consecutive failures → playbook STALE flag → full agent-mode rewrite.**
- Top ~10 highest-volume sites baad mein Playwright scripts mein graduate
  hongi (markdown fallback rehta hai).

## 4. Verified repos/tools (04-09-2026)

### Adopt (recommend=true)
| Repo | Stars/Status | Kyon |
|---|---|---|
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | 36.8k★, v0.0.80 Sep-26 | Lane B + `--extension` bridge; `browser_fill_form` built-in |
| [@playwright/cli](https://playwright.dev/docs/getting-started-cli) | 13.1k★, v0.1.19 | token-efficient CLI, `--persistent`, state-save/load |
| [Skyvern](https://github.com/Skyvern-AI/skyvern) | 22.9k★, commits Sep-26 | form-fill benchmark leader; CDP-attach to logged-in Chrome; parameterized saved Workflows (AGPL note) |
| [Stagehand](https://github.com/browserbase/stagehand) | 24.1k★, MIT | act/observe + cached replay + self-heal; CDP attach (Chrome ko `--remote-debugging-port` se kholna padega) |
| [Patchright](https://github.com/Kaliiiiiiiiii-Vinyzu/patchright) | 4.3k★, lockstep releases | undetected fork for touchy Lane-B sites (stealth claims decay hoti hain — monitor) |
| [agent-browser](https://github.com/vercel-labs/agent-browser) (Vercel) | 42k★ | CLI, `--auto-connect` to logged-in Chrome — Bash se drive hota hai, near-zero integration |
| Playwright codegen + actionability | core, 95.6k★ | record-once → parameterized per-site scripts |

### Pattern/data grabs (adopt ideas, not tool)
- [s87343472/backlink-pilot](https://github.com/s87343472/backlink-pilot) — 259-site `targets.yaml`, per-site form adapters, "scout" field-discovery, rate limiting — hamara hi idea open-source mein
- [Fh-Ndiritu/list-my-startup-skill](https://github.com/Fh-Ndiritu/list-my-startup-skill) — same human-auth/AI-fills split, Do/Refresh/Skip registry, resumable batch tracker
- [whatsuppiyush/backlink-claude-skill](https://github.com/whatsuppiyush/backlink-claude-skill) — **340-directory DB (DR/dofollow)** → Site DB mein import karo
- [nyyhao/saascity-launch-kit](https://github.com/nyyhao/saascity-launch-kit) — 150-directory CSV → import
- [gmickel/sheets-cli](https://github.com/gmickel/sheets-cli) — update-by-key + atomic batch writes for Sheets
- [SawyerHood/dev-browser](https://github.com/SawyerHood/dev-browser) — "learned scripts" per site pattern
- [vercel-labs/skills](https://github.com/vercel-labs/skills) — `npx skills` se internal skills distribute karo
- **Already installed, under-used:** `marketing-skills:directory-submissions` (13-tier taxonomy + readiness gate) aur `claude-seo` suite (`seo-local` NAP audit = citation QA layer)
- Papers: Agent Workflow Memory (CMU, ICML 2025), Memp (procedural memory lifecycle)

### Avoid
- **browser-use** (112k★ but redundant — apna alag LLM loop + API spend, playbook persistence solve nahi karta; ideas borrow karo)
- **workflow-use** (pre-production, broken recorder, apna browser launch karta hai — human session bypass, AGPL; JSON-playbook+fallback PATTERN copy karo)
- **LaVague** (dead Jan-25), **lmnr-ai/index** (archived), playwright-extra stealth (dead), Healenium (wrong stack), temp-mail APIs

## 5. Phased upgrade plan

1. **Ab (done)**: extension lane + markdown playbooks + selector-hint columns + stale-flag rule
2. **Agla hafta**: 340-dir + 150-dir lists Site DB mein import; `directory-submissions` skill ka taxonomy/readiness-gate reuse; `agents@fameninja.com` Workspace user banao (team banaye — AI nahi)
3. **Pilot**: Playwright MCP `--extension` bridge Lane-A pe + 5 🟢 sites Lane-B pe (codegen + storageState + Patchright)
4. **Scale**: top-10 playbooks → deterministic scripts; Metrics mein lane-wise links/hour compare
