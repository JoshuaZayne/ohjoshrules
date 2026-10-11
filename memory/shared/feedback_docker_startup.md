---
name: always-start-docker-before-running-broker-code
description: Docker Desktop must be launched and confirmed running before any docker compose commands
metadata:
  node_type: memory
  type: feedback
  originSessionId: d8a60bec-334c-4db0-9f39-6d64b4103cad
  modified: 2026-10-11T08:04:46.916Z
---

Always check if Docker is running before attempting to build or launch any broker containers. If Docker is not running, launch Docker Desktop first and wait for the daemon to be ready before proceeding.

**Why:** User explicitly asked to make sure Docker is launched before trying to run any code. Docker Desktop on Windows takes 30-60+ seconds to initialize.

**How to apply:** Before any `docker compose` command, run `docker info` to check. If it fails, launch Docker Desktop via PowerShell and poll until `docker info` succeeds.

**Gotcha (fixed 2026-10-11):** if Docker Desktop never becomes ready (backend balloons to ~15 GB, `com.docker.diagnose` running, WSL `docker-desktop` distro Stopped), check `%APPDATA%\Docker\settings-store.json` for a UTF-8 BOM. The UI error reads `invalid character 'ï' looking for beginning of value`. Strip the first 3 bytes (EF BB BF); Docker is ready ~10 s later. A backup was left beside it as `settings-store.json.bom-backup_2026-10-11_020113`. The BOM was written 2026-08-09, almost certainly by PowerShell 5.1 `Set-Content/Out-File -Encoding utf8`, so never edit that file that way; use `[IO.File]::WriteAllText` with a no-BOM UTF8Encoding.
