---
name: project_rusttos_ninjatrader
description: "branch agent/ninjatrader: OIF files, read only C# bridge as a Rust constant, Trade API; practice only; not yet run live"
metadata:
  node_type: memory
  type: project
  originSessionId: e716c090-6953-47c5-a5b3-26ff91284361
  modified: 2026-11-08T23:22:12.613Z
---

**Summary moved from the memory index (2026-11-08):** RustTOS NinjaTrader lane (crate rusttos-ninjatrader, docs/ninjatrader, branch agent/ninjatrader in worktree RustTOS_agents/ninjatrader): desktop OIF files, read only C# bridge kept as a Rust constant, database reader, Trade API and market data; practice accounts only; nothing yet run against a real NinjaTrader or login (2026-11-08)

Built 2026-11-08 by session ohjos-4d on branch `agent/ninjatrader` from e664b86 (worktree `F:\GitHub Repos\RustTOS_agents\ninjatrader`), not pushed, not merged; the coordinator merges. Crate `crates/rusttos-ninjatrader`, docs `docs/ninjatrader` (README plus pages 01 to 09), worklog `docs/worklog/2026-11-08_151917_ninjatrader.md`. 113 tests, 593 checks. Programs: `rusttos-ninjatrader-check` (`--money`, `--contracts`, `--live-data`, `--install-bridge`, can't send) and `rusttos-ninjatrader-order` (rehearses unless `--send`).

**User's design decision:** "can we design it so it sends a c## command to ninja trader for certain calls? but everything else is in Rust? I want to manage my memerory usage in rust." So a small read only C# AddOn, `RustTosBridge`, answers on 127.0.0.1:36975 with a token. Its source is a Rust text constant in `desktop/bridge_source.rs` (shader precedent; no `.cs` in the repo), written to `Documents\NinjaTrader 8\bin\Custom\AddOns` only on `--install-bridge`, then F5 in the NinjaScript Editor. A test refuses any order word in that C#. Orders go through OIF files instead. Rust can't manage NinjaTrader's own .NET memory, only its own: say so plainly.

**Why no DLL:** the repo forbids `unsafe`. Port 36973's protocol is undocumented, so RustTOS only knocks on it.

**State at 2026-11-08 16:21 MST:** NinjaTrader 8.1.8.5 installed, never logged in here (empty `db`, `log`), not running. No Trade API credentials (`NINJATRADER_USERNAME`, `NINJATRADER_PASSWORD`, `NINJATRADER_CID`, `NINJATRADER_SEC` go in `.env`). So the user's real money has NOT been read. The shipped database (`Program Files\NinjaTrader 8\db\NinjaTrader.sqlite`: 215 futures among 1,618 products; last updated 2022-05-20, newest months 2024) is a stale catalog, and its 100,000 balances are practice defaults. Bridge compiled against the real DLLs but never installed or run. The docs don't state API cost or who qualifies; user needs to ask NinjaTrader for `cid` and `sec`.

**How to apply:** real orders are refused by code (Sim, Playback, DEMO only); going real needs the user's word plus shared ledger, lock and caps across brokers. Next: the first real run order on page 9. Use PowerShell, since Git Bash rewrites `/6EH27`; or `MSYS_NO_PATHCONV=1`. Older Python NinjaTrader code in the Brokers repo was tested as leads and found wrong on DLL path, port (36222, 36523 vs 36973), `Command` arguments and CANCEL field positions; nothing was taken from it. See [[project_rusttos]], [[feedback_verify_external_claims]].
