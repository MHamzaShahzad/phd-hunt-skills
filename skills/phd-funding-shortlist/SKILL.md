---
name: phd-funding-shortlist
description: Shortlist universities and specific PhD positions where funding (studentships, scholarships, RA/TA, government scholarships) is actually available to the applicant, based on their nationality and profile. Writes ~/phd-hunt/research/shortlist.md and updates tracker.csv. Use when the user asks for funded PhDs, scholarships, a shortlist, or "where can I get funding".
---

# PhD Funding Shortlist

## Inputs
- `~/phd-hunt/profile.md` (nationality, funding requirement, intake)
- `~/phd-hunt/research/universities.md` (from **phd-university-scout**). If it's missing, run that skill first, or run a narrower search if the user only wants funded positions.

## Funding categories to check, per university
1. **Advertised funded positions:** a specific project with a named supervisor and salary or stipend (best: highest chance, clear process).
2. **Doctoral training programs:** e.g. UKRI CDTs/DTPs, EU MSCA Doctoral Networks, Helmholtz/Max Planck schools, ETH/EPFL doctoral schools.
3. **University scholarships:** institutional international PhD scholarships (check whether they're open to the user's nationality).
4. **Government/external scholarships:** DAAD, Fulbright, Commonwealth, Chevening (Master's only — exclude), Erasmus Mundus, CSC, GKS, MEXT, HEC (Pakistan) overseas scholarships, Endeavour/RTP, Vanier, Swedish Institute, etc. Match them to the user's nationality.
5. **Professor-funded RA positions:** US/Canada/Australia mostly. Evidence: an active grant (NSF/NIH/ERC/ARC/NSERC award pages), "I'm recruiting" on the lab site, or recent new students.

## Workflow
1. For each university in the long list, find **concrete evidence** of funding open to the user: URL, amount, coverage (tuition + stipend?), nationality restrictions, and deadline.
2. Drop entries that have no funding route or whose deadline has passed for the target intake. Keep a "dropped" section with the reason.
3. Classify the rest:
   - **A, apply now:** funded, open, eligible, deadline within the window
   - **B, contact a professor first:** funding depends on supervisor support (US/CA/AU/Asia scholarships)
   - **C, watch:** funding likely, but the call isn't open yet
4. Write `~/phd-hunt/research/shortlist.md` with a table: Tier | University | Position/Scholarship | Funding (amount, coverage) | Eligible? | Deadline | Supervisor(s) if named | Source. Sort by deadline.
5. Append the A and B entries to `~/phd-hunt/tracker.csv` with `status=shortlisted`, without duplicating existing rows (match on university + department + professor).
6. Summarize in chat: counts per tier, the five nearest deadlines, and the recommended next step (usually **phd-professor-outreach** for tier B and named-supervisor A entries).

## Rules
- Funding claims must come from an official page (university, funder, or government) opened this session. Aggregator pages (FindAPhD etc.) are fine for discovery, but confirm on the source page.
- Flag stipends below the country's typical living cost.
- Don't give financial advice beyond reporting what each source says.
