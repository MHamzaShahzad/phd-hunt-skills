#!/usr/bin/env python3
"""Check every skills/*/SKILL.md has valid frontmatter and working relative links."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors = []

for skill in sorted((ROOT / "skills").iterdir()):
    if not skill.is_dir():
        continue
    md = skill / "SKILL.md"
    if not md.exists():
        errors.append(f"{skill.name}: missing SKILL.md")
        continue
    text = md.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{skill.name}: missing frontmatter")
        continue
    fm = dict(re.findall(r"^(\w+):\s*(.+)$", m.group(1), re.M))
    if fm.get("name") != skill.name:
        errors.append(f"{skill.name}: frontmatter name '{fm.get('name')}' must match folder")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", skill.name):
        errors.append(f"{skill.name}: name must be lowercase letters, digits, hyphens")
    desc = fm.get("description", "")
    if not desc or len(desc) > 1024:
        errors.append(f"{skill.name}: description missing or over 1024 chars")
    for link in re.findall(r"\]\(((?!https?:)[^)#]+)\)", text):
        if not (skill / link).exists():
            errors.append(f"{skill.name}: broken link {link}")
    print(f"ok  {skill.name}" if not any(e.startswith(skill.name) for e in errors) else f"ERR {skill.name}")

for e in errors:
    print("  -", e)
sys.exit(1 if errors else 0)
