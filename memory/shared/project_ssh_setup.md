---
name: project_ssh_setup
description: "SSH_Setup repo: workstation OpenSSH access, 7-point diagnostics, electrical power telemetry, and interactive guide (docs/index.html)"
metadata: 
  node_type: memory
  type: project
---

Repo: `F:\GitHub Repos\SSH_Setup` (GitHub: `JoshuaZayne/SSH_Setup`, branch `main`). A modular Python and PowerShell suite for establishing secure remote SSH access across computers, running host diagnostics, tracking real-time electrical power telemetry, and serving interactive reference documentation.

The master guide and documentation:
1. `README.md` (185 KB, over 3,200 lines): Comprehensive manual detailing 60 real-world production SSH use cases (remote system administration, secure file transfer with SCP/SFTP, port tunneling, GPU and machine learning compute automation, defensive cybersecurity threat hunting, and disaster recovery), asymmetric cryptographic key hardening (Ed25519 KDF), home router zero-trust ringfencing, and CMOS power models.
2. `docs/index.html` (876 KB, over 15,700 lines): Standalone interactive web guide titled "Remote SSH Access & Power Telemetry Suite (v3.0)". Features a multi-shell syntax comparison matrix (PowerShell, Bash, Sudo, CMD, .BAT), a live JavaScript electricity cost projection calculator, one-click copy command cells, and reverse SSH labs.

Serving the interactive HTML guide:
- Double click `docs/index.html` to open directly in any web browser.
- Run `scripts/start_guide_server_prompt.bat` or `scripts/start_guide_server_prompt.ps1` to launch a local HTTP server with automatic port detection.
- Or execute `python -m ssh_setup.serve_guide` from `src/` (listens on port 8080).

Automated host setup and diagnostics:
- Host setup: `scripts/setup_openssh.ps1` installs OpenSSH Server on Windows, starts `sshd`, configures automatic service startup, and opens TCP port 22 in Windows Advanced Firewall.
- 7-Point Diagnostic Audit: `scripts/verify_ssh_setup.ps1` audits OpenSSH service state, firewall rules, port 22 listener binding, AC sleep timeout prevention (so the host does not sleep during remote sessions), authorized_keys NTFS ACL permissions, network routing, and telemetry sensor health. Python OOP runner: `src/ssh_setup/diagnostics/runner.py`.

Electrical power telemetry:
- CLI tool: `watt_tracker.py` queries hardware sensors (LibreHardwareMonitor WMI, NVIDIA NVML, mobile battery fuel gauge, Linux RAPL microjoule counters, and CMOS gate-switching models) to report real-time wattage with terminal sparklines.
- Cost model: `src/ssh_setup/core/cost_model.py` projects electricity costs per minute, hour, day, and month based on configurable utility rates ($/kWh).

Remote control and mobile features:
- Reverse SSH practice labs: Connecting from PC to iPhone and mobile devices (Blink, Termius, iSH).
- Screen mirroring and remote app launching: Instructions and scripts for VNC/RDP over SSH tunnels and booting applications remotely (including thinkorswim).

Who is using SSH, added 2026-11-22 (all verified working on DimaskusPC):
- `scripts/ssh_sessions.py`: live "who is on my SSH right now" view. Joins the TCP table and process table (one PowerShell call) to the OpenSSH/Operational event log, so each row shows device, address, user, accepted key fingerprint, session age and the child processes that session is running, then accepted logins and refused attempts over a window. Flags: `--watch --interval`, `--hours`, `--refused-only`, `--export`, `--port`. Reuses `SSH_PATTERNS` and `LOGIN_RESULTS` from `device_activity_monitor.py`; friendly names come from `config/peers.json` plus `logs/device_names.json`. Launcher: `Who_Is_On_My_SSH.bat` at the repo root.
- `scripts/run_ssh_watch.ps1`: runs `device_activity_monitor.py` continuously, picks a machine wide interpreter (resolves to `C:\Python314\python.exe`, which is correct for a SYSTEM task), logs to `logs/ssh_watch/ssh_watch_<date>.log` with 30 day retention.
- `scripts/install_ssh_watch_task.ps1` plus self elevating `Install_SSH_Watch_Task.bat`: registers scheduled task `SSH_Watch_DeviceActivity`, SYSTEM, AtStartup (not AtLogon, because SSH logins land in session 0), no execution time limit, restart every minute. `-Status` works unelevated; `-Remove` uninstalls. INSTALLED AND VERIFIED RUNNING 2026-11-22 12:25 MST.
- `logs/device_names.json` now labels both machines, both tailnet addresses and the router.

