# /compare/*

Deviations from MASTER.md shared by every page built on T5 (`tools/pages/compare.py`).
Everything not listed here is inherited.

**Neutral. No silo owns a compare page.** `SILO = "compare"` and `ACTIVE = "/"`, so no nav item
takes `aria-current` and every GA4 event from these pages is attributable without being attributed
to a product. This neutrality is what makes a compare page the one legal cross-silo route under spec
section 07 rule 3, and it is a compliance property rather than a stylistic one.

**Both two-path buttons are `.btn-cta`.** Giving one product the amber and the other a ghost outline
on a page titled "X vs Y" is a recommendation disguised as a layout decision, and readers can tell.
If a future page genuinely needs to recommend one side, it is not a compare page.

**The breadcrumb's middle crumb is unlinked.** `[("Home", "/"), ("Compare", None), (title, None)]`.
There is no `/compare/` index page, and `chrome.crumbs()` renders an unlinked intermediate crumb as
plain text with `aria-current` reserved for the last one. Do not invent an index page to make the
crumb clickable.

**The answer is in the hero lead, in three sentences**, before the table. A reader who bounces after
the first paragraph should still leave with the answer. The lead also carries the mandated hub
up-link where one silo is clearly the reader's origin.

**The table is the signature object and there is only one.** `.compare-table` inside
`.table-scroll.table-signature`, with `.reveal` on the scroll container itself and never on a
wrapper. A row passed with an empty cell list renders as a `th[colspan]` group row, which is how a
long table keeps its section breaks inside itself rather than being split into several tables.

**`compare.two_path()` cards carry no eyebrow.** The card already has an h3 and a labelled button;
a third label for the same thing put these pages at four eyebrows against a house ceiling of three.
The h3 keeps the differentiator, the product name goes in the button where it is the action.

**The "where each one wins" grid is two `.bento-3` cells, blue and tinted.** Two cells, not three:
the table is already the page's dense object and a second six-cell grid competes with it.

**Cost sections state the shape and refuse to invent the numbers.** Both current compare pages
explicitly say why they are not printing a figure. Where a real number exists it is linked to the
silo's own `$--` rate page rather than reprinted, which also serves spec section 07 rule 7.

## `/compare/whole-life-vs-universal-life/` only

**Built, but held back from publication.** Spec section 05 makes it conditional on Apex being able
to place universal life. Until that is confirmed it is in `SITEMAP_EXCLUDE` in `tools/build.py`,
nothing on the site links to it, its universal life CTA points at `/contact/`, and
`tools/pages/compare_whole_vs_ul.py` carries a `[CONFIRM UL CARRIER APPOINTMENTS BEFORE PUBLISHING]`
comment that renders into the built HTML. All four of those are one change, not four; see
`REPLACE-BEFORE-LAUNCH.md` section 7.

**No dollar figure anywhere.** Universal life outcomes depend on a credited rate and a cost of
insurance schedule we hold no rate cards for. An illustrative number would be a projection printed
in the same typeface as a guarantee, which is the exact failure this page is warning readers about.
