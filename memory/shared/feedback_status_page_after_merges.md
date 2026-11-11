---
name: feedback_status_page_after_merges
description: "RustTOS: after any branch update or main merge, refresh the Desk Board status page (every sheet) and keep daily/weekly/monthly main change tracking"
metadata:
  node_type: memory
  type: feedback
  originSessionId: dc78bf08-c2c0-4db7-a104-fb644f183808
  modified: 2026-11-11T01:33:36.305Z
---

User, 2026-11-10 ~18:30 MST (RustTOS session): "once a branch gets updated or pushed to main that we need to updated: file:///F:/GitHub%20Repos/RustTOS_agents/status_page/index.html#branches and make sure every sheet is correct as much as possible, and we should track daily, weekly and monthly changes to the main code".

**Why:** the status page ("RustTOS Desk Board") is how the user sees branches, rounds, agents and what is on main; stale sheets mislead them.

**How to apply:**
1. Whenever a RustTOS branch is committed, handed off, merged, or main moves, bring the Desk Board up to date in the same turn: run `bash "F:/GitHub Repos/RustTOS_agents/status_page/refresh_page.sh"` (rebuilds branches.js from git and live.js from status files; the scheduled task "RustTOS status page refresh" also runs it every 5 minutes), then check every sheet (Branches, Work, Agents, Needs, Built, Safety, Data, Data repo, Commands, Gateway, Log) and fix any that is wrong or out of date for what changed. Most sheets other than Branches and live are hand kept (data.js, round.js, coordinator.js, agents.js, commands.js, datarepo.js); the coordinator session ohjos-aa owns most of them, so tell it what changed or edit only the part your own work covers.
2. Keep a daily, weekly and monthly record of changes to main (commits and merges landed, branches merged, files and lines added and removed, tests added) on the page, refreshed with the rest.
3. The status page folder is outside the repo (no Rust only rule there); never write into the RustTOS repo for it.

Related: [[project_rusttos]], [[feedback_commit_details]] (merge commit standard), [[feedback_read_clock_before_timestamps]].
