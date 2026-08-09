---
name: project_boxspread_analysis
description: "BoxSpreadAnalysis repo - box spread financing analytics + ZN/ZB Treasury math, and the SPY/EXO product corrections it encodes"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4bab8f0e-4cff-416f-9d8c-704913e26353
  modified: 2026-08-09T08:32:01.288Z
---

**BoxSpreadAnalysis** (created 2026-08-09) lives at `F:\GitHub Repos\BoxSpreadAnalysis`,
pushed to **private** repo `github.com/JoshuaZayne/BoxSpreadAnalysis`.

Analyses box spreads (4-leg option structure = a fixed-rate zero-coupon loan) and
ZN/ZB Treasury futures. Core is **stdlib-only** so it runs on desktop/laptop/USB/Pi.
Run with the Anaconda 3.9 python already on PATH; `python -m pytest` (285 tests).
CLI: `python -m boxspread.cli {box,scan,product,bond,futures,convert}`.

**Product facts it encodes that the user's original list had wrong:**
- **SPY is NOT European** - it's American-style, physically settled. Worst possible
  box underlying (early assignment + ex-dividend assignment). Marked box-ineligible.
  **XSP** is the correct substitute (same notional as SPY options, European, cash
  settled, Section 1256).
- **"EXO" is not a listed root** - the European S&P 100 option is **XEO**. Its
  American twin **OEX** is one transposition away and unsafe for a box. Aliased with
  a warning.
- **"SPEOX" could not be identified** against any Cboe root; lookup raises rather
  than guessing (SPESG and XEO suggested as likely intent).

**Treasury gotchas encoded:**
- 32nds sub-tick digit is **eighths printed as floor(fraction*10)**, not tenths.
  `110'165` = 110.515625, NOT 110.165. Digits 4 and 9 never appear.
- **ZN ticks in HALF-32nds at $15.625**, not ZB's 1/32 at $31.25. Ironbeam's spec
  page has this wrong; CME and Barchart confirm the half-tick.
- ZB is called the 30-year contract but its basket has been 15 to under 25 years
  since the 2011 UB split.

**Schwab adapter** (`boxspread/brokers/schwab_client.py`) is wired but unconfigured:
uses the `schwab-py` already installed in Anaconda, reads creds from a gitignored
`.env` (see `.env.example`). Needs an app at developer.schwab.com in "Ready For Use"
state; keys from a still-pending app authenticate then 401 on data.

Design decisions worth remembering: exercise style is a first-class type (copied from
QuantLib) so no code path can price a box without seeing it; `universe.get_product()`
**refuses** to guess an exercise style for unknown roots. See `docs/research_notes.md`
for the open-source survey (py_vollib test patterns, FinancePy conversion factor,
and the five things ibkrbox/chiaolun box calculators leave out).

Related: [[user_github_and_devices]], [[feedback_cross_device_paths]],
[[project_thinkscript_version_tracking]]
