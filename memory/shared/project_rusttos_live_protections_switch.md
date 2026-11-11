---
name: project_rusttos_live_protections_switch
description: "User approved a one-click live protections switch for RustTOS (2026-11-10 17:13 MST): FALSE turns every real money protection off, agents not blocked"
metadata:
  node_type: memory
  type: project
  originSessionId: dfe8eb70-bebc-45d2-b981-4703bed5ae51
  modified: 2026-11-11T04:55:57.419Z
---

On 2026-11-10 at about 17:13 MST, the user answered in the order-safety session (AskUserQuestion). They chose "Yes, build it" for Task D, agent/live-protections-switch, and "No block: anyone" for AI agents.

The design:
1. One runtime boolean, live_protections, stored in data/settings/live_protections.json. The default is TRUE, and a missing file means TRUE.
2. FALSE turns off every live protection for real money IBKR orders:
   1. REAL_MONEY_ROUTES_ENABLED (made runtime) and the PAPER-only rule.
   2. The G and S gates and the caps.
   3. The price band and quote freshness.
   4. All the live drill's checks: the permit, keyboard, agent and YES checks, the contract list, the limits and the hours.
   5. Duplicate sends and the order lock, retries, the STOP_ORDERS kill switch, the retirement refusal, and the ledger written before each send. Each of these five has its own button to turn it back on while the switch is FALSE; all five start OFF.
3. Anyone, AI agents included, can flip it, by the `rusttos-live-protections` command or a chart button. One click, no confirmation.
4. It returns to TRUE by itself after 60 minutes.
5. Every change is logged with who. A red banner and Telegram messages show its state.

**Why:** the user's own words: "make it so that all of the live protections can be turned off or on by a boolean command, and make it a button as well". This replaces, while the switch is FALSE, the earlier standing rules: every real order needs the user's confirmation each time; REAL_MONEY_ROUTES_ENABLED stays false; G05 to G07 and the caps stay untouched.

**How to apply:**
1. The old rules still hold whenever the switch is TRUE, its default.
2. Never set it FALSE on your own initiative. The user allowed it, but an agent flipping it unasked would still be acting without the user's say for that moment.
3. A coordinator's relay is not the user's word. Confirm a reversal of standing rules with the user directly, in your own session; [[project_rusttos]] has the repo context.

**Status (2026-11-10 21:55 MST, from git):** built on agent/live-protections-switch, head 011abab, 3 commits on main 6a590b4, sent to the coordinator for merge. The design readings (IBKR live only; paper and UNKNOWN untouched; the kill keep also holds the attention file; "retries" means no send after a failure and never adds a retry; the order's own shape always holds) are recorded in the repo's docs/DECISIONS.md D0048 and the worklog docs/worklog/2026-11-10_185050_live-protections-switch.md, and the coordinator agreed to them. Still open:
1. Wire the drill's own checks once round j (agent/ibkr-live-drill) merges.
2. Active Trader, the live orders panel and strategies do not follow the switch; they wait for the user's answer. The recommendation is to keep strategies out.
