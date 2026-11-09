---
name: feedback_outlook_com_send_rate
description: "suspended after ~40 emails at 5 s; keep 60+ s apart, small batches"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2edaab43-0968-4b37-b12b-0e3dca580b74
  modified: 2026-11-07T13:44:43.044Z
---

**Summary moved from the memory index (2026-11-08):** Bulk email from joshua.a.zayne@hotmail.com: Outlook.com SUSPENDED sending after ~40 emails when spacing dropped to 5 seconds (2026-11-07); keep 60+ seconds apart and small batches

On 2026-11-07 the attorney outreach (scripts/send_attorney_inquiries.ps1, Microsoft Graph) sent about 20 emails at 30 second spacing without trouble, then the user asked for one per second; I advised 5 seconds instead, and after roughly 20 more at 5 seconds (each with 4 to 5 recipients, near identical text to outside addresses) Outlook.com returned 403 ErrorAccountSuspend: "Account suspended. Follow the instructions in your Inbox to verify your account." 14 sends failed and the user's main email account was blocked in the middle of a legal deadline week.

**Why:** consumer Outlook.com accounts flag rapid bursts of similar outbound mail as spam; the threshold is unpublished and lower than it looks. Graph throughput was never the limit.

**How to apply:**
1. For any bulk send from a personal Outlook.com or hotmail account, use a RANDOM gap between messages. The user first set 30 to 45 seconds, then (2026-11-07, later the same morning) "have the random email sent be from 5-55 seconds"; scripts/send_attorney_inquiries.ps1 now defaults to -MinPauseSeconds 5 -MaxPauseSeconds 55 (average about 30), stops after 2 failures (send errors plus bounces, logged from postmaster notices), skips any address already in Sent Items unless named in -AllowResendTo, and takes -Exclude for broken inboxes. Keep CC lists short.
2. If the user asks for faster sending, explain this suspension and do not go below 30 seconds; never 1 to 5 seconds.
3. On ErrorAccountSuspend, stop immediately (do not retry, do not ask for a new sign-in in a loop); the user must verify the account at outlook.live.com (instructions in the Inbox) before anything else.
4. The send log (documents/attorney_outreach_log.csv in ThicketHillProperty) marks failures as errors, so a later run resends only those, once.

Related: [[feedback_outlook_drafts_recipe]], [[project_thicket_hill_oct2026_status]].
