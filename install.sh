#!/bin/bash
# Installs/updates the assembly-line skills into ~/.claude/skills/
set -e
SRC="$(cd "$(dirname "$0")/skills" && pwd)"
DEST="$HOME/.claude/skills"
mkdir -p "$DEST"
for skill in backlink-assembly-line backlink-pack-generator saas-listing-pack backlink-live-validator infographic-backlink ppt-pdf-backlink; do
  rm -rf "$DEST/$skill"
  cp -R "$SRC/$skill" "$DEST/$skill"
  echo "installed: $skill"
done
echo "Done. Claude Code restart karo ya naya session kholo — skills load ho jayengi."
