---
name: reference_new_outlook_com
description: "How to read the user's Outlook.com/hotmail mail on this Windows PC; New Outlook has no COM/MAPI, must use classic Outlook"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 1b737734-5063-4aa8-9b83-fa47a43e091d
---

On this Windows PC the user runs **"New Outlook for Windows"** (`Microsoft.OutlookForWindows_8wekyb3d8bbwe`). New Outlook exposes **NO MAPI/COM automation** and keeps **almost no local mail cache**, so `New-Object -ComObject Outlook.Application` attaches only to the **classic Outlook** profile, which by default holds just `u0773052@utah.edu` (school).

The user's real personal mail is in **Microsoft/Outlook.com accounts**: `joshua.a.zayne@hotmail.com` (the big one, ~2,966 inbox), `ohjoshrules@hotmail.com`, `ojoshrules@hotmail.com`, plus `zaynebots@`/`zaynesbot@hotmail.com`. The connected claude.ai **Gmail** MCP only sees `ohjoshrules@gmail.com` (which does aggregate `ohjoshrules@hotmail.com` mail, but NOT the joshua.a.zayne accounts).

**To read these accounts locally:**
1. Discover signed-in MS accounts: `Get-ChildItem 'HKCU:\Software\Microsoft\IdentityCRL\UserExtendedProperties'`.
2. Launch classic Outlook: `C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE` (user toggles "New Outlook" off if it reopens new).
3. User does **File > Add Account** for the desired hotmail address; it creates a `.ost` and syncs.
4. Read via COM: `[Runtime.InteropServices.Marshal]::GetActiveObject("Outlook.Application")`, then `GetNamespace("MAPI").Folders`. Each added account = one store. If COM throws `0x80080005 Server execution failed`, Outlook is still starting/showing a dialog: wait and retry.
5. **Search fast**: filter by date range + keyword on Subject/Sender; do NOT iterate `.Items` one-by-one over thousands of messages (slow, may background-timeout). HTMLBody saved to .html then Edge headless `--print-to-pdf` makes clean PDF receipts.

Used for [[project_travel_expenses_may2026]].
