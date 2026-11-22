---
name: project_f_drive_dedupe_2026-11-22
description: "F: duplicate cleanup of 2026-11-22: the four reusable scripts in Machine\\dedupe_tools, the 38.79 GB reviewable plan, and what is still undecided"
metadata:
  node_type: memory
  type: project
  originSessionId: 2dc7a551-6dd9-4b58-8eb7-2b8ebee5c886
  modified: 2026-11-22T10:06:44.826Z
---

Duplicate hunt on `F:` started 2026-11-22, with the owner's rule that NOTHING is deleted without them naming it.

1. THE TOOLS, durable at `C:\Users\ohjos\Machine\dedupe_tools\` (they were written in a session scratchpad, which
   gets cleared, so they were copied out on purpose). Each takes folders as arguments and paths by environment
   variable, deletes nothing, and is documented in plain English at the top:
   1. `find_dupes.py` (REPORT_PATH): byte identical duplicates. Groups by exact size, then the hash of the first
      1 MB, then the whole file, so only real candidates are ever fully read. 395.94 GB in 8.1 minutes.
   2. `plan_dupes.py` (PLAN_PATH, DELETE_LIST_PATH): turns those into a keep/delete proposal with the deciding rule
      named per set, and a machine readable delete list. Rules: STAGING, COPY SUFFIX, NESTED SAME NAME, COPY NAME.
   3. `plan_to_html.py` (PLAN_PATH, HTML_PATH): one self contained offline HTML review page, tick boxes, live
      approved total, filter box, and a button that saves the approved delete list.
   4. `content_dupes.py` (REPORT_PATH, optional LIMIT_IMAGES / LIMIT_VIDEOS): SAME CONTENT, different bytes.
      Images get a pHash (32x32 grey, DCT, low 8x8 above median), a dHash as a second opinion because pHash
      collides on flat images, a 4x4 colour signature to stop bursts collapsing, and EXIF model plus capture time.
      Videos get duration, resolution, codec and a pHash of frames at 5, 25, 50, 75 and 95 percent of duration, so
      the comparison is independent of length and resolution. Every group is marked NEW or ALREADY KNOWN against a
      full byte hash, so the value over the byte scan is visible. Measured rate: 25 images and 1.92 videos a second.
2. FINDINGS. Byte identical: 42.26 GB in 1,075 sets. After excluding `Josh's Stuff`, whose high copy sets are
   installed program internals that MUST NOT be touched (one is 142 copies of the same Git for Windows binary under
   different names, others are VS Code shipping one bundle per extension folder), the reviewable plan proposes
   38.79 GB across 682 sets and leaves 2.33 GB across 290 sets for the owner to decide.
3. WHERE THE SPACE ACTUALLY IS: of 380.7 GB in Media_Archive_2019 plus PhotoLibrary plus PhoneImportStaging, videos
   are 365.59 GB in only 930 files, and ALL images together are 11.05 GB in 4,089 files. Perceptual image hashing
   can therefore only ever recover a sliver; video is the whole game. Those folders also hold 35,120 `.java` files
   (0.36 GB), apparently a JDK or source tree in the wrong place.
4. ZERO HEIC or HEIF files exist there. `pillow-heif` was installed before counting, which was a mistake: it was
   unnecessary and it upgraded Pillow from 10.0.1 to 11.3.0 as a side effect. Count file types BEFORE installing a
   decoder for them. Anaconda also carries pre-existing broken package stubs (`-rotobuf`, `-umpy`, `-ffi`).
5. A RULE TRAP worth remembering: a "looks like a copy" test must compare stems WITHIN a duplicate set. Treating any
   trailing `_<digits>` as a copy marker fails, because `IMG_4238.mov` itself ends that way, so both files look like
   copies and nothing is decided. Comparing within the set, and capping the suffix at two digits so `_2026` is not a
   copy, moved 14.36 GB out of the review pile and into decided.
6. OUTPUTS, all in `C:\Users\ohjos\Notes\`, timestamped: `F_duplicate_deletion_plan_*.txt`,
   `F_duplicate_delete_list_*.txt`, `F_duplicate_review_*.html` (the page to review) and
   `F_same_content_report_*.txt` plus its `.json`. One known cosmetic flaw: the plan's "Files compared" line counts
   files SEEN, not files of 1 MB or more actually compared, and its "Rule meanings" block omits COPY SUFFIX.
7. STILL UNDECIDED, nothing deleted: the owner has not yet approved any deletion from the 38.79 GB plan, and the
   290 review sets are unjudged.

Related: [[project_rusttos_state_2026-11-22]], [[reference_desktop_hardware_inventory]], [[feedback_no_data_deletion]],
[[project-e-drive-backup-slack]], [[feedback_file_timestamps]].
