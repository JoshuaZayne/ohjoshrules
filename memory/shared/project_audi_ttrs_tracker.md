---
name: project_audi_ttrs_tracker
description: "Audi TT RS 2020-2023 used-price tracker — standalone repo, WebFetch-gathered cars.com snapshots + SQLite trend analysis"
metadata: 
  node_type: memory
  type: project
  originSessionId: d31d1692-06ab-404d-a66c-87e7746d1901
  modified: 2026-08-03T02:58:18.496Z
---

**Repo:** `F:\GitHub Repos\AudiTTRSPriceTracker\` (local git, first commit bf98bdd; NOT yet on GitHub as of 2026-08-02). Standalone, deliberately separate from the RAM truck scraper (that pipeline is truck-specialized and doesn't transfer). Tracks the **Audi TT RS, model years 2020-2023** (2023 = the final/discontinued year) to see how used prices move over time — a discontinued low-volume enthusiast car that may be forming a price floor.

**Design:** aggregator search pages hard-wall bare HTTP, so listings are gathered by the AGENT's WebFetch (a library script can't call WebFetch) into a dated snapshot file `snapshots/YYYY-MM-DD.txt` (one line per car: `YEAR | PRICE | MILEAGE | LOCATION`), then `python track.py ingest <file>` folds it into `ttrs_history.db` (SQLite, gitignored) and `python track.py analyze` reads it. cars.com reads cleanly via WebFetch; AutoTrader/Edmunds 403; CarGurus just re-lists the same cars. cars.com URL is in the README.

**Recurring workflow (build the trend):** WebFetch the cars.com URL -> save lines to a dated snapshot -> ingest -> analyze. Listings keyed by `year+location` (no VIN in the summary) so re-ingesting catches price cuts on the same car + grows the market-median-by-run trend. Automate via a scheduled Claude routine (the WebFetch step needs the agent).

**Findings (2026-08-02 baseline, n=7 — TT RS is scarce nationwide):** median $73,894 ($53k-$104k); **price~mileage -0.71, ~ -$650 per 1,000 mi (~-$6.5k/10k)** = mileage-dominated, the low-mileage-collectible premium. Trend needs a 2nd snapshot. Hedonic year/mileage split is preliminary at small n (year/mileage collinear).

**Open:** push to GitHub (offered), and/or schedule the weekly gather. Reuses the econometric approach from [[project_ram_megacab_scraper]]'s `scripts/trees/econometrics.py`.
