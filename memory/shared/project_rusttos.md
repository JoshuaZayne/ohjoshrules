---
name: project_rusttos
description: "RustTOS repo (F:\\GitHub Repos\\RustTOS, private JoshuaZayne/RustTOS): standalone all-Rust thinkorswim-style platform with wgpu GPU charting; phase 0 done 2026-11-01 (commit 042e984); rules enforced by cargo test"
metadata:
  node_type: memory
  type: project
  originSessionId: dfe8eb70-bebc-45d2-b981-4703bed5ae51
  modified: 2026-11-01T23:44:20.322Z
---

RustTOS: standalone Rust app meant to do what thinkorswim does, plus GPU native charting (wgpu, since the desktop GPU is an AMD RX 7900 XTX, so no CUDA), a stronger indicator engine, and live broker API data. Started 2026-11-01. Roadmap: `RustTOS/docs/ROADMAP.md` is the ONLY roadmap. The CodeMapping_Brain roadmap file is just a pointer; never copy steps back into it, and commit Roadmap References name `docs/ROADMAP.md`. Phase 0 done (commit 042e984, pushed). Next up is phase 1: feature catalog, and decoding the `@v10@` chart CONFIGURATION payload by comparing read-only copies of the ~30 workspace XML files TOS has already saved. Never ask the user to change or save anything in TOS.

Rules the user set for this repo, all enforced by `cargo test` through `crates/repo-tools`:
1. Everything is coded in Rust. An allow list refuses .py/.ps1/.js/.wgsl etc.; shaders go in .rs string constants. The only exception is the `.githooks/commit-msg` shim.
2. "Log track everything": `rusttos_core::logging::start_logging` writes timestamped files to logs/; there is a worklog entry per session in `docs/worklog/`, a decision log in `docs/DECISIONS.md`, and commits must pass the six-section hook (`git config core.hooksPath .githooks` on a fresh clone).

3. Everything runs locally, with NO Docker, broker feeds included. The user decided this on 2026-11-01 16:41 MST ("make this repo not use docker only installing shit for intial setup, once setup for this repo, make it so everything is local"); see decision D0007. Installing is for initial setup only, then `cargo run -p repo-tools -- setup`. The Rust-only test also refuses Dockerfiles and compose YAML.

4. The repo is independent (user, 2026-11-01 17:07 MST: "make this repo independent from anything else"; decision D0008). It must not name other repos, CodeMapping_Brain, personal folders or memory paths, and no code may read from or import outside it; `crates/repo-tools/src/independence.rs` fails `cargo test` on any outside reference. The global rules that apply are written into its own CLAUDE.md. Because of this, the reuse-before-writing rule means reuse inside RustTOS, never import from other repos.
5. TOS safety: the user worries their Schwab account could be blocked or blacklisted. CLAUDE.md rule 7: TOS is read-only (copy files to a temp folder and read the copy, never write to the TOS folder), with no automation of, injection into, or attaching to TOS, and no capturing its traffic or calling its servers. Live data comes only from official broker APIs.

**Why:** the user explicitly asked for an all-Rust repo with everything tracked, and later for everything to run locally. Their goal is a TOS-like app that accepts ANY data feed or indicator and charts it better than TOS does.

**How to apply:** cargo lives at `C:\Users\ohjos\.cargo\bin`, which is not on the default PATH of the Bash/PowerShell tools, so prepend it. TOS is studied clean room only (decision D0001): never decompile the jars in `C:\Program Files\thinkorswim\usergui\<build>`. Schwab has no official Rust SDK. The lead crate is `schwab-sdk` (jonathan-g-davis), with `rustyschwab` as runner up; the pick is deferred to phase 2.
