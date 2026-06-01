---
name: Van 48V mini split AC build
description: User is designing a van conversion with a 48V house bank powering a mini split AC system; weighing alternator charging options
type: project
originSessionId: 9c745779-d480-4af5-87ef-8c4358f22e22
---
User is building out a van AC system using a 48V house battery bank to run a mini split (chosen for efficiency).

**VEHICLE IS A TRANSIT CONNECT, NOT A FULL-SIZE TRANSIT.** VIN NM0LS7E28K1399891 decoded via NHTSA (2026-05-31): 2019 Ford Transit Connect XL Cargo Van, 2.0L 4-cyl GDI, built in Valencia Spain, Class 1D GVWR (5,001–6,000 lb). This is a compact van, ~127 cu ft cargo (LWB), ~1,570 lb payload — totally different platform than what I assumed in the first conversation.

**Locked decisions (post-VIN-decode):**
- Van: 2019 Ford Transit Connect XL (LWB assumed; confirm SWB vs LWB).
- Mini split: 9k BTU 120VAC (NOT 12k — 12k oversizes ~127 cu ft cargo space). Senville LETO 9k as baseline pick.
- House bank: 2× Battle Born 48V/100Ah LFP = ~10 kWh, ~200 lb (15 kWh = 3 batteries listed as upgrade).
- Charging path: NOT a second alternator — no commercial kit exists for the Transit Connect 2.0L. Instead: upgrade stock alternator to DC Power 270XP 12V (~$850), then stack 2× Victron Orion XS 12/48-25 DC-DC chargers (2.4 kW total, 3rd optional for 3.6 kW).
- Solar: 400W baseline (2× Renogy 200W rigid). 600W achievable but tight. 800W NOT REALISTIC on Connect LWB roof (~35-42 sq ft usable after MaxxFan).
- Target AC runtime: 9 hours/day (5.4 kWh @ 600W avg).
- Shore power: Victron MultiPlus-II 48/3000 120V handles invert + charge + transfer + PowerAssist in one box.

**Why the 2nd-alt path is dead for this vehicle:** Nations, Balmar, Arco, American Power all skip the Transit Connect platform off-the-shelf — the transverse 2.0L Duratec engine bay is too tight for their stock brackets. The 270XP + stacked DC-DC path is the practical answer ($2,000 all-in for 3.6 kW @ 48V).

**One theoretical 48V alternator option exists:** Arco Zeus A8000-48V is the smallest/lightest 48V alternator on the market and Arco/Trek Systems will fabricate custom brackets. For the Connect's 2.0L Duratec they'd need a one-off bracket (no MK1201-equivalent exists — that's for the 3.5L EcoBoost Transit). Cost estimate $4,500-7,000 all-in including custom fab and Litens overrunning pulley (recommended for 4-cyl engines). Contact: support@trek.systems with the VIN. Only worth pursuing if the owner drives < 1 hr/day routinely.

**BOM total (baseline build):** ~$15,000-16,000 hardware-only, before labor/install. Documented in detail in the workbook below.

**Daily energy budget:** ~7.8 kWh/day load. 400W solar = 1.5 kWh; 1 hr driving via 2× Orion = 2.4 kWh; shore = 1.7 kWh/hr. Sustainable off-grid needs ~2 hr driving daily OR 600W solar + 1.5 hr OR shorter AC use. Shore power makes everything trivial.

**Reference videos user is drawing from:**
- https://www.youtube.com/watch?v=7iGNl0Vmz7A
- https://www.youtube.com/watch?v=OwcgNvBUPic

**Generated artifacts (2026-05-31, rev 3):**
- `C:\Users\ohjos\Desktop\van_48v_build_2026\Van_48V_Build_Report_v3.xlsx` — current workbook (12 sheets). Re-runnable via `generate_report.py`. Note: when Excel has the file open, the script gets a PermissionError; write to a new versioned filename or close Excel first.
- `C:\Users\ohjos\Desktop\van_48v_build_2026\charging_architecture.png` — matplotlib-generated diagram (1100×690 @ 150 DPI). Embedded in the Charging Architecture sheet. Re-runnable via `generate_diagram.py`.
- Rev 3 sheets: README, Vehicle (SWB), Roof & Solar (20+ product links), Plan A — Mini Split (door-mount rejected; engineered as head-above-door + condenser on hitch swing-arm), Plan B — 48V Rooftop AC (with startup/cooldown/steady/ECO wattage columns), Mini Split Comparison (35 units), 9k BTU — 15 Sources, Charging Architecture (with embedded PNG diagram + 48V alternator section), BOM — Plan A, BOM — Plan B, Where to Buy (3 retailers per item), Energy Budget, Sources.

**Rev 3 confirmed user inputs (2026-05-31):**
- ~80" measurement from back of front seat to rear door → SWB inferred (cargo 72.6").
- Bare roof (no factory rails).
- Full-time vanlife 5 days/week → bank upsized to 15 kWh.
- NO existing Class III hitch receiver. If Plan A is chosen, must add Curt **C13167** (~$280 parts, eTrailer custom-fit for 2019 Connect) + ~$225 shop install = ~$500 extra. Plan B doesn't need a hitch. NOTE: Earlier revisions used wrong part number "13134" — corrected throughout to C13167.

