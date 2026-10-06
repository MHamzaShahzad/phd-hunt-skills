---
name: phd-professor-outreach
description: Identify relevant professors at shortlisted universities, research their recent work, prepare tailored documents (CV variant, research statement/proposal), compose personalized emails in the applicant's own voice, attach the CV and required documents, and send them from the applicant's own mailbox after approval. Also handles follow-ups. Use when the user asks to find professors/supervisors, write or send emails to professors, cold-email for a PhD, or follow up.
---

# PhD Professor Outreach

## Inputs
- `~/phd-hunt/profile.md`. If it's missing, run **phd-profile**.
- `~/phd-hunt/tracker.csv` (shortlisted rows). If it's empty, run **phd-funding-shortlist**.
- `~/phd-hunt/docs/`: CV.pdf, transcripts, degree certificates, research proposal, test scores.
- Writing guide: [references/voice-and-style.md](references/voice-and-style.md). **Read it before drafting anything.**

## Phase 1: Identify professors
If `tracker.csv` already has rows from **phd-researcher-discovery** (notes contain `paper-first`) with dossiers in `research/`, reuse them and skip to Phase 2 for those people. Otherwise, for each shortlisted university or department:
1. Open the faculty directory and lab pages. Candidates are professors whose last 3 years of work overlap the profile's match keywords.
2. For each candidate, collect from sources you actually open (Google Scholar, DBLP, lab site, recent papers, grant pages):
   - Title and rank, research lines, **2–3 recent papers (2023+)** with a one-line understanding of each
   - Recruiting signals: "open positions", an active grant, a funded project ad, a lab size trend
   - Red flags: emeritus, moving, "not taking students", sabbatical
   - **Email address, verified** from the official directory, lab page, or a paper's corresponding-author line. A pattern-guessed address is NOT verified: mark `email_verified=no`, and never send to it.
3. Score fit from 1 to 10 with a one-line reason. Save a dossier for each professor at `~/phd-hunt/research/prof-<slug>.md`.
4. Add the professors to `tracker.csv` (`status=identified`). Contact **one professor per department** at a time unless the ad names several. Show the user the list and let them remove names.

## Phase 2: Build documents
- **CV:** use the user's `CV.pdf` as-is by default. If they want tailored versions, use the docx/pdf skills to produce `CV_<University>.pdf`, reordering emphasis only. Never add content that isn't true.
- **Research statement/proposal:** if the position or country requires one (common in UK, EU, AU, and Asia), draft a 1–2 page version tailored to the group, using the profile's research statement as the base. Save it to `~/phd-hunt/docs/<University>/`.
- **Required docs** per the position ad: transcripts, degree certificate, English test, publication list. Check what exists in `docs/`, list what's missing, and ask the user for it. Don't fabricate.
- Keep filenames human and simple: `Firstname_Lastname_CV.pdf`, not `CV_final_v3_AI.pdf`.

## Phase 3: Compose emails
Follow [references/voice-and-style.md](references/voice-and-style.md) exactly. For each professor, write `~/phd-hunt/drafts/<slug>.md` containing:
```
To: <verified email>
Subject: <specific subject>
Attachments: <paths>
---
<plain-text body>
---
Facts used: <every claim about the professor's work, with source URL>
```
Then run the **self-check** in the style guide on every draft. Show the drafts to the user in batches of up to 5 and apply their edits. When the user rewrites a sentence, treat their wording as the new voice reference for later drafts.

## Phase 4: Send (only with explicit approval)
- **Never send without the user's explicit "yes, send" for that specific batch in chat.** Approving one batch doesn't approve the next.
- Send from the user's **own** mailbox, so the email has their real address, signature, and sent history:
  1. **Gmail/Outlook connector** (preferred): if a mail connector is connected, create **drafts** with attachments, then send the approved ones. Check with `mcp__ccd_connectors__session_connectors_status`. If none is connected, suggest the user connect Gmail, or use option 2.
  2. **Claude in Chrome**, with the user's logged-in webmail: compose, paste the body, attach the files via file_upload, and leave it as a draft, or send after approval.
  3. **Fallback:** produce the final text and attachment list, and the user sends it themselves.
- Pacing: at most ~8–10 new emails a day, spread out (not a burst at the same minute), sent during the recipient's local working hours (Tue–Thu mornings are best). Plain text, no tracking pixels, no mass BCC: one email per professor.
- After sending, update `tracker.csv`: `status=sent`, `sent_date`, and `followup_date` = sent + 10–14 days. Move the draft to `~/phd-hunt/sent/`.

## Phase 5: Follow-ups and replies
- When asked to check, list rows past `followup_date` with no reply. Draft **one** short follow-up per professor (3–4 sentences, replying in the same thread, adding one new piece of info if possible). Don't send a second follow-up.
- If the user pastes a reply, update the status (`positive`, `declined`, `redirect`, `interview`) and draft a response, or prep notes for an interview (their recent papers, likely questions, questions to ask them).

## Hard rules
- No invented facts, papers, scores, or compliments. Every specific claim about the professor appears in "Facts used" with a URL.
- No emailing unverified addresses, people who said "no students", or the profile's exclusions.
- Never send the same email body to two professors.
