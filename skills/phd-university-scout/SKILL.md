---
name: phd-university-scout
description: Search universities across the applicant's target countries for PhD programs that match their research profile. Produces a ranked long list in ~/phd-hunt/research/universities.md. Use when the user asks to find, search, or list universities or PhD programs, or "where should I apply".
---

# PhD University Scout

## Prerequisite
Read `~/phd-hunt/profile.md`. If it's missing or the Research/Targets sections are `TBD`, run the **phd-profile** skill first.

## Workflow

1. **Plan per country.** For each target country, note how PhD admission works, because this changes the search:
   - **UK / Ireland / Netherlands / Nordics / Germany / Switzerland / Austria / Belgium / France:** many PhDs are advertised *positions* (paid jobs or funded studentships). Search job portals first.
   - **USA / Canada:** admission goes through department programs. Funding usually comes through RA/TA positions, and the professor's interest matters a lot.
   - **Australia / NZ:** university scholarships (RTP and similar) plus supervisor endorsement before applying.
   - **Asia (China, Korea, Japan, HK, Singapore, Taiwan):** government scholarships (CSC, GKS, MEXT, HKPFS, SINGA) plus a supervisor acceptance letter.
   - Anything else: search "<country> PhD admission international funded".
2. **Search.** Use WebSearch and WebFetch. Good sources:
   - FindAPhD, EURAXESS, Academic Positions, jobs.ac.uk, Nature Careers, ScholarshipDb, university "PhD vacancies" pages, DAAD PhDGermany
   - Subject rankings for the field (QS/THE/CSRankings/ShanghaiRanking by subject) to identify strong departments. Rankings are a starting point, not the deciding factor.
   - Department pages: confirm the research group in the user's area actually exists.
3. **Filter and score** each university/department (1–5 per criterion):
   - Research match: groups working on the profile's keywords
   - Funding likelihood for international students of the user's nationality
   - Eligibility: CGPA, English test, Master's requirement
   - Timing: the deadline is reachable for the target intake
   - The user's own preferences (country rank, tier, city)
4. **Output** to `~/phd-hunt/research/universities.md`: a table sorted by total score, with columns University | Country | Department/Group | Why it matches | Admission route | Deadline | Source URLs. Aim for 30–60 entries unless the user asks otherwise.
5. **Report** the top 15 in chat, then ask whether to continue to **phd-funding-shortlist**.

## Rules
- Every row must have at least one source URL you actually opened. Never list a deadline or requirement from memory. Mark it `verify` if you couldn't confirm it.
- Respect the exclusions in the profile.
- For large searches, run one research subagent per country in parallel, and give each the profile keywords and this scoring rubric.
