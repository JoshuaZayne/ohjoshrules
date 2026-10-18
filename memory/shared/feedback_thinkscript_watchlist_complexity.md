---
name: feedback_thinkscript_watchlist_complexity
description: thinkScript watchlist TooComplexException tracks recursion chain depth (shift-register slots = depth 23 failed; working EMA columns = depth 2); only log a pass when the user confirms that exact file runs
metadata:
  node_type: memory
  type: feedback
  originSessionId: 83278193-d6eb-4085-ace1-167c2497bcd2
  modified: 2026-10-18T04:35:59.049Z
---

thinkorswim watchlist custom quote columns raise `com.devexperts.tos.thinkscript.runtime.TooComplexException` ("may not be reliable with real-time data"). On 2026-10-17 EVERY Quant Pivots ladder column with a 20- or 50-slot shift register (`slot_k = slot_(k-1)[1]`, recursion chain depth 23 or 53) failed, whatever its size score (349 to 592). The user's working EMA columns have depth 2. The fix that keeps depth at 2: a one-rec Wilder ruler, and reading the completed period as `pHigh[1]` / `pLow[1]` / `pOpen[1]` on the boundary bar instead of chains of previous-period recs. Charts tolerate deep chains.

**Why:** I logged the 2156_39 column as "working" because the user saw magenta cells. It was never confirmed, and two rounds of fixes chased a wrong theory (size, then a history counter) before the re-paste showed 2156_39 failing too. The user asked for these results to be documented in decision trees, with the watchlist tree separate from the chart tree.

**How to apply:** Only record a watchlist pass when the user says that exact file runs. Run `recursion_chain_depth()` / `python thinkscript_capabilities.py <file>` in the indicators repo, and keep new columns at depth 2 or 3. Log every paste result in `WATCHLIST_COMPLEXITY_OBSERVATIONS`, then run the tests and `--write-docs`. When something breaks, roll back to a CONFIRMED good file and change one thing at a time. Never `open(path, "w").write(f(open(path).read()))`, because it truncates the file first. Related: [[feedback_thinkscript_fold_getvalue_crash]], [[project_thinkscript_version_tracking]].
