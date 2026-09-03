# -*- coding: utf-8 -*-
"""WHOLE LIFE FOR SENIORS. Spec P2, template T4. PHONE WEIGHTED.

One of the two phone-first exceptions in this silo. The reason is the same as
on the term seniors page: after sixty five the answer turns on health answers
and on which carriers are appointed in the visitor's state, and a five field
form cannot get there.

The page carries a rate chart because the title promises rates, and it uses
rate_chart's "call" row CTA rather than the prefill button, which is what that
mode exists for on a phone weighted page: the click-to-call sits inside the age
cell so the table never needs a fourth column.

It also carries the silo's honest off ramp. Below roughly fifty thousand
dollars of face amount, the product built for the job is final expense, and
the sanctioned cross silo route is a link to that hub (spec s07 rule 3).
"""
import chrome as C

PATH = "/whole-life-insurance/for-seniors/"
OUT = "whole-life-insurance/for-seniors/index.html"
ACTIVE = "/whole-life-insurance/"
SILO = "whole-life"
TITLE = "Whole Life Insurance for Seniors: Rates & Acceptance | Apex"
OG_TITLE = "Whole life insurance for seniors"
DESC = ("What whole life insurance costs after 65, which underwriting route you are likely to be "
        "offered, and when a smaller final expense policy is the better answer.")

TRAIL = [("Home", "/"), ("Whole Life Insurance", "/whole-life-insurance/"),
         ("For seniors", None)]

AGE_BANDS = [("60 to 64", None), ("65 to 69", None), ("70 to 74", None),
             ("75 to 79", None), ("80 to 85", None)]
COVERAGE_COLS = ["$25,000", "$50,000", "$100,000"]

# The acceptance routes. Descriptions of how a programme behaves, not prices,
# so nothing in this table is a placeholder.
ROUTES = [
    ("Health questions",
     "A full application, medical records, and usually a paramedical exam.",
     "A short set of yes or no questions. No exam.",
     "None at all."),
    ("Who gets declined",
     "Applicants with serious or recent conditions. A decline here is common and is not the end of "
     "the road.",
     "Applicants who answer yes to a knockout question, which differs sharply between carriers.",
     "Nobody within the issue ages."),
    ("Waiting period before full benefit",
     "None. Full benefit from day one, subject to the two year contestability review.",
     "Often none, sometimes graded. It depends on which questions you answered yes to.",
     "Normally two years. Death from illness inside that window returns premiums plus interest, "
     "not the face amount."),
    ("Face amounts typically available",
     "The widest range, well into six figures.",
     "Moderate. Commonly up to the low tens of thousands.",
     "Smallest. Built for a funeral rather than a legacy."),
    ("Cost per thousand of coverage",
     "Lowest of the three.",
     "Higher. You pay for the carrier not looking closely.",
     "Highest of any life product sold."),
    ("Issue ages commonly written",
     "To around 80, and narrower above 75.",
     "To around 85.",
     "To around 85, occasionally higher."),
]

