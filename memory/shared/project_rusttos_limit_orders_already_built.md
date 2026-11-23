---
name: project-rusttos-limit-orders-already-built
description: "RustTOS todo item 31 is WRONG: Active Trader's limit ticket, price box, stop and target boxes all exist; only DAY/GTC is missing, and that is blocked by safety check K06"
metadata:
  node_type: memory
  type: project
  originSessionId: 1357db99-9ad1-48ec-8f53-a505f7663727
  modified: 2026-11-23T10:46:53.383Z
---

**The RustTOS live todo's item 31, "Active Trader has no limit orders", is wrong, and it is wrong in a way that
blocks other work.** It marks item 30 (buying a euro contract) and complaint 34's third ask (quick executions) as
blocked on something that is already built.

**What actually exists, read on 2026-11-23:**

1. `crates/rusttos-chart/src/chart_app/limit_ticket.rs`, 714 lines, whose own first line reads: "Active Trader's
   visible limit ticket: a price box for each side, the Buy LMT and Sell LMT buttons, and the line of words that
   says what a press would send." It is drawn from `active_trader.rs:1493`.
2. The price box per side, with a minus and plus button that step one tick, and a Bid or Ask button that puts the box
   back to following the inside market.
3. The stop box AND the target box, both in ticks: `draw_bracket_ticks` at
   `crates/rusttos-chart/src/chart_app/live_orders_panel.rs:2167`, drawn on the limit row itself, where 0 reads
   "none" and sends no stop or target.
4. `press_limit_ticket` hands the box's price to `press_order`, the same path a ladder click uses: the same pricing,
   the same checks, the same receipts, no second way out.

**Why the todo's search missed it:** item 31 says "`active_trader.rs` is 1,919 lines and offers exactly two order
kinds". It searched inside that ONE file. The limit ticket is a separate module that `active_trader.rs` calls.

**The one thing genuinely missing, and it is not missing by accident: DAY or GTC.** `LIMIT_LIFE_WORD` is the fixed
text "DAY" and `LIMIT_LIFE_NOTE` says why. A good till canceled entry is refused by a real money safety check:
`crates/rusttos-core/src/live_orders.rs:317`, check **K06**, "the order lasts today only (DAY, never good till
canceled)". `order_ticket.rs:254` hardcodes `OrderDuration::Day` to match.

**How to apply:**
1. Do not rebuild the limit ticket. Read `limit_ticket.rs` first.
2. Adding a GTC choice means LOOSENING K06, which is a real money protection. That needs the owner's explicit say so
   for that specific change, and it should be asked as a decision, not slipped in as part of a feature.
3. Items 30 and complaint 34's third ask are NOT blocked by 31 as written. What they are actually waiting on should
   be re-read before anyone reports them blocked again.
4. The same caution applies to the rest of section 3: its verdicts came from searching single files, and at least
   this one was wrong in the direction of "not built" when it was built.

Related: [[project_rusttos]], [[project-rusttos-no-paper-account-anywhere]],
[[project_rusttos_live_protections_switch]], [[project_rusttos_round_driver_and_tracker]].
