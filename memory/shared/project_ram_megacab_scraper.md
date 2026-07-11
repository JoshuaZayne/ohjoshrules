---
name: project_ram_megacab_scraper
description: "Running & extending the RamMegaCabDataScrapper (nationwide RAM 2500/3500 Mega Cab Limited finder), incl. per-state coverage architecture and ops gotchas"
metadata: 
  node_type: memory
  type: project
  originSessionId: 468393e6-4a1e-4823-b465-9c38783b1153
---

Repo: `C:\Users\ohjos\repos\RamMegaCabDataScrapper` (GitHub JoshuaZayne/RamMegaCabDataScrapper). Docker-sandboxed scraper; hunts RAM 2500/3500 Mega Cab in Limited / Limited Longhorn nationwide, buckets results per state.

**Run it:** `run.bat` (or `run.bat -NoBoard` for raw stream; sets up live watchdog otherwise). Requires Docker Desktop running. `run.ps1` auto-runs `tangle.py` then docker build → plan → fetch → analyze. Full run with all sources is long (~1–2 hrs; 59 sources as of 2026-07-07). Outputs land in `output/` and are copied to Desktop (trucks.md/xlsx, alerts). Runs are NOT auto-committed.

**Literate code:** source of truth is `docs/src/**/*.md` (four-backtick ```python fence). Edit the `.md`, then `python tangle.py` regenerates the `.py`; `python tangle.py --check` guards drift; `python tools/litcode.py detangle` syncs back if you edited a `.py` directly. New sources: add `docs/src/scraper/sources/<name>.py.md` and register in `docs/src/scraper/sources/__init__.py.md` (both the import block AND `ALL_SOURCES`).

**Per-state coverage model:** every state (50 + DC) is a bucket (`config.TARGET_STATES`). `config.SEARCH_ZIPS` maps each state to its capital-city ZIP — the canonical way to parameterize a source per state. A source module exposes `SOURCE`, `SUPPORTS_HUMAN`, `URLS: list[UrlSpec]`, optional `API_URLS` (JSON/api tier). `UrlSpec(url, state_hint, city_hint)` — `state_hint` stamps the bucket when the card text has no parseable state. Fast/JSON sources (SUPPORTS_HUMAN=False) can cover all 51 states cheaply; browser-tier ones are capped by the 360s per-source budget so keep their URL counts modest.

**2026-07-07 improvement (lifted state coverage 5 → 28 states, 95 → 348 listings):** added 15 new per-state source modules + a smarter auto-accept. Best performers were all fast-tier: TrueCar/eBay/iSeeCars States, Craigslist Nationwide, AutoTempest States. Auto-accept knob `FILTER_ACCEPT_ON_HINT` (filter.py): recovers real Mega Cabs from a mega-cab-scoped search when no CONFLICTING cab appears in the listing's own text, flagged `cab-unconfirmed` (recovered 204). The old strict "mega cab unconfirmed" gate was the #1 killer of real trucks.

**The premium-source lever:** CarGurus/CarMax/Cars.com/AutoTrader, extra search engines, OEM locator, gov auctions fall through to the `unlocker` tier and return 0 UNLESS `UNLOCKER_*` (ZenRows/ScraperAPI/etc.) or `SCRAPER_PROXIES` are set in `.env`. Enabling these is the highest-leverage next step for the remaining zero-states (MI/NY/NJ/PA/VA/TN...).

**Ops gotcha:** stopping a run mid-build (`docker compose down` during image build) can corrupt the BuildKit layer cache — next build fails with `failed to prepare extraction snapshot ... parent snapshot ... does not exist`. Fix: `docker builder prune -af` (+ `docker rmi rammegacabdatascrapper`) then rebuild clean.

**2026-07-11 — cross-run HTML cache lever (`scraper/htmlcache.py`):** new fetch-time short-circuit. Every fetched search page is saved to `output/html_cache/<slug>.html` + `.meta.json` (kept, not deleted) and reused as next run's baseline. The single choke point is `extract_listings_from_html` (`sources/_common.py`): on entry it fuzzy-compares the new fetch to the cached page (stdlib `difflib` ratio over *visible text* — scripts/styles/tags stripped, so ad/session churn doesn't count; `SequenceMatcher(autojunk=False)` is REQUIRED or big pages score ~0.2). If ≥ `HTML_CACHE_SIMILARITY` (0.90) it reuses last run's already-enriched listings and refreshes ONLY price (cheap `iter_anchors`+`extract_price`) + availability (`availability.offline_flags_from_text` on fresh card text), skipping full field detection + embedded-JSON parse + downstream VDP enrichment. Env knobs (all in `config.py`): `HTML_CACHE_ENABLE=1`, `HTML_CACHE_SIMILARITY=0.90`, `HTML_CACHE_MAX_AGE_DAYS=4` (rolling window; pruned at fetch-phase start). Tradeoff: a non-price field change carries over from last run until the page drops <90% or hits the 4-day expiry; SPA/embedded-JSON listings keep cached price on a hit. Cache dir is gitignored. Log marker on a hit: `[cache-hit 0.9xx] ... reused N listing(s)`. Landed on branch `feat/html-cache-fuzzy-refresh` (tests: `tests/test_htmlcache.py`).
