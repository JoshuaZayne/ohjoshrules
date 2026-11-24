---
name: reference-desktop-shell-hang-icmp-wedge
description: "DimaskusPC 2026-11-23: every bash/sh call and git hook hung because the Windows ICMP and host name path was wedged; how it was diagnosed, what leaked, what NOT to do"
metadata:
  node_type: memory
  type: reference
  originSessionId: 1357db99-9ad1-48ec-8f53-a505f7663727
  modified: 2026-11-23T17:52:31.208Z
---

**Symptom on the desktop (DimaskusPC), 2026-11-23 from about 05:39 MST:** every Bash tool call returned nothing
and never finished, `git commit` in RustTOS hung forever inside `sh .githooks/commit-msg`, `git push` hung, and
hundreds of `bash.exe` piled up (246 by 09:06, 1,029 processes in all). Live recorders, TCP and DNS kept working.

**Cause, measured:** `ping -n 1 127.0.0.1` hangs, a .NET ICMP ping hangs, and Git's `usr\bin\hostname.exe` hangs,
while `true.exe`, `id.exe`, `ls /`, `cmd`, `git --version`, DNS lookups and a TCP connect all work. `bash` and `sh`
ask for the host name on startup, so every shell hangs there. A process stuck in that call accepts a kill but does
not finish going away (checked: test processes killed with `taskkill /F` were still listed minutes later).
Only a restart of Windows clears it; a clean shutdown may itself hang.

**What was NOT the cause (each was believed for a while and was wrong):** a git lock, a failing F: drive, too many
processes, process creation being broken.

**What leaked, in order of size:** two Python hook scripts that Claude Code runs through bash on every tool call
(about 90 each), `RustTOS_agents\status_page\refresh_page.sh` from the task "RustTOS status page refresh" (one
every 5 minutes), `sync_memory.py --sync` stuck in `git push` since 06:56, and 82 `PING.EXE` started in one second
at 05:39:05 by a python (PID 21044) that the Task Scheduler started in session 0 on 2026-11-22 12:25. That python's
command line cannot be read without administrator rights; `C:\Users\ohjos\Machine\who_started_the_pings.bat`
reports it. The owner ran it at 10:22: it is OUR OWN code, `F:\GitHub Repos\SSH_Setup\scripts\device_activity_monitor.py
--interval 30 --sweep-every 300`, started at boot as SYSTEM by the task "SSH_Watch_DeviceActivity" through
`run_ssh_watch.ps1` (installed 2026-11-22, one day before the fault). Every 5 minutes it pinged every address on
the home network, 96 at a time. Whether that sweep TRIGGERED the fault or was only its first victim is not known:
the hang began with that sweep's pings at 05:39:05, after about 200 sweeps that went fine. It froze because
`subprocess.run(..., timeout=30)` waits with NO limit for the stopped child to go away. Fixed the same day,
uncommitted in SSH_Setup: `scan_network.run` never waits forever and counts helpers that will not go away
(`stuck_helper_count`), and the sweep pings 16 at a time and stops pinging for good once one is stuck. The owner then said "I only care
about logs in over ssh", so `run_ssh_watch.ps1` now starts the monitor with `--ssh-only` by default (reads the
OpenSSH event log only: no pings, no connection or socket tracking, plus a `watch_heartbeat` value each pass);
`-FullNetworkWatch` brings the old behaviour back. Takes effect at the next boot. The owner then said "make each of those fixes", and all five were built the same
day in SSH_Setup (uncommitted: `scripts/ssh_login_alerts.py` new, `tests/test_ssh_login_alerts.py` new, 19 tests;
`device_activity_monitor.py`, `run_ssh_watch.ps1`, `scan_network.py` changed):
1. A Telegram message per accepted SSH login; logins missed while the watch was down come as one summary; a burst
   of failures from one address once an hour; at most 20 messages an hour.
2. `logs/ssh_known_keys.json` (fingerprint to name), filled once and never added to; a key not in it is flagged.
   On 2026-11-23 it held one unnamed key: 221 logins, user ohjos, from the Tailscale address 100.94.1.112.
