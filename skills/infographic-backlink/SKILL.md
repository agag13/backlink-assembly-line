---
name: infographic-backlink
description: "CHILD of backlink-assembly-line — create a complete infographic (design + PNG) for a client/product from verified facts, build the submission pack (title, description, sources, embed code), and submit to infographic/visual-content sites in the team's logged-in tabs. Use when the user says \"infographic backlink banao\", \"infographic pack\", or dispatches an infographic-submission batch. STATUS: sites being researched — first run needs Ankush's asset approval."
---

# Infographic Backlink (child skill)

Parent (`backlink-assembly-line`) owns dispatch/lifecycle; red lines inherited
(no signup/password/CAPTCHA; team logs in). This child owns: the infographic
itself + the submission pack + type-specific site rules.

## Pipeline

1. **Data collection** — facts ONLY from: Product Registry row, the client's
   live website (fetch fresh), and any stats source Ankush/team provides in
   the dispatch brief. Har number ke saath source. NEVER invent statistics —
   agar 5 solid data points nahi milte, infographic mat banao; bolo kya
   chahiye.
2. **Design** — HTML/SVG artboard → PNG export:
   - Portrait 800×2000px (±, site specs se adjust), brand colors from
     registry (logo link wahin hai), readable at thumbnail size
   - Structure: hook title → 4-7 data blocks → takeaway → footer with client
     logo + URL + "Sources:" list
   - Use the diagram/design toolchain (HTML/SVG + headless render to PNG);
     har site ke liye SAME image, alag description (dup-content rule
     descriptions pe lagta hai, image pe nahi)
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

## Blocked until (per client)

- Registry mein logo + brand colors link
- 5+ verified data points (client site se ya Ankush-provided source)
- Pehli baar: Ankush ka design approve
