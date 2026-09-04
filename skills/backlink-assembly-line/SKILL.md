---
name: backlink-assembly-line
description: PARENT orchestrator for batch backlink production — create a dispatch (10 sites × client/product), route pack generation to the right child skill by category, notify the team to log in, fill + submit packs in the team's logged-in Chrome tabs, write live URLs + timing to the sheet backend, hand the batch to backlink-live-validator, and announce the next dispatch. Use when the user says "dispatch banao", "batch chalao", "assembly line", "aaj ka batch", or asks to run the backlink production loop.
---

# Backlink Assembly Line (parent skill)

Runs the batch loop: **dispatch → team login → Claude fill+submit → sheet
update → QA → next dispatch**. One batch = 10 sites (configurable) for one
client/product.

## Family (parent routes, children generate)

| Category (Site DB col N type) | Child skill | Status |
|---|---|---|
| citation / classified | `backlink-pack-generator` | LIVE |
| directory-listing / vendor-profile | `saas-listing-pack` | LIVE |
| infographic-submission | `infographic-backlink` | SKELETON — asset pipeline defined, sites research-seeded |
| doc-slide-submission | `ppt-pdf-backlink` | SKELETON — uses pptx/pdf skills |
| web2.0 / profile / social-bookmark | planned (`web20-post-pack`, `profile-backlink-pack`, `social-bookmark-pack`) | see docs/ROADMAP-skill-tree.md |
| video-submission | planned (`video-backlink`, Phase 2) | roadmap |
| QA (all types) | `backlink-live-validator` | LIVE |

Route by Site DB column N (`Backlink Type`). Asset-based children (infographic,
ppt-pdf, video) add one step before packs: Claude CREATES the asset, and the
FIRST asset per client needs Ankush's explicit approval before dispatch.

The child owns: site shortlist rules, dedupe source, pack fields, content.
The parent owns: batch lifecycle, execution in browser tabs, backend writes,
notifications, metrics, QA handoff.

## Red lines (inherited by every child — never relax)

- Claude NEVER: creates accounts, enters passwords/credentials, solves or
  bypasses CAPTCHA. Login/signup/OTP is always the team's step.
- Forbidden sheet zones (never read/write/quote): Tracker `D–E`, worksheet
  `H–I`, per-client tabs, `business listing sites` beyond column H.
- A batch go-ahead from the user covers exactly that batch's enumerated
  fill+submit actions (including category picks and a listing form's standard
  terms checkbox). Anything beyond — payment, phone verify, unexpected
  permissions, CAPTCHA at submit — pause that site, mark `BLOCKED`, report.
- Facts in packs come from the registry + the client/product's own website.
  Nothing invented, ever.

## Backend (sheet = state store)

**Control spreadsheet: `1JI7Flzgx0LP4-q75luh3s5IEFq1-7-2iqcG8N7S4Aiw`**
("Backlink Assembly Line — Control", ankush@fameninja Drive). Four tabs:

- **`Site DB`** — reusable site database, ALL clients/products (seeded with
  the citations inventory + the 203-site LP list). Columns: Site · URL ·
  Category · Bucket · DA · Spam % · **Auto Rating** · Login Type ·
  Submission URL · Proven Live · Last Used · Notes. Rating values:
  🟢 AUTO-FULL (login ke baad Claude 100% complete karta hai) ·
  🟡 PARTIAL/OTP/VERIFY/APPROVAL (Claude bharta hai, human finish/wait) ·
  🔴 PITCH-ONLY / HUMAN-POST / HUMAN-ONLY / LOW-DA · ⚪ UNTESTED.
  **After every batch, update the attempted sites' Auto Rating from what
  actually happened** — "(est)" hat jaata hai, real result likho + Last Used.
  New clients shortlist FROM this DB first — that's its whole point.
- **`Product Registry`** — one row per product (FameNinja seeded). The
  **Keywords column is team-editable and changes often** — read it fresh at
  every dispatch prep, never cache keywords from a previous batch.
- **`Dispatch`** — batch queue (schema below).
- **`Metrics`** — one row per batch (schema below).

**`Dispatch`** columns:

Batch# · Date · Client/Product · Category · Site · Submission URL · Status ·
Assigned to · Login done at · Submitted at · Live URL · Verdict · Notes

Status machine: `QUEUED → AWAITING_LOGIN → READY → SUBMITTED | BLOCKED |
PENDING_APPROVAL | AWAITING_EMAIL_VERIFY | OUTCOME_UNKNOWN → (validator)
VALIDATED`. `OUTCOME_UNKNOWN` (submit clicked, result unclear) is NEVER
blindly retried — check the site's account/dashboard, the public page, and
the inbox first; a duplicate listing is worse than a delayed one. Live URLs are ALSO written to the
category's normal data tab (Tracker / Daily work report) so
`backlink-live-validator` finds them without any changes.

