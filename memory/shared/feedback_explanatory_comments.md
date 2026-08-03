---
name: feedback_explanatory_comments
description: User wants very explanatory comments in code they ask me to build out — what the code does AND why it matters
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d31d1692-06ab-404d-a66c-87e7746d1901
  modified: 2026-08-03T00:54:50.934Z
---

When building out new code for the user (scripts, models, pipelines), write **very
explanatory comments**: state what each block does AND why it's important — the
purpose/consequence, not just the mechanics. Module docstrings should explain the
decision the code makes and why it matters to the larger goal; inline comments
should justify non-obvious choices (anti-overfit guards, label design, why a
simpler approach was rejected).

**Why:** The user explicitly asked for this on the RamMegaCabDataScrapper ML tree
builds ("make the comments very explanatory of what the code is going to do, and
why its important"). They value code that teaches the reader the reasoning, not
just the how.

**How to apply:** This OVERRIDES the default "match surrounding comment density"
for code the user asks me to author/build out. Still keep comments accurate and
not redundant with obvious code. Applies to new build-out work; don't go
retrofitting unrelated existing files unless asked. See [[project_ram_megacab_scraper]].
