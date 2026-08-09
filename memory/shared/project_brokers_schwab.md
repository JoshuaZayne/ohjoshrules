---
name: project_brokers_schwab
description: "Brokers repo (multi-broker trading platform) — where the Schwab auth/data code and its authoritative runbook live, and the .env placeholder gotcha"
metadata: 
  node_type: memory
  type: project
  originSessionId: b4172c67-98c7-4893-b78b-d46ae378a41f
  modified: 2026-08-09T08:49:35.383Z
---

Repo: `F:\GitHub Repos\Brokers` (private, `JoshuaZayne/Brokers`). Multi-broker platform (Schwab, IBKR, IronBeam, TastyTrade, MooMoo, etc.) with one CLI entry point `run.py`.

**The authoritative Schwab runbook is `ARCHITECTURE.md` Section 11, "Schwab OAuth & Trader API"** (~line 7445, subsections 11.1 to 11.13). It covers the auth chain, the error catalog, the diagnostic ladder (11.11), and the proven end-to-end data flow (11.12.1). Look there first for anything Schwab, not at `broker_platform/brokers/schwab/API_SETUP_SCHWAB.txt`, which is the older generic guide.

Schwab auth entry point is **`scripts/schwab/auto_auth.py`** (Selenium + persistent Edge profile, handles 2FA), not the CLI. `reauth.py` deletes the stale token; `refresh_cron.py` + `install_refresh_task.ps1` run the daily refresh task. Token lands at `~/.schwab_token.json` in nested schwab-py format and dies after 7 days.

**`.env` gotcha:** `.env` is git-tracked and holds only `${PLACEHOLDER}` references; the real credentials live in gitignored `.env.secrets`. A short "value length" in `.env` means a placeholder, not a truncated key. Do not conclude credentials are malformed from `.env` alone.

**Local checkouts drift badly.** On 2026-08-09 the F: checkout was 83 commits behind `origin/main` and was missing the entire Schwab auth subsystem. Always `git fetch` and compare against origin before concluding code does not exist. Note `.env` being tracked means a pull can clobber local credentials, so stash or back it up first.

Data lands in `data/<broker>/csv/` and `data/<broker>/json/` plus InfluxDB (org `trading`, bucket `market_raw`). **Parquet is not implemented** anywhere despite the CLI advertising `data export --format parquet`. As of 2026-08-09 `data/schwab/` held only `watchlists.json`; the ~4 GB under `data/ibkr/` is git-tracked and arrived with the clone rather than being collected locally.

Related: [[user_github_and_devices]], [[project_f_drive_github_repos_reorg]]
