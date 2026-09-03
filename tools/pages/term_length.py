# -*- coding: utf-8 -*-
"""Shared body for the two term-length spokes (20 year and 30 year).

BUILD LEAN. Spec s10 test 1 flags both pages as unmeasured volume, so they are
built solid but shallow: six sections, no rate table of their own, and every
pricing question routed to /term-life-insurance/rates/ rather than duplicated.
That routing is also the point of a lean page under spec s07 rule 7, which
wants the money pages receiving more links than they send.

The two pages share this builder rather than being two hand written modules,
because they are a matched pair under test. If the volume validates, depth gets
added here once and lands on both. If it does not, folding them into
/term-life-insurance/rates/ is a two file deletion instead of a rewrite.

# ponytail: one builder for two pages. Split it only if the copy genuinely
# diverges, not merely because a third term length shows up.
"""
import chrome as C

VALIDATE_NOTE = """<!-- =====================================================================
     [VALIDATE VOLUME BEFORE INVESTING IN DEPTH]
     Spec section 10, test 1. Search volume for this exact term length is
     unmeasured. This page is deliberately built lean: it answers the
     query and routes pricing to /term-life-insurance/rates/ rather than
     carrying a rate table of its own. Before adding depth here, confirm
     the query has volume that the rates page is not already capturing.
     If it does not, fold this page into the rates page as a section and
     301 the path.
     ================================================================== -->"""


def render(years, h1, lead, fits, dates_intro, dates, cost_note, faq, siblings,
           cta_heading, cta_body, where):
    """One lean term-length page. `fits` is [(eyebrow, title, body)] of exactly
    three, so the bento gets its mandated white / blue / tinted variation."""
    cells = ""
    for i, (eyebrow, title, text) in enumerate(fits):
        variant = ["bento-cell-blue", "", "bento-cell-tint"][i]
        on_navy = i == 0
        cells += f"""
      <div class="reveal bento-cell {variant} bento-2">
        <p class="eyebrow{' text-white/80' if on_navy else ''}">{eyebrow}</p>
        <h3 class="mt-2 text-h4{' text-white' if on_navy else ''}">{title}</h3>
        <p class="mt-3 {'text-white/90' if on_navy else 'text-slate'}">{text}</p>
      </div>"""

    date_rows = "".join(
        (('<div class="mt-8">%s</div>' if i else "%s") % C.step(i + 1, t, b))
        for i, (t, b) in enumerate(dates))

    return f"""
{VALIDATE_NOTE}

{C.page_hero([("Home", "/"), ("Term Life Insurance", "/term-life-insurance/"),
              ("%d year term" % years, None)], h1, lead)}


<!-- Who it fits. Three cells, no more: this page is lean by design. -->
<section class="pb-14 md:pb-16">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Who a {years} year term actually fits</h2>
      <p class="reveal mt-5 text-slate">
        A term length is a guess about how long other people will need your income. These are the
        three situations where {years} years is the right guess rather than the default one.
      </p>
    </div>
    <div class="mt-10 bento" data-stagger="40">{cells}
    </div>
  </div>
</section>


{C.prose("Check it against your own dates", date_rows, intro=dates_intro, cls="section band")}


{C.inline_cta(cta_heading, cta_body, where, "/term-life-insurance/quotes/",
              "Get term life quotes")}


<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">What a {years} year term costs</h2>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <p class="reveal text-slate">{cost_note}</p>
        <p class="reveal mt-5 text-slate">
          Rather than reprint a slice of it here, the full grid lives on one page and is kept
          current in one place: <a class="link" href="/term-life-insurance/rates/">term life
          insurance rates by age</a>, with a term length toggle and a button on every row that
          carries the numbers into a quote form.
        </p>
        <p class="reveal mt-5 text-slate">
          If you are not yet sure of the amount rather than the length, the
          <a class="link" href="/term-life-insurance/calculator/">coverage calculator</a> works
          that out first and shows the arithmetic while it does.
        </p>
      </div>
    </div>
  </div>
</section>


{C.spoke_module("Related pages in term life",
                "Same silo, and the pages this one deliberately defers to.", siblings)}


{C.faq_section("Questions about %d year term" % years, faq, "term-%dy-faq" % years)}


{C.byline_section()}
"""
