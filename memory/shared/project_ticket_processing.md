---
name: project_ticket_processing
description: "TicketProcessing private repo - CO summons dict, Grand Junction traffic-attorney finder (OARC license/discipline + Reddit API), footage request generator; court 2026-10-30 8:15"
metadata:
  type: project
---

Private repo github.com/JoshuaZayne/TicketProcessing at `F:\GitHub Repos\TicketProcessing` (created 2026-10-04).
- `ticket_data.py` `TICKET` nested dict for a CSP summons (Mesa County, road 170 MP 21, 2026 Ram 3500, $174.50). Still None: citation_number, time_of_violation, violation_charged, trooper_name/badge.
- `find_attorneys.py` -> output/attorneys.xlsx/.md. OARC lookup (coloradolegalregulation.com) is a GET-nonce + POST form; detail page by `?Regnum=`. Reddit needs user's own API key in .env (reddit.com and AI web tools are blocked). Dan Shipp has a 1990 2-month suspension.
- `footage_request.py` builds the DA pro-se discovery email (notarized form, DArecords@mesacounty.us) and CSP GovQA portal text.
- Expanded 2026-10-04 to 21 Western Slope + statewide lawyers (region tiers). Win rate: `court_data_request.py` writes a CJD 05-01 sec 4.40 Addendum A request (courtdatarequests@judicial.state.co.us; T and R case classes releasable incl. attorney, agency, charges, findings, scheduled events); `attorneys/outcomes.py` scores CSVs in gitignored data/court_outcomes/ (Addendum A forbids putting data online). Trooper badge 1579 (name spelling unconfirmed, "Coontt?"), CSP Troop 4A Fruita.
- Officer no-show at FINAL hearing = dismissal with prejudice, C.R.C.I. 10(a); 6-month rule 10(b); counsel may appear for defendant 7(b). 40-day pay window likely lapsed ~2026-10-02. See docs/LEGAL_GUIDE.md.
- `count_dockets.py`: court docket export (coloradojudicial.gov/dockets/export, params attorneyBarNumber, caseClass T/R, courtType=C REQUIRED, courtLocations[0]) is today-forward only (~6 mo; past = HTTP 204) and has no attorney column, so it is queried per bar number. 2026-10-04 Mesa leaders: Acker 13, Tyler 8, Rubinstein/Luna/Nolan 5.
- `agy/` = a parallel Antigravity pipeline (keeps changing; commit only own paths, never `git add -A`) that appeared mid-session; unreviewed by Claude.

**Why:** User is deciding whether to hire a Mesa County traffic lawyer and wants the stop video.
**How to apply:** Court is Mesa County Court, Grand Junction, **2026-10-30 at 8:15**. There is no free "win rate" source (docket search shows only future hearings). User typed repo name "TitcketProcessing"; created as TicketProcessing.
- 2026-10-04 15:12-15:19 the user emailed 13 lawyers from **joshua.a.zayne@hotmail.com** (Outlook Classic); logged in `attorneys/outreach.py` (EMAILED/REPLIES), which feeds the spreadsheet's Emailed column. Not emailed: Acker (form only), Martin, Knifer, McElyea, Smith, Distefano, Ditlow, Troxell, Hernandez. Outlook COM works again (all stores open) but needs `SendAndReceive` before Sent shows new mail.
