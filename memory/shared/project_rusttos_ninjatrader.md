---
name: project_rusttos_ninjatrader
description: "branch agent/ninjatrader: OIF files, read only C# bridge as a Rust constant, Trade API; practice only; bridge proven live, no order sent"
metadata:
  node_type: memory
  type: project
  originSessionId: e716c090-6953-47c5-a5b3-26ff91284361
  modified: 2026-11-14T05:19:47.912Z
---

**Summary moved from the memory index (2026-11-08):** RustTOS NinjaTrader lane (crate rusttos-ninjatrader, docs/ninjatrader, branch agent/ninjatrader in worktree RustTOS_agents/ninjatrader): desktop OIF files, read only C# bridge kept as a Rust constant, database reader, Trade API and market data; practice accounts only; bridge reads proven live 2026-11-08 21:33 MST, no order or Trade API login yet

Built 2026-11-08 by session ohjos-4d on branch `agent/ninjatrader` from e664b86 (worktree `F:\GitHub Repos\RustTOS_agents\ninjatrader`), not pushed, not merged; the coordinator merges. Crate `crates/rusttos-ninjatrader`, docs `docs/ninjatrader` (README plus pages 01 to 09), worklog `docs/worklog/2026-11-08_151917_ninjatrader.md`. 113 tests, 593 checks. Programs: `rusttos-ninjatrader-check` (`--money`, `--contracts`, `--live-data`, `--install-bridge`, can't send) and `rusttos-ninjatrader-order` (rehearses unless `--send`).

**User's design decision:** "can we design it so it sends a c## command to ninja trader for certain calls? but everything else is in Rust? I want to manage my memerory usage in rust." So a small read only C# AddOn, `RustTosBridge`, answers on 127.0.0.1:36975 with a token. Its source is a Rust text constant in `desktop/bridge_source.rs` (shader precedent; no `.cs` in the repo), written to `Documents\NinjaTrader 8\bin\Custom\AddOns` only on `--install-bridge`, then F5 in the NinjaScript Editor. A test refuses any order word in that C#. Orders go through OIF files instead. Rust can't manage NinjaTrader's own .NET memory, only its own: say so plainly.

**Why no DLL:** the repo forbids `unsafe`. Port 36973's protocol is undocumented, so RustTOS only knocks on it.

**State at 2026-11-08 21:35 MST:** bridge installed and proven live: user logged in, pressed F5, and `--money`, `--live-data`, `--positions`, `--orders`, `--quote` all answered on connection `Live` (provider `Provider31`, which doesn't name the feed). NinjaTrader must be running for the bridge to answer. Read live: one real account, shown masked, plus Sim101, Playback101 and Backtest; `buying_power` read 0 on every account, so it isn't trustworthy yet, and the balance hasn't been compared with the Accounts tab. Login refreshed `Documents\NinjaTrader 8\db\NinjaTrader.sqlite` (385 futures, months into 2028), though its `Versions` date still says 2022 and misleads. Still no Trade API credentials (`NINJATRADER_USERNAME`, `NINJATRADER_PASSWORD`, `NINJATRADER_CID`, `NINJATRADER_SEC` go in `.env`), so plans on sale are unknown. No order file has been sent. Docs don't state API cost or who qualifies; user needs to ask NinjaTrader for `cid` and `sec`.

**A test of ours stopped NinjaTrader, 2026-11-08 21:56 MST:** a live quote request for a sample, almost certainly `BTCEUR`, raised an Abort, Retry, Ignore dialog (`TradingHours==null`, in `Tradovate.Adapter.SubscribeBars`), and Abort closes the program. The cause is unknown: its template exists, and unsupported `SPY` caused nothing. Assertions go to `Documents\NinjaTrader 8\trace\`, not the `log` folder, so read the trace after any live request. `SafeProducts` (a required input), the bridge's `Refusal` and `TraceWatch` guard against a repeat.

**State at 2026-11-08 22:55 MST:** NinjaTrader closed since the abort. Waiting on the user to reopen it and press F5. Bridge version 2 is installed as a file and not compiled by NinjaTrader. Then run `rusttos-ninjatrader-series --market-data <main folder>\data` (98 kinds of check on 17 currency and metal front months), and report the flags. Active Trader has an `NT` route to Sim101 (`desktop/bracket_desk.rs`), on stand ins only; a by hand Sim order needs the user's yes, and NinjaTrader's Automated Trading Interface option on. `rusttos-chart` isn't rebuilt or installed. IBKR has no live CME currency subscription on this account (error 354).

**State at 2026-11-13 22:20 MST:** merged to main as e48b02d (2026-11-09); branch retired, tag `archive/agent/ninjatrader`; worktree files in main `data\worktree_archive\2026-11-10\ninjatrader`. Status and next steps written to `docs/ninjatrader/10_status_and_next_steps.md` on branch `agent/ninjatrader-docs` (5b9da45, docs only, not merged). Still never run live: bridge v2, series test, compare sweep, NT press. Installed chart (main 6b68160) has the NT button; the four NinjaTrader programs are not built in main's target. Live money drills pinned 5 Trade API and desk findings (5xx and `{}` as refusals, case sensitive host, partial fills lost).

**How to apply:** real orders are refused by code (Sim, Playback, DEMO only); going real needs the user's word plus shared ledger, lock and caps across brokers. Next: the first real run order on page 9. Use PowerShell, since Git Bash rewrites `/6EH27`; or `MSYS_NO_PATHCONV=1`. Older Python NinjaTrader code in the Brokers repo was tested as leads and found wrong on DLL path, port (36222, 36523 vs 36973), `Command` arguments and CANCEL field positions; nothing was taken from it. See [[project_rusttos]], [[feedback_verify_external_claims]].
