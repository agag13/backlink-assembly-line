# Data snapshots

**Source of truth = Google Sheet** ("Backlink Assembly Line — Control"):
https://docs.google.com/spreadsheets/d/1JI7Flzgx0LP4-q75luh3s5IEFq1-7-2iqcG8N7S4Aiw/edit

Ye folder sirf versioned BACKUP rakhta hai — live kaam hamesha sheet mein
hota hai (ratings, Last Used, dispatch sab wahan update hote hain).

- `site-db-snapshot.csv` — Site DB tab ka export (last: 04-09-2026,
  817 sites: 33 citations + 203 LP-list + 581 flaqai-743 import; column M =
  G-Index verdict from the 04-09 Google indexing check — details sheet ke
  `Index Check` tab mein).

Refresh karne ke liye Claude se bolo: "Site DB snapshot update karo" —
wo sheet se fresh export karke isi file ko overwrite karega.
Passwords/credentials is folder mein kabhi nahi aate (Site DB mein hote
hi nahi).
