---
name: project_ram3500_autonation_deal
description: "Ongoing negotiation to buy a 2026 Ram 3500 Limited from AutoNation (Littleton CO), incl. contacts, target, trades, and deal docs"
metadata: 
  node_type: memory
  type: project
  originSessionId: c20cac6a-98c1-41e5-9601-db94a22bcc15
  modified: 2026-07-21T13:25:53.405Z
---

Buying a **2026 Ram 3500 Limited Mega Cab 4x4** from **AutoNation Dodge Ram Broadway, Littleton CO**. Stock **TG332645**, VIN **3C63R3PL0TG332645**. Listed **$91,497** (MSRP $104,665), **NEW**, and it's been on the lot ~105 days (since Mar 30, 2026). Loaded: HO Cummins, Limited Level 1 group, Night Edition, power sunroof, gooseneck/5th-wheel prep, new 8-speed HD. cars.com detail id `4d4770d1-14c8-4cd2-9a10-5eafcf169648`.

**Contacts:** salesperson **Renato Razuri** (RazuriR@autonation.com); **Sales Manager Kris Staroske** (staroskek@autonation.com, 815-354-4360) — Kris controls pricing, so **reply to Kris, cc Renato**, address it to Kris.

**Price reality (from the RamMegaCabDataScrapper comps):** VIN-verified NEW 2026 3500 **Limiteds** clear **$90k–$98k** (median ~$96.5k), so this truck at $91,497 is already low-end. **$85k is NOT comp-supportable** for a loaded new Limited (a used 2026 Limited is ~$90k). Realistic strong target **~$87–88k**. Real leverage = **105-day aging + 2027 HDs landing ~Oct 2026** + own financing (kills reserve, keep the ~$6k cash) + 2 trades + LLC/Section 179 — NOT comps. Target/ask being pushed: **$86,500** framed as a motivated-seller/certainty discount, not a market claim.

**Trades for THIS deal (just two, NOT the Ram 1500):** 2020 **Jeep Wrangler** (VIN 1C4JJXFM4LW343576, USAA lien — pull fresh 10-day payoff, target $30k) + 2019 **Ford Transit Connect** XL LWB (VIN NM0LS7E28K1399891, likely clear, target $15k). Get written Carvana/CarMax offers as the floor; negotiate truck price separately from trades; CO/UT trade-in tax credit (~$3k on $45k) means the dealer can be under Carvana and still net even.

**Kris's key pushback (2026-07-13):** several of the emailed comps were **Laramies** (VIN `...ML...`), not Limiteds — our scraper mislabeled them. This drove the scraper **VIN-trim fix** (PL=Limited, ML=Laramie) — see [[project_ram_megacab_scraper]] (PR #4, `parse.trim_from_vin`/`reconcile_trim`).

**Deal docs (F:\iCloudDrive\Documents\Carvana Ram\):** `2026-Ram-Deal-Master.md` (financing CU-vs-captive, incentive buckets, LLC/BusinessLink), and `AutoNation-2026-Ram-3500-Limited-Deal.md` (the 9-step playbook + post-negotiation closing/delivery/Section-179 steps). Email how-to: [[reference_check_email_outlook_com]].

**Twin unit found (2026-07-20):** AutoNation has a SECOND identical truck on the same Littleton lot — stock **TG332644**, VIN **3C63R3PL9TG332644**, **Bright White Clearcoat**, listed **$92,997** (MSRP $104,665, NEW, 20 mi). Same exact build as TG332645 (HO Cummins, Limited Level 1, Night Edition, sunroof, gooseneck/5th-wheel prep, 8-speed HD). Consecutive stock numbers = ordered together. The original TG332645 at $91,497 is the CHEAPER and more aged of the two, so it stays the stronger lever. cars.com id `b1e12357-6c0a-48a7-bcbf-57a0da7b5deb`.

**Negotiation history:** Kris replied 07/13 (flagged our comps as Laramies), user sent $86.5k aging/certainty rebuttal 07/13 22:40. Kris replied 07/14 11:59 ("waiting on GM/GSM to look at the aggressive discount, send me your trades"). User replied 07/14 13:45 (locked $86.5k + both trade VINs) and sent an unanswered follow-up 07/15 23:10. Kris/AutoNation went silent 5 days.

**State as of 2026-07-21:** The **$87,000-on-either-truck** offer (before tax/title, incl $500 veteran; TG332645 or white TG332644, Kris's pick; framed as a $500 bump to close this week; re-asked for Jeep Rubicon + Transit Connect cash trade numbers) is now **SENT** to Kris cc Renato (subject "Re: 2026 Ram 3500 Limited comps", delivered 07/21 07:25). Awaiting Kris's reply. (Separate live lever: South Shore CDJR, nfredericks@sscdjr.com, emailed 07/17 on a Limited.)

**GOTCHA — Outlook stuck-Outbox on COM-created mail:** the 07/20 send sat in the Outbox unsent for a day. Cause: a mail item created via `CreateItem` + **`.Save()`** (the draft/`.Display()` flow) lands in the Outbox WITHOUT the submit flag, so Send/Receive skips it forever (Outlook was online, not Work Offline, no open inspector). Fix that worked: recreate a fresh `CreateItem`, set body/To/CC + `SendUsingAccount`, call **`.Send()`** (not Save), delete the stuck copy, then start SyncObjects. Lesson: to actually SEND from COM use `.Send()`; `.Save()`+`.Display()` only drafts, and if the user hits Send on that draft it can still get stuck. There was a second identical stuck item (07/03 spend email) confirming the pattern.
