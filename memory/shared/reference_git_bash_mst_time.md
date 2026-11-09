---
name: reference-git-bash-mst-time
description: "In Git Bash on the desktop, TZ=America/Phoenix silently prints UTC; use TZ=MST7 or plain date"
metadata:
  node_type: memory
  type: reference
  originSessionId: dfe8eb70-bebc-45d2-b981-4703bed5ae51
  modified: 2026-11-09T14:57:19.108Z
---

On the Windows desktop, Git Bash's `date` does not know the zone name America/Phoenix: `TZ=America/Phoenix date` silently falls back to UTC (seen 2026-11-09: it printed 14:50 while the real time was 07:50 MST). A format string with a literal "MST" then mislabels UTC as MST.

Use `TZ=MST7 date '+%Y-%m-%d %H:%M:%S MST'` (POSIX zone string, works), plain `date` (the machine is on MST), or PowerShell `Get-Date`. Check against `date -u` when a time matters.

Matters because the user requires real MST times on every claim ([[feedback_verifiable_claims]], [[project_rusttos]]).
