---
name: project-rusttos-level2-devices-roadmap
description: "RustTOS Level 2 across devices: on 2026-11-24 the LAPTOP recorded depth and uploaded every 2 min while the desktop Gateway was down; roadmap for Gateway up catch up and device sync"
metadata:
  node_type: memory
  type: project
  originSessionId: 91289bf2-7e78-473d-a1f7-297fdb2dcefb
  modified: 2026-11-24T08:28:35.698Z
---

Measured 2026-11-24 01:27 MST: after the desktop's Windows restart its IB Gateway stayed logged out (passkey second factor, so no cold auto login), while the laptop ZayneSurface11 was recording Level 2 (6AZ26, 6EZ26, 6JZ26), ticks and bars and uploading to JoshuaZayne/RustTOS-data-backup release `intraday-<UTC day>` every 2 minutes. Nothing on the desktop pulls those uploads automatically.

**Why:** one IBKR login gives 3 depth books across all computers together, so two recorders on the same username fight. The owner asked how to start Level 2 the instant the Gateway is up, catch the data repo up, and keep every device in sync.

**How to apply:**
1. Check who is recording with `Desktop\RustTOS commands\7 ...\13 Which computer is recording` (reads the repo's intraday uploads).
2. The plan, with measured facts and TODO steps (A Gateway up, B catch up, C device sync, proposed frequencies): `F:\GitHub Repos\CodeMapping_Brain\content\roadmaps\2026-11-24_012823_rusttos-gateway-up-level2-and-device-sync.md`. Open owner decisions: which ONE computer records Level 2; which IBKR login each computer uses.
3. Do not log the desktop's Gateway in without asking while the laptop is recording: the same username may end the laptop's session.

Related: [[project_rusttos]], [[reference-ibkr-logins-and-subscriptions]], [[reference-rusttos-desktop-commands-folder]].
