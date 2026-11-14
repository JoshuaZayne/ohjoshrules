---
name: project-rusttos-handoff-2026-11-13
description: "RustTOS state and working rules at the 2026-11-13 restart; where the handoff, agents log and owner questions files live"
metadata:
  node_type: memory
  type: project
  originSessionId: 2bfbbc04-5c73-44f0-81de-78c30076bbf2
  modified: 2026-11-14T06:23:44.457Z
---

RustTOS build driven by one round driver session with Opus builders. At the stop main was 6b68160 (round au); round av (options pricing core, 38dbf04 on agent/final-merge-3) hung in its chart tests and must be rerun first. Before a computer restart on 2026-11-13 (about 22:00 MST) the whole state was written to `F:\GitHub Repos\RustTOS_agents\HANDOFF_restart_2026-11-13_214903.md`; read it first when resuming. The running record is `F:\GitHub Repos\RustTOS_agents\AGENT_LOG_2026-11-07_235708.md`; open questions for the user are in `F:\GitHub Repos\RustTOS_agents\QUESTIONS_FOR_OWNER_at_2026-11-13_1000.md`; the gap analysis and phases are Plan 2 in the repo at `docs/todo/2026-11-13_014831_plan_2_gap_analysis_five_platforms.md`.

**Update 2026-11-13 23:22 MST (new session after the restart):** round av was rerun and passed (71,103 passed, 0 failed; the chart hang did not come back). Local main and the trunk are 38dbf04, tag main-2026-11-13-av. The push to GitHub FAILED and GitHub main was still 6b68160: that session ran in Windows session 0, where the stored GitHub sign in (Windows credential list, gh) is not reachable; the user must push from a desktop terminal or sign in. Check `git rev-parse origin/main` before assuming it is pushed. IB Gateway was not logged in after the restart, so the weekend fetch was not restarted. Next work is the handoff file's section 6 (lane A: finish agent/chart-speed-2; lane B: broker reconnect handling).

**Why:** the user asked for a documented stopping point and a way to pick up where the work left off.

**How to apply:** working rules the user set on 2026-11-12 and 13, after drive F filled and a memory stop: at most two builders (lane A chart and order screens, lane B behind the screen), 4 build jobs each; a round builds at 8 jobs, holds `RustTOS_agents\.round_running` and runs with `memory_watch.sh`; builders check that marker, free memory (20 GB) and free disk (40 GB) before every cargo command and commit after every finished item; clear a builder's `target` folder after its round; installs and chart rebuilds only on the user's yes; no order is sent, changed or canceled by an agent; no stop on the user's euro position (their instruction). See also [[project_rusttos_round_driver_and_tracker]] and [[project_rusttos]].
