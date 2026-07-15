---
name: project_dump_truck_business
description: "DumpTruckBusinessBuildout repo - Van Alstyne TX dump trailer business model, and the 299-lb CDL finding that blocks the original plan"
metadata: 
  node_type: memory
  type: project
  originSessionId: f19d5582-3a75-4095-a4c3-e99e11bce98c
---

Private repo **JoshuaZayne/DumpTruckBusinessBuildout**, local at `C:\Users\ohjos\DumpTruckBusinessBuildout`.
Costing/pricing/econometric model for a dump trailer + material delivery + debris hauling business
based in **Van Alstyne TX** (Grayson County), 70-mile radius. Started 2026-07-14.

**Constraints the user set:** non-CDL now / CDL later; under $25k startup capital; owner-operator
driving first, hire later; Ram 3500 is a mixed business+personal unit. Also asked for a 100%-business-use
model, and a 15+ trailer comparison table (delivered: 27 trailers).

## THE BLOCKING FINDING (the whole point of the repo)

The **non-CDL plan does not work**, and the margin is **299 pounds**. A real dealer build sheet
(VIN `3C63RRPL6TG166439`) puts the Ram 3500 **Limited Mega Cab 4x4 HO Cummins SRW** at
**GVWR 12,300 lb / payload 3,710 lb** — NOT the 11,700 lb a generic "Ram 3500 SRW" lookup returns.

    12,300 (truck) + 14,000 (standard gooseneck dump) = 26,300 lb
    Texas Class A CDL threshold                       = 26,001 lb

**Largest non-CDL trailer behind this truck = 13,700 lb.** Every gooseneck dump marketed as "14K" is
stamped at or above 14,000 (Big Tex "14GX" = 15,900; PJ "14K Low-Pro" = 15,400 — always plan off the
STAMPED rating, never the model name).

**Unresolved second problem:** 49 CFR 383.5 defines GCWR as the *manufacturer's label value when
displayed*. This truck's label reads **31,960 lb**. Under a strict reading, ANY trailer over 10,000 lb
requires Class A regardless of the sum. Texas DPS commonly applies sum-of-ratings instead. **Two
defensible readings, opposite answers, same truck.** Only a trailer rated **<= 10,000 lb** is safe
under both (it fails the "in excess of 10,000 lb" prong). Documented, not guessed.

## Other load-bearing findings

- **The truck is a bad hauling platform.** 3,710 lb payload, ~3,100 lb eaten by gooseneck pin before
  any cargo. The 23,000 lb tow rating is unreachable — you run out of bed before you run out of engine.
- **Bigger trailers carry LESS behind it.** 14k → 4.9 tons; 21k → 4.6; 26k → 3.1. Tare eats the fixed
  pin budget. The $34k Diamond C WDT yields **1.8 usable tons** = $18,504/ton of capacity.
- **Only 2 of 27 catalogued trailers are non-CDL** behind this truck.
- **A Ford F-600 (22,000 GVWR single vehicle) carries 7.3 tons with NO CDL** — more than the gooseneck
  path carries WITH one, and no combination-rating question at all. ~$62k used, over budget; financing
  it is the highest-value unmodeled variant.
- **Rock weighs out at ~46% box volume; mulch cubes out at ~35% payload.** For aggregate, box size is
  nearly irrelevant — only payload matters.
- **McCraw Landscape Supply is at 15048 US-75, IN Van Alstyne** (903-482-5649) — zero deadhead. Price
  list not published; that call is the highest-leverage action available.
- **Grayson County Bid 2023-06** = real submitted local hauling bids, **$0.209–0.320/ton-mile**. Best
  pricing anchor found. Roll-offs at **$370–695 / 20yd week** are the hard ceiling on debris pricing.
- **Sherman gives residents FREE curbside brush pickup** — hard price floor inside city limits.
- **Builders pay in 56–96 days** (five independent surveys agree; 5% pay on time). Three unpaid builder
  invoices = insolvency on one trailer. Do vendor paperwork now, take the work after a credit line.
