#!/bin/bash
# Khaali PASS_ entries ke liye naye random passwords bana ke .env mein bhar deta hai.
# Ye script AAP chalate ho — Claude passwords kabhi nahi dekhta.
set -e
cd "$(dirname "$0")"
[ -f .env ] || { echo ".env nahi mila"; exit 1; }
filled=0
while IFS= read -r line; do
  case "$line" in
    PASS_*=)
      var="${line%%=}"
      pw="$(openssl rand -base64 18 | tr '+/' 'Xz' | cut -c1-20)"
      # portable in-place edit
      awk -v v="$var" -v p="$pw" 'BEGIN{FS=OFS="="} $1==v && $2=="" {$2=p} {print}' .env > .env.tmp && mv .env.tmp .env
      filled=$((filled+1))
      ;;
  esac
done < .env
chmod 600 .env
echo "Done: $filled naye passwords .env mein save ho gaye (chmod 600)."
echo "Dekhne ke liye:  open .env   — inhe baad mein 1Password mein bhi daal lena."
