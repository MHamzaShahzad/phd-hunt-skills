---
name: phd-researcher-discovery
description: Paper-first discovery of potential PhD supervisors. Find researchers actively publishing in the applicant's domain (via OpenAlex, Google Scholar, Semantic Scholar, arXiv, DBLP), list them, check their labs and universities, and look for PhD vacancies or funding with them. Use when the user wants to find researchers or labs by research topic, "who is publishing on X", find supervisors from papers, or check vacancies in specific labs.
---

# PhD Researcher Discovery (paper-first)

This is the bottom-up counterpart to **phd-university-scout**. Instead of starting from universities, start from recent papers. That finds the people doing the most relevant work right now, including at universities that rankings would miss.

## Inputs
- `~/phd-hunt/profile.md`: match keywords, target countries, intake, funding needs. If it's missing, run **phd-profile**.
- Optional: specific papers the user admires. Use their authors, plus the papers that cite them, as extra seeds.

## Phase 1: Build queries
From the profile keywords, write 3–6 search queries: specific phrases, not single words (e.g. "federated learning medical imaging", not "AI"). Include synonyms and method + application pairs. Show them to the user for a quick check.

## Phase 2: Harvest researchers
Run the script (it uses only the standard library, with a curl fallback for SSL):
```bash
python3 ~/.claude/skills/phd-researcher-discovery/scripts/find_researchers.py \
  --query "<q1>" --query "<q2>" --since <current year - 3> \
  --countries <ISO-2 codes from the profile, e.g. GB,DE,NL> --pages 3 \
  --out ~/phd-hunt/research/researchers_raw.csv
```
- It keeps **last or corresponding authors** (usually the group leader) with at least 2 matching papers, and ranks them by number of matching papers, how many queries they match, how recent they are, and citations.
- Widen the search with `--pages 5` or more queries if it returns too few people. Narrow it with more specific queries or `--min-papers 3` if it returns too many.
- Extra seeds: for each paper the user admires, look up its citing works and related authors on Semantic Scholar or Google Scholar, and add them.
- For CS, cross-check DBLP and top-venue proceedings (NeurIPS/ICML/CVPR/ACL etc.). For biomedicine, cross-check PubMed.

## Phase 3: Verify each researcher (top 30–50)
For each person, open real pages (WebSearch + WebFetch, one subagent per batch of about 10 if there are many):
1. **Position:** are they a PI who can supervise PhDs (Professor, Associate/Assistant Professor, Group Leader, Reader, Lecturer in the UK)? Drop postdocs and students, but note their PI, since that PI is often a good target.
2. **Current affiliation:** OpenAlex can be out of date. Confirm on the university page.
3. **Lab page:** the group name and URL, current team size, recent PhD graduates, and "join us"/"open positions" text.
4. **Vacancies and funding:**
   - The lab's or department's vacancy page, the university jobs portal, FindAPhD, EURAXESS, jobs.ac.uk, Academic Positions: search for "<name> PhD".
   - Active grants (ERC, UKRI/gtr.ukri.org, NSF, NIH RePORTER, DFG GEPRIS, ARC, NSERC) that mention PhD positions or have years left to run.
   - Doctoral programs or scholarships at that university open to the user's nationality.
5. **Verified email** from the official directory, lab page, or a paper's corresponding-author line. A guessed address = `email_verified=no`.
6. **Red flags:** emeritus, moving, "not accepting students", the group appears inactive.

## Phase 4: Output
- `~/phd-hunt/research/researchers.md`: a table sorted by fit, with columns Name | Title | University (Country) | Lab URL | Why relevant (2 recent papers) | Vacancy/funding status (open now / grant-funded / scholarship route / none found) | Email verified? | Sources.
- Append the verified PIs to `~/phd-hunt/tracker.csv` with `status=identified`, adding `paper-first` to `notes`. Deduplicate against existing rows by name + university.
- Save a dossier per person at `~/phd-hunt/research/prof-<slug>.md` in the same format as **phd-professor-outreach** uses, so outreach can reuse it directly.
- In chat: the top 10, how many have an open vacancy right now, and the recommended next step. Researchers with open vacancies go to **phd-funding-shortlist** for eligibility checks. Researchers with only a funding route go straight to **phd-professor-outreach**.

## Rules
- Every claim (title, vacancy, grant, email) needs a URL opened this session. Mark anything else `unverified`.
- Script output is a lead list, not a verified list. Never email anyone from the raw CSV without Phase 3.
- Respect the profile's exclusions and target countries.
