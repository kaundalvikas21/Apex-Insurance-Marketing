# -*- coding: utf-8 -*-
"""RETURN OF PREMIUM TERM. Spec P3, template T4. FORM CTA.

Spec s05: this page builds trust more than it sells. The agency does not
generally recommend the product, and the page says so in the hero rather than
burying it under a balanced-looking summary. A reader who arrives here has
usually been pitched ROP by someone else and wants to know whether they were
being sold to.

The worked cost table is the page's signature object. Every dollar cell is
`$--`: the honest comparison is between two premiums we do not have rate cards
for yet, and the SHAPE of the comparison is the part that does not change when
the numbers arrive. What the table shows without any numbers at all is the
structure of the trade: a larger premium, for the same death benefit, with a
refund of the premiums at the end and nothing in between.

There is no invented rate of return anywhere on this page. The opportunity cost
section names the mechanism and refuses to put a percentage on it, because any
percentage we chose would be the argument rather than the evidence.
"""
import chrome as C

PATH = "/term-life-insurance/return-of-premium/"
OUT = "term-life-insurance/return-of-premium/index.html"
ACTIVE = "/term-life-insurance/"
SILO = "term-life"
TITLE = "Return of Premium Term Life Insurance: Is It Worth It? | Apex"
OG_TITLE = "Return of premium term life insurance"
DESC = ("How return of premium term works, what the refund actually costs you, and the small "
        "number of situations where it is the right buy. An honest look, not a pitch.")

TRAIL = [("Home", "/"), ("Term Life Insurance", "/term-life-insurance/"),
         ("Return of premium", None)]

COST_ROWS = [
    ("Death benefit", "$500,000", "$500,000",
     "Identical. This is the point people miss: you are not buying more coverage."),
    ("Monthly premium", "$--", "$--",
     "The ROP premium is typically a large multiple of the standard one, not a small markup."),
    ("Total paid over 30 years", "$--", "$--",
     "The whole extra amount, which is the number to judge the refund against."),
    ("Paid back if you outlive the term", "$0", "$--",
     "Usually the base premiums only. Policy fees and riders are often excluded."),
    ("Paid back if you cancel in year 15", "$0", "$--",
     "Partial, on a surrender schedule set at issue. Frequently far less than half."),
    ("Net cost if you outlive the term", "$--", "$--",
     "Before considering what the extra premium could have done elsewhere."),
    ("Interest paid on the refund", "Not applicable", "None",
     "The refund is a return of your own money, not a return on it."),
]

WINS = [
    ("The disciplined case", "You would genuinely not invest the difference",
     "Not &quot;you intend to&quot;. If the honest answer is that the extra premium would be "
     "absorbed into everyday spending, then a forced savings mechanism with a refund at the end "
     "beats an intention that never gets acted on. This is a real argument and it is the strongest "
     "one for the product."),
    ("The high income case", "You have filled every tax advantaged account first",
     "If the retirement accounts are maxed and this is genuinely surplus, the calculus changes, "
     "because the alternative use of the money is a taxable account rather than a tax advantaged "
     "one. This is a narrow case, and it is worth checking with a tax professional rather than an "
     "insurance agent."),
    ("The certainty case", "You value a known outcome more than a probable one",
     "The refund amount is written into the contract at issue. Nothing else in this comparison "
     "is. Some people will pay a real premium for a number they can point to, and that is a "
     "preference rather than a mistake, as long as it is priced honestly."),
]

FAQ = [
    ("Is return of premium life insurance worth it?",
     "For most households, no. You pay a substantially higher premium for the same death benefit, "
     "and the refund at the end is your own money back with no interest. For the difference to be "
     "worth it, you have to be certain you will keep the policy for the entire term, and you have "
     "to be someone who genuinely would not have put the extra premium anywhere else. Both of "
     "those are true of some people. Neither is true of most."),
    ("Do you get all your money back with return of premium?",
     "Usually the base premiums, and usually only if you hold the policy for the full term. "
     "Policy fees, rider charges, and any modal payment loading are commonly excluded, so the "
     "refund is normally a little less than everything you actually paid. The exact definition is "
     "in the policy, and it is worth reading the words rather than the brochure, because carriers "
     "differ on this."),
    ("What happens if I cancel a return of premium policy early?",
     "You receive a partial refund on a schedule set at issue, and in the early years that "
     "schedule is unkind. It is common for a policy surrendered in the first several years to "
     "return little or nothing, and for one surrendered halfway through the term to return well "
     "under half the premiums paid. Since the higher premium is the reason people lapse these "
     "policies, this is the risk that actually bites."),
    ("Is the return of premium refund taxable?",
     "A refund of your own premiums is generally treated as a return of basis rather than income, "
     "so it is generally not taxable. Generally is doing real work in that sentence: the treatment "
     "depends on the policy's structure and your own circumstances, and we are a licensed "
     "insurance agency, not tax advisers. Confirm it with a tax professional before you rely on "
     "it in a plan."),
    ("Do you recommend return of premium term life insurance?",
     "Rarely, and we would rather tell you that here than after you have sat through a call. For "
     "the overwhelming majority of the households we work with, standard term at the right length "
     "and amount, with the difference in premium put anywhere at all, is the better decision. We "
     "will still quote it if you want it quoted, and we will show you both side by side so the "
     "gap is visible rather than described."),
]

