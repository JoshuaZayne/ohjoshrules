---
name: project-rusttos-feed-watchdog-not-deployed
description: "RustTOS every-minute 'data is down' Telegram alert is committed and pushed (agent/complaints-recheck) but NOT running: the live watchdog binary is the old one until the owner OKs a rebuild"
metadata:
  node_type: memory
  type: project
  originSessionId: 91289bf2-7e78-473d-a1f7-297fdb2dcefb
  modified: 2026-11-24T07:07:42.723Z
---

The feed watchdog change (Telegram every 60 s while the Schwab or IBKR recorder is down, silent 15:00 to 16:00 MST measured in America/Phoenix, outside the day's cap) was committed as 69f8aef3 and pushed on agent/complaints-recheck on 2026-11-24 (branch head 6725ae87, which also holds main d9b867fd). It is not on main.

**Why it matters:** it is NOT in service. The running program is `data/bin/rusttos-feed-watchdog-background.exe` in the main RustTOS folder, built before the change. It only takes effect once rebuilt from that branch, copied over that exe, and the program restarted. As of 2026-11-24 the owner had not said to do that.

**How to apply:** do not tell the owner the every-minute alert is live until the rebuild and restart are done with their OK. Once done (or once the branch reaches main and is deployed), delete this memory.

Related: [[project_rusttos]], [[reference-desktop-shell-hang-icmp-wedge]].
