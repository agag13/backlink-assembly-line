# Site selection & ranking rules

## Eligibility (hard filters)

1. Working Status must be ✅ (or the domain has a proven-live listing URL in
   Tracker col F for any client). Anything marked timed-out/dead → skip.
2. Decision 🔴 → never. Missing Working Status AND no proven-live evidence →
   skip (long-tail rows with only a name in col A are candidates only after
   someone verifies them).
3. Root domain already used for THIS client (Tracker cols B/C+G history, or
   Daily work report for content links) → exclude. City/language subdomains
   collapse to the root domain.
4. Spam Score > 9% → exclude (team's stated 10% limit; 🟡 "near limit" rows
   rank last).

## Ranking (within eligible)

Score each site, sort descending:

| Signal | Points |
|---|---|
| Decision 🟢 "STRONG – USE" | +40 |
| Decision 🟢 "USE" / "USE / secondary" | +30 |
| Proven live (a real listing URL for another client exists in Tracker) | +25 |
| DA ≥ 40 | +20 · DA 25–39 → +10 · DA < 15 → −20 |
| Spam ≤ 2% | +10 |
| Geo/niche relevance to client (India-wide or client's region/industry) | +15 |
| Geo mismatch (UK/UAE/USA/Canada-only directory for an India-local client) | −25 and label `OPTIONAL – geo mismatch` |
| Decision 🟡 (hold / verify first) | −10 and label `verify DA/spam first` |
| Metrics self-reported or starred (`*`) | −5 |

Ties: prefer the site the team has completed fastest before (proven-live for
more clients = smoother signup flow).

## Relevance notes per known client type

- Medical (doctors, hospitals): health/medical categories exist on generic
  directories; justdial-style India directories rank up.
- Education/training (academies): "Education", "Training Centre", "Coaching"
  categories; India-wide + city directories rank up.
- Real estate / local business: city-specific and classifieds directories.

## Output honesty

- Show DA/Spam/Decision exactly as the sheet has them ("—" stays "—").
- If a shortlist slot is filled by a 🟡 or geo-mismatch site because nothing
  better is unused, say that in the queue row — the human decides.
