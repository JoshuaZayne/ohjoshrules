---
name: feedback_thinkscript_fold_getvalue_crash
description: "thinkScript gotcha: reading a fold accumulator inside GetValue() crashes the thinkorswim compiler; run thinkscript_capabilities.py before handing over any study"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 83278193-d6eb-4085-ace1-167c2497bcd2
  modified: 2026-10-18T03:51:35.659Z
---

Reading a `fold` accumulator inside `GetValue(...)` (for example `fold i = 0 to n with s = start do GetValue(x, BarNumber() - s, 100000)`) crashes thinkorswim's compiler: `UnexpectedASMException`, `NullPointerException: field` at `FoldingSubGenerator.putFoldingAccumulatorRead`. Hit on 2026-10-17 in the Quant Pivots H4/L4 watchlist column. It passed every static rule we had at the time.

**Why:** thinkorswim has no offline compiler, so "looks valid" is not "compiles". The user pasted the column and got a raw Java stack trace.

**How to apply:** In the indicators repo, run `python thinkscript_capabilities.py <file.txt>` (knowledge base + decision tree) on any thinkScript before handing it over, and use the `thinkscript-compat-checker` agent in `.claude/agents/`. Prefer `rec` shift-register slots over `fold` for per-period windows. Only use `GetValue(series, index)` with the fold INDEX. When thinkorswim rejects something new, add a KNOWLEDGE_BASE entry, a detector, and a test. Related: [[feedback_thinkscript_def_no_strings]], [[project_thinkscript_version_tracking]].
