# ohjoshrules

Cross-project rules, permissions, and **shared Claude Code memory** that
follow the user across devices (desktop, laptop, Raspberry Pi).

## Contents

- **`PERMISSIONS.md`** — baseline permissions / approval rules for assistants
  working in any of the user's repos.
- **`memory/`** — source of truth for Claude Code memories that should be
  available on every device. See [`memory/README.md`](memory/README.md).
- **`sync_memory.py`** — device-aware sync script. Run it to pull the latest
  memories into the local Claude Code memory directory, or push new local
  memories back up to GitHub.

## Quick start on a new device

```bash
# 1. Clone somewhere that persists (any device)
git clone https://github.com/JoshuaZayne/ohjoshrules.git

# 2. Pull memories into this device's Claude Code memory dir
cd ohjoshrules
python sync_memory.py            # Windows
./sync_memory.sh                 # Linux / Raspberry Pi
```

After that, every future Claude Code session on this device starts with the
shared memory already loaded. When Claude saves new memories locally, run
`python sync_memory.py --sync` to push them up so the other devices pick
them up on their next pull.
