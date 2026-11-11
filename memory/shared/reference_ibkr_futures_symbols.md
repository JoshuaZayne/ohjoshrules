---
name: reference-ibkr-futures-symbols
description: "How IBKR (TWS API / IB Gateway) wants futures and futures options named: fields, currency symbol names, one digit year, exchanges, option classes; checked 2026-11-11"
metadata:
  node_type: memory
  type: reference
  originSessionId: c27e3dc7-dd5d-4152-87c8-5c524b19ecf8
  modified: 2026-11-11T07:40:26.644Z
---

How to ask IBKR for any future (metals, currencies, energy, indices, rates). Verified 2026-11-11 00:16 to 00:18 MST by a read only probe against the live IB Gateway (contract details and symbol search only), and against the RustTOS root table `crates/rusttos-ibkr/src/contracts.rs` lines 51 to 98 at main 78df09b. Related: [[project_rusttos]].

NO special characters. No leading slash (Schwab/TOS `/6EZ26` is Schwab only), no exchange suffix, no colon. A contract is separate fields:
1. symbol (IBKR's name, see below), security type `FUT` (options `FOP`), exchange (REQUIRED for futures: `CME`, `CBOT`, `NYMEX`, `COMEX`; leaving it empty fails), currency `USD`.
2. contract month `YYYYMM` (e.g. `202612`), or the exact last trading date `YYYYMMDD`; EMPTY month returns every listed month (PL gave 14, PLX6 to 2028).
3. trading class = the CME root (`6E`, `PL`); set it so one product comes back when a symbol covers several.
4. local symbol (IBKR's ticker) uses a ONE digit year: `6EZ6`, `PLF7`, `PLX6` (Schwab writes `PLF27`). Asking by local symbol plus exchange also works.
5. Most exact: IBKR's numeric contract id (e.g. 680895289 = PLF27). RustTOS looks ids up once and stores them in `data/reference/ibkr_contracts.csv` (265 rows as of 2026-11-11).

Symbols that DIFFER from the CME root (currencies use the currency name; the CME code goes in trading class):
1. 6E = EUR, 6B = GBP, 6A = AUD, 6C = CAD, 6J = JPY, 6S = CHF, 6N = NZD, 6M = MXP (not MXN).
2. Micros keep their own root as the symbol: M6E, M6A, M6B, MSF, MCD, MJY.

Same as the CME root (symbol, exchange):
1. Metals on COMEX: GC, SI, HG, MGC, SIL, MHG. Platinum PL on NYMEX (multiplier 50).
2. Energy on NYMEX: CL, NG, HO, RB, MCL, QG, QM.
3. Indices on CME: ES, NQ, RTY, EMD, NKD, MES, MNQ, M2K, MNK; on CBOT: YM, MYM.
4. Rates on CBOT: ZN, ZB, UB, TN, ZF, ZT, ZQ; on CME: SR1, SR3.

Futures options (`FOP`): local symbol has ONE space, `OGZ6 C1870` (gold Dec 2026 call 1870). The option trading class differs from the future's. The RustTOS collector's standard monthly class table (`crates/rusttos-ibkr/src/fop_class_choice.rs` STANDARD_CLASSES): 6E EUU, 6B GBU, 6A ADU, 6J JPU, 6C CAU, 6S CHU, GC OG, SI SO, HG HXE, PL PO, NG LNE, CL LO. Weeklies have other classes (gold Dec 2026 returned 9 classes: OG, OG1, G1M, G1R, G1T, G1W, G2R, G2T, G3T); pick the standard class first or a weekly gets used by mistake (happened 2026-11-10 with 2CD and H2W).

IBKR has NO platinum (PL) or palladium (PA) futures options: symbol search lists PL (IND, NYMEX) with derivatives FUT, IOPT, BAG only; every FOP lookup (PL on NYMEX 202612 to 202703, class PO, symbol PO, no exchange) said "No security definition"; the GC COMEX control returned 2,634 rows. Probe output: `F:\GitHub Repos\RustTOS_agents\status_page\platinum_probe_2026-11-11_001644.txt`.

**How to apply:** when adding a new futures root to an IBKR reader, put it in the contracts.rs root table with IBKR's symbol, exchange, multiplier and tick; check an unfamiliar root first with a contract details call that leaves the month empty (reference data only, no market data). Palladium futures checked 2026-11-11 00:42:05 MST: PA on NYMEX, multiplier 100, tick 0.5, class PA, quarterly H M U Z plus near serial months (PAX6 to PAU9); being added to the root table on agent/ibkr-palladium (not merged as of 2026-11-11 00:45 MST).
