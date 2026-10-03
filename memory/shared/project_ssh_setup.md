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

Related: [[user_github_and_devices]], [[project_local_llm_coding_setup]], [[reference_ohjoshrules_memory_sync]]
