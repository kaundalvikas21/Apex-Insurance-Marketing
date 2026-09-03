# -*- coding: utf-8 -*-
"""WHOLE LIFE RATES. Spec P1, template T2. Form and phone at equal weight.

Same shape as /term-life-insurance/rates/: the chart is the page and it comes
first, before any prose. Two differences follow from the product.

There is no term length toggle, because there is no term. What there is
instead is a paid-up question, and it is deliberately NOT a toggle: a ten pay
or twenty pay whole life policy is a different contract rather than a different
cell, and putting it on a switch beside sex and tobacco would imply the chart
could price it. It is handled in prose under the chart.

Every cell is `$--` by decision (MASTER.md line 23). The toggles drive the
caption, not the numbers, until the carrier rate cards land.

Coverage columns match whole.quote_form()'s coverage select exactly, because
the row buttons prefill into it and an amount the select does not offer would
silently blank the field.
"""
import chrome as C
import whole

PATH = "/whole-life-insurance/rates/"
OUT = "whole-life-insurance/rates/index.html"
ACTIVE = "/whole-life-insurance/"
SILO = "whole-life"
TITLE = "Whole Life Insurance Rates by Age (2026 Rate Chart)"
OG_TITLE = "Whole life insurance rates by age"
DESC = ("Whole life insurance rate chart by age and coverage amount, with male and female and "
        "tobacco splits. What moves a permanent premium, and how to lower one you were quoted.")

# 30 to 79 in five year bands. The mid age is what the row's quote button
# carries into the form, because a band cannot be typed into an age field.
AGE_BANDS = [("30 to 34", "32"), ("35 to 39", "37"), ("40 to 44", "42"), ("45 to 49", "47"),
             ("50 to 54", "52"), ("55 to 59", "57"), ("60 to 64", "62"), ("65 to 69", "67"),
             ("70 to 74", "72"), ("75 to 79", "77")]

# Must stay identical to whole.quote_form()'s coverage select.
COVERAGE_COLS = ["$25,000", "$50,000", "$100,000", "$250,000", "$500,000"]

# The coverage a row's button carries. Falls with age because that is what
# people actually buy at these ages, and a prefill that has to be corrected is
# worse than one that is close.
ROW_COVERAGE = {"30 to 34": "250000", "35 to 39": "250000", "40 to 44": "250000",
                "45 to 49": "100000", "50 to 54": "100000", "55 to 59": "100000",
                "60 to 64": "50000", "65 to 69": "50000", "70 to 74": "25000",
                "75 to 79": "25000"}

FAQ = [
    ("What is the average cost of whole life insurance?",
     "There is no useful average, which is why this page is a chart rather than a number. Age, "
     "coverage amount, sex, tobacco use, health class, and how long you intend to pay premiums "
     "for each move the figure by more than any average would tell you. What is fair to say is "
     "the shape: for the same death benefit, whole life costs several times what term costs, "
     "because the policy is designed to still be in force on the day you die rather than to "
     "expire before it."),
    ("Why is whole life so much more expensive than term?",
     "Because a term policy is priced on the chance you die during the term, and most people do "
     "not, so most term policies never pay a claim. A whole life policy is priced on the "
     "certainty that it will pay one eventually, plus the cash value it is required to build "
     "along the way. You are not paying more for the same thing. You are paying for a different "
     "thing, and whether that thing is worth it depends entirely on whether the need is "
     "permanent."),
    ("Does the premium ever go up?",
     "Not on a level premium whole life policy. The premium is fixed in the contract at issue and "
     "cannot be raised by the carrier, which is one of the three guarantees this product is sold "
     "on. That is not true of every permanent product: universal life premiums can and do need "
     "topping up, which is a different conversation."),
    ("Do men and women pay different rates?",
     "Yes, in most states. Women statistically live longer, so the same coverage generally costs "
     "a woman less than a man of the same age and health. Montana requires unisex rates, so the "
     "split does not apply there."),
    ("How much more does tobacco cost?",
     "Commonly two to three times the premium for the same coverage, and on a permanent policy "
     "you carry that difference for the rest of your life rather than for a term. Most carriers "
     "ask about the last twelve months. Some will reconsider the class after a documented period "
     "without nicotine, which is worth asking about rather than assuming."),
    ("Can I get whole life without answering health questions?",
     "Yes, through a guaranteed acceptance policy, and it is the most expensive way to buy a "
     "dollar of death benefit that we offer. It also carries a waiting period for natural causes. "
     "It is a real answer for people who have no other one, and a poor answer for anyone who "
     "could pass a simplified issue health questionnaire instead."),
]


def schema():
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("Whole Life Insurance", "/whole-life-insurance/"),
                           ("Rates", None)]),
            C.faq_schema(FAQ),
            C.person_schema(PATH)]


