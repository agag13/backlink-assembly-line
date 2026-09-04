# Backlink Assembly Line — Team Handover Documentation

> Ye ek hi file poore system ki documentation hai. Naye team member ko sirf
> ye repo do — ye file padh ke wo kaam shuru kar sakta hai.
> Process ka picture: `docs/assembly-line-diagram.html` browser mein kholo.

---

## 1. Ye system kya hai (30 second mein)

Hum backlinks (business listings, citations, SaaS/product directory listings)
**batches mein** banate hain. Kaam ka batwara fix hai:

| Claude karta hai | Aap (human) karte ho |
|---|---|
| Sites choose karna (DB se, ratings ke saath) | Account signup, email/OTP verify |
| Ready-to-paste content pack banana | CAPTCHA, login |
| Logged-in tabs mein form fill + submit | Jahan Claude atke wahan finish karna |
| Sheet mein live URL + time likhna | Live URL verify karna |
| QA (validator) + metrics | Passwords sheet ke apne columns mein rakhna |

**Claude KABHI nahi karega:** account banana, password bharna, CAPTCHA solve
karna, fake review likhna. Ye policy bhi hai aur quality/ban-risk decision
bhi — isko bypass karne ki koshish mat karna.

---

## 2. System ke hisse (architecture)

```
Claude Code (aapke laptop pe)
│
├── skills/backlink-assembly-line   ← PARENT: wizard, batch lifecycle, metrics
│     ├── skills/backlink-pack-generator   ← citations/listings ke packs
│     ├── skills/saas-listing-pack         ← SaaS/product directories ke packs
│     └── skills/backlink-live-validator   ← QA: live URL verify + verdict
│
└── Google Sheets (backend / memory)
      ├── "Backlink Assembly Line — Control"  ← MAIN sheet (neeche section 3)
      ├── "GMB Profile Sheet" (citations data: Tracker, Target listing URL)
      └── "komal work sheet" (content backlinks: Daily work report)
```

Skill = Claude ke liye likha hua SOP. Repo in skills ka source of truth hai;
`install.sh` unhe `~/.claude/skills/` mein copy karta hai.

---

## 3. Control Sheet — full reference

Sheet: **"Backlink Assembly Line — Control"**
ID: `1JI7Flzgx0LP4-q75luh3s5IEFq1-7-2iqcG8N7S4Aiw`

> ⚠️ **Ye sheet ankush@fameninja ke Drive mein hai.** Jo Google account aapne
> Claude Code ke Sheets connection (Composio) mein joda hai, **usi email pe ye
> sheet share honi chahiye** — warna Claude ko `403 PERMISSION_DENIED` milta
> hai aur poora parent skill (`dispatch banao`, Site DB, Product Registry,
> Metrics) chalta hi nahi. 04-09-2026 pe verify kiya:
> `jrwordpress@rankkking.net` (is machine ka ek hi connected Sheets account)
> ke paas access **nahi** hai. Fix: ya to sheet us email pe share karo, ya
> ankush@fameninja ko Composio mein dusre Sheets account ki tarah jodo.

### Tab 1: `Dispatch` (batch queue — system ka heartbeat)

| Column | Kya hai | Kaun bharta hai |
|---|---|---|
| Batch# | batch number (1, 2, 3…) | Claude |
| Date | dd-mm-yyyy | Claude |
| Client/Product | e.g. FameNinja, SKY7 Academy | Claude |
| Category | citations / saas-listing | Claude |
| Site | site ka naam | Claude |
| Submission URL | kahan login/submit karna hai | Claude |
| **Status** | neeche ki state machine | Claude (aap bhi kar sakte ho) |
| Assigned To | team member ka naam | Ankush/Claude |
| Login Done At | kab login complete hua | Claude ("batch ready" pe) |
| Submitted At | kab submit hua | Claude |
| Live URL | PUBLIC listing URL (dashboard nahi!) | Claude |
| Verdict | validator ka result | Validator |
| Time (sec) | us site pe laga time | Claude |
| Notes | warnings, reasons | Claude |

