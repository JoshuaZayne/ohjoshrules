---
name: project_thicket_hill_counsel_package
description: "Lawyer zip (scripts/build_counsel_package.py): signed docs folder 03, date-order list, email parts; file 12 redaction rule"
metadata:
  node_type: memory
  type: project
  originSessionId: 7796d438-c338-42cc-a460-53a11d7dffb8
  modified: 2026-11-09T18:36:50.339Z
---

On 2026-11-09 at 11:33 MST the counsel package was rebuilt with every signed document. Build: `Highland_counsel_package_2026-11-09_113343.zip` (146 files, 82.5 MB), plus 11 email-sized parts in `documents/counsel_package/split_for_email_2026-11-09_113343/`. These replace the 11:25 three-part split, which had no signed documents 01 to 17.

Layout: folder 03 holds every signed document in date order (the highlighted waiver guide, Kevin's six, unsigned reference copies, second copies, key pages). Folder 09 holds the HOA CCRs, rules and design gallery terms. Folder 10 holds catalogs and pricing; folder 11 holds lender documents. `00_DOCUMENT_LIST_IN_DATE_ORDER.html` lists every file by date. File names follow number_date_what_who-signed, because the user said chronological naming matters.

**Why:** the builder's privacy scan reads only text. Signed file 12 (VA Certificate of Veteran Status request) has Joshua's service and claim numbers and Kevin's SSN inside scanned images. Only `signed_documents_highland_*/Redacted_For_Sharing/12_*REDACTED*.pdf` may go out.
**How to apply:** rebuild with `python scripts/build_counsel_package.py`; check any new scanned PDF by eye for numbers before adding it. Kevin's page 4 in file 12 shows his name in a signature font dated 9/01/2026, but Adobe's audit shows only Joshua signed. See [[project_thicket_hill_disabled_vet_law]], [[project_attorney_outreach_responses]].
