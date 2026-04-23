---
name: Windows case-insensitive folder collisions during reorg
description: Avoid creating new folders whose names collide with Windows standard folders; use distinctive versioned names and verify before moving files
type: feedback
originSessionId: 15eafbc4-9b2a-4224-8d55-91df6f86ddf9
---
When organizing files on Windows, never create a new top-level folder whose name matches (case-insensitive) an existing Windows standard folder. NTFS is case-insensitive, so `mkdir documents` silently resolves to the existing `Documents\` and files get merged into unrelated content.

**Why:** During the 2026-04-23 reorg of `C:\Users\ohjos\`, I created `documents\` to hold `DD214.pdf` and `bullet trap building build.pdf`. The mkdir folded into the Windows `Documents\` folder and the two PDFs ended up mixed among ~80 pre-existing personal files. User explicitly asked that we "have a name and version control so we dont merge files like that again."

**How to apply:**
- Before creating any new folder during a reorg, run `ls -la` on the parent to check for case-insensitive collisions with reserved Windows folders: `Documents`, `Downloads`, `Desktop`, `Pictures`, `Music`, `Videos`, `Contacts`, `Favorites`, `Links`, `Saved Games`, `Searches`, `3D Objects`, `AppData`.
- Use distinctive, versioned names that cannot collide, e.g. `docs_reorg_2026_04_23\`, `josh_docs\`, `project_docs\` — not bare `documents\`.
- When moving into a folder that could exist, prefer an absolute fresh name or create a dated subfolder (`Documents\reorg_2026_04_23\`) so the move is auditable and reversible.
- After any bulk move, immediately `ls` the destination and compare file count to what was moved. If the count is higher than expected, investigate before continuing.
- Consider `git init` in the user's working tree (or at least a timestamped `.bak` manifest of file locations) before large reorgs so moves are reversible.