**Status values (state machine):**
`QUEUED` → `AWAITING_LOGIN` (aapki baari) → `READY` (login ho gaya) →
`SUBMITTED` ya `BLOCKED` (CAPTCHA/payment/OTP atka — aap finish karo) ya
`PENDING_APPROVAL` (site approve karegi, wait) → `VALIDATED` (QA pass).

### Tab 2: `Site DB` (236+ sites — reusable database, SABSE valuable cheez)

Har site ki permanent knowledge. Naya client aaye to shortlist YAHIN se banti
hai — isliye isko sahi rakhna sabki zimmedari hai.

> ⚠️ **Known seam (04-09-2026) — abhi ye poora sach nahi hai.** LIVE citations
> child `backlink-pack-generator` Site DB **padhta hi nahi**; wo shortlist GMB
> sheet ke `business listing sites` tab aur komal sheet ke `Backlinks Sites`
> tab se banata hai (DA/Spam/Decision columns, Auto Rating nahi). Parent skill
> bhi apne aap se ulta bolta hai — `SKILL.md` line 20: "the child owns site
> shortlist rules, dedupe source", line 51: "New clients shortlist FROM this DB
> first". **Batch #1 se pehle Ankush decide kare: ya Site DB single source
> banega (child ko wahan point karo), ya Site DB sirf ratings/history store
> rahega (to ye section aur §5/§7 ka wording badlo).** Jab tak decide nahi
> hota, citations ke liye asli shortlist source wo do tabs hain.

| Column | Kya hai |
|---|---|
| Site / URL | site |
| Category | citations / saas |
| Bucket | business-listing, launch-platform, review-site, startup-directory, tech-media, community, india, design-dev, classified |
| DA / Spam % | Moz metrics (jahan pata hai) |
| **Auto Rating** | neeche ki legend — har batch ke baad UPDATE hoti hai |
| Login Type | email account / login-first / OTP |
| Submission URL | direct add-listing link |
| Proven Live | kya kabhi real live listing bani hai (YES) |
| Last Used | aakhri baar kab use hui |
| Notes | quirks (geo, approval delay, etc.) |

**Auto Rating legend:**
- 🟢 `AUTO-FULL` — login ke baad Claude 100% complete kar deta hai
- 🟡 `PARTIAL / OTP / VERIFY / APPROVAL` — Claude bharta hai, aap finish karte ho ya approval ka wait hota hai
- 🔴 `PITCH-ONLY` (media sites — listing nahi, PR pitch) / `HUMAN-POST` (communities — Claude draft dega, post AAP karoge) / `HUMAN-ONLY` / `LOW-DA`
- ⚪ `UNTESTED` — abhi try nahi hui
- "(est)" = estimate hai; pehli real batch ke baad Claude isko real result se badal deta hai

### Site Playbooks (repo ka `playbooks/` folder)

Ek baar jis site pe form bhara, Claude uska process `playbooks/<domain>.md`
mein save karta hai (steps, field mapping, quirks, live URL kahan milta hai).
Agli baar wahi playbook padh ke seedha bharta hai — na re-discovery, na
galti repeat. Har submit ke baad update + `Last verified` stamp hota hai,
aur `git pull` se ek member ka seekha process poori team ko milta hai.
Rule: playbook mein PROCESS only — credentials/client content kabhi nahi.

**Status:** abhi `playbooks/` mein sirf `README.md` + `_TEMPLATE.md` hain, koi
site playbook nahi (kyunki pehla batch submit nahi hua). Pehla submit hi pehla
playbook banayega — us se pehle "pichhli baar ka process" padhne ko kuch nahi
hai, ye normal hai.

### Tab 3: `Product Registry` (clients/products ka ground truth)

Har product/client ki ek row: naam, website, tagline, category, **Keywords
(editable — jab chahe badlo, Claude har dispatch pe fresh padhta hai)**,
descriptions ka source, phone, public email, address/NAP, pricing, logo link.
`[TEAM FILL]` dikhe to wo value bharna aapka kaam hai — Claude guess NAHI
karega, wo us site ko skip kar dega.

