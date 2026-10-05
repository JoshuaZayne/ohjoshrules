---
name: project-securityexam-tc-access-deadline
description: Training Consultants (SIE/Series7 courseware) access expires 2026-10-26 — hard deadline for any remaining live scrapes.
metadata: 
  node_type: memory
  type: project
  originSessionId: 6cd0fa16-e03e-4905-a791-4728577bc69a
  modified: 2026-08-19T05:46:05.684Z
---

User's Training Consultants courseware access (courses.trainingconsultants.com) expires **2026-10-26**. Confirmed 2026-08-18 that stored credentials in `~/repos/SecurityExamPrep/.env` still authenticate (`python -m scraper.login` succeeded, `.auth/state.json` refreshed).

**Why:** after 2026-10-26 the site becomes unreachable with these credentials, so anything not yet scraped/captured is permanently lost. The known gap: `scraper.flashcards_section` has never successfully pulled the official TC flashcard bank — it lands on a session-setup wizard (`/flashcards/default.aspx`) instead of the card view. Fix needed: click `#btnSrcAll`, then `__doPostBack('ctl00$ContentPlaceHolder1$btnGoSession','')`, then iterate the session UI. See [[project_securityexam_rebuild_roadmap]].

There is no public API for Training Consultants (classic ASP.NET WebForms, `__doPostBack`/viewstate only) — Playwright scraping is the only route in. FINRA's public exam-outline data is already ingested at `data/exam_outlines.json`.

**How to apply:** any SecurityExamPrep work between now and 2026-10-26 should treat "anything requiring a live TC session" (flashcards_section fix, re-capturing textbook pages, re-scraping courses/nav) as higher priority than downstream work (exporters, PWA UI, notebooks) that only needs already-captured JSON and can happen anytime, deadline or not.

**Update 2026-08-19**: `scraper.flashcards_section` fixed (real wizard click flow + card-viewer DOM, see `docs/TODO.md`). Full unattended harvest launched for both SIE (531 official cards) and Series 7 — check `logs/flashcards_full_run_*.out` for completion, expect several hours. Once done, re-run `scripts\build-exports.bat` to fold the new `<EXAM>_flashcards_official.json` into every export format. Active roadmap: [[project_securityexam_rebuild_roadmap]] successor at `~/repos/CodeMapping_Brain/content/roadmaps/2026-08-18_232434_security-exam-study-experience-upgrade.md`. New `docs/CLI_COMMANDS.md` is now the canonical detailed command reference. Still queued: MCQ/cloze quality pass, webapp UI/JS overhaul, freeform note-taking, PDF review.
