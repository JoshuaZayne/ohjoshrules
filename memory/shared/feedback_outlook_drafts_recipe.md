---
name: feedback_outlook_drafts_recipe
description: "never drive Outlook by COM; draft AND send through Graph server side, four steps, no retry loops, never crash Outlook"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2edaab43-0968-4b37-b12b-0e3dca580b74
  modified: 2026-11-23T16:57:40.611Z
---

**Summary moved from the memory index (2026-11-08):** Outlook must never be crashed again: use ThicketHillProperty/scripts/create_outlook_draft.ps1 ONCE (it preflights and stops); never New-Object Outlook.Application, never retry loops, never Start-Process OUTLOOK.EXE repeatedly; recovery from 'exhausted all shared resources'

The user said 2026-11-07: "update agy memory so it doesnt crash outlook anymore". On 2026-11-06 agy spent about 100 actions trying to "open the draft in Outlook"; every retry opened a new MAPI session (headless `OUTLOOK.EXE -Embedding` copies) until Outlook showed "Outlook has exhausted all shared resources" and could not start again, even after restarts, because Word, Excel and OneNote (open for days, last reboot 2026-10-01) kept the MAPI shared memory alive. The draft could not be created at all.

**Why:** each failed `New-Object -ComObject Outlook.Application`, each COM retry loop, and each repeated launch leaks a MAPI session; once the shared pool is exhausted, only closing every Office app or restarting Windows fixes it.

**How to apply (hard rules for Claude and agy):**
1. To make an email draft, run ONCE: `powershell -File "C:\Users\ohjos\ThicketHillProperty\scripts\create_outlook_draft.ps1" -HtmlPath <body.html> -Subject "<subject>"` (optional -To -Cc -Bcc -Attachments). It checks that classic Outlook is open and ready and that no error dialog shows, attaches with GetActiveObject only, retries at most 3 times on that one session, saves in the account's Drafts, displays, never sends. If it prints STOP, tell the user what it says and stop.
2. Never call `New-Object -ComObject Outlook.Application` when Outlook might be running, never write a retry loop around Outlook COM, never launch OUTLOOK.EXE more than once per task, and never open .eml/.msg files with Start-Process to "make a draft" (that is a read-only message, not a draft).
3. If anything about Outlook fails twice, stop and report; do not improvise new approaches against Outlook.
4. Recovery when the dialog "Outlook Data File / exhausted all shared resources" appears: ask the user to save and close Word, Excel and OneNote and close Outlook, or restart the PC. Never close the user's Office documents yourself. Background helpers iCloudOutlookConfig64.exe and mmgaserver.exe may be stopped. A force-closed Outlook asks "start in safe mode?" next time; answer No.
5. New Outlook (olk.exe, "Inbox - Joshua Zayne - Outlook") has no COM; it cannot be scripted. Classic Outlook is OUTLOOK.EXE.
6. WORKS WITHOUT CLASSIC OUTLOOK (verified 2026-11-07): `powershell -File "C:\Users\ohjos\ThicketHillProperty\scripts\create_graph_draft.ps1" -HtmlPath <body.html> -Subject "<subject>" [-To ..] [-Cc ..] [-Bcc ..]` creates a formatted draft in joshua.a.zayne@hotmail.com's Drafts through Microsoft Graph (shows in New Outlook too), never sends. It reuses a DPAPI-encrypted sign-in in %LOCALAPPDATA%\ThicketHillProperty\graph_refresh_token.dat; if that expires it prints a device code for the user to enter at login.microsoft.com/device. Do not use the Microsoft.Graph PowerShell module's Connect-MgGraph in Windows PowerShell 5.1 (fails with "An error occurred when writing to a listener"). Prefer this over classic Outlook COM for drafts.

7. SENDING, and why it cannot lock up Outlook (verified 2026-11-23, the Fornaro reply sent 08:45:23 MST with a 6.4 MB attachment): Graph edits the mailbox server side over HTTPS, so there is no handle on the running OUTLOOK.EXE, no object model to leave dangling and no MAPI session to leak. Desktop Outlook only syncs the result down. OUTLOOK.EXE PID 28752 stayed `Responding: True` through the whole send. The working sequence, which must stay four separate steps so a failure leaves a draft rather than a half sent message:
   a. `POST /me/messages/{id}/createReply` to build the draft threaded to their message, which carries In-Reply-To, References and their address automatically. It also pulls their inline signature images in as attachments with `isInline: True`, so any "only one attachment" guard must filter those out or it will trip.
   b. `PATCH /me/messages/{draftId}` with the body. Set `contentType: HTML` and keep the quoted original after a `<hr>`.
   c. Attachments over about 3 MB need `POST .../attachments/createUploadSession` and chunked PUTs with `Content-Range`, each chunk a multiple of 320 KiB. Graph reports the attachment slightly LARGER than the file on disk because the size is MIME encoded, so verify `>= raw bytes`, never `==`. Check for an existing copy before uploading or a re-run attaches the same file twice.
   d. `POST /me/messages/{draftId}/send`, then confirm by READING Sent Items back and checking Drafts is empty. Never retry a send.
   Gotchas that cost time: Graph access tokens last about an hour, and an expired one returns `InvalidAuthenticationToken` while a PowerShell script keeps going, so later lines print empty results that look like real findings; `$orderby=sentDateTime desc` must be URL encoded as `%20desc` or Python's http.client raises `InvalidURL`; and `contentId` is not a selectable property on `microsoft.graph.attachment`, only `isInline` is.
8. NEVER call `Get-GraphAccessToken` in a foreground shell. If the saved refresh token lacks the scope asked for, it falls back to a device code loop that blocks up to 15 minutes, and it prints the code with `[Console]::WriteLine`, which does NOT reach a redirected output file, so the shell looks dead. Instead POST to `/devicecode` directly, print the URL and code for the user, then exchange the code. Mail.Send was first consented on this machine 2026-11-23; the DPAPI store at %LOCALAPPDATA%\ThicketHillProperty\graph_refresh_token.dat still holds a read only grant, so asking for Mail.Send triggers a fresh sign in.
9. Bash tool calls that `cd` into F: and grep the repo recursively routinely blow a 120 second timeout on this machine. Use the Grep tool or PowerShell for anything touching F:.

Related: [[reference_check_email_outlook_com]], [[project_thicket_hill_oct2026_status]], [[project_atv_rollover_claim]], [[feedback_no_auto_reply]].
