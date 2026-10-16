---
name: project_va_self_assessment
description: "VA_SelfAssessment repo (private, F:\\GitHub Repos\\VA_SelfAssessment): VISN 19 BOSS auditor ePerformance self-assessment linter + LEAF CC audit follow up metrics + draft builder, built 2026-10-15"
metadata:
  node_type: memory
  type: project
  originSessionId: 50972bbb-ca99-4034-a47a-8b5a30113f40
  modified: 2026-10-16T05:44:51.271Z
---

The user's day job includes **VISN 19 B.O.S.S. Auditor and Training Specialist** at the VA (SLC). Repo `github.com/JoshuaZayne/VA_SelfAssessment` (PRIVATE) at `F:\GitHub Repos\VA_SelfAssessment`, created 2026-10-15 (commit f556a1b). Run `python -m self_assessment lint|leaf|build|compare|demo`.

Source email: "Writing Self-Assessments VISN 19 DONE BEFORE 10/7/26", from Joshua.Zayne@va.gov to **ohjoshrules@hotmail.com** Inbox (2026-09-08, RE 2026-09-18). It is ALL screenshots: the performance element **Training Compliance (Critical)** with standards Program Administration / Training Guides Compliance / Training Execution (thresholds: Fully Successful at most 3 failures or valid complaints, Exceptional at most 1), plus the VISN 19 writing guide deck. It does **not** contain last year's written narrative, even though the user called it that; the prior text must be pasted from ePerformance into `content/prior_year_self_assessment.txt`.

The user wants the self-assessment to highlight that they started using **LEAF** (Light Electronic Action Framework) for **Community Care (CC) audit follow ups**, which made facility responses faster. Their phrase "increasing the response times" means faster; the linter flags that wording as reversed.

**Tools (added 2026-10-15)** in the same repo, each ONE stdlib-only .py + .bat for the VA work PC (no pip there), output DPAPI-encrypted (.vmi/.bis) with an in-memory localhost viewer; guide at tools/START_HERE.md:
1. tools/va_mail_insights: Outlook scan via pywin32 or embedded PowerShell (-EncodedCommand), sent folders first so bodies are only pulled for my threads; follow ups, response days, LEAF vs email, categories from an editable .ini.
2. tools/bisl_reader (v2 of the BISLWebScraper20260101 repo, copied unchanged to legacy/): the SAT Audit Facility Dashboard at vaww.pbi.cdw.va.gov/PBI_RS is a PAGINATED (SSRS) report, so it uses URL access export (?/path&rs:Format=XML|CSV), REST /api/v2.0 folder listing, SOAP GetItemParameters for the dependent Facility list, and PowerShell Invoke-WebRequest -UseDefaultCredentials for Windows sign-in. The web service virtual dir on the VA server is UNKNOWN; Discover probes candidates. Tested only against tests/bisl_mock_server.py.
3. Mail tool fills the whole write-up (self_assessment_writeup_template.txt) from mail, calendar and the BISL history; BISL Reader has catalog map (report_catalog.csv) and fiscal-year backfill (menu 8). Delivered to the work PC by an Outlook DRAFT (2026-10-15, not sent) with the code inline between ASCII separators; --fingerprint ignores line endings so pasted copies verify. Weekly metric emails mention 'audits', so [detect] not_followup keeps them out of follow ups.
4. Gotcha: configparser read_string(defaults)+read(file) MERGES sections, so deleted facilities/categories came back; list sections are now replaced, not merged.
5. State 2026-10-15 22:45 MDT: commit 2e4c1d7 pushed (third tool tools/reference_tracker; shared block master tools/common/shared_block.py synced by tools/sync_shared.py; tests/test_code_style.py enforces whole-word names and the 5-part ''' docstrings; tools/code_map.py + tests/test_code_map.py fail on duplicate code). 201 tests pass.
6. Another AI tool (likely Antigravity, run by the user) also edits this repo: it added "Round 4" (steps 18 to 22: record_method_log, bundle_code_and_logs, suggest_policy_response, relationship map, path summary) and tests/test_remaining_gaps.py. Its generator writes boilerplate docstrings ("Executes X (handles X)"); check `git status` and file sizes before editing, and rewrite generated docstrings by hand.
8. Number-only logs (commit 388560d, 2026-10-15): every person in every log is a 14-digit token (kind digit, 12 random, Luhn). Key file "Encryption Key.json" on the VA computer's Desktop (VA_TOKEN_KEY_FILE overrides), vault %LOCALAPPDATA%\VA_SelfAssessment\pseudonym_vault.sqlite; only tools/reveal_tokens/reveal_tokens.py with the 30-80 character passphrase reveals. Reports keep real names. Backup = Outlook draft to Joshua.Zayne@va.gov with the key file, NEVER the passphrase. Tests force VA_TOKEN_KEY_FILE to a missing file (tests/conftest.py). Design: CodeMapping_Brain/content/roadmaps/2026-10-15_230026_va-pseudonym-tokens-design.md.
9. 2026-10-16: f4d33cf adds the evaluation bullet by bullet ([evaluation] settings, evidence per duty PA1..TE4). v4 code draft (4 tools) is in ohjoshrules@hotmail.com Drafts, NOT sent, verified by fingerprint; the old v2 draft there is superseded. Only one formal decision tree exists (#COO# wait time); MSE SOP and guidebook 03.4.25 measures are mapped but not built yet.
7. Personal data: the supervisor default in [people] is blank in code (set it in the local gitignored settings .ini); demo/test data use made-up names only. ec939a1 in history still holds the old names (user chose not to rewrite history).

**Why:** numbers must come from the follow up export (`data/cc_audit_followups.csv`, gitignored), never typed in or guessed; unfilled facts stay as [[TODO]].
**How to apply:** pending from the user as of 2026-10-15: prior year text, the CSV, LEAF go live date, real counts. Coworker names go in gitignored `private/names_to_flag.txt`. Roadmap: CodeMapping_Brain/content/roadmaps/2026-10-15_143139_va-self-assessment-builder.md. See [[reference_check_email_outlook_com]].
