---
name: project-ironbeam-api-and-business-account
description: "Ironbeam futures: demo API (Jan 2026), key disabled for ~2,000 calls/min, limit 5 per second; Dimaskus LLC corporate account canceled 2026-06-04 for missing documents"
metadata:
  node_type: memory
  type: project
  originSessionId: 1bce6fe7-f3f2-4733-a974-2989fee10ed0
  modified: 2026-11-25T16:11:06.739Z
---

Read from Outlook on 2026-11-25 (joshua.a.zayne@hotmail.com thread "API Access", and dimaskusllc@gmail.com store). Contact: Brent Murphy, Business Development, brent.murphy@ironbeam.com, 312.765.7236; main 312-765-7200, trading@ironbeam.com.

1. 2026-01-21: Brent sent DEMO API credentials (username, password, API key are in that email) plus REST docs link. Base URL used: https://demo.ironbeamapi.com/v2/ . Symbol format XCME:ES.H26 (exchange:root.monthcode+2-digit year).
2. 2026-01-22: commissions PDF "Ironbeam Commissions 2026.pdf" (updated 1/14/2026): commission $2.00/side standard, $0.99 equity micros, clearing $0.25, plus exchange/NFA (ES all in 3.65, MES 1.61, ZN 3.07, CL 3.77).
3. 2026-01-22/23: user emailed Certification of Beneficial Owners, passport, EIN; filed business application in portal (login email to dimaskusllc@gmail.com); linked Schwab bank via Plaid; sent small ACH. Ironbeam: "approved, final checks".
4. Jan 23 to 29: demo data problems, all user errors: `market` not `marketdata` in path (404), quotes subscribe needs open WebSocket stream, live/demo keys swapped, trailing space in key (400).
5. 2026-03-11: Ironbeam DISABLED the API key, ~2,000 calls/min from an auth retry death loop. User throttled to 1/s. 2026-03-13: limit is 5 requests per second.
6. 2026-03-17 to 05-13: reminders for driver's license, proof of address, corporate articles, written ownership statement, IRS EIN letter. 2026-06-04: corporate application CANCELED for missing documents.

7. 2026-11-25 ~09:10 MST: owner asked for a Rust Ironbeam WebSocket client in RustTOS feeding the Quantower style desk. Worktree `RustTOS_agents\ironbeam-link`, branch agent/ironbeam-link from agent/chart-redesign cb61a67b, cargo output on F:\RustTOS_targets\ironbeam-link (owner chose F: because C: was 91 percent full; he declined deleting the 1.3 TB of merged session caches). Decisions D0800 to D0809. Orders not built (held). Proven only against fakes until the account is reopened. Official OpenAPI 2.1 spec and reference copied into that worktree's docs/ironbeam/. Old Python client in Brokers repos is mostly guesses; do not port it.

**How to apply:** any Ironbeam code needs a hard request cap under 5/s and a backoff that stops on auth failure. Reopening needs a fresh application with those documents (see [[project_dimaskus_llc_entity_docs]]). Python Ironbeam client code exists in Brokers_surface_base (tests/test_ironbeam_client.py).
