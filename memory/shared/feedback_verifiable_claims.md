---
name: feedback_verifiable_claims
description: "Every data claim to the user must carry its source and the exact as-of time with time zone, and be re-checkable by them"
metadata:
  node_type: memory
  type: feedback
  originSessionId: d8a60bec-334c-4db0-9f39-6d64b4103cad
  modified: 2026-10-11T09:48:25.661Z
---

When reporting market data, prices, freshness or any measured fact, state: the source (file path or API), the exact as-of timestamp with time zone (exchange time and the user's Mountain time, or UTC), and how the user can re-check it (command, report file, or dashboard panel). Separate "verified" from "inferred", and say plainly when something is stale or unverified.

**Why:** 2026-10-11 the user asked "how do we know that chart for the ES is correct and most up to date" and "I need better ways to verify the information you are giving me is accurate to the exact time you are saying its accurate."

**How to apply:** For Brokers market data, run `python scripts/dashboard/verify_bars.py <SYMS> --crosscheck` (writes data/dashboard/verify/verify_<SYMS>_<timestamp>.json/.txt) and quote its numbers with the report path. Distinguish FRESH/STALE (market open) from UP TO DATE/BEHIND (market closed). Never call data "current" from a file mtime; use the newest bar timestamp. Related: [[project_schwab_dashboard_trading]], [[feedback_file_timestamps]].
