---
name: reference-run-log
description: Pipeline run history and per-script ask/output is captured in data/run_log.json and rendered into content/memory/run_observations.md and content/scripts/<name>.md
metadata: 
  node_type: memory
  type: reference
  originSessionId: e2ef58d5-9b19-4f19-aef7-7007c021715a
---

The CodeMapping_Brain pipeline (`run_all.py`) writes every phase invocation to `~/repos/CodeMapping_Brain/data/run_log.json` (via `scripts/run_logger.py`) with: `phase`, `cmd`, `rc`, `duration_s`, `ts_start`, `ts_end`, `stdout_tail`, `stderr_tail` (last 40 lines).

`scripts/memory_from_runs.py` consumes that log and produces:

- `content/memory/run_observations.md` :: per-phase last-success / last-failure tail, plus a repo activity table
- `content/scripts/<name>.md` :: one node per pipeline script: docstring ("ask"), best-effort reads/writes, last invocation tail ("output")
- `content/scripts/index.md` :: discoverable index of every script

Per-repo git post-commit hooks (installed by `scripts/install_repo_hooks.py`) append to `data/repo_activity.json`, which the same renderer surfaces in `run_observations.md`. Hooks are opt-in: run the installer once per machine. Sentinel `# codemap-managed-hook v1` prevents clobbering user hooks.

Look here when:
- Debugging which phase last failed.
- Auditing what a specific script does and what it reads/writes.
- Tracking which repos have committed recently (cross-machine visibility lives here too once hooks are installed).
