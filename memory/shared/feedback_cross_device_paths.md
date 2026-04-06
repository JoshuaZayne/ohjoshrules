---
name: Cross-device path handling preference
description: How the user wants hardcoded paths handled so code runs on desktop, laptop, and Raspberry Pi
type: feedback
---

When code has hardcoded absolute paths that differ across the user's devices (desktop C:\, laptop F:\, USB D:\, Raspberry Pi /home/), convert them using a **loop-based resolver**, not by deleting the old paths.

**Why:** The user explicitly said "dont delete anything file location wise just create a loop to see which location the codes on so it will still work on any of those devices." They want the original paths preserved so they can audit what was there before, and they want the same code to run unchanged on all three machines.

**How to apply:**
- Create a `device_paths.py` at the repo root with a `find_existing_path(candidates)` helper that loops through candidate paths and returns the first that exists (falling back to the first candidate).
- List candidates in device order: desktop C:\ -> laptop F:\ -> USB D:\ -> `~/...` -> `/home/pi/...`.
- Expose resolved constants (e.g. `ICLOUD_ROOT`, `IBKR_ROOT`, `WEEK4_FOLDER`) plus a `DEVICE_NAME` detection (`desktop` / `laptop` / `raspie` / `unknown`).
- In source files, add `sys.path.insert` + `from device_paths import ...`, assign the resolved value to the original variable name, and **keep the original hardcoded line as a comment above it**.
- Done this way for: Brokers, InterActiveBrokers-Project, Efficient_Frontier, FinanceCode, FinanceExamMCP (docstring-only).
