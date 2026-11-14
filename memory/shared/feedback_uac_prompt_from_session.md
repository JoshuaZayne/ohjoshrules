---
name: feedback_uac_prompt_from_session
description: Admin (UAC) prompts started from a Claude session hide behind windows and time out; give the user a self elevating .bat to double click instead
metadata:
  node_type: memory
  type: feedback
  originSessionId: cccc1980-e14d-4fe8-81f6-b5bb02397b42
  modified: 2026-11-14T05:34:38.828Z
---

On the desktop, `Start-Process -Verb RunAs` launched from the Claude session raised a UAC prompt the user could not see ("cant see the yes"); it timed out and nothing ran. The user then asked Claude to click Yes, which is impossible: UAC runs on the secure desktop that no program can control.

**Why:** the session is not admin (IsInRole Administrator = False), and its elevation prompts do not come to the foreground.
**How to apply:** for anything needing admin, write the work as a .ps1 plus a self elevating .bat in the target folder, open the folder in Explorer, and have the user double click the .bat (user started prompts appear in front). Explain up front that Claude cannot click UAC. Example: [[project_desktop_driver_updates]].
