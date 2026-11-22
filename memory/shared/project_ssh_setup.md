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
- `scripts/install_ssh_watch_task.ps1` plus self elevating `Install_SSH_Watch_Task.bat`: registers scheduled task `SSH_Watch_DeviceActivity`, SYSTEM, AtStartup (not AtLogon, because SSH logins land in session 0), no execution time limit, restart every minute. `-Status` works unelevated; `-Remove` uninstalls. AS OF 2026-11-22 THE TASK IS NOT YET INSTALLED: the owner has to run the .bat and approve the prompt.
- `logs/device_names.json` now labels both machines, both tailnet addresses and the router.

Host facts confirmed 2026-11-22: sshd Running, `LogLevel VERBOSE`, `PasswordAuthentication no`, `AuthenticationMethods publickey`, `AllowUsers ohjos`, keys in `C:\ProgramData\ssh\administrators_authorized_keys` (not `~/.ssh`, because ohjos is an administrator; the file is ACL locked and unreadable unelevated). 196 accepted logins from the laptop over the tailnet in 72 hours, zero refused attempts. `Get-NetFirewallRule` returns "Access is denied" unelevated, so firewall claims need the elevated rlink check.

Screen share state 2026-11-22: Sunshine service Running on the desktop, listening on 47984/47989/47990, AMD AMF h264, HEVC and AV1 encoders all found, capture 5120x1440. `sunshine_state.json` already holds ONE paired client named "Laptop" (paired 2026-11-13), so laptop to desktop streaming is paired already. The 2026-11-13 failure in `logs/pairing/` was the REVERSE direction (desktop as client, laptop's Sunshine unpaired). ViGEmBus is NOT installed, so no gamepad input passes to a stream. `apps.json` offers Desktop and Steam Big Picture.

Related: [[user_github_and_devices]], [[project_local_llm_coding_setup]], [[reference_ohjoshrules_memory_sync]]
