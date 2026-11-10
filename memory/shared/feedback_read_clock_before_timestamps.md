---
name: feedback-read-clock-before-timestamps
description: "never type a time from memory into a message, brief or reply; read TZ=MST7 date first"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 480f2ae3-588a-435b-bb15-a2402ff8ddc4
  modified: 2026-11-10T18:13:09.321Z
---

Every time written into a message to another session, an agent brief, a commit, a log or a reply to the user must come from the clock (`TZ=MST7 date` in Git Bash on the desktop) or from a log line, never typed from memory. A time from a log line must say which log it came from.

**Why:** in the RustTOS coordinator session of 2026-11-10, hand typed times ran 7 to 20 minutes ahead of the clock twice: once overnight, then again in messages and agent briefs at about 11:00 MST. Agents copied them into worklogs, and corrections had to be sent. The user requires every claim to carry a correct time with zone ([[feedback_verifiable_claims]]).

**How to apply:** before any message that names a time, run `TZ=MST7 date`. For when the user asked something, write "about HH:MM MST", taken from the nearest log line written from the clock. See [[reference-git-bash-mst-time]] (TZ=America/Phoenix silently prints UTC in Git Bash).
