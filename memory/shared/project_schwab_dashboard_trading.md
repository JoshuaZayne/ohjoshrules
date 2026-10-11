---
name: project_schwab_dashboard_trading
description: "Schwab dashboard Trade panel (stocks/ETFs/multi-leg options, preview then confirm) on branch Dimaskus_Surface_merge; not yet live-tested, needs Schwab re-auth"
metadata:
  node_type: memory
  type: project
  originSessionId: d8a60bec-334c-4db0-9f39-6d64b4103cad
  modified: 2026-10-11T09:22:32.940Z
---

Built 2026-10-11 on Brokers branch `Dimaskus_Surface_merge` (commit eeb3731f, worktree `F:\GitHub Repos\Brokers_merge`, NOT pushed). The branch is the trial merge of Surface_Local_Branch into refactor/platform-restructure-2026-08 (bb8a7aa0; no new test failures vs either parent).

Trade panel in the local dashboard (`schwab_dashboard.bat`, http://127.0.0.1:8765): host Flask only proxies `/api/trade/*`; `scripts/dashboard/trade_service.py` runs in the schwab-puller Docker image on 127.0.0.1:8766; `order_builder.py` is pure. User chose: stocks+ETFs+multi-leg options, preview-then-confirm with max-dollar cap (default $10k, `--max-order-usd`), polled quotes every 3 s. Futures view-only.

**Not yet verified live:** desktop Schwab token is stale (~/.schwab_token.json from 2026-08-11) and `.env.secrets` / `data/schwab/schwab_token.json` are not in the worktree. First live use: re-auth, run from a checkout that has secrets, preview first, tiny size.

**Why:** real-money order path; send-at-most-once rules (preview_id consumed before send, no retry, UNKNOWN on network error) are deliberate.

**How to apply:** do not route panel orders through `TraderAPI.place_order` (falls back to raw POST after any SDK error = duplicate risk) or `SchwabClient.execute_order` (`@retry_on_failure` x3, first account only, equity only). Tests run in Docker via a pytest run that must restore `Broker_architecture.md`/`docs/PROCESS_REGISTRY.md` afterwards (tests/conftest.py rewrites them). Roadmap: CodeMapping_Brain/content/roadmaps/2026-10-11_030617_schwab-dashboard-trading-panel.md. Related: [[project_brokers_schwab]], [[feedback_moomoo_isolation]], [[feedback_docker_startup]].

Charts/verification added 2026-10-11 (commit b087a9ce): `scripts/dashboard/bars.py` builds 1-30 min and 1-24 h bars from the 1m Parquet store, session-anchored (futures 17:00 CT, stocks 09:30 ET with Schwab 24/5 overnight from 20:00 ET belonging to the next day); tick charts from data/schwab/ticks are conflated level-one quote updates, not trades. Verify panel + `verify_bars.py` CLI. Do not reuse `historical_downloader.resample_1m_to_higher` for charts (UTC-anchored).
