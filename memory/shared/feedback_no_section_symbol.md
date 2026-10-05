---
name: feedback-no-section-symbol
description: "Never use the section-sign symbol in any document or output; write the word \"section\" instead."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b0cc7eca-7d03-44e1-b161-622a272d4070
---

NEVER use the section-sign character (U+00A7, the "section" symbol) in any
document, file, comment, commit message, or chat output. Write the word
"section" (e.g., "section 9.11", "see section 4") instead.

**Why:** The user explicitly banned it on 2026-05-23 ("NEVER EVER USE THIS ... IN
ANY DOCUMENT") after seeing it in a generated report.

**How to apply:** When cross-referencing document sections, use "section N" in
prose or a markdown link like `[section 9.11](#anchor)`. A purge agent exists at
`~/.claude/agents/section-symbol-purger.md` to find and remove the symbol
everywhere. Related: [[feedback_no_dashes]] (same spirit: banned punctuation).
