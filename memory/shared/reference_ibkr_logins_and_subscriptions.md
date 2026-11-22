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

WHY THAT ENTITLEMENT READING IS SOLID, since the same session had other faults: in the SAME run 14 feeds delivered
live realtime data with prices, including FDAX and FESX FUTURES on EUREX and HSI and MHI futures on HKFE, plus
BTC.USD, ETH.USD, European equities, mutual funds and EUR.USD on IDEALPRO. Futures streaming works on this login.
What is refused is every US exchange: CME, CBOT, NYMEX and COMEX for futures, and IEX, BATS, ARCA and NASDAQ for
stocks. A half connected session does not refuse Chicago while serving Frankfurt and Hong Kong in the same eight
seconds. The pattern is geographic, not technical.

A SEPARATE FAULT, and the correction of an earlier wrong guess. The empty account summary is NOT a Financial Advisor
account group problem. From IB Gateway's own `launcher.log` (plain text, in the install folder):
1. 11:23:06 the login was attempted in PAPER mode, "mapProdToPaper ... PAPER_CONNECT=0x2000".
2. 11:23:06 IBKR refused: "NSErrorResponse.NO_PAPER_MAPPING [errorMsg=no paper user configured]". This is proof, in
   IBKR's own words, that no paper trading is enabled on the login.
3. 11:23:07 the consequence, and the ONLY farm event in the whole log: "Disconnect all farms due to competing session
   [control=false, context=no paper user configured]". Nothing reconnected them.
4. 11:25:47 a second attempt authenticated, "authType=MARKET_DATA_CONNECTION", "authenticated=true", into a user
   directory the log had to CREATE, then stopped at "Changing state for connection from PRELOGON to PRELOGON".
TRY FIRST when accounts read empty: select Live, not Paper, in the login dialog and restart the session. Build FA
account group support only if that does not fix it.

TWO LESSONS WORTH MORE THAN THE INCIDENT:
1. An open API port is NOT proof of a usable session. The market data half and the account and order half of an IB
   Gateway session come up INDEPENDENTLY. Port 4001 answered, 14 market data feeds were live, and the account side
   had never logged on, all at once. Check for notices 2110, 2103 usfarm, 2105 ushmds and 2157 secdefil, and for an
   account summary that actually answers, before believing a session is healthy.
2. `jts.ini` in the IB Gateway install folder is readable and useful: `[Communication] 2ndFactor` lists one
   obfuscated settings directory PER LOGIN ever used on the machine, `[Logon] tradingMode` is l for live,
   plus `ApiOnly` and `TrustedIPs`. A directory with no `ibg.<weekday>.xml` history is a login that has never run
   there before. The per-session settings files themselves are encrypted (an `IBGZENC` header) and cannot be read.
   The log also lists the second factors offered: passkey, IB Key and the mobile authenticator app, with `pwd=1`,
   and CHALLENGE messages are issued on every login. So a stored username and password does NOT buy an unattended
   login; auto login is not a pure software fix.

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


## IB Gateway automatic login, built 2026-11-22: what works and what CANNOT

THE HARD LIMIT: this account's second factor is a PASSKEY, a physical key that must be chosen on
screen and plugged in. No software can do that. Unattended login from cold is IMPOSSIBLE and must
never be promised. What IS possible is IBC's AutoRestartTime: IB Gateway writes a file named
`autorestart` after a successful login when AutoRestartTime is set, and while that file exists IBC
restarts Gateway with NO password and NO passkey. So the shape is: a person logs in by hand once,
and the daily restart is then free. Set to 03:05 PM, inside the CME maintenance break, at the
owner's instruction; they also want historical backfill prioritised in that hour.

THREE BUGS HIT WHILE BUILDING IT, each of which wasted a cycle:
1. `StartGateway.bat` hard-set `TWS_MAJOR_VRSN=1019` and a `Documents\IBC\config.ini` path with
   plain `set`, clobbering anything passed in the environment. Installed Gateway is 1050. Fixed by
   rewriting those lines as `if not defined NAME set NAME=default`, so the environment wins and a
   manual double-click still behaves. Detect the version from the numbered folders, never type it.
2. IBC could not find Java. Gateway ships its own private JRE and it is the only Java present, so
   `JAVA_PATH` must be set to `<gateway>\<version>\jrein`.
3. THE SUBTLE ONE. All three IBC batch scripts run `setlocal enableextensions enabledelayedexpansion`
   and pass the password as `/PW:%TWSPASSWORD%`. Under delayed expansion cmd.exe EATS an exclamation
   mark inside a value. The advisor password contains one, so Gateway's dialog came up with the
   username filled and the password field EMPTY. Percent, caret, ampersand, pipe and angle brackets
   would break the same way. FIX: never put a credential on a command line for IBC. Generate a
   runtime config file from IBC's config.ini with IbLoginId, IbPassword and TradingMode filled, and
   point `CONFIG` at it; IBC's Java reads the file and no shell ever parses it.
4. `TWS_SETTINGS_PATH` left empty makes IBC's `where /R` search for the autorestart file match
   nothing, so it says "full authentication will be required" every time. Point it at the folder
   holding the per-login settings directories.

WHAT WAS BUILT, all in the owner-only logins folder beside the env files:
- `start_gateway.ps1 -Login personal|advisor|business [-WaitMinutes 30]`: reads the env file,
  validates it, generates the runtime config, starts IBC, then WAITS patiently, reporting every 30
  seconds, and never closes the window.
- `watch_gateway.ps1`: scheduled task "RustTOS IB Gateway autologin watchdog", every 5 minutes.
  Three brakes, all proven: it stands back while a login lock file exists, stands back while a
  Gateway window is open, and REFUSES to start anything (exit 3) when there is no autorestart file,
  because a restart would then stop at a passkey prompt nobody is watching.

THE LESSON ABOUT CONDUCT, worth more than the code: while the owner was part way through a passkey
login, repeated automated restarts closed the window under them. Do not retry against a resource a
person is actively using. A login in progress is a human action; wait for it.
