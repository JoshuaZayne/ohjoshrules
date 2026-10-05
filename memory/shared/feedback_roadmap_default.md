---
name: feedback-roadmap-default
description: Every non-trivial planning task must default to creating a TODO roadmap .md in CodeMapping_Brain/content/roadmaps and updating it as work progresses
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e2ef58d5-9b19-4f19-aef7-7007c021715a
---

Whenever Claude does any non-trivial planning, design, or multi-step task, the FIRST action is to create a TODO roadmap markdown file at `~/repos/CodeMapping_Brain/content/roadmaps/YYYY-MM-DD_HHMMSS_<slug>.md`, then update it as steps complete.

**Why:** User wants to prevent work loss across chat boundaries: any future Claude can pick up where the last left off, and the codemap becomes a real planning hub. Explicitly requested as a global default on 2026-05-22.

**How to apply:**
- Frontmatter: `title, type: roadmap, tags: [roadmap, planning], status, created, repo`.
- Sections: `## Goal`, `## Steps` (numbered checkbox list), `## Context`, `## Outcomes`.
- Index it in `content/roadmaps/index.md`.
- Save a `project`/`reference` memory pointing to the file.
- Skip for: single-shot fixes, pure conversational answers, tasks already covered by an in-progress roadmap (update that instead).
- Full rule lives in `C:\Users\ohjos\CLAUDE.md` under "CRITICAL — Planning Roadmap Default". See also [[reference-codemap-aliases]] and [[feedback-file-timestamps]].
