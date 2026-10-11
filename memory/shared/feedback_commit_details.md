---
name: feedback_commit_details
description: All git commits must be extremely detailed: exact files, exact lines, before vs after, technical reasoning, runtime isolation, and test verification
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ee66bb5c-78a6-42fe-93f2-3a4be8d8057c
  modified: 2026-10-11T05:40:00.000Z
---

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
