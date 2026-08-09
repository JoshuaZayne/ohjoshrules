---
name: project_local_llm_coding_setup
description: "Local LLM coding setup on the desktop — hardware, LM Studio models + benchmarks, Antigravity, Gemini CLI removed"
metadata: 
  node_type: memory
  type: project
  originSessionId: c0a9b32a-21ae-4389-a4d6-78da8cd26041
  modified: 2026-08-09T19:45:55.627Z
---

Desktop rig used for running local coding LLMs (set up July 2026).

**Hardware:** AMD Ryzen Threadripper 1950X (16C/32T) · 80 GB RAM · Radeon RX 7900 XTX with **24 GB VRAM** (Win32_VideoController misreports it as 4 GB — read true VRAM from registry `HardwareInformation.qwMemorySize`).

**Runtime:** LM Studio (`lms` CLI at `~/.lmstudio/bin/lms.exe`). Selected engine = **llama.cpp Vulkan 2.24.0** (correct AMD backend; a ROCm 2.24.0 runtime is available-but-not-installed if we ever want to benchmark it). Server: `lms server start`, OpenAI-compatible at `http://localhost:1234`. `lms` has NO delete command — remove models by deleting their folder under `~/.lmstudio/models/<publisher>/`.

**Models downloaded + benchmarked** (same prime/linked-list smoke test, warm-up then 500-tok timed gen):
- **Qwen2.5-Coder-7B-Instruct** (Q4, 4.68 GB) — 40.7 tok/s, fully GPU. Fast daily driver / autocomplete. Catalog shortname didn't resolve; pulled via HF URL `lmstudio-community/Qwen2.5-Coder-7B-Instruct-GGUF`.
- **Gemma 4 31B** dense (Q4, 19.9 GB, arch `gemma4`) — 17.3 tok/s, fully GPU (18.5 GiB). Best quality/speed balance. This is the recommended everyday model.
- **Qwen3-Coder-Next** 80B MoE (48.5 GB, arch `qwen3next`) — only 4.7 tok/s: too big for 24 GB VRAM so experts spill to RAM. `qwen3next`/Gated-DeltaNet DOES load on runtime 2.24.0. Keep for huge-context/hard tasks only. Offload tuning may raise speed.

**Gotcha:** big downloads from some HF repos throttle to ~1.6 MB/s and time out; `lms get` has no auto-resume, so I wrap it in a retry loop (`scratchpad/dl_retry.sh`) — it resumes partial downloads across attempts.

**Ollama (added Aug 2026, alongside LM Studio):** Ollama 0.32.1 native Windows, running on **ROCm** (gfx1100), not Vulkan. Model: `qwen3.6:latest` (36B MoE, Q4_K_M, 23 GB, tools + thinking + vision, 256K ctx). Benchmarked at 64K context: 41 of 42 layers on GPU, 20.8 GB VRAM, only 877 MB spill, **14.9 tok/s**. KV cache is only 1.25 GB at 64K because the arch is hybrid (10 full-attention layers, 40 recurrent), so long context is cheap on this model. Models live at `F:\OllamaModels`.

**Big Ollama gotcha:** the Ollama desktop app stores its own settings in `%LOCALAPPDATA%\Ollama\db.sqlite` (table `settings`, columns `expose` and `models`), and **those override the `OLLAMA_HOST` / `OLLAMA_MODELS` environment variables entirely**. Setting the env vars does nothing. Stop the app, edit the DB, restart. `expose=1` makes it bind `0.0.0.0`; `models` is the blobs/manifests parent dir. This is how 22.3 GB of blobs ended up dumped loose in `C:\Users\ohjos\blobs` despite the machine env var pointing at F:.

**Also done this setup:** removed the broken Gemini CLI (`@google/gemini-cli` + `~/.gemini`); installed **Google Antigravity 2.2.1** (`%LOCALAPPDATA%\Programs\Antigravity`). Original small `gemma-4-e4b` model was deleted. See [[user_github_and_devices]] for the machine, [[feedback_cross_device_paths]] for path handling.