Citations clients ka NAP purani jagah hi hai: GMB sheet → `Target listing
URL` tab. Naya citation client = wahan row add karo.

### Tab 4: `Metrics` (kitne time mein kitne backlinks)

Har batch ki ek row: sites, start/login/end time, total minutes, **links/hour**,
submitted/blocked/pending counts, validated success %. Ankush isi se
throughput dekhte hain — ise manually mat chhedo, Claude bharta hai.

### 🚫 Forbidden zones (kabhi mat todna, Claude bhi nahi todta)

- GMB sheet `Tracker` columns **D–E** (Email/Password) — sirf aap use karo
- komal worksheet columns **H–I** (Email/Password) — sirf aap
- Per-client tabs (SKY7 Academy, Fortis, etc.) — passwords hain, Claude kabhi nahi kholta
- `business listing sites` tab column **I ke aage** — wahan credentials mile the; Claude sirf A–H padhta hai. **Behtar: credentials wahan se hata do**

---

## 4. Setup (naya team member, ~10 min)

1. Claude Code install + login (desktop app ya CLI)
2. **GitHub access** — ye repo **private** hai. Ankush aapko `agag13` ke
   collaborator ki tarah add karega. Uske baad git ko authenticate karna
   zaroori hai (`gh auth login`, ya SSH key, ya PAT) — bina auth `git clone`
   `Invalid username or token` / `Authentication failed` deta hai:
   ```bash
   gh auth login          # ek baar, browser se
   git clone https://github.com/agag13/backlink-assembly-line.git
   cd backlink-assembly-line && ./install.sh
   ```
   SSH pasand ho to: `git clone git@github.com:agag13/backlink-assembly-line.git`
3. **Sheets access** — Ankush se ye chaar sheets apne Google account pe share
   karwao, aur **wahi account** Claude Code ke Google Sheets connection
   (Composio) mein jodo:
   - Control `1JI7Flzgx0LP4-q75luh3s5IEFq1-7-2iqcG8N7S4Aiw` (parent skill)
   - GMB Profile Sheet `1X0ig5ZqryO_LtY2bSdX92bhNq2Mu9bJ63AiIocs6F7c` (citations)
   - komal work sheet `1eCIq46EgNmx77uBXwx3HIOdtd6T39KDx31w0nBscrrg` (content)
   - Backlink QA Results `1AU_sykyWYAD8chcqfMI6OHs5rNJgBgQmIJpTt8lpo84` (validator log)
4. Claude Chrome extension install karo
5. Test: Claude Code mein `dispatch banao` bolo — wizard chale to setup done.
   `403 PERMISSION_DENIED` aaye to step 3 adhoora hai (§3 ka warning padho).

---

## 5. Roz ka kaam (detailed runbook)