**Rev 6 high-wattage solar panel research (2026-05-31):**
- Verified rigid panel dimensions for 300W-600W class. Key finding: **EcoFlow 400W (67.8 × 44.6 × 1.4 in, 48 lb, $499) FITS the Connect SWB roof** — single-panel 400W option with fewer roof penetrations than 2× 200W. 
- 500-550W panels (90 × 44 in) are at the absolute length limit of the SWB roof (~90" usable) — RISKY.
- 590-600W class (94 × 45 in or 85.5 × 51.3 in for Trina) — does NOT fit (Renogy 590W too long, Trina 600W too wide).
- Updated Roof & Solar sheet has all major sections with TWO vendor link columns (Primary + Alt) for cross-shopping.

**Rev 3 corrections from prior revisions:**
- MPPT bug fix: SmartSolar 100/30 is 12/24V ONLY. Use SmartSolar 150/35 ($194) for 48V systems. Updated in BOM and Where to Buy.
- Battle Born does NOT make a 48V/100Ah module — it's 4× 12V/100Ah in series. EG4 LL-S 48V/100Ah ($1,500 each) is a real 48V battery and cheaper per kWh; included as the recommended budget alternative.

**Door-mount mini split REVISITED — owner went with welded bracket on driver-side rear door (v9, 2026-05-31).** After being walked through the weight concerns (~65 lb on stock hinges = ~150% overload), owner decided to commit to the door-mount approach. Plan A updated to use the Senville 2-piece outdoor wall-mount bracket ($39.99) welded to driver-side rear door, with REQUIRED hinge reinforcement (Avatar Offroad HD hinges or welded third-hinge plate). NO hitch needed. Saves ~$1,255 vs the rejected swing-arm path. Engineering risks (door sag, hinge wear, latch alignment failure within 6-12 months without reinforcement) flagged explicitly in the Plan A sheet with a WARN-styled section.

**Most powerful 48V rooftop ACs surveyed (Plan B sheet):**
- RecPro 48V 13.5k BTU heat pump — $1,999 — MOST POWERFUL, but oversized for 127 cu ft Connect
- Velit 3000R 48V — 12k BTU — $2,449
- Nomadic Cooling X3 Helix 48V — 11.8k BTU — $2,800-3,200
- Velit 2000R 48V — 10k BTU — $1,900-2,200
- Nomadic Cooling X2 Helix 48V — 9.5k BTU — $2,200-2,700 — BEST FIT for Connect (44 lb, 6.9" tall)
- RecPro 48V 9.5k BTU heat pump — $1,849
- Velit 2000R Mini 48V — 7.5k BTU — $1,500 — BUDGET FIT for Connect

**Open follow-ups for next conversation:**
- Confirm SWB vs LWB (NHTSA VIN decoder didn't return wheelbase).
- Confirm whether the van has factory roof rails or bare roof — affects panel mounting hardware.
- Confirm typical use case: full-time vanlife / weekend / work van — drives final bank size.

**Why:** Decisions cascade into BOM, wire/fuse sizing, and bus architecture. The biggest lesson from this conversation: ALWAYS run the VIN before assuming platform. The user said "Transit, small roof" which I read as full-size Transit low-roof; the VIN revealed Transit Connect, which is an entirely different vehicle.

**How to apply:** When user returns, refer to the workbook for current state — don't re-derive. If they decide to change a major variable (battery count, AC type, solar size), regenerate the workbook by editing `generate_report.py` and re-running it. Always cross-check vehicle identity with VIN decode before recommending parts.
