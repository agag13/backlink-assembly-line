---
name: ppt-pdf-backlink
description: "CHILD of backlink-assembly-line — take a READY PPTX/PDF deck (made by Ankush's separate content skills), run intake checks (in-deck URL, size, formats), build per-site submission packs, and upload+submit to document/slide-sharing sites (SlideShare/Scribd/Calameo/FlipHTML5 class) in the team's logged-in tabs. Creation is NOT this skill's job — submission only (format conversion/10-page cuts allowed). Use when the user says \"ppt submit karo\", \"slide submission\", \"pdf submission\"."
---

# PPT / PDF Backlink (child skill)

Parent owns dispatch/lifecycle; red lines inherited. This child owns the deck
+ pack + doc-site rules.

## Pipeline

**DIVISION (Ankush's decision, Sep 4):** deck CREATION is skill ki jimmedari
NAHI — wo Ankush ki alag content skills se banta hai. Ye skill READY DECK
leti hai aur submission karti hai.

1. **Asset intake** — input: final deck (PPTX and/or PDF) + client + target
   URL. Intake checks (fail → creation wale ko wapas): 10–16 slides, deck ke
   ANDAR full https:// URL kisi slide pe (description links strip hote hain
   — in-deck URL survive karta hai), <20MB, fonts embedded. Zaroorat pe
   Claude format-conversion kar sakta hai (PPTX→PDF export, Issuu ke liye
   10-page cut) — ye packaging hai, creation nahi. Flipbook sites (Calameo/
   FlipHTML5 class) ke liye PDF version clickable hyperlinks ke saath ho.
2. **Pack** (per site): Title ≤70 chars · Description 100–200 words unique
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

## Blocked until (per dispatch)

- Ready deck (Ankush ki content skills se) jo intake checks pass kare
- Pehli baar per client: Ankush ka go
