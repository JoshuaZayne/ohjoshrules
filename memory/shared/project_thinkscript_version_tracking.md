---
name: project_thinkscript_version_tracking
description: thinkorswim thinkScript studies live in a git-tracked folder; commit each change
metadata: 
  node_type: memory
  type: project
  originSessionId: 77d1ff79-a72b-462c-977f-55d5bdb9f957
---

The user's thinkorswim thinkScript studies (saved as .txt files) live in a git repo at `C:\Users\ohjos\ThinkScript_Studies\` and should be version-tracked. Commit after each meaningful change so the user can roll back.

First study tracked: `AEMA_Touch_Counter.txt` — an 8-length **OHLC4-based Adaptive MA** touch counter (NOT ordinary close MAs). Counts bars since price touched each adaptive MA, with a dashboard color progression white → green (2/4) → yellow (3/4) → red (>length) and an optional stretch alert.

**Why:** User explicitly asked to keep version tracking of these files.
**How to apply:** When editing any study in that folder, `git -C "C:\Users\ohjos\ThinkScript_Studies" commit` the change with a clear message. Remember these averages are built on OHLC4, not close. See [[feedback_cross_device_paths]] for path portability across the user's devices.
