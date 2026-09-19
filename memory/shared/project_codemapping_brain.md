---
name: project_codemapping_brain
description: "CodeMapping_Brain = the user's 'code base map': the code brain (codemap.py) that indexes every function/folder on a machine, finds duplicates, and powers the reuse-before-writing hook"
metadata: 
  node_type: memory
  type: project
  originSessionId: 34178c54-c10f-43c6-b548-81ced589d7ee
  modified: 2026-09-19T21:32:23.945Z
---

When the user says **"run code base map"**, "code base", "codemap", "code map", "brain map" or similar, they mean the repo **JoshuaZayne/CodeMapping_Brain** (desktop clone: `F:\GitHub Repos\CodeMapping_Brain`, cloned 2026-09-19). Run it with `python codemap.py run` (scan + similar + fix dry run); `python run_all.py --continue-on-error` runs that plus the older Obsidian/Quartz vault pipeline (22 phases).

**The code brain (added 2026-09-19, stdlib only, Python 3.7+; tested on 3.7 32-bit / 3.9 / 3.14 Windows and 3.12 Linux via WSL):**
- `brain/` package + `codemap.py` CLI: `scan`, `similar`, `fix [--apply]`, `find WORDS`, `check FILE|-`, `stats`, `install-hooks`, `hook-precheck`.
- Auto-discovers roots per machine: home + every data drive (Windows fixed/removable except C:, `/media` `/mnt` `/Volumes` on Linux/Pi/Mac) + `extra_roots` in `codemap.config.json`. Env overrides: `CODEMAP_ONLY_ROOTS`, `CODEMAP_SCAN_DRIVES=0`, `CODEMAP_HOME`, `CODEMAP_REPORT_DIR`.
- Index: `~/.codemap/brain.sqlite` (per machine, not in git). Desktop: ~54k defs from ~5.5k files, ~230 projects. Full scan ~2 min, incremental ~20 s.
- Reports: `data/brain/REPORT.md` (duplicate code clusters + similar folders + snapshot series), `data/brain/FIXES.md` + `fixes/*.diff`; also copied to `content/brain/` for Obsidian.
- Self-test: `python tests/test_brain.py` (temp fixture, never touches the real index).

**Gotchas learned building it:**
- Installed software (Miniconda, PyCharm, VS Code, Git, JDK, STATA on F:) is skipped by marker files (conda-meta, product-info.json, Code.exe, python.exe, unins000.exe ...), not by path.
- `F:\iCloudDrive` has thousands of cloud-only placeholder files; opening one triggers a download. The brain checks Windows file attributes and never opens them.
- A file literally named `nul` exists on F: (reserved name) and breaks `os.path.relpath`.

**Fix policy:** auto-fix only identical-logic top-level Python functions in the same project with a safe import path, safe-to-import canonical module, same outside-name bindings, clean git file; never commits; never edits versioned/backup snapshot files (`_v5`, `(1)`, `old/`, `OldIterations/` ...). As of 2026-09-19: 52 safe fixes ready (42 in Alphainsider strategies), **none applied yet** pending the user's go-ahead.

See [[feedback_reuse_existing_code]], [[feedback_cross_device_paths]], [[user_github_and_devices]].
