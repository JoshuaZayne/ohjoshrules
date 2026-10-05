---
name: project_futu_compensation_scenarios
description: "FUTU job compensation planning, TX/MFJ/5-kids tax scenarios at $160k/200k/215k/250k base, 401k+HSA maxed, and Feb performance bonus tiers"
metadata: 
  node_type: memory
  type: project
  originSessionId: d4155661-cdca-45c2-a55e-56db0253aed8
  modified: 2026-08-01T01:49:45.059Z
---

User works at FUTU (parent of MooMoo, [[project_moomoo_quota]]). Comparing base salary
scenarios of $160k / $200k / $215k / $250k under TX residency (no state income tax),
MFJ, 5 kids, standard deduction, using 2026 federal tax law (post-OBBBA brackets,
permanent). Pretax 401k maxed ($24,500, 2026 limit, no catch-up) and HSA family maxed
($8,750, 2026 limit) at every scenario. 401k only shields federal income tax; HSA
(payroll) shields federal income tax AND FICA wages, this distinction matters for the
FICA line. Child Tax Credit = 5 x $2,200 = $11,000 (2026, unchanged by OBBBA), doesn't
phase out until $400k MFJ so full credit applies at every level examined. At $160k,
taxable income falls so low after 401k+HSA+std deduction that CTC exceeds fed tax
liability, refundable Additional CTC (up to $1,700/kid) covers the small gap, so net
federal income tax is effectively $0 at that tier.

**Cash take-home (annual, 401k+HSA maxed):** $160k->$115,329.37, $200k->$144,512.87,
$215k->$155,995.37, $250k->$182,787.87. Monthly: $9,610.78 / $12,042.74 / $12,999.61 /
$15,232.32. The $200k->$215k step is the weakest raise (~$957/mo net) since Social
Security is already capped by $200k and that whole increment sits in the 22% bracket.

**FUTU annual review bonus structure** (paid every February, % of base salary):
rating 3 = 20% min bonus, rating 4 = 30%, rating 5 = 40%. Bonus stacks onto base for
that tax year (401k/HSA caps don't scale up with it), so it's taxed at the marginal
rate of the combined base+bonus income, not the base income alone. Net effective tax
rate on the bonus itself runs ~23.5% to ~27.7% depending on base level and whether the
combined income crosses into the 24% bracket or the $250k Additional Medicare Tax
(0.9%) threshold, both matter more as base + bonus climbs past ~$268k-280k combined.
Example net bonus figures: $160k base/rating 5 (40%) -> $47,555.50 net of $64,000
gross; $250k base/rating 5 (40%) -> $74,265.75 net of $100,000 gross.

**Caveat**: figures are a point-in-time 2026 federal tax law snapshot (brackets,
standard deduction, 401k/HSA limits, CTC amount all indexed/set for 2026 specifically).
Re-verify current-year IRS figures before reusing these numbers in a future year.
Full per-scenario tables (12 base x bonus-rating combos) were computed in chat on
2026-07-31, not reproduced in full here, only headline figures kept per memory policy.

**Second job: VA GS-09 (Dept of Veterans Affairs), confirmed real via actual LES files**
in `iCloudDrive/Documents/VA LES Statements/` (DFAS civilian LES, ~34 files spanning
Dec 2024-Apr 2026). User holds BOTH the VA GS-09 role and the FUTU role simultaneously
(same SSN/name on both). SCD Leave 04/29/13. Step 3->4 increase confirmed effective PP
ending 08/23/25 (LES literally says "BASIC PAY CHANGED"): basic pay $55,685->$57,425,
adjusted basic (w/ UT locality) $65,185->$67,222. Jan 2026 GS table-wide raise bumped it
again to $58,001 basic / $67,896 adjusted (not a step change). Next step increase
(4->5) has a 2-year WGI wait, due ~August 2027 if continuous service. GS WGI waiting
periods generally: 1yr for steps 1->2/2->3/3->4, 2yr for 4->5/5->6/6->7, 3yr for
7->8/8->9/9->10.

**Combined household income (VA $67,896 + FUTU base, same MFJ return)**: 401k/TSP
elective deferral cap is $24,500 TOTAL across both plans (IRC 402(g) is per-person, not
per-employer, doesn't double). HSA family cap stays $8,750 household-wide. Social
Security's $184,500 wage cap applies once per person across combined wages (excess
withheld by having 2 employers gets refunded via Schedule 3 credit at filing). Combined
cash take-home (2026 law): $160k FUTU base+VA -> $165,867.26/yr ($13,822.27/mo); $200k
-> $196,404.95/yr; $215k -> $207,631.53/yr; $250k -> $233,409.03/yr. VA's $67,896 nets
out to roughly +$50,600 to +$51,900/yr on top of the FUTU-only take-home figures above.
At the $215k/$250k FUTU-base combos, combined household income crosses into the 24%
bracket and triggers the 0.9% Additional Medicare Tax (MFJ $250k threshold).

**VA leave balances** (snapshot as of LES PP ending 04/04/26, the most recent on file,
will drift over time, re-check the latest file in `VA LES Statements/` before relying
on this): Annual Leave balance 109.50 hrs (~13.7 days), accruing 6.00 hrs/PP (the top
federal accrual tier, 3+ yrs service, consistent with SCD 04/29/13). Sick Leave balance
403.75 hrs (~50.5 days), accruing 4.00 hrs/PP (standard rate for all federal employees).
Max annual leave carryover cap is 240 hrs, current balance is well under that so no
use-or-lose risk right now. Leave year ends 01/09/27. There's also a PPL Birth (Paid
Parental Leave) entitlement showing 480 hrs with a term date of 08/06/26, worth
clarifying with the user next time this comes up, could relate to a recent/upcoming
birth given the 5-kids household context.

**Per-job standalone tables** (2026-08-01): FUTU uses the hypothetical maxed-401k+HSA
scenario-planning convention above. VA uses REAL current elections instead (8%
traditional TSP = $5,431.68/yr, Roth TSP $35/pp = $910/yr, no HSA, VA doesn't offer one)
since VA is a fixed real salary, not a range of what-if scenarios. VA standalone (as if
sole household income, illustrative only, real filing is joint/combined): taxable income
$30,264.32, fed tax pre-CTC $3,135.72, CTC wipes it to a $7,864.28 credit surplus (only
meaningful once combined with FUTU's higher tax bill on the real joint return), FICA
$5,194.04 (SS $4,209.55 + Medicare $984.49, VA alone never nears the $184,500 SS cap).
Net standalone tax picture is a $2,670.24 refund position; standalone cash take-home
$64,224.56/yr ($5,352.05/mo). This standalone framing is illustrative/mechanical only,
the real combined-household numbers above are the ones that matter for actual planning.

Note: earlier in this same research thread there was a false alarm over a blank W2
template + employment-verification letter found in the unrelated `1099_generation`
repo (employer "Dimaskus Capital Management", which IS a real user-owned Utah LLC per
Articles of Organization in iCloud, but the purpose of generating blank W2/verification
docs for it was never fully explained). That repo is NOT the source of the real VA/FUTU
income data above, those came from genuine LES/paystub files. The 1099_generation
repo's purpose remains an open question worth revisiting if it comes up again.
