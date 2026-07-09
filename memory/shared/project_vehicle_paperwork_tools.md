---
name: project_vehicle_paperwork_tools
description: VehiclePaperworkTools repo — extract VIN from dealer PDFs and generate Dimaskus vehicle POA .docx via Word COM
metadata: 
  node_type: memory
  type: project
  originSessionId: c9766650-d6ea-4c17-b7de-c39c31c450bb
---

Repo `C:\Users\ohjos\repos\VehiclePaperworkTools` (git, local-only as of 2026-07-09) holds Windows/PowerShell tools for Dimaskus Capital Management vehicle-registration paperwork:

- `scripts\Extract-VehicleVin.ps1` — opens a dealer PDF via Word COM, regex-finds the 17-char VIN (`[A-HJ-NPR-Z0-9]{17}`, no I/O/Q).
- `scripts\New-VehiclePoa.ps1` — fills `templates\PowerOfAttorney.Vehicle.template.docx` (`{{MAKE}} {{MODEL}} {{VIN}} {{YEAR}} {{STATE}} {{SIGN_DATE}}`) via Word COM Find/Replace.
- `scripts\Get-DocxText.ps1` — reads .docx text without Word (for verifying output).

**Why Word COM, not raw XML edit:** Word splits some field values (model, dates) across multiple `<w:r>` runs, so a raw string-replace in `word/document.xml` misses them; Word's Find works on the flattened text layer. When building templates, replace longer strings before their substrings (e.g. `25 SEP 2025` before `2025`).

Standing parties on the POA form: Principal = Joshua Zayne / Dimaskus Capital Management; Agent = Kim Johnson (Helena, MT). Source POA forms live in `F:\iCloudDrive\Dimaskus Capital Management\Power of Attorney Forms\`.

First run: 2019 Ford Transit Connect Van, **VIN NM0LS7E28K1399891** (Ken Garff American Fork Ford, deal 191098). Governing-law state defaulted to UTAH — confirm per registration state. See [[project_icloud_reorg]] for the F:\ iCloud layout.
