---
name: feedback_dont_edit_existing_md
description: "Don't modify existing .md files (especially ones another AI tool like Antigravity wrote) when applying content fixes; change .txt/.py or ask first"
metadata:
  node_type: memory
  type: feedback
  originSessionId: b1a303bc-5b53-4722-a84c-935cc04b33e7
  modified: 2026-10-04T20:52:06.970Z
---

When the user asks for wording fixes to drafts/emails, do NOT edit existing `.md` files in place, especially ones another tool (Antigravity, `agy/`) generated. Apply fixes to the `.txt` drafts and generator scripts, or ask where the change should go.

**Why:** 2026-10-04 in TicketProcessing, I bulk-edited 25 Antigravity `.md` files (email drafts and reports) along with the `.txt` drafts; the user said "please dont change old md files" and I had to reverse every substitution by hand (the files were untracked, so there was no git copy).

**How to apply:** Before any bulk `sed`/regex edit, list the target files and exclude `*.md` unless the user named them. Never bulk-edit untracked files you didn't create without a backup. Related: [[project_ticket_processing]].
