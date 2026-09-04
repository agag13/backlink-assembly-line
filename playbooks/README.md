# Site Playbooks — per-site process memory

Ek baar jis site pe form bhara, uska process yahan save hota hai —
`<domain>.md` (format: `_TEMPLATE.md`). Agli baar Claude pehle playbook
padhta hai, phir bharta hai → faster + zero re-discovery.

Rules:
- Har submit (success YA blocked) ke baad Claude playbook update karta hai
  aur `Last verified` stamp karta hai.
- Playbook fail ho jaye (site badal gayi) → broken step correct karo,
  file delete mat karo.
- PROCESS only — credentials/client content kabhi nahi.
- Playbook bana → Site DB ke Notes mein 📖 lag jaata hai.

Ye folder git mein hai, isliye ek member ka seekha hua process poori team
ko `git pull` pe mil jaata hai.
