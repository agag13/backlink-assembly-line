# Backlink Assembly Line

FameNinja off-page team ka batch backlink system. **Claude sochta hai, aap
submit karte ho** — Claude kabhi account nahi banata, password nahi bharta,
CAPTCHA solve nahi karta.

**📘 Poori documentation (naye member ko yahi do): [`docs/HANDOVER.md`](docs/HANDOVER.md)**
Process diagram: `docs/assembly-line-diagram.html` (browser mein kholo) ·
Team 1-pager: `docs/backlink-team-workflow.md`

## Ye "script" kaise chalti hai

Ye traditional script nahi hai jo terminal se `python run.py` hoti hai —
ye **Claude Code skills** hain. Skill = Claude ke liye likha hua SOP jo
Google Sheets padhta/likhta hai aur browser chalata hai. Repo ka kaam:
version control + har team member ke machine pe same skills install karna.

```
skills/
├── backlink-assembly-line/   ← PARENT: batch wizard + lifecycle + metrics
├── backlink-pack-generator/  ← child: citations/listings ke packs
├── saas-listing-pack/        ← child: SaaS/product directories ke packs
└── backlink-live-validator/  ← QA: har live URL logged-out check
```

Backend (state store): Google Sheet **"Backlink Assembly Line — Control"**
(`1JI7Flzgx0LP4-q75luh3s5IEFq1-7-2iqcG8N7S4Aiw`) — tabs: `Dispatch` (batch
queue), `Site DB` (236+ sites, auto-ratings), `Product Registry` (clients/
products + editable keywords), `Metrics` (kitne time mein kitne links).

## One-time setup (har team member, ~10 min)

1. **Claude Code install** karo (desktop app ya CLI) aur login.
2. **Ye repo clone karke skills install** karo. Repo **private** hai — pehle
   Ankush se `agag13` pe collaborator access lo, phir git authenticate karo
   (bina auth clone `Authentication failed` deta hai):
   ```bash
   gh auth login          # ek baar, browser se
   git clone https://github.com/agag13/backlink-assembly-line.git
   cd backlink-assembly-line && ./install.sh
   ```
3. **Sheets access**: Ankush se Control sheet + client sheets apne Google
   account pe share karwao, aur Claude Code mein Google Sheets connection
   (Composio/MCP) **usi account** se jodo — jis email pe sheet share nahi hai
   uska connection `403 PERMISSION_DENIED` deta hai aur parent skill chalta
   nahi. Sheet IDs ki poori list: `docs/HANDOVER.md` §4 step 3.
4. **Claude Chrome extension** install karo (batch submit isi se hota hai).

## Roz ka flow (5 steps)

1. **Batch banao** — Claude Code mein bolo: `dispatch banao`
   Claude wizard poochega: kis client ke liye? → kaunsi category
   (citations/saas)? → kitne sites (default 10)? Phir **Site DB se best
   unused sites ki list dikhayega ratings ke saath** — "go" bolo to batch
   Dispatch tab mein likh dega + packs de dega.
2. **Login karo** — batch ke 10 sites Chrome mein kholo, signup/OTP/CAPTCHA
   khud karo. Email/password sirf sheet ke designated columns mein.
3. **"Batch #N ready" bolo** — Claude tumhare logged-in tabs mein packs
   fill + submit karega, live URLs Dispatch + data tab mein likhega,
   Metrics update karega. Jahan CAPTCHA/payment aayega wo BLOCKED mark
   karke tumhe batayega (tum 10-sec mein finish kar dena).
4. **QA** — `backlink validator chalao` (ya Ankush ka daily run) — har link
   logged-out verify hota hai, verdict sheet mein.
5. **Agla batch** — Claude khud next dispatch propose karega. Loop.

## Rules (non-negotiable)

- 🟢/🟡/🔴 rating Site DB mein har batch ke baad update hoti hai — ratings
  se hi pata hai kaunsi site 100% auto hai.
- Fake reviews kabhi nahi (Trustpilot/Sitejabber/G2 pe sirf profile).
- Communities (Reddit/HN/LinkedIn) pe Claude sirf DRAFT dega — post team
  apni ID se apni voice mein karegi.
- Descriptions me facts sirf client ki website/registry se — kuch invent
  nahi karna, na karne dena.

## Skills update karne ke liye

Skill edit karo → `./install.sh` dobara → commit + push. Sab members
`git pull && ./install.sh` se sync ho jayenge.
