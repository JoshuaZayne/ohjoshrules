---
name: MooMoo API quota limit
description: MooMoo account has 300 total API pulls and HK Level 1 only — no US market data rights
type: project
---

MooMoo account (ID: 74699106) has a 300 total pull quota and HK Level 1 market data rights only. No US market data subscription.

**Why:** Free tier MooMoo account has limited API pulls. Must conserve carefully.

**How to apply:** Never run MooMoo data collectors without considering quota burn. Use long poll intervals (5+ minutes), limit to HK stocks only (ACTIVE_SYMBOLS), and stop collectors when not actively needed. Always warn before starting data collection scripts. The historical downloader especially burns quota fast — only run for specific targeted downloads.
