---
name: project_thicket_hill_counsel_package
description: "Lawyer zip (scripts/build_counsel_package.py): signed docs folder 03, date-order list, email parts; file 12 redaction rule"
metadata:
  node_type: memory
  type: project
  originSessionId: 7796d438-c338-42cc-a460-53a11d7dffb8
  modified: 2026-11-09T19:19:42.476Z
---

On 2026-11-09 the counsel package was rebuilt with every signed document. The current build is `Highland_counsel_package_2026-11-09_121729.zip` (148 files, 83.5 MB), plus 12 email-sized parts in `documents/counsel_package/split_for_email_2026-11-09_121729/`. It replaces the 11:33 build and the 11:25 three-part split; the 11:25 split had no signed documents 01 to 17.

It adds `12_Documents_to_request.html`, built from DOCUMENT_REQUESTS in the builder: 10 items that only Highland or Highland HomeLoans can supply. Nothing on it had been requested in writing as of 12:17 MST.

Layout: folder 03 holds every signed document in date order (the highlighted waiver guide, Kevin's six, unsigned reference copies, second copies, key pages). Folder 09 holds the HOA CCRs, rules and design gallery terms. Folder 10 holds catalogs and pricing; folder 11 holds lender documents. `00_DOCUMENT_LIST_IN_DATE_ORDER.html` lists every file by date. File names follow number_date_what_who-signed, because the user said chronological naming matters.

**Why:** the builder's privacy scan reads only text. Signed file 12 (VA Certificate of Veteran Status request) has Joshua's service and claim numbers and Kevin's SSN inside scanned images. Only `signed_documents_highland_*/Redacted_For_Sharing/12_*REDACTED*.pdf` may go out.
Redaction lesson (2026-11-09): measure boxes on a render whose pixel size you print (pixmap width and height), never from the image preview, which is scaled. Use search_for on pages that have text. Then check enlarged crops by eye. The first VA 26-1880 copy missed every number because of this.

Receipt search 2026-11-09: no Completed receipt exists for the lender's Solex packages (7/13, 8/13, 8/27, 9/2, 9/15, links at solex.com from docs@highlandhomeloans.com), the 6/29 Flex Gen DocuSign, or the 9/16 Adobe VA 26-1880. The 26-1880 the user downloaded is NOT signed: the Adobe signature page is blank. It is saved under Not_Signed_For_Reference, with a redacted copy.

**How to apply:** rebuild with `python scripts/build_counsel_package.py`; check any new scanned PDF by eye for numbers before adding it. Kevin's page 4 in file 12 shows his name in a signature font dated 9/01/2026, but Adobe's audit shows only Joshua signed. See [[project_thicket_hill_disabled_vet_law]], [[project_attorney_outreach_responses]].
