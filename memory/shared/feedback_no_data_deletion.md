---
name: feedback_no_data_deletion
description: "convert to verified Parquet, set rows aside, keep dated rollback copies"
metadata:
  node_type: memory
  type: feedback
  originSessionId: dfe8eb70-bebc-45d2-b981-4703bed5ae51
  modified: 2026-11-07T15:58:35.142Z
---

**Summary moved from the memory index (2026-11-08):** Never delete data if it can be helped: convert text (JSON, CSV, logs) to verified Parquet, set aside removed rows, keep dated rollback copies

Do not delete data when it can be kept. When something must get out of the way, convert it to a smaller format (Parquet with compression) and only remove the original after the copy reads back with the same rows and content; rows a repair or merge removes go to a set aside store; files about to be replaced (binaries, folders) get a dated copy first.

**Why:** the user said on 2026-11-07: "I dont want to delete data if it can be helped" and "converting the data to something smaller like a parquet would be preffered from like a json or csv file rather than deleting completely", then asked for over 50 checks that data is not lost or overwritten.

**How to apply:** in RustTOS this is built in (see [[project_rusttos]]): old logs move to `logs/archive` and become Parquet, check tables are Parquet, the import keeps `data/curve/set_aside/<run>` plus ledgers, and the preservation claim fingerprints every file each run. Apply the same habit in other repos: move aside instead of deleting, ask before any real deletion. Related: [[feedback_verify_external_claims]].
