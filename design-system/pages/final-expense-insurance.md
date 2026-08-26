# Page override: Final Expense Insurance (/final-expense-insurance/)
Inherits design-system/MASTER.md. The exemptions here override the Master wherever they conflict.

- Audience 60 to 85. `<html class="fe">`. DESIGN_VARIANCE 3: standard centred layout, large calm
  type, Fraunces headings at pulled-back sizes, body 19px, nothing under 18px inside `main`
  (including the state select), 56px buttons and inputs, 28px consent checkbox, inline links with
  a 48px hit area.
- Phone first: `btn-call btn-xl` orange with an Ink label above the fold; the four-field form is
  the secondary panel. Trust rail with the compact byline beneath, carrier row static.
- No kinetic headline, no stack, no marquee, no magnetic pull, no row cascade, no CTA lift, no
  sticky column. Fades only. No eyebrows.
- Phone CTA repeats after sections 4, 6, and 8 as bone bands with 2px Ink rules top and bottom
  and the same huge orange button, not navy bands.
- Tables three columns maximum: the rate table folds the row-level call CTA into the age cell and
  shows two coverage columns; the comparison table uses `rowgroup` label rows.
- The one navy section is the final phone + form section; the form panel stays white on it.
- Layout families in order: split hero + rail / scale card / table / split + card / call band /
  card trio / table / call band / split + list / card grid / call band / tile grid / split
  accordion / byline card / navy split + panel.
- Eyebrow budget 5, used 0.
