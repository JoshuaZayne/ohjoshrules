---
name: Shared memory sync via ohjoshrules repo
description: Where shared cross-device memories live and how to pull/push them
type: reference
---

The source of truth for memories that need to follow the user across **desktop / laptop / Raspberry Pi** lives in the GitHub repo **`JoshuaZayne/ohjoshrules`**, under `memory/`:

- `memory/shared/` — applies to every device
- `memory/desktop/`, `memory/laptop/`, `memory/raspie/` — only loaded on that device

Sync script: `sync_memory.py` at the repo root (plus `sync_memory.bat` / `sync_memory.sh` wrappers).

Commands:
- `python sync_memory.py` — git pull, then copy repo -> local Claude memory dir (rebuilds `MEMORY.md` index)
- `python sync_memory.py --push` — copy local Claude memory -> repo (no git)
- `python sync_memory.py --sync` — pull, push local up, commit + push to GitHub
- `python sync_memory.py --status` — show detected hostname + device + paths

Device detection is **hostname-first** via `device_registry.json` (e.g. `DimaskusPC` -> `desktop`), with a filesystem fallback for unregistered machines. When adding a new device, run `--status` to see its hostname, then add it to the registry.

When saving a memory that should only apply on one device, either drop the file directly into `memory/<device>/` in the repo, or add a line `<!-- device: laptop -->` inside the file and let `--push` route it automatically.

Clone location on each device is anywhere convenient (current laptop copy is at `F:\ohjoshrules`).
