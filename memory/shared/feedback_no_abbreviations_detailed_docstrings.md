---
name: feedback-no-abbreviations-detailed-docstrings
description: "PERMANENT code style: no abbreviated names anywhere (variables, parameters, functions), and every def/class gets a detailed ''' docstring with what it does, what it calls, step by step loops and counts, and a plain-English section for a non-coder"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 50972bbb-ca99-4034-a47a-8b5a30113f40
  modified: 2026-10-16T01:01:22.160Z
---

Two permanent rules for ALL code written for the user (stated 2026-10-15, VA_SelfAssessment repo, "now for memory permenantly"):

1. **No abbreviations in names.** Variables, parameters, loop variables, functions and classes use whole words: `settings` not `st`, `message` not `m`, `index` not `i`, `facility` not `fac`, `request` not `req`, `count` not `cnt`, `temporary_folder` not `tmp`. Standard acronyms that ARE the normal name of a thing are allowed (pdf, csv, html, url, json, xml, sql, http, id, ip, api, utc) plus the user's domain acronyms (fed, pid, nap, coo, visn, tms, leaf, ccc, sat, bisl, rtc, cid).
2. **Every def and class gets a detailed docstring in ''' '''** with these sections:
   - WHAT IT DOES (technical)
   - INPUTS / RETURNS (or HOLDS for a class)
   - CALLS (which other functions it uses)
   - STEP BY STEP (each step; what each loop iterates over, how many times, what it counts)
   - PLAIN ENGLISH (so a non-coder understands what it does and why)

**Why:** the user is not a coder and reads and edits this code himself (copied into VS Code at the VA); short names and thin comments make it impossible to follow. Builds on [[feedback_explanatory_comments]].

**How to apply:** write new code this way from the start; when touching an existing repo for the user, bring the touched code up to both rules. In VA_SelfAssessment a style test (tests/test_code_style.py) enforces both rules; keep it passing.
