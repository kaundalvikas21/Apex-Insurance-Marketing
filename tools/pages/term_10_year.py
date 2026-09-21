# -*- coding: utf-8 -*-
"""10 YEAR TERM. Spec P2/P3, template T4. FORM CTA.

The only term length the spec records a measured volume for (2,900), so unlike
the 20 and 30 year pages this one is NOT built on term_length.py. It gets its
own module and its own signature object: the renewal schedule table, which is
the thing a ten year buyer is not told and the reason this page can be genuinely
useful rather than another length page.

Every cell in that table is `$--`, like every other rate cell on this site. The
shape of the curve is the point, not the numbers.
"""
import chrome as C

PATH = "/term-life-insurance/10-year-term/"
OUT = "term-life-insurance/10-year-term/index.html"
ACTIVE = "/term-life-insurance/"
SILO = "term-life"
TITLE = "10-Year Term Life Insurance | Who It Suits | Apex"
OG_TITLE = "10 year term life insurance"
DESC = ("Who a 10 year term fits, what the price does in year eleven, and when a longer term is "
        "the cheaper choice. Quotes from multiple carriers, no obligation.")

TRAIL = [("Home", "/"), ("Term Life Insurance", "/term-life-insurance/"),
         ("10 year term", None)]

FITS = [
    ("The debt case", "A debt with about ten years left on it",
     "The last stretch of a mortgage, a business loan you personally guaranteed, or a parent plan "
     "loan. The obligation has a payoff date on a statement, and that date is inside ten years."),
    ("The bridge case", "Ten years to a pension or a retirement date",
     "If your household stops depending on your income the day a pension starts, insure the "
     "gap and not a year past it. Buying past the date the need ends is the most common way "
     "people overpay for term."),
    ("The add-on case", "A layer on top of coverage you already have",
     "A ten year layer stacked on a longer policy costs less than increasing the longer policy, and "
     "it ends on its own when the extra need does. This is the one case where ten years is "
     "chosen rather than settled for."),
]

DATES = [
    ("Write down the year the obligation ends",
     "The payoff year on the mortgage statement, the final year of the loan schedule, the year "
     "your youngest finishes school. Not the year you hope it ends. Subtract this year from it."),
    ("Add the years you would need to recover, not just repay",
     "A household that loses an income does not resume normal spending the month the debt clears. "
     "Most people add two to three years to the number above. That is usually the difference "
     "between a ten year term being right and being one renewal short."),
    ("Over ten years? Price the longer term first",
     "This is the step people skip. The premium difference between ten and twenty years at the "
     "same age is usually far smaller than the cost of having no coverage in year eleven. With "
     "the longer term you buy at today's age and health, not at year eleven's."),
]

FAQ = [
    ("How much does a 10-year term life insurance policy cost?",
     "Less than any other term length at the same age and coverage, because the carrier is taking "
     "ten years of risk instead of twenty or thirty. How much less depends almost entirely on "
     "your age and whether you use tobacco. Our rates page has the full chart by five year age "
     "band and coverage amount, and you can switch the term length."),
    ("What happens at the end of a 10-year term?",
     "The level premium ends and the death benefit does not automatically stop. Most policies "
     "continue on an annually renewable basis at a price recalculated for your age at that moment "
     "and rising every year afterward. It is a stopgap, not a plan. The more useful right is "
     "conversion to a permanent policy with no new health questions. On many ten year "
     "policies that right expires before the term does. Check the conversion deadline in your "
     "contract rather than assuming it runs the full ten years."),
    ("Is 10-year term life insurance worth it?",
     "It is worth it when the need genuinely ends inside ten years, and it is a false economy "
     "when it does not. The trap is that a ten year term looks cheap next to a twenty when you "
     "buy it, and expensive next to it at renewal. By then you are ten years older and may "
     "have picked up a condition that changes your health class. If there is any real chance the "
     "need runs past ten years, price the twenty before choosing."),
    ("Can I renew or extend a 10-year term policy?",
     "Renew, usually yes, at a price that resets to your age each year. Extend at the original "
     "premium, no. There is no mechanism for that in a level term contract. If you want ten more "
     "years at a level price you apply for a new policy. That application is underwritten on "
     "your health at that point, which is the risk the renewal provision exists to cover."),
    ("Should I buy 10-year term or 20-year term?",
     "Count the years until the obligation ends, add the recovery time, and if the total is under "
     "ten a ten year term is right. If it is close to ten, buy the twenty. The extra premium is "
     "known and small. The cost of being uninsurable in year eleven is unknown and large. It "
     "is not a risk worth carrying to save a few dollars a month."),
]

