---
name: project_thicket_hill_texas_home
description: "The Texas home repo (ThicketHillProperty) - where it lives, its pricing tooling, and the mail-sweep gotcha that hides self-emailed documents"
metadata: 
  node_type: memory
  type: project
  originSessionId: 866729e7-342d-4b93-bc80-546234a59ff2
  modified: 2026-08-07T06:32:00.896Z
---

**The "Texas home" repo is `C:\Users\ohjos\ThicketHillProperty`** (git, private) for **1725 Thicket Hill Drive, Van Alstyne, TX 75495** - Highland Homes **Leyland / Elevation CB**, Job **00896-087**, Thompson Farm 60s, Grayson County. Buyers Joshua and Olivia Zayne plus co-borrower Kevin Peccorini. Sales counselor **Pat Boyd (she/her)**, lender Hank Jackson at Highland HomeLoans.

**Tooling added 2026-08-07:** `pricing.json` + `pricing.py` (stdlib CLI: `table`, `bom`, `sqft N --span`, `report`) which generates `PRICING.md`; and `build_bom.py` which generates **`BOM_TEXAS_HOUSE_v2.xlsx`** (sheets Compare / BOM / Levels, all live formulas). Excel formula traps hit while building it: **MINIFS is not available** in this Excel build (returns #NAME?, use an array MIN with a 9.99E+307 sentinel), array `MATCH(1,(a)*(b),0)` needs an **`INDEX(...,0)` wrapper** to evaluate without Ctrl+Shift+Enter, and **`COUNTIFS(range,"<>")` counts a formula returning `""` as filled**, so guard on the raw input column, not the computed one. Verified by driving Excel over COM: zero formula errors. The contract lines reconcile **exactly to $716,680**, the subtotal printed on the Options Summary, and `pricing.py table` self-checks that every run.

**The numbers that matter:** base Leyland/CB $609,990; lot premium $20,000; structural options $76,540; brick $3,000 (fully credited back); credits -$43,550; **$50,000 of the price is placeholder** ($40,000 DESIGN CENTER + $10,000 PRE-CONSTRUCTION, both credited back after their meetings). The buyer's own **`BOM FOR TEXAS HOUSE .xlsx`** totals **$19,611** chosen, but it covers **flooring and bath finishes only** - no cabinets, counters, lighting, fixtures, appliances, paint - so it is a floor, not a total. Its `GROUP TOTAL COST` column has mis-dragged formulas; trust `TOTAL COST` per row.

**Cost per square foot is blocked on one input:** no Highland document states the square footage and the Sales Agreement disclaims it ("Buyer may rely only on engineered plan dimensions"). Highland's public page says the base Leyland is about 3,308 sq ft, but this job swaps Bedroom 4 / Lifestyle Room for the FlexGen Suite (1000-86) and adds the bay window (1350-50). TODO-27 tracks getting the engineered number; set `plan.square_feet` in pricing.json and rerun `pricing.py report`.

**Design Gallery designer is DESTINY GARCIA**, and her mail lands in **joshua.a.zayne@gmail.com** (also Tami Schow for scheduling, Robin Stevens earlier). On 2026-08-06 she sent Highland's own option-pricing screens: **WOOD Levels 1/2/3** (option # FLRW....-30/-31/-32) and **LVP Levels 3/4/5** (FLRV....-82/-83/-84), per room. This proves the spreadsheet's "LAMENENT" is **LVP LEVEL 3**, not laminate level 1. Whole-house hard surface: LVP L3 $8,764 (only complete grade), Wood L1 $7,470, Wood L3 $10,856, Tile L4 $13,332; as-chosen mix $9,407. Each screenshot is **cut off below Closet Under Stairs**, so PRIMARY ROOM is missing for five of six grades. Saved to `documents/design_gallery/`.

**TWO MAIL GOTCHAS (both cost a lot of time):**
1. `scripts/search_outlook_all.ps1` filters on builder keywords, so documents the user **emails to themselves from their phone** are invisible (the floor plan PDF and the BOM xlsx). Added `leyland`, `design gallery`, `bom for texas`, `highland homes pricing` to the term list.
2. **The `joshua.a.zayne@gmail.com` Outlook store lags badly.** Destiny's emails existed for a day but no sweep could see them until an explicit **`$ns.SendAndReceive($false)` plus ~30s wait**. Always force a sync before concluding mail does not exist. Note `New-Object -ComObject Excel.Application`/`Outlook.Application` also needs the **retry warm-up loop** or it throws RPC_E_CALL_REJECTED.

**When a document is reported missing:** force a sync, then do a **keyword-free recent-mail inventory across all stores listing attachment filenames**, and search by sender name. Do not trust the keyword sweep. See [[reference_check_email_outlook_com]].

**PDF gotcha:** Highland's Options Summary and change orders are **image-only PDFs** - pypdf returns nothing. Install `pymupdf` and rasterize (`get_pixmap(matrix=Matrix(3.5,3.5))`) to read them, or extract embedded images for photo-based notes.

**How to apply:** For any question about Texas home pricing, `pricing.json` is the source of truth and `python pricing.py table` proves it still reconciles. See [[project_dump_truck_business]] for the other Van Alstyne TX project.
