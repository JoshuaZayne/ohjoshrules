---
name: project-schwab-seasonality-gallery
description: Active roadmap to add OLS seasonality testing + per-timeframe futures chart gallery to the Schwab notebooks
metadata: 
  node_type: memory
  type: project
  originSessionId: b0cc7eca-7d03-44e1-b161-622a272d4070
---

Active build in ~/repos/Brokers Schwab notebook suite (started 2026-05-24): (1) OLS seasonality
testing (month-of-year + day-of-week return effects, HAC standard errors, joint F-test; optional
futures term-structure seasonality from curve snapshots) in a new `12_seasonality.ipynb`, backed by
a tested `scripts/schwab/nb_seasonality.py` helper; (2) a per-timeframe futures gallery that graphs
every continuous futures root at each stored interval (1m..4h,1d) using `available_intervals`.

Roadmap: ~/repos/CodeMapping_Brain/content/roadmaps/2026-05-24_224700_schwab-seasonality-and-futures-gallery.md

Key facts: statsmodels was MISSING in the host kernel (C:\Python314) and needs install (scipy +
mplfinance present); notebooks run host-side only (no broker import); daily store ~1255 trading days
(~5y) per future. Part of the broader [[project_brokers_market_data_pipeline]].
