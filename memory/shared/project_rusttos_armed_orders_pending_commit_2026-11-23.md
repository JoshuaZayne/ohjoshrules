---
name: project-rusttos-armed-orders-pending-commit-2026-11-23
description: "RustTOS branch agent/armed-orders has 15 files of finished, tested work NOT committed as of 2026-11-23 10:00 MST; a ready script commits them after the desktop is rebooted"
metadata:
  node_type: memory
  type: project
  originSessionId: ae451a03-660d-476d-a38a-bc12d941c0f8
  modified: 2026-11-23T17:18:42.979Z
---

As of 2026-11-23 10:00 MST the worktree `F:\GitHub Repos\RustTOS_wt_jobrunner` (branch `agent/armed-orders`, last pushed commit `e7878b46`) holds 15 changed or new files that are tested but NOT committed: the first real fire's fixes, the new `rusttos-what-if` program, a worklog and the live todo.

**Why:** every Git Bash / MSYS shell on the desktop hung from about 07:31 MST that day, and the repo's commit hook is a shell shim, so `git commit` hangs. The user was asked and chose to WAIT FOR A REBOOT rather than commit with the hook skipped (see [[feedback-never-skip-commit-hook]]).

**How to apply:**
1. After the reboot, confirm a shell starts, then run `C:\Users\ohjos\RustTOS_targets\armed-orders_pending_commit_2026-11-23_095938\commit_after_reboot.ps1` in PowerShell. It makes three commits with the three prepared messages in that folder (all three already pass `repo-tools validate-commit-message`), adds only named files, and does not push.
2. Then `git push origin agent/armed-orders` and refresh the Desk Board ([[feedback_status_page_after_merges]]).
3. If `git status --short` in that worktree is already clean and `git log` shows "rusttos-what-if: what it takes to bring an average to a target", this is done: delete this memory.
4. The whole record of the chat is `docs/worklog/2026-11-23_095359_armed-orders-first-fire-and-what-if.md` in that worktree (section 11 is the list of what is left). The same folder also holds the full diff and copies of the new files in case the worktree is lost.

5. The same record with full desktop paths is in the code base map: `F:\GitHub Repos\CodeMapping_Brain\content\sessions\2026-11-23_101815_ae451a03_full-record-rusttos-armed-orders-first-fire-and-what-if.md` (written 2026-11-23 10:18 MST, left uncommitted there like the 2026-11-02 record). The scripts that built the Desktop commands page were copied out of the scratch folder to `F:\GitHub Repos\RustTOS\data\status_page\page_tools_2026-11-23`.

State of the real order when this was written: `trail_6a` fired 05:34:06 MST, filled 08:06:00 MST (2 /6AH27 at 0.6619), take profit order 39 (sell 2 at 0.6705) working; the armed watcher service was up on the fixed binary. Related: [[project_rusttos]], [[reference-desktop-shell-hang-icmp-wedge]].
