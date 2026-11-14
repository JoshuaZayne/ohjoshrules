---
name: reference-rusttos-backups-and-data-jobs
description: "RustTOS data safety on the desktop: hourly backup task, C: mirror, daily full backup, low disk guard, and the scripts and logs that run them"
metadata:
  type: reference
---

Set up 2026-11-13 on the user's instruction ("could we make the hook happen on an hourly basis so we never lose any data"); the user approved the installs.

1. **Hourly backup:** Windows scheduled task "RustTOS hourly backup" at minute 20 runs `C:\RustTOS_backup_mirror\hourly_backup.cmd`: (a) robocopy, add and update only, of the files still being written and everything requested from IBKR (recorder staging, ticks, trade pages `ibkr_ticks`, history downloads, the history store, option files, orders, ledgers, settings, alerts, drawings, studies, reports) from `F:\GitHub Repos\RustTOS\data` to `C:\RustTOS_backup_mirror\open_files`; (b) `rusttos-data refresh --run` (seals closed days into `data\lake`); (c) `rusttos-backup incremental --run` to the private repo `JoshuaZayne/RustTOS-data-backup` and the mirror. Log: `C:\RustTOS_backup_mirror\hourly_backup_log.txt`.
2. **Daily full backup:** task "RustTOS data backup" at 15:10 (`rusttos-backup --publish --with-ticks`), unchanged.
3. **Mirror folder** `C:\RustTOS_backup_mirror` was chosen by the assistant (the user named none; the program refuses a mirror on the data drive). The user has not objected.
4. **Low disk:** drive F filled on 2026-11-12 about 17:42 to 17:47 MST from parallel builds and the IBKR recorder lost 8,670 rows. Since 2026-11-13 21:28 MST the installed recorders have a low disk guard and the feed watchdog reports `disk_space` and `memory` (Telegram once per level: disk under 20 GB, memory under 12 GB).
5. **Real trade history fetch:** `F:\GitHub Repos\RustTOS_agents\weekend_ticks.sh` (uses `rusttos_ibkr_ticks`; pages in `data\ibkr_ticks\<contract>\pages`, never rewritten, resumable). It is not a scheduled job yet; it must be started by hand after a restart (command in the handoff file, [[project-rusttos-handoff-2026-11-13]]).
6. Verified 2026-11-13: for 6EZ26, 35,195 of 35,216 minutes have exactly the same trade count and volume in the real trade pages and in the stored IBKR one minute bars (the tick charts' source).
