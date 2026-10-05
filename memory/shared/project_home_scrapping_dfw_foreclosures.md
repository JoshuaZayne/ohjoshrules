---
name: project_home_scrapping_dfw_foreclosures
description: "Home_Scrapping repo - DFW foreclosure auction workbook with per-property sheets, candidates, and validated links"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9963e99d-85bd-4489-930c-72590fb5ce89
---

`~/repos/Home_Scrapping` builds an Excel workbook of DFW foreclosure-auction picks (June 2 2026 sale). Canonical output: `DFW_Foreclosures_June_2026_FULL.xlsx` (~56 sheets: master "Foreclosures" 9 picks + "Equity Ranking" + "DFW Candidates" 34 finds + 8 City tabs + per-property sheets w/ bold DEAL ANALYSIS block, PDF text, embedded notice-of-sale scans + Link Legend).

IMPORTANT exception to [[feedback_file_timestamps]]: per user (2026-05-24), this workbook uses ONE canonical filename that build_final.py OVERWRITES each run (no YYYY-MM-DD_HHMMSS) - they had 7 duplicate timestamped copies causing Excel to reopen stale versions and throw errors. The "last checked" date lives inside the workbook (CHECKED const) instead of the filename. Do NOT auto-launch Excel after each rebuild (it stacked windows).

Scripts: `build_final.py` (consolidated builder, `--key` for Street View), `build_property_sheets.py` (earlier per-sheet builder), `validate_links.py` (HTTP-checks every hyperlink; run with the Bash sandbox DISABLED or curl returns code 0). Data: `data/dfw_candidates_jun2_2026.json`.

Key facts learned:
- Source PDFs in `pdfs/` are scanned legal notices (text layer present, NO house photos).
- Link reality (see repo `SCRAPING_METHODS.md`): Google Maps + Redfin verify HTTP 200 via curl; Zillow/Realtor/HAR always 403 to bots (browser-valid only). foreclosure.com fetches fine via WebFetch; auction.com is an empty SPA shell. Aggregators do NOT publish amount owed (needs county NOS PDF / servicer).
- Link policy: SINGLE-HOME ONLY (no search/area pages). Google Maps exact pin + Zillow /homedetails + verified Redfin /home/<id> + Realtor detail. Homes with no street # in NOS (Farmersville CR599, Turnbridge Manor, Birmingham Farms) get a red note, no listing link. Summaries use internal_link() (location attr) for in-workbook nav; all verified 0 dangling. Last audit: 107 web links 0 BROKEN, 201 internal links 0 dangling.

2026-05-25 update: 39 candidates (added 208 Gatwick Ct Wylie, 604 Maple Leaf Ln McKinney, 14771 Alstone Dr Frisco, 309 Whisperfield Dr Murphy, 3905 Kite Meadow Dr Plano; fixed exact addresses for 9716 Lance Dr / 2325 Regal Rd / 902 W Lamar St; corrected #01 Zillow zpid 26590383). Candidate JSON now supports `listing_url` (user-provided canonical single-home link, preferred), `owed`, and `status`. 14771 Alstone has real-ish owed: ~$400K liens (foreclosure.com) -> equity ~$284K (42%). Workbook 62 sheets; 99 OK / 24 BLOCKED-403 / 0 BROKEN, 227 internal nav links 0 dangling.

PENDING: user to supply Google Maps API key -> rerun `build_final.py --key <KEY>` to embed Street View photos. Roadmap: [[feedback_roadmap_default]] file `CodeMapping_Brain/content/roadmaps/2026-05-24_153900_home-scraping-per-property-sheets-and-new-auction-finds.md`.
