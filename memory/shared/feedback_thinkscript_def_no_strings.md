---
name: feedback_thinkscript_def_no_strings
description: "thinkScript gotcha — def/rec hold only numbers (doubles), never strings"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 77d1ff79-a72b-462c-977f-55d5bdb9f957
---

In thinkScript (thinkorswim/Schwab studies), a `def` or `rec` variable can ONLY hold a number (double). Assigning a string — e.g. `def tag = if x then "A" else "B";` — fails to compile with errors like `Expected double` and `Incompatible parameter: "A"`.

Build any text inline at the point it's consumed (inside `AddLabel(...)` or `AddChartBubble(...)` text arguments), where string/if-else expressions are allowed. Do not factor a string into a named variable.

**Why:** Hit this in the ThinkScript_Studies repo — a `def modelTag = if ... then "TrueSigma" ...` broke both ST_QuantPivots v11 studies at compile time.
**How to apply:** When writing/reviewing thinkScript in [[project_thinkscript_version_tracking]], never store strings in def/rec. Inline the conditional text directly in the label/bubble call. Also recall labels (AddLabel) don't render on the thinkorswim mobile app — use AddChartBubble for mobile-visible text.
