---
name: feedback-never-skip-commit-hook
description: "When a commit hook cannot run, the user chose to wait rather than commit with --no-verify, even with the hook's check run by hand (2026-11-23, RustTOS)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: ae451a03-660d-476d-a38a-bc12d941c0f8
  modified: 2026-11-23T17:00:37.776Z
---

On 2026-11-23 about 10:00 MST, in RustTOS, the commit hook could not start (no shell on the desktop would run). I had run the hook's only check, `repo-tools validate-commit-message`, by hand on all three messages and it passed. Offered "commit now with the hook skipped (recommended)" or "wait for a reboot", the user picked **wait for a reboot**.

**Why:** the user did not give a reason. My reading (mine, not theirs): they want commits to go through the repo's own gate the normal way, and a broken machine is a reason to fix the machine, not to go around the gate.

**How to apply:** when a hook cannot run, do not recommend skipping it. Finish and test the work, write the commit messages, validate them by hand if possible, put the messages plus a small commit script and the diff somewhere a reboot will not clear (not the session scratchpad), record it in memory, and say plainly that the commit is waiting. Scope: observed once, in RustTOS; treat it as the default for this user's repos unless they say otherwise. See [[project-rusttos-armed-orders-pending-commit-2026-11-23]].
