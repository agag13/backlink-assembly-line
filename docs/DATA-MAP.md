# Data Map — kya kahan save hota hai (aur kyun)

> Ek line mein: **roz ka LIVE kaam = Google Sheet · knowledge/process/docs =
> GitHub · Claude ki apni yaaddasht = memory folder · temporary processing =
> scratchpad (disposable).**

## 1. Google Sheet — "Backlink Assembly Line — Control" (LIVE STATE)

https://docs.google.com/spreadsheets/d/1JI7Flzgx0LP4-q75luh3s5IEFq1-7-2iqcG8N7S4Aiw/edit

Jo cheez har ghante badalti hai, wo yahan. Team yahi dekhti/edit karti hai.

| Tab | Kya rakhta hai | Kaun likhta hai |
|---|---|---|
| `Dispatch` | har batch ki live progress (status, live URLs, timing) | Claude (team bhi kar sakti hai) |
| `Site DB` | 857 sites: ratings, DA/spam, G-Index, Backlink Type | Claude (imports, checks, batch results) |
| `Product Registry` | clients/products + editable Keywords + NAP | Team/Ankush bharta hai, Claude padhta hai |
| `Metrics` | per-batch throughput (links/hour, success%) | Claude |
| `Index Check` | Google indexing audit ka detail | Claude (monthly re-run) |

Client sheets alag hain (GMB sheet ka `Tracker`, worksheet ka `Daily work
report`) — live URLs wahan bhi jaate hain taaki validator apni jagah kaam
karta rahe. Password columns Claude kabhi touch nahi karta.

## 2. GitHub repo — `agag13/backlink-assembly-line` (KNOWLEDGE, versioned)

Jo cheez SEEKHI gayi hai ya PROCESS hai, wo yahan — git history ke saath,
taaki har change ka record rahe aur team `git pull` se sync ho.

```
skills/          ← system ka DIMAAG: 6 skills (parent + 4 children + validator)
docs/            ← saari documentation (list neeche)
playbooks/       ← per-site process memory (har submit ke baad badhti hai)
data/            ← Site DB ka CSV snapshot (backup; source of truth sheet hai)
install.sh       ← team machines pe skills install karne ka ek-command tarika
```

### Documentation index (docs/)

| File | Kya hai |
|---|---|
| `HANDOVER.md` | **MAIN DOC** — naye member ko yahi do: system, tabs, statuses, runbook, FAQ |
| `ROADMAP-skill-tree.md` | poora skill tree: kya live, kya banna hai, kis order mein |
| `DATA-MAP.md` | ye file — kya kahan save hota hai |
| `backlink-team-workflow.md` | 1-page daily workflow (Hinglish) |
| `assembly-line-diagram.html` | process ka visual diagram |
| `RESEARCH-2026-09.md` | Playwright/agent-email/repos upgrade research |
| `RESEARCH-backlink-types-2026-09.md` | infographic/PPT/video/web2.0 sites + asset specs |
| `EVAL-flaqai-backlink-skills.md` | third-party skill evaluation (patterns adopted) |

Har SKILL.md khud apni documentation hai — "skill kya kar sakti hai" ka
authoritative jawab `skills/<name>/SKILL.md` mein hai; docs usko summarize
karte hain.

## 3. Claude ki memory (`~/.claude/projects/.../memory/`)

Claude ka apna project-notebook — sessions ke beech continuity: kya decide
hua, kya pending hai, kya seekha. Ye AAPKE liye document nahi hai (wo
docs/ hai) — ye Claude ke liye hai taaki naya session purani baat na bhoole.
Har bade decision ke baad Claude ise khud update karta hai.

## 4. Team machines (`~/.claude/skills/`)

Repo se `./install.sh` chala ke skills ki COPY yahan aati hai — runtime.
Source of truth repo hai; seedha yahan edit mat karo (pull pe overwrite).

## 5. Temporary (koi bharosa mat rakho)

- Session scratchpad + Composio remote workbench (`/mnt/files`) — parsing,
  batch API calls, intermediate files. Kaam ki cheez yahan NAHI chhodte —
  jo valuable hai wo turant sheet ya repo mein promote hota hai.

## Ek information ka safar (example)

naya site mila (research) → `Site DB` row (sheet) + research doc (repo docs/)
→ batch mein use hua → `Dispatch` + `Metrics` (sheet) → process seekha →
`playbooks/<domain>.md` (repo) → live URL → client data tab → validator
verdict (sheet) → mahine mein ek baar snapshot → `data/` (repo backup)
→ decision/learning → Claude memory + docs.
