---
name: project_schwab_catch_bats
description: Schwab repo-root one-click catch-server bats for snapshot/history/alerts/PnL + host helpers
metadata: 
  node_type: memory
  type: project
  originSessionId: b95a972e-2b84-45ce-87ce-a886c2401606
---

Four double-clickable launchers at `~/repos/Brokers/` root, all built off the
catch-server login (`scripts/schwab/login_flow.py`). Each guards Docker + token
and re-auths ONLY if the token is missing/stale (> 6.5 days), then runs its job.
Broker code stays in Docker (service `schwab-puller`, `--entrypoint python -m
scripts.schwab.<mod>`, which mounts `../data/schwab` read-write so files land on
host); only the OAuth login + pure-pandas alert/PnL math run on host.

- `schwab_catch_launch.bat` : auth-if-stale -> dry-run -> live daily snapshot. Args: `rebuild` `weekly` `history` `auth`.
- `schwab_catch_history.bat` : auth-if-stale -> `historical_downloader --skip-existing`. Arg: `full`.
- `schwab_catch_alerts.bat` : auth -> `pull_all` (writes accounts snapshot = holdings) -> `print_holdings.py` -> `get_history --interval 1m` for held -> `run_alerts.py` quant-pivot 3rd-band 4h (toast/telegram/sms, dedup). Arg: `quiet` (toast only).
- `schwab_catch_pnl.bat` : auth -> `pull_transactions` -> `account_report` (open P/L, Docker) -> `pnl_report.py` (realized FIFO, host). Args: `noupdate` `years N`.
- `schwab_catch_futures_alerts.bat` : HOST-only `run_alerts` quant pivots (3rd band 4h) over ALL futures contracts (print_futures.py: roots + contract months with 1m data) UNION active holdings, re-armed each 4h period. Args: `quiet` `roots` `hardreset` `refresh`. Verified: 333 symbols, 46s.

**Logging (all 5 bats):** each run calls `scripts/schwab/log_hook.ps1` (the per-run hook) which prunes `schwab_catch_*.log` older than 5 days (scoped so it never touches service logs like schwab_puller.log) and returns a timestamped log path `logs/schwab/<bat>_YYYY-MM-DD_HHMMSS.log`. The bat runs its body in a `:_run` subroutine with output redirected to that log, then `type`s it to console (no pipe -> goto/labels work; a pipe-tee BROKE labels with "cannot find the batch label"). Time tracking via `:_tstart`/`:_done` ([DateTimeOffset]::UtcNow.ToUnixTimeSeconds, single-quote for /f) prints start/end/elapsed. Each step captures its exact exit code (`set "_rc=!errorlevel!"`); on failure `:_err` logs `[ERROR] step '<name>' failed (exit code N)` + an actionable `[HINT]` + the log path, and every run ends with a scannable `[RESULT] OK|FAILED rc=N (elapsed Ns)`. Verified on all 5: history stopped mid-run -> `[WARN] step 'Historical backfill' (exit code 137)` + hint, then `[RESULT] OK (60s)`.

New host-safe helpers: `scripts/schwab/print_holdings.py` (comma list of held
symbols from latest `data/schwab/accounts/accounts_*.json`, filters option OCC
symbols) and `scripts/schwab/pnl_report.py` (realized FIFO PnL from
`data/schwab/transactions/*.csv` via `pnl.realized_events`, bucketed by
day/week/month/year AND asset class equity/option/future/forex/other, plus
open/unrealized by asset class from the accounts snapshot; classify() maps
Schwab assetType + symbol patterns; writes `pnl_realized.json`; terminal twin of
notebooks/schwab/06_pnl.ipynb). Verified total realized -$54,202.68.

**Why:** user wanted "just launch it and it works" entry points off the catch
service, then chain history + holdings quant-pivot alerts + PnL.

**How to apply:** for any Schwab run, prefer these bats. Gotcha: `run_alerts`
builds 4h bands from 1m history, so the alerts bat MUST pull 1m first or it says
"no intraday data". Also fixed a branch bug where `ironbeam_app` was misplaced
under `networks:` in `docker/docker-compose.yml` (blocked all compose builds);
moved it into `services:`. Realized-PnL smoke run: 3949 closing events,
total -$54,202.68. Related: [[project_schwab_run_tracker]],
[[project_schwab_analytics_alerts]], [[project_broker_bat_launchers]].
Roadmap: CodeMapping_Brain/content/roadmaps/2026-06-16_233646_schwab-catch-launchers-alerts-pnl.md
