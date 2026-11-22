---
name: feedback-never-git-add-all-shared-worktree
description: "NEVER `git add -A` in RustTOS: one shared worktree, several sessions, and a blanket add steals another session's uncommitted work"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 1357db99-9ad1-48ec-8f53-a505f7663727
  modified: 2026-11-22T22:02:18.960Z
---

**NEVER use `git add -A`, `git add .` or `git commit -a` in the RustTOS repository. Stage files BY NAME, and check
`git branch --show-current` before every commit.**

**Why, measured 2026-11-22.** All the agent worktrees were removed on 2026-11-22 at 02:15 MST, so the repository
now has ONE working folder that every session shares. At 14:48:42 another session checked out a new branch
(`agent/tos-study-port`) in that shared folder while this session was mid-task, and began writing TOS study ports.
At 14:59:08 this session ran `git add -A` and committed. The commit swept up 1,771 lines of the other session's
UNCOMMITTED work across four files in `rusttos-indicators`, on a branch this session had never chosen, under a
commit message about something else entirely.

Two separate failures, and both have to be fixed in habit, not in tooling:
1. The other session switched branches in a shared worktree, with uncommitted work present and no claim written.
2. This session staged everything in sight without looking at the branch or the file list.

**How to apply:**
1. Stage by name, every time: `git add path/one path/two`. Then read `git diff --cached --name-only` BEFORE
   committing and confirm every path is one you wrote.
2. Run `git branch --show-current` before committing. The branch can change under you between one command and the
   next, because the folder is shared.
3. If a commit has already mixed two sessions' work: save BOTH sides first (`git show <commit> -- <paths>` into
   patches outside the repo), then `git reset --mixed <parent>`, which returns everything to the working tree and
   loses nothing because the commit stays in the reflog. Fingerprint the other session's files with SHA-256 before
   and after, so you can prove you did not alter them.
4. A claim in the agent registry CANNOT catch this. The claim describes intent; a blanket `git add` captures
   whatever is on disk. The preflight check added the same day would also have missed it, and its own test says
   so. This is a habit rule, and only a habit rule fixes it.
5. When sessions must run in parallel, give each its own git worktree. One shared folder with several writers is
   the underlying fault; everything above is damage limitation.

Related: [[project_rusttos]], [[feedback_commit_details]],
[[project_rusttos_round_driver_and_tracker]], [[feedback-builder-parallelism-and-resources]].
