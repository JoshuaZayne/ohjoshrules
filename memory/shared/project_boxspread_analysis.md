---
name: project_boxspread_analysis
description: "BoxSpreadAnalysis repo - box spread financing analytics + ZN/ZB Treasury math, and the SPY/EXO product corrections it encodes"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4bab8f0e-4cff-416f-9d8c-704913e26353
  modified: 2026-08-09T18:35:34.741Z
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

**MEASURED Schwab commissions (2026-08-09)** — extracted from 76 option trades in
the Schwab brokerage statements (`Yearly_and_monthly_spend_per_CC`, accounts
765/620/604/060, 2025-12..2026-07). Statement rows annotate each trade
`Commission$0.65;IndustryFee$0.01`:
- **Options: flat $0.65/contract commission + ~$0.0113/contract IndustryFee = ~$0.66
  all-in.** ($1.30/2 contracts, $1.95/3 — commission is strictly per contract.)
  Schwab bundles the ORF into "IndustryFee"; there is no separate ORF line.
- **CRITICAL CAVEAT: zero index-option trades on record.** All 76 were single-name
  equity options, so there is NO evidence whether Schwab passes a Cboe index
  licence fee on SPX/RUT/NDX. Repo ships a matched pair to bracket it:
  `schwab_index` (default, $0.6613, no surcharge) and `schwab_index_conservative`
  ($1.1113, +$0.45 assumed). Difference = 0.4 bp on a 10-lot 1000-wide SPXW box,
  ~14 bp on a 1-lot 25-pt XSP box.
- **Futures: $2.25 commission + $1.60 exchange + $0.02 NFA per contract per side
  = $3.87/side, $7.74 round turn.** Observed fills were energy contracts, NOT
  ZN/ZB — exchange fee varies by exchange (Treasuries clear CBOT), so treat $1.60
  as indicative.

**Schwab auth reuses the Brokers repo** (see [[project_brokers_schwab]]) — no second
app needed. `schwab_client.py` loops candidate credential files: this repo's `.env`,
then `Brokers/.env.secrets` (real values), then `Brokers/.env` (config + placeholders),
matching Brokers' own load order. The loader **skips `${PLACEHOLDER}` values** or it
would authenticate with the literal string. Check state with
`python -m boxspread.cli schwab-status` (prints no secrets; exits non-zero if the
token is stale).

Design decisions worth remembering: exercise style is a first-class type (copied from
QuantLib) so no code path can price a box without seeing it; `universe.get_product()`
**refuses** to guess an exercise style for unknown roots. See `docs/research_notes.md`
for the open-source survey (py_vollib test patterns, FinancePy conversion factor,
and the five things ibkrbox/chiaolun box calculators leave out).

Related: [[user_github_and_devices]], [[feedback_cross_device_paths]],
[[project_thinkscript_version_tracking]]
