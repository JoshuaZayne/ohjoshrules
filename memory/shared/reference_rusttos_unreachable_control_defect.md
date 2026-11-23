---
name: reference-rusttos-unreachable-control-defect
description: "RustTOS has a recurring defect class: a control that is DRAWN and in the accessibility tree but cannot be pressed; three instances found, and the test shape that catches it"
metadata:
  node_type: memory
  type: reference
  originSessionId: 1357db99-9ad1-48ec-8f53-a505f7663727
  modified: 2026-11-23T10:46:35.056Z
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
3. **The settings window's Style section, STILL RED since 2026-11-16.** `every_settings_window_control_works_part_03_of_10`,
   ColorWell "Color" number 4. The test's own message names the mechanism: a `Foreground ... .with("popup")` layer is
   on top at the click point, because a colour well in a drop down already lives in a popup layer of its own. Two
   fixes were tried and both reverted: Escape closes the whole Style menu, and clicking the well twice runs before
   the judgement and hides the picker being judged.

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
