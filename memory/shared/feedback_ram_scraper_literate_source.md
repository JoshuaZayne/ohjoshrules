---
name: feedback_ram_scraper_literate_source
description: "RamMegaCabDataScrapper's scraper/*.py files are literate-programming outputs generated from docs/src/*.md — editing the .py directly gets silently reverted the next time tangle.py runs"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9de44948-f071-4346-89d9-1953e149c42d
  modified: 2026-08-05T21:00:12.857Z
---

In `~/repos/RamMegaCabDataScrapper`, every file under `scraper/` (except
`scripts/trees/*.py`, which are explicitly plain dev scripts) carries a
`# >>> LITCODE BANNER (generated; edit the docs/src/*.md, run python
tangle.py) <<<` marker at the top. That banner means the file's SOURCE OF
TRUTH is `docs/src/<same path>.py.md`, not the `.py` itself — `python
tangle.py` regenerates every `scraper/*.py` from its `.md` counterpart.

**Why: on 2026-08-05, I (Claude) edited `scraper/config.py`,
`scraper/cli/analyze.py`, and `scraper/excel.py` directly (adding a Parquet
snapshot feature and an Excel tab-color/guide reorg) without touching their
`docs/src/*.md` sources.** Every test passed (pytest never runs
`tangle.py`), so the drift was invisible for hours. It only surfaced when
the user asked for a real Docker scrape: `run.ps1` runs `python tangle.py`
as a pre-build step, which silently regenerated those three `.py` files
FROM the stale `.md` content — reverting all three edits, both in the
freshly-built Docker image and in the local working tree on disk. The
feature appeared to work (all tests green, code looked committed) but
produced zero output in a real run, since the shipped code was never really
there. See [[project_ram_megacab_scraper]] for the fix (commit `76c932f`).

**How to apply:** before editing ANY file under `scraper/` (top-level
package, not `scripts/`) directly, check for the LITCODE BANNER marker line
first (`grep -q "LITCODE BANNER" <file>` or just look at the top of the
file). If present:
- Prefer editing `docs/src/<path>.py.md` instead of the `.py` directly, then
  run `python tangle.py` to regenerate.
- If editing the `.py` directly is faster mid-flow, immediately mirror the
  same change into the `.md` and run `python tangle.py --check` before
  considering the change done — don't wait until a real `run.ps1` invocation
  to discover drift.
- A NEW file under `scraper/` (no existing `.md`) needs its own literate
  source too, for consistency — but do NOT run
  `scripts/dev/litcode.py detangle` to create it; that tool regenerates
  EVERY `scraper/*.py`'s `.md` from a bare-bones template, which would
  destroy the hand-written prose already in every other module's `.md`.
  Instead, generate just the banner via
  `python -c "import sys; sys.path.insert(0,'scripts/dev'); from litcode
  import banner; print(banner('scraper/<name>.py'), end='')"` and hand-craft
  the rest of the `.md` (header + fenced block) to match the existing files'
  structure.
- `python tangle.py --check` is the authoritative verification — run it
  before considering ANY `scraper/` change finished, not just at commit
  time.
