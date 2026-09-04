---
name: competitor-link-gap
description: "ANALYSIS child of backlink-assembly-line — find domains where a client's competitors have backlinks but we don't (via Apify Ahrefs-stats actors), rank by authority (OpenPageRank), filter toxic domains, check Tier-1/2 citation-directory coverage, and feed the top gaps into dispatch suggestions so batches are data-driven instead of guesswork. Use when the user says \"gap analysis chalao <client>\", \"competitor backlinks dekho\", or before planning a client's next batches."
---

# Competitor Link Gap (analysis child — no submissions)

Read-only analysis; output = ranked gap list + Site DB/dispatch suggestions.
Red lines inherited (never touch Email/Password columns; verdict columns
read-only).

## Inputs

1. **Competitor domains** — Product Registry column O `Competitor Domains`
   (comma-separated, 2–3 per client). Missing → Ankush se EK BAAR poochho,
   registry mein store karo. Kabhi guess mat karo.
2. **Our live links** (SUCCESS only):
   - Content sheet `1eCIq46EgNmx77uBXwx3HIOdtd6T39KDx31w0nBscrrg`
     `Daily work report`: col E live URL, sirf rows jahan col G = SUCCESS
   - Citations sheet `1X0ig5ZqryO_LtY2bSdX92bhNq2Mu9bJ63AiIocs6F7c`
     `Tracker`: col F live URL, sirf rows jahan col I = SUCCESS
   - Normalize to root domains.

## Pipeline

1. **Competitor backlink pull** (Apify, account `apify_pitman-betsey`):
   - Default: `maximedupre~ahrefs-free-website-stats-scraper`
     (~$0.0018/domain, mode: linking-website-focused) — linking websites list.
   - Deeper (zaroorat pe, Ankush bole to): `memo23~ahrefs-scraper`
     ($0.01/row — full backlink rows + anchors). Caveat: ye actor Ahrefs ke
     public tools scrape karta hai (apna Turnstile-handling karta hai) —
     third-party vendor risk, batch chhota rakho.
2. **Gap** = (competitor linking domains) − (our SUCCESS domains) − (already
   QUEUED/SUBMITTED in Dispatch for this client).
3. **Rank** by OpenPageRank score (free API, key env `OPR_API_KEY`; key nahi
   → rank skip karke note karo, list alphabetical + frequency-ranked
   (kitne competitors se link hai) de do).
4. **Toxic filter** — central QA sheet `1AU_sykyWYAD8chcqfMI6OHs5rNJgBgQmIJpTt8lpo84`
   ke `Domains` tab mein Toxic=RED wale hatao. (Tab abhi exist nahi karta —
   jab tak nahi hai, skip + note; validator project isse banayega.)
5. **Citation coverage** (citation clients ke liye) — Tier-1/2 list from
   `backlink-check` repo: `backlink-live-validator/references/citation-directories.md`
   (43 dirs, tiered; local copy validator skill mein). Client ki missing
   Tier-1/2 directories = dispatch suggestions ke SABSE UPAR.
6. **Output**:
   - Report: top ~20 gap domains (score, kaunse competitors, hamari
     coverage %) + missing Tier-1/2 list.
   - Site DB: gap domains jo DB mein already hain → Notes mein
     `gap:<client>` tag; naye domains → ⚪ UNTESTED rows with
     `src:gap-analysis` (submission-route research pehli dispatch pe hoga).
   - Dispatch suggestions: parent wizard in tagged domains ko G-Index +
     Auto-Rating rules ke saath top pe rakhta hai.

## Cost guardrail

Per client per run: ~3 competitors × $0.0018 ≈ $0.01 (maximedupre) —
negligible. memo23 deep pull sirf explicit ask pe (est. batao pehle).
Monthly refresh kaafi hai; har dispatch pe re-run mat karo.
