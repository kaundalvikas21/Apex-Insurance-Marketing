# -*- coding: utf-8 -*-
"""WHOLE LIFE DIVIDENDS. Spec P3, template T4. SOFT CTA.

The compliance line on this page, which is load bearing rather than decorative:

    DIVIDENDS ARE NOT GUARANTEED. EVER. UNDER ANY FRAMING.

So it is in the first two sentences of the hero, it is a visible notice above
the section that explains how dividends are declared, and every sentence about
future dividends is written in the conditional. There is no dividend scale
figure, no historical payout record, and no carrier name anywhere on this page,
because a real one of any of those would be an implied projection and an
invented one would be fabrication.

#how-they-are-declared is deep linked from the whole life hub. Do not rename it
without updating whole.py and REPLACE-BEFORE-LAUNCH.md section 6.
"""
import chrome as C

PATH = "/whole-life-insurance/dividends/"
OUT = "whole-life-insurance/dividends/index.html"
ACTIVE = "/whole-life-insurance/"
SILO = "whole-life"
TITLE = "Dividend-Paying Whole Life Insurance Explained | Apex"
OG_TITLE = "Dividend paying whole life insurance"
DESC = ("What a whole life dividend is, how carriers decide one, the four things you can do with "
        "it, and why no dividend is ever guaranteed. Written by a licensed agent.")

TRAIL = [("Home", "/"), ("Whole Life Insurance", "/whole-life-insurance/"),
         ("Dividends", None)]

OPTIONS = [
    ("Paid up additions",
     "The dividend buys a small piece of extra permanent coverage, fully paid for, which itself "
     "becomes eligible for future dividends.",
     "The most common election, and the one that compounds. Increases both the death benefit and "
     "the cash value."),
    ("Reduce the premium",
     "The dividend is applied against your next premium, so you pay the difference.",
     "Useful when the premium is the pressure point. The policy stops growing beyond its "
     "guarantees, and in a year with no dividend the full premium is due again."),
    ("Take it in cash",
     "The carrier pays the dividend out to you.",
     "Simple and visible. Generally treated as a return of premium rather than income up to your "
     "cost basis, but confirm the treatment with a tax professional."),
    ("Leave it on deposit",
     "The dividend stays with the carrier and accumulates at a declared interest rate.",
     "The interest here is normally taxable in the year it is credited, unlike the growth inside "
     "the policy itself."),
]

DECLARED = [
    ("Mortality experience",
     "Whether the carrier's policyholders died at the rate its pricing assumed. If fewer claims "
     "were paid than the pricing expected, that difference is one source of a divisible surplus. "
     "This is the largest component for most carriers most years."),
    ("Expense experience",
     "Whether running the company cost less than the pricing assumed. Administration, "
     "distribution, and overhead all sit here, and a carrier that is efficient in a given year has "
     "more surplus to divide than one that is not."),
    ("Investment experience",
     "What the carrier's general account, mostly high grade bonds held to maturity, actually "
     "earned against the rate it guaranteed. This is the component most sensitive to the interest "
     "rate environment, and it is why dividend scales across the industry moved with rates over "
     "the past two decades."),
    ("The board's decision",
     "The three above produce a surplus. The board decides how much of it to distribute, how much "
     "to retain for solvency, and what scale to declare. That decision is made annually, is "
     "discretionary, and is the reason no dividend can be promised in advance by anyone, "
     "including us."),
]

FAQ = [
    ("Are whole life insurance dividends guaranteed?",
     "No. Not by the carrier, not by the illustration, and not by any agent. A dividend is a "
     "distribution of the carrier's divisible surplus, declared annually at the discretion of its "
     "board, and it can be reduced or not paid at all. Carriers have done both. The guaranteed "
     "part of your policy is the guaranteed cash value schedule and the guaranteed death benefit "
     "printed in the contract, and a plan that only works if the dividends arrive is a plan that "
     "does not work."),
    ("What is a dividend on a whole life policy?",
     "It is a return of the part of your premium the carrier did not need. Whole life is priced "
     "conservatively on purpose, with cautious assumptions about how long policyholders live, what "
     "the company costs to run, and what its investments earn. When actual experience beats those "
     "assumptions, the difference forms a divisible surplus, and a participating policy is one "
     "that is eligible to share in it. That is why it is generally treated as a return of premium "
     "rather than as investment income."),
    ("How much are whole life dividends?",
     "We are not going to print a number, and you should be sceptical of any agency that does. "
     "The scale differs by carrier, by policy series, by issue year, and by policy size, and it "
     "changes annually. The only figure that means anything for your situation is the one on a "
     "current illustration from the specific carrier being proposed, showing the guaranteed and "
     "non guaranteed columns separately. We will send you one of those."),
    ("What is the best dividend option?",
     "For most people buying whole life for the long term, paid up additions, because it is the "
     "only option that compounds: the extra coverage it buys is itself eligible for future "
     "dividends. Reducing the premium is the right answer when affordability is the binding "
     "constraint and keeping the policy in force matters more than growing it. There is no option "
     "that is best for everyone, and you can usually change the election later."),
    ("Do dividends make whole life a good investment?",
     "They improve the outcome; they do not change the category. A participating whole life policy "
     "is insurance with a guaranteed savings component and a discretionary distribution attached, "
     "and it should be judged against that description rather than against an index fund. If the "
     "reason you are considering the policy is the dividend rather than the permanent death "
     "benefit, that is worth examining carefully before you buy."),
]

