---
name: feedback_verify_external_claims
description: "other repos are leads, not truth; 50+ numeric checks per fact taken in"
metadata:
  node_type: memory
  type: feedback
  originSessionId: dfe8eb70-bebc-45d2-b981-4703bed5ae51
  modified: 2026-11-07T15:58:40.658Z
---

**Summary moved from the memory index (2026-11-08):** Use other repos (especially Brokers) as leads, never as truth: every fact taken in gets 50+ numerical checks, time series checks, edge case flags, and a verdict from the tally

Treat what another repo or tool says (above all the Brokers repo) as good information to test, not as fact. Every claim RustTOS relies on gets at least 50 independent numerical checks, and the verdict comes from how many agree (all, a majority, or not confirmed), with every disagreeing check listed. Include time series checks (at least 3 families), edge case flags with how each is handled, broker tag checks, and checks that no data was lost or overwritten. Fix what can be fixed; flag the rest.

**Why:** the user said on 2026-11-07: "read brokers repo to see if the answer is already figured out there, but challenge and test it have multiple checks to make sure youre right" and "utilize broker repo as good information but dont trust it. need to verify everything in there especially if we use it with over 50 numerical checks per thing we pull into to make sure everything or majority agree". The checks then found the Brokers IBKR downloader had stripped bar time zones, which a single comparison had missed.

**How to apply:** in RustTOS run or extend `rusttos-source-checks` (see [[project_rusttos]]); a check that cannot judge must be skipped, not counted; make sure each checker is tested on a known bad case. Report verdicts with counts and the as-of time ([[feedback_verifiable_claims]]). Related: [[feedback_no_data_deletion]].