FAQ = [
    ("Can a 75 year old get whole life insurance?",
     "Yes. Most of our appointed carriers write whole life to around eighty five, and simplified "
     "issue and guaranteed acceptance policies are specifically designed for this age band. What "
     "narrows above seventy five is the face amount rather than the availability: the products "
     "still exist, and they are sized for a funeral and final bills rather than for income "
     "replacement."),
    ("Is whole life insurance a good idea for seniors?",
     "It is a good idea when the need is permanent and modest: a funeral, final medical bills, an "
     "outstanding debt, or a defined amount left to someone. It is a poor idea when it is being "
     "used as a savings vehicle late in life, because the cash value has very few years to do "
     "anything useful, or when the premium would strain a fixed income. A policy that lapses at "
     "eighty two because the premium became unaffordable is the worst outcome on this page, and "
     "it is avoided by buying an amount you can carry rather than the largest one you qualify for."),
    ("Do I have to take a medical exam?",
     "Usually not at these ages. Most whole life sold after sixty five is simplified issue, which "
     "means health questions and a prescription check rather than an exam. Fully underwritten "
     "whole life with an exam is still available and is the cheapest per thousand if your health "
     "supports it, so it is worth asking rather than assuming."),
    ("What is the difference between whole life and final expense insurance?",
     "Final expense is whole life. It is the same contract type, sold in smaller face amounts, "
     "with simplified underwriting and marketing aimed at covering a funeral. The guarantees are "
     "the same: level premium, permanent coverage, guaranteed cash value. If the amount you need "
     "is under about fifty thousand dollars, you are almost certainly looking for a final expense "
     "policy even if you searched for whole life."),
    ("Will my premium go up as I get older?",
     "No. That is the defining feature of the product. The premium is calculated once, at issue, "
     "from your age and health at that point, and it is guaranteed not to rise for as long as the "
     "policy is in force. This is the main reason people move from term to permanent coverage at "
     "this age: the term renewal premium does rise, every single year."),
]


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    route_rows = "\n            ".join(
        '<tr><th scope="row">%s</th><td>%s</td><td>%s</td><td>%s</td></tr>' % r for r in ROUTES)

    hero_cta = """<div class="reveal mt-8 flex flex-wrap items-center gap-4">
        %s
        <p class="text-micro text-muted">%s</p>
      </div>""" % (C.phone_link("whole_seniors_hero", "btn btn-call"), C.HOURS)

    return f"""
{C.page_hero(
    TRAIL,
    "Whole Life Insurance for Seniors",
    'After sixty five, <a class="link" href="/whole-life-insurance/">whole life insurance</a> is '
    'widely available and the premium is locked for life, which is exactly why people move to it '
    'at this age. What changes is the underwriting: most policies sold in this band are health '
    'questions rather than an exam, and a few ask nothing at all. This page covers what you are '
    'likely to be accepted for, what it costs, and the point at which a smaller policy is the '
    'better buy.',
    extra=hero_cta)}


<!-- =====================================================================
     ACCEPTANCE FIRST. The title promises rates and acceptance, and
     acceptance is the question that actually brought the visitor here.
     ================================================================== -->
<section class="pb-14 md:pb-16">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2">The three ways you can be accepted</h2>
      <p class="reveal mt-5 text-slate">
        All three produce a permanent policy with a level premium. They differ in what the carrier
        asks, what it costs, and whether the full benefit is payable from day one.
      </p>
    </div>

    <div class="reveal mt-8 table-scroll table-signature">
      <table class="compare-table" style="min-width:52rem">
        <caption class="sr-only">
          Fully underwritten, simplified issue, and guaranteed acceptance whole life compared.
        </caption>
        <thead>
          <tr>
            <th scope="col"><span class="sr-only">Feature</span></th>
            <th scope="col">Fully underwritten</th>
            <th scope="col">Simplified issue</th>
            <th scope="col">Guaranteed acceptance</th>
          </tr>
        </thead>
        <tbody>
            {route_rows}
        </tbody>
      </table>
    </div>

    <p class="reveal mt-6 text-slate max-w-3xl">
      Most people at these ages land in the middle column, and most people assume they belong in
      the right hand one. That assumption is expensive: guaranteed acceptance costs the most and
      carries a waiting period, and it is worth reaching for only after the middle column has
      actually said no. The detail on that product is on
      <a class="link" href="/whole-life-insurance/guaranteed-acceptance/">guaranteed acceptance
      whole life</a>.
    </p>
  </div>
</section>


<!-- =====================================================================
     THE RATE CHART. Row level click-to-call inside the age cell, which
     is what rate_chart's "call" mode is for on a phone weighted page.
     ================================================================== -->
<section class="section band" id="rates">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2">What it costs, by age</h2>
      <p class="reveal mt-5 text-slate">
        Monthly premium for a level benefit policy, non tobacco. Every row has a button that puts
        you through to a licensed agent who can price that band for your state and health in a few
        minutes.
      </p>
      <div class="reveal mt-6">
        {C.rates_flag("premiums")}
      </div>
    </div>

    {C.rate_chart(
        panels_id="whole-seniors-rates",
        cols=COVERAGE_COLS,
        rows=AGE_BANDS,
        toggles=[("Show premiums for", "wls-sex",
                  [("female", "Female"), ("male", "Male")], None)],
        caption="Monthly premium by age band and coverage amount.",
        row_cta="call",
        cta_location="whole_seniors_rate_row",
        min_width="40rem",
        top_margin="mt-8",
        aside="Non tobacco, level benefit. Tobacco rates are higher.")}

    <p class="reveal mt-8 text-slate max-w-3xl">
      Coverage above one hundred thousand dollars is routinely written at these ages and is priced
      the same way. The full grid, including the younger bands and the larger amounts, is on the
      <a class="link" href="/whole-life-insurance/rates/">whole life insurance rates</a> page.
    </p>
  </div>
</section>


{C.inline_cta(
    "One call settles which column you are in",
    "Tell a licensed agent your age, your state, and what you take. You will get a straight answer "
    "about whether you need to answer health questions at all, and what the difference costs. No "
    "application, and no obligation.",
    "whole_seniors_mid", "/whole-life-insurance/quotes/", "Or start a quote online",
    phone_first=True)}


<!-- =====================================================================
     THE OFF RAMP. Cross silo via the hub, per spec s07 rule 3.
     ================================================================== -->
<section class="section band-navy on-navy">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-6">
        <h2 class="reveal text-h2 text-white">If the amount you need is smaller</h2>
        <p class="reveal mt-5 text-white/85">
          Below roughly fifty thousand dollars of coverage, the product built for the job is sold
          under a different name:
          <a class="link !text-white" href="/final-expense-insurance/">final expense insurance</a>.
          It is the same contract, whole life, in a smaller size, with simplified underwriting and
          carriers who specialise in exactly this band.
        </p>
        <p class="reveal mt-5 text-white/85">
          The practical difference is who will write you and at what price. A carrier that is
          competitive at two hundred and fifty thousand dollars is frequently uncompetitive at
          fifteen thousand, and the reverse is just as true. Being appointed with both kinds is the
          only reason we can tell you which one you are.
        </p>
      </div>
      <div class="lg:col-span-5 lg:col-start-8">
        <div class="reveal card">
          <h3 class="text-h4 !text-ink">A rough rule that holds up</h3>
          <p class="mt-3 text-slate">
            If the purpose is a funeral and the bills that follow, you are looking for final
            expense. If the purpose includes leaving a meaningful amount behind, or covering an
            estate's liquidity, you are looking for whole life. If it is both, we quote both and
            you compare them on one call.
          </p>
          <div class="mt-5">
            {C.phone_link("whole_seniors_offramp", "btn btn-call btn-block")}
          </div>
          <p class="mt-3 text-micro text-muted text-center">{C.HOURS}</p>
        </div>
      </div>
    </div>
  </div>
</section>


{C.spoke_module(
    "Also in whole life insurance",
    "The pages most people read next when they are weighing this after sixty five.",
    [("/whole-life-insurance/what-is-whole-life-insurance/", "What whole life insurance is",
      "The definition and the mechanics, if you are starting fresh."),
     ("/whole-life-insurance/cash-value/", "How cash value works",
      "What it does, and what it realistically does after 65."),
     ("/whole-life-insurance/calculator/", "Whole life calculator",
      "Size the permanent need before you price it."),
     ("/whole-life-insurance/dividends/", "Dividends explained",
      "Why a non guaranteed column is not a promise."),
     ("/whole-life-insurance/is-it-worth-it/", "Is whole life worth it?",
      "The case for and against, side by side.")])}


{C.faq_section("Questions seniors ask about whole life", FAQ, "whole-seniors-faq")}


{C.byline_section()}
"""
