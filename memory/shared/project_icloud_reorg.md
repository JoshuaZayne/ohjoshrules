---
name: project_icloud_reorg
description: "Reorganizing F:\\iCloudDrive via a local, phased copy-clean-dedupe workflow (project scripts at C:\\Users\\ohjos\\iCloudReorg)"
metadata: 
  node_type: memory
  type: project
  originSessionId: e45c2b11-7288-4b60-b119-01000d1b779e
---

User is reorganizing **F:\iCloudDrive** (~90 GB, 55k files). Direct edits in iCloud break/undo things, so the approach is: work on a LOCAL copy, then (later) decide whether to push back to iCloud or migrate off. Started 2026-07-03.

**Why:** iCloud placeholder sync mangles bulk in-place changes; content reads on online-only files trigger mass downloads.
**How to apply:** All paths live in `C:\Users\ohjos\iCloudReorg\config.json` (configurable per machine, per [[feedback_cross_device_paths]]). Stage folders use distinctive `_v1` names to avoid Windows collisions, per [[feedback_windows_folder_collisions]].

Phased plan (gated — build+run one phase at a time):
- **Phase 0 DONE**: `1_scan.ps1` (metadata-only, no downloads) → `2_analyze.py`. Output in `inventory\` + `reports\`.
- **Phase 1 DONE (2026-07-03)**: `3_mirror.ps1` (has `-ReportOnly` pre-flight) mirrored 54,559 files / 88.59 GB → `stage_raw_mirror_v1`, robocopy exit 1, ZERO failures. `.Trash` excluded. Gotcha fixed: inside `$list.Add("..." -f a, b)` the method-call commas swallow the `-f` args — wrap the format expr in its own parens.
- **Phase 2 DONE (2026-07-03)**: `4_verify.py` (full SHA-256 both sides) = GATE PASS, 54,559/54,559 byte-identical, 0 missing/mismatch/error. Mirror is a proven bit-perfect backup; iCloud deletion now recoverable (still deferred). Produced `inventory\mirror_hashes_*.csv` for Phase 3 reuse. GOTCHA: the tree contains 2 files literally named `nul` (Windows reserved device name, from `> nul` redirects, under IL_work\...\ProjectTwo_LocalLLM and \Personal\Resume). Python `os.path.abspath`/`relpath`/`normpath` resolve `nul` to the `\\.\nul` device and crash. Fix: use the `\\?\` extended prefix WITHOUT normalizing, and build relative paths by string-slicing the root, never relpath. Phase 3 hashing must do the same.
- Phase 3: `5_dedupe_reorg.py` on `stage_working_v1`; exact-content-hash dupes → `quarantine_duplicates_v1` (move only, never auto-delete).
- Phase 4 (not yet written): delete iCloud + re-upload in batches — only after user reviews results.

Phase 0 findings: two populations — (1) a few huge media files = nearly all GB (GoPro DCIM 49.9 GB, one 23 GB Desktop .mov, video 72 GB/80 files); (2) dev-project internals (node_modules/.git/.lzma, ~28k .js/.ts files) = nearly all the file count but trivial size, and they inflate the "25k duplicates" number to a meaningless 839 MB reclaimable. Real dupes worth acting on = ~30-40 large book PDFs duplicated across BOOKS\ subfolders. C: has 785 GB free (no space constraint).
