---
name: reference-rusttos-unreachable-control-defect
description: "RustTOS has a recurring defect class: a control that is DRAWN and in the accessibility tree but cannot be pressed; three instances found, and the test shape that catches it"
metadata:
  node_type: memory
  type: reference
  originSessionId: 1357db99-9ad1-48ec-8f53-a505f7663727
  modified: 2026-11-23T13:24:57.978Z
---

**RustTOS's most common UI defect is a control drawn where a press cannot reach it.** It passes every test that
counts controls or looks them up by name, because the control really is there, in the right place, with the right
label. Only a test that PRESSES through the pointer catches it.

**Three instances found so far, all different mechanisms:**

1. **Active Trader, 2026-11-22.** Its top area is capped at `TOP_SHARE` (0.42) and scrolls, so a control drawn
   below the scroll area's clip looks pressable and is dead. Measured: the clip ended at y 656.2 while "Auto center"
   sat at y 652 to 672. egui gives a click outside a clip to nothing at all, in the real app exactly as in a test.
   Worked around in the tests with `click_in_trader_top` (scroll it in first); NOT fixed in the app.
2. **The chart grid's cell headers, 2026-11-23, FIXED.** The headers were drawn straight into egui's background
   layer, the same layer as all sixteen charts and their own interaction. A press on Expand, Pop out or x was lost on
   3 to 5 of 16 cells on every run, and never at 8 cells or fewer. egui reported `contains_pointer` FALSE on the very
   frame the press arrived, with the pointer provably inside the button's rectangle. Fixed by giving each header its
   own `egui::Area` at `Order::Middle` (commit 7a797525).
3. **The chart's bottom bar, 2026-11-23, FIXED.** `ui.horizontal` ran past the window's edge once a fourth control
   joined the quick measure's buttons, so the new button was drawn and dead. Wrapped, exactly as the symbol header
   already was for the same reason (commit 7ba25789). The test was run against the unwrapped bar and failed with
   `left: (19825.0, 200.0), right: (10.0, 30.0)`, so it really guards the fault.
4. **The hotkey editor's own first layout, 2026-11-23, FIXED before it was committed.** A four column `egui::Grid`
   whose fourth column, holding Bind and Clear, was pushed past the window's right edge. The giveaway: the Clear
   press did nothing and the note still read "saved: 1 key(s) bound". One wrapped row per action instead.
5. **The settings window's Style section, STILL RED since 2026-11-16.**
   `every_settings_window_control_works_part_03_of_10`, ColorWell "Color" number 4 at [420.2 336.0], value
   `#ffffffff` before and after.

**What is ESTABLISHED about that last one, and what is RULED OUT.** Three theories were tested and killed on
2026-11-23; do not spend time on them again:

1. RULED OUT: "a picker left open by the control before it". `use_and_judge` in `button_sweep_tests.rs:863` opens a
   FRESH harness for every control, so nothing a previous control did survives. This is what doomed the second of
   the two earlier reverted attempts.
2. RULED OUT: "the Style MENU's fourth colour well is below a scroll clip". Measured: the Style menu holds exactly
   ONE colour well, at y 654, and its middle is inside the menu's own area rect.
3. RULED OUT as evidence: the test's "a Foreground popup layer was on top at the click point" is EXPECTED, not a
   cover, because the well lives inside a popup already. Reading it as a cover is what led to the first reverted
   attempt, pressing Escape, which closed the whole Style menu.
4. ESTABLISHED: a colour well passes this sweep if its picker merely OPENS, because `only_opens_something()`
   (`button_sweep_tests.rs:259`) is true for `Role::ColorWell`, and the judgement is
   `app_changed || (only_opens_something && screen_changed)`. So the failure means the picker never opened at all.
5. ESTABLISHED: the fourth well is almost certainly `close_tick_color` in `thickness_controls`
   (`dialogs.rs:1834`), whose own comment says the colour "is edited on a copy and stored only on a real change,
   because the button rounds colors just by being drawn". Its default is white, which matches `#ffffffff`.
6. NOT YET MEASURED: the clip rect in force at the click point when the well is reached through the settings
   window. A measurement test that opened the settings window and THEN clicked "Style" hung for 40 minutes and had
   to be killed, so it needs a different route in: enumerate the wells without reopening the Style menu over the
   window.

**How to apply:**
1. A test that counts controls, or finds one by label and asserts it exists, proves NOTHING about whether it works.
   The grid had `query_all_by_label_contains("Pop out (grid chart").count() == 16` passing while 5 of those 16
   buttons were dead.
2. The test shape that catches it: query the node for its rectangle, then press at `rect.center()` through
   `hover_at` + `PointerButton` press and release, and assert the STATE changed. Never `node.click()`, which bypasses
   the hit test and so bypasses the whole defect.
3. Prove a new test of this shape actually bites: restore the file to its broken state and watch it fail. Both grid
   tests were run that way (they named cells 7, 9, 11, 12, 15 and 7, 9, 12, 14, 15).
4. When the hit test is the suspect, instrument the control's own `Response`: print `contains_pointer`, `hovered`,
   `clicked`, `interact_rect` and `ctx.layer_id_at(spot)` on every frame the pointer is inside. That is what named
   the cause in case 2 after geometry, ordering and click timing had all been ruled out.
5. A fresh screen often works where a sequence fails: case 2 passed on every cell with one fresh grid per cell, and
   failed only in a run of ordinary presses. So test the sequence, not just the single press.

Related: [[project_rusttos]], [[reference-rusttos-build-speed-measured]], [[project_rusttos_state_2026-11-22]].
