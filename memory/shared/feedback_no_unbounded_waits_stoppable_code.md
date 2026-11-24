---
name: feedback-no-unbounded-waits-stoppable-code
description: "PERMANENT coding rule from the 2026-11-23 desktop hang: every program our code starts gets a time limit and a whole family stop, nothing waits on a person, scheduled jobs cannot pile up, and shells are not used where a direct start will do"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 1357db99-9ad1-48ec-8f53-a505f7663727
  modified: 2026-11-23T17:52:14.540Z
---

The owner asked on 2026-11-23, after a morning lost to hung processes: "make sure all of our code can be killed if
needed", and then asked for the fixes and the way to write code so it does not happen again to be remembered.

**The rule: no code of ours may wait forever, and no code of ours may keep starting new copies of something stuck.**

**Why:** on 2026-11-23 a fault in Windows made one call (host name and ping) never return. Our code turned one
fault into about 290 hung processes because nothing had a limit: `sync_memory.py` ran `git push` with no time limit
under a task allowed 72 hours; a status page task started a new `bash --login` every 5 minutes; hook scripts went
through bash on every tool call; a python started 82 pings in one second. No program can be made stoppable while it
sits inside a call that never returns, so the protection has to be around it. See
[[reference-desktop-shell-hang-icmp-wedge]].

**How to apply, in any language, in every repo:**

1. **Every child program gets a time limit.** Never a bare `subprocess.run(...)`, `.output()`, `.status()`,
   `.wait()` or `Start-Process -Wait`. Pick a limit that fits the job (a push of small files: 2 minutes).
2. **When the limit runs out, stop the whole family, then stop waiting.** Start the child as the head of its own
   group (`CREATE_NEW_PROCESS_GROUP` on Windows, `start_new_session=True` elsewhere); on Windows stop it with
   `taskkill /F /T /PID`, elsewhere `os.killpg`; in Rust on Windows the right tool is a Job Object with kill on
   close. If the stopped child still has not gone after a short second wait, give up on it and return an error.
   Killing only the direct child leaves its helpers behind (git starts `git-remote-https` and a small shell).
3. **A child must never wait for a person.** Close its stdin (`DEVNULL`), set `GIT_TERMINAL_PROMPT=0` for git, pass
   the non interactive flag of whatever tool it is. A hidden scheduled job asking a question waits forever.
4. **Do not go through a shell when the program can be started directly.** The shell was the thing that hung.
   Start `python.exe script.py` or the `.exe` itself, not `bash -c "..."` or `bash --login script.sh`. In RustTOS,
   prefer a Rust program to a shell script.
5. **Scheduled tasks cannot pile up.** `MultipleInstances = IgnoreNew`, an `ExecutionTimeLimit` a little above the
   job's real length (never the 72 hour default), and the script's own limits shorter than the task's. A job that
   keeps failing should say so (log, alert) instead of quietly trying again forever.
6. **Never fan out without a cap, and never use ping as a clock or a health check.** A fixed small number of
   children at a time, each with its own limit.
7. **Network calls inside a program need limits too:** connect and read timeouts on every request.
8. **No hard coded drive letters in anything a schedule runs** (two tasks pointed at a D drive that did not exist
   and failed silently for months). See [[feedback_cross_device_paths]].
9. **Things the owner wants by hand run from a bat, not from a sign in or clock trigger.** Ask before adding any
   auto start.
10. **Prove the limit with a test:** a harmless stuck program that starts its own stuck helper; assert the call
    gives up near the limit and that BOTH processes are gone. `sync_memory.py` was proven this way (given up on
    after 4.8 seconds with a 4 second limit).
11. **When diagnosing, never silence the error of a kill** and then conclude a process "will not die".
12. **Python's `subprocess.run(..., timeout=N)` is NOT a complete time limit.** When the time runs out it stops the
    child and then waits for it to go away with no limit at all. That is what froze the SSH watch for a whole day
    on 2026-11-23 although its code "had a timeout". Use `Popen`, `communicate(timeout=N)`, `kill()`, then a SECOND
    `communicate(timeout=small)`, and give up if that one runs out too.
13. **A loop that runs for weeks needs a safety stop.** If a helper was stopped and would not go away, count it,
    start no more of that kind, and say so in the log on every skipped pass (the SSH watch's sweep does this with
    `stuck_helper_count`). Otherwise a correct time limit just turns one frozen program into a growing pile.

14. **A timeout option is a promise, not a proof: test the alert path on the fault it is for.** In Windows
    PowerShell 5.1, `Invoke-RestMethod -TimeoutSec 10` hung for more than 90 seconds on the wedged desktop (it looks
    at the network adapters before sending, and that look never returned). Python's `urllib` with a timeout got
    through on the same machine. The launcher's alert now runs the Python sender as a child and enforces the
    limit itself (`WaitForExit` then `taskkill /F /T`). Whoever waits must own the clock.
15. **Do not use Python's `ipaddress.is_private` to mean "my home network".** It also says yes to documentation
    and test ranges (203.0.113.x, 198.51.100.x, 192.0.2.x). List the ranges you mean (10/8, 172.16/12,
    192.168/16, fc00::/7) one by one.

**State of the code on 2026-11-23:** `C:\Users\ohjos\ohjoshrules\sync_memory.py` follows this
(`run_with_time_limit`, `stop_process_tree`). RustTOS does NOT yet: every child start goes through
`crates/rusttos-core/src/platform/child_process.rs`, which has no time limit, and at least 15 shipped call sites
wait with none (`gh`, `w32tm`, `powershell`, `schtasks`). The planned fix is one time limited runner in that module
and moving the callers onto it. Verify this is still true before repeating it.

Related: [[feedback_explanatory_comments]], [[feedback-no-abbreviations-detailed-docstrings]], [[project_rusttos]].
