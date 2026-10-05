---
name: project-brokers-market-data-pipeline
description: Active multi-phase roadmap to build recurring market-data pipelines across Schwab + IBKR + free-source events calendar + parquet/sqlite/postgres storage + Windows Task Scheduler orchestration. Started 2026-05-22.
metadata: 
  node_type: memory
  type: project
  originSessionId: ab66236a-9f95-4d9e-a400-58c56960bc39
---

Active roadmap building daily/weekly/monthly market-data collection across Schwab (equities + options), IBKR (equities + options + futures + forex), an events calendar (Yahoo earnings, FRED FOMC, BLS CPI/NFP, Treasury auctions), three storage backends (parquet/sqlite/postgres), and Windows Task Scheduler.

**Why:** seed question was "is there a best day of the week to buy options". The VIX-by-weekday proxy ships today (`~/repos/FinanceCode/analysis/dow_seasonality/vix_by_weekday.py`); the per-ticker IV answer requires accumulating chain snapshots since Schwab does not backfill historical option prices.

**How to apply:** before any work on broker market-data pipelines, equity OHLCV collectors, options-chain pulls, futures/forex pulls, events calendar collectors, or the Windows Task Scheduler orchestration -> read the roadmap and the 6 sub-plan docs first. Update the roadmap as steps complete; never spawn a parallel roadmap for the same scope.

**Roadmap:** `~/repos/CodeMapping_Brain/content/roadmaps/2026-05-22_224303_brokers-market-data-pipeline.md`

**Sub-plans (all under `~/repos/Brokers/docs/`):**
- `MARKET_DATA_PIPELINE_PLAN.md` (top-level)
- `TODO_storage.md` (parquet + sqlite + postgres)
- `TODO_schwab_pipeline.md` (80% wired; option chain wrapper missing)
- `TODO_ibkr_pipeline.md` (70% wired; canonical = broker_platform/brokers/ibkr/)
- `TODO_events_calendar.md` (net-new, free sources)
- `TODO_scheduler.md` (Task Scheduler + .bat + Docker liveness)

**Locked decisions (2026-05-22):**
- Build on top of `Surface_Local_Branch` (not rebase onto main)
- Watchlist scope = 50-100 symbols
- OPRA subscription confirmed active on IBKR
- Phase 2 (Schwab daily snapshot) starts first with stubbed storage
- Postgres deployment decision deferred to Phase 7

**Related:** [[feedback_moomoo_isolation]] (Docker+venv mandatory), [[feedback_docker_startup]], [[feedback_file_timestamps]], [[feedback_roadmap_default]].
