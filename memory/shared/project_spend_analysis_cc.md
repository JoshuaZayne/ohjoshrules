---
name: project_spend_analysis_cc
description: "Running the Yearly_and_monthly_spend_per_CC repo — Python version gotcha, iCloud sync, and the two bank income accounts"
metadata: 
  node_type: memory
  type: project
  originSessionId: 6a2630be-b2cc-47a1-892a-0fa2a7eeee2c
---

Repo `Yearly_and_monthly_spend_per_CC` (cloned at `C:\Users\ohjos\repos\Yearly_and_monthly_spend_per_CC`) parses AMEX + Fidelity + Schwab statements into an Excel spend/income workbook.

**Python gotcha:** the code uses 3.10+ syntax (`str | None`), but this machine's default `python` is 3.9. Run everything with **`py -3.13`** — pandas/openpyxl/pdfplumber are installed there. `build_report.py` builds the workbook + trends md; `validate.py` runs the reconciliation suite (should be all-pass).

**iCloud source docs** live at **`F:\iCloudDrive\Documents`** on the desktop (drive-letter mount). Note a stale, empty `C:\Users\ohjos\iCloudDrive\Documents` mount also exists — `sync_check_icloud.py` scores candidate mounts by folder content so it picks F: automatically. Relevant folders: `Credit Card Annual`, `Bank Statements` (Amex/Charles Schwab/Fidelity), `Mortgage Statement` (Freedom Mortgage, ~$2,079.94/mo P&I), `VA LES Statements` (VA GS-civilian pay stubs), `VA W2s`. Run `python sync_check_icloud.py [--copy]` to mirror new iCloud docs into `source_documents/` so the repo isn't iCloud-dependent.

**Income model:** two Bank accounts feed money-in analysis — Fidelity Cash/Bank (VA disability/education benefits, VACP/VAED TREAS) and Charles Schwab Checking …086 (VA civilian DFAS salary + allotments). `classify_inflow` splits deposits into true income vs transfers between the user's own accounts. See [[project_thinkscript_version_tracking]] for the commit-each-change habit — same applies here (private repo tracks source_documents + generated output).

**iCloud moved → local-mirror fallback (2026-07-04):** the live `F:\iCloudDrive\Documents` is now EMPTY (the [[project_icloud_reorg]] moved most of it to `.Trash`). `config.find_icloud_documents` was hardened with a try-block + fallback to the local reorg mirrors `~/iCloudReorg/stage_raw_mirror_*/Documents`, newest full mirror first (**v2** over v1; live-only v3 scores 0 subfolders and is skipped). So the pipeline runs entirely from local copies now — no iCloud needed. `sync_check_icloud.py --copy` pulls from whichever mirror the resolver picks.

**Coverage guard (2026-07-04):** `analyze.housing_gap_months(df)` = single source of truth for interior months missing the mortgage (~$2k/mo anchor fixed cost) → Fixed/Expenses understated = data gap, not low spend. Shaded red in notebook sections 018/050/080 and the Excel Income-vs-Expenses chart. Known unfilled gap: **Fidelity 7832 checking Dec 2023–Jun 2024** (statements not local; `transactions.CSV` starts 2024-07 — needs a fresh Fidelity export). One-command refresh: `launch_notebooks_fresh.cmd`.

**OPEN (2026-07-04):** imported 142 local files via `--copy`; full rebuild pipeline COMPLETED (outputs fresh) but `validate.py` FAILS on "exact-duplicate rows (is 101)" — overlapping statements double some txns; must dedupe before committing. All changes still UNCOMMITTED. Full state + next steps in `HANDOFF.md` at the repo root.
