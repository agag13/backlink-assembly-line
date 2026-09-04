# Evaluation: flaqai/backlink_skills (04-09-2026)

Repo: https://github.com/flaqai/backlink_skills · MIT · 665★/219 forks ·
created 17-08-2026 · by Flaq AI (flaq.ai — Singapore-registered AI-API
reseller, Chinese-operated)

## Verdict ek line mein

**Content asli aur achha hai, reputation manufactured hai.** Skills install
mat karo; patterns + list ka data le lo.

## Reputation (deep-checked)

- **Zero independent mentions**: HN, Reddit, Product Hunt, dev.to, YouTube,
  SEO forums, X — kahin bhi third-party discussion nahi. Indexed web se
  repo pe inbound links = 0. Sab first-party.
- **Star burst manufactured**: 665 mein se ~240 stars EK 20-hour window
  mein (19–20 Aug, China evening); 77% forks 48h ke andar; koi public
  launch source nahi mila — most likely WeChat/private Chinese channels
  blast (real developers, bot-farm nahi). 665★ pe sirf 4 watchers, 2
  issues = audience-grab, community nahi.
- **Author**: flaq.ai ka GitHub org ek content-marketing engine hai (25
  repos in 4.5 months, keyword-farmed "awesome prompts" repos; ye repo
  unka flagship). Repo khud unki link-building craft ka demo hai — 20
  translated READMEs, self-generated star chart, apni hi awesome-lists.
  Kisi bhi independent awesome-list (VoltAgent 33.7k★, Composio 16.2k★,
  Firecrawl) mein included NAHI hai.

## Content (padha, genuinely solid)

- Do submission skills (V1 batch / V2 quality) — engineering hamare se
  aage kai jagah: **16-state status model**, idempotency keys,
  evidence-vs-record separation, authorization matrix, audit script.
- Policy-aligned: explicit no-CAPTCHA-bypass, human verification queues,
  no invented facts, no fake metrics KPIs, nofollow-for-paid. (Contrast:
  backlink-pilot CAPTCHA-solver ship karta hai — red flag.)
- Codex skills, par SKILL.md format Claude Code se same standard —
  technically ~15 min mein portable. Portability ki zaroorat humein nahi.

## 743-site list (14 ka live spot-check)

- 12/14 alive, par heavily **AI-tool-directory flavored** (~153 AI/tool
  domains). SaaS/AI products ke liye ~30–40% genuinely valuable
  (awesomeindie, ctrlalt.cc, alternative.me, techpluto, saaspirate…);
  **doctors/academies ke liye sirf ~5–10%** eligible.
- 3 tiers: curated startup platforms ✅ · old-school general directories
  (jayde, linkcentre) 🟡 · pay-to-guarantee link farms
  (marketinginternetdirectory type) ❌ skip-by-default.
- Har entry dispatch se pehle liveness check maangti hai (silent decay).

## Hamare liye decision

| Karo | Mat karo |
|---|---|
| ✅ Patterns adopt: 16-state status model → Dispatch upgrade; V2 quality-gate checklist → site-selection reference | ❌ Skills verbatim install (hamari in-house skills se conflict + third-party instruction supply-chain risk) |
| ✅ List import as CANDIDATE data → Site DB `saas` category, ⚪ UNTESTED, source column "flaqai-743" | ❌ Stars ko trust signal maanna |
| ✅ Vendored pinned commit rakha hai (scratchpad clone; zaroorat pe repo mein `vendor/` kar sakte hain) | ❌ Upstream track karna (unka commit hamare agent ka behavior badal sakta hai) |

**Import math**: 340-dir DB + 150-dir CSV + is 743 list (dedupe ke baad)
→ Site DB ~600–900 unique sites ho jayega, teen sources ke saath.
