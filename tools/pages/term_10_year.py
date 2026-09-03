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
DESC = ("Who a 10 year term actually suits, what happens to the premium in year eleven, and when "
        "a longer term is the cheaper decision. Quotes from multiple carriers, no obligation.")

TRAIL = [("Home", "/"), ("Term Life Insurance", "/term-life-insurance/"),
         ("10 year term", None)]

FITS = [
    ("The closing gap", "A debt with about ten years left on it",
     "The last stretch of a mortgage, a business loan you personally guaranteed, or a parent plan "
     "loan. The obligation has a payoff date on a statement, and that date is inside ten years."),
    ("The bridge", "Ten years to a pension or a retirement date",
     "If your income stops being the household's dependency the day a pension starts, insure the "
     "gap and not a year past it. Buying beyond the date the need ends is the commonest way "
     "people overpay for term."),
    ("The top up", "A layer on top of cover you already hold",
     "A ten year layer stacked on a longer policy costs less than raising the longer policy, and "
     "it falls away on its own when the extra need does. This is the one case where ten years is "
     "chosen rather than settled for."),
]

DATES = [
    ("Write down the year the obligation ends",
     "The payoff year on the mortgage statement, the final year of the loan schedule, the year "
     "your youngest finishes education. Not the year you hope it ends. Subtract this year from it."),
    ("Add the years you would need to recover, not just repay",
     "A household that loses an income does not resume normal spending the month the debt clears. "
     "Most people add two to three years to the number above, and it is usually the difference "
     "between a ten year term being right and being one renewal short."),
    ("If the total lands above ten, price the longer term before you decide",
     "This is the step people skip. The premium difference between ten and twenty years at the "
     "same age is usually far smaller than the difference between being covered and not being "
     "covered in year eleven, because you are buying the longer term at today's age and health "
     "rather than at year eleven's."),
]

FAQ = [
    ("How much does a 10-year term life insurance policy cost?",
     "Less than any other term length at the same age and coverage, because the carrier is taking "
     "ten years of risk instead of twenty or thirty. How much less depends almost entirely on "
     "your age and whether you use tobacco. Our rates page carries the full grid by five year age "
     "band and coverage amount, with a term length toggle, rather than an average premium that "
     "would describe nobody."),
    ("What happens at the end of a 10-year term?",
     "The level premium ends and the death benefit does not automatically stop. Most policies "
     "continue on an annually renewable basis at a price recalculated for your age at that moment "
     "and rising every year afterwards. It is a bridge, not a plan. The more useful right is "
     "conversion to a permanent policy with no new health questions, and on many ten year "
     "policies that right expires before the term does, so check the conversion deadline in your "
     "contract rather than assuming it runs the full ten years."),
    ("Is 10-year term life insurance worth it?",
     "It is worth it when the need genuinely ends inside ten years, and it is a false economy "
     "when it does not. The trap is that a ten year term looks cheap next to a twenty at the "
     "point of sale, and expensive next to it at renewal, when you are ten years older and may "
     "have picked up a condition that changes your health class. If there is any real chance the "
     "need runs past ten years, price the twenty before choosing."),
    ("Can I renew or extend a 10-year term policy?",
     "Renew, usually yes, at a price that resets to your age each year. Extend at the original "
     "premium, no. There is no mechanism for that in a level term contract. If you want ten more "
     "years at a level price you apply for a new policy, and that application is underwritten on "
     "your health at that point, which is the risk the renewal provision exists to cover."),
    ("Should I buy 10-year term or 20-year term?",
     "Count the years until the obligation ends, add the recovery time, and if the total is under "
     "ten a ten year term is right. If it is close to ten, buy the twenty. The extra premium is "
     "known and small; the cost of being uninsurable in year eleven is unknown and large, and it "
     "is not a risk worth carrying to save a few dollars a month."),
]

