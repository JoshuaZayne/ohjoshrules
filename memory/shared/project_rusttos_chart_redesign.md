---
name: project-rusttos-chart-redesign
description: "RustTOS chart redesign to every Quantower and ATAS function (owner 2026-11-24): plan, base branch agent/chart-redesign, waves of build agents"
metadata:
  node_type: memory
  type: project
  originSessionId: 91289bf2-7e78-473d-a1f7-297fdb2dcefb
  modified: 2026-11-24T22:35:04.145Z
---

The owner asked on 2026-11-24 for the RustTOS chart to be redesigned with ALL functions shown in `C:\Users\ohjos\Documents\RUST FUNCTION Add ons.docx` (54 photos of Quantower and ATAS, a Quantower "First Start" video, and a BikoTrading ATAS tutorial whose DOM chapter is 18:03 to 21:18, his "1850" note), plus the channels' other videos. He wants a much better launcher look and feel that helps window resizing, and said to start building as soon as the plan is done (no separate approval step).

**Why:** he wants RustTOS to match the order flow platforms (footprint, CVD, big trades, DOM on chart, DOM trader, heatmap, profiles, VWAP bands, chart trading, workspaces).

**How to apply:**
1. Plan (per photo table, sections S1 to S21, four waves): `F:\GitHub Repos\CodeMapping_Brain\content\roadmaps\2026-11-24_021800_rusttos-chart-redesign-quantower-atas.md`.
2. Base branch `agent/chart-redesign` (complaints-recheck plus depth-tools, merge 9eafd11d, worktree `F:\GitHub Repos\RustTOS_agents\chart-redesign`). Wave branches start from it: wave 1 is agent/redesign-shell (S1), agent/redesign-settings (S5), agent/redesign-bars (S4), agent/redesign-orderflow (engine). The coordinator merges waves into agent/chart-redesign, not main.
3. Held for the owner: copy trading, any new path that sends a real order, buying data. Clean room: same functions, never copy their code or artwork.
4. Review material (frames, transcripts) was in the session scratchpad and may be gone; the plan file keeps the findings.
5a. State 2026-11-24 15:35 MST: agent/chart-redesign at 8fe99a08 holds S1, S3, S4, S5, S6, S7-S9, S10, S12, S13, S14, S15, S17, S21, S23, S24, S25, S26, S28, S30 (chart and alerts suites pass, 0 failed). Pending merges: redesign-controls (S18/S19, size keys being wired: owner said "sure wire them"), redesign-journal (S27, fixing replay ledger CSV quoting first), redesign-connections (S2), redesign-cleanup (data folder joins over ceiling 931 vs 921, plus Logs window), redesign-leftovers (S4/S5 leftovers). Held for owner: S11 DOM trader, S16 chart trading, S22 risk, S29 symbols mapping, S31 options (owner ranks). Follow up: tape filter and tracker alerts are not named rows in the alerts manager.
5. State 2026-11-24 09:10 MST: agent/chart-redesign at 5d8d627b, S1 complete (redesign-shell2 merged; every link channel incl. account is off by default, owner to confirm the account channel). Building: redesign-drawing (S14), redesign-profiles (S13), redesign-library (S6/S21), redesign-tape (S17/S24/S28, D0570-D0579, section 39). Earlier at dda00cd6 it held the order flow engine, S1 first part, S5 settings and themes, S4 bar types, S7/S8/S9 order flow drawing (redesigned footprint OFF by default, D0511, until the owner sees it), S10/S12 depth on chart and heatmap. Whole chart crate PASSES (45,584 of 45,592, 0 failed). A sharded-test shard can exit 1 with no failed test while agents load the machine; a rerun passed. Also building: redesign-library (S6/S21, D0560-D0569). Agents can pass every test while the app fails a plain `cargo check --workspace` (a #[cfg(test)] fn called from real code): always run both before a merge commit. Still building: redesign-profiles (S13, D0550-D0559), redesign-shell2 (S1 rest, decisions D0520-D0529), redesign-depth (S10/S12, D0530-D0539, also fixes that test), redesign-drawing (S14, D0540-D0549). Give each new agent its own decision number block; parallel agents clashed on D0492 and later every merge needed renumbering.
7. 2026-11-24 09:35 MST a merge test build died with os error 1455 ("paging file is too small"): commit limit was 128 GB RAM plus a fixed 16 GB page file, and five parallel Rust links hit it. Owner OK'd up to 800 GB of page file; `Desktop\Other launchers\Enlarge page file to 800 GB.bat` (self elevating, sets C:\pagefile.sys 128 GB start, 800 GB max, logs to Machine\page_file_change_*.txt) was written for the owner to double click; full effect after a restart, which must wait until build agents finish. Until then, rerun a build that fails with 1455. Root cause found 10:05 MST: `repo-tools sharded-test` builds with EVERY core (its --budget is test threads only), so always set CARGO_BUILD_JOBS=6 and prebuild with `cargo test --no-run -j 6` first; a rustc crash then "crate required to be available in rlib format" is the same memory problem.
6. Owner to check: the futures RTH table (decision D0509 on the merged branch; ES ends 15:00 Chicago at settlement, not 15:15).

Related: [[project_rusttos]], [[reference-rusttos-desktop-commands-folder]], [[feedback-builder-parallelism-and-resources]].
