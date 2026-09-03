# -*- coding: utf-8 -*-
"""TERM LIFE RATES. Spec P1, template T2. Form weighted.

"Rate chart by age" is an explicit format request, so the chart is the page and
it comes first, before any prose. Everything below it explains how to read it.

The chart hosts row level "Quote this" buttons that prefill the quote form
further down the page, which is why the form is on this page at all: a prefill
target has to exist in the same document.

Every cell is `$--` by decision (MASTER.md line 23). The toggles drive the
caption, not the numbers, until the carrier rate cards land.
"""
import chrome as C
import term
from icons import icon

PATH = "/term-life-insurance/rates/"
OUT = "term-life-insurance/rates/index.html"
ACTIVE = "/term-life-insurance/"
SILO = "term-life"
TITLE = "Term Life Insurance Rates by Age (2026 Rate Chart)"
OG_TITLE = "Term life insurance rates by age"
DESC = ("Term life insurance rate chart by age, coverage amount, and term length, with male and "
        "female and tobacco splits. See what moves your rate and how to lower it.")

# 25 to 74 in five year bands. The mid age is what the row's quote button
# carries into the form, because a band cannot be typed into an age field.
AGE_BANDS = [("25 to 29", "27"), ("30 to 34", "32"), ("35 to 39", "37"), ("40 to 44", "42"),
             ("45 to 49", "47"), ("50 to 54", "52"), ("55 to 59", "57"), ("60 to 64", "62"),
             ("65 to 69", "67"), ("70 to 74", "72")]

COVERAGE_COLS = ["$100,000", "$250,000", "$500,000", "$750,000", "$1,000,000"]

FAQ = [
    ("What is the average cost of term life insurance?",
     "There is no useful average, which is why this page is a chart rather than a number. Age, "
     "term length, coverage amount, sex, tobacco use, and your health class each move the premium "
     "by more than any average would tell you. A healthy 30 year old and a healthy 55 year old "
     "buying the same policy are not in the same order of magnitude."),
    ("Why do term life rates go up so much with age?",
     "Because the price tracks the chance of a claim during the term, and that chance rises "
     "faster than most people expect after about 45. The practical consequence is that waiting a "
     "year to decide is not free. The same policy bought at 46 instead of 45 costs more for its "
     "whole term, and every year of waiting is also a year in which your health can change."),
    ("Do men and women pay different rates?",
     "Yes, in most states. Women statistically live longer, so the same coverage generally costs "
     "a woman less than a man of the same age and health. Montana requires unisex rates, so the "
     "split does not apply there."),
    ("How much more does tobacco cost?",
     "Commonly two to three times the non tobacco premium for the same coverage, which is the "
     "largest single lever on this page after age. Carriers define tobacco use differently, and a "
     "few treat occasional cigar use or nicotine replacement therapy more favourably than others, "
     "so it is worth telling us exactly what you use rather than answering a plain yes."),
    ("Are these rates guaranteed?",
     "No, and no rate chart anywhere is. A chart shows the shape of pricing for a rate class. "
     "Your rate class is decided by the carrier after underwriting, and until a policy is issued "
     "any figure is an illustration. We tell you which class we quoted you at, so you can see "
     "what would change if the carrier lands you somewhere else."),
]


def schema():
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("Term Life Insurance", "/term-life-insurance/"),
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
<!-- =====================================================================
     HERO. Short on purpose. T2 puts the chart first, so the hero is a
     heading and one paragraph, not a hero.
     ================================================================== -->
