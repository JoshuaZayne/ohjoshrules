---
name: reference_terminal_ai_clis
description: "Inventory of terminal-based AI agent CLIs installed on the desktop, where each lives and its auth state (surveyed 2026-08-11)"
metadata: 
  node_type: memory
  type: reference
  originSessionId: b5ff3261-08b7-4d09-ae06-7a616c36f83b
  modified: 2026-08-12T01:57:22.895Z
---

Agentic coding CLIs installed on the **desktop** (`C:\Users\ohjos`), surveyed 2026-08-11.

**Windows, authenticated and usable:**
- `claude` — Claude Code 2.1.228, npm `@anthropic-ai/claude-code`. Creds at `~/.claude/.credentials.json`.
- `grok` — Grok CLI 0.2.106, npm `@vibe-kit/grok-cli` but the real binaries are `~/.grok/bin/grok.exe` and `agent.exe`. Auth at `~/.grok/auth.json` (not `config.json`). Has skills/sessions/memtrace dirs, so it is a full agent, not a chat wrapper.
- `kimi` — Kimi Code 0.27.0 at `~/.kimi-code/bin/kimi.exe`. Creds at `~/.kimi-code/credentials/kimi-code.json`.
- `agy` — Antigravity CLI 1.1.1 at `%LOCALAPPDATA%\agy\bin\agy.exe`. The terminal companion to the Antigravity IDE.

**Windows, needs one interactive login:**
- `gemini` — Gemini CLI 0.55.1. Configured for Google OAuth; user must run `gemini` once and pick "Login with Google". See [[project_local_llm_coding_setup]] for the PATH-shadowing history.

**WSL (Ubuntu-24.04):**
- `nemoclaw` v0.0.103, plus `nemo-deepagents` and `nemohermes`. See [[project_nemoclaw_install]].

**Not agents, but adjacent:**
- `ollama` 0.32.1 and `lms` (LM Studio) — local model runtimes that the above can point at.
- `gemma` / `gemma-cli` 0.1.12 (npm) — small helper CLI, note `gemma-cli` is not a command, the binary is `gemma`.
- `gask` — the user's own one-shot Gemini question script on `F:`.
- `gh` has no Copilot extension installed.

**Survey gotcha:** probing with guessed command names missed `kimi` and `agy` entirely. The reliable method is to dump PATH and inspect every suspicious directory, since these tools install to dotfile dirs like `~/.kimi-code/bin` rather than a shared bin.
