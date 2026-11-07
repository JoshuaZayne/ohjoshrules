---
name: feedback_outlook_drafts_recipe
description: "Outlook must never be crashed again: use ThicketHillProperty/scripts/create_outlook_draft.ps1 ONCE (it preflights and stops); never New-Object Outlook.Application, never retry loops, never Start-Process OUTLOOK.EXE repeatedly; recovery from 'exhausted all shared resources'"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2edaab43-0968-4b37-b12b-0e3dca580b74
  modified: 2026-11-07T12:18:20.691Z
---

The user said 2026-11-07: "update agy memory so it doesnt crash outlook anymore". On 2026-11-06 agy spent about 100 actions trying to "open the draft in Outlook"; every retry opened a new MAPI session (headless `OUTLOOK.EXE -Embedding` copies) until Outlook showed "Outlook has exhausted all shared resources" and could not start again, even after restarts, because Word, Excel and OneNote (open for days, last reboot 2026-10-01) kept the MAPI shared memory alive. The draft could not be created at all.

**Why:** each failed `New-Object -ComObject Outlook.Application`, each COM retry loop, and each repeated launch leaks a MAPI session; once the shared pool is exhausted, only closing every Office app or restarting Windows fixes it.

**How to apply (hard rules for Claude and agy):**
1. To make an email draft, run ONCE: `powershell -File "C:\Users\ohjos\ThicketHillProperty\scripts\create_outlook_draft.ps1" -HtmlPath <body.html> -Subject "<subject>"` (optional -To -Cc -Bcc -Attachments). It checks that classic Outlook is open and ready and that no error dialog shows, attaches with GetActiveObject only, retries at most 3 times on that one session, saves in the account's Drafts, displays, never sends. If it prints STOP, tell the user what it says and stop.
2. Never call `New-Object -ComObject Outlook.Application` when Outlook might be running, never write a retry loop around Outlook COM, never launch OUTLOOK.EXE more than once per task, and never open .eml/.msg files with Start-Process to "make a draft" (that is a read-only message, not a draft).
3. If anything about Outlook fails twice, stop and report; do not improvise new approaches against Outlook.
4. Recovery when the dialog "Outlook Data File / exhausted all shared resources" appears: ask the user to save and close Word, Excel and OneNote and close Outlook, or restart the PC. Never close the user's Office documents yourself. Background helpers iCloudOutlookConfig64.exe and mmgaserver.exe may be stopped. A force-closed Outlook asks "start in safe mode?" next time; answer No.
5. New Outlook (olk.exe, "Inbox - Joshua Zayne - Outlook") has no COM; it cannot be scripted. Classic Outlook is OUTLOOK.EXE.
6. WORKS WITHOUT CLASSIC OUTLOOK (verified 2026-11-07): `powershell -File "C:\Users\ohjos\ThicketHillProperty\scripts\create_graph_draft.ps1" -HtmlPath <body.html> -Subject "<subject>" [-To ..] [-Cc ..] [-Bcc ..]` creates a formatted draft in joshua.a.zayne@hotmail.com's Drafts through Microsoft Graph (shows in New Outlook too), never sends. It reuses a DPAPI-encrypted sign-in in %LOCALAPPDATA%\ThicketHillProperty\graph_refresh_token.dat; if that expires it prints a device code for the user to enter at login.microsoft.com/device. Do not use the Microsoft.Graph PowerShell module's Connect-MgGraph in Windows PowerShell 5.1 (fails with "An error occurred when writing to a listener"). Prefer this over classic Outlook COM for drafts.

Related: [[reference_check_email_outlook_com]], [[project_thicket_hill_oct2026_status]].
