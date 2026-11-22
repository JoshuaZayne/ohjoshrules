---
name: feedback-one-worktree-per-session
description: "RustTOS: every session gets its OWN git worktree and its OWN cargo output folder; never share one working folder"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 1357db99-9ad1-48ec-8f53-a505f7663727
  modified: 2026-11-22T22:15:10.339Z
---

The owner, 2026-11-22 15:20 MST: "set up a separate worktree for each session".

**Every session works in its own git worktree, on its own branch, with its own cargo output folder.** Never two
sessions in one working folder.

**Why.** On 2026-11-22 the repository had ONE working folder shared by several sessions. At 14:48 one session
checked out a new branch in it while another was mid task; at 14:59 the second ran `git add -A` and committed
1,771 lines of the first's uncommitted work under its own commit message. Recovered and verified with SHA-256,
but no claim system could have prevented it: a claim describes intent, a blanket add takes what is on disk. One
folder with several writers is the fault.

**What it costs, measured the same day:** a worktree's source checkout is 93 to 114 MB. The build cache beside it
was 50.3 GB. So the worktrees are nearly free, and the CACHES are what must be kept apart and off the recorders'
drive.

**How to set one up:** `new_session_worktree.ps1` in the agents folder beside the repository.

```
powershell -ExecutionPolicy Bypass -File new_session_worktree.ps1 -Name chart-speed `
    -Goal "the owner's seven chart fixes" -Crates rusttos-chart -Paths crates/rusttos-chart
```

It makes the worktree at `<agents folder>\<name>` on branch `agent/<name>`, makes a cargo output folder of its own
at `%USERPROFILE%\RustTOS_targets\<name>`, registers the claim through `rusttos_agent start` (printing the overlap
warnings, which are the point), and writes `open_<name>.cmd` beside it that opens a shell with both already set.
It refuses a name whose branch exists, a worktree folder that exists, a name that is not lower case words joined
by dashes, and any drive at 90 percent or more. `-WhatIfOnly` checks without making anything.

**How to apply:**
1. One session, one worktree, one branch, one cargo output folder. Open it with its `open_<name>.cmd`.
2. The main working folder is for the trunk. Do not do session work in it.
3. Build caches go on the roomy drive, one per session. Two sessions sharing one cache serialise on its lock and
   can poison each other's incremental state.
4. Before pushing: `rusttos_agent preflight <name>`, and stage files BY NAME
   ([[feedback-never-git-add-all-shared-worktree]]).
5. When finished, `rusttos_agent log <name> merged "..."` so the claim is released, then delete that session's
   cargo output folder. Check no other session is using a folder before deleting anything shared
   ([[feedback-builder-parallelism-and-resources]]).
6. A gotcha the script already handles: run cargo from the NEW worktree, never from wherever the script was
   started, because the main folder may hold another session's half written code that will not build.

Related: [[project_rusttos]], [[feedback-builder-parallelism-and-resources]],
[[feedback-never-git-add-all-shared-worktree]], [[project_rusttos_round_driver_and_tracker]].
