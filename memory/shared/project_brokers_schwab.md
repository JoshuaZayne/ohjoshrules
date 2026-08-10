---
name: project_brokers_schwab
description: "Brokers repo (multi-broker trading platform) — where the Schwab auth/data code and its authoritative runbook live, and the .env placeholder gotcha"
metadata: 
  node_type: memory
  type: project
  originSessionId: b4172c67-98c7-4893-b78b-d46ae378a41f
  modified: 2026-08-10T04:19:19.705Z
---

Repo: `F:\GitHub Repos\Brokers` (private, `JoshuaZayne/Brokers`). Multi-broker platform (Schwab, IBKR, IronBeam, TastyTrade, MooMoo, etc.) with one CLI entry point `run.py`.

**The authoritative Schwab runbook is `ARCHITECTURE.md` Section 11, "Schwab OAuth & Trader API"** (~line 7445, subsections 11.1 to 11.13). It covers the auth chain, the error catalog, the diagnostic ladder (11.11), and the proven end-to-end data flow (11.12.1). Look there first for anything Schwab, not at `broker_platform/brokers/schwab/API_SETUP_SCHWAB.txt`, which is the older generic guide.

Schwab auth entry point is **`scripts/schwab/auto_auth.py`** (Selenium + persistent Edge profile, handles 2FA), not the CLI. `reauth.py` deletes the stale token; `refresh_cron.py` + `install_refresh_task.ps1` run the daily refresh task. Token lands at `~/.schwab_token.json` in nested schwab-py format and dies after 7 days.

**`.env` gotcha:** `.env` is git-tracked and holds only `${PLACEHOLDER}` references; the real credentials live in gitignored `.env.secrets`. A short "value length" in `.env` means a placeholder, not a truncated key. Do not conclude credentials are malformed from `.env` alone.

**Local checkouts drift badly.** On 2026-08-09 the F: checkout was 83 commits behind `origin/main` and was missing the entire Schwab auth subsystem. Always `git fetch` and compare against origin before concluding code does not exist. Note `.env` being tracked means a pull can clobber local credentials, so stash or back it up first.

**The daily token refresh task is BROKEN (found 2026-08-09).** Scheduled task
`BrokersPlatform-SchwabTokenRefresh` runs
`anaconda3\python.exe "D:\code\brokers\scripts\schwab\refresh_cron.py"` with working
directory `D:\code\brokers` — the **USB stick path, which is not mounted**. Last run
2026-08-08 15:00 failed with `2147942667` (0x8007010B, "The directory name is
invalid"). This is why tokens keep going stale. Fix = re-point the task at
`F:\GitHub Repos\Brokers` (or re-run `install_refresh_task.ps1` from the current
checkout). Same class of breakage as [[project_f_drive_github_repos_reorg]].
As of 2026-08-09 there is no live token: only `~/.schwab_token.json.old`
(808 bytes, 17-Mar-26) remains, so a fresh `auto_auth.py` run is required.

**SECOND root cause of stale tokens, found + FIXED 2026-08-10.** `auto_auth.py`
wrote the token file by copying Schwab's raw `/token` response verbatim. That
response has `expires_in` (a duration) but **no `expires_at`** (an absolute
epoch). authlib, under schwab-py, decides whether to refresh by comparing
`expires_at` to the clock — with the key absent it never refreshes and keeps
resending a dead access token. Symptom looks like a credentials failure:
everything works for exactly 30 minutes, then every endpoint returns HTTP 401
`"detail": "Client not authorized"` until someone re-runs interactive OAuth.
Fix landed in `auto_auth.py` (derives `expires_at = now + expires_in`). To
repair an existing token file, add `expires_at` to its `token` dict; a past
value is fine and correctly triggers the refresh.

**Schwab market data coverage is confirmed 100%** (probed live 2026-08-10 via
`scripts/schwab/probe_symbols.py`): all 9 currency futures (6A 6B 6C 6E 6J 6M
6N 6S 6Z), all 5 metals (GC SI HG PL PA), energy, index, rates, 28 FX spot
pairs, core ETFs. 46/46. Futures need `/ROOT + CME month code + 2-digit year`,
e.g. `/6EQ26`, `/GCQ26`.

Data lands in `data/<broker>/csv/` and `data/<broker>/json/` plus InfluxDB (org `trading`, bucket `market_raw`). **Parquet is not implemented** anywhere despite the CLI advertising `data export --format parquet`. As of 2026-08-09 `data/schwab/` held only `watchlists.json`; the ~4 GB under `data/ibkr/` is git-tracked and arrived with the clone rather than being collected locally.

Related: [[user_github_and_devices]], [[project_f_drive_github_repos_reorg]]
