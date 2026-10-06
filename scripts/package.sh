#!/usr/bin/env bash
# Zip each skill for upload to claude.ai (Settings > Capabilities > Skills).
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$REPO/dist"
rm -rf "$OUT" && mkdir -p "$OUT"
cd "$REPO/skills"
for dir in */; do
  name="${dir%/}"
  zip -qr "$OUT/$name.zip" "$name" -x '*/__pycache__/*' '*.DS_Store'
  echo "dist/$name.zip"
done
