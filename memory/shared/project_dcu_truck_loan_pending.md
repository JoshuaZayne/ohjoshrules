---
name: project_dcu_truck_loan_pending
description: "REMIND USER: the new truck loan is with DCU (Digital Federal Credit Union); they still need to hand over its statements so it can be added to the spend repo (as of 2026-11-01)"
metadata:
  node_type: memory
  type: project
  originSessionId: f9b1edcd-3d91-4270-869f-f703e95eef0c
  modified: 2026-11-01T08:44:22.339Z
---

The new truck loan (the 2026 Ram 3500, see [[project_ram3500_autonation_deal]] and [[project_truck_financing_ram3500]]) is held by **DCU (Digital Federal Credit Union)**. On 2026-11-01 the user asked to be reminded that they still need to give me the DCU loan statements/export so the loan can be added to the Yearly_and_monthly_spend_per_CC ledger ([[project_spend_intake_and_accounts]]).

**Why:** the spend report's loan lines (Jeep/USAA, ATV/America First, motorcycle/Mountain America, Ford Transit/Chartway) are missing the truck, so housing+loan outflows and net worth understate the debt. Evidence it exists: a "Digital Federal Credit Union Changed Address Notification Confirmation" email (2026-08-15, joshua.a.zayne@hotmail.com) and an AMEX $2,000 "AN DODGE RAM BROADWAY LITTLETON CO" deposit on 2026-08-12 plus a $972.96 charge (both still Uncategorized).

**How to apply:** at the start of any session touching the spend repo, Brokers net worth, or the truck, remind the user to drop the DCU loan statements (PDF or CSV) into `source_documents/_inbox/`. Then add a DCU loan account (no parser exists yet; check the payment source account, likely Schwab 086 or Fidelity Z40) and a "Loan - Ram 3500 (DCU)" outflow category. Delete this memory once the DCU statements are in the repo.
