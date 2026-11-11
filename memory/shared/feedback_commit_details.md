---
name: feedback_commit_details
description: "extremely detailed commits AND merge commits: source branch, files, exact lines, fns/defs/tests added, before/after, reasoning, tests"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ee66bb5c-78a6-42fe-93f2-3a4be8d8057c
  modified: 2026-11-10T18:00:00.000Z
---

**Summary moved from the memory index (2026-11-08):** All git commits must be extremely detailed: exact files, exact lines, before vs after, technical reasoning, runtime isolation, and test verification

Whenever authoring or amending git commits, write **extremely detailed commit comments**:
1. Itemize every single file that was modified, added, renamed, or deleted with exact line ranges and code symbols.
2. Explicitly state the "What it was vs what it now is" (before vs after comparison) for each file or module.
3. Detail the exact technical rationale and reasoning behind every modification (purpose, consequence, and why simpler options were rejected).
4. Declare the runtime boundary and isolation tier (Host Only, Docker Isolated, or Pure Math) plus cross-device path compatibility.
5. Provide verification and test evidence with exact test commands, passing metrics, execution duration, and exit codes.
6. Reference the active roadmap file under CodeMapping_Brain/content/roadmaps/ and the specific completed step.

**Why:** The user explicitly requested this rigor ("can we make sure that we also do this kind of details on our commits?" and "how can we improve the permanent git commit standards?"). Detailed commits guarantee an auditable, reproducible codebase across desktop, laptop, and Raspberry Pi environments.

**How to apply:**
- Structure commit messages following .gitmessage:
  1. Header: concise summary line under 72 characters.
  2. Section 1: Files and Exact Line Numbers.
  3. Section 2: What It Was vs What It Now Is.
  4. Section 3: Technical Rationale.
  5. Section 4: Runtime Boundary and Isolation.
  6. Section 5: Verification and Test Evidence.
  7. Section 6: Roadmap Reference.
- Follow typography rules: no em-dashes, no en-dashes, no `--` sentence connectors, no section signs. Use numbered lists (1., 2., 3.) instead of markdown dash bullets for prose.
- Enforce automatically using scripts/dev/validate_commit_msg.py and the git commit-msg hook.

**Merge commits (user, 2026-11-10 ~17:55 MST, RustTOS session):** "for all future branches when they get merged can we improve the comments that highlights what branch they came from, and what goes and what exact lines of code they touched along with what defs and fns and test methods its created ... so that comments are very well defined". A bare "Merge agent/x" message is NOT acceptable any more. Every merge commit message must contain:
1. Source: the branch merged, its head commit, the target branch and its commit before the merge, and every agent branch or commit it carries (for an integration branch, list each included branch with its head).
2. What goes in: a one line purpose per included branch.
3. Files and exact lines: every file added, changed or removed, with the exact line ranges touched (for shipped files that only gained an include, say so with the line numbers).
4. Definitions: every fn, def, struct, enum, trait, impl and const ADDED, CHANGED or REMOVED, with file and line, grouped by file.
5. Test methods created: the count per test file and per function under test, plus the test names (or the name pattern and range, e.g. `round_net_case_01` to `_52`, when there are thousands).
6. Conflicts: each conflicted file and exactly how it was resolved.
7. Verification: the checks run on the merged code (commands, pass/fail counts, exit codes, times with zone) and where the results file is; for fast lane merges, the audit line.
8. The usual six sections (.gitmessage) and the typography rules above.

**How to apply for merges:** in RustTOS, generate the body from git with `cargo run -q -p repo-tools -- commit-report --merge <branch> --into <target> [--checks <merge_checks results json>]` (it lists files, line ranges, items added/changed/removed and unit tests from the real diff), then add sources, purposes, conflicts and the test-method summary, and commit with `git merge --no-ff --no-commit` + `git commit -F <file>`. In other repos without commit-report, gather the same facts with `git diff --stat`, `git diff -U0` and a symbol listing. When another session (e.g. the RustTOS coordinator ohjos-aa) does the merge, hand it these facts with the branch so its merge message can carry them.
