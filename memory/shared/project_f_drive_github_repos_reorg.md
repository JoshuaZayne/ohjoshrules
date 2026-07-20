---
name: project_f_drive_github_repos_reorg
description: "On the desktop, F: git repos were consolidated into F:\\GitHub Repos\\ (2026-07-20), which can break hardcoded F:\\<repo> paths"
metadata: 
  node_type: memory
  type: project
  originSessionId: 588efd0d-54a5-4bef-9cba-a0656b7a30f5
---

On 2026-07-20 the desktop's F: drive was reorganized: all 34 top-level git repos
(clones of github.com/JoshuaZayne) were moved into **F:\GitHub Repos\<repo>**.

Exceptions / notes:
- **ohjoshrules** was deliberately left at **F:\ohjoshrules** (memory-sync repo — see [[reference_ohjoshrules_memory_sync]]).
- Loose F:\ root files were sorted into F:\{PDFs,Documents,Spreadsheets,Code,Images,Archives,Misc}. Old `F:\PDF's` was merged into `F:\PDFs`.
- Full move log: **F:\_reorg_log_2026-07-20.csv** (every move is reversible; temp files went to Recycle Bin).
- `iCloudDrive`, `iCloudDriveCache`, `.claude` were left untouched.

**Gotcha:** this only happened on the DESKTOP. Scripts with hardcoded `F:\<repo>` paths
break because the repo now lives at `F:\GitHub Repos\<repo>`. Fix pattern (matches
[[feedback_cross_device_paths]]): add `os.path.dirname(os.path.abspath(__file__))`
(a `_SCRIPT_DIR` self-locating entry) as the FIRST candidate in `device_paths.py`
path lists. Already applied to **Brokers** (PROJECT_ROOT + LOG_DIR). Not yet applied
to InterActiveBrokers-Project or YoutubeVideoUpload (they weren't broken).

**Duplicate:** `TalkToSpeech` and `VoiceToSpeech` are the same repo (VoiceToSpeech.git),
same commit, identical code apart from CRLF line endings. Both kept per user choice.
