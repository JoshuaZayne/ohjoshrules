---
name: project_nemoclaw_install
description: "NVIDIA NemoClaw install on the desktop (WSL2 + Docker + local Ollama), what is done and the two steps still blocking it"
metadata: 
  node_type: memory
  type: project
  originSessionId: 0637b3ac-9ee1-4b8c-8b48-57545ee8f74d
  modified: 2026-08-09T20:02:27.894Z
---

Installing NVIDIA NemoClaw (github.com/NVIDIA/NemoClaw), an agent sandbox stack, on the desktop. Started 2026-08-09.

**Key constraint:** the desktop has an AMD RX 7900 XTX, no NVIDIA GPU, so NemoClaw's managed vLLM and NIM inference paths are unavailable. The only viable path is the `ollama` provider pointed at the Windows host Ollama. NemoClaw itself runs in Docker inside WSL2 and reaches the host at `host.docker.internal:11434`. Native Windows is explicitly unsupported by NVIDIA; WSL is required.

**Model choice:** stay on `qwen3.6:35b`, which is also NemoClaw's own default starter model when GPU memory allows. It fits this card. See [[project_local_llm_coding_setup]] for the benchmark. Do not downgrade to 27b, that variant is dense and trades quality for almost no speed.

**Done:**
- Ubuntu-24.04 WSL2 distro installed and made the default distro (was `docker-desktop`, which is the Docker utility distro and a bad default).
- Non-root user `josh` created with NOPASSWD sudo, systemd enabled via `/etc/wsl.conf`.
- Node v22.23.2, npm 10.9.8, Python 3.12.3 in the distro (NodeSource repo, since Ubuntu 24.04 ships Node 18 which is too old).
- Ollama set to bind `0.0.0.0` and models relocated to `F:\OllamaModels`, both via the db.sqlite override described in [[project_local_llm_coding_setup]].

- Docker Desktop WSL integration working, `docker` 29.1.3 usable from inside Ubuntu-24.04.

**Docker WSL integration gotcha (cost real time):** enabling it produced `DockerDesktop/Wsl/ExecError ... docker-desktop-user-distro proxy ... exit status 1`. Cause was a **stale `/mnt/wsl/docker-desktop` mount**, where `docker-desktop-user-distro` was a 0-byte non-executable file dated from an earlier session, so Docker was exec'ing an empty file. Fix: stop Docker Desktop, `wsl --terminate` both Ubuntu-24.04 and docker-desktop, let Docker Desktop restart. The mount is then repopulated (the binary should be ~20 MB and `-rwxr-xr-x`). Editing `IntegratedWslDistros` in `%APPDATA%\Docker\settings-store.json` alone does nothing; the GUI toggle is what actually triggers it.

- WSL to host Ollama connectivity working.

**Firewall gotcha (the big time sink):** WSL could not reach host Ollama, and adding an inbound allow rule for port 11434 did NOT help, in any scope. Cause was **pre-existing `ollama.exe` inbound Block rules**, the kind Windows silently creates when a "Defender Firewall has blocked some features of this app" popup gets dismissed. **In Windows Firewall, Block always beats Allow**, so no port rule can ever override an app Block rule. Diagnosis sequence that worked: confirm Windows itself reaches the WSL adapter IP (it did), confirm WSL reaches the internet but cannot even ping the host gateway, then `netsh advfirewall set allprofiles state off` briefly to prove the firewall is involved. Fix:
`powershell -NoProfile -Command "Get-NetFirewallApplicationFilter | ? { $_.Program -like '*ollama*' } | Get-NetFirewallRule | ? { $_.Action -eq 'Block' } | Remove-NetFirewallRule"`
This box has similar leftover Block rules for chrome, python, PyCharm, iTunes, NinjaTrader, Apache and others, so suspect the same pattern for any future local service that mysteriously refuses connections.

**Tooling limitation worth remembering:** the `Get-NetFirewallRule` / `Get-NetFirewallApplicationFilter` cmdlets return **nothing at all** from a non-elevated shell, including `-PolicyStore ActiveStore` queries which report 0 rules. That silence looks exactly like "no such rule exists" and produced one wrong conclusion here. Use elevated `netsh advfirewall firewall show rule` as the source of truth instead.

**Model tag note:** NemoClaw wants the tag `qwen3.6:35b` but the pulled tag was `qwen3.6:latest`. Use `ollama cp qwen3.6:latest qwen3.6:35b` to alias it. Both tags then share one ID and no blobs are duplicated, avoiding a 24 GB re-download.

**Install command once unblocked** (run in the Ubuntu shell):
`curl -fsSL https://www.nvidia.com/nemoclaw.sh | NEMOCLAW_AGENT=openclaw NEMOCLAW_PROVIDER=ollama NEMOCLAW_MODEL=qwen3.6:35b NEMOCLAW_CONTEXT_WINDOW=65536 NEMOCLAW_ACCEPT_THIRD_PARTY_SOFTWARE=1 bash`

**Known upstream gotchas:** use the native `ollama` provider, not the generic compatible-endpoint one, because the latter ignores `NEMOCLAW_LOCAL_INFERENCE_TIMEOUT` and leaks a 60s default that cuts off slow reasoning models (NemoClaw issue #2403). NVIDIA's own docs rate Ollama "Risky" for multi-tool agent loops versus vLLM with a tool-call parser, so expect some tool-dispatch flakiness.
