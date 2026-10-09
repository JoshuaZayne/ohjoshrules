---
name: project_ema_touch_futures_roadmap
description: "Active roadmap (2026-10-08) for EMA Touch Counter futures accuracy + watchlist loading; chart touch math verified sound, real causes identified"
metadata:
  node_type: memory
  type: project
  originSessionId: a981feae-b13a-47c4-a2a2-18ce9032dcc7
  modified: 2026-10-09T00:45:15.348Z
---

Roadmap: `F:\GitHub Repos\CodeMapping_Brain\content\roadmaps\2026-10-08_182227_ema-touch-futures-accuracy-and-watchlist-loading.md`.

Primary repo is `C:\Users\ohjos\indicators` (GitHub JoshuaZayne/indicators), mirrored file-for-file into `C:\Users\ohjos\ThinkScript_Studies` (see [[project_thinkscript_version_tracking]]). Antigravity wrote most of it.

Findings: the chart touch engine misses 0 visible touches in simulation. Wrong or non-resetting counts come from the AEMA being seeded at a different first bar when the watchlist (or a short chart time span) loads fewer bars (200/365 need roughly 3 x length bars), from futures EXT session mismatch, from the stale EMA_Touch_Watchlist_Column.txt, and from the ~1,200 to 1,500 custom cell limit in TOS. The diagnostics column has an enum typo that should stop it compiling.

Real-data study tool: `indicators/ThinkOrSwim/EMA Count/ema_touch_timeframe_study.py` (--self-test, --summarize). Its data comes from Brokers `data/ibkr/csv/ohlc_*.csv`, which are git-tracked but deleted from the F: working tree; read them with `git show HEAD:<path>`, don't restore 4 GB. Native IBKR 2h/4h bars overlap (mixed anchors) so rebuild from 1h; timestamps are CT. Key result: 3/6 lengths touch ~every bar; streak percentiles are timeframe invariant, so one per-length threshold set fits 1m through 4D.

**Why:** User needs exact touch resets on the 4h for futures entries and wants changes that only improve, not churn.
**How to apply:** Read the roadmap's Steps before touching these studies; keep chart and watchlist math identical; don't edit ARCHITECTURE.md without asking ([[feedback_dont_edit_existing_md]]).