**`Metrics`** tab, one row per batch: Batch# · Sites · Start · Login-done ·
End · Total min · Links/hour · Submitted · Blocked · Validated-SUCCESS %.
This answers "kitne time mein kitne backlinks".

## Team wizard (bare invocation)

When invoked with no arguments ("dispatch banao", `/backlink-assembly-line`),
run as a wizard — ask, don't assume:

1. **"Kis client/product ke liye?"** — options = rows of `Product Registry`
   (+ citation clients from `Target listing URL`). Unknown name → offer to
   add a registry row first.
2. **"Kaunsi category?"** — citations / saas-listing (route child by answer).
3. **"Kitne sites?"** — default 10.
4. Shortlist from **Site DB**: filter out sites already used for that
   client/product (Dispatch history + category data tabs), sort 🟢 first,
   then proven-live ⚪, then 🟡 (flagged); never 🔴 in an auto batch.
   **Also respect column M (G-Index)**: 🔴 NOT-INDEXED → exclude (Google
   us site ke pages hi nahi utha raha — link ka zero benefit); 🟠 THIN →
   bottom only; 🟢 ACTIVE ranks above 🟡 SLOW at equal rating. Re-run the
   check monthly ("index check chalao" → Apify site:/qdr:m queries →
   `Index Check` tab + column M refresh).
   **Show the proposed list with ratings and wait for "haan/go"** before
   writing Dispatch rows. The person can swap sites by name.
5. On confirm → continue at Batch lifecycle step 1 with those choices.

## Batch lifecycle

1. **Dispatch prep** — parse client/product + category + count (default 10).
   Route to the child skill → ranked shortlist + packs. Ask the user (or read
   the dispatch brief row) for anchor/keyword ONLY if the registry lacks it —
   never guess. Write `Dispatch` rows as `AWAITING_LOGIN`.
2. **Notify team** — send the numbered site list + submission URLs via
   Telegram (Composio, needs configured chat_id; fallback: print in chat for
   the user to forward). Message: "Batch #N — in sites pe login karke 'batch
   #N ready' bolo."
3. **Wait for "batch ready"** — the team confirms login (in chat, or the user
   relays). Mark `READY`, stamp Login-done-at.
4. **Fill + submit** — in the team's logged-in Chrome tabs (Claude-in-Chrome
   extension), one tab at a time. **Verification-first preflight**: before
   typing anything, open the form read-only and surface the earliest
   CAPTCHA/OTP/payment wall — walls found up front go to the human queue in
   one batch instead of interrupting mid-fill. **Idempotency check**: skip
   any site whose (root domain × client) already has a SUBMITTED/LIVE/
   PENDING row anywhere in Dispatch history. Then: paste pack fields, pick
   category, upload image, submit, copy the PUBLIC live/listing URL. Stamp
   Submitted-at per site. CAPTCHA/OTP/payment mid-flow → skip, mark
   `BLOCKED` with reason. Approval-queue sites → `PENDING_APPROVAL`; email
   confirmation pending → `AWAITING_EMAIL_VERIFY`; unclear result →
   `OUTCOME_UNKNOWN` (see status rules — never blind-retry).
5. **Sheet update** — Dispatch rows + the category's data tab (Live URL row).
   Append the `Metrics` row with timings.
6. **QA handoff** — run `backlink-live-validator` on the batch's live URLs
   (or queue it for the day's validator run). Verdicts land in the sheet.
7. **Next dispatch** — immediately prep batch #N+1 (step 1) and notify the
   team, so login work and Claude work pipeline in parallel.

## Site playbooks (per-site process memory)

Repo folder `playbooks/` (git-versioned, team-shared) — one file per root
domain: `playbooks/<domain>.md`, format in `playbooks/_TEMPLATE.md`.

- **Before filling a site**: read its playbook if it exists — follow the
  recorded steps/field order/quirks instead of re-discovering the form.
- **After every submit on a site** (success OR blocked): write/update its
  playbook — steps actually taken, field mapping (pack field → form field),
  category picker vocabulary, image requirements, where the live URL
  appears, approval delay, and what blocked (CAPTCHA at which step). Stamp
  `Last verified: <date> (<client>)`.
- Playbook exists → note `📖` in Site DB Notes; a playbook that failed on
  replay gets its broken step corrected, not deleted.
- Playbooks contain PROCESS only — never credentials, never client content.

## Reporting

After every batch, report in chat: submitted / blocked (with reasons) /
pending-approval counts, total time, links/hour, and the next batch number.
Weekly (on ask): totals per client, per category, validated-success rate from
the validator's verdict columns.
