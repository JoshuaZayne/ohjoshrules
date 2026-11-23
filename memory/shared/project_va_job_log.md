---
name: project_va_job_log
description: "VA VR&E monthly job log (EAA payments): VA_JobLog repo, month picker bat, never-say-got-a-job rule, offer rows held back, follow ups only from what the user enters"
metadata:
  node_type: memory
  type: project
  originSessionId: 9447959a-e2fd-4653-b666-82c17f5f9cae
  modified: 2026-11-23T08:42:37.986Z
---

**What the VA wants (email "Job Log Requirements for Employment Assistance Awards (EAA) Payments", eVA <eva@va.gov>, signed Michael Johnson, Employment Specialist, VBA VR&E; in joshua.a.zayne@hotmail.com Inbox, 2026-09-17 and 2026-10-07):** a job log every month, at least 20 applications, each with date applied, employer, phone, position, method of application, point of contact, outcome. Attached form "Job Log.docx" is titled JOB SEARCH ACTIVITY RECORD (7 columns).

**Repo (made 2026-11-23 at the user's request, local only, NOT pushed to GitHub, first commit 6496a3b on main):** `F:\GitHub Repos\VA_JobLog`. Code in `_src\job_applications\` (moved out of the resumes repo, which is now only read for resume folder matching; pointer note left in resumes `_src`). Double click `build_va_job_log.bat`: lists months with counts, asks which months, writes `output\va_job_log\<timestamp>\` with `by_month\`, one combined form, `REVIEW_ONLY_not_for_VA_...xlsx`, `job_log_rows_...csv`, `changes_since_previous_run_...txt`, `follow_up_worksheet_...csv`; appends `output\va_job_log\run_history.csv`. Options: `--months 2026-09 2026-10` or `2026-05 to 2026-11`, `--all`, `--list`, `--refresh-outlook`, `--start`. `output\` is gitignored (private email text). Tests: `python -m pytest tests -q` (14 pass).

**User rule (2026-11-23, their words: "do NOT ever ever put we got a job. just say pending etc. NEVER SAY WE GOT A JOB"):** the Result column only says pending, awaiting response, or not selected; a code guard and a test enforce it.
**My handling, told to the user:** an application whose emails show an offer is NOT relabelled pending or not selected. It is left off the form and listed on the "Held Back" sheet. Held: University of Utah TA offer letter (2025-07), Mercor Sales Agents work offer (2025-12), MooMoo VP Trading Surveillance (2026-02, user's own "Offer Letter Status" email), Mercor Evaluator offer accepted (2026-08). User has not said what to do with these.

**Follow ups (2026-11-23):** the user asked to re-enter May to December 2025 applications into January-to-now months as follow ups or reapplies so months average over 50, then said they had made the follow ups in January by phone or DM. I declined to generate those rows: there is no record of them, so I would be choosing dates, methods and results myself on a form tied to a VA payment. What exists instead: a "Followed Up (dates, how)" column on the form fed only by `content\job_applications\follow_ups.csv` (the user types it; each build writes a worksheet to fill), and `manual_contacts.csv` for contacts the user made that leave no email. Do not auto fill either file.

**State on 2026-11-23 01:42 MST:** 1,080 applications on the form since 2025-05, 11 held back. Months under 20: 2026-03 to 2026-09 (September 2026 has 10); October 2026 has 25; nothing after 2026-10-15.
**Why nothing after 10-15:** Classic Outlook has not synced joshua.a.zayne@gmail.com (where nearly all receipts land) since 2026-10-15 17:28, IMAP error 800CCCD2 on Inbox (dimaskusllc@gmail.com the same since 2026-09-20). The claude.ai Gmail connector is the spouse's mailbox, and gmailAPIManager has no credentials. Fix paths: repair that account in Outlook, or drop LinkedIn's data export `Job Applications.csv` into `output\job_applications\linkedin_export\`.

**Gotchas found:**
1. `scan_outlook_jobs.ps1` returned 0 emails until "ReceivedTime" and "SenderName" were added as table columns; it now refuses to overwrite a good scan with an empty one and keeps rollback copies.
2. `normalize_company_key` matched "futu" inside "future" (PayFuture, FMX Futures Exchange became MooMoo). Fixed with a word boundary.
3. The scanner ranks a rejection above an offer, so every email of an application is checked for offer wording.
4. The VA template's table is a floating table stored before the title lines; strip `w:tblpPr` and reorder.
5. Classic Outlook date filters here are day/month order; only use 01/01/YYYY style bounds.
6. LinkedIn has no API for a member's applied jobs; use the account data export.
7. Phone and named contact are empty for online applications; optional `employer_contacts.csv`.

See [[project_resume_builder]], [[reference_check_email_outlook_com]].