SIBLINGS = [
    ("/term-life-insurance/20-year-term/", "20 year term",
     "The most common length, and who it fits."),
    ("/term-life-insurance/30-year-term/", "30 year term",
     "Long mortgages and young children."),
    ("/term-life-insurance/level-term/", "Level term explained",
     "What the level premium guarantees, and what follows it."),
    ("/term-life-insurance/what-is-term-life-insurance/", "What term life insurance is",
     "The plain definition, if you are starting from scratch."),
    ("/term-life-insurance/no-medical-exam/", "No medical exam term",
     "Same day options, and what they do to your health class."),
    ("/term-life-insurance/return-of-premium/", "Return of premium term",
     "Getting the premiums back, and what that costs."),
]

RENEWAL_ROWS = [
    ("Years 1 to 10, the level term", "The premium set at issue", "Fixed by contract"),
    ("Year 11, the first renewal", "$--", "Recalculated for your age at year 11"),
    ("Year 12", "$--", "Rises again"),
    ("Year 13", "$--", "Rises again"),
    ("Year 14", "$--", "Rises again"),
    ("Year 15", "$--", "Rises again"),
]


TEN_YEAR_COST = """<h3 class="reveal  text-h4">What changes the price</h3>
<p class="reveal mt-3 text-slate">
        Ten years is the cheapest level term a carrier will normally write, because it is the
        least risk it is taking. After that, the two things that change the price most are your
        age today and whether you use tobacco. Health class, coverage amount, sex, and state
        come after those, in roughly that order. The term length itself is rarely the largest
        factor, which is why buying the shortest one saves less than it appears.
      </p>
      <h3 class="reveal mt-8 text-h4">Where to see the full rate chart</h3>
<p class="reveal mt-3 text-slate">
        The full chart is on one page: <a class="link" href="/term-life-insurance/rates/">term life
        insurance rates by age</a>. You can switch the term length, and a button on every row
        carries the numbers into a quote form.
      </p>
      <h3 class="reveal mt-8 text-h4">Not sure of the amount?</h3>
<p class="reveal mt-3 text-slate">
        The <a class="link" href="/term-life-insurance/calculator/">coverage calculator</a>
        works out the amount and shows the math.
      </p>"""


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    cells = ""
    for i, (eyebrow, title, text) in enumerate(FITS):
        variant = ["bento-cell-blue", "", "bento-cell-tint"][i]
        navy = i == 0
        cells += f"""
      <div class="reveal bento-cell {variant} bento-2">
        <p class="eyebrow{' text-white/80' if navy else ''}">{eyebrow}</p>
        <h3 class="mt-2 text-h4{' text-white' if navy else ''}">{title}</h3>
        <p class="mt-3 {'text-white/90' if navy else 'text-slate'}">{text}</p>
      </div>"""

    date_rows = "".join(
        (('<div class="mt-8">%s</div>' if i else "%s") % C.step(i + 1, t, b))
        for i, (t, b) in enumerate(DATES))

    renewal = "".join(
        '<tr><th scope="row">%s</th><td class="tnum">%s</td><td>%s</td></tr>' % r
        for r in RENEWAL_ROWS)

    return f"""
{C.page_hero(
    TRAIL,
    "10-Year Term Life Insurance",
    'A ten year term is the shortest and cheapest length most carriers sell, and it suits '
    'one specific situation.',
    answer=(
        'That situation is an obligation with a known end date inside the next ten years. '
        'Outside it, ten years is usually the wrong length of <a class="link" '
        'href="/term-life-insurance/">term life insurance</a> to buy. It is not a '
        'bad product. The problem is what happens in year eleven, and this page is mostly '
        'about that.'),
    extra=C.hero_cta("/term-life-insurance/quotes/", "Get my term life quote"),
    media=C.figure("term-table", C.MEDIA_SIZES, eager=True))}


<section class="pb-14 md:pb-16">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Who a 10 year term fits</h2>
      <p class="reveal mt-5 text-slate">
        The right term length is how long other people will need your income. These are the
        three situations where ten years fits.
      </p>
    </div>
    <div class="mt-10 bento" data-stagger="40">{cells}
    </div>
  </div>
</section>


<!-- =====================================================================
     THE RENEWAL SCHEDULE. This page's signature object.

     Every premium cell is `$--` by decision (MASTER.md s7). The shape of
     the curve is what a ten year buyer needs to see, and a marked fake
     number still gets screenshotted.
     ================================================================== -->
<section class="section band" id="what-happens-in-year-eleven">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">What happens in year eleven</h2>
      <p class="reveal mt-5 text-slate">
        This is the part of a ten year term that is not explained when you buy it. The policy
        does not usually stop at the end of the tenth year. It switches to an annually renewable
        premium: the price is recalculated for your age at that moment, and again every year
        after that. Nobody buys a ten year term intending to pay that. Plenty of people end up
        paying it because the renewal notice arrives before a replacement policy does.
      </p>
    </div>

    {C.rates_flag("premium cells")}

    <div class="reveal mt-8 table-scroll table-signature">
      <table class="rate-table" style="min-width:34rem">
        <caption>
          The shape of a ten year term after the level period ends.
          Figures are structural placeholders, not quoted premiums.
        </caption>
        <thead>
          <tr>
            <th scope="col">Policy year</th>
            <th scope="col" class="tnum">Monthly premium</th>
            <th scope="col">How it is set</th>
          </tr>
        </thead>
        <tbody>
          {renewal}
        </tbody>
      </table>
    </div>

    <p class="reveal mt-4 text-micro text-muted max-w-3xl">
      <span class="pill mr-2">Rates last updated: {C.RATES_DATE}</span>
      Source: [CARRIER RATE CARD NAME AND EDITION]. Renewal provisions differ by carrier and by
      state, and some policies end at the term rather than renewing at all. Read the renewal and
      conversion sections of your own contract, or ask us to read them with you.
    </p>

    <div class="reveal mt-10 grid lg:grid-cols-2 gap-4">
      <div class="card">
        <h3 class="text-h4">Check when your conversion right expires</h3>
        <p class="mt-3 text-slate">
          Most term policies let you convert some or all of the death benefit to a permanent policy
          with no new health questions. On a ten year policy that right frequently expires at year
          seven or eight, not at year ten. If your health has changed, conversion may be the only
          coverage still available to you, so the deadline is worth knowing before you need it.
        </p>
      </div>
      <div class="card">
        <h3 class="text-h4">Do not cancel before the new policy starts</h3>
        <p class="mt-3 text-slate">
          If you intend to buy a new policy at the end of the term, apply while the old one is
          still running. An application can be declined, postponed, or offered at a worse class
          than you expected. The gap between canceling one policy and being issued another is
          the one period when your family has no coverage.
        </p>
      </div>
    </div>
  </div>
</section>


{C.steps_section("Check ten years against your own dates",
         "Three numbers decide this, and all three are things you can look up in about ten "
               "minutes rather than estimate.",
         DATES)}


{C.inline_cta(
    "Price ten and twenty years side by side",
    "Six questions, about two minutes. A licensed agent comes back with premiums from named "
    "carriers at both lengths, at a health class we can defend. You see the actual gap rather "
    "than guess at it. No obligation, and no cost.",
    "term_10y_mid", "/term-life-insurance/quotes/", "Get my term life quote")}


{C.prose("What a 10 year term costs", TEN_YEAR_COST,
         intro="What changes the price of a 10 year policy, and where to see the full rate chart.")}


{C.spoke_module("Related pages in term life",
                "More on term life, including the pages this one points to for detail.", SIBLINGS)}


{C.faq_section("Questions about 10 year term", FAQ, "term-10y-faq")}


{C.closing_band("term-band", "See what a 10 year term would cost you",
    "Tell us your age, state and the amount you have in mind. We quote ten and twenty years, so "
    "you can see the gap before you choose.",
    "term_10y_close", silo="term")}

{C.byline_section()}
"""
