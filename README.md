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

## Scheduled sync

To avoid running `sync_memory.py --sync` by hand, set it up as a recurring
background job.

**Important:** run the installer from a **permanent** clone location (e.g.
`C:\Users\<user>\ohjoshrules` or `~/ohjoshrules`) — not from a USB drive
that gets unplugged, or the scheduled task will fail when the drive is
missing.

### Windows (Task Scheduler)

```cmd
cd C:\Users\<user>\ohjoshrules
install_schedule.bat               :: hourly (default, no admin needed)
install_schedule.bat /daily 09:00  :: daily at 09:00
install_schedule.bat /hourly       :: explicit hourly
```

Notes:
- `/sc onlogon` requires admin rights on Windows, so it isn't the default.
  If you want a logon trigger, either run `install_schedule.bat` from an
  elevated prompt and pass `/sc onlogon` to `schtasks` directly, or drop a
  shortcut to `scheduled_sync.bat` into `shell:startup`.
- Output is logged to `sync_memory.log` next to the script. The log is
  auto-trimmed when it exceeds ~1 MB and is gitignored.
- Inspect / run the task manually:
  ```cmd
  schtasks /query /tn "ClaudeMemorySync" /fo LIST /v
  schtasks /run   /tn "ClaudeMemorySync"
  ```
- Remove the task: `uninstall_schedule.bat`

### Linux / Raspberry Pi (cron)

```bash
cd ~/ohjoshrules
./install_schedule.sh                 # every hour at :05 (default)
./install_schedule.sh "*/15 * * * *"  # every 15 minutes
```

Notes:
- The script appends a cron entry tagged with the marker `# ClaudeMemorySync`
  so it can be cleanly removed later.
- Output is logged to `sync_memory.log` next to the script.
- Inspect the entry: `crontab -l`
- Remove the entry: `./uninstall_schedule.sh`
