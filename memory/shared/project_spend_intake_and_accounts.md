---
name: project_spend_intake_and_accounts
description: Document intake dropbox + the parsed-account/statement structure in the Yearly_and_monthly_spend_per_CC repo (how to add new statements and have the report build off them)
metadata: 
  node_type: memory
  type: project
  originSessionId: a9e289a4-d2cb-453d-8b06-5e7ae5ca6722
  modified: 2026-08-03T07:01:11.421Z
---

Repo: `C:\Users\ohjos\repos\Yearly_and_monthly_spend_per_CC` (private GitHub JoshuaZayne/…, default branch **master**, runs on **Python 3.13** only — the Windows Store install; conda base 3.14/3.9 lack pyarrow / are too old).

## Adding new documents — the intake dropbox
Drop ANY statement/CSV/PDF into `source_documents/_inbox/`, then:
```
py -3.13 -m spend_report.data_io.intake            # route it (add --dry-run to preview)
py -3.13 -m spend_report.orchestration.report_builder
```
`spend_report/data_io/intake.py` identifies each file by its **content** (not filename), renames it to the standard convention, and moves it to the right per-account folder. Parsers all glob their folders, so the next build automatically incorporates it — no config/accounts.json edits needed. Unrecognized files are left in the inbox and listed. The inbox is gitignored except README.txt.

**Fidelity downloads need their own router** (intake does NOT handle them):
```
py -3.13 -m spend_report.data_io.fidelity_statement_organizer          # dry run
py -3.13 -m spend_report.data_io.fidelity_statement_organizer --move   # sweeps ~/Downloads
```
Fidelity names every statement `Statement<MMDDYYYY>.pdf`, so downloads collide as `Statement12312025 (3).pdf` — the **`(n)` suffix means a DIFFERENT ACCOUNT or granularity, never a copy**. Never dedupe these by filename or byte hash: a re-downloaded statement has different PDF metadata but identical text, so the organizer compares **extracted text**. It also skips quarterly/year-end reports at load time because they restate the same activity as the monthlies (only monthly statements feed the ledger).

## Parsed accounts & their folders (each has its own parser + a sheet)
- **Schwab brokerage** (`accounts/Charles Schwab Brokerage - <name> (<suf>)/Brokerage Statements/<YYYY-MM-DD>.pdf`): Pure Gains (620), Insurance (604), Options (765), Vehicles (060). Parser `schwab_brokerage_pdf`.
- **Schwab futures & forex** (same account folders, `Futures & Forex/` subfolder): futures accts TDAGZ578(→765)/SCHAE608(→060), forex FX495194011(→765)/FX61464060(→060). Parsers `schwab_futures_pdf`, `schwab_forex_pdf`, `schwab_futures_1099b_pdf`. 1099-B Section-1256 gains are folded into the tax projection.
- **Schwab bank** (`schwab_bank_pdf`, wired into the ledger): Main-Vehicles checking …086 (in `Charles Schwab (5086)/csv/`), Pure Gains checking …565, Savings …630. Deposits into 565/630 are OWN-account transfers (parking for interest), NOT income.
- **Monetary Metals** (`documents/Monetary Metals/<YYYY-MM>.pdf`, `monetary_metals_pdf`): gold+silver held under **Dimaskus LLC**.
- **TSP** (`documents/TSP/`): the InvestmentActivityDetail CSVs are contributions (`tsp_csv`); the participant-statement PDFs carry the BALANCE (`tsp_statement_pdf`) — Uniformed Services (military) + Civilian plans.
- **Fidelity brokerage** (`fidelity_investment_pdf`, added 2026-08-02): ONE "INVESTMENT REPORT" PDF covers MANY accounts — Z28-754409, Z32-368439 (cash mgmt), Z35-177267, Z40-457979 in `accounts/Fidelity Investments (Joshua portfolio)/`, plus the joint Z31-887703 in its own folder. Dormant/no-activity: IRAs 244-968051, 244-968071, 249-671391, HSA 259-199580, UTMA Z29-743185 (Alaira), Z29-743190 (Agreius), Z34-206237 (Zavier).
- **Fidelity Crypto** (`fidelity_crypto_pdf`): accounts 8291498726 (Joshua) and 8065197254 (Olivia) — both **$0.00 in every statement**, dormant.
- **NavyFed ANNUAL SUMMARY** (`navyfed_annual_pdf`, added 2026-08-03): NFCU mails a yearly summary under the SAME `*_VISASTMT.pdf` / `*_MCSTMT.pdf` name as the monthlies, but with a "Transaction Detail" layout instead of a monthly activity block. `navyfed_cc_pdf` found no anchor and returned **0 rows**, silently losing whole years. Cards seen only here: **9538** (2023-2024), **5893** (Mastercard, 2022), plus 7084 (2022) and 7531 (2025). Parsing them added **1,584 rows / +$155K card spend** and filled the 2022-2024 hole. Gotchas: a negative category total prints as `-$673.01` (sign BEFORE the `$`), and rows end in `CR` (credit) or `PY` (payment).

## Net Worth sheet (the rollup that ties balances together)
`analyze.net_worth_summary()` shows every account's LATEST balance — from the PARSED statement where we have one (`Source = statement`), else the accounts.json Dec-2025 snapshot (`Source = accounts.json`). accounts.json is grouped by category (`checking/savings/investment/business/kids/retirement_tsp_hsa`, no flat `accounts` key). To make a snapshot account live: add its statement + parse its balance (like TSP/086 were) and add its number to `parsed_numbers`. See [[project_spend_analysis_cc]].