SIBLINGS = [
    ("/whole-life-insurance/cash-value/", "How cash value works",
     "Where dividends land, and the guaranteed schedule underneath."),
    ("/whole-life-insurance/what-is-whole-life-insurance/", "What whole life insurance is",
     "The definition, the mechanics, and the fine print."),
    ("/whole-life-insurance/is-it-worth-it/", "Is whole life worth it?",
     "The honest case for and against, side by side."),
    ("/whole-life-insurance/calculator/", "Whole life calculator",
     "Size the permanent need, with the method shown."),
    ("/whole-life-insurance/for-seniors/", "Whole life for seniors",
     "What a dividend realistically does when bought after 65."),
    ("/whole-life-insurance/guaranteed-acceptance/", "Guaranteed acceptance",
     "No health questions, and why these rarely pay dividends."),
]


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


LEAD = (
    'A dividend on a participating '
    '<a class="link" href="/whole-life-insurance/">whole life insurance</a> policy is a share of '
    "the carrier's surplus, returned to policyholders when the company's actual experience beats "
    'the cautious assumptions it priced with. It is not interest, it is not an investment return, '
    'and it is never guaranteed: the board declares it annually and can reduce it or skip it '
    'entirely. What follows is how one is decided, what you can do with it, and how to read an '
    'illustration that shows one.')


