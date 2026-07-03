---
name: project_email_cleanup_outlook_com
description: "How to run the EmailSearchandCleanup organizer against live Classic Outlook, incl. the COM warm-up gotcha"
metadata: 
  node_type: memory
  type: project
  originSessionId: f1ad4e8b-4fca-4b29-8714-e6fc307da0ba
---

The `EmailSearchandCleanup` repo (JoshuaZayne/EmailSearchandCleanup) organizes/cleans mail via **Classic Outlook COM/MAPI**. Operational notes learned running it live:

- User defaults to **New Outlook** (`olk.exe`, `UseNewOutlook=1`), which has **no COM**. Classic Outlook is installed at `C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE` and must be **launched and left running** for any of the scripts to work.
- COM calls intermittently throw `RPC_E_CALL_REJECTED (0x80010001)` / `CO_E_SERVER_EXEC_FAILURE (0x80080005)` when Outlook is busy syncing. **Warm up COM with a retry loop** (New-Object Outlook.Application → GetNamespace MAPI, retry ~8× with sleeps) before running `scan_folder.ps1`, and wrap `execute_cleanup.ps1` in a busy-retry too.
- **Run scripts in-process** (`& .\script.ps1`), NOT via `powershell -File ...` — a nested child process fails to bind the running Outlook COM server and silently scans 0 records.
- Large batches (~3k moves) generate transient per-item failures under load; a **second pass after Outlook settles clears them** (moves change EntryIDs, so rebuild the plan from a fresh scan rather than re-running the stale plan).
- 2026-07: ran the organizer live across 8 accounts — inbox 6,790 → 2,918 one-offs; ~3,780 filed + 93 VA newsletters trashed. Code improvements on branch `fix/portfolio-cleanup`. See [[project_thinkscript_version_tracking]] for the git-per-change habit and [[user_github_and_devices]].
