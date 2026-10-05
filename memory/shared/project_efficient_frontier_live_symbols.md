---
name: project_efficient_frontier_live_symbols
description: Active roadmap to add live ticker ingestion + solver upgrades to the Efficient_Frontier repo
metadata: 
  node_type: memory
  type: project
  originSessionId: f84f1b88-7b0f-4ad1-9b6a-5715f1c98638
  modified: 2026-08-18T10:05:23.289Z
---

Roadmap: `~/repos/CodeMapping_Brain/content/roadmaps/2026-08-18_013636_efficient-frontier-live-symbols.md`.

Repo `~/repos/Efficient_Frontier` (mirrored at `FinanceCode/Efficient_Frontier/`) now has `DataLoader.load_symbols(symbols, source='auto', cov_estimator='sample'|'sample_unbiased'|'ledoit_wolf', annualize=True)` as the one-call entry point for feeding it new tickers, no manual Excel layout required.

**Why:** user asked how to greatly improve the tool for new symbols, then said to also pull from their existing Brokers/Schwab parquet data rather than only yfinance.

**How to apply:** `source='auto'` tries `~/repos/Brokers/data/parquet/ohlcv_history/timeframe=<tf>/<SYMBOL>.parquet` first (612 Schwab-sourced symbols already on disk, free, no network, plain file I/O so [[feedback_moomoo_isolation]]'s Docker+venv broker rule does not apply to reading it), falling back to a live yfinance pull per-symbol for anything not tracked there. `device_paths.py` gained `BROKERS_PARQUET_ROOT` + `BROKERS_REPO_ROOT`. `PortfolioOptimizer._validate_inputs` now warns on ill-conditioned covariance (points at `cov_estimator='ledoit_wolf'`).

A real 67-symbol basket the user supplied (blue chips + REITs/BDCs/CEFs/covered-call ETFs) surfaced 2 real bugs same-day, both fixed: yfinance's default 1-month lookback caused zero date-overlap against the [stale] broker parquet store, and a `datetime64[us]` vs `datetime64[s]` index mismatch on concat.

`schwab_topup(symbols)` / `load_symbols(..., schwab_topup=True)` shells out (subprocess, never an import) to the Brokers repo's `schwab_catch_history.bat symbols "A,B,C"` to pull genuinely-new tickers via a real Schwab login before falling back to yfinance. That bat mode was built by the `broker-isolation-enforcer` agent (keeps Docker+venv isolation authoritative), which caught cmd.exe's bare-comma argument-splitting bug (`symbols AAPL,MSFT` unquoted silently drops MSFT); fixed on both sides, independently reverified by me that a second interpolation level (the composed `docker compose ... !SYMARG!` line) does NOT re-split on commas.

Shipped and tested 2026-08-18, 202/202 tests passing (24 new total across the day). Deferred: replacing the per-point SLSQP frontier loop with a closed-form solve (performance only, not blocking).

Live run completed same day. Found + fixed a real bug in my own `schwab_topup()`: passing the quoted symbol list as a subprocess list arg let `list2cmdline` escape the embedded `"` to `\"`, which cmd.exe's batch tokenizer chokes on; fixed via `shell=True` with one flat command string. Separately, the Schwab OAuth token was stale and `login_flow.py`'s catch-server hit the documented ~30s code-expiry race (`invalid_grant`); recovered via the repo's own `exchange_token.py <redirect_url>` fallback (instant, non-interactive exchange). Found a real pre-existing bug in the Brokers repo's `scripts/schwab/historical_downloader.py::get_sector()`: naive `startswith()` prefix matching against futures-root strings misclassifies the equity ticker CLX (Clorox) as an Energy Futures symbol (collides with "CL" = crude oil root) and silently drops it with zero bars, no error. Not fixed (shared classification path, out of scope, documented in the roadmap for whoever picks it up). Net result: 67-symbol basket's broker-parquet coverage went 27->64/67 (FOG and AFT confirmed missing on both Schwab and yfinance independently, likely bad/untracked tickers).

Fixed the CLX root cause in `historical_downloader.py::build_symbol_list()`/`get_sector()`: naive `startswith(futures_root)` matching, tightened to require a genuine month-code+year suffix via shared `_matches_futures_root()`. Would also have broken RBLX/PLD/NGL/ESI/SIL if ever passed explicitly. **Gotcha**: `scripts/schwab/` isn't bind-mounted in the compose file, code is baked into the image at build time - edits need `docker compose build schwab-dl-history` before they take effect (rebuild was still running 20+ min in, not yet reverified live).

Added `load_symbols(align='pairwise')`: each mean/covariance entry uses a symbol's own full history / pairwise-complete overlap instead of truncating everyone to the newest fund's inception (huge for a basket spanning 2.5-25 years). Not compatible with `cov_estimator='ledoit_wolf'`. Added `_nearest_psd()` eigenvalue-clipping repair since pairwise covariance isn't guaranteed PSD.

Added real bad-print/ticker-reuse detection (`DataLoader.MAX_ABS_LOG_RETURN=1.6`, any single-day log return over ~5x gets excluded + reported in `meta['suspect_symbols']`, falls through to next source). Caught 3 confirmed real cases on the live basket: **WDTE** ($0.0001 for 18yr then $44.11 overnight, 441,099% "return" - clear stale-ticker artifact), **MAIN** (pre-2007 data predates the actual Main Street Capital IPO), **DAL** (pre-2007 data predates Delta's bankruptcy reorganization).

Full basket now actually optimizes: `load_symbols(source='auto', align='pairwise', cov_estimator='sample_unbiased', annualize=True)` -> 65/67 loaded, `PortfolioOptimizer` long-only MVP/tangent both sane, 100-point frontier, plot saved. 217/217 tests passing (32 new this session). Known open caveat: WDTE's short clean history (~549 days, no drawdown yet) dominates tangent-portfolio weight (79%) - the well-known short-history-overfitting problem, not yet mitigated (ledoit_wolf unavailable in pairwise mode; a min-history filter or per-asset weight cap would be the next fix if the user wants it automatic).
