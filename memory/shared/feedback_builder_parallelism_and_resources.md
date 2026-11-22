---
name: feedback-builder-parallelism-and-resources
description: "Parallel build agents on the desktop: RAISED 2026-11-22 to four agents at 6 jobs each, with cargo output moved OFF the recorders' drive onto C:"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 1357db99-9ad1-48ec-8f53-a505f7663727
  modified: 2026-11-22T20:13:47.328Z
---

## CURRENT RULE, set by the owner 2026-11-22 13:15 MST

Four build agents at once, **6 build jobs each** (24 jobs against 32 logical processors), and **all cargo output
goes to C:, never the recorders' drive**. `CARGO_TARGET_DIR` is set at the user level to a target folder under the
home directory on C:.

**Why it was raised:** the old cap of two agents at 4 jobs was set on 2026-11-12 when drive F filled and a recorder
lost 8,670 rows, and when memory stops were killing jobs. Both constraints are gone. Measured 2026-11-22 13:10 MST:

| | when the old cap was set | now |
| --- | --- | --- |
| RAM | memory stops killing jobs; 16 GB as of 05:02 that morning | 127.88 GB, 105.76 free, 8 of 8 slots |
| commit limit | 31.88 GB | 143.88 GB |
| F: free | hit ZERO on 11-12 | 247 GB |
| C: free | not used for builds | 1,908 GB |
| logical processors | 32 | 32, unchanged |

**Why the target folder move matters more than the job count:** disk, not memory, was the binding constraint, and
the disk in question was the one the live recorders write to. A build can no longer fill it. That removes the
original cause of the 2026-11-12 data loss rather than working around it. The folder already existed with a warm
cache, so the move cost no cold rebuild.

## BOTH DRIVES MAY BE USED, with a finish and reduce cycle (owner, 2026-11-22 14:47 MST)

The owner: "you can use both drives, but when they get full we need to 'finish' them and then commit and reduce
them". So build output is NOT confined to C:. Either drive may carry it. What matters is what happens as one
fills:

0. FIRST, before reclaiming anything: find out whether another session is using it. The repository has ONE shared
   working folder, so `<repo>/target` may be the build cache another session is compiling into right now.
   Deleting it forces them into a full rebuild mid-task. The owner, 2026-11-22 15:10 MST: "wait until sessions
   finish, and dont repeat todays lesson twice". WAIT. Shared build output is reclaimed only when no other
   session is working, or when they say they are done.
1. When a drive passes about 85 percent full, STOP starting new work on it.
2. FINISH what is in flight: bring the piece to a state where its tests pass.
3. COMMIT it, so nothing in the build folder is the only copy of anything.
4. REDUCE: delete that work's build folder. `cargo clean -p <crate>` for one crate, or remove the whole target
   folder when the piece is done and committed.
5. Only then start the next piece.

NOTE the trap found the same day: setting `CARGO_TARGET_DIR` with
`[Environment]::SetEnvironmentVariable(...,'User')` writes the registry but does NOT reach processes that are
already running, including the shells of the session that set it. Builds kept going to the old drive for hours
and F: fell from 249 GB free to 164 GB. Either pass `CARGO_TARGET_DIR` on the command itself, or accept that the
setting only applies to terminals opened afterwards. Check it with `echo $CARGO_TARGET_DIR` in the shell that
will actually run cargo, not with the registry value.

**How to apply:**
1. At most four build agents at once, in lanes that do not touch the same code; 6 build jobs each.
2. Before every build still read free memory and free disk. The old stop levels (20 GB memory, 40 GB disk) are now
   easy to meet; treat them as a floor, not a target, and stop with a checkpoint commit if either is approached.
3. Cargo output may go on either drive (see the section above). C: is the better default because it is far larger
   and is not the drive the live recorders write to, but F: is allowed. What is NOT allowed is letting either
   drive fill: follow the finish, commit, reduce cycle above.
4. After a piece lands on main, delete its build folder before starting the next. One agent worktree reached
   93.3 GB on its own.
5. Never run a test round and agent builds at the same time without a marker the agents check.
6. **Still ask before raising this again.** The owner has approved each increase in turn: one agent, then two
   (2026-11-13), then four (2026-11-22).
7. Re-measure RAM before relying on it. This machine's RAM changed by 112 GB twice in one day on 2026-11-22; see
   [[reference-desktop-hardware-inventory]]. The modules run at 2133, not their rated 3000, and the owner chose on
   2026-11-22 to leave them there rather than risk another POST training failure.

## History

On 2026-11-12 (about 18:13 MST) the owner said: "I think we need to pause blowing up my disk space, I think its
could be slowing it down? so how can we focus on 1 agent at a time, finish its build out, upload it to main, then
clean up my F and C drive of whatever extra stuff it was using?" Earlier that day six build agents plus a test
round had filled drive F (a recorder lost 8,670 rows) and a memory stop had killed two jobs. On 2026-11-13 (about
10:30 MST) the owner approved two at once ("do it, so yes") after being shown which work does not overlap. On
2026-11-22 the owner asked to look at the resources again and approved four at 6 jobs with the output moved to C:.

Interpretation (mine): this applies to any heavy compile work on the desktop, not only RustTOS.
