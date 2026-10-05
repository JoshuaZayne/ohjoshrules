---
name: project_broker_bat_launchers
description: Per-broker startup/history/currency .bat launchers under Brokers/scripts/<broker>/
metadata: 
  node_type: memory
  type: project
  originSessionId: 25a8425d-6a76-4411-a108-b996aae65e52
---

Brokers repo has uniform Windows `.bat` launchers per broker under `scripts/<broker>/`, named
`<broker>_startup.bat` / `<broker>_history.bat` / `<broker>_currency.bat` (broker-prefixed,
function-named, unique). Built 2026-06-16 for IBKR, IronBeam, Schwab, TastyTrade, MooMoo.

All follow the gold-standard `scripts/schwab/run_daily_snapshot.bat` template: `%~dp0` drive-agnostic
root, preflight (docker compose v2 present + both compose files exist), liveness gate, single
`docker compose run/up`, `:LogRun` -> `logs/<broker>_<task>_runs.log`. **Docker-only, never host
SDK** (isolation policy). Exit codes: 1=Docker down, 2=TWS/OpenD down, 3=quota abort,
4=missing compose file, 5=no compose v2.

Per-broker specifics:
- IBKR/Schwab history reuse pre-existing `run_daily_snapshot.bat`/`run_weekly_snapshot.bat`; Schwab has NO currency bat (equities/ETFs only); `schwab_startup.bat` checks the 7-day token age but re-auth is host-only `login_flow.py`.
- IBKR `ibkr_currency.bat`: default runs fx-correlation refresh, `--puller` brings up live 11-pair FX stream.
- IronBeam history = `collect_historical_data.py` via the collector image; the old `IronBeam/IronBeam_API_Code/start_collector.bat` (host python, hardcoded D:\) is now a shim to `ironbeam_startup.bat`.
- MooMoo history/currency are quota-guarded (YES prompt) for the 300-pull HK-L1 cap [[project_moomoo_quota]]; needs OpenD gateway on host:11111.

cmd gotcha learned: unescaped `()` inside an `if`-block echo closes the block early ("... was unexpected at this time"). Keep parens out of echoes inside blocks. The pre-existing snapshot bats still carry this `(live)` bug.

Docs: per-broker docs/architecture/<Broker>_architecture.md (Launchers section), RUN_TRACKER.md
section 4b, docs/KNOWN_BUGS.md. (The old main-doc section 6.4.0 was removed when the architecture
doc was split: see [[project_broker_architecture_docs]].) Roadmap:
CodeMapping_Brain/content/roadmaps/2026-06-16_231244_broker-startup-bat-files.md.
Related: [[project_broker_architecture_docs]] [[project_schwab_run_tracker]] [[feedback_docker_startup]].
