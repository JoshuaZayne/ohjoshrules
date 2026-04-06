# Shared Claude Code memory

This folder is the source of truth for memories that should follow the user
across all their devices (desktop, laptop, Raspberry Pi).

## Layout

```
memory/
  shared/      memories that apply everywhere (default location)
  desktop/    only merged when running on the Windows desktop
  laptop/     only merged when running on the Windows laptop / F: drive setup
  raspie/     only merged when running on the Raspberry Pi
```

## Lifecycle

1. **Pull** — on any device, run `python sync_memory.py` (or `sync_memory.bat` /
   `sync_memory.sh`). That does `git pull`, then copies `shared/` and this
   device's folder into the local Claude Code memory directory and rebuilds
   `MEMORY.md` from every file's frontmatter.
2. **Learn** — during a normal Claude Code session, Claude saves new memories
   into the local Claude memory directory as usual.
3. **Push** — when you want those new memories to follow you, run
   `python sync_memory.py --sync`. That does `git pull`, copies local memories
   back into this repo (shared by default, or into a device folder if the file
   contains a `<!-- device: desktop -->` style marker), then `git commit` and
   `git push` so the other machines can pick them up.

## Device detection

`sync_memory.py` uses the same loop-based resolver pattern as `device_paths.py`
in the other repos. It checks for:

- `C:\Users\ohjos` (desktop)
- `F:\iCloudDrive` (laptop)
- `/etc/rpi-issue` or `/home/pi` (Raspberry Pi)

You can override detection with the `CLAUDE_MEMORY_DIR` environment variable
if a new machine doesn't match any candidate.

## Making a memory device-specific

Two ways:

1. Put the `.md` file directly in `memory/desktop/`, `memory/laptop/`, or
   `memory/raspie/` here in the repo.
2. Inside the memory file, add a marker comment on its own line near the top:

   ```html
   <!-- device: laptop -->
   ```

   When `sync_memory.py --push` runs, it will file the memory into that
   device's folder instead of `shared/`.

## Quick reference

| Command | What it does |
|---|---|
| `python sync_memory.py` | git pull, then repo -> local Claude memory |
| `python sync_memory.py --push` | local Claude memory -> repo (no git) |
| `python sync_memory.py --sync` | pull, push local up, then commit+push |
| `python sync_memory.py --status` | show detected device + paths |
| `python sync_memory.py --dry-run` | print actions without writing |
