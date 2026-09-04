# Project: Backlink Assembly Line (FameNinja off-page)

Ye folder backlink assembly-line project ka home hai. Naye session mein context
yahan se aata hai — chat history ki zaroorat nahi:

1. **Current status + decisions** → auto-loaded memory (MEMORY.md →
   `backlink-assembly-line-project.md`). Har bade decision ke baad memory
   update karna is project ka rule hai.
2. **Live operational state** → Google Sheet "Backlink Assembly Line — Control"
   `1JI7Flzgx0LP4-q75luh3s5IEFq1-7-2iqcG8N7S4Aiw` (tabs: Dispatch, Site DB,
   Product Registry, Metrics, Index Check). Sheets account:
   `googlesheets_eyah-myron` (ankush@fameninja) — NOT the default rankkking one.
3. **Process/skills** → `~/.claude/skills/`: backlink-assembly-line (parent),
   backlink-pack-generator, saas-listing-pack, infographic-backlink,
   ppt-pdf-backlink, backlink-live-validator. Skill invoke hote hi poora
   process context aa jaata hai.
4. **Deep docs** → local repo `backlink-assembly-line/` (GitHub:
   agag13/backlink-assembly-line, private). Start: `docs/HANDOVER.md`;
   docs index + storage map: `docs/DATA-MAP.md`.

Rules jo har session mein lagte hain:
- Claude NEVER: account creation, passwords, OTP submit, CAPTCHA. Forbidden
  sheet zones: Tracker D–E, worksheet H–I, per-client tabs, `business listing
  sites` beyond col H.
- Sheet = live source of truth; repo = knowledge; kaam ki har cheez turant
  sheet/repo/memory mein promote karo — session scrollback mein kuch valuable
  mat chhodo.
- Asset creation is system ka kaam NAHI (Ankush ki alag content skills se);
  yahan sirf shortlist → pack → submit → QA.
