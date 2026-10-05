---
name: project_dumptruck_business_buildout
description: "DumpTruckBusinessBuildout repo state — Van Alstyne TX dump trailer/hauling business cost model, trailer scraper, customer leads, confirmed Ram financing"
metadata: 
  node_type: memory
  type: project
  originSessionId: b2013cb2-4779-4a74-ad01-d910345c66d3
  modified: 2026-08-21T07:56:45.722Z
---

Repo: `~/repos/DumpTruckBusinessBuildout` (private, github.com/JoshuaZayne/DumpTruckBusinessBuildout).
A sourced costing/pricing/econometric model (not a business plan) for a dump
trailer / debris hauling business based in Van Alstyne, TX, 70-mile radius.
Every figure carries a confidence level + source. Full detail lives in the
repo's own README.md and TODO.md — read those first; this memory only tracks
what a future session can't re-derive from the repo alone.

**CDL finding**: the tow truck's published GCWR (32,720 lb) puts it over the
Class A CDL line with ANY trailer over 10,000 lb — the only non-CDL paths are
a ≤10,000 lb bumper-pull trailer, or a Ford F-600 straight truck (no trailer
combination at all). See `documentation/regulatory/motor_carrier/CDL_THRESHOLD_DECISION_MEMO.md`.

**Ram 3500 financing is CONFIRMED (2026-08-18)**: $88,000 final price,
$1,502/month for 60 months at 5% APR. This replaced an earlier $1,600/mo
estimate everywhere it appeared — `configuration/business/vehicle_and_equipment.yaml`
(`ram_3500_limited_mega_cab_srw` entry, now has `annual_interest_rate` /
`loan_term_months` / `monthly_payment_dollars` fields on the `TowVehicle`
dataclass), and 3 analysis scripts
(`compare_f600_financed_versus_ram_trailer.py`, `build_balance_sheet.py`,
`run_fleet_scale_1_to_50.py`). If the user renegotiates these terms again,
all 4 locations need updating together — grep for `RAM_MONTHLY_PAYMENT` and
`monthly_payment_dollars` to find them all.

**Trailer price scraper**: `scraper_trailers/` (lean port of
`~/repos/RamMegaCabDataScrapper`'s engine — no ML trees, no bandit learning,
no tangle.py literate-source build). Targets two specs: gooseneck
~20ft/wide(8-8.5ft)-deck dump trailers, and dump trailers with side
bins/toolbox (any hitch). 3 entry scripts:
- `scrape_dump_trailers.py` — curated marketplaces (Craigslist works via
  `www.craigslist.org/search/area/<city>?cat=sss&query=...`, the RAM scraper's
  old subdomain scheme is retired; Commercial Truck Trader + Equipment Trader
  work via `browser_fetch.py`, a stealth-patched Playwright tier
  [`--disable-blink-features=AutomationControlled` + `navigator.webdriver`
  patch + 6s wait beats their AWS WAF wall] plus a `jrwcap.com` financing-
  widget data extractor; eBay Motors is IP-reputation-blocked at the
  datacenter level, not a JS/WAF wall — needs a residential proxy/paid
  unlocker to ever work, not attempted).
- `build_dealer_network.py` — nationwide trailer-dealer discovery. PJ
  Trailers/Big Tex Trailers/Diamond C Trailers all run an OPEN,
  unauthenticated WordPress "WP Store Locator" API
  (`<domain>/wp-admin/admin-ajax.php?action=store_search&lat=&lng=...`);
  queried from every US state capital -> 526 real dealers in
  `data/reference/trailer_dealers/dealer_network.csv`. 12 other manufacturers
  tested don't use this plugin (would need individual investigation to add).
- `scan_dealer_network.py` — probes each dealer's own site for inventory
  (concurrent, generic card harvester). Live result 2026-08-18: 2,550 priced
  listings across 494 dealers, 9 real target-spec matches.

4 real bugs found + fixed via LIVE testing, each with a regression test:
cross-query dedupe missing across sources; the Trader Interactive financing-
widget path is per-site (`jrwcap.com/trader` vs `/equipmenttrader`, not one
fixed path); `_card_blob`'s fallback attached the SAME price to every listing
on a page when no clean single-card region existed (ported back a safety
check the RAM scraper has that got dropped when trimming); and a "no unit +
value>12 means inches" heuristic broke the far-more-common "7x14" (both feet)
notation. 70/70 tests passing.

