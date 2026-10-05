---
name: project_kevin_history_help
description: "KevinHistoryHelp repo for Kevin Peccorini's HIST100 discussion post homework help"
metadata: 
  node_type: memory
  type: project
  originSessionId: ac53623f-934b-44c6-85f9-fad07c3239b9
  modified: 2026-07-28T14:13:39.001Z
---

New repo `~/repos/KevinHistoryHelp` (2026-07-28) helps draft answers to Kevin Peccorini's (`kevin.peccorini@yahoo.com`) HIST100 discussion assignments (Professor Reeves, textbook *Ways of the World* by Strayer & Nelson 5th ed.). Kevin emails questions + a `Discussion Template.docx` showing the expected format (Name/Date/Course/Professor header, ~200-word body, Reference line); he runs drafts through Gemini and rewords them himself before submitting.

**Why:** Kevin is a friend who forwards his class discussion questions asking for help; he can't email the 193MB textbook PDF, so chapter-question answers use general historical knowledge with page-number citations left as placeholders for him to fill in from his own copy.

**How to apply:** Reused/adapted code rather than building fresh: yt-dlp caption-pull pattern from `Spring2026/MGT_6540_Ethics/MediaGallery/download_youtube_captions.py`, and `srt_to_plain_text` logic adapted from `CanvasVideoScrapper/canvas_transcript.py`. Deliberately skipped `Spring2026/essay_engine` (wrong shape: full MLA/APA paper format + mandatory-Docker runner, not a fit for a single discussion-post). Each new assignment gets its own `assignment_YYYY-MM-DD/` folder with prompt.md, TODO.md (how-to-answer breakdown), draft_answers.md, and a generated docx via `scripts/build_docx.py`. Roadmap: [[reference_run_log]] pattern, full roadmap at `CodeMapping_Brain/content/roadmaps/2026-07-28_140000_kevin-history-discussion-help.md`.
