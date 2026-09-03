# /final-expense-insurance/quotes/ and /final-expense-insurance/cost/

Deviations from MASTER.md shared by the silo's two P1 money pages. Everything not listed here is
inherited, including the whole of the `html.fe` senior mode.

**T1 and T2 are inverted, not adapted.** T1 says the form is the page and T2 puts a prefill button
on every rate row. Both assume a form is the primary action. In this silo it is not: final expense
is phone weighted everywhere and the buyer is 60 to 85. So on `/quotes/` the hero's primary is a
full width `.btn-call.btn-xl` in a `.card`, with `FE.callback_form()` beside it in the `.panel` as
the secondary, and on `/cost/` there is no form on the page at all until the closing ask. Every
other part of both templates is kept, because the objections they answer are the same ones.

**Row level CTA is `row_cta="call"`, never `"prefill"`.** `chrome.rate_chart()`'s call mode puts
the click-to-call inside the age cell rather than in a fourth column, which is the only way these
tables stay inside the three column senior cap. It also means neither page needs a prefill target,
which is why `/cost/` can carry a chart without carrying a form beside it.

**Two coverage columns, `$10,000` and `$25,000`.** That is the band most policies in this category
are written in, and the copy under each chart says explicitly that amounts between and above are
written every day. Do not add a third column to be helpful: three coverage columns plus the age
header is four, and four breaks the cap.

**`/cost/` is the silo's canonical price page.** Six built pages route their cost question here
rather than answering it themselves, which is why it is lean on definitions and dense on price
behaviour. When rate cards land, this is the table to populate first. Nothing else in the silo
duplicates it, and nothing else should.

**Bento grids become plain card grids.** `.bento` with `data-stagger` is a motion pattern and
`.fe main` opts out of motion. Both pages use `grid md:grid-cols-2` or `md:grid-cols-3` of `.card`
instead, with no `.reveal` cascade on the cells. The section still reads as a group; it just does
not animate into one.

**`/quotes/` carries no byline.** T1 does not, and neither does `/term-life-insurance/quotes/`.
`/cost/` does, because it is a page that makes claims about how prices behave and a named reviewer
is part of that claim.

**One photograph each, and never beside a table.** `/quotes/` places `fe-path` on
`post_submit_section(media=)`, which sits two sections above the cost chart. `/cost/` places
`fe-quiet` on the `chrome.prose()` rail of "how to bring a quoted price down", which is below the
chart and above a navy band. Neither page takes a hero photograph: on `/quotes/` the hero holds a
form, and on `/cost/` the section immediately below the hero is a rate table.
