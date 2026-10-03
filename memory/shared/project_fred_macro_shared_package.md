---
name: project_fred_macro_shared_package
description: FredMacroData repo (fred_macro package) = the ONE shared FRED downloader; used by Brokers and MarketCommentaryResearch (created 2026-10-02)
metadata:
  node_type: memory
  type: project
  originSessionId: cbe75536-e18b-4367-9ec3-e6cd6153689b
  modified: 2026-10-03T06:45:15.629Z
---

**FredMacroData** (private, `JoshuaZayne/FredMacroData`, desktop clone `F:\GitHub Repos\FredMacroData`) holds the `fred_macro` package: 31 FRED series in 10 groups + derived 10s30s/20s30s/5s10s/2s30s spreads, keyless `fredgraph.csv` endpoint, `fred-macro` CLI, 9 offline tests. Editable-installed into Anaconda on the desktop.

Consumers find it via installed import OR a device path loop (F:\GitHub Repos, C:\Users\ohjos, D:\Code, ~, /home/pi):
- **Brokers** `scripts/fred/fred_downloader.py` is a thin wrapper (data -> `Brokers/data/fred/csv`, gitignored). **Not** in Brokers `requirements.txt` on purpose: the Docker image installs from it and has no creds for the private repo.
- **MarketCommentaryResearch** (private, `F:\GitHub Repos\MarketCommentaryResearch`): one folder per video/interview (summary.md, chart HTML, `make_all.py`, `build_fred_charts.py` + template, `fetch_transcript.py`). Transcripts are gitignored (copyrighted). First entry: 2026-09-30 David Levenson / Rebel Capitalist.

**v1.1.0 (2026-10-03):** 37 series; added Optimal Blue DAILY mortgage indexes (OBMMIC30YF, OBMMIC15YF, OBMMIJUMBO30YF, OBMMIFHA30YF, OBMMIVA30YF, OBMMIUSDA30YF; 2017+, weekly avg tracks Freddie MORTGAGE30US at 0.997 corr, +0.13pt). MarketCommentaryResearch now has `shared/` (fred_data.py: data dir, fred_macro import, load/value_on, chartkit inliner; chartkit.js: SVG lineChart pasted into each page) and `mortgage_quotes/` (append-only quotes.csv + points_analysis.py). Points are valued as PV(points + payments + payoff balance) vs Optimal Blue par, discounted at ZN-equiv (7y from DGS5/DGS10) and ZB-equiv (DGS20) yields; user flagged that the simple points/savings breakeven was wrong. pandas gotcha: `row.product` is Series.prod, use `row["product"]`.

**Why:** user asked for a shared package instead of duplicate downloaders ([[feedback_reuse_existing_code]]).
**How to apply:** add new FRED series to `fred_macro/catalog.py`, never a new downloader. Partial runs rewrite `manifest.json` with only those series. Gaps: ICE BofA spreads ~3 yrs only, no MOVE index on FRED, USNIM ended 2020. YouTube captions: youtube-transcript-api works; old yt-dlp gets HTTP 429.

Related: [[project_brokers_schwab]], [[feedback_cross_device_paths]].
