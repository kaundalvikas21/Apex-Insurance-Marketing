# Page override: Final Expense hub (`/final-expense-insurance/`)

Inherits `design-system/MASTER.md`. These overrides win over everything else on this page.

- **Type:** `html.fe` bumps the ramp on `main` so nothing renders below 18px. **Montserrat
  throughout**, the H1 is the only serif. No italic line on this page.
- **Targets:** 56px minimum on every button, input, chip, and accordion summary.
- **Motion:** fades only. No translate, no scale, no stagger, no lift, no row cascade.
- **CTA weighting (spec 09):** phone first. `.btn-call.btn-xl` above the fold at every tested
  width, repeated after sections 4, 6, and 8 as `.call-panel` (a lifted card on a sage band with
  the phone button at display size). The third repeat is the page's forest band.
- **Secondary CTA:** four-field single-step form in a `.panel`, hero right column and again at the
  end beside the phone.
- **Coverage scale:** a full-radius sage track with a forest band marking the $8k to $20k range.
- **Rate table rows** carry call buttons, not quote buttons.
- **Contrast:** ink on ivory 9.1:1, forest on ivory 11.5:1, white on forest 12.3:1. Nothing on the
  page relies on taupe for text.