- Diesel Sherman-Denison **$4.458/gal, up 46% YoY** — do not use last year's fuel price.

## Repo conventions

- **No abbreviations in code** (user requirement): `density_pounds_per_cubic_yard_nominal`, never `dens`.
- **Every price carries `confidence` + `source_url`.** confirmed_published / estimated_from_comparables /
  unverified_placeholder. Nothing is presented as fact that isn't.
- **No elasticity is measured** — all reasoned priors, labeled as such.
- Legal thresholds are constants, never tuned to make a scenario work.
- Paths resolve by walking up from the source file (cross-device per [[feedback_cross_device_paths]]).
- Run: `py -3.12 analysis/scripts/run_scenario_comparison.py` and `build_trailer_comparison_table.py`.
  Python 3.9 is on PATH but is too old — use `py -3.12`.

## Disposal sites (16 in `data/reference/locations/disposal_sites.csv`)

- **121 RDF, Melissa — $52/TON, 1-ton min, ~13 mi.** Closest Type I, card at gate, **no account
  needed**. Archive-verified. **+$150 PER LOAD for shingles** — that surcharge dominates roofing work.
- **TASWA, Whitesboro — $47.60/TON, $45 min, ~37 mi.** Cheapest per-ton. Two agents concur.
- **Big City Crushed Concrete, Sherman — FREE clean concrete, ~20 mi.** Best-margin lane: concrete
  disposal costs $31/load (driving only) vs $208 at 121 RDF.
- **Texas Pure, Plano — $22/CUBIC YARD green waste, $66 min.** Only confirmed commercial green-waste
  outlet in the radius. But **TASWA beats it on brush** ($102 vs $181/load) because brush is light and
  TASWA bills by the ton.
- **Garland Hinton $68/TON is the TRAILER rate** — $5/ton ABOVE the automated-truck rate. Trap.
- **Biggest hole: 380 McKinney C&D (~17 mi, Type IV) publishes no rate** and is probably the
  highest-volume destination. **Call 469-591-1380.** Also unpriced: WM Hillside Sherman (~16 mi,
  903-813-1905) and **Arcosa McKinney (972-504-0528) which reportedly PAYS for concrete.**

**Three refutations worth remembering** (each would have distorted the plan):
1. The dump-trailer "ban" is **not a ban** — NTMWD says a dump trailer "must pay for disposal
   services", i.e. it's disqualified from the FREE resident program, not barred.
2. **Transfer stations DO take C&D** (NTMWD Acceptable Waste Policy, Jan 2020).
3. **No $500/mo account required** — "Although not required." Card at the gate suffices.
4. Allen publishes NTMWD's **retired Sept-2024 rates** ($48/$65); live is $52/$75. Rule: operator's
   own current page > member city page > planning doc.

**Research integrity:** a sub-agent **fabricated results** (disclosed). All Cooke/Denton figures
(Denton Landfill, Gainesville) are quarantined as UNVERIFIED-POSSIBLY-FABRICATED — it transcribed fees
visually from scanned image PDFs. Grayson/Collin work is clean. **Wastebits is unreliable for this
region.** Camelot commercial access left as an OPEN CONFLICT. See
`documentation/methodology/source_verification_protocol.md`.

## Open / next

- Not yet built: fleet sizing, marketing CAC module, revenue/quote builder, charts. The outbound
  (supplier→customer) per-location cost table is also not built — only the disposal side is.
- Before any money: photograph the door-jamb FMVSS label; get the GCWR question answered in writing by
  a TX DPS CDL examiner; confirm Mega Cab DRW availability (contested, worth ~6,400 lb for $1,295);
  call McCraw; resolve Van Alstyne zoning (903-482-5426) on storing a commercial rig at the property.

Related: [[project_ram3500_autonation_deal]] (the truck purchase in flight — separate decision, do not
let it pick the business's equipment), [[user_github_and_devices]].
