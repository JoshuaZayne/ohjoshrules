---
name: reference-rusttos-lab-manual
description: "RustTOS lab manual (2026-11-25): 15 HTML pages on how to explore data, set up and test each model, and reach the 80 percent win rate goal; where it lives and its key measured findings"
metadata:
  node_type: memory
  type: reference
  originSessionId: 030adbe3-54de-4de0-b8e4-959637b22e49
  modified: 2026-11-27T23:51:00.309Z
---

Written 2026-11-25 (about 04:50 to 05:45 MST) at the owner's request for an extreme detail explanation of how
to test, explore data, and set up each model (OLS, difference in differences, ARMA/GARCH, logistic, trees,
boosting, MCMC, neural network) toward "100 strategies over 80 percent win rate with math defined entry, stop
and target".

**Where:** the `RustTOS_strategy_docs` folder beside the RustTOS repo (same place as the 46 method pages,
outside the repo because of its Rust only language policy). Files `lab-*.html`, linked from the top of
`index.html`. Open `lab-start-here.html` first. Scripts behind every data figure, and the page checker
`check_pages.py`, are in `lab-scripts\` there. NOT in git. The in repo index `docs/strategy/ml_methods.md`
does not mention it yet (would need a branch and commit).

**Pages:** 1 start here, 2 goal math, 3 explore data, 4 rows and labels, 5 testing protocol, 6 OLS, 7 DiD,
8 ARMA/GARCH, 9 logistic, 10 trees/forest, 11 boosting, 12 MCMC, 13 neural network, 14 strategy factory,
15 build list (phases A to G; start with A1 series statistics, A2 barrier label, A3 barrier baseline).

**Measured findings worth remembering (stored candles, read 2026-11-25 about 05:00 MST):**
1. Random entries with a stop 4 times the target win 78 to 81 percent on ES and 6E: the random walk rate
   S/(S+T). A win rate must be read against break even p* = (S + cost)/(S + T), never alone.
2. The newest 6E 30 minute tier report has five tiers at 80 to 91 percent wins, all sitting at break even.
3. Direction has almost no memory (lag 1 autocorrelation about 0); size has a lot (0.2 to 0.3).
4. Cost of a losing trade as a share of a 5 minute bar's ATR: NQ 3 percent, GC 5, ES 16, CL 17, 6E 49,
   ZN 130. Most existing studies default to 6E, one of the most expensive; NQ and GC are barely explored.
5. `mcmc_optimizer.rs` is a Bayesian logistic regression on 12 trade readings, NOT a strategy parameter
   search; `docs/ARCHITECTURE.md` sections 12.1 and 13.14 describe the code wrongly.
6. Nine model modules on `agent/ml-backtesting` (learning_frame, learning_honesty, linear_models and so on)
   have no caller; the build list's "lab command" is what turns them on.

**Build state (2026-11-27 16:50 MST):** `agent/ml-backtesting` is merged into main. ALL of phase A (A1 to A7)
is ON MAIN at 81356ee8 (tag `main-2026-11-27-be`, round be, landed 16:46 MST together with the chart's link to
pulled copies, `agent/pulled-quotes-chart`). Commits 04b13605 (A1 to A3) and 40b1f854 (A4 excursion table, A5
`labelled_frame.rs`, A6 `bar_readings.rs`, A7 `rusttos-levels explore` plus `--rows-out` Parquet export).
Main was NOT pushed (owner asked for the merge only; 6 commits ahead of origin when written). Round be was
run by hand (clippy, check-all, sharded-test --workspace --big) because `rusttos_round` takes EVERY finished
`agent/*` branch and cannot be told which ones; it wanted another session's stale branch first.
Repo decisions D0980 to D0987, architecture sections 70 and 71. Next: phase B (the lab command that
trains any model on the labelled table, and the reliability table). Lessons measured there: baseline entries
closer together than a trade's length overlap, so the Jeffreys range is too narrow; at stop 2, target 1, hold
20 on stored candles (read 2026-11-27 08:52 MST) 15 of 16 sides of ES, NQ, GC, 6E at 5 and 30 minutes win
less with no rule than their break even rate (6E 5 minute needs 77.0 percent against 63 to 65).
Command: `rusttos-levels explore ES,NQ --bars 5_min,30_min --stop 2 --target 1 --hold 20 --out FOLDER`.

Code facts in the pages are from `agent/ml-backtesting` at dc821fe3; recheck against the code before relying
on them. Related: [[project_rusttos]], [[feedback_verifiable_claims]].
