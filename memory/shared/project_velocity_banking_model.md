---
name: project_velocity_banking_model
description: Velocity Banking mortgage model in Excel for two homes; verdict at 25% LOC velocity loses to direct prepay
metadata: 
  node_type: memory
  type: project
  originSessionId: 9a715d4b-cc1c-4110-875a-d8e8fe9b13c2
---

User asked to model "Velocity Banking" (YouTube AqOplfWlYY8, VANNtastic!) for two home
scenarios. Built into `C:\Users\ohjos\Downloads\Mortgage_Amortization_VelocityBanking_2026-06-11_025316.xlsx`
(separate from the base amort file `Mortgage_Amortization_2026-06-11_014636.xlsx` because that
one was open/locked in Excel at save time).

Inputs: monthly income $14k, total monthly outflow $10k (incl. mortgage) => free cash flow
$4,000/mo. Personal LOC rate = **25%** (user corrected up from an initial ~13%).
Homes: A = $310k @ 6.5%/30yr; B = $550k @ 2.5%/30yr.

KEY VERDICT (recompute if any input changes): at a 25% LOC, velocity banking is strictly
worse than just paying the $4k/mo straight onto principal. Home A: direct = 5.2yr / $55,112
interest vs velocity (best $15k chunk) $68,298 (~$13k worse). Home B: direct = 8.2yr / $59,029
vs velocity $80,641 (~$22k worse). Optimal velocity chunk ~$15k. On the 2.5% loan, aggressive
prepay is itself debatable vs investing the cash flow. The video misleads by comparing velocity
only against doing nothing, and falsely claims the nominal rate is really ~150%.

CONSOLIDATED into git repo ~/repos/Mortgage_Vol_Calculator (commit d52a71c, 13 files): 36-sheet live
workbook (excel/Mortgage_MASTER_Analysis.xlsx); src/mortgage_core.py is the single source of truth;
src/verify_methods.py runs 4 numerical methods + Decimal + C++ cross-check (src/verify.cpp), all agree
<=1e-7 and Excel reconciles to 0.0000; src/optimize_allocation.py is a Lagrangian/KKT optimizer (scipy
LP + dual shadow price) proving velocity is dominated when LOC rate > mortgage rate; docs/ has
METHODOLOGY/FINDINGS/OPTIMIZATION. Cadence extended to 4-9 months; least-bad = 4mo (still loses to direct).
C++ compiler = g++ 14.2 at ~/AppData/Local/Microsoft/WinGet/Packages/BrechtSanders.WinLibs.*/mingw64/bin/g++.exe
(choco needs admin; winget user-scope works). No LibreOffice/pycel/formulas on Python 3.14.

Excel sheets are LIVE/recalculating month-by-month (yellow cells editable). Roadmap:
[[feedback_roadmap_default]] -> CodeMapping_Brain/content/roadmaps/2026-06-11_025316_velocity-banking-mortgage-model.md
Builder scripts in ~/Downloads: build_amortization_*.py, build_velocity_*.py.