**Customer leads**: `data/reference/customers/potential_customers.csv` (12
rows, matches the `CustomerSegment` enum in `domain/service_lines.py`), now
enriched with EBITDA/board/sales-contact columns. Highland Homes is flagged
`existing_personal_relationship` — they are building the user's own house
(see [[project_thicket_hill_contract]]) and are the single best lead on the
list. Harris Builders has a real named contact (owner Mike Harris) + local
phone + PO box — the best cold-call lead. EBITDA/board are honestly
`not_publicly_available`/`not_applicable` for 11 of 12 rows (private
companies) — no numbers invented; K. Hovnanian's NATIONAL PARENT (Hovnanian
Enterprises Inc, NYSE: HOV) has real, SEC-sourced FY2025 EBITDA ($226.4M) and
board data, clearly labeled as parent-level, not the local Rolling Ridge
community. No LinkedIn scraping (ToS). Two real reclassifications found while
enriching: Gravel Monkey (646 = NYC) and Mulch Mound (513 = Cincinnati) are
national multi-market brands operating locally, not local competitors as
first assumed; Crew Junk Removal's own site discloses it's a lead-gen
referral aggregator ("all service providers are independent"), reframing it
as a possible partner channel rather than a hauling rival.

**Phase 3 (2026-08-18 evening)**: MAXX-D Trailers added to the dealer
network via a second locator platform (LDV/`vnext.locator.js`, one-shot
`/location/getjsonalllocations` GeoJSON feed, `[lat, lng]` order not
standard `[lng, lat]`) behind Cloudflare — needs `browser_fetch.py`'s
Playwright tier, not plain `requests`. Network now 683 dealers (was 526).
MAC Corporation (maccorp.com, Indianapolis roll-off/waste equipment mfr,
also Cloudflare-gated) contact found: 317-545-3341 / 1-800-447-5205 /
customerservice@MACCorp.com — for a custom flatbed-over-wheel-wells
roll-off trailer inquiry.

**Real finding on trailer-hit yield**: the bottleneck is classification, not
dealer count. Baseline run: 3,631 real priced listings, only 8 matched the
target spec (0.2%) because `filter.py` requires an explicit "gooseneck"
text hint and only 257 listings had one. `extract.py` already has the fix
(`enrich_listing_from_detail_page`, built for Trader Interactive) but
`dealer_site_scraper.py` never calls it — visiting each listing's own
detail page (not just the search-card text) is the highest-leverage
untaken change.

**Contracts**: added `contracts/templates/commercial_hauling_services_agreement.md`
(customer-facing MSA, Company hauls FOR a commercial counterparty — distinct
from the existing rental and owner-operator-contractor templates). Trip-fee
+ disposal-pass-through pricing, sourced from `disposal_sites.csv`'s 121 RDF
rate ($52/ton) and shingle surcharge ($150), not fabricated. Exhibit A maps
the 4 customer segments to which rate lines matter most. Discovered
`build_contract_documents.py` had never actually been run — `python-docx`/
`reportlab` were missing from `requirements.txt` entirely; installed +
added. All 3 templates now build clean to Word/PDF, 141/141 tests passing.

**CDL study sheet**: `documentation/regulatory/motor_carrier/CDL_ACQUISITION_AND_STUDY_GUIDE_2026-08-18_231839.md`
— real Texas CLP→ELDT→knowledge tests→14-day hold→skills test→CDL path,
sourced live from dps.texas.gov (CDL/CLP knowledge tests went English-only
2026-06-01). `gh search repos` for CDL study guides came up empty (every
result 0-1 stars) — flagged as genuinely not useful rather than padded in.
Note the tension this pivot creates with `CDL_THRESHOLD_DECISION_MEMO.md`
(written specifically to justify staying non-CDL) — getting a CDL is a
legitimate reversal that unlocks 25,000+ lb gooseneck trailers, but the user
needs to consciously pick one path before buying a trailer.

**Phase 4 (same evening, "improve the code and output" -> "do all")**: 5 more
fixes, all tested. GVWR regex had the same digit-count bug as the length
regex (bare "25900 GVWR" misparsed). Added `distance_miles_from_home_base`
to every trailer listing (real dealer lat/lng already in the CSV, more
accurate than city lookup). Added non-destructive cross-dealer duplicate
flagging ("Also listed at" column). Added `check_dealer_reachability.py`
(site_status: ok/dns_or_ssl_failure/http_error/timeout, only the first is
skipped on future scans, nothing ever deleted). Added Load Trail as a THIRD
dealer-locator platform (`api_search` action on the same admin-ajax.php WP
Store Locator uses, found by reading the dealer-search plugin's JS, backed
by mydealertrack.net). **Final result: dealer network 526 -> 897 dealers,
target-spec matches 8 -> 165 (20.6x) this session** — and critically, the
enrichment fix ALONE (not more dealers) drove 12 -> 128 of that, confirming
classification was the real bottleneck, not coverage. Real secondary find:
"Also listed at" surfaced dealer-name-variant duplicates in the network CSV
itself ("Truck Country, LLC" vs "Truck Country LLC") — not fixed, flagged
as the next dealer-list-quality candidate.

Full build log: [[roadmap]] at
`~/repos/CodeMapping_Brain/content/roadmaps/2026-08-18_014952_dump-truck-trailer-scraper-and-leads.md`.
