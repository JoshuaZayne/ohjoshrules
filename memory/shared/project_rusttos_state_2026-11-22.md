---
name: project_rusttos_state_2026-11-22
description: "RustTOS as of 2026-11-22 03:05 MST: main green at 71,501 tests, chain_route merged, F: cleanup gave back 139 GB, todo backlog still barely started"
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
3c. MERGED 2026-11-22 02:54 MST. The chain_route work is on main as merge commit bcdb444f, pushed, and the
   branch is deleted locally and on origin. `cargo test --workspace -j 8` passed WHOLE: 132 targets, 71,501
   tests, 0 failed, 0 ignored, 15m29s (02:38:32 to 02:54:01 MST). `git diff 1e429224 main` is empty, so the tree
   that passed is exactly main's tree. Decisions high water is now D0483.
3d. TWO CHECKS that will bite again, both hit during this merge:
   1. `data_folder_joins` is a RATCHET at `MOST_DATA_FOLDER_JOINS = 921` in crates/repo-tools. Any new
      `join("orders")` or other literal data folder name raises the count and fails the suite. The number may
      NEVER be raised. Use `rusttos_core::data_layout::resolve_known(data, Path::new("orders"))`, or in
      rusttos-ibkr `crate::order_ledger::orders_folder(data)`.
   2. `independence.rs` FORBIDDEN_EXTERNAL_REFERENCES bans naming the personal repo folder layout, the iCloud
      sync folder, the assistant memory folder and other repos, in ANY file including docs. My own plan file
      broke this and left main red from 7ef9c079 until 1e429224. Never write this machine's absolute paths into
      a RustTOS doc; describe the location instead.
4. Today's plan and the session worklog are committed on main as 7ef9c079, the cleanup record as bfce1f0c, the
   merge as bcdb444f, all pushed:
   `docs/todo/2026-11-22_020123_branches_to_main_and_todo_plan.md` and
   `docs/worklog/2026-11-22_020123_branches-to-main-survey.md`. The plan's section 4 holds the order of work.
5. Of the ten files in `docs/todo/`, the live one is `2026-11-20_034343_touch_edge_search_todo.md`. The complaints
   tracker `2026-11-11_020723_user_complaints_tracker.md` has statuses 11 days and 59 commits stale, so re-verify
   each of its 23 items against main before building any of them. The three files from 2026-11-06, 11-07 and 11-10
   are history: every builder branch they name is gone from the remote, meaning merged and deleted.
6. F: CLEANUP TOTAL for 2026-11-22: 166.4 GB free to 305 GB free, 83 percent to 68 percent full, 139 GB back.
   Two parts: 95 GB from the agent worktrees (item 3) and 51.7 GB from Ollama. Ollama went 59.81 GB to 8.07 GB:
   `ollama rm` cleared qwen3.6:latest and qwen2.5:14b (29.4 GB, both manifest indexes and blobs), then a hidden
   `library/llamacpp/3899b1c0...` manifest that `ollama list` cannot see had to be removed BY HAND plus a sweep
   of blobs no manifest referenced (22.30 GB: a 21.46 GB model and a 0.84 GB vision projector). KEPT and verified
   with `ollama show`: gemma4:12b and qwen3-embedding:0.6b. The 9 manifest JSONs were backed up first to
   `Notes\OllamaManifestBackup_2026-11-22_022341`. `RustTOS/target` (9.8 GB) was kept on purpose.
6a. Still on F: and untouched, none of it regenerable: Media_Archive_2019 313.72 GB, the iCloud sync folder
   92.88 GB, PhotoLibrary 63.22 GB, SCHOOOL_RAID0_ 34.06 GB, Josh's Stuff 14.41 GB.
6b. THE TODO BACKLOG IS STILL BARELY STARTED. Of the plan's section 4 only the chain route is done. Not started:
   re-verify the 23 items of the 2026-11-11 complaints tracker against main (statuses now 11 days and 60 plus
   commits stale); the touch edge search NEXT items, cheapest first being Benjamini-Hochberg false discovery
   control over the coin shares, which needs no broker and no new data; the Desk Board status page refresh that
   [[feedback_status_page_after_merges]] requires after today's merge.
7. Questions still unanswered by the owner: may `backtest-studio-ml-mcmc`, `sessions-07-to-09-schwab-dialogs-focus`
   and `ssh-ascii-watchdog-and-backtest-fix` be deleted now that their commits are all in main; start the IBKR
   recorder with Windows; may `rusttos_ibkr_fop_curve` run against live IB Gateway on port 4001 and at what time.

8. SESSION OF 2026-11-22 11:20 to 11:50 MST, what changed. Main is now 879b24a9, pushed, Desk Board refreshed.
   1. THE BIG FINDING: IB Gateway had been LOGGED OUT since 2026-11-17 04:45 UTC. Five days in which this desktop
      recorded NOTHING from IBKR: no quotes, no depth, no trade prints, no backfill. Evidence: the gateway clock's
      7,046 consecutive closed checks, the recorder stuck on "waiting for IB Gateway (no answer on its port)", a
      backfill queue of 9,992 jobs and 1,162 open holes. There is NO auto login. This one cause has lost more data
      than every other cause together. Schwab is down too since 2026-11-16: its token refresh task fails with
      0x8007010B and the recorder says "network: expected value at line 1 column 1".
   2. The laptop's 6A, 6E and 6J depth is now HERE. Days 2026-11-19, 11-20 and 11-21 from release depth-2026-11:
      79 files, 2,938,698 rows, every file SHA-256 verified twice (staging and in place) against its day's
      manifest.csv, 0 bad, nothing overwritten. Before this, 6A and 6J depth existed nowhere but the laptop.
   3. The 708 MB "pull from laptop" sitting in a dated staging folder on C: is 100 percent REDUNDANT: every one of
      its files in curve, spot_proxy, stock_history, forex_rates, margins, ibkr_backfill and ibkr_ticks is already
      in the data folder (ibkr_ticks matched exactly, 2,062 files both sides). It is safe to delete, which would
      give C: 708 MB back. Not deleted; waiting on the owner.
   4. Advisor login measured: NO US futures market data. See [[reference-ibkr-logins-and-subscriptions]], which is
      the durable note. Three login env files were created outside the repo with owner-only ACLs.
   5. Done from section 4 of the plan: the Desk Board refresh (item 3) and a new repo doc
      docs/data_streaming_services.md mapping every streaming service per broker, per client id and per login.
      Still NOT started: the 23 complaints tracker items, and Benjamini-Hochberg false discovery control.

Related: [[project_rusttos]], [[project_rusttos_round_driver_and_tracker]], [[project_rusttos_handoff_2026-11-13]],
[[feedback_status_page_after_merges]], [[feedback_commit_details]].
