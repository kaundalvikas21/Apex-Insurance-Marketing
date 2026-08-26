# Page override: Final Expense Insurance hub (`/final-expense-insurance/`)
Inherits `design-system/MASTER.md`. The exemptions here override the Master wherever they conflict.

- **Audience:** 60 to 85. Senior accessibility is conversion work. `<html class="fe">`.
- **Type:** Inter throughout, nothing in `main` below 18px, tap targets 56px (buttons) and 48px
  (row buttons). Verified in the browser: zero text nodes under 18px at 375, 768, 1024, 1440.
- **Motion:** opacity reveal only. No `.glow`, no `.bento`, no `data-count`, no `data-stagger`,
  no row cascade, no card lift, no chart. Static, calm, large.
- **CTA weighting:** phone first. `.btn-call.btn-xl` above the fold, repeated in a navy
  `call_band()` after sections 4, 6, and 8. The four-field form is the secondary panel.
- **Tables, three columns maximum.** Cost by age is `Age | $10,000 | $25,000` with the row-level
  call CTA inside the age cell (the spec requires it per row; the brief caps columns at three).
  The three-product comparison is `Final expense | Term life | Whole life` with each fact as a
  `th[colspan="3"]` group row above its three cells.
- **Coverage scale:** rounded track in bright blue, three plain cards beneath.
- Layout families in order: hero + panel, strip, card + scale, table, split + card, navy band,
  card trio, table, navy band, split + list, card grid, navy band, tile grid, accordion, byline,
  split + panel. Eyebrow budget 4, used 0.
