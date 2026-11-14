---
name: feedback-builder-parallelism-and-resources
description: "Limit parallel build agents on the desktop: at most two, 4 build jobs each, watch disk and memory, clean build folders after each lands"
metadata:
  type: feedback
---

On 2026-11-12 (about 18:13 MST, RustTOS) the user said: "I think we need to pause blowing up my disk space, I think its could be slowing it down? so how can we focus on 1 agent at a time, finish its build out, upload it to main, then clean up my F and C drive of whatever extra stuff it was using?" Earlier that day six build agents plus a test round had filled drive F (a recorder lost 8,670 rows) and Claude Code's memory stop had killed two jobs. On 2026-11-13 (about 10:30 MST) the user approved going to two at once ("do it, so yes") after being shown which work does not overlap.

**Why:** each Rust build folder is 10 to 75 GB and several compiles at once exhaust memory; the user's live recorders share the same disk.

**How to apply:**
1. At most two build agents at once on this machine, in lanes that do not touch the same code; 4 build jobs each (the user's cap is 12 in total).
2. Before every build read free memory and free disk; stop with a checkpoint commit when low (20 GB memory, 40 GB disk were the levels used).
3. After a piece lands on main, delete its build folder before starting the next; keep the round's own build folder trimmed.
4. Never run a test round and agent builds at the same time without a marker the agents check.
5. Ask before raising the number of agents again. Interpretation (mine): this applies to any heavy compile work on the desktop, not only RustTOS.
