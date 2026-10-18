---
name: project_thinkscript_version_tracking
description: thinkorswim thinkScript studies live in a git-tracked folder; commit each change
metadata: 
  node_type: memory
  type: project
  originSessionId: 77d1ff79-a72b-462c-977f-55d5bdb9f957
  modified: 2026-10-18T04:01:02.525Z
---

The user's thinkorswim thinkScript studies (saved as .txt files) live in a git repo at `C:\Users\ohjos\ThinkScript_Studies\` and should be version-tracked. Commit after each meaningful change so the user can roll back.

First study tracked: `AEMA_Touch_Counter.txt` — an 8-length **OHLC4-based Adaptive MA** touch counter (NOT ordinary close MAs). Counts bars since price touched each adaptive MA, with a dashboard color progression white → green (2/4) → yellow (3/4) → red (>length) and an optional stretch alert.

The main repo is `F:\GitHub Repos\indicators` (symlinked at `C:\Users\ohjos\indicators`); ThinkScript_Studies holds byte-identical mirrors. Quant Pivots convention: edit in `ThinkOrSwim/QuantPivots/`, then copy to `ThinkOrSwim/Watchlists/`, the `ThinkOrSwim/` root (Status/Touch_Count/Diagnostics only) and ThinkScript_Studies, plus a `_YYYY-MM-DD_HHMM_SS` snapshot; commit both repos. As of 2026-10-17 (version 2026-10-17_2228_00) the QP "sigma" is an ATR multiple over COMPLETED periods. Chart: `ST_QuantPivots_Universal.txt` (exact 20-slot average) and `ST_QuantPivots_Universal_Wilder.txt`. Watchlist columns: ONE lean Wilder version (no `_Wilder` duplicates), recursion depth 2, to be paired with the Wilder chart; slot registers in columns raised TooComplexException (see [[feedback_thinkscript_watchlist_complexity]]). No fold / GetValue (crashed the TOS compiler, see [[feedback_thinkscript_fold_getvalue_crash]]). H8 = 3.7779 units, H4 = 1.5. Always take version stamps from `date`. Never reintroduce `Average()`/`StDev()` on per-period series in these files. Repo has `thinkscript_capabilities.py` (knowledge base + decision tree, validator rule 12, Claude Code PostToolUse hook in `.claude/settings.json`) and agent `.claude/agents/thinkscript-compat-checker.md`.

**Why:** User explicitly asked to keep version tracking of these files.
**How to apply:** When editing any study in that folder, `git -C "C:\Users\ohjos\ThinkScript_Studies" commit` the change with a clear message. Remember these averages are built on OHLC4, not close. See [[feedback_cross_device_paths]] for path portability across the user's devices.
