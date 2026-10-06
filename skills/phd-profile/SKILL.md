---
name: phd-profile
description: Build or update the applicant's PhD search profile (research interests, degrees, CGPA, publications, tests, target countries, funding needs, constraints) stored at ~/phd-hunt/profile.md. Use when the user says "set up my profile", "update my profile", shares a CV for PhD applications, or when any other phd-* skill finds the profile missing or incomplete.
---

# PhD Profile

Every other phd-* skill (university-scout, funding-shortlist, professor-outreach) reads `~/phd-hunt/profile.md`. This skill creates and maintains it.

## Workflow

1. **Collect sources.** Ask for the CV (PDF/DOCX) if not already in `~/phd-hunt/docs/`. Copy it there as `CV.pdf`. Extract everything you can from it before asking questions.
2. **Fill gaps by asking.** Only ask about fields the CV doesn't answer. Use AskUserQuestion for choices (countries, intake, funding), and plain questions for free text. Required fields:
   - Full name, nationality/passport (affects scholarships and visas), current country
   - Degrees: title, university, years, CGPA/scale, thesis title and one-line summary
   - Research interests: 2–4 specific topics, plus 5–10 keywords used to match professors
   - Publications (with links/DOIs), projects, industry experience
   - Tests: IELTS/TOEFL/GRE/language scores and expiry dates (or "planned")
   - Target countries (ranked), target intake (e.g. Fall 2027), and any city/university-tier preferences
   - Funding: fully funded only? Accept a tuition waiver plus a stipend? Minimum stipend?
   - Constraints: family, visa history, deadlines, "do not contact" universities or people
   - Documents available: CV, transcripts, degree certificates, research proposal, writing sample, recommendation letters (names of referees)
   - Writing voice: 2–3 emails or paragraphs the user wrote themselves (used to match their style — see phd-professor-outreach)
3. **Write the profile** to `~/phd-hunt/profile.md` using the template below. Show a short summary and ask the user to correct anything wrong.
4. **Never invent** achievements, scores, or publications. Mark unknowns `TBD`.

## Template

```markdown
# PhD Profile — <Name>
_Last updated: YYYY-MM-DD_

## Identity
- Nationality: | Current location: | Email used for outreach:

## Education
| Degree | University | Years | CGPA | Thesis |

## Research
- Core interests:
- Match keywords:
- One-paragraph research statement (in the user's voice):

## Outputs
- Publications:
- Projects / experience:

## Tests
| Test | Score | Date | Expires |

## Targets
- Countries (ranked):
- Intake:
- Funding requirement:
- Exclusions:

## Documents (in ~/phd-hunt/docs/)
| File | Status |

## Voice samples
> (paste the user's own writing here)
```

Also create `~/phd-hunt/tracker.csv` if missing, with this header:
`id,university,country,department,professor,title,email,email_verified,profile_url,fit_score,funding_type,deadline,status,draft_path,sent_date,followup_date,notes`
