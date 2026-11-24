---
name: project-rusttos-chart-redesign
description: "RustTOS chart redesign to every Quantower and ATAS function (owner 2026-11-24): plan, base branch agent/chart-redesign, waves of build agents"
metadata:
  node_type: memory
  type: project
  originSessionId: 91289bf2-7e78-473d-a1f7-297fdb2dcefb
  modified: 2026-11-24T09:23:53.844Z
---

The owner asked on 2026-11-24 for the RustTOS chart to be redesigned with ALL functions shown in `C:\Users\ohjos\Documents\RUST FUNCTION Add ons.docx` (54 photos of Quantower and ATAS, a Quantower "First Start" video, and a BikoTrading ATAS tutorial whose DOM chapter is 18:03 to 21:18, his "1850" note), plus the channels' other videos. He wants a much better launcher look and feel that helps window resizing, and said to start building as soon as the plan is done (no separate approval step).

**Why:** he wants RustTOS to match the order flow platforms (footprint, CVD, big trades, DOM on chart, DOM trader, heatmap, profiles, VWAP bands, chart trading, workspaces).

**How to apply:**
1. Plan (per photo table, sections S1 to S21, four waves): `F:\GitHub Repos\CodeMapping_Brain\content\roadmaps\2026-11-24_021800_rusttos-chart-redesign-quantower-atas.md`.
2. Base branch `agent/chart-redesign` (complaints-recheck plus depth-tools, merge 9eafd11d, worktree `F:\GitHub Repos\RustTOS_agents\chart-redesign`). Wave branches start from it: wave 1 is agent/redesign-shell (S1), agent/redesign-settings (S5), agent/redesign-bars (S4), agent/redesign-orderflow (engine). The coordinator merges waves into agent/chart-redesign, not main.
3. Held for the owner: copy trading, any new path that sends a real order, buying data. Clean room: same functions, never copy their code or artwork.
4. Review material (frames, transcripts) was in the session scratchpad and may be gone; the plan file keeps the findings.

Related: [[project_rusttos]], [[reference-rusttos-desktop-commands-folder]], [[feedback-builder-parallelism-and-resources]].
