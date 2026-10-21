---
name: project_atv_rollover_claim
description: "ATV rollover claim (Side By Side Share rental, renter Conner Corbin, Karl Malone $6,427.67 estimate vs platform $2,818.41 offer) lives in TicketProcessing/ATV_accident with a Utah Bar lawyer finder"
metadata:
  node_type: memory
  type: project
  originSessionId: c5bc23de-465d-409f-8b0e-7a173ca7df9b
  modified: 2026-10-17T22:13:44.920Z
---

Folder `F:\GitHub Repos\TicketProcessing\ATV_accident\` (branch `atv-accident`, commits aedddb2 + c8345da, created 2026-10-17, not pushed, not merged to main).

Facts: 2021 Can-Am Outlander XMR 1000R, VIN 3JBLWAX49MJ000547, rented via Side By Side Share 2026-09-11 to Conner Corbin (385-505-1007), who booked the "2025 CAN AM XTP" listing but took the Outlander, kept it 2 days and paid for 1. Rolled it. Signed departure form says existing damage "NONE"; signed return form lists the new damage. Karl Malone Powersports Provo RO 258550 (Carson Wamboldt) = $6,427.67 ($6,272.17 damage). Platform proposed $2,818.41 on 2026-10-16, **unsigned**, with "full and final resolution" wording. The user's own insurer denied it because of the rental use. Renter's rollover deductible is $6,000.

Mail: the claim emails are in joshua.a.zayne@hotmail.com, the shop emails in ojoshrules@hotmail.com, and the platform account is dimaskusllc@gmail.com (its Outlook store had only synced through 2026-09-20).

Tools: `damages.py` (3 claim sizes: $977 / $3,042 / $3,654), `find_utah_attorneys.py` (Utah Bar licensee directory POST to services.utahbar.org/cv5/cgi-bin/utilities.dll/CustomList, "First~" / "~Last~" wildcards; active = "Active Attorney" + "Paid"). Run them with the Anaconda `python` (py -3.12 lacks requests).

**SENT 2026-10-17 16:12** from dimaskusllc@gmail.com (CC copy saved in evidence/emails/2026-10-17_161244_*). Its ask: A plan $2,818.41 + B renter up to the $6,000 deductible $3,181.59 + C second day $200 = $6,200 through the platform, plus D $522.94 owed by the renter directly. Total owed $6,722.94, before the cargo box. Reply deadline **2026-10-30**. Still open: dates for 3 of the 4 lost rental days, and the cargo box quote from Karl Malone (Carson). Branch atv-accident pushed to origin (not merged to main).

Platform reply email: built by `platform_email.py` and checked by `verify_email_numbers.py` (15 checks). The user wants it sent **from dimaskusllc@gmail.com with CC joshua.a.zayne@hotmail.com**. Draft created 2026-10-17 in `\\dimaskusllc@gmail.com\[Gmail]\Drafts` using the DeliveryStore Drafts + InvokeMember SendUsingAccount method. That Outlook store had stopped syncing on 2026-09-20, so confirm delivery by checking that the CC copy arrived.

**2026-10-19 platform reply** (saved in evidence/emails/2026-10-19_113655_*): holds $2,818.41, declines to collect from renter, says the vehicle swap means "any terms you quote do not apply", denies loss of use and second day. Attached the 09-30 revised RO ($7,098.56). Rebuttal: XMR listing approved on platform 09-06, insurance card texted to Luke 09-06, Josh S platform bookings of XTP (6a9b04ae) and XMR (6aa41c4d) for 09-15/16 lost = $750 loss of use. The user insists on keeping the $200 second day and the $750 loss of use (don't suggest dropping them). Loss of use basis: 2 platform-booked nights (09-15/16, XTP + XMR) plus 09-22 asked for and agreed in texts but not yet booked; never describe 09-22 as booked. WARNING: the Josh S texts (evidence/private_do_not_send/, git-ignored) show delivery/helmets to be paid by Venmo, which the Terms say voids coverage for all the owner's vehicles: never send them to the platform. The platform's 'pre-booking' frames show mud splatter plus light scuffs, no cracks or breaks. `claim_after_platform_reply.py` gives repair $5,673.03, renter owes $3,804.62. Final point-by-point reply (10 numbered points + Part B second day, attachments A1 to A14) in output/platform_reply_final_2026-10-20_181500.txt; DRAFT CREATED 2026-10-20 in Outlook \dimaskusllc@gmail.com\[Gmail]\Drafts (subject 'RE: Final Claim Resolution', 14 attachments verified), NOT sent. Plate mount dropped (zip-tied before rental), no Sept 11 call log so that claim is out; renter owes $3,697.92, repair $5,566.33. COM gotcha: OpenSharedItem locks a .msg until closed; run Outlook COM inside Start-Job with a timeout, plan in docs/COURT_PLAN_2026-10-20.md. Open: Sept 11 call log to Luke, Josh S booking screenshots, plate mount before photos. Outlook COM was blocked by a "Reminders" dialog; retry each call on RPC_E_CALL_REJECTED. 2026-10-20: the dimaskusllc@gmail.com Outlook store is still frozen at 2026-09-20 (forcing a sync did nothing; last mails are Google security alerts) and the Gmail connector is olivia.m.zayne, so mail sent to dimaskusllc can't be read; have the user forward to joshua.a.zayne@hotmail.com. The platform's Box folders have itemDownload=false (preview only, no metadata).

**Why:** the user wants a Utah lawyer and options for the roughly $3k the platform won't cover. Related: [[project_ticketprocessing_mesa_court]].
**How to apply:** record lawyer call notes in `utah_attorneys/consultations.py`. The next steps are in `docs/UTAH_LEGAL_GUIDE.md`.
