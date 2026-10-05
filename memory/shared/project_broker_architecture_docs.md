---
name: project_broker_architecture_docs
description: Brokers architecture docs split into main Broker_architecture.md + per-broker docs/architecture/ files
metadata: 
  node_type: memory
  type: project
  originSessionId: 25a8425d-6a76-4411-a108-b996aae65e52
---

The Brokers repo architecture docs are split as: main `Broker_architecture.md` at repo root
(renamed from `ARCHITECTURE.md` 2026-06-17) holding platform-wide design + a "Per-broker
architecture documents" index, and one detail doc per broker under
`docs/architecture/<Broker>_architecture.md` for Schwab, IBKR, IronBeam, TastyTrade, MooMoo.
The main doc's section 6.x broker blocks are now overview + link only.

Legacy standalone docs (InteractiveBrokers/.../Architecture_for_IBKR.md, IronBeam/ARCHITECTURE.md,
IronBeam/.../Architecture_for_IronBeam.md, docs/TASTYTRADE_API_ARCHITECTURE.md) kept their content
but got a canonical-pointer banner at top (so their maintaining Agent_09 docs agents do not
regenerate empty files).

Functional code that reads the main doc was repointed from ARCHITECTURE.md to Broker_architecture.md:
`agents/agent_architecture_doc.py`, `broker_platform/core/healer_prompts.py` (also now loads the
per-broker doc per broker via `_BROKER_ARCH_DOC`), `tests/conftest.py`, `scripts/docs/gen_todo_log.py`.

Bug registry lives at `docs/KNOWN_BUGS.md`: BUG-001 (IronBeam start_collector.bat host-execution
isolation violation, FIXED) and BUG-002 (cmd unescaped-paren `(Phase 6)`/`(live)` parse bug, OPEN
in 7 pre-existing launchers run_daily/weekly_snapshot, run_monthly_*, run_events_collect, run_monthly_reconcile).

Gotcha: `sed s/ARCHITECTURE.md/.../` over-matches the tail of `TASTYTRADE_API_ARCHITECTURE.md`, guard against it.
Roadmap: CodeMapping_Brain/content/roadmaps/2026-06-17_000115_broker-architecture-doc-split.md.
Related: [[project_broker_bat_launchers]] [[project_schwab_run_tracker]].
