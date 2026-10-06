#!/usr/bin/env bash
# Install the skills into ~/.claude/skills for Claude Code.
#   ./scripts/install.sh          symlink (edits in this repo apply immediately)
#   ./scripts/install.sh --copy   copy instead of symlink
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
MODE="${1:-}"

mkdir -p "$DEST"
for dir in "$REPO"/skills/*/; do
  name="$(basename "$dir")"
  rm -rf "${DEST:?}/$name"
  if [ "$MODE" = "--copy" ]; then
    cp -R "$dir" "$DEST/$name"
  else
    ln -s "${dir%/}" "$DEST/$name"
  fi
  echo "installed $name"
done
mkdir -p "$HOME/phd-hunt"/{docs,drafts,sent,research}
echo "Done. Working files will live in ~/phd-hunt/"
