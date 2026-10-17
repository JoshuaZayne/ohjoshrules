---
name: project_atv_rollover_claim
description: "ATV rollover claim (Side By Side Share rental, renter Conner Corbin, Karl Malone $6,427.67 estimate vs platform $2,818.41 offer) lives in TicketProcessing/ATV_accident with a Utah Bar lawyer finder"
metadata:
  node_type: memory
  type: project
  originSessionId: c5bc23de-465d-409f-8b0e-7a173ca7df9b
  modified: 2026-10-17T21:19:25.643Z
---

Folder `F:\GitHub Repos\TicketProcessing\ATV_accident\` (branch `atv-accident`, commits aedddb2 + c8345da, created 2026-10-17, not pushed, not merged to main).

Facts: 2021 Can-Am Outlander XMR 1000R, VIN 3JBLWAX49MJ000547, rented via Side By Side Share 2026-09-11 to Conner Corbin (385-505-1007), who booked the "2025 CAN AM XTP" listing but took the Outlander, kept it 2 days and paid for 1. Rolled it. Signed departure form says existing damage "NONE"; signed return form lists the new damage. Karl Malone Powersports Provo RO 258550 (Carson Wamboldt) = $6,427.67 ($6,272.17 damage). Platform proposed $2,818.41 on 2026-10-16, **unsigned**, with "full and final resolution" wording. The user's own insurer denied it because of the rental use. Renter's rollover deductible is $6,000.

Mail: the claim emails are in joshua.a.zayne@hotmail.com, the shop emails in ojoshrules@hotmail.com, and the platform account is dimaskusllc@gmail.com (its Outlook store had only synced through 2026-09-20).

Tools: `damages.py` (3 claim sizes: $977 / $3,042 / $3,654), `find_utah_attorneys.py` (Utah Bar licensee directory POST to services.utahbar.org/cv5/cgi-bin/utilities.dll/CustomList, "First~" / "~Last~" wildcards; active = "Active Attorney" + "Paid"). Run them with the Anaconda `python` (py -3.12 lacks requests).

Platform reply email: built by `platform_email.py` and checked by `verify_email_numbers.py` (15 checks). The user wants it sent **from dimaskusllc@gmail.com with CC joshua.a.zayne@hotmail.com**. Draft created 2026-10-17 in `\\dimaskusllc@gmail.com\[Gmail]\Drafts` using the DeliveryStore Drafts + InvokeMember SendUsingAccount method. That Outlook store had stopped syncing on 2026-09-20, so confirm delivery by checking that the CC copy arrived.

**Why:** the user wants a Utah lawyer and options for the roughly $3k the platform won't cover. Related: [[project_ticketprocessing_mesa_court]].
**How to apply:** record lawyer call notes in `utah_attorneys/consultations.py`. The next steps are in `docs/UTAH_LEGAL_GUIDE.md`.
