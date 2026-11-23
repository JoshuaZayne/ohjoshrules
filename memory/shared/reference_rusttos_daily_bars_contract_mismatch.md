---
name: reference-rusttos-daily-bars-contract-mismatch
description: "RustTOS daily charts fall back to Schwab because IBKR's single contract file is compared against Schwab's continuous front month; measured 2026-11-22"
metadata:
  node_type: memory
  type: reference
  originSessionId: 1357db99-9ad1-48ec-8f53-a505f7663727
  modified: 2026-11-23T05:36:14.728Z
---

**RustTOS daily charts draw Schwab's bars, not IBKR's, and the reason is a comparison fault, not bad IBKR data.**

**What the chart logs at every start** (6E, 2026-11-22):

```
1_day: IBKR not trusted (NOT CONFIRMED: only 11.9 percent of 67 decided checks agree), so Schwab's 5,970 bars
```

Every other store goes IBKR first and is trusted: 1_min 735,366 IBKR bars (232,765 over Schwab's, 502,601 where
Schwab had none), 5_min 6,819, 15_min 5,117, 30_min 2,968. Only 10_min falls back for an honest reason, which is
that IBKR holds no 10 minute files at all.

**The gate** is `KIND_DAILY_CLOSE` in `crates/rusttos-feed/src/joined_history.rs`, "the trade date's daily close is
within one tick of Schwab's", needing 90 percent agreement over at least `MINIMUM_DECIDED_CHECKS` (50) decided
days, judged by `ClaimTally::verdict` in `crates/rusttos-feed/src/source_checks.rs`.

**Measured 2026-11-22 22:30 MST**, comparing `data/curve/history/source=ibkr/timeframe=1_day/6EZ26.parquet`
against the daily rows of `data/joined/2026-11-22_154039/timeframe=1_day/6E.parquet`:

1. 1,050 shared dates. **1,050 of 1,050 differ by more than one tick.** Not a near miss.
2. The difference is a steady positive offset of about +0.013 to +0.014, roughly 270 ticks of 0.00005, and it
   DECAYS over time: +279 ticks on 2026-02-04, +215 by 2026-02-20.
3. The IBKR file is one contract for its whole life, 2021-12-14 to 2026-02-20, and has no `contract` column.
4. The joined daily file is 100 percent `schwab` rows with an empty `contract` column.

**The cause.** `6EZ26` is the December 2026 contract. Schwab's `6E` daily is a continuous front month series. For
most of Z26's life the front month was much nearer, so Z26 traded a carry premium above it, and carry shrinks as
expiry approaches, which is exactly the decaying offset above. A far dated contract compared against a continuous
front month can never agree within one tick, so the gate rejects IBKR's daily every time and will keep doing so.

**How to apply:**
1. The gate is doing its job. Do not loosen the threshold, and do not call IBKR's daily data bad: it is the pairing
   that is wrong.
2. The fix belongs in what gets compared: pair IBKR's contract file against Schwab's bars for THAT SAME contract
   month, or roll IBKR's contracts into a continuous series by the same rule Schwab's continuous series uses,
   before the daily check runs.
3. A quick way to confirm any fix: the per row `source` and `contract` columns of
   `data/joined/<stamp>/timeframe=1_day/<root>.parquet`. Today it is all `schwab`; a working fix shows `ibkr` rows.
4. The same shift diagnostic in `data/reports/source_checks_*.txt` already hints at it with median gaps far too
   large to be timing: 6E 15_min 0.004556, and 6J 0.008387 on a price near 0.0065, which is larger than the price
   itself.
5. Not an RTH problem: every IBKR history request in the repo already asks `TradingHours::Extended`.

Related: [[project_rusttos]], [[reference-ibkr-futures-symbols]], [[project_rusttos_state_2026-11-22]].
