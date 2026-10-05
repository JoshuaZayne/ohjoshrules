---
name: project_trailer_deals_scraper
description: "TrailerDealsScraper repo (sibling of the Ram scraper): nationwide gooseneck + bumper-pull trailers, 25-35 ft, 12k-30k GVWR, ranked vs fair value; TrailerTrader open JSON API is the backbone (~31 calls for the whole US), API-call ledger + TTL cache + caps"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9e031425-83af-46e6-b475-44dffae9f197
  modified: 2026-09-24T08:10:19.349Z
---

Built 2026-09-24 at `~/repos/TrailerDealsScraper` (sibling of [[project_ram_megacab_scraper]]; same 3-container Docker isolation, cascade fast>api>human>unlocker, bandit, method cache, url_health). Run with `GET-TRAILERS.bat`, output `output/trailers/latest/trailers.xlsx`. Roadmap: `CodeMapping_Brain/content/roadmaps/2026-09-24_013139_trailer-deals-scraper.md`.

Key facts (measured live, not guessed):
- TrailerTrader `https://backend.trailertrader.com/api/inventory` is open (no key), filters gvwr_min/max, length_min/max, pull_type server-side, per_page cap 350, valid sort only -createdAt / price / -price (bad sort returns HTML 200), state filter is `location=<Full State Name>` (`region=` is ignored), rate limit X-RateLimit-Limit 100. Records never carry `gvwr`; the band a row is returned in IS its GVWR. Records with no structured length (about half) are dropped by the length filter, so the plan sweeps GVWR bands with NO length filter (9 bands, ~31 calls total, ~8.6k rows) plus 2 recall sweeps (no GVWR filter).
- Detail URL is `https://trailertrader.com/<slug>--<token>.html`; token = base62 of the id, alphabet `a-z0-9A-Z`, digits reversed (decoded from the site JS, verified).
- Craigslist static search works for `search/tra?query=a|b|c`; more than ~10 terms or a dotted term like `17.5k` breaks it (HTTP 400 / lost results).
- CTT, TruckPaper, eBay HTML, RVTrader all 403 plain GETs; walled source is skipped unless unlocker / storage_state / TRAILER_TRY_WALLED.
- Host Python 3.14 segfaults writing parquet (pyarrow); Docker py3.12 is fine, so set SCRAPER_PARQUET=0 for host-side runs.

**Why:** user wants best trailer prices in every state while minimizing API calls, like the Ram scraper.
**How to apply:** when tuning, change `.env` TRAILER_* rather than code; API spend is in `output/state/api_usage.jsonl`; the Bash tool chokes on big heredocs containing apostrophes, use Write for files.
