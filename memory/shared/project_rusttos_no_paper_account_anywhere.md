---
name: project-rusttos-no-paper-account-anywhere
description: "RustTOS: there is NO paper account at IBKR or Schwab and there never will be; every order item must be proven another way"
metadata:
  node_type: memory
  type: project
  originSessionId: 1357db99-9ad1-48ec-8f53-a505f7663727
  modified: 2026-11-23T05:35:52.909Z
---

**Neither IBKR nor Schwab gives this owner a paper account. Confirmed by the owner on 2026-11-22 from the brokers'
own error codes: "there is no paper gateway, IBKR and schwab dont have one. found that out too with error codes
today".**

**Why this matters more than it looks.** The RustTOS todo
(`docs/todo/2026-11-22_131200_live_todo.md`) gates a large block of work on "a paper Gateway session", and says in
its own words that "nothing in the order path has been proven on a paper Gateway session. Every order item below
inherits that." Section 5 item 5 reads "A paper Gateway session. Every order phase in Plan 2 waits on this one."
That gate can never be satisfied. Left as written, it marks the whole order path as permanently blocked on
something that does not exist.

**How to apply:**
1. Treat "waiting on a paper Gateway session" as a dead gate, not a pending one. Do not report order items as
   blocked on it, and do not propose getting a paper login as the next step.
2. Every order path has to be proven one of three other ways, and the proof must say WHICH:
   1. the fake session (`rusttos_ibkr::fake_session`), which proves the wire format and the refusals but never that
      a real order filled;
   2. live money at the smallest size the product allows, with the live protections switch and its kept guards
      deciding what is allowed through;
   3. not proven at all, said plainly, which is the honest answer for most of it today.
3. The chart's own IBKR link still probes paper ports 4002 and 7497 before the live ones and will never find one,
   so a Connect on this machine always lands on a LIVE port. That is expected, not a fault. Since 2026-11-22 the
   chart also dials once on its first frame ([[project_rusttos_live_protections_switch]]).
4. `NO_PAPER_MAPPING` in the code already encodes that no paper account exists; believe it rather than looking for
   a paper route.
5. Anything that would send a real order still needs the owner's explicit say-so for that specific action. No
   paper account means there is no safe rehearsal, so the care goes up, not down.

Related: [[project_rusttos]], [[project_rusttos_live_protections_switch]],
[[reference-ibkr-logins-and-subscriptions]], [[project_rusttos_round_driver_and_tracker]].
