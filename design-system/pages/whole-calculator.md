# /whole-life-insurance/calculator/

Deviations from MASTER.md. Everything not listed here is inherited.

**The page title promises a premium and a cash value, and the calculator computes neither.** That is
the deviation, and it is deliberate. A premium needs a carrier rate card and a health class; a cash
value column needs a carrier illustration. We hold neither, and producing them would be the same
fabrication as printing a rate (section 7). So the tool sizes the **permanent need**, and a full
section explains on the page why the other two numbers cannot be produced in a browser. It carries
`[PLACEHOLDER: NO CARRIER RATE CARDS LOADED]`.

**One calculator engine, two ladders.** `site.js` section 10 already implements this arithmetic:
two multiplied terms plus a flat term, minus existing coverage, rounded **up** to a coverage ladder.
Rather than a second implementation, this page reuses it with `data-calc-ladder` and maps the roles
to whole life's questions:

| site.js role | This page's label |
|---|---|
| `debt` | Funeral, final bills, and debts |
| `children` x `perchild` | People you want to leave something to, at an amount each |
| `existing` | Permanent coverage already in force |

`income` and `years` are simply absent from the markup; `num()` returns 0 for a missing field, so
their product drops out of the sum. The role names are the engine's, the visible labels carry the
meaning.

**The ladder must match the quote form.** `[25000, 50000, 100000, 250000, 500000]`, which is exactly
the option set on `whole.quote_form()`'s coverage select. A recommendation off that list would
silently blank the field when the prefill assigns it. `_check()` in the module asserts this at
build time, along with the worked example's arithmetic and the two edge cases (already covered, and
above the top rung).

**Inputs sit outside the form.** As on the term calculator: inside a `<form>`, `collect()` would
validate them and `FormData` would post the visitor's finances to the CRM.

**No eyebrows in the "cannot account for" bento.** Five cells there would have put the page four
over the `ceil(sections / 3)` eyebrow budget, and the headings already name each cell.