def lever(title, body, weight):
    return f"""<div class="reveal bento-cell bento-2">
        <p class="text-micro font-semibold uppercase tracking-[0.12em] text-muted">{weight}</p>
        <h3 class="mt-2 text-h4">{title}</h3>
        <p class="mt-3 text-slate">{body}</p>
      </div>"""


def body():
    return f"""
<section class="pt-6 pb-10 glow">
  <div class="container-ax">
    {C.crumbs([("Home", "/"), ("Whole Life Insurance", "/whole-life-insurance/"), ("Rates", None)])}

    <div class="mt-8 max-w-3xl">
      <h1 class="reveal text-h1">Whole Life Insurance Rates by Age</h1>
      <p class="reveal mt-5 text-lead text-slate">
        The chart below is the pricing grid for
        <a class="link" href="/whole-life-insurance/">whole life insurance</a>: age band by
        coverage amount, split by sex and tobacco use. The premium in each cell is the one you
        would keep paying for the rest of your life, which is the single most important thing to
        understand before reading any of it. Every row has a button that carries its numbers into
        the quote form further down.
      </p>
    </div>
  </div>
</section>


<!-- =====================================================================
     THE CHART. First real section on the page, per T2.
     ================================================================== -->
<section class="pb-14 md:pb-16" id="chart">
  <div class="container-ax">
    <div class="reveal max-w-3xl">
      {C.rates_flag("premiums")}
    </div>

    {C.rate_chart(
        panels_id="whole-rates-full",
        cols=COVERAGE_COLS,
        rows=[(band, {"age": mid, "coverage": ROW_COVERAGE[band]}) for band, mid in AGE_BANDS],
        toggles=[("Sex", "wr-sex", [("female", "Female"), ("male", "Male")], "sex"),
                 ("Tobacco", "wr-tobacco", [("no", "No"), ("yes", "Yes")], "tobacco")],
        caption="Monthly premium for a level premium, participating whole life policy by age band "
                "and coverage amount.",
        row_cta="prefill",
        prefill_target="whole-rates-quote-form",
        min_width="56rem",
        top_margin="mt-6",
        toggle_grid="grid sm:grid-cols-2 gap-6 max-w-lg")}

    <p class="reveal mt-6 text-slate max-w-3xl">
      The grid prices a policy you pay for as long as you live. A ten pay or twenty pay policy
      compresses the same coverage into fewer, larger premiums and is a different contract rather
      than a different cell, so it is quoted rather than charted. Issue ages above this grid are
      routinely available and are covered on
      <a class="link" href="/whole-life-insurance/for-seniors/">whole life for seniors</a>. If your
      health would not pass a questionnaire at all, the relevant page is
      <a class="link" href="/whole-life-insurance/guaranteed-acceptance/">guaranteed acceptance
      whole life</a>, which is priced well above anything here.
    </p>
  </div>
</section>


<!-- =====================================================================
     WHAT MOVES YOUR RATE. T2, ordered by how much each lever is worth.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">What actually moves your rate</h2>
      <p class="reveal mt-5 text-slate">
        In rough order of size. On a permanent policy the first two are worth more than everything
        below them put together, and unlike a term policy you carry the difference for life.
      </p>
    </div>

    <div class="mt-10 bento" data-stagger="40">
      {lever("Your age at application",
             "Not your age when you decide, your age when the carrier issues the policy. On a "
             "permanent policy this sets a premium you pay for decades, so a year of waiting is "
             "the most expensive year on this list. Some carriers price to your nearest birthday "
             "rather than your last.",
             "Largest")}
      {lever("Tobacco and nicotine use",
             "Commonly two to three times the premium for the same coverage, held for the rest of "
             "your life rather than for a term. Most carriers look at the last twelve months.",
             "Very large")}
      {lever("How long you pay premiums for",
             "A policy paid up at 65, or in ten or twenty years, costs far more per month than "
             "one you pay for life, because the same money is being collected over fewer years. "
             "It is not a worse deal, it is a different schedule.",
             "Large")}
      {lever("Your health class",
             "Preferred plus down through standard, then rated classes and, at the far end, "
             "simplified issue and guaranteed acceptance. Build, blood pressure, prescriptions, "
             "and family history decide this, and carriers disagree about all four.",
             "Large")}
      {lever("Coverage amount",
             "Scales less than proportionally, so doubling the face amount rarely doubles the "
             "premium. Carriers also set band breaks, and being just over one is cheaper per "
             "dollar than being just under it.",
             "Moderate")}
      {lever("Riders you attach",
             "A waiver of premium, a child rider, or an accelerated death benefit each add cost. "
             "Some are worth it and some are sold because they are easy to sell. Ask what each "
             "one costs as a line item rather than accepting a bundled premium.",
             "Situational")}
    </div>
  </div>
</section>


<!-- =====================================================================
     HOW TO LOWER A QUOTED RATE. T2. Legitimate levers only.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">How to lower a rate you have been quoted</h2>
        <p class="reveal mt-5 text-slate">
          All of these are legitimate. None of them involves leaving something off an application,
          which is not a discount, it is a reason for a claim to be contested.
        </p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        {C.step(1, "Ask whether the need is actually permanent",
                "The largest saving available on this page is discovering that you needed twenty "
                "years of cover rather than lifelong cover. That is not a rate reduction, it is a "
                "different product, and it is the honest first question.")}
        <div class="mt-8">
          {C.step(2, "Apply to a different carrier",
                  "The same health history can land two classes apart at two carriers, and on a "
                  "permanent policy that gap compounds for decades. This is what an independent "
                  "agency is for, and it is the lever you cannot pull on your own.")}
        </div>
        <div class="mt-8">
          {C.step(3, "Take the full underwriting route",
                  "If you are in reasonable health, a fully underwritten policy with a "
                  "paramedical exam almost always beats the simplified issue version of the same "
                  "coverage. The exam is free and takes about twenty minutes at your home.",
                  "Simplified issue exists for people who would fail an exam, not as a convenience upgrade.")}
        </div>
        <div class="mt-8">
          {C.step(4, "Right size the face amount",
                  "Permanent coverage is usually bought for a specific, bounded job: a funeral, a "
                  "final tax bill, a legacy of a stated size. Sizing it to that job rather than "
                  "to a round number is normally a bigger saving than any class improvement.")}
        </div>
        <div class="mt-8">
          {C.step(5, "Strip the riders you were not asking for",
                  "Ask for the premium with and without each rider. Anything you cannot explain "
                  "the purpose of back to the agent is a line you can probably remove.")}
        </div>
        <div class="mt-8">
          {C.step(6, "Split the need between two policies",
                  "A small permanent policy for the part of the need that never goes away, plus "
                  "term for the part that does, often costs less than one large permanent policy "
                  "and covers the same exposure.")}
        </div>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     WHY OUR NUMBERS MAY DIFFER FROM YOUR QUOTE. T2. The honesty section
     that stops a rate chart being read as a promise.
     ================================================================== -->
<section class="section band-navy on-navy">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2 text-white">Why your quote may not match this chart</h2>
      <p class="reveal mt-5 text-white/85">
        A rate chart is an illustration of shape. It shows how premiums move between ages and
        coverage amounts. It cannot show what a carrier will decide about you, and any chart that
        claims otherwise is selling you a number it does not have.
      </p>
    </div>
    <div class="mt-10 grid md:grid-cols-3 gap-6 max-w-5xl" data-stagger="60">
      <div class="reveal">
        <h3 class="text-h4 text-white">A chart assumes a rate class</h3>
        <p class="mt-3 text-white/85">
          Usually the best or second best. Most applicants are issued at standard or standard
          plus, which is a different number and an entirely normal outcome.
        </p>
      </div>
      <div class="reveal">
        <h3 class="text-h4 text-white">A premium is not the whole contract</h3>
        <p class="mt-3 text-white/85">
          Two policies at the same premium can build very different guaranteed cash value. Compare
          the guaranteed columns of the illustrations, not the monthly figures.
        </p>
      </div>
      <div class="reveal">
        <h3 class="text-h4 text-white">Carriers differ by state</h3>
        <p class="mt-3 text-white/85">
          Product availability, riders, minimum face amounts, and pricing all vary. The carrier
          that is cheapest in one state may not write in yours at all.
        </p>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     THE FORM. Present because the chart's row buttons need a prefill
     target in this document. The phone sits level with it, per the silo's
     CTA parity rule.
     ================================================================== -->
<section class="section" id="quote">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">Get the real number</h2>
        <p class="reveal mt-5 text-slate">
          Five questions, about two minutes. A licensed agent comes back within {C.SLA} with
          premiums from named carriers at a class we can defend, rather than a chart cell. Ask for
          a full illustration and we will order the carrier's own document, with the guaranteed
          columns kept visibly apart from the projected ones.
        </p>
        <p class="reveal mt-5 text-slate">
          If you used a "Quote this" button above, your age and coverage are already filled in and
          the form has skipped to what is still missing.
        </p>
        <div class="reveal mt-6 pt-6 border-t border-rule">
          <p class="text-slate">Or talk it through with a licensed agent. Same person, same
          comparison, and you can ask the awkward questions as they come up.</p>
          <div class="mt-4">{C.phone_link("whole_rates_form", "btn btn-call")}</div>
          <p class="mt-3 text-micro text-muted">{C.HOURS}</p>
        </div>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <div class="reveal panel">
          {whole.quote_form("whole-rates-quote-form", "whole_rates_quote", "wrq")}
        </div>
      </div>
    </div>
  </div>
</section>


{C.faq_section("Questions about whole life rates", FAQ, "whole-rates-faq")}


<section class="section-tight band">
  <div class="container-ax">
    <div class="reveal">{C.byline()}</div>
  </div>
</section>
"""
