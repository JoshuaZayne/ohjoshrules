---
name: project_schwab_dashboard_trading
description: "Schwab dashboard on Brokers branch Dimaskus_Surface_merge (worktree F:\\GitHub Repos\\Brokers_merge, NOT pushed): TradingView-style futures terminal, trade panel, Accounts P/L charts, RAG assistant (Docker, qwen3.6), 111 browser tests; how to run tests, Schwab quote semantics, runtime gotchas, open user decisions"
metadata:
  node_type: memory
  type: project
  originSessionId: d8a60bec-334c-4db0-9f39-6d64b4103cad
  modified: 2026-10-11T23:11:11.491Z
---

Brokers branch `Dimaskus_Surface_merge`, worktree `F:\GitHub Repos\Brokers_merge` (trial merge of Surface into refactor/platform-restructure-2026-08). Many commits on 2026-10-11, last d96349cf (% change fix) and 519e28ae (Accounts tab); NOT pushed (user has not approved a push). Launch: `schwab_dashboard.bat` or `python scripts/dashboard/schwab_dashboard.py` (http://127.0.0.1:8765; `--no-trading`, `--no-assistant`).

Page (rebuilt 2026-10-11): Lightweight Charts 4.2.3 vendored, session-anchored timeframes and tick charts, watchlist sections, details with full data paths, tabs Data currency / Data health / Coverage / Contracts / Trade / Accounts / Jobs / Assistant. Agents: `#page-state` JSON, `/llms.txt`, `/api/describe` (scripts/dashboard/agent_api.py).

Assistant: Docker container `brokers-assistant:2026-10-11.2` (Schwab image + sqlite-vec 0.1.9, anthropic 1.8.0, mcp 1.30.0), started on first Assistant-tab open; hybrid FTS5 + sqlite-vec retrieval (qwen3-embedding:0.6b), qwen3.6 via Ollama default, Claude only if ANTHROPIC_API_KEY is set (env or .env.secrets; not set as of 2026-10-11). MCP server built but NOT registered: `python scripts/assistant/mcp_command.py` prints the `claude mcp add` line; register only with the user's OK.

**Why:** real-money order path (preview then confirm, send at most once, kill switch); least privilege for the assistant (no token/accounts/.env mounts).

**How to apply:**
1. Tests: unit suites in Docker image `brokers-assistant-test:2026-10-11.2` (pytest; restore Broker_architecture.md and docs/PROCESS_REGISTRY.md afterwards, the root conftest rewrites them). Browser suite on the host: `python -m pytest tests/ui` (Playwright 1.48.1 + installed Edge, ~2 min; synthetic data, fake Schwab, real assistant service with a scripted model).
2. Schwab quote semantics (read live 2026-10-11, pinned in tests/test_dashboard_quote_change.py): futurePercentChange and netPercentChange are PERCENTS, not fractions (page showed futures 100x until d96349cf; compute 100*netChange/closePrice instead). A future's closePrice = settlement of the session BEFORE the one its last trade is in (Sunday morning still Thursday's; rolls ~16:00 CT before the open). A stock's top-level netChange restarts at the 16:00 ET close (after-hours move only); the day's change is in the `regular` block. Transactions store holds only TRADE + DIVIDEND_OR_INTEREST (no transfers), so net liq jumps can be transfers.
3. Gotchas found 2026-10-11: Playwright 1.48.1 driver dies when a download starts in Edge 155 (check download links by requesting the href); `Browser.close()` can hang (use `pw.stop()`); Ollama embedder at default num_ctx 32768 (5.8 GB) evicts qwen3.6 (23 GB), keep num_ctx 2048; SQLite writes on the Windows bind mount are ~70x slower (index works on container disk); Flask jsonify sorts keys; Python default args like `bars_dir=BARS_DIR` bind at definition (broke test isolation once); Lightweight Charts with autoSize + a range set while the box is 0 px wide (new card, hidden tab) squeezes all points into the last pixels (accounts.js sizes charts by ResizeObserver instead); pull_all's date-only accounts_YYYY-MM-DD.json must be dated by name, not mtime (a checkout restamps it).
4. Do not route panel orders through `TraderAPI.place_order` or `SchwabClient.execute_order` (retry/fallback = duplicate-order risk).
5. Open user decisions: commit the ~272 job-output data files; repair GC/SI impossible-date rows; fix IronBeam contract_specs.py ticks (ZT, 6A, 6S, 6N); push the branch; register the MCP server; add ANTHROPIC_API_KEY for Claude.

Roadmaps: CodeMapping_Brain/content/roadmaps/2026-10-11_030617..., 033900..., 041000..., 062110... (committed bcd1b45). Related: [[project_brokers_schwab]], [[feedback_moomoo_isolation]], [[feedback_docker_startup]], [[project_local_llm_coding_setup]].