SIBLINGS = [
    ("/term-life-insurance/20-year-term/", "20 year term",
     "The most common choice, and who it actually fits."),
    ("/term-life-insurance/30-year-term/", "30 year term",
     "Long mortgages and young children."),
    ("/term-life-insurance/level-term/", "Level term explained",
     "What the level premium guarantees, and what follows it."),
    ("/term-life-insurance/what-is-term-life-insurance/", "What term life insurance is",
     "The plain definition, if you are starting from scratch."),
    ("/term-life-insurance/no-medical-exam/", "No medical exam term",
     "Same day options, and what they cost you in class."),
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
    'A ten year term is the shortest and cheapest length of '
    '<a class="link" href="/term-life-insurance/">term life insurance</a> most carriers sell, and '
    'it suits one specific situation: an obligation with a known end date inside the next decade. '
    'Outside that situation it is usually the wrong purchase, not because it is a bad product but '
    'because of what happens in year eleven. This page is mostly about year eleven.')}


<section class="pb-14 md:pb-16">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Who a 10 year term actually suits</h2>
      <p class="reveal mt-5 text-slate">
        A term length is a guess about how long other people will need your income. These are the
        three situations where ten years is the right guess rather than the cheapest one.
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
        This is the part of a ten year term that is not explained at the point of sale. The policy
        does not usually stop at the end of the tenth year. It converts to an annually renewable
        premium recalculated for your age at that moment, and then recalculated again every year
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
        <h3 class="text-h4">The conversion right is the one that matters</h3>
        <p class="mt-3 text-slate">
          Most term policies let you convert some or all of the death benefit to a permanent policy
          with no new health questions. On a ten year policy that right frequently expires at year
          seven or eight, not at year ten. If your health has changed, conversion may be the only
          coverage still available to you, so the deadline is worth knowing before you need it.
        </p>
      </div>
      <div class="card">
        <h3 class="text-h4">Do not cancel until the replacement is in force</h3>
        <p class="mt-3 text-slate">
          If you intend to buy a new policy at the end of the term, apply while the old one is
          still running. An application can be declined, postponed, or offered at a worse class
          than you expected, and the gap between cancelling one policy and being issued another is
          the only period in this whole exercise where your family is genuinely exposed.
        </p>
      </div>
    </div>
  </div>
</section>


{C.prose("Check ten years against your own dates", date_rows,
         intro="Three numbers decide this, and all three are things you can look up in about ten "
               "minutes rather than estimate.")}


{C.inline_cta(
    "Price ten and twenty years side by side",
    "Six questions, about two minutes. A licensed agent comes back with premiums from named "
    "carriers at both lengths, at a class we can defend, so you can see the actual gap rather "
    "than guess at it. No obligation, and no cost.",
    "term_10y_mid", "/term-life-insurance/quotes/", "Get term life quotes")}


<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">What a 10 year term costs</h2>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <p class="reveal text-slate">
          Ten years is the cheapest level term a carrier will normally write, because it is the
          least risk it is taking. What moves the number after that is your age today and whether
          you use tobacco, then health class, coverage amount, sex, and state, in roughly that
          order. The term length itself is rarely the largest factor, which is exactly why buying
          the shortest one is a smaller saving than it appears.
        </p>
        <p class="reveal mt-5 text-slate">
          Rather than reprint a slice of it here, the full grid lives on one page and is kept
          current in one place: <a class="link" href="/term-life-insurance/rates/">term life
          insurance rates by age</a>, with a term length toggle and a button on every row that
          carries the numbers into a quote form.
        </p>
        <p class="reveal mt-5 text-slate">
          If the amount rather than the length is the open question, the
          <a class="link" href="/term-life-insurance/calculator/">coverage calculator</a> works
          that out first and shows its arithmetic while it does.
        </p>
      </div>
    </div>
  </div>
</section>


{C.spoke_module("Related pages in term life",
                "Same silo, and the pages this one deliberately defers to.", SIBLINGS)}


{C.faq_section("Questions about 10 year term", FAQ, "term-10y-faq")}


{C.byline_section()}
"""
