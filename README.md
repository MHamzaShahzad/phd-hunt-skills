# PhD Hunt Skills for Claude

A set of [Claude skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) that help you find a **funded PhD**: from building your profile, to finding universities and supervisors, to writing personal outreach emails that professors actually answer.

Everything is grounded in sources Claude opens during the session. Nothing is invented, and no email is sent without your explicit approval.

## Skills

| Skill | What it does |
|---|---|
| [`phd-profile`](skills/phd-profile/SKILL.md) | Builds your applicant profile from your CV plus a few questions. Every other skill reads it. |
| [`phd-university-scout`](skills/phd-university-scout/SKILL.md) | Searches your target countries the way PhD admission actually works there (advertised positions, department programs, scholarships). Ranks the matches. |
| [`phd-funding-shortlist`](skills/phd-funding-shortlist/SKILL.md) | Keeps only funded routes you're eligible for (studentships, doctoral networks, university and government scholarships, RA posts), confirmed on official pages. |
| [`phd-researcher-discovery`](skills/phd-researcher-discovery/SKILL.md) | Paper-first: finds the people actively publishing in your area (OpenAlex, Scholar, DBLP, etc.), then checks their labs, vacancies and grants. |
| [`phd-professor-outreach`](skills/phd-professor-outreach/SKILL.md) | Researches each professor, prepares documents, and drafts personal emails in your own voice. Sends from your own mailbox only after you approve. Tracks follow-ups. |

```
phd-profile ──► phd-university-scout ──► phd-funding-shortlist ──┐
            └─► phd-researcher-discovery ────────────────────────┴─► phd-professor-outreach
```

All working files (profile, tracker, drafts, dossiers) live in `~/phd-hunt/` on your machine. They are never stored in this repo.

## Install

### Claude Code: as a plugin (recommended)
```
/plugin marketplace add MHamzaShahzad/phd-hunt-skills
/plugin install phd-hunt@phd-hunt-skills
```

### Claude Code: manually
```bash
git clone https://github.com/MHamzaShahzad/phd-hunt-skills.git
cd phd-hunt-skills && ./scripts/install.sh
```

### Claude.ai / Claude desktop app
```bash
./scripts/package.sh
```
Then upload each zip from `dist/` under **Settings → Capabilities → Skills**.

## Usage

Just ask in plain language:

- "Set up my PhD profile" (attach your CV)
- "Find universities in the UK, Germany and the Netherlands for my profile"
- "Shortlist the ones with funding I'm eligible for"
- "Who's publishing on federated learning for medical imaging in Europe? Check if their labs have PhD openings"
- "Draft emails to the top 5 professors"
- "Which professors need a follow-up?"

## Principles

- **Evidence over memory:** every deadline, funding claim, title and email address must come from a page opened in the session.
- **Your voice, your facts:** emails are written from your own writing samples and your CV. There are no generic templates and no made-up compliments or achievements. Read every draft before it goes out.
- **You stay in control:** nothing is sent without your explicit approval of each batch. Emails go out from your own account, paced and one per professor.
- **Respectful outreach:** emails are only sent to verified addresses, never to people who've said they aren't taking students, and with at most one follow-up.

## Optional setup

- `OPENALEX_EMAIL=you@example.com` gives faster, more reliable [OpenAlex](https://openalex.org) access for researcher discovery. `OPENALEX_API_KEY` is also supported.
- Connect a Gmail or Outlook connector in Claude to create drafts and send directly. Otherwise Claude uses Claude in Chrome, or hands you the final drafts to send yourself.

## Contributing

New skills and improvements are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
