---
name: project_emailsearchandcleanup
description: EmailSearchandCleanup repo - Outlook preapproval PDF/OCR extraction + inbox/trash/junk cleanup pipelines
metadata: 
  node_type: memory
  type: project
  originSessionId: 9fbb2c61-0377-4b03-8785-661c7a460934
---

`~/repos/EmailSearchandCleanup/` — two Classic-Outlook (COM/MAPI) toolkits built 2026-06-16.

**preapproval/** — finds every house pre-approval email across all Outlook stores and
extracts each lender's loan amount/rate/expiration into `output/PREAPPROVAL_REPORT.md`.
5 stages: `01_search_outlook.ps1` → `02_filter_results.ps1` → `03_extract_emails.ps1`
(saves bodies + PDF attachments) → `04_parse_pdfs.py` (pdfplumber + **rapidocr OCR
fallback** for image-only letters like Freedom Mortgage; fixes `$832.750.00`→`$832,750`
and `90→9 days` OCR artifacts) → `05_build_report.py`. Run `scripts/run_all.ps1`.
Findings: 6 lenders — Chase ($500k@5.625%, updated $550k@5.49%), Freedom ($832,750 VA,
OCR'd), Veterans United ($900k, portal), Rocket (portal), USAA + Navy Federal (app stage).

**cleanup/** — `lib/classify.py` scores bulk/spam vs keep (List-Unsubscribe header, gibberish/
homoglyph sender, promo tokens vs known senders/.gov/.edu/genuine replies); conservative
inside Trash/Junk. `scan_folder.ps1` dumps inbox/trash/junk to JSON. Inbox report
recommends move-to-trash; `trashcleanup/build_report.py` rescues mis-filed Trash/Junk
mail before deletion and only green-lights emptying if nothing needs rescuing.
`trashcleanup/execute_cleanup.ps1` is the ONLY mutating script: dry-run by default,
typed `DELETE` confirm; handles move-to-trash / move-to-folder (auto-creates folder) /
move-to-inbox / permanent-delete. Run `run_cleanup.ps1` (read-only).

Added later: `build_junk_senders.py` learns recurring junk senders from Junk+Trash
(freq + classifier, excl. known-important + `config/allowlist.txt`) → auto vs review
buckets; `auto_trash_inbox.py` matches them in Inbox → move-to-trash plan (per-email,
skips bills, allowlist matches address AND display name). `sort_bills.py` is a per-email
bill-pay/receipt router → dedicated **Bills** folder (Xpress Bill Pay, Cap One, Apple
Card, Amex, Citi, Fidelity, etc.). `config/allowlist.txt` protects the user's **CPA = Pinnacle CPAs / Pinnacle Accountancy
Group of Utah, firm domain `pinncpas.com`** (jen@=Jenifer McCorkle "Jenn", Scott@=Scott
Rhead, Jared@=Jared Stevens) + their platforms safesendreturns.com / mangobilling.com /
quickfee.com / efileservices.net, plus GitHub/Chase/.gov/Substack/PyQuant. Allowlist
matches address AND display name. `config/blocklist.txt` = always-trash. Learned 74
auto-trash senders; top junk = saksfifthavenue@e.saks.com, firearms retailers,
restaurants, airlines. Per-email guards skip BILLS and TRAVEL (is_travel: itinerary/
boarding pass/e-ticket/flight confirmation/check-in) from auto-trash, so airline
marketing senders still get trashed but real tickets/itineraries are preserved.

Classic Outlook COM only — New Outlook has no MAPI ([[reference_new_outlook_com]]). Reuses
the Outlook-COM pattern from Travel_expenses. `output/` is git-ignored (personal mail).
Roadmap: `CodeMapping_Brain/content/roadmaps/2026-06-16_200215_emailsearchandcleanup.md`.

**User cleanup rules (encoded in classify.py + inbox_cleanup.py):**
- KEEP broker/bank STATEMENTS, trade confirmations, tax docs (is_statement) from Chase,
  Moomoo, IBKR, NinjaTrader, Webull, Fidelity, E*TRADE, Schwab, Navy Federal, USAA, MACU,
  etc. — but DELETE those same senders' non-statement alerts/notifications/promos.
- DELETE Lorex camera motion/PIR alerts (alerts@lorextechnology.com): the emails are
  15-167KB thumbnail notifications, NO actual video attached (clips stay on camera/cloud),
  so "keep long videos" is impossible. Keep only Lorex order/password/account mail.
- DELETE Mint, Zillow, Indeed outright. DELETE Fold App (foldapp / m.foldapp.com, blocklist).
- Uber receipts (order/trip) -> "Uber Receipts" FOLDER for work reimbursement; Uber
  account/sign-in kept; Uber promos deleted. (is_social/is_signin: social apps deleted,
  sign-in/security held 3 days = SOCIAL_SIGNIN_DAYS.)
- Permanent-delete bug fixed: Delete() on a Junk item only MOVES it to Deleted Items;
  execute_cleanup now moves to the store's Deleted Items first, then Delete()s (true purge).
- 45-day unread hold (STALE_DAYS) applies to APPROVED/allowlisted senders + ambiguous mail,
  NOT to confirmed promo (which deletes at any age). Junk folder = rescue legit then delete all.
- Big inbox: ohjoshrules@gmail.com has ~27k inbox messages (10k were Lorex). Per-account
  review table: scripts/inbox_by_account.py -> INBOX_BY_ACCOUNT.md (Focused/Other NOT
  exposed by Classic Outlook COM). Targeted cleanup: scripts/inbox_cleanup.py.
