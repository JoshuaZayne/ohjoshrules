---
name: project_rusttos_state_2026-11-22
description: "RustTOS as of 2026-11-22 02:15 MST: every branch already in main, F: cleanup gave back 95 GB, and the chain_route work the cleanup nearly destroyed"
metadata:
  node_type: memory
  type: project
  originSessionId: 2dc7a551-6dd9-4b58-8eb7-2b8ebee5c886
  modified: 2026-11-22T09:04:58.390Z
---

RustTOS state measured 2026-11-22 01:58 to 02:01 MST (`git fetch --all`, `git rev-list --count main..<ref>` over all
70 refs, in `F:\GitHub Repos\RustTOS`).

1. The branch consolidation the owner asked for is DONE, not pending. After a `git pull --ff-only` that moved local
   `main` from 8a9b9eb9 to aaf2b07a, every local and remote branch is contained in `main` except two, and both say in
   their own commit subject they are not meant for main: `agent/option-history-test` (1 commit, 2026-11-12) and
   `origin/agent/chart-speed-2` (1 commit, 2026-11-13). Do not merge those two.
2. The trap: local `main` was 59 commits BEHIND `origin/main`, which made three already merged branches
   (`agent/touch-lab` 53, `agent/device-seal-pull` 26, `agent/backtest-exits` 2) look unmerged. Always pull `main`
   before judging any RustTOS branch as having unmerged work, or you will create empty merge commits.
3. DONE 2026-11-22 02:15 MST: the 29 agent worktrees were removed and 25 local branches deleted. `F:` went from
   166.4 GB free to 261 GB, 83 percent full to 73 percent, measured with `df -h /f`. Nearly all of it was one
   folder: `RustTOS_agents/final-merge-3/target` held 93.3 GB. `RustTOS/target` (9.8 GB) was KEPT on purpose, so
   the next `cargo test` is not a full rebuild. Only `F:\GitHub Repos\RustTOS` is a worktree now, and 6 local
   branches remain. The 59 agent coordination records under `RustTOS_agents\` (agent_catalog.jsonl, AGENT_LOG,
   AGENT_RULES history, GPU lock queues) were NOT touched. No remote branch was deleted.
3a. THE LESSON, worth more than the disk: one worktree, `chain-route-flaky-tests`, held 1,290 added lines across 12
   files that were on no branch and in no commit anywhere, and removing it would have destroyed them. ALWAYS run
   `git status` in every worktree before removing any of them, and never pass `--force` to `git worktree remove`.
   That work was the open "route seam" of the order chains work of 2026-11-14: `chain_route.rs` (298 lines),
   `chain_route_tests.rs` (345), `paper_route_chain_tests.rs` (372), `LiveOrderRoute::submit_chain`, and decisions
   D0380 and D0381. `main` has `order_chains.rs` (a chain's shape) but nothing that carries a chain to a route, so
   no screen could send one. Saved as commit 3a84504c on `agent/chain-route-flaky-tests` and pushed. NEXT: run
   `cargo test` on it, then merge to main. It cannot send real money orders; `submit_chain` refuses by default.
3b. `git branch -d` refuses a branch that is behind its own upstream even when every commit is in main, which is
   what happened to `agent/touch-lab`. Check both tips with `git merge-base --is-ancestor <tip> main` and only then
   use `-D`. Do not reach for `-D` before that check.
4. Today's plan and the session worklog are committed on main as 7ef9c079, with the cleanup recorded in the
   plan's section 6 as bfce1f0c, both pushed:
   `docs/todo/2026-11-22_020123_branches_to_main_and_todo_plan.md` and
   `docs/worklog/2026-11-22_020123_branches-to-main-survey.md`. The plan's section 4 holds the order of work.
5. Of the ten files in `docs/todo/`, the live one is `2026-11-20_034343_touch_edge_search_todo.md`. The complaints
   tracker `2026-11-11_020723_user_complaints_tracker.md` has statuses 11 days and 59 commits stale, so re-verify
   each of its 23 items against main before building any of them. The three files from 2026-11-06, 11-07 and 11-10
   are history: every builder branch they name is gone from the remote, meaning merged and deleted.
6. Not run on 2026-11-22: `cargo test`, any build, clippy. Still on `F:` and deliberately untouched, because none
   of it is regenerable: Media_Archive_2019 313.72 GB, iCloudDrive 92.88 GB, PhotoLibrary 63.22 GB, OllamaModels
   59.81 GB, SCHOOOL_RAID0_ 34.06 GB, Josh's Stuff 14.41 GB (sizes as of the 2026-11-21 inventory, not
   re-measured). Of those only OllamaModels is replaceable by downloading again.
7. Questions still unanswered by the owner: may `backtest-studio-ml-mcmc`, `sessions-07-to-09-schwab-dialogs-focus`
   and `ssh-ascii-watchdog-and-backtest-fix` be deleted now that their commits are all in main; start the IBKR
   recorder with Windows; may `rusttos_ibkr_fop_curve` run against live IB Gateway on port 4001 and at what time.

Related: [[project_rusttos]], [[project_rusttos_round_driver_and_tracker]], [[project_rusttos_handoff_2026-11-13]],
[[feedback_status_page_after_merges]], [[feedback_commit_details]].
