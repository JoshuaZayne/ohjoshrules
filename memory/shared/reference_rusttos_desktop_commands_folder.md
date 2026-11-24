---
name: reference-rusttos-desktop-commands-folder
description: "Desktop\\RustTOS commands has four sections (CLI, HTML pages, Level 2 depth and heatmap, Charts), each with a 00 STEPS file; the RustTOS HTML pages moved INTO it on 2026-11-24"
metadata:
  node_type: memory
  type: reference
  originSessionId: 91289bf2-7e78-473d-a1f7-297fdb2dcefb
  modified: 2026-11-24T07:31:26.265Z
---

Layout set up at the owner's request on 2026-11-24 ("sections for the html files ... the heatmap code on order depth ... folders that have steps ... folder with cli commands"):

1. `C:\Users\ohjos\Desktop\RustTOS commands\00 READ ME - what is in each folder.txt`
2. `1 CLI commands\`: launchers 01 to 12, `00 STEPS - read me first.txt`, and `Commands to copy and paste.txt` (the exact command behind every launcher in all four sections).
3. `2 HTML pages\`: launchers 20 to 26 plus the pages themselves, `RustTOS_Commands_2026-11-18_165903.html` and `RustTOS_Touch_Lab_2026-11-20_031741.html` (MOVED here from the Desktop). Launchers 21, 24 and 25 look in their own folder first, then the old Desktop path.
4. `3 Level 2 depth and heatmap\`: 40 heatmap window (`rusttos-depth`), 41 ladder (`rusttos-levels book`), 42 signals once with `--no-send`. Programs from branch agent/depth-tools, release builds in `C:\Users\ohjos\RustTOS_target_depth\release`.
5. `4 Charts\`: 30 live, 31 paper.
6. `Desktop\Other launchers\`: Schwab Login and Run RAM Scraper (the scraper bat still points at the old `C:\Users\ohjos\repos\` path and does not work).

**How to apply:**
1. When adding a RustTOS launcher, put it in the matching section with the next free number and add a step to that section's `00 STEPS` file and a line to `Commands to copy and paste.txt`. Never put a launcher that sends, cancels or moves an order here.
2. The page scripts in `F:\GitHub Repos\RustTOS\data\status_page\page_tools_2026-11-23\*.py` still name `C:\Users\ohjos\Desktop\RustTOS_Commands_2026-11-18_165903.html`. Before editing the Commands page with them, point them at `2 HTML pages\`, or they will not find it (or will write a second copy on the Desktop).
3. Move logs: `C:\Users\ohjos\Machine\rusttos_commands_move_log_2026-11-24_002542.csv` and `desktop_bats_move_log_2026-11-24_002236.csv`.

Related: [[project_rusttos]], [[feedback_status_page_after_merges]].
