---
name: CodeMapping_Brain aliases
description: Informal names the user uses for the CodeMapping_Brain repo (codemap, basemap, code map, brain map, etc.) and where it lives
type: reference
originSessionId: b4871434-c3ba-49a8-96d1-792014744b2e
---
When the user says any of "codemap", "code map", "basemap" (in a non-GIS context), "code mapping", "brain map", "map repo", or asks for "the markdown/requirements file that lists all my repos and agents", they mean:

`C:\Users\ohjos\repos\CodeMapping_Brain\`

What it is: master cross-machine catalog (Obsidian vault + Quartz site) of every repo, agent, skill, memory entry, course, domain, and machine. 85 cross-linked markdown nodes under `content/`.

Key files to look at first:
- `README.md`: project overview, pipeline phases, multi-machine layout
- `content/MAP.md`: single-page tour of every node
- `content/index.md`: Quartz homepage
- `build_nodes.py`: data tables for repos / agents / skills / memory / courses / domains
- `run_all.py`: full discovery + similarity + augment + tailor pipeline

How to view:
- Obsidian: open `content/` as a vault, use graph view
- Quartz HTML: `npm i` once, then `npx quartz build --serve` (http://localhost:8080)

If "basemap" comes up in a GIS / Folium / matplotlib context, that's a different thing — disambiguate before assuming.
