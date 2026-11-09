---
name: Broker Docker + venv isolation requirement
description: "all broker code in Docker with venv; RustTOS is the exception (local)"
type: feedback
---

**Summary moved from the memory index (2026-11-08):** ALL broker code (all 13 brokers) must run inside Docker with a Python venv, never on local hardware. Exception: the RustTOS repo runs everything locally (user decision 2026-11-01).

All broker-related code must run inside Docker with a Python virtual environment. Never run any broker code directly on local hardware. This applies to ALL 13 brokers: IBKR, IronBeam, TastyTrade, Schwab, MooMoo, Coinbase, E*Trade, Fidelity, NinjaTrader, TradeStation, Vanguard, Webull, FIX.

**Why:** User is extremely firm about this — broker SDKs and any related code must be fully isolated from the local machine. This is a hard security/isolation boundary. Originally stated for MooMoo, then expanded to all brokers.

**How to apply:** Before running any broker script, test, or SDK call, ensure it is executed inside the appropriate Docker container which has its own venv. Both Docker AND venv are required — one without the other is not acceptable. The `BrokerClient.__init__()` enforces this at the Python level — process exits if not in Docker + venv. Each broker has a `docker-compose.<broker>.yml` override file.

**Exception: RustTOS (decided by the user 2026-11-01 16:41 MST).** The repo `F:\GitHub Repos\RustTOS` runs everything locally, broker feeds included, with no Docker. The user said: "make this repo not use docker only installing shit for intial setup, once setup for this repo, make it so everything is local". Do not reintroduce Docker there. The rule above still applies to the Python Brokers repo and every other broker code. See [[project_rusttos]].
