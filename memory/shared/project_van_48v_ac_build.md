---
name: Van 48V mini split AC build
description: 48V off-grid build — PIVOTED from a Transit Connect van to a HOUSE build; real sunk cost $17,165.43 reconstructed from receipts
metadata:
  node_type: memory
  type: project
originSessionId: 9c745779-d480-4af5-87ef-8c4358f22e22
---

**PIVOT (2026-07-09): this is now a HOUSE / off-grid structure build, NOT the van.** The user cancelled the 2019 Transit Connect van build and is repurposing all hardware into a house 48V system. The pivot resolves the old roof-fit problem — 5.25 kW solar + 16 kWh battery are house-scale.

**Repo/workbook:** `C:\Users\ohjos\Desktop\van_48v_build_2026\` — generator `generate_report.py` writes `Van_48V_Build_Report_v26.xlsx` (current). `OUT` is hardcoded (no auto-bump) — bump the version in the script when Excel has the file open (PermissionError otherwise). The `sunk_items` list at the top of `generate_report.py` is now the SINGLE SOURCE OF TRUTH for owned cost (total computed as `SUNK_TOTAL`, referenced in README sheet, BOM header, BOM total cell, and final prints).

**REAL SUNK COST = $17,165.43** (was mis-recorded as $2,633.88 — workbook only knew 2 of the purchases). 7 owned line items, confirmed from receipts:
1. Senville #269641 — $715.60 — LETO 9k mini split + bracket (in ohjoshrules@gmail)
2. Voltaico Invoice VO-20585 — $1,918.28 — MultiPlus-II 48/5000, Lynx Distributor M10, Orion-Tr Smart 48/12-30A, SmartSolar MPPT 150/35, Cerbo GX MK2 (in ojoshrules@hotmail)
3. Off Grid Stores #OGS27520 — $3,355.81 — **RuiXU Lithi2-16, 51.2V/314Ah = ~16 kWh LiFePO4 UL9540 server-rack battery** + LTL freight (300+ lb, signature delivery) (in ojoshrules@hotmail / utah.edu)
4. Amazon shore parts — $175.74 — Camco 30A cord, Kohree 30A inlet, solar disconnect (in u0773052@utah.edu)
5. Solar panels — 15 × 350W @ $450 = $6,750.00 (5.25 kW array)
6. Solar mounting brackets — 15 × $250 = $3,750.00
7. Solar wiring — $500.00

**How the receipts were found (reusable):** Gmail connector only sees `ohjoshrules@gmail.com`. The rest were scattered across **Classic Outlook COM** accounts: `ojoshrules@hotmail.com`, `ohjoshrules@hotmail.com`, `joshua.a.zayne@hotmail.com`, `joshua.a.zayne@gmail.com`, `u0773052@utah.edu`, plus iCloud/others. Search method that worked: warm up Outlook COM (retry loop, see [[project_email_cleanup_outlook_com]]), then **DASL index restrict** (`@SQL` with `urn:schemas:httpmail:subject/fromname/fromemail LIKE '%token%'`) — walking every item folder-by-folder TIMES OUT (10 min); DASL restrict only touches matches and is fast.

**Owned hardware carries to the house.** Key open gaps flagged in the workbook:
- **Solar controller gap:** 5.25 kW of panels vs one SmartSolar 150/35 (~2 kW at 48V). Needs 2-3 more MPPTs (e.g. 250/100) or a bigger unit.
- **JS Alternators DECLINED** the alternator job ("unable to offer an alternator for your vehicle") — moot now anyway (house, not van).
- **BOM re-architecture still pending:** the `BOM — Plan A` sheet + `generate_diagram.py` still contain LEGACY van picks (Eco-Worthy battery, EcoFlow 400W, alternator, DC-DC, door-mount, hitch). Remaining-to-buy (~$12k) reflects the van plan, not the house. README + Build-facts + sheet index were updated for the house pivot; the deep BOM/diagram were NOT yet rebuilt.

**Vehicle (legacy, for reference):** 2019 Ford Transit Connect XL, VIN NM0LS7E28K1399891, SWB, bare roof, 2.0L Duratec.

**Why:** The user was right that the recorded cost was way off; the gap was entirely in non-Gmail inboxes. Always check the full Outlook account set via COM+DASL, not just the Gmail connector.

**GIT / CROSS-DEVICE DIVERGENCE (2026-07-10, repo JoshuaZayne/van-48v-build, PRIVATE):** Two lines of work exist — do NOT blindly merge:
- **`main`** = the OTHER device's parallel work (committed as ojoshrules@hotmail.com). It reconciled to **$5,989.69** (email-confirmed items only — Senville+Voltaico+RuiXU, NO solar) using a cleaner **overlay module `ruixu_buildout.py`** (`apply_overlay(wb)` post-processes the workbook instead of editing 2,600 lines inline), added "RUiXU Cabinet Build" + "Cabinet Parts" sheets, reached **v29**. Still van-framed.
- **`house-pivot`** = THIS session's commit. Full **$17,165.43** (adds the ~$11k solar the user gave verbally — panels/brackets/wiring, NOT in any email), **house pivot**, v26, plus `Solar_Prepayment_Agreement_DCM_Zayne.md`. User chose to LEAVE it as a separate branch (not merge to main).
- Ideal future reconciliation: adopt main's overlay architecture, extend it to $17,165.43 + house pivot, keep the prepayment agreement. User has NOT authorized this yet.

**TAX-STRUCTURE LINE (important):** The prepayment agreement was steered toward a related-party scheme (backdate to 3/3/2025, route Joshua's money through his own Dimaskus entity at a 65% markup, minimize entity profit) to inflate Joshua's 30% federal solar credit (IRC 25D) and dodge tax. I declined to optimize that (it's tax fraud: related-party self-dealing + backdating + inflated credit basis; 25D is placed-in-service-based and was terminated after 2025-12-31). Offered only a straight arm's-length version + "see a CPA." Hold that line if it resurfaces.

**How to apply:** For further cost questions, `sunk_items` in generate_report.py (on the house-pivot branch) is authoritative at $17,165.43. If the user resumes the house design, the next real task is the BOM/diagram re-architecture (strip van-only lines, add MPPT capacity, house AC distribution). See [[user_github_and_devices]] and [[project_email_cleanup_outlook_com]].
