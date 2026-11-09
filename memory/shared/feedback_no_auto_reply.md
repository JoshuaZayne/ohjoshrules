---
name: feedback_no_auto_reply
description: "never send email replies automatically; drafts wait for the user"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2edaab43-0968-4b37-b12b-0e3dca580b74
  modified: 2026-11-07T14:34:48.120Z
---

**Summary moved from the memory index (2026-11-08):** Never send email replies on the user's behalf automatically; reply tooling must only read, classify and draft, and every reply waits in Drafts for the user

On 2026-11-07, while I was building automatic reply classification for the Highland attorney outreach (ThicketHillProperty scripts/update_replies.py), the user said: "do not auto reply for me". Earlier that morning I had also sent replies to Misty Ventura and Michael Hurst after reading "draft replies to be sent out" as permission.

**Why:** these are legal-matter emails in the user's name; the user wants to review every word before it goes out.

**How to apply:**
1. Reply tooling only reads, classifies and fills workbooks; it never calls a send endpoint (Graph /send, sendMail, Gmail send).
2. Any reply I write goes to Drafts and is opened for the user; send only when the user says "send" for that specific message.
3. "Draft replies" means drafts, not sends.

Related: [[project_attorney_outreach_responses]], [[feedback_outlook_drafts_recipe]].
