---
name: feedback_reuse_existing_code
description: "Before writing any new function/module, check the code brain for existing code and import/reuse it instead of writing a new copy"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 34178c54-c10f-43c6-b548-81ced589d7ee
  modified: 2026-09-19T21:32:29.608Z
---

Before writing or creating any new function, class, script or module, check whether the user already has code for it, and reuse or import it instead of writing a new copy.

**Why:** The user asked for this explicitly (2026-09-19) after the code brain found ~3,000 groups of duplicated code across their repos (the same helpers copied between Brokers, InterActiveBrokers-Project, FinanceCode, iCloud copies ...). They want new work to build on existing code, not add more duplicates.

**How to apply:**
- Search first: `python "<CodeMapping_Brain>/codemap.py" find <words describing the function>` (desktop path `F:\GitHub Repos\CodeMapping_Brain`); for a draft file, `codemap.py check <file>`.
- In Claude Code a PreToolUse hook (Write|Edit|MultiEdit) runs `codemap.py hook-precheck` automatically and injects "already exists at X, reuse with `from ... import ...`" notes. When that note appears, prefer the import unless the difference is intentional, and say so.
- If the brain is missing on a machine: `python codemap.py scan` then `python codemap.py install-hooks`.
- Cross-project matches: suggest a shared library rather than importing across repos ad hoc.

Related: [[project_codemapping_brain]].
