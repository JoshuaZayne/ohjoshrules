---
name: Harden Claude settings file ACLs
description: User wants ~/.claude/settings.json and settings.local.json locked down so only they can edit
type: feedback
originSessionId: cef13322-9cd7-492f-8a7e-969776f26ab8
---
Lock down `~/.claude/settings.json` and `~/.claude/settings.local.json` with
explicit, non-inherited ACLs: owner + SYSTEM + Administrators full control,
no wider groups (Users, Authenticated Users, Everyone).

**Why:** User is security-conscious about the permissions file and does not
want a drifted parent-folder ACL or an unexpected group membership to let
another process or account rewrite Claude's permission rules silently.

**How to apply:**
- On Windows: `icacls "<path>" /inheritance:r /grant:r "<user>:(F)" "SYSTEM:(F)" "Administrators:(F)"`
- On Linux/Mac equivalent (raspberry pi, etc.): `chmod 600 <path>` and `chown <user>:<user> <path>`
- Apply proactively on any device where the user mentions working with Claude
  Code (desktop, laptop, Raspberry Pi — see user_github_and_devices memory).
- User said "only I can edit" — kept SYSTEM + Administrators for recoverability;
  if user later says strip those too, comply.
