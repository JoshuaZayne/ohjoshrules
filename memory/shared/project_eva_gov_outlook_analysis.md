---
name: project-eva-gov-outlook-analysis
description: EmailSearchandCleanup/domain_search scripts that pull all Outlook mail to/from/cc a domain (default eva.gov) and report topics + requests
metadata:
  type: project
---

~/repos/EmailSearchandCleanup/domain_search/: run.ps1 -> 01_extract_domain_mail.ps1 (Classic Outlook COM, JSON) -> 02_analyze.py (report_*.md + requests_*.csv in output/). Domain param default va.gov (there is no eva.gov mail: sender is eva@va.gov, VA VR&E e-VA). Pass comma lists; script splits them because -File passes one string. Roadmap: ~/repos/CodeMapping_Brain/content/roadmaps/2026-09-18_215128_eva-gov-outlook-analysis.md

**Why:** user wants to know topics and what eva.gov contacts have requested of them.
**How to apply:** rerun with -Domains to widen; related to [[project_emailsearchandcleanup]].

First real run 2026-09-19: 251 msgs involve eva@va.gov. Open asks as of 2026-09-17: sign/return VAF 10-5345, monthly job log 20+ apps for EAA payments, e-VA job search questionnaire.