<section class="pt-6 pb-10 glow">
  <div class="container-ax">
    {C.crumbs([("Home", "/"), ("Term Life Insurance", "/term-life-insurance/"), ("Rates", None)])}

    <div class="mt-8 max-w-3xl">
      <h1 class="reveal text-h1">Term Life Insurance Rates by Age</h1>
      <p class="reveal mt-5 text-lead text-slate">
        The chart below is the full pricing grid for
        <a class="link" href="/term-life-insurance/">term life insurance</a>: age band by coverage
        amount, split by term length, sex, and tobacco use. Every row has a button that carries
        its numbers into the quote form further down, so you do not have to retype them.
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
        panels_id="term-rates-full",
        cols=COVERAGE_COLS,
        rows=[(band, {"age": mid, "coverage": "500000"}) for band, mid in AGE_BANDS],
        toggles=[("Term length", "tr-length",
                  [("20", "20 years"), ("10", "10 years"), ("15", "15 years"), ("30", "30 years")],
                  "term_length"),
                 ("Sex", "tr-sex", [("female", "Female"), ("male", "Male")], "sex"),
                 ("Tobacco", "tr-tobacco", [("no", "No"), ("yes", "Yes")], "tobacco")],
        caption="Monthly premium by age band and coverage amount.",
        row_cta="prefill",
        prefill_target="term-rates-quote-form",
        min_width="58rem",
        top_margin="mt-6",
        toggle_grid="grid sm:grid-cols-[8fr_4fr_4fr] gap-6 max-w-4xl")}

    <p class="reveal mt-6 text-slate max-w-3xl">
      Coverage above $1,000,000 is routinely available and is quoted the same way; it is left off
      the grid because at that point the carrier's underwriting programme matters more to the
      price than the column does. Terms of 10, 15, 20, and 30 years are the standard set. A few
      carriers write 25 and 35 year terms, and we will tell you when one is worth having.
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
        In rough order of size. The first two are worth more than everything below them put
        together, which is why the chart is built around them.
      </p>
    </div>

    <div class="mt-10 bento" data-stagger="40">
      {lever("Your age at application",
             "Not your age when you decide, your age when the carrier issues the policy. Some "
             "carriers price to your nearest birthday rather than your last, which can put you a "
             "year older than you think you are.",
             "Largest")}
      {lever("Tobacco and nicotine use",
             "Commonly two to three times the premium for the same coverage. Most carriers look "
             "at the last twelve months, some at the last two to five years for a preferred class.",
             "Very large")}
      {lever("Your health class",
             "Preferred plus, preferred, standard plus, standard, and then rated classes. Blood "
             "pressure, cholesterol, build, and family history decide this, and carriers disagree "
             "about all four.",
             "Large")}
      {lever("Term length and coverage amount",
             "A 30 year term costs meaningfully more than a 20. Coverage scales less than "
             "proportionally, so doubling the amount rarely doubles the premium.",
             "Moderate")}
      {lever("Sex and state",
             "Women generally pay less for the same coverage. Montana requires unisex rates. "
             "State also decides which carriers can write you at all.",
             "Moderate")}
      {lever("Occupation, travel, and hobbies",
             "Aviation, diving, climbing, and some occupations attract a flat extra or an "
             "exclusion rather than a worse class. Often smaller than people fear.",
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
        {C.step(1, "Apply to a different carrier",
                "The single biggest lever, and the one you cannot pull on your own. The same "
                "health history can land two classes apart at two carriers. This is what an "
                "independent agency is for.")}
        <div class="mt-8">
          {C.step(2, "Take the medical exam",
                  "If you are in good health, a fully underwritten policy with a paramedical exam "
                  "almost always beats the no exam version of the same coverage. The exam is free "
                  "and takes about twenty minutes at your home.")}
        </div>
        <div class="mt-8">
          {C.step(3, "Fix the fixable, then apply",
                  "Blood pressure and cholesterol readings respond to treatment within months, "
                  "and a class change is worth more than most people expect. Worth doing only if "
                  "you are not currently uninsured and exposed.",
                  "If you have no coverage at all right now, buy something first and improve on it later.")}
        </div>
        <div class="mt-8">
          {C.step(4, "Right size the term and the amount",
                  "A 30 year term when the mortgage has 18 years left is paying for 12 years you "
                  "do not need. Matching the term to the obligation is usually a bigger saving "
                  "than shaving the coverage amount.")}
        </div>
        <div class="mt-8">
          {C.step(5, "Ask about a reconsideration later",
                  "If you were rated for something that has since improved, most carriers will "
                  "reconsider the class after a period, typically a year, without a new policy.")}
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
        A rate chart is an illustration of shape. It shows how premiums move between ages, terms,
        and coverage amounts. It cannot show what a carrier will decide about you, and any chart
        that claims otherwise is selling you a number it does not have.
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
        <h3 class="text-h4 text-white">Carriers differ by state</h3>
        <p class="mt-3 text-white/85">
          Product availability, riders, and pricing all vary. The carrier that is cheapest in one
          state may not write in yours at all.
        </p>
      </div>
      <div class="reveal">
        <h3 class="text-h4 text-white">Underwriting is about you</h3>
        <p class="mt-3 text-white/85">
          Build, family history, prescriptions, and your driving record are all read together. A
          chart cannot know any of them.
        </p>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     THE FORM. Present because the chart's row buttons need a prefill
     target in this document. Secondary to the chart, so it sits here
     rather than in the hero.
     ================================================================== -->
<section class="section" id="quote">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">Get the real number</h2>
        <p class="reveal mt-5 text-slate">
          Six questions, about two minutes. A licensed agent comes back within {C.SLA} with
          premiums from named carriers at a class we can defend, rather than a chart cell.
        </p>
        <p class="reveal mt-5 text-slate">
          If you used a "Quote this" button above, your age and coverage are already filled in and
          the form has skipped to what is still missing.
        </p>
        <div class="reveal mt-6 pt-6 border-t border-rule">
          <p class="text-slate">Or talk it through with a licensed agent.</p>
          <div class="mt-4">{C.phone_link("term_rates_form", "btn btn-call")}</div>
          <p class="mt-3 text-micro text-muted">{C.HOURS}</p>
        </div>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <div class="reveal panel">
          {term.quote_form("term-rates-quote-form", "term_rates_quote", "trq")}
        </div>
      </div>
    </div>
  </div>
</section>


{C.faq_section("Questions about term life rates", FAQ, "term-rates-faq")}


<section class="section-tight band">
  <div class="container-ax">
    <div class="reveal">{C.byline()}</div>
  </div>
</section>
"""