Host facts confirmed 2026-11-22: sshd Running, `LogLevel VERBOSE`, `PasswordAuthentication no`, `AuthenticationMethods publickey`, `AllowUsers ohjos`, keys in `C:\ProgramData\ssh\administrators_authorized_keys` (not `~/.ssh`, because ohjos is an administrator; the file is ACL locked and unreadable unelevated). 196 accepted logins from the laptop over the tailnet in 72 hours, zero refused attempts. `Get-NetFirewallRule` returns "Access is denied" unelevated, so firewall claims need the elevated rlink check.

Screen share state 2026-11-22: Sunshine service Running on the desktop, listening on 47984/47989/47990, AMD AMF h264, HEVC and AV1 encoders all found, capture 5120x1440. `sunshine_state.json` already holds ONE paired client named "Laptop" (paired 2026-11-13), so laptop to desktop streaming is paired already. The 2026-11-13 failure in `logs/pairing/` was the REVERSE direction (desktop as client, laptop's Sunshine unpaired). ViGEmBus is NOT installed, so no gamepad input passes to a stream. `apps.json` offers Desktop and Steam Big Picture.

Streaming host fix, added 2026-11-22: `Fix_Streaming_Experience.bat` (self elevating) plus `scripts/fix_streaming_experience.ps1`. Four idempotent steps: install ViGEm.ViGEmBus through winget (winget v1.29.380 is present; package `ViGEm.ViGEmBus` 1.22.0), add inbound firewall rules for TCP 47984/47989/48010 and UDP 47998-48010 scoped by remote address to 192.168.0.0/24 and 100.64.0.0/10 only (47990 web UI deliberately NOT opened), pin `encoder = amdvce` in sunshine.conf after a timestamped backup, then restart the service and print encoders plus paired clients. RUN AND VERIFIED 2026-11-22 12:25 MST.

Desktop shortcuts created 2026-11-22 in `C:\Users\ohjos\Desktop` (the active Desktop; an unused `OneDrive\Desktop` also exists): "Who Is On My SSH", "Install SSH Watch Task", "Fix Streaming Experience".

Network facts for streaming, measured 2026-11-22 12:00 MST: the SSID is named "TP-Link_FORTRESS 2.4G" but the actual link is 5 GHz, channel 157, 802.11ac, 866.7 Mbps both directions at 100 percent signal, so Wi-Fi is NOT the bottleneck despite the misleading name. Sunshine 7.1.431 answers serverinfo HTTP 200 on 127.0.0.1, 192.168.0.152 and 100.125.102.88. The laptop is reachable direct at 192.168.0.211:41641 over the tailnet.

SSH access INTO the laptop from the desktop, as of 2026-11-22: `ssh SurfacePro` fails with "Permission denied (publickey)" because `id_ed25519_surfacepro` ("shell-DIMASKUSPC->ZAYNESURFACE11") was never authorized on the laptop; run `scripts/enroll_desktop_shell_key.ps1` ON THE LAPTOP to fix. The `rlink-zaynesurface11` and `-ts` aliases DO connect but are tunnel only: a remote command returns empty output with exit code 0, so no shell is available. Consequence: the laptop cannot be driven from a desktop session, so Moonlight settings have to be done by hand there.

INSTALL RESULTS, 2026-11-22 12:25 MST, all verified live:
1. ViGEm Bus Driver 1.22.0 installed through winget, `C:\WINDOWS\system32\drivers\ViGEmBus.sys`, state Running, start mode System. NO REBOOT WAS NEEDED.
2. Scheduled task `SSH_Watch_DeviceActivity` installed, running as SYSTEM, monitor process alive, per run logs under `logs/ssh_watch/`, error file empty, new events appended every 30 to 40 seconds.
3. Firewall rules present. IMPORTANT: rlink had ALREADY created five rules ("rlink Sunshine TCP/UDP (peer LAN only)" Private, "rlink Sunshine TCP/UDP (peer + clients tailnet IPs, Tailscale only)" Any, and "rlink block Sunshine web UI from network" Block Any), so the firewall was never the blocker. The two rules added by fix_streaming_experience.ps1 are REDUNDANT but looser in one useful way: rlink pins the peer IP, so a DHCP change would break its LAN rule while the /24 rule keeps working.
4. `encoder = amdvce` pinned; Sunshine now tries only amdvce and finds h264_amf, hevc_amf and av1_amf. Backup `sunshine.conf.2026-11-22_121426.bak`.

FOUR GOTCHAS LEARNED THE HARD WAY, 2026-11-22, all now encoded in the scripts:
1. ViGEmBus is a KERNEL DRIVER, so `Get-Service *ViGEm*` returns nothing even when it is installed and running. Use `Get-CimInstance Win32_SystemDriver`. The wrong check made a successful install look like a failure needing a reboot.
2. A scheduled task that runs as SYSTEM is INVISIBLE to an unelevated shell: both `Get-ScheduledTask` and `schtasks /query` report it missing. Twice this looked like "something deleted the task". `install_ssh_watch_task.ps1 -Status` now says so and falls back to judging liveness from the log file age.
3. `Win32_Process.CommandLine` is NULL for processes owned by other users when not elevated, so any unelevated "is my SYSTEM process running" check that filters on CommandLine silently finds nothing.
4. `Start-Process -ArgumentList` does NOT quote arguments: an unquoted `F:\GitHub Repos\...` path reached Python as two arguments and died with "can't open file 'F:\GitHub'". Every repo path here contains a space, so quote script paths explicitly. Related trap: `$ErrorActionPreference = 'Stop'` turns a native command's stderr into a TERMINATING error, which killed the watcher silently; the runner now launches the monitor as a redirected child process with stdout and stderr in separate per run files, and sets PYTHONIOENCODING=utf-8 since SYSTEM has no console code page.

Also added: `scripts/run_all_installs_elevated.ps1`, which runs every elevated job behind ONE consent prompt and writes a transcript to `logs/installs/installs_<stamp>.log`. Each job is wrapped in its own try block, because on the first attempt one job's status display threw and cancelled the next job entirely.

Documentation state after 2026-11-22: the new tooling is written up in THREE places, all pushed to origin/main. (1) `docs/SSH_WATCH_AND_STREAMING.md`, 213 lines, the standalone reference. (2) `README.md`, Key Features items 4 and 5 plus a new "Who Is Using My SSH" section before the electricity formulas, with TOC entries. (3) `docs/index.html`, new content section 19 (id `ssh-watch`, nav entry 25), the changelog h2 renumbered to 20, a v3.2.0 row, and the sidebar tag now "v3.2.0 Session Visibility Edition". The owner gave explicit permission to edit those last two, which were earlier sessions' work. The `<title>` in index.html still says v3.0 and was already out of step before this; left alone. NOTE for future HTML edits: content h2 numbering and sidebar nav numbering are TWO DIFFERENT SCHEMES in that file (nav ran to 25 while content ran to 19); keep each internally consistent rather than trying to reconcile them. The repo tree in README was already an incomplete inventory of scripts/ and still is.

Related: [[user_github_and_devices]], [[project_local_llm_coding_setup]], [[reference_ohjoshrules_memory_sync]]
