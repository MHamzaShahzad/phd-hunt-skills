# Contributing

## Adding a new skill

1. Copy the template: `cp -R templates/skill-template skills/<your-skill-name>`
2. Edit `skills/<your-skill-name>/SKILL.md`:
   - `name` must match the folder name (lowercase letters, digits, hyphens).
   - `description` says **what it does and when to use it**. Claude uses it to decide when to trigger the skill, so include the phrases users would actually say.
   - Keep `SKILL.md` focused (under ~300 lines). Put long reference material in `references/` and code in `scripts/`, and link to them.
3. If it reads or writes shared state, use `~/phd-hunt/profile.md` and `~/phd-hunt/tracker.csv`, so it fits with the other skills.
4. Run `python3 scripts/validate.py`.
5. Add a row to the skills table in `README.md`, and bump `version` in `.claude-plugin/plugin.json`.
6. Try it in Claude Code: `./scripts/install.sh`, then ask Claude something that should trigger it.

## Guidelines

- Never commit personal data (CVs, profiles, trackers, real email drafts). `.gitignore` blocks the usual paths.
- Skills must not send messages or submit applications without explicit per-batch user approval.
- Prefer verifiable sources and require URLs for factual claims.
