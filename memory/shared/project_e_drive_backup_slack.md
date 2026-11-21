---
name: project-e-drive-backup-slack
description: "E: Geek Squad backup drive is 100 percent full; 362 GB of it is exFAT 512 KB cluster slack, plus two corrupt 44 GB image files"
metadata:
  node_type: memory
  type: project
  originSessionId: d02ded55-483e-408b-b7ff-1c90a9ff273f
  modified: 2026-11-21T08:07:11.331Z
---

E: (volume label "GS#16", Samsung PSSD T7 external SSD, 1,863.0 GB) reported 0.00 GB free on 2026-11-21 00:59 MST. Findings from a full enumeration that night:

## What is on it

One folder, `E:\Joshua Zayne 0773-261118-01925`, a Geek Squad style full backup of this machine. The number is the service ticket style identifier. Inside:

1. `F (1TB RAID )\` : 802.52 GB, a copy of the F: drive
2. `User Data\` : 659.09 GB, a copy of the user profile

Totals: 1,461.62 GB of real file content across 824,191 files and 79,482 directories (robocopy listing agreed at 1,569,400,198,408 bytes).

## Why the drive reads full at only 1,461 GB of data

E: is formatted exFAT with a 512 KB allocation unit. C: and F: both use 4 KB. Every file consumes at least one full cluster, and 765,482 of the 824,191 files are smaller than 1 MB.

1. Logical data: 1,461.62 GB
2. Allocated on disk, computed as `ceil(size / 512KB) * 512KB` per file: 1,824.15 GB
3. Slack wasted in files: 362.53 GB
4. Directories, 79,482 at one cluster each: about 38.8 GB
5. 1,824.15 + 38.8 = 1,862.9 GB, against the 1,862.98 GB the volume reports used. The accounting closes exactly.

Reformatting at a 32 KB cluster size would cut file slack from 362.53 GB to roughly 12.58 GB, recovering about 350 GB. That requires copying 1.46 TB off, reformatting, and copying back, so it needs a landing place first. NOTHING HAS BEEN DONE. No files touched, no reformat.

## Two corrupt files, 88 GB together

1. `...\User Data\OneDrive\Pictures\Camera Roll\School\IMG_6098.JPG` : 44.08 GB, created 2026-11-18 21:23:24, content modified 2024-10-14
2. `...\User Data\OneDrive\Pictures\Camera Roll\Screenshots\20240529_195538.jpg` : 44.08 GB, created 2026-11-18 22:55:14, content modified 2024-05-29

A JPG cannot legitimately be 44 GB. Both are byte identical in size and both were created when the backup was written, so these are almost certainly transfer corruption. Not verified by reading headers yet, and not deleted.

The one genuinely large legitimate file is `...\F (1TB RAID )\Media_Archive_2019\GoPro_Fusion_Rendered\VIDEO_0007.mov` at 67.98 GB.

**Why:** the drive is at zero free space, so it cannot take another backup, and more than a fifth of its capacity is recoverable without deleting a single real file.

**How to apply:** before proposing any cleanup, respect [[feedback_no_data_deletion]]: set files aside and keep dated rollback copies rather than deleting. The two 44 GB images should be validated by reading their headers before anything else. A reformat needs 1.46 TB of staging space, which the machine does not currently have free, so stage it or do it in passes. Machine context: [[reference-desktop-hardware-inventory]].
