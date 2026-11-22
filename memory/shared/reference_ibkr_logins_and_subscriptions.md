---
name: reference-ibkr-logins-and-subscriptions
description: "IBKR market data is sold per LOGIN: the advisor login serves no US futures; where the three login env files live"
metadata:
  node_type: memory
  type: reference
  originSessionId: 1357db99-9ad1-48ec-8f53-a505f7663727
  modified: 2026-11-22T18:47:55.049Z
---

An IBKR market data subscription belongs to a LOGIN (username), not to a person and not to an account. Two logins of
the same owner do not see the same data. Measured with `rusttos_ibkr_subscription_probe` (read only, client 8971),
same program and same 15 subscriptions both times, only the login in IB Gateway differing:

1. PERSONAL login, 2026-11-11: 10 of 15 WORKS, including subscription 6 "US Futures Value Bundle PLUS (NP,L2):
   CME, CBOT, NYMEX, COMEX depth" and subscription 9 "US Securities Snapshot and Futures Value Bundle".
2. ADVISOR login, 2026-11-22 11:28 to 11:34 MST: subscriptions 6 AND 9 are REFUSED, IBKR code 354 "Requested market
   data is not subscribed ... Delayed market data is available". Every US futures contract tried was refused:
   6E, ES, MES, GC, CL, ZN. Code 354 is a PERMISSION answer, not a market hours answer, so a closed market does not
   explain it. Report: `data/reports/ibkr_subscription_probe_2026-11-22_112802.txt` in the RustTOS repo.

CONSEQUENCE: subscription 6 is what serves the 6E, 6A and 6J depth books. Any futures recording (depth, top of book,
trade prints, backfill) must run on the PERSONAL login, or the subscriptions must be bought again for the advisor
login. Do not assume an advisor or business login inherits anything.

Two more things measured the same day:
1. The advisor login's account discovery could NOT finish. `reqAccountSummary` over the "All" group returned 0 rows
   with no end marker. That is the known behaviour of a Financial Advisor master: advisor support needs account
   GROUPS, which RustTOS does not ask for yet. So "discover all accounts per login" is still an open build item.
2. IB Gateway can have its API port OPEN while not being connected to IBKR at all: notices 2110 (connectivity to the
   server is broken), 2103 usfarm, 2105 ushmds, 2157 secdefil. An open port is therefore NOT proof of a working feed;
   check for those notices and for an account summary that answers.

THE LOGIN FILES, created 2026-11-22: `C:\Users\ohjos\.rusttos\logins\ibkr_personal.env`, `ibkr_advisor.env` and
`ibkr_business.env`. Deliberately OUTSIDE the RustTOS repo so no commit, branch or backup release can carry them;
the repo's `.gitignore` refusing `.env` is only the second guard. ACLs were stripped of inheritance and granted to
`DIMASKUSPC\ohjos` only (no SYSTEM, no Administrators); check with `icacls`. They hold PLACEHOLDERS only, filled in
by the owner. RustTOS reads them through `RUSTTOS_ENV_FILE` and
`rusttos_core::secret_settings::setting`, which prefers a real environment variable and falls back to the file;
`mask_secret` keeps a secret out of every log line. Existing key style in the repo's own `.env`:
`IBKR_ACCOUNT_NUMBER_<last three>` and `SCHWAB_ACCOUNT_NUMBER_<last three>` / `_HASH_`.

The owner said 2026-11-22 they do not think paper trading is enabled on any account. RustTOS calls an account PAPER
only when BOTH signs agree: the id starts with "DU" AND the port is a paper port (4002 Gateway, 7497 TWS). Anything
else is treated as real money and can never place an order, so a live-only setup is safe by default but gives no
place to prove an order path.

Related: [[project_rusttos]], [[project_rusttos_state_2026-11-22]], [[reference-ibkr-futures-symbols]],
[[reference-rusttos-backups-and-data-jobs]], [[project_brokers_schwab]].
