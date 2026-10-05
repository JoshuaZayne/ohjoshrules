---
name: Always start Docker before running broker code
description: Docker Desktop must be launched and confirmed running before any docker compose commands
type: feedback
---

Always check if Docker is running before attempting to build or launch any broker containers. If Docker is not running, launch Docker Desktop first and wait for the daemon to be ready before proceeding.

**Why:** User explicitly asked to make sure Docker is launched before trying to run any code. Docker Desktop on Windows takes 30-60+ seconds to initialize.

**How to apply:** Before any `docker compose` command, run `docker info` to check. If it fails, launch Docker Desktop via PowerShell and poll until `docker info` succeeds.
