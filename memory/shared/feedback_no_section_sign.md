---
name: feedback_no_section_sign
description: User dislikes the § (section sign) — never use it in output or files
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d922e761-6958-4bbd-b601-44af9f52b242
---

The user dislikes the `§` (section-sign) character. Never use it — not in prose, code comments, docs, or filenames. When cross-referencing a numbered section, write "section N" instead of "§N".

**Why:** Explicit stated dislike of the symbol.

**How to apply:** Never emit `§`. If it already exists in files being edited, replace it with "section" (e.g. `§8` → `section 8`). Already scrubbed from `Yearly_and_monthly_spend_per_CC/ARCHITECTURE.md`.
