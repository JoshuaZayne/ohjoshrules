---
name: project_attorney_outreach_responses
description: "Highland Homes outreach 2026-11-07: replies and the fit gate (attorney_search/fit.py)"
metadata:
  node_type: memory
  type: project
  originSessionId: 2edaab43-0968-4b37-b12b-0e3dca580b74
  modified: 2026-11-07T15:31:41.925Z
---

**Summary moved from the memory index (2026-11-08):** Highland Homes attorney outreach (2026-11-07): who was emailed, who replied (Dial and Ventura declined), what each reply taught, and the fit gate (attorney_search/fit.py) that now screens every lawyer before sending

Attorney outreach for the 1725 Thicket Hill dispute (repo ThicketHillProperty), sent 2026-11-07 from joshua.a.zayne@hotmail.com through Microsoft Graph (scripts/send_attorney_inquiries.ps1), CC Olivia, Kevin, joshua.a.zayne@gmail.com. Reply requested by Mon 2026-11-09; Highland's flooring default deadline is Fri 2026-11-13.

**Status as of 2026-11-07 ~06:55 MST:** 57 inboxes in the first wave (62 lawyers, the 60 rated plus Shields Legal Group, which opposed Highland on appeal 05-24-00946-CV), plus the expanded top picks (11 sent before the fit gate existed, the rest resumed after it). Bounces: inquiriesbrady@sparkslaw.com and info@ccsb.com (resent to brady@ and caltman@ cc lcurrie@), info@faegredrinker.com (mail loop on Faegre's side; excluded), the Shields personal note to dramsey@/bhiggins@ (blocked by Microsoft as spam; their firm inbox has the full inquiry). Live status: documents/ATTORNEY_OUTREACH_STATUS.md; answers: attorney_search/output/ATTORNEY_RESPONSES.xlsx (user fills the yellow columns; never overwrite them).

**Replies and what each one taught:**
1. Karl Dial, Greenberg Traurig, 06:16 MST: "I am unable to take this case at this time." Lesson: firms of over 200 lawyers decline or carry builder-client conflicts; skip them. Suggested reply: thanks, ask for a referral, ask for confidentiality.
2. Misty Ventura, Shupe Ventura, 06:44 MST: "My firm does not handle matters involving private-party disputes." Lesson: a land use, municipal or government practice (areas Government/Administrative, Public Utility; site "focuses on the practice of land use law") is not a litigator for homebuyers, even with a residential real estate certification. Reply drafted: thanks, referral, confidentiality.
3. Aaron C. Lee Law Firm, auto reply 05:42: a title company fee attorney office. Lesson: closing-only practices ("title company", "real estate closings", "fee attorney") are skipped unless litigation evidence is strong.
4. Hallett & Perrin inbox auto reply (S. Gay, out until after Thanksgiving); Leland De La Garza was copied directly.

5. Michael Hurst, Lynn Pinker, 06:57: referral "Recommend Julie Pettit: 972-533-0048" (Pettit Law Firm, Dallas, passes the fit gate). The 07:05 referral email to jpettit@pettitfirm.com was BLOCKED by Microsoft (550 5.7.520 spam), the second such block after the Shields personal note: short one-off personal notes from hotmail to new addresses get blocked; send those from a gmail account or call.
6. Misty Ventura, 06:50: referred Robert Miklos (Ferguson Braswell Fraser Kubasta, a Plano firm; land use and real estate profile, fails the fit gate on paper; conflict check essential). I MISSED this: it reached a gmail or yahoo copy, not hotmail, and I told the user "she sent only one reply." I can read only joshua.a.zayne@hotmail.com (Graph) and olivia.m.zayne@gmail.com (Gmail connector), not joshua.a.zayne@gmail.com or kevin.peccorini@yahoo.com. When reporting replies, always name which inboxes were checked and ask the user to forward anything that landed elsewhere.

7. By 08:30 MST: Jim Pikl (Scheef & Stone) CAN HELP (available Mon 11/9 afternoon, $5k retainer or $20k if litigation, $375 to $1,200/hr, no contingency under $5M; dislikes clients who consulted AI first). Referrals: O'Kane -> Noah Nadler, Alex Adewunmi; Boston (conflict) forwarded to Frank C. Fleming (solo, lawyerfcf@gmail.com, 2004 public reprimand/probation on State Bar), who is to call Monday; Dial (second reply: represented Highland) -> Andy Korn, Scott Keller; Sparks -> legal aid links. Cagle (Buchalter) declined, called the email unsolicited.
8. Reply pipeline: scripts/update_replies.py (read-only Graph fetch, attorney_search/reply_classifier.py + question_answers.py per-question bins) -> responses_tracker.py -> rate_attorneys.py -> add_call_sheet_to_ratings.py -> archive_outputs.py. Never sends. If a save fails, Excel still holds the file even after the user "closed it": check open workbooks via COM and close only a Saved workbook when the user wants it closed.

**Fit gate (attorney_search/fit.py, wired into scripts/prepare_attorney_outreach.py):** a lawyer must show litigation (litigation practice area, trial or appellate certification, appeals, or litigation on the website) AND real estate, construction, consumer or contract dispute work; skipped for transactional or closing signals when litigation evidence is thin, builder-side signals (for example McCathern "representing homebuilders & developers", Cox "represent construction clients including builders"), firms over 200, not in private practice, off-topic-only practices, land use or government practices without litigation, and firms that already declined (--declined-firms). Calibrated 9 of 9 on known outcomes; 228 of 290 expanded-pool lawyers with email pass. Thad Spalding (appellate, no subject evidence) was emailed before the gate existed. McCathern, PLLC was emailed in the first wave but its site advertises representing homebuilders: treat any reply with conflict caution.

**Why:** the user said "make sure we are only sending emails that can help us, improve the checks and update the memory of responses."

**How to apply:** build every future recipient list with prepare_attorney_outreach.py (fit gate on by default), add any firm that declines to --declined-firms, log replies in ATTORNEY_RESPONSES.xlsx by exact full name (a first-name match once wrote Dial's reply onto Karl Rybicki's row), and keep the send safeguards in [[feedback_outlook_com_send_rate]]. Related: [[project_thicket_hill_oct2026_status]], [[feedback_outlook_drafts_recipe]].

## Outcome (2026-11-09, about 15:30 MST)

1. **Retained as dual counsel:** Frank Fleming (solo, Dallas, 214-373-1234, lawyerfcf@gmail.com, $350/hr, $5,000 deposit replenished) and Mary Melle (Calhoun Bhella LLP, John Price's Dallas colleague, 214-577-3447, mmelle@calhounbhella.com, $695/hr).
2. **Paid 2026-11-09:** Melle $695.00 (AMEX via LawPay to the firm trust account, transaction 177553805); Fleming $350.00 (Zelle from Schwab, confirmation ending 7227) against his invoice "Atty Fees 01". Total $1,045.00. Recorded in documents/attorney_pricing.json "payments" and the workbook Pricing tab.
3. **Both received** the clean counsel package (documents/counsel_package/clean_2026-11-09_151242/, three zips) on 2026-11-09, 15:16 to 15:23 MST.
4. **Open with counsel:** deadlines (Erick and Riney both warned of limitation periods), Friday 2026-11-13 flooring selection, the Highland HomeLoans Adobe Sign request for a revised VA-26-1880 (do not sign before asking), Fleming's 2004 discipline record.
5. **Gotchas learned:** lawyers may answer inside our quoted email (update_replies reads inline answers only when they say so); Gmail blocks zips containing .js; emailed wire instructions should be confirmed by phone (pay by card link instead).
