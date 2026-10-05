---
name: project_schwab_run_tracker
description: "Brokers/RUN_TRACKER.md launch+resume hub; Schwab snapshot gotchas (revoked token, rebuild-after-edit)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 2a81be7d-ff9a-4949-b8c8-9ddedac0cd1a
---

`~/repos/Brokers/RUN_TRACKER.md` is the launch + session-resume hub for broker data jobs:
copy-paste PowerShell for Docker check, Schwab token-age check, re-auth, image rebuild,
dry-run/live daily+weekly snapshot, log tailing; plus a script map and an append-only run
history. Use it first when relaunching Brokers work.

Schwab daily data-getter = the `schwab-snapshot-daily` one-shot compose service ->
`scripts/schwab/snapshot_daily.py`. Launch (bypassing the buggy `run_daily_snapshot.bat`):
`docker compose -f docker/docker-compose.yml -f docker/docker-compose.schwab.yml run --rm schwab-snapshot-daily`.

Two recurring "it ran fine last week" causes, both hit on 2026-06-03:
1. Revoked/expired Schwab refresh token (7-day HARD wall, not rotatable; a new/partial auth
   revokes the prior one). Symptom: `invalid_grant: Refresh token is invalid, expired or revoked`.
   Fix: re-auth with `python scripts/schwab/login_flow.py` (real browser + local catch-server,
   no copy/paste; you do login+2FA+Allow+click-through the 127.0.0.1 "not secure" warning).
   DO NOT use `auto_auth.py` -- ARCHITECTURE.md 6.4 says Schwab bot detection BLOCKS WebDriver
   logins; it deletes the old token then fails, leaving none. Authoritative token file the
   container reads = `data/schwab/schwab_token.json` (NOT ~/.schwab_token.json, which is locked/empty).
   Health: `scripts/schwab/health_check.py` / `refresh_cron.py`.
2. Stale Docker image after editing code/watchlist/portfolios. The snapshot container bakes
   `broker_platform/config/portfolios.json` (and `data/universe/` is .dockerignored, so the
   canonical watchlist is NOT used; portfolios.json drives the pull). Symptom:
   `Unknown broker: 'schwab'. Available brokers: []`. Fix: rebuild the schwab image.

On 2026-06-03 added FUTU + 20 semis/tech/cyber/leveraged tickers to portfolios.json +
watchlist.json (now 582 resolved) and fixed the `equities`-key resolver in snapshot_daily.py.
Roadmap: `~/repos/CodeMapping_Brain/content/roadmaps/2026-06-03_002243_schwab-watchlist-futu-semis.md`.
Related: [[project_schwab_analytics_alerts]] [[project_brokers_market_data_pipeline]] [[feedback_moomoo_isolation]].
