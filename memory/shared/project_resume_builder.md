---
name: project_resume_builder
description: "The resumes repo — two working copies (iCloud is live, GitHub Repos is stale), and the new YAML-driven resume_builder that supersedes the monolithic generator"
metadata: 
  node_type: memory
  type: project
  originSessionId: 14d8c2e4-2676-420c-84f6-9a0d482f370a
  modified: 2026-10-23T21:58:53.824Z
---

The resume repo is `github.com/JoshuaZayne/resumes` (PRIVATE). It lives at
**`F:\GitHub Repos\resumes`** and is fully pushed.

**Moved out of iCloud on 2026-08-14.** It used to live at
`F:\iCloudDrive\IL_work\Python_code\Personal\Resume`; that path no longer
exists. iCloud was syncing `.git` and resolving conflicts by duplicating files,
which corrupted refs (a stray `refs/remotes/origin/main 2` broke `git fetch`
outright), deleted `README.md` / `_docs/ARCHITECTURE.md` / `_docs/TODO.md` /
`_src/resume_generator.py` by renaming them to numbered copies, and left 50+
duplicate `resume_generator N.py` scripts in `_src`. Never put a git repo back
under iCloud. See [[project_f_drive_github_repos_reorg]].

Generated `.docx` and `.pdf` outputs ARE tracked deliberately (~270 files, the
repo is ~10 MB); the `.gitignore` exclusion for them was removed on request.

## resume_builder (added 2026-08-14)

New data-driven system at `_src/resume_builder/`, documented in
`_docs/RESUME_BUILDER.md`. Content is YAML under `content/`, layout is code.
Run from `_src`: `python -m resume_builder.cli build futu_director_tsfcc`
(or `cover futu_director_cover` for the cover letter; `list` shows all).

**He edits the generated .docx directly in Word.** ALWAYS read the saved Word
file and sync its changes into the YAML before rebuilding, or his edits are
silently overwritten. This has already happened once.
Prints page count and warns when over target. Trim with `enabled: false` on any
section or bullet rather than deleting wording.

It supersedes, but does not delete, `_src/resume_generator 52.py` (a 1,700-line
`create_resume()` with an if/elif branch per job category) and the 51 other
numbered copies in `_src` (iCloud conflict sprawl). Those still hold unmigrated
content for ~34 other target roles.

`_src/build_futu_clearing 3.py` must NOT be run again: it was a one-shot
python-docx patcher that hardcoded a source path to a specific February 2026
MooMoo docx, and it produced the April 2026 FUTU resume outside the generator,
which is why that version was unreproducible.

## resume_engine (built 2026-10-23, branch jd-resume-engine)

`_src/resume_engine/` tailors a resume to a job description: 8 steps, 268
checks (30+ per step, enforced by a test), 4 decision modes, grounded LLM
summary (any number/name/credential not on the resume rejects it). Run from
`_src`: `python -m resume_engine.cli preview|tailor --job-file ../job.txt`.
Output goes to `output/engine_runs/<ts>_<job>/`; it never edits base YAML.
Data in `content/engine/*.yaml`. Tests: `python -m pytest tests/resume_engine -q`
(86 passed). Guide `_docs/RESUME_ENGINE.md`, agent rules `AGENTS.md`.
It replaced a Qwen Code prototype whose memory falsely claimed 30/30 steps
done. The two variants disagree on years (8+ clearing_vp, 9+ director); do
not reconcile without asking. Roadmap:
CodeMapping_Brain/content/roadmaps/2026-10-23_141217_resumes-job-description-engine-rebuild.md.
See [[project_local_llm_coding_setup]] for the gemma4 runaway gotcha.

Decision tree improvements (2026-10-23, branch decision-tree-improvements):
benchmark = the 10 `*/JOB_DESCRIPTION.md` files (label = their folder), run
`python -m resume_engine.cli evaluate --no-llm`. Before: right resume first
2/10. After: top1 100%, leave-one-out 90% (keyword and gemma4). Top1 is partly
recognition (each resume was written for its posting); leave-one-out
(intended-role match with the own resume removed) is the honest metric.
Base selection now reads every category folder's newest .docx (34 + InsightGlobal
+ MooMoo). GOTCHA: all legacy resumes were regenerated 2026-08-14 with the Futu
surveillance role on top, so their full text all reads "surveillance"; the
archetype profile uses only lines shared by fewer than half the resumes. `tune`
best weights did not beat current weights on leave-one-job-out, so not applied.
`feedback --audit ... --base ...` grows content/engine/labels.yaml. 283 checks, 108 tests.

## Employment context

He is VP of Trade Surveillance at **Futu Clearing Inc.** (Moomoo's US clearing
entity) since Mar 2026, Dallas TX / Jersey City NJ. Prior: Dimaskus Capital
Management (family office) 2015-2026. Uses **Eventus Validus** for post-trade
surveillance parameter configuration. Has AML/financial crimes experience too
(BSA, USA PATRIOT Act, FinCEN, OFAC, CDD/EDD, SAR governance).

Targeting the **Director, Trade Surveillance & Financial Crimes Compliance** role
at Futu US. Note the entity subtlety: that JD scopes the *retail* broker-dealer
(Moomoo Financial Inc.), while his title sits at Futu Clearing Inc.

## Gotchas

- YAML folded scalars (`>`) leave a trailing newline, which makes Word stretch the
  last line of justified paragraphs edge to edge. `schema.clean_text()` fixes it;
  any new text field must go through it.
- PDF export must use COM `DispatchEx`, not `Dispatch`. Word is a single-instance
  COM server, so `Dispatch` attaches to the user's open Word and the automation's
  `Quit()` would close their session and unsaved work.
- `doc.SaveAs2` can raise a bare `AttributeError: Open.SaveAs2` from stale pywin32
  late-binding type info; fall back to `ExportAsFixedFormat` then `SaveAs`.
