---
name: project_truck_financing_ram3500
description: "Financing plan for a new 2026 RAM 3500 Limited (~$85K) — best lenders, rebate-vs-promo math, action plan"
metadata: 
  node_type: memory
  type: project
  originSessionId: 32c5c671-67dd-4593-a751-3243affc48b4
---

Actively shopping a **new 2026 RAM 3500 Limited (~$85,000)** as of July 2026 (distinct from the usual USED Limited/Longhorn Mega Cab hunt in [[project_ram_megacab_scraper]]). Did a verified deep dive on auto financing. User is Utah-based, excellent credit (~800+), military/veteran-eligible (USAA/NavyFed/PenFed), already banks Navy Federal + Mountain America (MACU) — see [[project_spend_analysis_cc]] for the bank parsers, [[user_github_and_devices]].

**Core strategic conclusions (these are durable; exact APRs below are time-sensitive — re-verify before acting):**
1. **Always take the manufacturer REBATE, not the promo APR.** The 2026 RAM 3500 promo (5.9%/84mo) forces forfeiting ~$6,500 in rebates ($6,000 cash + $500 Military Bonus Cash). Rebate + credit-union financing beats the promo by **$7.7K–$18.3K** total. The promo's payment ($1,238/mo on $85K) is even *higher* than most CU 72mo options — it's the worst deal on the board.
2. **Shortest term you can afford wins** — 60mo vs 84mo saves ~$10.6K interest. Term matters more than small APR gaps.
3. **Headline "as low as" rates are teasers** — always pull the full term grid. NavyFed's 3.89% is 12–36mo only; USAA's real 60mo rate is 5.49% (not the 4.29% headline).

**Verified lender ranking (July 2026, financing $78,500 after rebate):**
- 🥇 **Utah First CU (Utah-local, the rate to beat):** 60mo **3.50%** / 72mo **4.00%** / 84mo 5.99% (2022+ vehicles, incl. 0.25% checking discount; finances up to 125% NADA, no $ cap; keeps rebates; no prepay penalty). → 60mo = $1,428/mo, $85,683 total.
- 🥈 **Navy Federal (user banks here):** 36mo 3.89% / 60mo 4.29% / 72mo 4.59% / 84mo 5.99%. 84mo needs ≥$30K. Pre-approval locks **90 days** (longest — best for shopping).
- 🥉 **Capital One Auto:** SOFT-PULL pre-qual (no credit hit), excellent-credit 72mo ~3–5%, max ~$150K. Best risk-free leverage quote.
- USAA: 60mo 5.49% (−0.25% autopay), military-only — weaker than expected, backup only.
- PenFed: 3.39% ONLY via car-buying service / higher direct; teaser-weighted.
- MACU (user banks here): 4.99% w/ MyStyle Checking — convenient, not cheapest.
- LightStream: 7.24% — SKIP, not competitive despite premium reputation.

**Action plan:** (1) soft-pull pre-quals at Capital One + PenFed first; (2) hard-apply Utah First + Navy Federal within a 14-day window (counts as one pull); (3) buy as cash buyer, claim the rebate; (4) only take dealer financing if it beats the pre-approval AND keeps the rebate (it won't); (5) target 60mo @ 3.50% ($1,428/mo) or 72mo @ 4.00% ($1,228/mo).

**Scripts (EPHEMERAL — in session scratchpad, will be wiped):** `truck_loan_ranked.py` (verified grid, ranked payment table) + `truck_loan_math.py` (rebate-vs-promo). Simple loan-payment math (`P*r/(1-(1+r)^-n)`); rebuild in seconds if lost. Not yet committed to any repo.
