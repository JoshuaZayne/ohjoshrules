---
name: project-rusttos-complaints-recheck-pending-commit-2026-11-23
description: "RustTOS agent/complaints-recheck: two commits (every minute data down alert, chat summary) are STAGED and waiting for a restart of the desktop; where the script and messages are"
metadata:
  node_type: memory
  type: project
  originSessionId: 1357db99-9ad1-48ec-8f53-a505f7663727
  modified: 2026-11-23T17:09:03.809Z
---

As of 2026-11-23 10:20 MST, worktree `F:\GitHub Repos\RustTOS_agents\complaints-recheck`, branch
`agent/complaints-recheck`, head `1b9a80eb`, has FOUR files staged and nothing committed past that head:

1. `crates/rusttos-alerts/src/feed_watchdog.rs`, `feed_watchdog_tests.rs` and `bin/rusttos_feed_watchdog.rs`: the
   feed watchdog tells the owner by Telegram every 60 seconds while the Schwab or IBKR recorder is down, silent
   15:00 to 16:00 MST (measured in America/Phoenix on purpose), not limited by the day's cap. 31 watchdog tests pass.
2. `docs/worklog/2026-11-23_095202_chat_summary_grid_headers_data_alerts_shell_wedge.md`: the full record of that
   chat, with 18 numbered things still left to do.

**Why they wait:** the commit hook is a shell script and no shell could start on the desktop that day
([[reference-desktop-shell-hang-icmp-wedge]]). The owner chose to wait for a restart instead of committing with the
hook skipped ([[feedback-never-skip-commit-hook]]). A commit made with the hook skipped (`070d6699`) was taken back.

**How to apply, after the desktop has been restarted:**
1. Run `C:\Users\ohjos\Machine\rusttos_pending_commit_complaints_recheck\commit_after_restart.ps1`. It checks the
   branch, the head and the four staged files, then makes the two commits through the hook and stops at anything
   unexpected. Both messages there already passed `repo-tools validate-commit-message` by hand.
2. If the staging area was lost, `staged_difference.patch` in that folder holds all four files' changes.
3. Enable the task "RustTOS status page refresh" again (it was disabled during the hang).
4. The alert is NOT in service until the watchdog is rebuilt and copied over
   `F:\GitHub Repos\RustTOS\data\bin\rusttos-feed-watchdog-background.exe` and that program restarted; the owner
   has not yet said to do that.
5. The branch is 12 behind main and none of its commits are pushed.

Delete this memory once the two commits have landed. Related: [[project_rusttos]],
[[feedback-no-unbounded-waits-stoppable-code]].
