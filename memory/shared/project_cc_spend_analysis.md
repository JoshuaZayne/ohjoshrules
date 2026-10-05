---
name: project_cc_spend_analysis
description: "Yearly_and_monthly_spend_per_CC repo — AMEX + Fidelity spend analysis to Excel, private GitHub"
metadata: 
  node_type: memory
  type: project
  originSessionId: 820f93ef-faa6-419f-8b21-1800a569b535
---

Repo `~/repos/Yearly_and_monthly_spend_per_CC` (PRIVATE GitHub:
github.com/JoshuaZayne/Yearly_and_monthly_spend_per_CC). Analyzes credit-card +
bank spend per year/month/card and exports an Excel workbook.

**Sources** (copied out of iCloud `~/iCloudDrive/Documents/Credit Card Annual` into
`source_documents/`): AMEX Charles Schwab Platinum monthly statements (2026 Jan-Jun)
+ `YearEndSummary_2025.pdf` (full-year 2025, authoritative); Fidelity Visa (...1012)
CSV exports `Credit Card - 1012_*.csv` (Date,Transaction,Name,Memo[MCC],Amount);
Fidelity bank `transactions.CSV` (Date,Desc,Amount). Credit reports ignored.

**Parsers** in `src/parsers/`: `amex_pdf` (handles BOTH statement layouts — older
graphical Jan-Apr w/ ⧫ markers + newer May+; extracts charges by sign+desc, reconciles
to stated totals), `amex_yearend` (2025 txn detail w/ charge-vs-credit by word x-position,
threshold x1~520; + official category table), `fidelity_cc_csv` (col auto-detect + MCC
from Memo), `fidelity_bank_csv`. Categorizer `src/categories.py` = keyword rules + MCC
fallback; is_subscription forced True only when category=="Subscriptions".
Entry point `build_report.py` -> `output/Spend_Analysis_<ts>.xlsx` (14 sheets incl
Credit Cards, AMEX 2025 official, Bank Accounts, By Category x Year, Category x Month,
By Card x Category, Top Merchants, Recurring, Subscriptions, Utilities, Food, Monthly,
All Transactions) + `output/Spend_Trends_<ts>.md` (post-build hook; also `generate_trends.py`).
Tables carry TOTAL rows/cols. Recurring purchases show Card(s)=AMEX/Fidelity/Both per
year & per month. 2025 AMEX from year-end, 2026 AMEX from monthly statements (filtered
to year==2026 to avoid Dec-2025 double-count). Grand CC spend $106,557.56.

`validate.py` = 71 numerical reconciliation checks (tol $0.01): grand spend ties across
all aggregations, TOTAL rows == column sums, category pivot==detail, AMEX per-statement
charges==stated, AMEX 2025 net==$19,036.35 official, bank net, subs total. build_report
prints a quick reconciliation line each run. Gotchas found via checks: Venmo card-funded
transfers ARE spend but payment-reversals/returned-payment-fees are NOT; generic "market"
rule shadowed "AMAZON MARKETPLACE" (added high-priority retail-brand rules before grocery).
Uncategorized spend ~1.9% ($2,021, 6 one-offs). New hobby categories: Powersports &
Offroad, Firearms & Shooting, Tools & Hardware, Recreation & Sports, etc.

**iCloud gotcha** [[feedback_icloud_caution]]: cloud-only placeholders COPY AS NULL
(all-zero) files and reads time out; must verify non-zero content before trusting a copy.
`refresh_from_icloud.py` re-pulls with that verification. 4 non-essential files never
hydrated (2 credit reports, 2 redundant) — see source_documents/_PENDING_REDOWNLOAD.md.
Roadmap: CodeMapping_Brain/content/roadmaps/2026-06-28_235815_yearly-monthly-cc-spend.md
