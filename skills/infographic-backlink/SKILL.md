---
name: infographic-backlink
description: "CHILD of backlink-assembly-line — take a READY infographic (made by Ankush's separate content skills), run intake checks, build per-site submission packs (title, unique descriptions, sources line, embed code), and submit to infographic/visual-content sites in the team's logged-in tabs. Creation is NOT this skill's job — submission only. Use when the user says \"infographic submit karo\", \"infographic backlink\", or dispatches an infographic-submission batch."
---

# Infographic Backlink (child skill)

Parent (`backlink-assembly-line`) owns dispatch/lifecycle; red lines inherited
(no signup/password/CAPTCHA; team logs in). This child owns: the infographic
itself + the submission pack + type-specific site rules.

## Pipeline

**DIVISION (Ankush's decision, Sep 4):** infographic CREATION is jimmedari is
skill ki NAHI hai — wo Ankush ki alag content-creation skills se banta hai
(ya team deti hai). Ye skill READY ASSET leti hai aur distribution/submission
karti hai.

1. **Asset intake** — input: final infographic PNG (ya uska file/link) +
   client + target URL. Intake checks (fail → wapas bhejo, submit mat karo):
   portrait ~800×2000–4000px, <1.5MB, footer mein client logo + URL +
   cited sources, thumbnail pe readable. Derivative crops missing hon
   (Pinterest 735×1102, OG 1200×630) to Claude crop kar sakta hai — ye
   resize hai, creation nahi.
2. **Canonical first** — confirm the infographic client ki apni site pe
   embed-code box ke saath live hai; directories usi canonical page ko
   target karti hain. Nahi hai → pehle wo (team/Ankush), phir dispatch.
3. **Pack** (per site):
   - Title (≤70 chars, keyword natural) · Description 150–300 words UNIQUE
     per site · Tags · Source-attribution line · **Embed code** block
     (`<a href="client-url"><img src="..." alt="..."></a> Courtesy: <client>`)
     · client URL as the credit link
4. **Approval gate** — pehla infographic per client Ankush ko dikhana
   (SendUserFile PNG), "go" ke baad hi dispatch. Baad ke batches auto.
5. **Submit** — parent ka normal flow (verification-first preflight, team
   login, fill+upload+submit, live URL → Dispatch + data tab).
6. **QA** — validator Gate 3 checklist for infographic type: image loads
   logged-out, credit link present + correct target, description intact.

## Site rules

- Sites come from Site DB `Backlink Type = infographic-submission` (seeded
  from research — DA/alive/process columns respected; 🔴 NOT-INDEXED never).
- Email-pitch-only sites (editor ko mail karna ho) → pack + draft email
  banega, SEND team karegi apne mail se.
- Reddit/Pinterest-type: Claude asset + caption draft dega, POST team karegi
  apni ID se (community rule, parent se inherited).
- Paid-placement sites default skip; Ankush explicitly bole to hi.

## Blocked until (per dispatch)

- Ready infographic PNG (Ankush ki content skills se) jo intake checks pass kare
- Canonical page client ki site pe live (embed-code box ke saath)
- Pehli baar per client: Ankush ka go
