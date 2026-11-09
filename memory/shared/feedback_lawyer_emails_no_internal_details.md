---
name: feedback_lawyer_emails_no_internal_details
description: "emails to lawyers: say only what they need; never explain our tooling, scripts, files or delivery problems"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2edaab43-0968-4b37-b12b-0e3dca580b74
  modified: 2026-11-09T19:32:16.000Z
---

Emails written for the user to lawyers (or any outside party) carry only what the recipient needs: the request, the facts, the attachments. Never explain how the material was made or why something was resent: no mention of scripts, report websites, AI, file formats, spam filters or Gmail blocks.

**Why:** on 2026-11-09 Gmail blocked the first part of the counsel package to Frank Fleming because the zip held a report website's .js files. I rebuilt it without them and the resent email told him "My first copy of part 1 was blocked by Gmail because the package included a small interactive report website with script files". The user: "WHY THE FUCK WOULD WE EXPLAIN THE SCRIPTS TO HIM?" One lawyer (Pikl) had already said he avoids clients who used AI, so revealing tooling can cost the user credibility.

**How to apply:**
1. A resend says at most "Here is part 1 again." Nothing about why.
2. Before any email goes out, cut every sentence about our process; if a sentence would only matter to us, it does not go in.
3. Strip script and tooling files (.js, report_site, analysis internals) from packages sent to counsel before drafting, not after a bounce.

Related: [[feedback_no_auto_reply]], [[project_attorney_outreach_responses]].
