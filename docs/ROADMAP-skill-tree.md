# Skill Tree — Backlink Assembly Line ka poora plan

> Principle har type ke liye SAME hai: **research → asset/pack Claude banata
> hai → team login → Claude fill+submit → sheet + metrics → validator QA.**
> Har child sirf apne type ka expert hai; parent dispatch/loop chalata hai.

```
backlink-assembly-line (PARENT — dispatch, lifecycle, metrics, notify)
│
├── ✅ LIVE
│   ├── backlink-pack-generator      → citations · business listings · classifieds
│   ├── saas-listing-pack            → SaaS/product/startup directories
│   └── backlink-live-validator      → QA (sab types; checklists per type)
│
├── 🔜 TEXT-BASED (sites zyada tar Site DB mein already hain)
│   ├── profile-backlink-pack        → author/company profiles (about-pages,
│   │                                  dev/design profiles — Behance/Dribbble type)
│   ├── web20-post-pack              → WordPress.com/Blogger/Tumblr/Telegraph pe
│   │                                  450–700 word useful mini-articles (Claude
│   │                                  likhega, per-platform suspension rules ke saath)
│   └── social-bookmark-pack         → bookmarking sites (inventory mein hain)
│
├── 🆕 ASSET-BASED (Claude ASSET bhi banayega — yahi naya frontier hai)
│   ├── infographic-backlink         → Claude: data collect (client site/registry se)
│   │                                  → HTML/SVG design → PNG export → title/desc/
│   │                                  embed-code pack → team login → submit
│   ├── ppt-pdf-backlink             → Claude: PPTX/PDF deck (pptx + pdf skills
│   │                                  se) → SlideShare/Scribd/Issuu/FlipHTML5
│   │                                  type sites pe upload+submit
│   └── video-backlink (PHASE 2)     → 60–120s slideshow MP4 (images + TTS
│                                      voiceover + captions, ffmpeg) → YouTube/
│                                      Vimeo/Dailymotion — research pending
│
└── 🔁 DISCOVERY & MAINTENANCE
    ├── index check (monthly)        → "index check chalao" — G-Index refresh
    └── site-discovery routine       → scheduled agent jo naye high-quality
                                       sites dhoondta rahe (proposal neeche)
```

## Backlink Type taxonomy (Site DB column N — LIVE)

| Type | Site DB mein abhi | Kaun banayega |
|---|---|---|
| citation | 38 | backlink-pack-generator ✅ |
| directory-listing | 378 | saas-listing-pack ✅ |
| vendor-profile (G2/Capterra class) | 29 | saas-listing-pack ✅ |
| classified | 1 (+ sheet-1 inventory) | backlink-pack-generator ✅ |
| social-bookmark | 2 (+ sheet-1 inventory) | social-bookmark-pack 🔜 |
| web2.0 / community-post | 109 | web20-post-pack 🔜 (Claude draft, HUMAN post on communities) |
| profile | 13 | profile-backlink-pack 🔜 |
| media-pitch | 33 | PR/newsjack skills (alag process) |
| infographic-submission | 0 → research chal rahi hai | infographic-backlink 🆕 |
| doc-slide-submission | 0 → research chal rahi hai | ppt-pdf-backlink 🆕 |
| video-submission | 0 → research chal rahi hai | video-backlink (Phase 2) |
| ? (unmapped) | 214 | pehli baar use hone pe classify |

## Asset-based flow (infographic example — sab pe same pattern)

1. **Data**: registry + client website se real facts/stats (invent kabhi nahi;
   stats chahiye to Ankush/team source dega)
2. **Create**: Claude infographic design karta hai (HTML/SVG → PNG, brand
   colors, 800×2000-ish portrait) + 150–300 word description + sources +
   embed code
3. **Review gate**: pehla asset har client ka Ankush approve kare, uske baad
   batch mode
4. **Dispatch**: normal batch — team login → Claude upload + submit → live URL
   → validator QA (content checklist mein "image loads + embed + attribution")

## Site-discovery routine (proposal — Ankush ki haan chahiye)

Monthly scheduled cloud agent (Claude routine):
- Har type ke liye naye candidate sites dhoondhe (search + competitor
  backlink patterns), liveness + index check kare, Site DB mein ⚪ UNTESTED
  add kare, aur ek summary bheje.
- Saath mein G-Index refresh (index check) + DEAD cleanup.
- Setup: `/schedule` se cron routine — Ankush approve karega tab.

## Priority order (jo pehle banega)

1. **infographic-backlink** — skeleton ban gaya, sites ki research aaj ki
2. **ppt-pdf-backlink** — skeleton ban gaya (pptx/pdf skills ready hain)
3. **web20-post-pack** — text-only, sasta, jaldi
4. profile + social-bookmark packs — inventory ready
5. video-backlink — Phase 2 (TTS + ffmpeg pipeline test ke baad)
