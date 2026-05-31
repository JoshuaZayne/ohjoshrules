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

**Why the 2nd-alt path is dead for this vehicle:** Nations, Balmar, Arco, American Power all skip the Transit Connect platform — the transverse 2.0L Duratec engine bay is too tight. Custom fab would be $1,500-3,000 with no guarantee of working. The 270XP + stacked DC-DC path is the right answer.

**BOM total (baseline build):** ~$15,000-16,000 hardware-only, before labor/install. Documented in detail in the workbook below.

**Daily energy budget:** ~7.8 kWh/day load. 400W solar = 1.5 kWh; 1 hr driving via 2× Orion = 2.4 kWh; shore = 1.7 kWh/hr. Sustainable off-grid needs ~2 hr driving daily OR 600W solar + 1.5 hr OR shorter AC use. Shore power makes everything trivial.

**Reference videos user is drawing from:**
- https://www.youtube.com/watch?v=7iGNl0Vmz7A
- https://www.youtube.com/watch?v=OwcgNvBUPic

**Generated artifacts (2026-05-31):**
- `C:\Users\ohjos\Desktop\van_48v_build_2026\Van_48V_Build_Report_2026-05-31.xlsx` — full workbook (README, Vehicle, Roof & Solar, Mini Split Options, Charging Architecture, BOM, Energy Budget, Sources). Re-runnable via the sibling `generate_report.py` (openpyxl).

**Open follow-ups for next conversation:**
- Confirm SWB vs LWB (NHTSA VIN decoder didn't return wheelbase).
- Confirm whether the van has factory roof rails or bare roof — affects panel mounting hardware.
- Confirm typical use case: full-time vanlife / weekend / work van — drives final bank size.

**Why:** Decisions cascade into BOM, wire/fuse sizing, and bus architecture. The biggest lesson from this conversation: ALWAYS run the VIN before assuming platform. The user said "Transit, small roof" which I read as full-size Transit low-roof; the VIN revealed Transit Connect, which is an entirely different vehicle.

**How to apply:** When user returns, refer to the workbook for current state — don't re-derive. If they decide to change a major variable (battery count, AC type, solar size), regenerate the workbook by editing `generate_report.py` and re-running it. Always cross-check vehicle identity with VIN decode before recommending parts.
