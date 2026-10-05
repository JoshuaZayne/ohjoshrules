---
name: Broker Docker + venv isolation requirement
description: ALL broker code (all 13 brokers) must run inside Docker with a Python venv — never on local hardware. Non-negotiable.
type: feedback
---

All broker-related code must run inside Docker with a Python virtual environment. Never run any broker code directly on local hardware. This applies to ALL 13 brokers: IBKR, IronBeam, TastyTrade, Schwab, MooMoo, Coinbase, E*Trade, Fidelity, NinjaTrader, TradeStation, Vanguard, Webull, FIX.

**Why:** User is extremely firm about this — broker SDKs and any related code must be fully isolated from the local machine. This is a hard security/isolation boundary. Originally stated for MooMoo, then expanded to all brokers.

**How to apply:** Before running any broker script, test, or SDK call, ensure it is executed inside the appropriate Docker container which has its own venv. Both Docker AND venv are required — one without the other is not acceptable. The `BrokerClient.__init__()` enforces this at the Python level — process exits if not in Docker + venv. Each broker has a `docker-compose.<broker>.yml` override file.
