# Page override: Get a quote (`/get-a-quote/`)
Inherits `design-system/MASTER.md`. Only deviations are listed.

- **Purpose:** the master money page. The form is the page; every section below it answers one objection that stops someone finishing it, in the order the objection occurs.
- **Split hero:** `.panel` form in the right seven columns, H1 and three proof lines in the left five, phone `.card` beneath them. `.glow` on the section. No photograph: nothing on this page is atmospheric, and an image beside a form is a reason to look away from it.
- **Product selector:** step 1 is a `.choice-col` of three `.choice-block` options. `.choice-block` stacks name over description, where the base `.choice` centres a single line. The description uses `.choice-note`, never a `text-muted` utility: utilities outrank the components layer, so a utility colour survives the navy checked fill and leaves slate text on a navy tile. Same reason `.stat-value` is handled by name.
- **Branching:** every branch lives in the DOM at once; `[data-step-for]` fieldsets are `disabled` for the branches not chosen. Term gets three steps, whole life one, final expense one, then a shared final step. Progress segments are authored for the longest branch (four) and stay fully visible until a product is picked, so the bar never grows under the reader.
- **One consent block,** on the shared final step. `initForm()` binds a single `[data-consent]` per form, and one ask immediately above the button actually pressed is also the correct reading of the rule.
- **Radio names are unique per branch** (`term_sex`, `term_tobacco`, `wl_sex`). `validateRadioGroup()` queries the whole form by name, so a shared name attaches the error to whichever fieldset came first in the DOM, which may be a hidden one.
- **Rates:** the sample table sits *below* the form and is not gated. Four columns, `$--` cells, `C.rates_flag()` above and a dated `.pill` beneath. Row buttons prefill age into `#quote-form`.
- **CTA weighting:** form first, phone a genuine second (hero card, step 1 fallback, closing band). This page owns no silo, so neither product's weighting applies.
- Layout families in order: split hero + panel, bento pair, split + steps, card trio, table, split + bento, accordion, navy band. Eyebrow budget 3, used 3.
