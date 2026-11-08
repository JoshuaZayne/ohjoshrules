---
name: project_ssdi_guide
description: "SSDI repo (F:\\GitHub Repos\\SSDI, private JoshuaZayne/SSDI): disabled-veteran SSDI guide, 54-row state DDS CSV, state lookup script; created 2026-11-07"
metadata:
  node_type: memory
  type: project
  originSessionId: 5e772145-f916-4997-8413-2c7846c92379
  modified: 2026-11-08T02:49:02.378Z
---

The user (a disabled veteran) asked on 2026-11-07 for a repo on applying for SSDI. Built at `F:\GitHub Repos\SSDI`, pushed as private `JoshuaZayne/SSDI` (first commit 79c02f6).

Contents: README, docs/01 to 08 (eligibility, steps, checklist, by-state, lawyer, appeals, after approval, sources), `data/state_dds_directory.csv` (54 rows, blank website = not confirmed), `scripts/ssdi_state_lookup.py <STATE> [--write-checklist]`, and `reference/` holding two SSA PDFs the user downloaded to `C:\Users\ohjos\Documents` (SSDI.pdf = pub 05-10519, EN-05-10075.pdf).

**Why:** Dollar figures change every January (SGA, credit amount, TWP, COLA). The figures in the repo are 2026 and 2027, and the fee cap is $9,200.

**How to apply:** When updating, refresh the README key-numbers table and docs/08_sources.md together. SSA blocks curl (403), so verify SSA pages through search results or Internet Archive snapshots. The user lives in CO or TX (see [[project_thicket_hill_texas_home]]), so the docs carry notes for those two states.
