# Backlink Assembly Line — Team Workflow (1 pager)

**Kaun kya karta hai:** Claude sochta hai, aap submit karte ho. Claude kabhi
account nahi banayega, password nahi bharega, CAPTCHA solve nahi karega —
woh aapka kaam hai (isi liye quality high aur ban-risk low rehta hai).

## Roz ka flow (per team member)

**Step 1 — Queue lo (2 min)**
Claude Code mein bolo: `aaj ki backlink queue do <client> ke liye`
Claude dega: sites ki ranked list (DA / spam / Decision ke saath), har site ka
submission link, aur har site ka ready-made **content pack**.
- Sites pehle se filter hote hain: 🔴 kabhi nahi, already-used sites us client
  ke liye repeat nahi, spam >9% out.

**Step 2 — Site kholo, account banao (aap khud)**
- Signup / email verify / OTP / CAPTCHA / login — sab manually.
- Email + password **sheet ke apne columns mein hi** likho (Tracker D–E ya
  worksheet H–I). Claude in columns ko kabhi nahi padhta.

**Step 3 — Pack paste karo (30–60 sec)**
Pack mein sab ready hai: Business Name, Category (alternates ke saath), Short
+ Long description (har site ke liye alag — copy same text do sites pe MAT
karo), Address/NAP block, Phone, Website, Tags, Image note.
- Jo field site pe nahi hai, skip karo. Jo extra maange, pack ke "Site notes"
  dekho ya Claude se pucho.

**Step 4 — Live URL record karo**
Submit hone ke baad live/listing URL copy karke sheet mein daalo:
- Business listing → **GMB sheet › Tracker** (Date, Website, Keyword/Client,
  Live Link)
- Article/profile/bookmark → **worksheet › Daily work report** (Date, Target
  URL, Keywords, Activity, Live URL)
- Dashboard/settings URL nahi — **public listing URL** hi paste karo.

**Step 5 — QA apne aap hota hai**
Ankush/Claude `backlink-live-validator` chalata hai: har link logged-out check
hota hai (live? target URL laga? content complete? address hai?), Google/Bing
indexing dekhi jaati hai, aur verdict sheet mein wapas likha jaata hai.
- `SUCCESS` = done. Koi aur verdict = reason column padho, fix karo, dubara
  Live URL update karo.

## Rules (short)

1. Ek site ek client ke liye ek hi baar (Claude dedupe karta hai, phir bhi
   dhyan rakho).
2. Description edit kar sakte ho, par **facts add mat karo** — jo client ki
   site pe nahi hai, woh listing mein bhi nahi.
3. Password sirf designated columns mein. Kisi chat/message mein kabhi nahi.
4. Site pe kuch weird lage (paid demand, adult ads, malware popup) — skip
   karo aur Claude ko batao, woh inventory mein note karega.
5. Din ke end pe jitne bhi packs incomplete rahe, queue mein wapas chale
   jaate hain — chhupao mat, bas batao.

## Claude commands (jo aap bol sakte ho)

| Bolo | Milta hai |
|---|---|
| `aaj ki backlink queue do SKY7 ke liye` | Ranked sites + packs |
| `content pack banao <client> ke liye <site>` | Ek site ka fresh pack |
| `backlink validator chalao` | QA run + sheet verdicts |
| `queue sheet mein likho` | Pack Queue tab mein log |
