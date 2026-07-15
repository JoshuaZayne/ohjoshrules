---
name: reference_check_email_outlook_com
description: "How to read/search the user's email — Classic Outlook (hotmail) via PowerShell COM, and Gmail via MCP"
metadata: 
  node_type: memory
  type: reference
  originSessionId: c20cac6a-98c1-41e5-9601-db94a22bcc15
---

The user reads email in **Classic Outlook (desktop)**. Accounts: **joshua.a.zayne@hotmail.com** (Outlook/hotmail, the one used for the Ram deal) and **ohjoshrules@gmail.com** (Gmail, connected via the claude.ai Gmail MCP). Also has ohjoshrules@hotmail.com.

**To search / read Outlook mail, use PowerShell + Outlook COM** (not the Gmail MCP — that's only the gmail account):
- `$ol = New-Object -ComObject Outlook.Application; $ns = $ol.GetNamespace("MAPI"); $null = $ns.CurrentUser` — the `CurrentUser` access is the **COM warm-up** that prevents CreateItem/read errors.
- Inboxes across all accounts: `$ns.GetDefaultFolder(6)` (Inbox) plus `foreach ($f in $ns.Folders) { $f.Folders["Inbox"] }`. Sent = `GetDefaultFolder(5)` / `$f.Folders["Sent Items"]`.
- Sort newest-first: `$items = $inb.Items; $items.Sort("[ReceivedTime]", $true)`, then bound the loop (`if ($n -gt 150) break`) — don't scan the whole store.
- Filter on `$m.SenderEmailAddress`, `$m.Subject`; read `$m.Body`, `$m.UnRead`, `$m.ReceivedTime`, `$m.ConversationTopic`. Dealer emails append an **eLead tracking footer** — strip everything from `"---Please Do Not Delete"`.
- **Create a draft:** `$mail = $ol.CreateItem(0)`; set `.Subject`, `.To`, `.HTMLBody`; pick the sending account via `foreach ($a in $ol.Session.Accounts){ if ($a.SmtpAddress -eq "...") { $mail.SendUsingAccount = $a } }`; `.Display()` opens it for review (Outlook launches if closed). Build HTML with `@'...'@` single-quoted here-strings (literal `$`, no interpolation of prices) and use HTML entities (`&mdash;`, `&ndash;`) to dodge console-encoding mangling.

**Multi-account gotcha (the source of "search errors"):** the profile has ~10 mail stores, and **3 are NOT normal mailboxes** — "Public Folders - u0773052@utah.edu", the **iCloud** add-in store, and the utah.edu Exchange store. Blindly looping every store and doing `$store.Folders["Inbox"]` (or `$ns.Folders[...]`) **errors** on those. Fixes that make search bulletproof: (1) COM warm-up first; (2) **skip Public Folders** + wrap each `$store.GetRootFolder()` / `.Folders.Item("Inbox")` in try/catch; (3) only read **mail items** — `if ($it.Class -ne 43) { continue }` — meeting/receipt items throw on `.SenderEmailAddress`; (4) guard `$items.Sort("[ReceivedTime]",$true)`; (5) date cutoff + item cap so a huge mailbox doesn't hang. Reusable tool: **`F:\iCloudDrive\Documents\Carvana Ram\Search-Outlook.ps1`** (`-Query` regex, `-Account` filter, `-Days`, `-Max`, `-IncludeSent`). The deal account is **joshua.a.zayne@hotmail.com**; the default/CurrentUser store is ohjoshrules@hotmail.com.

**Gmail account** (ohjoshrules@gmail.com): use the MCP tools — `search_threads`, `get_message`, `create_draft` (note: draft attachments are flaky; embed data in the HTML body). create_draft requires a recipient (To/Cc/Bcc). See [[project_ram3500_autonation_deal]] for the deal this was used on.
