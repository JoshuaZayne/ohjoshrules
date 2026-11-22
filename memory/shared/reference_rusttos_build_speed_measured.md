---
name: reference-rusttos-build-speed-measured
description: "RustTOS check speed, measured 2026-11-22: sccache gives 0 percent hits and nextest is 2.1x SLOWER on Windows; cargo test at -j 24 is the fast path"
metadata:
  node_type: memory
  type: reference
  originSessionId: 1357db99-9ad1-48ec-8f53-a505f7663727
  modified: 2026-11-22T21:05:00.969Z
---

Measured on DimaskusPC 2026-11-22 (32 logical processors, 127.88 GB RAM, cargo output on C:). Do NOT re-attempt the
two dead ends below without new evidence; each cost an hour.

## Two things that DO NOT work here, both measured

1. **sccache: 0 percent cache hit rate.** Three identical builds of `rusttos-core` into three fresh target folders,
   with `CARGO_INCREMENTAL=0`: 186 compilations, **0 cache hits**, 547 MiB written to the cache and never read.
   Non-cacheable reasons it reported: crate-type bin 26, proc-macro 10, missing input 4. It was installed, enabled,
   measured, and removed again; `RUSTC_WRAPPER` is unset. NOTE: an agent named `faster-rounds` already had
   "sccache" in its goal on 2026-11-11, so this is the SECOND time it has been tried.
2. **cargo-nextest: 2.1 times SLOWER.** Like for like, same scope (`--workspace --exclude rusttos-chart`), same
   `-j 24`, same 26,143 tests, both passing: `cargo test` 273 seconds, `cargo nextest run` 573 seconds. Nextest's
   test execution alone was 404 s, longer than cargo test's whole run. Cause: nextest runs every test in its own
   PROCESS, and 26,143 process creations on Windows cost far more than on Linux, where nextest normally wins. It
   was never installed system wide, only run from a scratch folder.

## What IS the fast path

1. `cargo test --workspace -j 24`. The old habit of `-j 8` dates from when this machine had far less memory.
2. `repo-tools sharded-test` ALREADY EXISTS and is better than plain cargo test for a full round: it shards across
   a 32 core budget, routes chart tests through the graphics card guard, runs failed tests again alone to catch
   flakes, and proves its shard plan before running. Sessions have been ignoring it and running plain `cargo test`.
3. Tiered gates, cheapest first: `cargo test -p repo-tools --test repository_rules` (about 7 seconds, catches the
   documentation, naming, independence and data folder joins rules) then the changed crates, then the workspace.
4. A fail fast full run is a cheap smoke test in its own right: on 2026-11-22 a fail fast run surfaced a red main
   in 52 seconds that two sessions had missed all afternoon.

## Rough sizes, for planning

1. Non chart workspace: 26,143 tests, 273 s at `-j 24`.
2. `rusttos-chart` holds roughly 45,000 more tests; the whole workspace was 71,501 tests in 929 s at `-j 8`.
3. The dependency graph is 584 packages, of which 572 are third party and identical in every agent worktree, and
   there are 121 test targets.

Related: [[feedback-builder-parallelism-and-resources]], [[project_rusttos]],
[[reference-desktop-hardware-inventory]].
