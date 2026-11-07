---
name: feedback_outlook_drafts_recipe
description: "How to open or create an Outlook email draft on the desktop the FIRST time: use ThicketHillProperty/scripts/create_outlook_draft.ps1; never loop New-Object Outlook.Application; how to recover from 'exhausted all shared resources'"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2edaab43-0968-4b37-b12b-0e3dca580b74
  modified: 2026-11-07T00:42:49.361Z
---

Creating or opening an email draft in classic Outlook (joshua.a.zayne@hotmail.com) must work on the first try. On 2026-11-06 agy spent about 100 actions failing to "open the draft in Outlook", and its retries each opened a new MAPI session until Outlook died with "Outlook has exhausted all shared resources". The user called it "a struggle bus".

**Why:** every `New-Object -ComObject Outlook.Application` or retry loop that creates sessions eats MAPI shared resources; once exhausted, Outlook cannot start until every process holding MAPI lets go.

**How to apply:**
1. Use the working script, do not improvise: `powershell -File "C:\Users\ohjos\ThicketHillProperty\scripts\create_outlook_draft.ps1" -HtmlPath <body.html> -Subject "<subject>" [-To ..] [-Cc ..] [-Bcc ..] [-Attachments ..]`. It attaches to the running Outlook, warms up with `$ns.CurrentUser`, creates the item in the account's own Drafts (`$account.DeliveryStore.GetDefaultFolder(16).Items.Add(0)`), sets SendUsingAccount via InvokeMember and checks it, saves, and calls Display(). It never sends.
2. Opening a .eml or .msg file with Start-Process is NOT a draft; it opens a read-only message. Do not use that route.
3. If a COM call fails twice, STOP and diagnose; do not retry in a loop. List Outlook's visible windows (EnumWindows on OUTLOOK.EXE) to read any dialog text.
4. If the dialog says "Outlook has exhausted all shared resources": stop every OUTLOOK.EXE (headless `-Embedding` copies included), stop the background helpers `iCloudOutlookConfig64.exe` and `mmgaserver.exe`, then start Outlook normally and answer "No" to the safe mode prompt. If it still fails, Word, Excel or OneNote also hold MAPI (OLMAPI32.DLL): ask the user to save and close them, or reboot. Never close the user's Office documents without asking.
5. Outlook started by COM runs headless (`-Embedding`, no main window); the user cannot see drafts in it. Start Outlook visibly first.

Related: [[reference_check_email_outlook_com]], [[project_thicket_hill_oct2026_status]].
