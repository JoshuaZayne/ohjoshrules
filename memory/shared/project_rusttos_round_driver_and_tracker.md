---
name: project_rusttos_round_driver_and_tracker
description: "RustTOS: session ohjos-1c drives merges to main (since 2026-11-11); complaints tracker, Plan 2, and where later complaints are logged"
metadata:
  type: project
---

On 2026-11-11 about 01:32 MST the user said in session ohjos-1c: "I stopped everything so you can control how all the merges, branches, agents finish and tie everything to your plan. I want you driving this build ... manage how they get merged on to main". The coordinator ohjos-aa stopped writing the round at 01:34 MST and handed over (file `F:\GitHub Repos\RustTOS_agents\HANDOFF_round_k_2026-11-11_011059.md`).

The user also asked (about 02:05 MST) that every complaint be documented and tied to the plan step that owns it. Tracker: `F:\GitHub Repos\RustTOS_agents\USER_COMPLAINTS_TRACKER_2026-11-11_020723.md` (21 complaints, steps A to P, each with what "addressed in full" means). It should move into the repo as `docs/todo/2026-11-11_020723_user_complaints_tracker.md` with the first branch after round k.

**Why:** the user wants one driver and wants no complaint lost between steps.

**How to apply:**
1. Before starting any step of the plan, open the tracker and work to its "addressed in full" lines; update statuses with evidence.
2. Standing rules still hold while driving: main moves only after the full round on the exact commit; merge messages from commit-report; refresh the status page after main moves ([[feedback_status_page_after_merges]]).
3. Tools built that night: `rusttos_round` (round planner, in repo-tools) and `rusttos-feed-watchdog` (alerts crate); both were merged into round k (agent/final-merge-3), not yet on main when this was written.
4. User feedback that night: "stop guessing", said about a broker capability claim. Test against the broker before stating what it serves (the IBKR API stock data test: code 10089, an extra API subscription is needed; delayed data is available).
5. Schwab keys gotcha confirmed again: `Brokers_merge\.env` holds placeholders, the real app key and secret are in `.env.secrets` ([[project_brokers_schwab]]).

**Update 2026-11-13:**
1. The tracker now lives in the repo: `docs/todo/2026-11-11_020723_user_complaints_tracker.md` (complaints 1 to 38). Complaints 39 to 49 and every later ask are recorded with their causes in the agents log `F:\GitHub Repos\RustTOS_agents\AGENT_LOG_2026-11-07_235708.md` and still need moving into the tracker file through a round.
2. The forward plan is Plan 2 (a gap analysis against TradingView, thinkorswim, E*TRADE, Webull and tastytrade, 87 rows, 8 phases): repo `docs/todo/2026-11-13_014831_plan_2_gap_analysis_five_platforms.md`. The steps A to P plans remain in `RustTOS_agents\plans`.
3. Rounds are named by letters (k through av by 2026-11-13) with tags `main-<date>-<letters>`; a round is workspace clippy, `check-all`, then `sharded-test --workspace --big` through the graphics card guard, about 20 to 25 minutes.
4. State at the 2026-11-13 restart and what to do next: [[project-rusttos-handoff-2026-11-13]].

Related: [[project_rusttos]].