def body():
    declared = "".join(
        (('<div class="mt-8">%s</div>' if i else "%s") % C.step(i + 1, t, b))
        for i, (t, b) in enumerate(DECLARED))

    option_rows = "".join(
        '<tr><th scope="row">%s</th><td>%s</td><td>%s</td></tr>' % o for o in OPTIONS)

    return f"""
{C.page_hero(
    TRAIL,
    "Dividend-Paying Whole Life Insurance Explained",
    LEAD,
    media=C.figure("whole-arbor", C.MEDIA_SIZES, eager=True))}


<section class="pb-14 md:pb-16">
  <div class="container-ax">
    <div class="max-w-3xl">
      {C.flag('No dividend shown, described, or implied on this page is guaranteed, projected, '
              'or promised. Dividends are declared annually at the discretion of the carrier and '
              'may be reduced or not paid at all. Any figure a reader sees must come from a '
              'current, carrier issued illustration with the guaranteed and non guaranteed '
              'columns shown separately.',
              'COMPLIANCE: DIVIDENDS ARE NOT GUARANTEED')}
    </div>
  </div>
</section>


<section class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">What a dividend actually is</h2>
        <p class="reveal mt-5 text-slate">
          The word is borrowed from company shares, and it misleads almost everybody who hears it.
          A whole life dividend is closer to a refund than to a payout.
        </p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <p class="reveal text-slate">
          Whole life is priced on deliberately cautious assumptions. The carrier assumes people
          will die somewhat sooner than it really expects, that running the company will cost
          somewhat more, and that its investments will earn somewhat less. Those assumptions are
          built into a premium that is fixed for life, which means the carrier has to be able to
          keep its promise even if the pessimistic version comes true.
        </p>
        <p class="reveal mt-5 text-slate">
          Most years, the pessimistic version does not come true. The difference between what was
          assumed and what actually happened forms what the carrier calls a divisible surplus. A
          participating policy is one that is eligible to share in it, and your share of it is the
          dividend. That is why it is generally treated for tax purposes as a return of premium
          rather than as income: it largely is your own money, returned because it turned out not
          to be needed.
        </p>
        <p class="reveal mt-5 text-slate">
          Two things follow from that description, and they are the two things people most often
          get wrong. A dividend is not a rate of return on your cash value, so comparing it to an
          investment yield compares two different kinds of number. And because it depends on
          experience that has not happened yet, no honest person can tell you what next year's will
          be.
        </p>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     #how-they-are-declared is deep linked from the whole life hub
     (whole.py). Renaming this anchor breaks that link silently:
     check.py strips fragments when it crawls.
     ================================================================== -->
<div id="how-they-are-declared" class="sr-only" aria-hidden="true"></div>
{C.prose("How a dividend is declared", declared,
         intro="Four inputs, in the order they matter to most carriers most years. The fourth is "
               "the one that makes the first three non binding.",
         cls="section", aside='<p class="text-sm text-muted">A carrier that has paid a dividend '
                              'every year for a very long time has demonstrated something real '
                              'about its discipline. It has not, and cannot, promise the next '
                              'one.</p>')}


<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">The four things you can do with one</h2>
      <p class="reveal mt-5 text-slate">
        You elect this at application and can usually change it later. The election matters more
        over thirty years than most buyers realise at the point of sale.
      </p>
    </div>

    <div class="reveal mt-10 table-scroll table-signature">
      <table class="compare-table" style="min-width:46rem">
        <caption class="sr-only">The four standard dividend options on a participating whole life
        policy</caption>
        <thead>
          <tr>
            <th scope="col">Option</th>
            <th scope="col">What happens</th>
            <th scope="col">What it means in practice</th>
          </tr>
        </thead>
        <tbody>
          {option_rows}
        </tbody>
      </table>
    </div>

    <p class="reveal mt-4 text-micro text-muted max-w-3xl">
      Availability and naming of these options differ by carrier and by policy series. Tax
      treatment described here is general information, not tax advice; we are a licensed insurance
      agency and not tax advisers. Confirm your own position with a tax professional.
    </p>
  </div>
</section>


<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">How to read an illustration that shows dividends</h2>
        <p class="reveal mt-5 text-slate">
          This is the single most useful skill on this page, and it takes about two minutes to
          learn.
        </p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        {C.qa("Find the two sets of columns",
              "Every compliant whole life illustration has a guaranteed section and a non "
              "guaranteed section, usually side by side or on facing pages. The guaranteed columns "
              "assume no dividend is ever paid. The non guaranteed columns assume the carrier's "
              "current dividend scale continues unchanged for the entire illustration, which is a "
              "modelling convention rather than a forecast.")}
        {C.qa("Read the guaranteed columns first, and judge the policy on them",
              "If the policy only makes sense on the non guaranteed columns, it does not make "
              "sense. This is the test, and it is the reason a good agent will hand you the "
              "illustration open at the guaranteed page.", "mt-8")}
        {C.qa("Check what dividend scale the illustration was run at",
              "It is printed on the illustration, usually in small type near the header or in the "
              "narrative pages. An illustration run at a scale the carrier has since reduced will "
              "show non guaranteed values that are already out of date, which is why a current one "
              "matters.", "mt-8")}
        {C.qa("Ask for the same policy illustrated at a lower scale",
              "Most carriers can produce an illustration at a reduced dividend scale on request. "
              "Comparing it against the current scale version shows you how much of the outcome "
              "depends on a decision nobody has made yet. If the two versions look very different, "
              "you have learned something important about the proposal.", "mt-8")}
      </div>
    </div>
  </div>
</section>


<!-- The soft CTA. No amber, no form: this reader is evaluating, not buying,
     and the honest next step is a document rather than a call script. -->
<section class="section-tight">
  <div class="container-ax">
    <div class="reveal card measure">
      <h2 class="text-h4">See an illustration with both columns</h2>
      <p class="mt-3 text-slate">
        We will send you a current illustration from a named carrier for your age, with the
        guaranteed and non guaranteed columns shown separately and the dividend scale it was run at
        pointed out. We will do that whether or not you intend to buy anything, and we will tell
        you if the guaranteed columns alone do not support what is being proposed.
      </p>
      <div class="mt-5 flex flex-wrap items-center gap-4">
        <a class="btn btn-ghost" href="/whole-life-insurance/quotes/">Request a policy illustration</a>
        {C.phone_link("whole_dividends_soft", "link-static inline-flex items-center gap-2 text-sm",
                      "or call " + C.PHONE_DISPLAY, 18)}
      </div>
    </div>
  </div>
</section>


{C.spoke_module("Related pages in whole life",
                "Dividends are one discretionary layer on a contract that is mostly guarantees. "
                "These cover the rest of it.", SIBLINGS)}


{C.faq_section("Questions about whole life dividends", FAQ, "whole-div-faq")}


{C.byline_section()}
"""
