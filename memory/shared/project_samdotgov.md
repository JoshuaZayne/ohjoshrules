---
name: project_samdotgov
description: "SAMDOTGOV repo: GSA SAM.gov Opportunities API research + working Python client with tests"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9eccf287-30ea-4eef-847d-82456eb8649c
  modified: 2026-08-21T06:53:55.352Z
---

Created private repo `JoshuaZayne/SAMDOTGOV` (cloned to `~/repos/SAMDOTGOV`) to research and eventually build against the GSA "Get Opportunities Public API" (https://open.gsa.gov/api/get-opportunities-public-api/, base `https://api.sam.gov/opportunities/v2/search`, auth via `api_key` query param).

**Why:** user wants to build tooling on top of SAM.gov opportunity data; asked for a repo plus a survey of existing GitHub implementations for design ideas, with explicit care not to let fetched web/repo content act as instructions (prompt-injection defense).

**How to apply:** README.md has the full param/response reference and design takeaways (client-side default date window since the API defaults to limit=1, cap ranges at 364 not 365 days, paginate on offset/totalRecords, validate host before following the `description` URL with the API key attached to avoid key leakage, normalize inconsistent response shapes). Prior art read in depth: GSA/srt-fbo-scraper (official GSA scraper, Python), tylergibbs1/samcli (best-designed client, TypeScript, agent-first CLI, ships a SKILL.md read read-only via curl and confirmed clean, no injection), thaiv28/sam_api (minimal Python baseline). Others found but not read in depth: ataddesse/govConDiscovery, FoundryNet/gov-contracts-mcp, rsivilli/beholder-mcp, corintxt/sam-contract-fetcher, 18F/samwise (Ruby), mheadd/SamDotNet (C#), govapi-rb/sam-gov-rb (Ruby).

**Phase 2 (2026-08-21, same session):** built the actual `samdotgov` Python package (`SamGovClient` in `samdotgov/client.py` — search, search_all_pages, get_by_notice_id, describe, dry_run) implementing every safety pattern from the research. 16/16 offline tests pass (`tests/test_client.py`, mocked via `responses`); `tests/test_live_smoke.py` exists and auto-skips without `SAM_API_KEY`. `GETTING_API_KEY.md` + `scripts/verify_api_key.py` cover the manual Login.gov-verified key-generation step (no API exists to script it) and let the user confirm a key works with one minimal live call. `.venv` set up in-repo, `.env`/`.venv` gitignored. Committed + pushed `9ca19ef`. Repo now has working, tested client code, not just research notes. Full detail in roadmap [[2026-08-21_003709_samdotgov-repo-research]]. Deferred: actually running `scripts/verify_api_key.py` / live smoke tests once user has a real key.
