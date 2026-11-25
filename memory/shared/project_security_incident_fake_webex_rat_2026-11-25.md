---
name: project-security-incident-fake-webex-rat-2026-11-25
description: "Desktop RAT compromise 2026-11-25 (fake Webex -> Zoho Assist + ScreenConnect); removed, but rotate broker API creds and treat as potentially-compromised until reimage"
metadata:
  node_type: memory
  type: project
  originSessionId: 7510f94d-d9ef-4a28-b04c-06459121f36f
  modified: 2026-11-25T22:42:02.542Z
---

On 2026-11-25 (~15:01 to 15:14 MST) DimaskusPC was briefly compromised. The user downloaded `WebexMeeting.Setup.exe` from the fake site **webexlive.cc** (NOT Cisco). It was a renamed **Zoho Assist Unattended Agent** that also installed a **ScreenConnect** client configured for unattended access to attacker host **polarmantar.top = 45.87.61.81** (port 8041). Both are legitimate remote-access tools abused as a RAT. The genuine `Webex.exe` the user also downloaded (Cisco-signed) is fine.

**Exposure window ~13 minutes.** Confirmed the PC resolved/contacted polarmantar.top (DNS cache), but no live session remained after removal.

**Remediation done this session:** both products MSI-uninstalled (event log 15:14 "Removal completed successfully"), services/processes killed, folders gone, fake installer quarantined to `Desktop\Quarantine_2026-11-25\*.BLOCKED` (SHA256 369D3366C4AFBD35A280232B6FBA8A04153CBE98AB357A003BCAFAA32C949D10). Full Defender scan launched. All browsers (Chrome/Brave/Edge/Firefox) cleared of cookies/history/cache (passwords + bookmarks kept). Forensic scan found **no new persistence** (no new services, scheduled tasks, Run keys, SSH keys, shell-profile edits, Claude-settings/hook edits, git-config/hook edits, or modified credential files).

**Desktop helper scripts created:** `CLEANUP_REMOTE_ACCESS_MALWARE_2026-11-25.bat`, `BLOCK_ATTACKER_IP_2026-11-25.bat` (firewall + hosts null-route), `HARDEN_FIREWALL_2026-11-25.bat` (default-deny inbound). These need the user to double-click (UAC) because the Claude session is not elevated.

**Still owed by the USER (standing):**
1. From a CLEAN device: change email, brokerage (IBKR/Schwab), bank passwords; "sign out all sessions"; enable 2FA; call IBKR/Schwab fraud lines (window 15:01-15:14 MST).
2. **Rotate all broker/service API keys and `.env` secrets** on this machine: reading leaves no trace, so treat plaintext creds as potentially exfiltrated. [[project_brokers_schwab]] [[project_rusttos]]
3. Expect follow-up social engineering (fake "support"/"bank" calls/emails). Verify via official numbers only.
4. Gold standard for a hands-on-keyboard RAT is a full Windows reimage; until then treat the machine as not-fully-trusted for sensitive logins.

Why this matters: the real loss vector is stolen credentials/session cookies used from the attacker's own device, which no local firewall stops.
