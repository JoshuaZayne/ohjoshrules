---
name: project_resume_builder
description: "The resumes repo — two working copies (iCloud is live, GitHub Repos is stale), and the new YAML-driven resume_builder that supersedes the monolithic generator"
metadata: 
  node_type: memory
  type: project
  originSessionId: 14d8c2e4-2676-420c-84f6-9a0d482f370a
  modified: 2026-08-14T07:46:53.722Z
---

The resume repo is `github.com/JoshuaZayne/resumes`, and it exists as TWO working
copies on the desktop:

- **`F:\iCloudDrive\IL_work\Python_code\Personal\Resume\`** is the LIVE one. 34
  company/role folders, `main` is ~15 commits ahead of origin with most role
  folders untracked. Work here.
- **`F:\GitHub Repos\resumes\`** is a stale thinner snapshot from the 2026-07-20
  F: drive reorg (see [[project_f_drive_github_repos_reorg]]). Only 6 company
  folders. Do not edit; it will confuse you into thinking content is missing.

## resume_builder (added 2026-08-14)

New data-driven system at `_src/resume_builder/`, documented in
`_docs/RESUME_BUILDER.md`. Content is YAML under `content/`, layout is code.
Run from `_src`: `python -m resume_builder.cli build futu_clearing_vp`.
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
