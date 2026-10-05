---
name: project-payissue-roadmap
description: Completed roadmap for the PayIssue 14-essay distinctiveness + visuals + depth iteration (v3 done 2026-05-22_225617)
metadata: 
  node_type: memory
  type: project
  originSessionId: b7addf98-e9ee-4d55-8ce6-8ceb787aca47
---

PayIssue repo at `~/repos/PayIssue/` holds a personal essay project arguing pay range transparency, internal posting, title vs pay alignment, percentage-of-base bonus mechanics, and locality pay disclosure (NJ vs TX). v1 has 14 essays in 14 styles but only one voice.

Active roadmap: `~/repos/CodeMapping_Brain/content/roadmaps/2026-05-22_223952_payissue-essays-iteration.md`.

**Why:** Iterated through three passes: v1 single-author (~14k words, one voice), v2 parallel writer agents with persona briefs + tables + 3 matplotlib charts (~14k words, 14 voices), v3 depth pass with the word cap removed (45,307 words total, each agent expanded its own draft in place). Completed 2026-05-22_225617.

**Status:** done. v1 lives in `Essays/`, v2 and v3 share `Essays_v2/` (only the timestamps in filenames differ). Drafts are markdown in `Essays_v2/drafts/`. Renderer is `generate_essays_v2.py`. Chart PNGs in `Essays_v2/figures/`. Full architecture documented in `ARCHITECTURE.md` at the repo root.

**How to apply:** If a future chat wants further iteration, read `~/repos/PayIssue/ARCHITECTURE.md` first (it documents the agents, personas, content-ownership map, visuals layer, and how to extend). The renderer is reusable: write a new markdown draft to `Essays_v2/drafts/`, register it in `ESSAYS` in `generate_essays_v2.py`, and run. The shared writer brief at `~/repos/PayIssue/agents/v2_shared_brief.md` holds the content-ownership map that prevented overlap.

Related: [[feedback-roadmap-default]], [[feedback-no-dashes]], [[feedback-file-timestamps]].
