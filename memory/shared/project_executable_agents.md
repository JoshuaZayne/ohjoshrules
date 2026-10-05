---
name: project-executable-agents
description: Self-executing agent MD files in CodeMapping_Brain — markdown that runs its own code block and rewrites its results section
metadata: 
  node_type: memory
  type: project
  originSessionId: 4b2a06eb-7b46-4ba1-b02d-10a82a886a05
---

CodeMapping_Brain has a tier of **executable agent** markdown files under `~/repos/CodeMapping_Brain/content/agents/`. Each carries a fenced ` ```python agent ` probe block plus `AGENT:RESULTS:START/END` markers. The runner `scripts/run_agents.py` extracts the probe, runs it in a subprocess (cwd = repo root, so it can read `data/*.json` and `content/`), parses the probe's last JSON stdout line (contract: `{status, summary, metrics{name:number}, details[]}`), and splices a PASS/WARN/FAIL badge + metric table with Δ-prev deltas + stdout tail into the same file. Per-agent history lives in `data/agent_runs.json`.

Detection requires `agent: executable` in frontmatter (deliberately NOT a loose "has a python block" fallback — the `executable-agents.md` overview describes the contract in prose and must not self-execute).

The 5 agents: orphan-finder (dangling `[[wikilinks]]` + orphan nodes), test-gap-reporter (`data/test_gaps.json`), dep-drift-watcher (`data/dep_drift.json`), broker-isolation-checker (broker repos in `discovered.json` missing a Dockerfile — static read only, never executes broker SDK, so [[memory-broker-isolation]] holds), node-census (node counts per tier).

Wired as the `agents` phase of `run_all.py` (after `memory`, before `tailor`). Run standalone: `python scripts/run_agents.py [--list|--only <name>|--strict]`. Add a new one by dropping `agent-*.md` with the frontmatter flag + probe + markers.

Roadmap: `content/roadmaps/2026-05-31_003128_executable-agent-md-files.md`. Overview node: `content/agents/executable-agents.md`. Related: [[project-codemap-graph-redesign]], [[memory-run-log]], [[feedback-roadmap-default]].
