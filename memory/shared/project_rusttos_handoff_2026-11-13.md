---
name: project-rusttos-handoff-2026-11-13
description: "RustTOS state and working rules at the 2026-11-13 restart; where the handoff, agents log and owner questions files live"
metadata:
  node_type: memory
  type: project
  originSessionId: 2bfbbc04-5c73-44f0-81de-78c30076bbf2
  modified: 2026-11-14T09:41:05.119Z
---

RustTOS build driven by one round driver session with Opus builders. At the stop main was 6b68160 (round au); round av (options pricing core, 38dbf04 on agent/final-merge-3) hung in its chart tests and must be rerun first. Before a computer restart on 2026-11-13 (about 22:00 MST) the whole state was written to `F:\GitHub Repos\RustTOS_agents\HANDOFF_restart_2026-11-13_214903.md`; read it first when resuming. The running record is `F:\GitHub Repos\RustTOS_agents\AGENT_LOG_2026-11-07_235708.md`; open questions for the user are in `F:\GitHub Repos\RustTOS_agents\QUESTIONS_FOR_OWNER_at_2026-11-13_1000.md`; the gap analysis and phases are Plan 2 in the repo at `docs/todo/2026-11-13_014831_plan_2_gap_analysis_five_platforms.md`.

**Update 2026-11-13 23:22 MST (new session after the restart):** round av was rerun and passed (71,103 passed, 0 failed; the chart hang did not come back). Local main and the trunk are 38dbf04, tag main-2026-11-13-av. The push to GitHub FAILED and GitHub main was still 6b68160: that session ran in Windows session 0, where the stored GitHub sign in (Windows credential list, gh) is not reachable; the user must push from a desktop terminal or sign in. Check `git rev-parse origin/main` before assuming it is pushed. IB Gateway was not logged in after the restart, so the weekend fetch was not restarted. Next work is the handoff file's section 6 (lane A: finish agent/chart-speed-2; lane B: broker reconnect handling).

**Update 2026-11-14 00:55 MST:** round aw landed locally: main and the trunk are 3068315 (tag main-2026-11-14-aw), the IBKR reconnect reconcile pass (desk side only, no screen yet). Still not on GitHub (origin/main 6b68160) until the user adds the new SSH key `~/.ssh/id_ed25519_github.pub` to GitHub. The user asked to start Plan 2 phase 2: lane B `agent/day-loss-history` does the phase 1 leftovers (day loss wiring, account history lock) then phase 2 item 2 readers (account figures, confirm figures, order history). Phase 1 is built but not "done": nothing is proven on a paper Gateway and the risk and reconnect screens are not built.

**Update 2026-11-14 02:45 MST:** rounds ax (f63e070: chart speed second half, deferred extra windows) and ay (2acd1fe: day loss from the account history store, account figures, confirm figures, order history reader) landed locally; tag main-2026-11-14-ay. origin/main still 6b68160 (rounds av to ay unpushed). Nothing from these is installed (chart on screen is round au). Running: lane A `agent/chart-fixes` (the owner's seven chart fixes), lane B `agent/order-chains-templates` (Plan 2 phase 2 item 1: size calculator, full templates, order chains). The round script is copied from `final-merge-3/data/reports/round_av_2026-11-13_213505/run_checks.sh` with the folder name replaced; merges use `repo-tools commit-report --merge BRANCH` and its FILL IN lines must be filled.

**Why:** the user asked for a documented stopping point and a way to pick up where the work left off.

**How to apply:** working rules the user set on 2026-11-12 and 13, after drive F filled and a memory stop: at most two builders (lane A chart and order screens, lane B behind the screen), 4 build jobs each; a round builds at 8 jobs, holds `RustTOS_agents\.round_running` and runs with `memory_watch.sh`; builders check that marker, free memory (20 GB) and free disk (40 GB) before every cargo command and commit after every finished item; clear a builder's `target` folder after its round; installs and chart rebuilds only on the user's yes; no order is sent, changed or canceled by an agent; no stop on the user's euro position (their instruction). See also [[project_rusttos_round_driver_and_tracker]] and [[project_rusttos]].
