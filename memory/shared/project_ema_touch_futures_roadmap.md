---
name: project_ema_touch_futures_roadmap
description: "EMA Touch Counter futures accuracy, cross-currency inverse DXY proof, random forest ribbon folding cross-validation, 100 to 200 EMA conditional touch probabilities, 22 EMA daily overextension streaks, and standalone interactive web visualizers"
metadata:
  node_type: memory
  type: project
  originSessionId: a981feae-b13a-47c4-a2a2-18ce9032dcc7
  modified: 2026-10-12T23:35:00.000Z
---

Active Roadmaps:
1. `F:\GitHub Repos\CodeMapping_Brain\content\roadmaps\2026-10-08_182227_ema-touch-futures-accuracy-and-watchlist-loading.md`
2. `F:\GitHub Repos\CodeMapping_Brain\content\roadmaps\2026-10-12_150800_ema-cross-currency-dxy-inverse-analysis.md`
3. `F:\GitHub Repos\CodeMapping_Brain\content\roadmaps\2026-10-12_153500_random-forest-ema-folding-strategy.md`
4. `F:\GitHub Repos\CodeMapping_Brain\content\roadmaps\2026-10-12_162000_ema-touch-trading-strategy-architecture.md`
5. `F:\GitHub Repos\CodeMapping_Brain\content\roadmaps\2026-10-12_162800_interactive-web-dashboards-live-strategy-and-backtesting.md`

Primary Repositories:
1. `indicators` (GitHub JoshuaZayne/indicators): ThinkOrSwim/EMA Count/ contains thinkScript studies, master analysis workbooks, and visualizers.
2. `Brokers_merge` (GitHub JoshuaZayne/Brokers, branch Dimaskus_Surface_merge): contains `gui/ema_touch_strategy_backtest_dashboard.html`, live strategy showcasing in `scripts/dashboard/static/index.html` and `js/chart.js`, and Flask route `/backtest`.

Key Empirical Findings and Statistical Architecture:
1. Cross-Currency Inverse DXY Validation:
   - 6E (-0.985), 6B (-0.972), 6J (-0.968), 6S (-0.981), and 6M (-0.991) exhibit decisive negative correlation against DXY.
   - Separate master workbooks generated: `ema_currency_analysis_6B.xlsx`, `6J.xlsx`, `6S.xlsx`, `6M.xlsx`, and `ema_cross_currency_dxy_inverse_and_touch_master.csv`.
2. Higher Timeframe Touches and Streak Distributions:
   - Evaluated 55, 100, 200, and 365 EMAs.
   - On 4H, 6E completed 122 candles separated below 100 EMA (99.5th percentile historically, all-time record 130 candles).
   - On Daily, 22 EMA overextension shows 626 historical streaks: all-time record 60 daily bars, mean 6.87 bars, median 4.0 bars. Current live streak stands at 20 daily bars below (93.5th percentile). Saved to `6E_daily_22_ema_past_50_streaks_2026-10-12_232000.xlsx`.
3. Random Forest Cross-Validation and EMA Ribbon Folding:
   - Tested K-Fold, Stratified K-Fold, Group K-Fold, TimeSeriesSplit, Leave-One-Out, and Nested CV.
   - Discovered that when Stage 1 fold occurs (12 crosses 22), follow-through to 100 EMA has 98.0% probability on 4H (median lead 5.5 candles / 22 hrs) and 96.0% on Daily.
   - When Stage 2 barrier clears (close above 55 EMA), probability of touching 100 EMA is 93.5% on 4H and 97.2% on Daily.
4. 100 EMA to 200 EMA Conditional Probabilities and Duration:
   - Daily (1-Day): 90.34% overall (131/145); 91.67% when approaching from below (66/72). Median duration to touch 200 once 100 is hit is 6.5 to 7.0 trading days.
   - 4-Hour: 100.0% follow-through (46/46). Median duration to touch 200 once 100 is hit is 9.0 to 9.5 candles (36 to 38 hours).
5. Trend Change Determination (100 EMA vs 200 EMA):
   - 100 EMA determines the intermediate / cyclical trend inflection (momentum pivot), but carries a 40.6% whipsaw rate on Daily.
   - 200 EMA determines the macro secular trend (institutional regime), requiring daily candle close acceptance, dynamic support flip, and 100/200 Secular Cross (which averages 190.4 daily bars per cycle).
6. Interactive Dashboards:
   - Standalone visualizer: `gui/ema_touch_strategy_backtest_dashboard.html` and `scripts/dashboard/static/backtest.html` (served via `http://127.0.0.1:8765/backtest`).
   - Live chart showcasing: toolbar buttons `⚙ 100-Touch Strategy` and `📈 Backtest Visualizer` in `scripts/dashboard/static/index.html`.
