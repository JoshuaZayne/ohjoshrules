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

7. **THE BACKUP STEPS ARE CHAINED, AND ONE STRAY FILE KILLS THE REST (found 2026-11-22 16:05 MST).**
   `rusttos-backup` runs three steps in order in `main`: the dated backup, then `run_tick_backup`, then
   `run_ibkr_backup`. Each is guarded by `if ... && !step(...) { return ExitCode::from(1); }`, and
   `run_tick_backup` ends with `let mut all_good = report.problems.is_empty();`. So ANY file under
   `data/ticks` that is not a `.csv` tick file makes the tick step return false and the program exits
   before the IBKR step ever runs. It prints no error: the line `IBKR days packed into ...: N` is
   simply ABSENT. Check for that line, never for an error.
   What it cost: two files of 96 and 394 bytes, `MYM.csv.at_35684225.bin` and `.txt`, left by the torn
   line set aside of 2026-11-15 under `data/ticks/set_aside/`, blocked EVERY IBKR day backup from
   2026-11-15 to 2026-11-22. Six days of this desktop's own trade tapes, top of book and depth sat
   unbacked while every run still reported the parts it did upload. Fixed with no code change by
   MOVING both files (never delete) to `data/ledgers/torn_line_set_aside_2026-11-15_231059_utc/`,
   which takes them out of the tick scan and into `set_aside_and_ledgers.zip`, so they are packed
   instead of skipped. The re-run then packed 8 days, 7,695,496 rows, and uploaded 5 IBKR tick days
   and 7 depth days.
8. **What the data repo does and does not hold.** Dated release (`data-<stamp>`): `store`, `curve`,
   `joined`, `ledgers`, `margins`, `orders`, `reports`, `schwab_accounts`, `stock_history`,
   `forex_rates`, `ibkr_backfill`, `ibkr_ticks`. Monthly rolling releases: `lake-YYYY-MM` (hourly),
   `ticks-YYYY-MM`, `ibkr-ticks-YYYY-MM`, `ibkr-trades-YYYY-MM`, `depth-YYYY-MM`, `bars5s-YYYY-MM`.
   NEVER packed, per the manifest's own line 3: logins and tokens, `.env`, logs, chart settings,
   `drawings`, `studies`, screenshots, `curve/backup`. In NO release at all: `accounts`, `alerts`,
   `paper`, `backfill_worklist`, `spot_proxy`, `reference`, `status_page`, `settings`, `test_logs`.
   So `settings`, `drawings` and `studies` are hand made work living only on F: and the C: mirror.
   The current day is never packed by any path.
