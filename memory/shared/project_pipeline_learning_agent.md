---
name: project-pipeline-learning-agent
description: "Active overlay roadmap that adds step instrumentation, PyTorch failure classifier, step-decomposer LLM agent, and diagnostic LLM agent over every broker pipeline. Goal is highest practical automation. Sits alongside the main brokers market-data pipeline roadmap."
metadata: 
  node_type: memory
  type: project
  originSessionId: ab66236a-9f95-4d9e-a400-58c56960bc39
---

Active subsystem under construction: a self-monitoring + self-healing overlay for every broker pipeline.

**Why:** Once Schwab + IBKR + events + scheduler pipelines all run on cadence, hand-watching them does not scale. User explicitly asked for PyTorch learning checks of what works and what doesn't, an agent to identify steps per process, and the highest practical automation.

**How to apply:** any work that touches pipeline instrumentation, telemetry, step decomposition, failure classification, automated retries, or diagnostic agents -> read this roadmap and the parent [[project-brokers-market-data-pipeline]] first. Do NOT spawn a parallel roadmap for the same scope.

**Roadmap:** `~/repos/CodeMapping_Brain/content/roadmaps/2026-05-23_000000_pipeline-learning-diagnostic-agent.md`

**Subsystem layers:**
- L1 step instrumentation library (`broker_platform/observability/`) + JSONL/parquet event store
- L2 step-decomposer LLM agent emitting `docs/runbooks/<pipeline>.md` + applying `@step` decorators
- L3 PyTorch failure classifier (per-pipeline or shared) + cold-start rule-based fallback
- L4 diagnostic LLM agent on failure with safe-action whitelist for auto-apply
- L5 dashboards, weekly summary, full retrofit

**Status (2026-05-23): L1+L2+L3+L4-safe-heal-slice SHIPPED.**
- L3 classifier built under `broker_platform/observability/classifier/` (features, rules cold-start, PyTorch HealthMLP, dataset+train gate at 200 samples, HealthClassifier auto rules<->MLP switch). 19 tests pass.
- L4 safe-heal: `heal.py` Healer, auto-apply whitelist = {reauth} only, confidence>=0.80, audit log to `data/telemetry/heals/`. Decision was "auto-heal a safe whitelist".
- Schwab re-auth instrumented: `scripts/schwab/refresh_cron.py` emits `schwab.token_refresh` step events; `scripts/schwab/health_check.py` is the read-only verdict CLI.
- ARCHITECTURE.md section 9.11 documents the whole thing + run commands.
- **ONE BLOCKER to full automation:** `install_refresh_task.ps1` needs an ELEVATED PowerShell (non-admin = Access Denied). User must run it once as admin to register the daily 03:00 re-auth task. Until then the 7-day token wall is NOT auto-handled on this machine.

**Resolved decisions (2026-05-23):** PyTorch confirmed for L3; auto-apply = tight whitelist (reauth) not propose-only; event store = JSONL (parquet rollup still deferred).

**Next (L5):** wire a watchdog/cron call-site that invokes `HealthClassifier.predict` + `Healer.handle` on a cadence; train MLP once >=200 real labelled runs accumulate; dashboard + weekly summary.

**Related:** [[project_brokers_market_data_pipeline]] (parent), [[feedback_moomoo_isolation]], [[feedback_roadmap_default]].