SIBLINGS = [
    ("/term-life-insurance/what-is-term-life-insurance/", "What term life insurance is",
     "The plain definition, and how standard term compares."),
    ("/term-life-insurance/level-term/", "Level term explained",
     "What a level premium guarantees, and for how long."),
    ("/term-life-insurance/30-year-term/", "30 year term",
     "The length most return of premium policies are written at."),
    ("/term-life-insurance/10-year-term/", "10 year term",
     "The short end, and what happens at the renewal."),
    ("/term-life-insurance/no-medical-exam/", "No medical exam term",
     "Accelerated and simplified issue, and what they cost."),
    ("/term-life-insurance/20-year-term/", "20 year term",
     "The other common length, and who it fits."),
]


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    rows = "".join(
        '<tr><th scope="row">%s</th><td class="tnum">%s</td><td class="tnum">%s</td>'
        '<td>%s</td></tr>' % r for r in COST_ROWS)

    wins = ""
    for i, (eyebrow, title, text) in enumerate(WINS):
        variant = ["bento-cell-blue", "", "bento-cell-tint"][i]
        navy = i == 0
        wins += f"""
      <div class="reveal bento-cell {variant} bento-2">
        <p class="eyebrow{' text-white/80' if navy else ''}">{eyebrow}</p>
        <h3 class="mt-2 text-h4{' text-white' if navy else ''}">{title}</h3>
        <p class="mt-3 {'text-white/90' if navy else 'text-slate'}">{text}</p>
      </div>"""

    mechanics = "".join([
        C.qa("You pay a higher premium for the same death benefit",
             "A return of premium policy is a standard level term policy with a refund provision "
             "attached. The coverage, the term, and the payout to your family if you die during it "
             "are the same as the standard policy beside it. The only difference is the price and "
             "what happens at the end."),
        C.qa("If you outlive the term, the carrier refunds the premiums",
             "Usually the base premiums, without interest, provided the policy was in force for "
             "the whole term. That refund is written into the contract at issue, so it is a known "
             "number rather than a projection. It is also, precisely, your own money coming back "
             "to you after twenty or thirty years.", "mt-8"),
        C.qa("If you cancel early, you get a fraction of it",
             "The surrender schedule is set at issue and is heavily back loaded. A policy given up "
             "in the early years typically returns little or nothing, and one given up at the "
             "halfway point commonly returns well under half. Since the higher premium is itself "
             "the main reason people give these policies up, the two risks compound.", "mt-8"),
        C.qa("The refund is not a return, it is a repayment",
             "This is the sentence the product is usually sold without. No interest is credited, "
             "no growth is shared, and the amount does not change with market conditions. The "
             "carrier held your extra premium for thirty years and gives back the same dollars, "
             "which are worth less than the dollars you handed over.", "mt-8"),
    ])

    return f"""
{C.page_hero(
    TRAIL,
    "Return of Premium Term Life Insurance",
    'Return of premium is standard '
    '<a class="link" href="/term-life-insurance/">term life insurance</a> with one addition: if you '
    'are still alive at the end of the term, the carrier refunds the premiums you paid. The '
    'coverage is identical to a standard policy of the same size and length, the premium is '
    'substantially higher, and the refund carries no interest. We rarely recommend it, and this '
    'page explains the arithmetic behind that rather than asking you to take it on trust.')}


{C.prose("How it actually works", mechanics,
         intro="Four mechanics, and the fourth is the one that decides it.")}


<!-- =====================================================================
     THE WORKED COMPARISON. This page's signature object.

     Every dollar cell is `$--` (MASTER.md s7). The structure of the trade
     is legible without a single real number, which is the point: a marked
     fake premium here would become the argument.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">The same coverage, priced two ways</h2>
      <p class="reveal mt-5 text-slate">
        One household, one death benefit, one thirty year term, two structures. This is the
        comparison a return of premium quote should always be shown next to, and almost never is.
      </p>
    </div>

    {C.rates_flag("premium and total cost cells")}

    <div class="reveal mt-8 table-scroll table-signature">
      <table class="compare-table" style="min-width:52rem">
        <caption class="sr-only">
          Standard 30 year term compared with return of premium 30 year term at the same death
          benefit. Dollar figures are structural placeholders.
        </caption>
        <thead>
          <tr>
            <th scope="col"><span class="sr-only">What is being compared</span></th>
            <th scope="col">Standard term</th>
            <th scope="col">Return of premium</th>
            <th scope="col">What it means</th>
          </tr>
        </thead>
        <tbody>
          {rows}
        </tbody>
      </table>
    </div>

    <p class="reveal mt-4 text-micro text-muted max-w-3xl">
      <span class="pill mr-2">Rates last updated: {C.RATES_DATE}</span>
      Source: [CARRIER RATE CARD NAME AND EDITION]. Refund definitions, surrender schedules, and
      which charges are excluded from the refund differ by carrier and by state. The policy
      wording governs, not a comparison table.
    </p>
  </div>
</section>


<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">What the refund really costs</h2>
        <p class="reveal mt-5 text-slate">
          The honest objection to return of premium is not that the refund is fake. It is real and
          it is contractual. The objection is what the extra premium was doing for thirty years
          while the carrier held it.
        </p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <p class="reveal text-slate">
          Take the difference between the two premiums in the table above. That difference leaves
          your account every month for thirty years, and at the end of it you receive the same
          dollars back with nothing added. Whatever those dollars would have done in any account
          you actually own, an index fund, a retirement account, an offset against the mortgage, or
          a savings account, is the true cost of the refund.
        </p>
        <p class="reveal mt-5 text-slate">
          We are deliberately not putting a percentage on that here. Any rate of return we chose
          would be doing the arguing for us, and we would be choosing it knowing which way we
          wanted the comparison to come out. Put your own number in, using an account you genuinely
          hold, and the comparison becomes yours rather than ours.
        </p>
        <p class="reveal mt-5 text-slate">
          There is a second cost that is easier to overlook. Thirty years of dollars returned at
          face value are worth less than the dollars that went in, because prices move over thirty
          years. The refund is nominal, not real. That is not a criticism of the carrier; it is
          simply what a repayment without interest is.
        </p>
        <p class="reveal mt-5 text-slate">
          Set against all of that is one genuine benefit, which the next section is about: if the
          alternative is that the money is spent rather than invested, a contractual refund beats
          an intention.
        </p>
      </div>
    </div>
  </div>
</section>


<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">When it is genuinely the right buy</h2>
      <p class="reveal mt-5 text-slate">
        Three situations, and we would place the policy in all three without hesitation. If none of
        them describes you, the standard policy is the better decision and we will say so on the
        call.
      </p>
    </div>
    <div class="mt-10 bento" data-stagger="40">{wins}
    </div>
  </div>
</section>


{C.inline_cta(
    "See both quoted side by side",
    "Six questions, about two minutes. We will come back with a standard term premium and a return "
    "of premium premium for the same coverage from named carriers, so the gap is a number you can "
    "look at rather than an argument you have to referee. No obligation, and no cost.",
    "term_rop_mid", "/term-life-insurance/quotes/", "Get term life quotes")}


<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">Before you decide either way</h2>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <p class="reveal text-slate">
          Settle the amount and the length first. Those two decisions matter more to your household
          than the refund provision does, and they are the ones that are hard to change later. The
          <a class="link" href="/term-life-insurance/calculator/">coverage calculator</a> sizes the
          amount and shows its working, and
          <a class="link" href="/term-life-insurance/rates/">term life insurance rates by age</a>
          shows how the premium moves with length so you can see what you are actually trading.
        </p>
        <p class="reveal mt-5 text-slate">
          Then ask one question about yourself, honestly: if you bought the standard policy, where
          would the difference in premium go? If you can name the account, buy the standard policy.
          If you cannot, return of premium may be the version of this decision you will actually
          stick to, and sticking to it is worth more than being theoretically right.
        </p>
      </div>
    </div>
  </div>
</section>


{C.spoke_module("Related pages in term life",
                "The standard product this page is measured against, and the lengths it is "
                "usually written at.", SIBLINGS)}


{C.faq_section("Questions about return of premium term", FAQ, "term-rop-faq")}


{C.byline_section()}
"""
