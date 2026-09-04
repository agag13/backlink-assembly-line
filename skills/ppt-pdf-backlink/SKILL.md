---
name: ppt-pdf-backlink
description: "CHILD of backlink-assembly-line — create a complete PPTX/PDF deck for a client/product (via the pptx/pdf skills) from verified facts, build the submission pack (title, description, tags), and upload+submit to document/slide-sharing sites (SlideShare/Scribd/Issuu/FlipHTML5 class) in the team's logged-in tabs. Use when the user says \"ppt backlink banao\", \"slide submission\", \"pdf submission pack\". STATUS: sites being researched."
---

# PPT / PDF Backlink (child skill)

Parent owns dispatch/lifecycle; red lines inherited. This child owns the deck
+ pack + doc-site rules.

## Pipeline

1. **Content** — 8–12 slide deck from Registry + client website facts (same
   no-invention rule). Deck angle per client type: doctor → patient-education
   ("10 baatein jo <topic> ke baare mein jaanni chahiye"), academy → career/
   skills guide, SaaS/agency → how-to ya checklist. Ek deck = ek topic,
   genuinely useful — brochure nahi.
2. **Build** — `pptx` skill se PPTX (brand colors/logo from registry) + `pdf`
   version. Last slide = client intro + URL + contact. Slide 2 ya footer mein
   naked URL (kai sites description links strip karti hain — deck ke ANDAR ka
   URL survive karta hai).
3. **Pack** (per site): Title ≤70 chars · Description 100–200 words unique
   per site · Tags/category · Language · License (public).
4. **Approval gate** — pehla deck per client Ankush approve kare
   (SendUserFile), phir batch mode.
5. **Submit** — parent flow; file upload logged-in tab mein. `PENDING_APPROVAL`
   common hai in sites pe.
6. **QA** — validator: doc publicly opens logged-out (CRITICAL — kuch sites
   login-gate karti hain, wo verdict LOGIN_WALL), URL slide readable, title/
   desc intact.

## Site rules

- Sites from Site DB `Backlink Type = doc-slide-submission` (research-seeded).
- FlipHTML5 team already use karti hai (proven-live) — pehla pilot wahin.
- Same deck har site pe OK; descriptions unique. Ek client ka ek topic ek hi
  baar per site.

## Blocked until (per client)

- Registry: logo/brand link
- Topic ka enough real material (client site se) — warna Ankush se topic/
  points maango
- Pehli baar: Ankush ka deck approve
