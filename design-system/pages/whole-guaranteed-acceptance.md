# /whole-life-insurance/guaranteed-acceptance/

Deviations from MASTER.md. Everything not listed here is inherited.

**Phone first, inside a silo that is otherwise at parity.** The whole life silo puts the form and
the phone at equal weight. This page and `/whole-life-insurance/for-seniors/` are the two
exceptions the spec names, and the reason here is different from the seniors page: the visitor has
usually already been declined somewhere, and the only useful next step is a person telling them
whether they need this product at all. A five field form cannot ask that, and getting it wrong is
expensive for the visitor rather than for us. So the hero CTA is `.btn-call.btn-xl`, the mid page
`chrome.inline_cta()` is `phone_first=True`, and the rate chart uses `row_cta="call"`.

**`#who-it-is-for` is a contract.** The whole life hub's "If you cannot qualify" card deep-links to
it. It is an `sr-only` div placed immediately **above** the `chrome.prose()` call, never below it,
or the jump lands past the heading. `check.py` strips fragments when it crawls links, so nothing
will catch this if the id is renamed: see REPLACE-BEFORE-LAUNCH.md section 6.

**Consolidation ready, and the comment renders into the HTML.** The page overlaps deliberately
with `/whole-life-insurance/for-seniors/`, with the final expense silo, and with
`/final-expense-insurance/no-waiting-period/`. That overlap was flagged in the brief rather than
discovered later. The `[CONSOLIDATION READY]` comment at the top of `body()` names the intended
301 target and says which section moves if the page is folded. Same pattern as
`compare_whole_vs_ul.py`'s gate comment, with one difference: this page is **not** held back from
the sitemap, because eight built pages link to it and it answers a real query today.

**The waiting period table carries no `$--` and no rate flag.** It is a behaviour table, not a
price table: MASTER.md section 6 rule 6. Two columns, describing what the contract pays in each
window. The price table further down is a separate object and carries both the flag and the dated
pill.

**Two photographs, both away from the tables.** Hero (`whole-acceptance`, the page's one eager
image) and one `chrome.prose()` `media=` figure on the opening section. Nothing sits beside the
waiting period table, the rate chart, the spoke grid, the FAQ, or the byline.

**"When not to buy this" is four `chrome.step()` rows and must not be shortened.** It is the
section the page exists to carry. An agent who leads with this product is the failure mode named
in the copy, and the page has to be willing to say so at length or the rest of it does not read as
honest.
