---
name: project_spend_intake_and_accounts
description: Document intake dropbox + the parsed-account/statement structure in the Yearly_and_monthly_spend_per_CC repo (how to add new statements and have the report build off them)
metadata: 
  node_type: memory
  type: project
  originSessionId: a9e289a4-d2cb-453d-8b06-5e7ae5ca6722
---

Repo: `C:\Users\ohjos\repos\Yearly_and_monthly_spend_per_CC` (private GitHub JoshuaZayne/…, default branch **master**, runs on **Python 3.13** only — the Windows Store install; conda base 3.14/3.9 lack pyarrow / are too old).

## Adding new documents — the intake dropbox
Drop ANY statement/CSV/PDF into `source_documents/_inbox/`, then:
```
py -3.13 -m spend_report.data_io.intake            # route it (add --dry-run to preview)
py -3.13 -m spend_report.orchestration.report_builder
```
`spend_report/data_io/intake.py` identifies each file by its **content** (not filename), renames it to the standard convention, and moves it to the right per-account folder. Parsers all glob their folders, so the next build automatically incorporates it — no config/accounts.json edits needed. Unrecognized files are left in the inbox and listed. The inbox is gitignored except README.txt.

## Parsed accounts & their folders (each has its own parser + a sheet)
- **Schwab brokerage** (`accounts/Charles Schwab Brokerage - <name> (<suf>)/Brokerage Statements/<YYYY-MM-DD>.pdf`): Pure Gains (620), Insurance (604), Options (765), Vehicles (060). Parser `schwab_brokerage_pdf`.
- **Schwab futures & forex** (same account folders, `Futures & Forex/` subfolder): futures accts TDAGZ578(→765)/SCHAE608(→060), forex FX495194011(→765)/FX61464060(→060). Parsers `schwab_futures_pdf`, `schwab_forex_pdf`, `schwab_futures_1099b_pdf`. 1099-B Section-1256 gains are folded into the tax projection.
- **Schwab bank** (`schwab_bank_pdf`, wired into the ledger): Main-Vehicles checking …086 (in `Charles Schwab (5086)/csv/`), Pure Gains checking …565, Savings …630. Deposits into 565/630 are OWN-account transfers (parking for interest), NOT income.
- **Monetary Metals** (`documents/Monetary Metals/<YYYY-MM>.pdf`, `monetary_metals_pdf`): gold+silver held under **Dimaskus LLC**.
- **TSP** (`documents/TSP/`): the InvestmentActivityDetail CSVs are contributions (`tsp_csv`); the participant-statement PDFs carry the BALANCE (`tsp_statement_pdf`) — Uniformed Services (military) + Civilian plans.

## Net Worth sheet (the rollup that ties balances together)
`analyze.net_worth_summary()` shows every account's LATEST balance — from the PARSED statement where we have one (`Source = statement`), else the accounts.json Dec-2025 snapshot (`Source = accounts.json`). accounts.json is grouped by category (`checking/savings/investment/business/kids/retirement_tsp_hsa`, no flat `accounts` key). To make a snapshot account live: add its statement + parse its balance (like TSP/086 were) and add its number to `parsed_numbers`. See [[project_spend_analysis_cc]].
