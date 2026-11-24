---
name: reference-rusttos-preflight-stale-base
description: "RustTOS `rusttos_agent preflight` keeps blocking after main is merged into the branch, because it measures from the claim's base_commit, which a merge never updates"
metadata:
  node_type: memory
  type: reference
  originSessionId: 91289bf2-7e78-473d-a1f7-297fdb2dcefb
  modified: 2026-11-24T07:07:36.508Z
---

`rusttos_agent preflight NAME` (crates/repo-tools/src/bin/rusttos_agent.rs, `preflight_command`) measures "what the trunk changed" as `git diff BASE..trunk`, where BASE is the claim manifest's `base_commit` from `rusttos_agent start`. Merging main into the branch does not change that field, so a file both sides touched stays a BLOCKER ("changed by you AND on the trunk since <base>") forever, even when main is fully inside the branch.

Seen 2026-11-24 on agent/complaints-recheck: after merging origin/main (d9b867fd) the preflight still named chart_app.rs and chart_grid_view_tests.rs "since 0514d475".

**How to apply:**
1. After merging main in, prove it with `git merge-base --is-ancestor origin/main HEAD` (exit 0 = main is inside, nothing on main can be dropped) and with no file changed on both sides since `git merge-base HEAD origin/main`. If both hold, the blocker is stale; say so in the merge message and push (the enforced gate is the pre-push hook).
2. A branch with no claim at all (agent/armed-orders, agent/depth-tools, agent/todo-next-steps) gets "no agent called X is written down" and cannot be preflighted.
3. Not fixed in the tool as of 2026-11-24: the clean fix is to judge from `merge-base(branch, trunk)` when the trunk is an ancestor, or to update `base_commit` on a trunk merge.

Related: [[feedback-one-worktree-per-session]], [[feedback-never-git-add-all-shared-worktree]], [[project_rusttos]].
