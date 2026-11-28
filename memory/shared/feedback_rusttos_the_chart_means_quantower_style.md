---
name: feedback-rusttos-the-chart-means-quantower-style
description: "RustTOS: when the owner says 'the chart' or 'restart so I can see it' he means the Quantower style redesign (agent/chart-redesign), not main's plain chart; Desktop bat opens it"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 030adbe3-54de-4de0-b8e4-959637b22e49
  modified: 2026-11-28T00:21:08.592Z
---

On 2026-11-27 about 17:15 MST, after I rebuilt main's chart, installed it at `target\release\rusttos-chart.exe`
and started it to show a new feature, the owner said: "no no no the chart is not like the quant tower. i want a
bat file for the quant tower".

**Why:** the chart he looks at is the redesign (branch `agent/chart-redesign`, the desk laid out like his Quantower
screen), which is NOT on main. Main's chart is the old look. (My reading: he had expected the new feature to show
up inside the Quantower style chart.)

**How to apply:**
1. Before "rebuild and restart the chart so I can see it", say which chart a feature will appear in. If the work is
   on main only, tell him up front that the Quantower style chart will not show it until main is merged into
   `agent/chart-redesign` (on 2026-11-27 that merge conflicted in 27 files; the redesign forked from main on
   2026-11-24 and lacked rounds bb, bc, bd and be).
2. Launcher made that day: `C:\Users\ohjos\Desktop\RustTOS Quantower style chart.bat`. It starts the newest build in
   `C:\Users\ohjos\RustTOS_targets\chart-redesign\release\rusttos-chart.exe`, else the kept copy
   `F:\GitHub Repos\RustTOS\target\release\rusttos-chart_quantower_style.exe`, with the same `--market-data` and
   `--symbol 6E` as the normal shortcut. The older launcher `4 Charts\06 Open the REDESIGNED chart (preview).bat`
   opens the same program.
3. The redesign opens as about twelve OS windows (desk bar, depth, tape, charts); to check it on screen, capture
   each window of the process, not only the main window handle.

Related: [[project-rusttos-chart-redesign]], [[project_rusttos]].