3. Flags: not a key login, key not on the list, source outside home networks and Tailscale.
4. The launcher reads `logs/ssh_watch_heartbeat.json` once a minute and tells the owner once when the watch stops
   and once when it is back; it sends through `ssh_login_alerts.py --send-text` with its own 30 second limit.
5. The SSH log is read by record number (`-FilterXPath ... EventRecordID>N -Oldest`), new entries only.
The Telegram login is read from the path in `logs/ssh_watch_settings.json`, which on the desktop names RustTOS's
`.env`; SSH messages therefore arrive in the same chat as the RustTOS alerts. Not yet seen running for real: the
first boot after the restart is the first real pass (look for "mode : SSH logins only" in
`logs/ssh_watch/ssh_watch_runs.log`).

**How to apply:**
1. If Bash calls hang with empty output on the desktop, test with PowerShell `Start-Process ... -PassThru` and
   `WaitForExit(12000)`: `usr\bin\true.exe` versus `usr\bin\hostname.exe`. If only `hostname.exe` hangs, it is this.
2. Do NOT probe with ping or any ICMP call: each probe adds one more process that cannot finish dying, and
   `Remove-Job -Force` on a thread job stuck in ICMP hangs the whole script.
3. Never hide errors on a kill (`-ErrorAction SilentlyContinue`) and then conclude "it will not die". The session 0
   pings answered "Access is denied", which was a permission fact, not a kernel fact.
4. Use PowerShell, Read, Grep and Edit instead of Bash until the restart; cargo and git themselves work.
5. Pause "RustTOS status page refresh" until the restart (it was disabled 2026-11-23 about 09:00 MST and must be
   enabled again afterwards).

Fixed the same day: `C:\Users\ohjos\ohjoshrules\sync_memory.py` now runs git under a 120 second limit and stops
the whole process tree (proved with a stuck program that started its own stuck helper), and the task
ClaudeMemorySync is capped at 15 minutes instead of 72 hours.

Also changed the same day, at the owner's request that Python broker code run only when a bat is fired:
1. Tasks "BrokersPlatform-SchwabFuturesCapture" and "BrokersICloudSync" are DISABLED. Their bats, written and not
   yet run: `scripts\schwab\run_capture_futures.bat` and `scripts\run_icloud_sync.bat` in
   `F:\GitHub Repos\Brokers_merge`.
2. "BrokersPlatform-SchwabTokenRefresh" refused ("Access is denied", it was made with administrator rights);
   `C:\Users\ohjos\Machine\disable_schwab_token_refresh_task.bat` turns it off. Its bat:
   `scripts\schwab\run_token_refresh.bat`.
3. Found: there is no D drive on the desktop, so the token refresh and iCloud sync tasks, which pointed at
   `D:\code\brokers`, had been failing on every run (result 2147942667).
4. Backups of each task as it was: `C:\Users\ohjos\Machine\task_backup_*_2026-11-23_*.xml`.
5. A commit could not run its hook (a shell script) during the hang. The owner chose to WAIT for a restart rather
   than commit with the hook skipped ([[feedback-never-skip-commit-hook]]); one commit made with `--no-verify`
   before that was known was taken back. The waiting work is described in
   [[project-rusttos-complaints-recheck-pending-commit-2026-11-23]].
6. Running the repository rules test before committing a document caught a real rule: files in RustTOS may not name
   outside folders or projects ("GitHub Repos", "Brokers_merge", "Brokers repo" were all refused).
7. Do not use `git stash` to set staged files aside in a RustTOS worktree: stashes are shared by every worktree, and
   a `stash push --staged` followed by a failed `pop` left staged work out of the working folder until it was
   restored by hand.

The full record of that chat is in RustTOS at
`docs/worklog/2026-11-23_095202_chat_summary_grid_headers_data_alerts_shell_wedge.md`, and the coding rule that
came out of it is [[feedback-no-unbounded-waits-stoppable-code]].

Related: [[reference-desktop-hardware-inventory]], [[project_rusttos]], [[shared-memory-sync-via-ohjoshrules-repo]].