### Step 1 — Batch banao
Claude Code mein: **`dispatch banao`**
Claude poochega: kis client ke liye? → category? → kitne sites (default 10)?
Phir Site DB se best unused sites dikhayega (🟢 pehle, ratings ke saath) —
citations category mein filhaal shortlist `business listing sites` /
`Backlinks Sites` tab se aati hai, §3 Tab 2 ka "known seam" note dekho.
List theek hai to **"go"** bolo; koi site badalni ho to naam lo ("Justdial
hata ke Sulekha daal do"). Confirm hote hi Dispatch tab mein rows + packs
mil jayenge.

### Step 2 — Login (aapka kaam)
Batch ke sites Chrome mein kholo. Signup/verify/OTP/CAPTCHA sab khud.
Email + password **sirf sheet ke designated columns mein** likho (section 3
ke forbidden zones dekho — wahi columns aapke hain).

### Step 3 — "Batch #N ready" bolo
Claude tumhare logged-in tabs mein ek-ek karke: pack paste → category select
→ image upload → submit → **public live URL** copy → sheet update. Jahan
CAPTCHA/payment/OTP aa gaya, wo site `BLOCKED` hogi Notes ke saath — tum us
tab pe jaake 10-second mein finish kar do aur live URL Claude ko de do (ya
khud column K mein daal do).

### Step 4 — QA
**`backlink validator chalao`** — har live URL logged-out check hota hai
(404? link laga? content complete? address hai? indexed?). Verdict + reason
sheet mein aata hai:
- `SUCCESS` = done ✅
- `404_NOT_FOUND` / `LOGIN_WALL` = link public nahi hai — fix karo
- `TARGET_URL_MISSING` = page hai par hamara link nahi laga
- `CONTENT_INCOMPLETE` = form ke fields adhoore the — poora karke resubmit
- `ADDRESS_MISSING` = listing mein NAP nahi aaya
- Index status (Google/Bing) info hai, fail nahi — naye links 1–2 hafte lete hain

### Step 5 — Loop
Claude khud agla batch propose karega. Din ke end pe Metrics row check karo —
wahi aapka scoreboard hai.

---

## 6. Rules (short list, poster bana lo)

1. Ek site ek client ke liye ek hi baar.
2. Facts sirf client ki website/registry se — kuch invent nahi.
3. Fake reviews KABHI nahi — review sites pe sirf company profile.
4. Communities (Reddit/HN/LinkedIn) pe Claude sirf draft dega; post aap
   apni ID se, apni bhasha mein karoge.
5. Media sites (TechCrunch, Inc42 type) = listing nahi, PR pitch — wo alag
   process hai (Ankush se poocho).
6. Password kisi chat/message mein kabhi nahi — sirf sheet ke apne columns.
7. Site weird lage (paid demand, malware, adult ads) — skip + Claude ko
   batao, wo Site DB mein note karega.
8. Public listing URL hi sheet mein jaata hai — dashboard/settings URL QA
   mein fail hota hai.

---

## 7. Naya client/product kaise add hota hai

1. `Product Registry` mein row bharo (SaaS/product) — ya citations ke liye
   GMB sheet ke `Target listing URL` mein (project, map url, Address,
   website, keyword, daily target).
2. Bas. Agla `dispatch banao` bolo — Claude Site DB se us client ke liye
   fresh shortlist bana dega (jo sites us client pe use ho chuki hain wo
   khud filter ho jayengi). **Yahi Site DB ka fayda hai: har naya client
   pichle saare experience ka reference free mein paata hai.**

---

## 8. FAQ / Troubleshooting

**Q: Claude bola "registry incomplete", pack nahi bana raha.**
Registry mein us client ki row nahi hai ya `[TEAM FILL]` khaali hai. Bhar
do, dobara bolo. (Claude guess karke galat NAP nahi daalega — by design.)

**Q: Keywords change karne hain.**
`Product Registry` → Keywords column edit karo. Bas. Agli dispatch se naye
keywords use honge.

**Q: Site `PENDING_APPROVAL` mein atki hai.**
Normal hai (G2, Crunchbase type). Validator baad mein check karta rahega.
Kuch karna nahi hai.

**Q: Claude ne site `BLOCKED` kari.**
Notes padho — CAPTCHA/OTP/payment hoga. Tab kholo, finish karo, live URL
column K mein daalo, status `SUBMITTED` kar do.

**Q: `install.sh` ke baad bhi skill nahi chal rahi.**
Claude Code ka naya session kholo. Phir bhi nahi to `ls ~/.claude/skills/`
mein check karo ki ye **4 backlink folders** hain: `backlink-assembly-line`,
`backlink-pack-generator`, `saas-listing-pack`, `backlink-live-validator`.
(Us folder mein doosre unrelated skills bhi ho sakte hain — total count
maayne nahi rakhta, ye 4 naam maayne rakhte hain.)

**Q: Claude bolta hai `403 PERMISSION_DENIED` / "caller does not have permission".**
Sheet aapke connected Google account pe share nahi hai. §4 step 3 ki list
dekho, Ankush se wahi email pe share karwao. Dhyaan: **Composio mein jo
account default hai wahi use hota hai** — agar aapke do Google accounts jude
hain to sheet usi pe share honi chahiye jise skill naam se maangta hai.

**Q: Composio account ID badal gaya (`googlesheets_...` / `serpapi_...`).**
Skills apne `## Config` section mein account ID naam se likhte hain. Connection
hata/dobara juda to ID badal jaati hai aur skill first run pe fail hoti hai.
Naya ID nikaalo (Claude se bolo "list my googlesheets connections") → repo mein
skill ka Config update karo → `./install.sh` → push. **04-09-2026 pe aisa hua
tha:** `googlesheets_eyah-myron` aur `serpapi_moony-chaja` dono khatam ho gaye
the; ab `googlesheets_panna-spider` + `serpapi_kohl-bon` hain.

**Q: Skills mein change karna hai.**
Repo mein edit karo → `./install.sh` → commit + push. Baaki sab
`git pull && ./install.sh`. Seedha `~/.claude/skills/` mein edit mat karo —
`install.sh` pehle `rm -rf` karta hai, to wo edit agle install pe udd jaayega.
**Agar kabhi majboori mein local fix kiya** (jaise dead account ID), to usko
turant repo mein bhi daalo aur push karo — warna baaki team ke paas woh fix
nahi jaata aur unki skill tooti rehti hai.

---

## 9. Abhi ka status (04-09-2026 handover ke waqt)

**Ankush ke setup pe (fameninja account):**

- ✅ Control sheet live, Site DB 236 sites seeded, FameNinja registry row ready
- ✅ **Batch #1 queued (FameNinja, saas-listing):** Crunchbase, Wellfound,
  F6S, Clutch, G2, Serchen, Sitejabber, Trustpilot, IndiaMART, Justdial —
  status `AWAITING_LOGIN`, packs bane hue hain
- ⏳ Pending: FameNinja ka public email + exact address + logo link registry
  mein (`[TEAM FILL]`) — iske bina Justdial/IndiaMART nahi honge
- ⏳ Pending: Telegram group ID (notifications ke liye; abhi chat mein milta hai)
- SKY7 Academy ke 5 citation packs bhi pehle se bane hain (Ankush ke paas)

**Dusre machine pe verify kiya (04-09-2026, `jrwordpress@rankkking.net`):**

| Cheez | Haal |
|---|---|
| Control sheet `1JI7Flz…` | ❌ `403 PERMISSION_DENIED` — share nahi hai. Isliye Site DB / Batch #1 / registry ki upar wali lines **is machine se verify nahi ho saktin** (galat nahi — sirf padhi nahi ja saktin), aur parent skill chal nahi sakta |
| GMB Profile Sheet | ✅ `Tracker`, `Target listing URL`, `business listing sites` + per-client tabs (Fortis Hospital Noida, Gaur City, SKY7 Academy, Dr. Rahul Manchanda) — §3 ke forbidden zones sach hain |
| komal work sheet | ✅ `Daily work report`, `Backlinks Sites`, `Keywords` |
| Backlink QA Results `1AU_syky…` | ✅ `Sheet1` ke columns validator ke run-log se exactly match, write bhi kaam karta hai |
| Validator (Step 4) | ✅ **do real run log ho chuke:** content 247 rows → 64 SUCCESS (51%), citations 166 rows → 45 SUCCESS (42%), Fortis:LDC = 14:0 |
| `Domains` tab (DA/DR enrichment) | ⏳ abhi nahi bana — pehli enrichment run ise banayegi |

Matlab: **QA half live hai, production (parent) half sirf Ankush ke account pe
chalta hai.** Kisi bhi naye member ka pehla kaam §4 step 3 (sheet sharing) hai.

## 10. Commands cheat-sheet

| Bolo | Hota hai |
|---|---|
| `dispatch banao` | wizard → naya batch + packs |
| `batch #N ready` | Claude fill+submit shuru karta hai |
| `backlink validator chalao` | QA run, verdicts sheet mein |
| `content pack banao <client> ke liye <site>` | ek site ka fresh pack |
| `metrics dikhao` | ab tak ka scoreboard |
| `<site> ki rating update karo` | Site DB correction |
