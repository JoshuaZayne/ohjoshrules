---
name: project_atv_rollover_claim
description: "ATV rollover claim vs Side By Side Share and renter Conner Corbin: notice of dispute SENT 2026-10-31 21:35 MT (asks $750 loss of use, charge renter $1,555.71+, pay $3,023.66 on account); SxS response due Mon 2026-11-02 17:00 MT; lives in TicketProcessing/ATV_accident"
metadata:
  node_type: memory
  type: project
  originSessionId: c5bc23de-465d-409f-8b0e-7a173ca7df9b
  modified: 2026-11-01T03:36:08.836Z
---

Folder `F:\GitHub Repos\TicketProcessing\ATV_accident\`, branch `atv-accident` (pushed; latest d4c0f14 on 2026-10-20; not merged to main). Plan and step list: `docs/COURT_PLAN_2026-10-20.md`. Older guide: `docs/UTAH_LEGAL_GUIDE.md`.

Facts: 2021 Can-Am Outlander MAX XMR 1000R, VIN 3JBLWAX49MJ000547, owned by Dimaskus LLC. Renter Conner Corbin (385-505-1007) booked the XTP (booking 6aa385a7), took the XMR the morning of 09-11, returned it the night of 09-12, paid 1 night, rolled it onto its LEFT side. Signed Departure Form: existing damage "NONE", $6,000 rollover deductible (p1), 3.9% processing fee "may be passed to the Renter" (p5). Karl Malone Powersports Provo (Can-Am dealer, user confirmed) RO 258550 revised 09-30 = $7,098.56. SxS offer $2,818.41 (resolution dated 09-30), still unsigned. Dillon (Dillon Newman, SxS claims) asked about the vehicle swap 09-13; SxS still paid out 09-14 and adjusted for 5 weeks.

**SENT 2026-10-20 19:02** from dimaskusllc@gmail.com (CC copy in evidence/emails/2026-10-20_190214_*, 15 attachments A1 to A15). Text: `output/platform_reply_final_2026-10-20_180857.txt`. Asks: pay $2,818.41 with no fee deducted; charge renter's card $3,697.92 (unpaid repair $2,747.92 + loss of use $750 + second day $200) plus the $144.22 fee; reconsider under their Terms (Damage section: after notice + 48 h the payment "will be charged"); accept signature with reservation line; else written refusal, mediation, renter name/address. Response due **Friday 2026-10-30**. Numbers from `claim_after_platform_reply.py` (repair $5,566.33; light bar, plate mount, duplicate handguard excluded; seat at $134.99 backrest).

Decisions the user made: keep the $200 second day and $750 loss of use (do not suggest dropping them). Loss of use = 2 platform-booked nights 09-15/16 (XTP 6a9b04ae, XMR 6aa41c4d) + 09-22 asked for and agreed in texts but never booked: never call 09-22 booked. Plate mount dropped (zip-tied before rental). No Sept 11 call log, so never claim that call.

Hazards: the Josh S texts (`evidence/private_do_not_send/`, git-ignored) discuss paying delivery/helmets by Venmo; the Terms say fee bypass voids coverage for all the owner's vehicles: never send them to SxS. SxS Box folders are view-only (itemDownload=false), so no photo metadata. The "pre-booking" frames show mud splatter and light scuffs, no cracks. An old garbled 2026-10-17 draft ("Booking 6aa385a7 ... confirmations needed") is still in dimaskusllc Drafts: never send it.

**SxS REPLIED 2026-10-29 11:50** (to hotmail CC; saved, not yet committed, in `evidence/emails/2026-10-29_115047_joshua.a.zayne_Re_Final_Claim_Resolution_revised_3023.66/`): revised total $3,023.66 = repairs $2,665.52 + partial payouts $198.14 (RH rear fender $64.57, LH radiator support $35.25, Kemimoto backrest $90, rear mudguards $3.12/$5.20) + loss of use $160 (09-15/16 booking $200 less $40 fee). Declines second day (departure form return 11:59 next day), declines renter collection, says pre-rental photos show prior damage so "NONE" does not control. Acceptance page says "full and final resolution of this claim". New shop RO dated 10-28 ($2,526.10 incl. $144.99 customer-pay winch rope) shows radiator support 705016599 and handguard pair at qty 0 even though SxS approved them ($274.98). Under the user's numbers the renter balance becomes $3,492.67 (repair $2,702.67 + loss of use $590 + second day $200). The user's 10-26 nudge from dimaskusllc showed sender name "Joshua Johnson".

Next (was: if SxS refuses by 10-30): sign with the reservation line, collect $2,818.41, demand letter to the renter for $3,697.92, then Utah small claims (limit $20,000). Disputes with SxS itself go to FairClaims arbitration.

Mail access: claim mail is in joshua.a.zayne@hotmail.com; the dimaskusllc@gmail.com Outlook store has not synced since 2026-09-20 (sending still works; verify via the hotmail CC). See [[reference_check_email_outlook_com]].


**2026-10-30 reply DRAFTED (not sent):** `output/platform_reply_draft_2026-10-30_153923.txt`, opened as an Outlook draft from dimaskusllc (attachments B1 = Josh S 09-04 platform "corporate retreat" message, B2 = 09-12 23:55 email without its 32 MB of attachments). Numbers from `claim_after_revised_proposal.py`: plan repairs asked $4,835.87 (+$1,824.10 for 3 fenders, labor, quantities, $100 supplies; +$38.96 rear mudguards in full; +$109.15 backrest cover 708002891 $134.99 + 0.3 h from the 09-23 order instead of the $90 partial); documented loss now $6,551.58 (repair $5,601.58 incl. LH radiator support at SxS's own $35.25); renter share $3,527.92 at the current offer, exactly $1,555.71 if the plan pays as asked. Letter also asks: hidden-damage supplement not barred by 'FULL AND FINAL', cargo box decided on a Karl Malone quote (USER MUST GET THE QUOTE; never priced), LH radiator support checked for bending, Schedule C line-by-line collection answers. Wording: 'second day of use', not 'second unit'; loss of use $750; undisputed minimum renter charge $1,555.71; response due Tue 2026-11-03 17:00 MT (draft now v3 `output/platform_reply_draft_2026-10-30_154745.txt`, formal notice with Schedule A Terms T1-T23 and Schedule B forms F1-F6 verbatim). User confirmed 2026-10-30: the ATV is still at Karl Malone, out of service (in since 09-14). The user cancelled the XTP booking 6a9b04ae THEMSELVES (did not want to risk the $18k XTP under coverage that was paying short), so never claim the XTP night as loss caused by the damage. Loss of use now rests on the Outlander alone: booked night 6aa41c4d $200 plus uncapped "down time" (Terms, Allowed Use: renter "remains responsible for all damage to the rental, missing equipment, down time, and Owner's administrative expenses") at $200/day (48 days = $9,600 on 10-30), asking the platform only the $750 cap and reserving the rest against the renter. Departure Form p4 return time is "2359 on 09/12/26" (written by the owner), so the second day is argued as an agreed 2-unit possession, not a late fee.

**2026-10-30 18:52 v4:** current letter is `output/platform_reply_draft_2026-10-30_185222.txt` (pushed to the Outlook draft, not sent). User wants EVERY time limit 48 hours or less (said "cut back this 7 day bull shit"); response deadline moved to Mon 2026-11-02 17:00 MT. Added "WHO OWES WHAT UNDER YOUR TERMS" tables (A plan covers owner, B renter owes, C SxS undertook, D owner duties met). Fact check tool: `python fact_check_letter.py <letter.txt>` (15 methods M01-M15, registers in `fact_check_registers.py`, writes output/fact_check_matrix_<stamp>.xlsx/.md; exit 1 on any FAIL). Open strategy risks flagged by reviewers, awaiting user decision: deductible argument (VIII.9-10) lets SxS say the plan owes nothing under $6,000; the 10-20 letter said Dimaskus "will accept $2,818.41"; 10-17 email also says SxS "cannot enforce an additional unit's charge"; accord and satisfaction risk in signing "FULL AND FINAL".

**2026-10-31 20:33 v5:** current letter `output/platform_reply_draft_2026-10-31_203320.txt` (in the Outlook draft, not sent). The user applied reviewer items 2,3,4,5,6,8,9,10 and did not pick #1 (the deductible argument VIII.9-10 stays), #7 (the $9,600 down time stays), #11 (the $40 fee fight, the Kemimoto $599.99 seat and "completely over" stay) or #12 (length). Changes made:
1. New Definitions item 4 explains that the Oct 20 acceptance of $2,818.41 lapsed.
2. Part VII.5 quotes the full Oct 17 "cannot enforce" sentence and answers it.
3. Part XII asks SxS to pay the $3,023.66 now "as a partial payment on account ... not in full settlement and not as an accord and satisfaction"; the protest wording now begins "Signed under protest".
4. The Sept 22 rental sentence is cut, and the second day is to be charged through the platform.
5. The "refunded / earned nothing" claim is cut.
6. Remittance is now "less only Owner Fees T5 permits", with those fees charged to the Renter.
7. The "does not dispute as owed" wording and II.3 are softened.
8. Part XI items 15 and 16 ask for the Protection Plan Policy, Fees Policy, Booking Agreement (new Schedule A T24, Other Policies) and proof the Renter bought the plan; interest is reserved in XII.6.
9. "seven weeks" now reads "nearly seven weeks".
The fact checker was updated (T24, "Signed under protest" exemption, Oct 20 historical figures allowed, "nearly seven weeks") and shows 0 FAIL, 0 date WARN.

**2026-10-31 20:39 v6:** current letter is `output/platform_reply_draft_2026-10-31_203902.txt`.
1. The user thinks in DAYS. SxS's "unit" (Oct 17: "one unit (night) gives the renter 24 hours") and the payout's "1 night" mean the same 24-hour, $200 period.
2. The letter now defines "a Rental Day" (Definitions 1(h)) and uses it in all of our own prose.
3. "Unit" and "night" appear only inside SxS quotes.
4. Never use "unit" in our own words: it reads as a second vehicle.

**2026-10-31 20:47 v7:** current letter is `output/platform_reply_draft_2026-10-31_204630.txt` (in the Outlook draft, not sent).
1. Dated Oct 31 at the user's request. The deadline stays Mon Nov 2 at 5 PM MT. Down time is 49 days, $9,800.
2. Alignment fixes:
   1. VIII.9(b) no longer says the plan only pays above the deductible, and new VIII.9(d) says no double recovery.
   2. Pay-now wording is consistent in I.9, IX.2, row 8 and the Part XII title.
   3. The Definitions 4(c) aftermarket wording matches VI.B.
   4. The VIII action now includes the $965.71 alternative.
   5. Part VII and C3 now cite F4 and T18.
   6. "Rentals" is now singular.
   7. $5,601.58 is described as the claimed Repair Order lines, not the Repair Order.
3. The checker now reads the letter's own "Date:" line for day counts (LETTER_DATE, DOWN_TIME_START).

**2026-10-31 20:58 v8:** current letter is `output/platform_reply_draft_2026-10-31_205821.txt`.
1. The user wants times to the second wherever possible. Email times now carry seconds from the email headers, in Mountain Time (the PC's time zone is Mountain).
2. The A14 text to Luke (11:29 PM) and the A13 screenshots have no seconds, so they stay to the minute.
3. Box upload times are minute-only, in UTC: 03:45 to 03:47 UTC on 09-30, which is 9:45 to 9:47 PM MDT on 09-29.
4. Header times for reference:
   1. B2: 09-12 23:55:41, sent from the user's hotmail.
   2. A6: 09-13 00:54:26.
   3. A5 Dillon: 09-13 02:46:46.
   4. A7 payout: 09-14 00:01:00.
   5. A4: 09-11 09:20:57.
   6. Renter's booking message: 09-10 22:38:11.
   7. B1: 09-04 11:49:49.
   8. SxS emails: 10-17 15:34:17, 10-19 11:36:55 and 10-29 11:50:47.
   9. Our letters: 10-17 16:12:44 and 10-20 19:02:14.
5. Checker M13 now FAILs a time given to the second that doesn't match its evidence folder's second.

**2026-10-31 21:23 v9:** current letter is `output/platform_reply_draft_2026-10-31_212332.txt` (in the Outlook draft, not sent). This was the final consistency pass. Fixes:
1. The $40 was deducted from the $200 booking, not from the $160 (Part I.2, C7).
2. New VIII.9(d): fees charged to the Renter belong to SxS, not to the owner.
3. Neither proposal applies a deductible (checked both PDFs), so IX.1(b) now says "exclusions, betterment scale, loss of use cap".
4. VIII.1 no longer says "most of the balance"; $1,555.71 of $3,527.92 is 44%.
5. The second day's basis is Part VII, not T15/T16.
6. "Changed three times" became "changed with each review".
7. Added [sic] to "turned to quickly".
8. B2 is described as sent from hotmail.
9. XII.2 now refers to Part I items 1 and 2.

**2026-10-31 21:29 v10:** current letter is `output/platform_reply_draft_2026-10-31_212914.txt` (in the Outlook draft, not sent).
1. The $40 is SxS's Owner Service Fee (20% of Vehicle Fees), shown on A7 and A4 as "Side By Side Share fee -40.00".
2. Part III.3 now explains what the fee is, why SxS applied it, why it doesn't apply, and when it matters. It matters only if loss of use stays at one booking; at $750 it drops out.
3. New Schedule A entry T25 (Service Fees).
4. Part III.1(d)-(f) rejects the "good-faith accommodation" label: the payment is owed under T15, good faith is a duty under T19 and Florida's implied covenant (T23). The letter asks SxS to state the payment as loss of use under T15.
5. The user says TWO further rentals were lost. Only 6aa41c4d is on the platform; Sept 22 exists only in the private texts. The user chose GENERIC wording: "lost further rentals while it stood in the shop", claimed as T16 down time. Never name Sept 22 or the customer.
6. The checker now accepts any T number that exists in Schedule A.

**2026-10-31 21:31 v11:** current letter is `output/platform_reply_draft_2026-10-31_213149.txt` (in the Outlook draft, not sent). Final check passed with 0 FAIL. It now says "owed under T15" throughout, and III.3(d) cites T25 to show the fee is taken "within 24 hours of when the Renter arrives"; for 6aa41c4d no renter arrived.

**SENT 2026-10-31 21:35:09 MT**, from dimaskusllc to admin@sidebysideshare.com, CC hotmail (received 21:35:17 with B1 and B2 intact).
1. Record: `evidence/emails/2026-10-31_213509_dimaskusllc_SENT_RE_Final_Claim_Resolution_notice_of_dispute/`.
2. Text: `output/platform_reply_final_2026-10-31_213509.txt`.
3. Not committed yet: the fact-check scripts, the 10-29 evidence and the sent folder are untracked on branch atv-accident.
4. RESPONSE DUE Mon 2026-11-02 17:00 MT. If there is no answer, every request is treated as declined: pursue the Renter (demand letter, then Utah small claims) and FairClaims arbitration against SxS (Part XII.5).
5. The user still owes the Karl Malone cargo box quote, and should ask the shop to check the LH radiator support for bending, the frame and mounts, steering and alignment, and oil in the air intake.

**Why:** the user wants to recover the full loss from the renter via the platform, or in court if needed. Related: [[project_ticketprocessing_mesa_court]], [[feedback_legal_letter_style]].
**How to apply:** check joshua.a.zayne@hotmail.com for SxS's reply before 2026-10-30; save it under evidence/emails and answer it the same point-by-point way.

**SxS REPLIED 2026-11-03 09:30:04** (sent 09:29:22; saved `evidence/emails/2026-11-03_093004_joshua.a.zayne_Re_Final_Claim_Resolution_SxS_reply/`, message.txt built from body.txt). $3,023.66 "remains our final offer", sign "without alterations", send a mailing address for a check. NEW grounds: (1) "$55 Venmo payment" for rental equipment, citing User Conduct "outside the platform to circumvent fees or rules"; (2) no completed vehicle inspection form or service receipts, citing the 2026-02-10 onboarding email; (3) XTP/Outlander swap "would ordinarily be declined". Silent on the second day, loss of use, Schedule C, mediation and all 16 information requests.

**2026-11-04 00:50 rebuttal DRAFTED (not sent):** `output/platform_reply_draft_2026-11-04_005014.txt`; deadline Thu 2026-11-05 17:00 MT; adds T26 to T35, F7 to F10, attachments D1 to D5 (D1 Return Form p2 = `evidence/forms_filled_2026-09-11/form_page_10.png`, D2 p1 = form_page_09, D3 Pre-Booking Checklist = form_page_06 to 08, D4 = 09-10 22:38:10 booking email, D5 = 02-10 16:40:52 "Call Notes & Listing Link", now saved in evidence/emails). Key facts:
1. The $55 was for a helmet and a ramp, written by the user on SxS's Return Form p2 "Total Post-Booking Fee" line ("PAID VIA VENMO Helmet RAMP 55"), signed by both, under SxS's printed "For post-booking adjustments under ~$50.00, we encourage both parties to settle these amounts directly". It went to SxS in the 32 MB forms PDF "Conner C- XMR  10 sep 2026 .pdf" attached to the 09-12 23:55:41 hotmail email (B2), before the claim opened.
2. Risks NOT put in the letter: the 02-10 email says Luke set up add-ons on the XTP listing (bring back dirty, patch kit, tow kit, guided tour) and asked for the inspection form "before that first booking ... every 180 days or so"; the Pre-Booking Checklist says new hosts should complete the Vehicle Inspection Form. Unknown whether the user ever submitted it, and whether either listing offered a helmet or ramp add-on.
3. Letter refuses to sign the unaltered "full and final" page; if no answer, FairClaims (T22) and the Renter in Utah small claims.
4. fact_check_letter.py M15 now allows "Venmo" only on a line tied to the $55 helmet/ramp/Return Form (still FAILs with delivery, trailer, $125, $35, Josh S). Remaining checker FAILs on this draft are known limits (handwriting, attachment filename, "90 days" read as a day count, $274.98 and $10,600 = 53 x $200).

**2026-11-04 01:02 LEGAL restructure (CURRENT, not sent):** at the user's request the rebuttal was rebuilt in the format of the Thicket Hill "Request for Mutual Termination" PDF sent to Highland 2026-11-02 (see [[project_thicket_hill_oct2026_status]]): letterhead/addressee (Two Steps Twice LLC d/b/a Side By Side Share), defined terms incl. Business Day / Decision Deadline (Thu 2026-11-05 5 p.m. MT), I Requested Action, II Statement of Facts 1 to 16, III Governing Provisions (T and F numbers kept from the Oct 31 letter, all quoted), IV.A to F analysis (position / Response / Supporting record), V Proposed Resolution, VI Deadlines and Down Time, VII Communications, VIII Other Matters, IX No Accord and Satisfaction / Reservation / Preservation / Dispute Resolution, X Summary of Requests, Exhibits (A1 to A15, B1, B2, C, D1 to D6), Attachment 1 Collection Instruction and Response Form. Text: `output/platform_rebuttal_LEGAL_draft_2026-11-04_011500.txt`; PDF: `output/platform_rebuttal_LEGAL_draft_2026-11-04_011500_PDF_2026-11-04_010251.pdf` (21 pages). New typesetter `build_letter_pdf.py` (reportlab; .txt stays the source the fact checker reads; `--footer` text + Page X of Y). The 00:50 draft is superseded. Nothing committed.
