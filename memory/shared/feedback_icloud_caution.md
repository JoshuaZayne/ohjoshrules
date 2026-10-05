---
name: iCloud caution
description: iCloud syncs across multiple computers with different paths — avoid direct access, use repo copies instead
type: feedback
---

Avoid touching iCloud files directly. iCloud syncs across multiple computers so:
- File paths differ per machine (e.g., `~/iCloudDrive/` on this PC, different on others)
- Direct symlinks to iCloud break on other machines
- Cloud sync causes errors when files are accessed too frequently

**Why:** Multiple computers touch iCloud. Direct references to iCloud paths will only work on one machine and cause sync/path errors on others.

**How to apply:**
- Set everything up in the repo first
- Only touch iCloud once to copy files INTO the repo
- Use a single reference file (like COURSE_BRIDGE.md) to document where iCloud originals live
- Never create symlinks pointing to iCloud
- If referencing iCloud paths in docs, note which machine they apply to
