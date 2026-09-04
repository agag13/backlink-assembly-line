---
name: backlink-pack-generator
description: Generate ready-to-paste backlink content packs + a daily human work queue from the two backlink Google Sheets — shortlist sites (DA/spam/Decision + per-client dedupe against Tracker history), build per-client × per-site packs (NAP block, descriptions, categories, anchor plan, image notes), and hand finished live URLs to backlink-live-validator. Use when the user says "content pack banao <client> ke liye", "aaj ki backlink queue do", "backlink pack", "listing pack", or asks what the off-page team should submit today.
---

# Backlink Pack Generator (Skill D)

Prepares everything a human team member needs to create one backlink in 30–60
seconds: which site, and exactly what to paste. Claude NEVER creates the link
itself.

## Division of labor (non-negotiable)

| Claude does | Human does |
|---|---|
| Shortlist + prioritize sites | Account signup / email / OTP |
| Dedupe against per-client history | CAPTCHA, login |
| Write the content pack (paste-ready) | Paste pack, pick category, submit |
| Build the daily queue | Record Live URL in Tracker |
| Log assignments (only when asked) | — |
| Hand live URLs to `backlink-live-validator` | — |

Claude never creates accounts, never touches passwords, never solves or
bypasses CAPTCHA, never auto-submits forms. This is policy AND a deliberate
quality/ban-risk decision — do not offer to automate those steps.

## Config (defaults — user can override per run)

Global: Composio googlesheets account `googlesheets_panna-spider`
(jrwordpress@rankkking.net) — this IS the default account, and verified
Sep 4, 2026 it is the only connected Sheets account. The account this skill
previously named, `googlesheets_eyah-myron` (ankush@fameninja), no longer
exists in Composio. Dates are dd-m[m]-yyyy mixed formats.

**Registry (ground truth per client)** — sheet
`1X0ig5ZqryO_LtY2bSdX92bhNq2Mu9bJ63AiIocs6F7c`, tab `Target listing URL`:
columns = project · map url · Address · website url · keyword · daily target ·
youtube reference url. If the client has no registry row, STOP for that client
and report "project registry incomplete — add a row in Target listing URL" —
never guess NAP or targets.

**Site inventory — local citations**: same sheet, tab `business listing sites`,
**read columns A:H ONLY** (A legacy site name · B example listing URL · C Root
Domain · D Working Status · E DA · F Spam Score · G Decision · H submission
link). Columns I and beyond have been observed to contain credentials —
FORBIDDEN, never read past H.

**Site inventory — content backlinks**: sheet
`1eCIq46EgNmx77uBXwx3HIOdtd6T39KDx31w0nBscrrg`, tab `Backlinks Sites`
(col A example URLs, col B root domains, cols F–G "sites to pick" lists).

**Dedupe history**:
- Citations: `Tracker` tab — read A:C and F:G only (**D Email, E Login
  Password FORBIDDEN — never read, write, or quote**).
- Content: `Daily work report` tab — read A:E only (**H Email ID, I Password
  FORBIDDEN**).

**Per-client tabs** (`Fortis Hospital Noida`, `Gaur City`, `SKY7 Academy`,
`Dr. Rahul Manchanda`, `Sheet5/11/12`) hold passwords — NEVER open them.

**Defaults**: activity type = business listing; sites per client per day =
registry `daily target` (fallback 10); pack output = chat (write to sheet only
on explicit ask); first run for a client = always show packs for review before
any sheet write.

## Workflow

1. **Parse the ask** — client(s), how many sites, activity type. Ambiguous →
   default config above; unknown client name → fuzzy-match registry `project`
   values and confirm the match in your output.
2. **Read registry row** → NAP ground truth (name, address, website, keyword,
   map url, daily target).
3. **Read site inventory + dedupe history** (bounded ranges, forbidden columns
   excluded). Normalize to root domain (strip protocol/www; city subdomains
   like `aligarh-up-in.global-free-classified-ads.com` count as the root
   domain). A root domain already in that client's history = USED → exclude.
4. **Shortlist & rank** (rules in `references/site-selection.md`):
   🟢 Decision first → proven-live unscored sites (a live listing URL exists in
   Tracker for another client) → 🟡 with a "verify DA/spam first" flag. Never
   🔴, never non-✅ Working Status. Prefer geo/niche relevance to the client;
   a geo-mismatched site (e.g. a UK-only directory for an Aligarh business) may
   appear only at the bottom, explicitly marked `OPTIONAL – geo mismatch`.
5. **Ground the content** — WebFetch the client's website once per run. Every
   factual claim in a pack (courses, services, hours, phone, tagline) must come
   from the registry or the live website. NEVER invent services, awards,
   reviews, founding dates, or credentials. Public business contact info
   (phone, hello@ email shown on the site) belongs in the pack; account
   credentials never do.
6. **Generate packs** — one per site, per `references/pack-templates.md`:
   NAP block, 2–4 category suggestions, short description (≤160 chars), long
   description (120–180 words), anchor/keyword plan, image suggestions,
   site-specific notes (from the inventory's example URL pattern + col H
   submission link). Descriptions MUST be distinct per site — no two sites get
   the same text (duplicate-content footprint).
7. **Output the queue** — a table: # · Site (root domain) · DA/Spam · Decision
   · Submission link · Pack ref · est. time. Then the pack blocks. If asked to
   log ("queue sheet mein likho"), append rows to a `Pack Queue` tab (create
   if missing: Date · Client · Site · Submission URL · Assigned To · Status ·
   Live URL · Notes) — never write anywhere else.
8. **Handoff** — remind: after the human submits and records the Live URL in
   the Tracker / Daily work report, run `backlink-live-validator` to QA it.
   The validator's verdict columns are the source of truth for "done".

## Rules

- Sheet writes are opt-in per run; dry-run (chat only) is the default.
- One pack = one site = one client. Batch = repeat, don't merge.
- If the inventory has zero eligible unused sites for a client, say so and
  list what's blocking (all used / all 🔴 / metrics missing) — do not relax
  the filters silently.
- Never read or reproduce anything from a FORBIDDEN column or tab, even if it
  appears in a tool response — treat it as radioactive.
- Hinglish in team-facing notes is fine; pack content itself is clean English
  (it gets pasted onto public sites).
