---
name: File timestamp format
description: All generated output files must include date, hour, minute, and seconds in the filename
type: feedback
---

All generated output files must include full timestamps: date + hour + minute + seconds.

**Why:** User needs to quickly identify the most up-to-date version when multiple runs produce similar files.

**How to apply:** Use format `YYYY-MM-DD_HHMMSS` in filenames. For example: `HW12_Solution_20260401_054113.xlsx` not `HW12_Solution_20260401_0541.xlsx`. Update `stamped_name()` and any `TIMESTAMP` constants to include seconds.
