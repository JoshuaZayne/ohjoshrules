---
name: feedback-architecture-md-append-only
description: "RustTOS docs/ARCHITECTURE.md is APPEND ONLY: never delete or shorten a section, only add and improve"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 1357db99-9ad1-48ec-8f53-a505f7663727
  modified: 2026-11-22T20:06:08.155Z
---

The owner, said twice: on 2026-11-20 ("update todo lists and archiecture md file - dont be removing sections from
that md file ony adding too it") and again on 2026-11-22 ("make sure in memory we dont delete stuff in archiecture
md file but that we append and improve it").

`docs/ARCHITECTURE.md` in the RustTOS repository is APPEND ONLY. Never delete a section, never shorten one, never
replace one with a tidier summary, and never "reorganise" it. Add new sections, and improve existing ones by adding
to them.

**Why:** it is the one place the whole build is described, written across many sessions by different agents. A
section that looks redundant to the session reading it is usually the only record of a decision someone made for a
reason that is not visible from the code. Deleting it destroys the reason and nobody notices until the mistake is
repeated.

**How to apply:**
1. Edit it with additions only. If something in it is now WRONG, do not delete the wrong text: leave it and add a
   dated correction beneath it saying what changed and when, the way the worklog files do.
2. After any substantial piece of work, append what changed: the new modules, what they do, what was measured, and
   the decision numbers. Do this in the same session as the work, not later.
3. The same instinct applies to the todo files in `docs/todo/`: statuses are updated in place, but sections are not
   removed.
4. This is a different rule from [[feedback_dont_edit_existing_md]], which is about not touching .md files other AI
   tools wrote. This one is about a file that IS ours and must still only grow.

Related: [[project_rusttos]], [[feedback_commit_details]], [[feedback_explanatory_comments]].
