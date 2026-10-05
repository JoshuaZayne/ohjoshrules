---
name: project_travel_expenses_may2026
description: "Travel expense report for the May 10-22 2026 Jersey City NJ trip; repo Travel_expenses, Delta+Sonesta amounts still pending"
metadata: 
  node_type: memory
  type: project
  originSessionId: 1b737734-5063-4aa8-9b83-fa47a43e091d
---

Travel expense report for the **May 10 to 22, 2026** Jersey City NJ trip. Repo: `~/repos/Travel_expenses`. Builder: `scripts/build_report.py`. Output: `output/Travel_Expense_Report_<timestamp>.xlsx` (tabs: All Expenses, Daily Summary, Category Summary). Roadmap: `~/repos/CodeMapping_Brain/content/roadmaps/2026-05-28_205800_travel-expenses-may-trip.md`.

Source PDFs (17 Uber Eats food receipts) live in `iCloudDrive/Documents/MooMoo_/TRAVEL TRIP RECEIPTS 10-22 MAY 2026`, copied into `receipts_pdf/`. Meals = $783.37. 3 Uber rides from Gmail = $115.29 Ground Transport. Confirmed total = $898.66.

**COMPLETE.** GRAND TOTAL $6,539.45 = Meals $783.37 (17 Uber Eats PDFs) + Ground Transport $115.29 (3 Uber rides) + Airfare $1,222.80 (Delta round-trip SLC<->EWR $1,132.80 net + 2x checked bag $45) + Lodging $4,417.99 (Sonesta Simply Suites Jersey City, 12 nights: $1,352.85 + $3,065.14). Amex booking EJQSYH charged $1,156.80 then credited -$24.00 = $1,132.80 net (matches Delta receipt). Delta SkyMiles #9162239488; Sonesta Travel Pass #145824262; Sonesta confs 31948SG129260 + 31948SG129918, itin 5157B37726830; ticket # 7439150311. Final 6-tab Excel: All Expenses (+From/To/Email Sent), Daily Summary, Category Summary, Email Receipts, Attachments & Photos, Trip Info & Members. All receipts saved to email_receipts/ as HTML+PDF; Amex e-ticket PDFs in email_receipts/attachments/.

**KEY LESSON (reusable):** the Delta/Sonesta mail lived in Microsoft accounts (joshua.a.zayne@hotmail.com, ojoshrules@hotmail.com) used via "New Outlook for Windows", which exposes NO MAPI/COM and keeps NO local cache, so `New-Object -ComObject Outlook.Application` only saw the classic-Outlook profile (utah.edu). Signed-in MS accounts are listed at HKCU:\Software\Microsoft\IdentityCRL\UserExtendedProperties. Fix: add the account to CLASSIC Outlook (File > Add Account); then COM reads it. Use date-restricted keyword search, not item-by-item over thousands of messages. Related: [[feedback_icloud_caution]], [[feedback_no_dashes]], [[feedback_file_timestamps]].
