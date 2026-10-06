#!/usr/bin/env python3
"""Find active research group leaders from recent papers via OpenAlex.

Searches recent works for each query, keeps likely PIs (last or corresponding
authors), and ranks them by how many matching papers they have.

Usage:
  find_researchers.py --query "graph neural networks" --query "drug discovery" \
      --since 2023 --countries GB,DE,NL --pages 3 --out researchers.csv

Optional env: OPENALEX_API_KEY, OPENALEX_EMAIL (polite pool).
"""
import argparse
import csv
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict

API = "https://api.openalex.org/works"
FIELDS = "id,title,publication_year,cited_by_count,doi,authorships,primary_location"


def fetch(params):
    if os.environ.get("OPENALEX_API_KEY"):
        params["api_key"] = os.environ["OPENALEX_API_KEY"]
    if os.environ.get("OPENALEX_EMAIL"):
        params["mailto"] = os.environ["OPENALEX_EMAIL"]
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            try:
                with urllib.request.urlopen(url, timeout=30) as r:
                    return json.load(r)
            except urllib.error.URLError as e:
                if "CERTIFICATE" not in str(e):
                    raise
                # macOS python.org builds often lack CA certs; fall back to curl
                out = subprocess.run(["curl", "-sf", "--max-time", "30", url],
                                     capture_output=True, check=True).stdout
                return json.loads(out)
        except Exception as e:  # rate limits, transient errors
            if attempt == 3:
                print(f"request failed: {e}", file=sys.stderr)
                return {"results": []}
            time.sleep(2 ** attempt)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--query", action="append", required=True)
    ap.add_argument("--since", type=int, default=2023)
    ap.add_argument("--countries", default="", help="ISO-2 codes, comma separated")
    ap.add_argument("--pages", type=int, default=3, help="pages of 100 per query")
    ap.add_argument("--min-papers", type=int, default=2)
    ap.add_argument("--out", default="researchers.csv")
    a = ap.parse_args()

    countries = {c.strip().upper() for c in a.countries.split(",") if c.strip()}
    people = defaultdict(lambda: {"papers": [], "cites": 0, "insts": defaultdict(int),
                                  "countries": defaultdict(int), "queries": set(),
                                  "years": set(), "orcid": ""})

    for q in a.query:
        filt = f"from_publication_date:{a.since}-01-01,type:article|preprint|proceedings-article"
        if countries:
            filt += ",institutions.country_code:" + "|".join(sorted(countries))
        for page in range(1, a.pages + 1):
            data = fetch({"search": q, "filter": filt, "per-page": 100,
                          "page": page, "select": FIELDS, "sort": "relevance_score:desc"})
            works = data.get("results", [])
            if not works:
                break
            for w in works:
                auths = w.get("authorships") or []
                for au in auths:
                    is_pi = au.get("author_position") == "last" or au.get("is_corresponding")
                    if not is_pi or len(auths) < 2:
                        continue
                    insts = au.get("institutions") or []
                    if countries and not any(i.get("country_code") in countries for i in insts):
                        continue
                    aid = (au.get("author") or {}).get("id")
                    if not aid:
                        continue
                    p = people[aid]
                    p["name"] = au["author"].get("display_name", "")
                    p["orcid"] = au["author"].get("orcid") or p["orcid"]
                    if w["id"] not in [x[0] for x in p["papers"]]:
                        venue = ((w.get("primary_location") or {}).get("source") or {}).get("display_name", "")
                        p["papers"].append((w["id"], w.get("title") or "", w.get("publication_year"),
                                            w.get("doi") or "", venue))
                        p["cites"] += w.get("cited_by_count") or 0
                        p["years"].add(w.get("publication_year"))
                    p["queries"].add(q)
                    for i in insts:
                        p["insts"][i.get("display_name", "")] += 1
                        p["countries"][i.get("country_code", "")] += 1
            time.sleep(0.2)

    rows = []
    for aid, p in people.items():
        if len(p["papers"]) < a.min_papers:
            continue
        papers = sorted(p["papers"], key=lambda x: x[2] or 0, reverse=True)
        rows.append({
            "name": p["name"],
            "institution": max(p["insts"], key=p["insts"].get) if p["insts"] else "",
            "country": max(p["countries"], key=p["countries"].get) if p["countries"] else "",
            "matching_papers": len(papers),
            "latest_year": max(y for y in p["years"] if y),
            "total_cites_matching": p["cites"],
            "queries_matched": "; ".join(sorted(p["queries"])),
            "recent_titles": " || ".join(f"{t} ({y}, {v})" for _, t, y, _, v in papers[:3]),
            "recent_dois": " ".join(d for _, _, _, d, _ in papers[:3] if d),
            "openalex_id": aid,
            "orcid": p["orcid"],
        })
    rows.sort(key=lambda r: (r["matching_papers"], len(r["queries_matched"]), r["latest_year"],
                             r["total_cites_matching"]), reverse=True)

    with open(a.out, "w", newline="") as f:
        if rows:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
    print(f"{len(rows)} researchers written to {a.out}")
    for r in rows[:15]:
        print(f"- {r['name']} | {r['institution']} ({r['country']}) | "
              f"{r['matching_papers']} papers, latest {r['latest_year']}")


if __name__ == "__main__":
    main()
