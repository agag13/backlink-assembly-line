---
name: saas-listing-pack
description: "CHILD of backlink-assembly-line — content packs for SaaS/product directory listings (launch platforms, review sites, startup directories, India-specific dirs from the rankkking free-listing-sites list). Use when the user says \"saas listing pack\", \"product listing banao\", or dispatches a SaaS-category batch. STATUS: skeleton — needs the website list + a product registry row before first run."
---

# SaaS Listing Pack (child skill — SKELETON)

Generates ready-to-paste packs for listing a SaaS/product/company on
directories. Parent (`backlink-assembly-line`) owns execution; red lines
inherited from the parent apply.

## BLOCKED UNTIL (ask Ankush, don't guess)

1. **Website list** — Ankush's curated list (source of categories:
   https://lp.rankkking.com/free-listing-sites/ — 200+ sites in 8 buckets:
   Launch Platforms, SaaS Review Sites, Startup Directories, Tech Media,
   Communities, India-Specific, Business Listings, Design & Dev). Need the
   sheet/tab where this inventory + per-site status will live.
2. **Product registry** — one row per product (like `Target listing URL` for
   citations): product name · tagline (≤60 chars) · website · category ·
   short + long description source · pricing model · logo/screenshot assets ·
   maker/company info · launch date · support email (public).

## Site categories → pack shape

| Bucket | Extra fields beyond the base pack |
|---|---|
| Launch platforms (Product Hunt, BetaList…) | tagline, first-comment/maker note, gallery images, launch date |
| Review sites (G2, Capterra, SaaSHub…) | feature list, pricing tiers, alternatives-to/competitors, category taxonomy per site |
| Startup directories (F6S, Crunchbase…) | founding year, team size, funding stage, HQ location |
| India-specific (Inc42, IndiaMART, Justdial…) | NAP block, India pricing (₹), GST-friendly business name |
| Communities (Reddit, IndieHackers…) | NOT form-fill — needs a written post; generate as draft for HUMAN to post in their own voice. Never auto-post to communities. |

Base pack = product name · tagline · short desc (≤160) · long desc
(120–200 words, unique per site) · categories/tags · website URL · logo +
screenshots note · maker info · site-specific notes.

## Rules (in addition to parent red lines)

- Review sites: NEVER write or solicit fake reviews; we list the product,
  reviews come from real users only.
- Tech media / blogs bucket = pitches, not listings — route the user to the
  newsjack/PR skills instead of generating a "pack".
- Descriptions unique per site (same rotation rules as
  `backlink-pack-generator` references/pack-templates.md).
- Dedupe: one product listed once per site; track in the SaaS inventory tab.
