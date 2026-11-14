---
name: project-home-folder-reorg-2026-11-14
description: "Desktop home folder reorganized 2026-11-14: 11 home repos now in F:\\GitHub Repos, loose files in Records/School/Machine/Notes/Archive; move log and what old paths map to"
metadata:
  node_type: memory
  type: project
  originSessionId: ba63db71-b54f-4229-93b0-785382017f76
  modified: 2026-11-14T18:47:53.807Z
---

On 2026-11-14 the user asked for `C:\Users\ohjos` on the desktop to be organized ("plan it out and then do it"). Older memories that name the paths below are stale: use the new locations.

**Repos moved from the home folder to `F:\GitHub Repos\<name>`** (copied, verified by file count, bytes, HEAD and git status, then the old copy removed): Cali_Mutual_Divorce_process, DumpTruckBusinessBuildout, iCloudReorg, PhonePhotoImport, ThinkScript_Studies, ThicketHillProperty, signature_analysis (was `projects\`), and from `repos\`: EmailSearchandCleanup, MercSprinter15PassVanDataScrapper, VehiclePaperworkTools, Yearly_and_monthly_spend_per_CC. `C:\Users\ohjos\repos` and `projects` no longer exist.

**New home folders:**
1. `Records\`: Dimaskus_IBKR, HighlandHomeLoans_Docs, docs_reorg_2026_04_23 (holds DD214.pdf), iCloudReorg_RescuedV2Only.
2. `School\`: the three datascience course repos, Math, PycharmProjects, eclipse-workspace.
3. `Machine\`: installers, system, dxdiag.txt, test files, and `reorg_logs\`.
4. `Notes\`: broker repo review text files (2026-10), 6E_trade, other notes.
5. `scripts\password_generator\` and `scripts\vehicle_payment_calculator\`.
6. `Archive\home_reorg_2026-11-14\`: old program settings (PyCharm 2018 to 2019, Eclipse, Evernote), empty folders, leftovers, and `ssh_guide_loose_files\` (old home copies of SSH_Setup files plus `mobile_ssh_guide`).

**Undo list:** `C:\Users\ohjos\Machine\reorg_logs\home_reorg_move_log_2026-11-14_114250.csv` (every move, old path and new path). Roadmap: `F:\GitHub Repos\CodeMapping_Brain\content\roadmaps\2026-11-14_114250_home-folder-reorganization.md`.

**Left in the home root on purpose:** `watt_tracker.py` (the SSH guide tells the reader to run it from there), `PYTHON_CODE_MASTER.md` (linked from the ohjoshrules master files), `ohjoshrules`, `logs`, `scripts`, `localLLM`, `Code`, `DriverAudit`, `.schwab_token.json`, `.broker_fallback_counter.json`, the orphan `iCloudDrive`.

**Deleted with the user's approval the same day:** `rusttos_coverage_targets` (about 201 GB of build output, idle since 2026-11-11) and the iPhone backup under `Apple\MobileSync\Backup` (about 87 GB).

**Why:** the user wanted `ls` in the home folder to be readable, one folder per kind of thing. **How to apply:** put new repos in `F:\GitHub Repos`, not the home folder; keep the home root free of loose files; when an old note names `C:\Users\ohjos\<repo>` or `~/repos/<repo>`, look in `F:\GitHub Repos` first. See [[project_f_drive_github_repos_reorg]], [[feedback_windows_folder_collisions]].
