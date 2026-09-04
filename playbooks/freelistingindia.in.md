# Playbook: freelistingindia.in

Last verified: 04-09-2026 (FameNinja signup) · Auto Rating: 🟢 (signup agent-complete tak) · Time: ~3 min

## Entry
- Signup: homepage → "Register" → "Register with Email"
- Login type: email account, email-verification required

## Steps (jo actually chale — pilot run 1)
1. Homepage → Register click
2. "Register with Email" click → **Cloudflare verification screen aata hai** → 10s wait, khud clear ho jaata hai
3. Form: Name, Username, Email, Password, Confirm Password
4. Submit → agar "Username already exists" → naya username try karo
   (FameNinja taken tha → FameNinjaAgency chala)
5. Success → **email verification required** (mail aati hai, link click)

## Quirks / blocks
- Cloudflare interstitial register pe — wait karo, CAPTCHA nahi hai
- Username uniqueness strict; display-name alag field hai
- Account tabhi usable jab email verify ho jaye

## Field mapping
| Pack field | Form field | Notes |
|---|---|---|
| Business Name | Name | |
| — | Username | unique, conflicts common |
| Email | Email | verification mail aati hai |
