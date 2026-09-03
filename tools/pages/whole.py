# -*- coding: utf-8 -*-
"""WHOLE LIFE HUB. Spec section 03. Split CTA at genuine parity.

Form and phone get equal visual weight: same height, same width, same optical
mass. Gold on the form CTA, solid navy on the phone CTA. Parity is by weight,
not by making both of them gold.

Section 7b, "who this does not suit", carries the same prominence as 7a. Per
the spec it is the strongest E-E-A-T signal on the page, so it is a full
column beside its opposite rather than a footnote under it.
"""
from icons import icon
import chrome as C
import forms as F

PATH = "/whole-life-insurance/"
OUT = "whole-life-insurance/index.html"
ACTIVE = PATH
SILO = "whole-life"
TITLE = "Whole Life Insurance: Guarantees, Cash Value, and Cost | Apex"
OG_TITLE = "Whole life insurance, explained without the sales pitch"
DESC = ("Whole life insurance guarantees a death benefit, a level premium, and a cash value. "
        "See how it works, what it costs against term, and who it genuinely does not suit.")

FAQ = [
    ("What makes whole life insurance permanent?",
     "Three things are contractually guaranteed for as long as you pay the premium: the death "
     "benefit, the premium amount, and a schedule of guaranteed cash values. There is no term to "
     "outlive and the carrier cannot cancel the policy or re-rate you because your health changed. "
     "That contractual certainty is what you are paying the extra premium for."),
    ("How much more does whole life cost than term?",
     "For the same death benefit at the same age, whole life commonly costs several times what a "
     "20 year term policy costs. The gap is largest when you are young, because term is cheapest "
     "then. This is not a hidden markup: you are buying coverage for 50 years instead of 20, plus "
     "a guaranteed cash value, so the money has to come from somewhere."),
    ("Are dividends guaranteed?",
     "No. Dividends are not guaranteed. A participating policy from a mutual carrier may pay a "
     "dividend when the company's actual mortality, expense, and investment results are better "
     "than the conservative assumptions priced into the policy. Some carriers have paid one every "
     "year for a very long time, which is a real track record and still not a guarantee. Any "
     "illustration showing a non guaranteed column is showing an assumption, and the guaranteed "
     "column is the only one you are entitled to."),
    ("Can I take money out of the cash value?",
     "Yes, by policy loan or by surrender, and both have consequences. A loan accrues interest and "
     "reduces the death benefit by the outstanding balance if it is not repaid. A surrender ends "
     "the policy, and any gain above your cost basis is taxable. Taking too much out can also "
     "cause the policy to lapse, which can trigger a tax bill on gains you no longer have. Ask for "
     "the numbers before you borrow, not after."),
    ("What is a guaranteed acceptance policy?",
     "It is a whole life policy issued with no health questions and no exam, so nobody is turned "
     "down within the eligible ages. In exchange the coverage amount is small, the premium per "
     "dollar of coverage is the highest of any product we offer, and there is a two or three year "
     "waiting period for death from natural causes. It exists for people who cannot qualify any "
     "other way, and it should be the last option considered, not the first."),
    ("Is whole life a good investment?",
     "It is not an investment, and treating it as one usually ends badly. It is insurance with a "
     "guaranteed savings component attached, priced accordingly. Cash value grows slowly in the "
     "early years and there is often little or none in the first two or three. If your goal is "
     "returns rather than a guaranteed death benefit, almost any comparison starts by asking "
     "whether you have filled your tax advantaged retirement accounts first."),
    ("What happens if I stop paying the premium?",
     "You have options rather than an automatic loss. If there is enough cash value, the policy "
     "can pay its own premium for a while, or convert to a smaller paid up policy that needs no "
     "further payments, or be surrendered for its cash value. In the first few years, when there "
     "is little or no cash value, stopping usually means losing the policy and what you paid in. "
     "That is the main risk of buying more whole life than you can comfortably sustain."),
    ("Do I need a medical exam?",
     "Usually yes for a fully underwritten policy, which is also where the best pricing is. Some "
     "carriers offer accelerated underwriting on smaller face amounts for healthy applicants. "
     "Simplified issue and guaranteed acceptance need no exam at all, and cost more."),
]

SPOKES = [
    ("/whole-life-insurance/quotes/", "Whole life quotes", "What we need from you, and what comes back."),
    ("/whole-life-insurance/rates/", "Whole life rates", "Premium by age and coverage, from current rate cards."),
    ("/whole-life-insurance/calculator/", "Whole life calculator", "Model premium against cash value over time."),
    ("/whole-life-insurance/what-is-whole-life-insurance/", "What whole life insurance is", "The plain definition, with the fine print left in."),
    ("/whole-life-insurance/guaranteed-acceptance/", "Guaranteed acceptance whole life", "No health questions, and what that costs you."),
    ("/whole-life-insurance/for-seniors/", "Whole life for seniors", "What is available after 65 and what it is for."),
    ("/whole-life-insurance/cash-value/", "How cash value works", "Growth, loans, surrender, and the tax treatment."),
    ("/whole-life-insurance/dividends/", "Dividends and participating policies", "How they are declared and why they are not guaranteed."),
    ("/whole-life-insurance/is-it-worth-it/", "Is whole life worth it?", "The honest case for and against, side by side."),
]


def schema():
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("Whole Life Insurance", None)]),
            C.faq_schema(FAQ),
            C.person_schema(PATH)]


def _acc(q, a):
    return C.acc(q, a, "wl-faq")


ERR = icon("circle-alert", 16, "shrink-0 mt-px")


REQUEST_TYPE_FIELD = '''<!-- Flipped to "illustration" by the tertiary CTA below. -->
<input type="hidden" name="request_type" value="quote">'''


def quote_form(form_id="wl-quote-form", form_name="wl_hero_quote", id_prefix="wl"):
    """Five fields, one step. Equal partner to the phone CTA beside it.

    Parameterised so the whole life spokes can host their own copy: two forms
    posting the same data-form-name would make the GA4 form_submit event
    useless for telling the hub apart from the calculator.
    """
    p = id_prefix
    return f"""
        <form id="{form_id}" class="mt-6" data-ax-form data-silo="whole-life"
              data-form-name="{form_name}" data-success-target="{p}-success" novalidate>

          {F.scaffold(REQUEST_TYPE_FIELD, 10)}

          <div class="grid sm:grid-cols-2 gap-x-4">
            <div class="field">
              <label class="field-label" for="{p}-age">Your age</label>
              <input class="input" id="{p}-age" name="age" type="text" inputmode="numeric"
                     required data-validate="age" data-error="Enter an age between 18 and 85.">
              <p class="field-error">{ERR}<span></span></p>
            </div>

            <div class="field" data-error="Choose one so we can price it correctly.">
              <span class="field-label" id="{p}-sex-label">Sex</span>
              <div class="choice-row" role="group" aria-labelledby="{p}-sex-label">
                <label class="choice"><input type="radio" name="sex" value="female" required><span>Female</span></label>
                <label class="choice"><input type="radio" name="sex" value="male" required><span>Male</span></label>
              </div>
              <p class="field-error">{ERR}<span></span></p>
            </div>
          </div>

          <div class="field">
            <label class="field-label" for="{p}-state">Your state</label>
            <select class="select" id="{p}-state" name="state" required data-error="Please choose your state.">
              <option value="">Choose your state</option>
              {C.state_options()}
            </select>
            <p class="field-error">{ERR}<span></span></p>
          </div>

          <div class="field">
            <label class="field-label" for="{p}-coverage">Coverage you have in mind
              <span class="field-hint block font-normal">A rough figure is fine. We will talk it through.</span>
            </label>
            <select class="select" id="{p}-coverage" name="coverage" required
                    data-error="Choose an amount, or pick the closest.">
              <option value="">Choose an amount</option>
              <option value="25000">$25,000</option>
              <option value="50000">$50,000</option>
              <option value="100000">$100,000</option>
              <option value="250000">$250,000</option>
              <option value="500000">$500,000 or more</option>
              <option value="unsure">Not sure yet</option>
            </select>
            <p class="field-error">{ERR}<span></span></p>
          </div>

          <div class="field">
            <label class="field-label" for="{p}-phone">Best number to reach you</label>
            <input class="input" id="{p}-phone" name="phone" type="tel" autocomplete="tel"
                   required data-validate="phone" data-error="Enter a 10 digit phone number.">
            <p class="field-error">{ERR}<span></span></p>
          </div>

          <p id="{p}-illustration-note" data-prefill-note hidden
             class="flag !bg-navy-050 !border-navy !text-navy mb-4">
            {icon("file-text", 16, "inline-block align-text-bottom mr-1")}
            You have asked for a full illustration. We will send the guaranteed and non guaranteed
            columns side by side, with the carrier named.
          </p>

          {F.consent_block(p, C.BRAND, 10)}

          <button type="submit" class="btn btn-cta btn-block">Get whole life quotes</button>
          <p class="field-error" data-form-error>{ERR}<span></span></p>
          <p class="mt-3 text-micro text-muted">Free &#183; No obligation &#183; Licensed agents</p>
        </form>

        <div id="{p}-success" class="success">
          <div class="flex items-start gap-3">
            {icon("circle-check", 30, "shrink-0 text-green")}
            <div>
              <h3 class="text-h3 !font-display !font-semibold">Got it</h3>
              <p class="mt-3 text-slate">
                A licensed agent is putting your comparison together now. You will get named
                carriers, the guaranteed numbers, and where a figure is an assumption rather than a
                guarantee we will say so on the page it appears.
              </p>
              <div class="mt-5">
                {C.phone_link(p + "_success", "btn btn-call", "Or call " + C.PHONE_DISPLAY)}
              </div>
            </div>
          </div>
        </div>"""


def cash_value_chart():
    """Shape only. No numbers on the value axis, because a number there would
    be a projection, and we do not have carrier data to project from."""
    return """
      <figure class="reveal bento-cell bento-4">
        <figcaption class="text-h4">What the first forty years usually look like</figcaption>
        <p class="mt-2 text-sm text-muted">
          Cash value starts behind what you have paid in, catches up somewhere in the second
          decade, and passes it after that. Where that crossover falls depends entirely on the
          carrier, your age, and the policy design.
        </p>

        <svg class="chart mt-6" viewBox="0 0 640 300" role="img"
             aria-label="Line chart. A dashed line rises in a straight line, showing cumulative premiums paid. A solid line starts at zero, stays below the dashed line for roughly the first twelve to fifteen policy years, crosses it, and finishes above it, showing guaranteed cash value.">

          <line class="chart-grid" x1="56" y1="40"  x2="620" y2="40"></line>
          <line class="chart-grid" x1="56" y1="105" x2="620" y2="105"></line>
          <line class="chart-grid" x1="56" y1="170" x2="620" y2="170"></line>
          <line class="chart-grid" x1="56" y1="235" x2="620" y2="235"></line>
          <line class="chart-axis" x1="56" y1="20"  x2="56"  y2="260"></line>
          <line class="chart-axis" x1="56" y1="260" x2="620" y2="260"></line>

          <path class="chart-fill chart-fade"
                d="M56,260 C170,246 250,220 320,178 C400,130 500,80 620,52 L620,260 Z"></path>

          <path class="chart-line chart-premium chart-fade-early" d="M56,260 L620,72"></path>
          <path class="chart-line chart-value chart-draw"
                d="M56,260 C170,246 250,220 320,178 C400,130 500,80 620,52"></path>

          <g class="chart-fade">
            <line class="chart-marker" x1="330" y1="20" x2="330" y2="260"></line>
            <circle cx="330" cy="172" r="4.5" fill="#0A1F44"></circle>
            <text class="chart-label" x="338" y="36" font-weight="600" fill="#0A1F44">Crossover</text>
          </g>

          <text class="chart-label" x="56"  y="280" text-anchor="middle">Year 0</text>
          <text class="chart-label" x="197" y="280" text-anchor="middle">10</text>
          <text class="chart-label" x="338" y="280" text-anchor="middle">20</text>
          <text class="chart-label" x="479" y="280" text-anchor="middle">30</text>
          <text class="chart-label" x="620" y="280" text-anchor="middle">40</text>
          <text class="chart-label" x="18" y="145" transform="rotate(-90 18 145)" text-anchor="middle">Dollars</text>
        </svg>

        <div class="mt-4 flex flex-wrap gap-x-8 gap-y-2">
          <span class="inline-flex items-center gap-2 text-sm">
            <span class="w-7 border-t-2 border-dashed border-muted"></span>Total premiums paid
          </span>
          <span class="inline-flex items-center gap-2 text-sm">
            <span class="w-7 border-t-2 border-navy-700"></span>Guaranteed cash value
          </span>
        </div>

        <p class="flag mt-6">
          Illustrative shape only. This chart carries no dollar amounts and is not a quote, a
          projection, or a carrier illustration. Guaranteed cash values differ by carrier, age,
          health, coverage amount, and policy design. Ask us for a real illustration with the
          guaranteed column shown separately.
        </p>
      </figure>"""


def body():
    permanence_media = C.figure("whole-permanence", "(min-width: 1024px) 38vw, 92vw",
                                cls="reveal mt-8", glow=True)
    acceptance_media = C.picture("whole-acceptance", "(min-width: 1024px) 38vw, 92vw",
                                 cls="media media-strip !rounded-none", img_cls="media-img")
    # Mid-page banner, placed after the cash value proof and before the
    # who-it-suits split, at roughly 60% scroll depth.
    legacy_band = C.banner(
        "whole-band",
        "The number does not move for the rest of your life",
        "The premium is fixed, the death benefit is guaranteed, and the cash value is contractual. "
        "Tell us your age and what you want it to do, and a licensed agent comes back with named "
        "carriers and the guaranteed columns, not an illustration.",
        '<a class="btn btn-cta btn-block" href="#quote" data-cta-location="whole_band">'
        'Get my whole life quotes</a>'
        + C.phone_link("whole_band", "btn btn-ghost btn-block mt-3",
                       "Call " + C.PHONE_DISPLAY, 20),
        eyebrow="Guaranteed, not projected")
    spokes = C.spoke_module(
        "Explore whole life insurance",
        "Nine pages covering the parts of whole life that need more than a paragraph.",
        SPOKES)
    faq_html = "\n        ".join(_acc(q, a) for q, a in FAQ)
    byline = C.byline()

    return f"""
<!-- =====================================================================
     HERO. Dual CTA at genuine parity: the form panel and the call panel are
     the same width, the same height, and the same optical weight.
     ================================================================== -->
<section class="pt-6 pb-14 md:pb-16 glow">
  <div class="container-ax">
    {C.crumbs([("Home", "/"), ("Whole Life Insurance", None)])}

    <div class="mt-8 max-w-3xl">
      <h1 class="reveal text-h1">Whole Life Insurance</h1>
      <p class="reveal mt-5 text-lead text-slate">
        Coverage that does not expire, a premium that does not rise, and a cash value that is
        guaranteed in the contract. It costs considerably more than term, and this page explains
        exactly when that trade is worth making and when it is not.
      </p>
    </div>

    <div class="mt-10 grid lg:grid-cols-2 gap-6 items-stretch" id="quote">

      <div class="panel reveal flex flex-col">
        <h2 class="text-h3 !font-display !font-semibold">Compare quotes</h2>
        <p class="mt-2 text-sm text-muted">Five questions. A licensed agent replies within {C.SLA}.</p>
        {quote_form()}
      </div>

      <div class="panel reveal flex flex-col">
        <h2 class="text-h3 !font-display !font-semibold">Or talk to a licensed agent</h2>
        <p class="mt-2 text-sm text-muted">
          Whole life has more moving parts than term. Most people find it faster to ask.
        </p>

        <div class="mt-6">
          {C.phone_link("wl_hero_call", "btn btn-call btn-block !min-h-[64px] !text-lead", "Call " + C.PHONE_DISPLAY, 24)}
          <p class="mt-3 text-micro text-muted">{C.HOURS}</p>
        </div>

        <ul class="mt-8 grid gap-4">
          <li class="flex items-start gap-3">{icon("check", 20, "shrink-0 text-green mt-1")}<span class="text-sm">We name the carrier and show the guaranteed column separately</span></li>
          <li class="flex items-start gap-3">{icon("check", 20, "shrink-0 text-green mt-1")}<span class="text-sm">We will tell you if term is the better answer for you</span></li>
          <li class="flex items-start gap-3">{icon("check", 20, "shrink-0 text-green mt-1")}<span class="text-sm">No obligation, and your details are never sold on</span></li>
        </ul>

        <div class="mt-auto pt-8">
          <p class="text-sm font-semibold text-navy">Want the full numbers in writing?</p>
          <p class="mt-2 text-sm text-muted">
            An illustration shows the guaranteed and non guaranteed columns year by year for the
            whole life of the policy.
          </p>
          <button type="button" class="btn btn-ghost btn-block mt-4"
                  data-prefill='{{"request_type":"illustration"}}'
                  data-prefill-target="wl-quote-form"
                  data-prefill-reveal="wl-illustration-note">
            {icon("file-text", 20, "shrink-0")}Request an illustration
          </button>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Trust strip, within one viewport of both CTAs. -->
<section class="border-y border-rule bg-surface">
  <div class="container-ax py-6">
    <div class="flex flex-wrap items-center justify-between gap-x-8 gap-y-3 trust-strip">
      <span class="inline-flex items-center gap-2 text-navy font-semibold">
        {icon("shield-check", 18, "shrink-0")}Licensed in {C.STATES} states
      </span>
      <span class="inline-flex items-center gap-2">
        {icon("scale", 18, "shrink-0")}Independent. We work for you, not for one carrier.
      </span>
      <span class="inline-flex items-center gap-2">
        {icon("building", 18, "shrink-0")}{C.YEARS} years placing life insurance
      </span>
      <span class="inline-flex items-center gap-2">
        {icon("shield-check", 18, "shrink-0")}Your details are never sold to other agencies
      </span>
    </div>
  </div>
</section>

<!-- =====================================================================
     2. WHAT MAKES IT PERMANENT.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">What makes it permanent</h2>
        {permanence_media}
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <p class="reveal text-lead text-slate">
          Term life rents you coverage for a fixed number of years. Whole life is a contract for
          your entire life, and the carrier prices it on the assumption that it will eventually pay
          out, because it will.
        </p>
        <p class="reveal mt-5 text-slate">
          To keep the premium level across fifty years instead of twenty, the carrier charges more
          than the cost of insuring you in the early years and less than it in the later ones. The
          surplus from the early years is held inside the policy, earns interest at a rate the
          contract guarantees, and becomes the cash value. That is the whole mechanism. Everything
          else on this page is a consequence of it.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     3. THE THREE GUARANTEES.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">The three guarantees</h2>
      <p class="reveal mt-5 text-slate">
        These are contractual for as long as the premium is paid. They are the reason the product
        exists and the reason it costs what it costs.
      </p>
    </div>

    <div class="mt-10 bento" data-stagger="40">
      <div class="reveal bento-cell bento-2">
        <div class="flex items-center gap-3">
          {icon("shield-check", 26, "shrink-0 text-navy-700")}
          <h3 class="text-h4">The death benefit</h3>
        </div>
        <p class="mt-4 text-slate">
          It pays whenever you die, at 40 or at 100. There is no term to outlive and the carrier
          cannot cancel the policy because your health changed.
        </p>
      </div>
      <div class="reveal bento-cell bento-2 bento-cell-blue">
        <div class="flex items-center gap-3">
          {icon("banknote", 26, "shrink-0 text-white")}
          <h3 class="text-h4">The premium</h3>
        </div>
        <p class="mt-4 text-white/85">
          Fixed at the age you buy it and level for life. It does not rise with age, with inflation,
          or after a diagnosis.
        </p>
      </div>
      <div class="reveal bento-cell bento-2 bento-cell-tint">
        <div class="flex items-center gap-3">
          {icon("trending-up", 26, "shrink-0 text-navy-700")}
          <h3 class="text-h4">The cash value</h3>
        </div>
        <p class="mt-4 text-slate">
          A schedule of guaranteed values, printed in the contract, year by year. You can borrow
          against it or surrender the policy for it.
        </p>
      </div>
    </div>

    <p class="reveal mt-8 text-sm text-muted max-w-3xl">
      All guarantees depend on the claims paying ability of the issuing carrier. Check the
      carrier's financial strength ratings, and ask us for them if they are not in front of you.
    </p>
  </div>
</section>

<!-- =====================================================================
     4. HOW CASH VALUE BUILDS.
     ================================================================== -->
<section id="cash-value" class="section glow">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">How cash value builds</h2>
      <p class="reveal mt-5 text-slate">
        Slowly at first, and that surprises people. In the first two or three years there is
        often little or no cash value at all, because the carrier's costs of putting the policy
        on the books come out first. After that it compounds at the guaranteed rate, and the gap
        between what you have paid and what the policy is worth narrows, then reverses.
      </p>
    </div>

    <div class="mt-10 bento" data-stagger="40">
      {cash_value_chart()}

      <div class="reveal bento-cell bento-2 bento-cell-tint">
        <p class="eyebrow">Read before you buy</p>
        <div class="mt-4">{C.stat(40, "policy years on the chart", suffix=" yrs")}</div>
        <p class="mt-4 text-slate">
          A whole life contract is measured in decades. The single most important thing to
          understand before buying is the early years: a policy surrendered in year three usually
          returns less than was paid into it.
        </p>
        <p class="mt-auto pt-5 text-sm text-muted">
          Ask for a carrier illustration with the guaranteed column shown separately, then read
          only that column.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     5. DIVIDENDS.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">
      <div class="lg:col-span-6">
        <h2 class="reveal text-h2">Dividends and participating policies</h2>
        <p class="reveal mt-6 text-slate">
          A participating policy from a mutual carrier may pay an annual dividend. It is not
          investment income. It is a return of part of the premium, paid when the company's actual
          mortality, expense, and investment results come in better than the conservative
          assumptions built into the price.
        </p>
        <p class="reveal mt-4 text-slate">
          You can usually take a dividend in cash, use it to reduce the premium, leave it to
          accumulate at interest, or buy paid up additions, which is small blocks of extra
          permanent coverage that themselves build cash value.
        </p>
      </div>

      <div class="lg:col-span-5 lg:col-start-8">
        <div class="reveal card border-navy">
          <div class="flex items-start gap-3">
            {icon("circle-alert", 26, "shrink-0 text-navy mt-0.5")}
            <div>
              <h3 class="text-h4">Dividends are not guaranteed</h3>
              <p class="mt-3 text-slate">
                Not this year, not next year, not ever. Several mutual carriers have paid one every
                year for more than a century, and that record is genuinely meaningful, and it is
                still not a promise.
              </p>
              <p class="mt-4 text-slate">
                When you read an illustration, find the guaranteed column. That is what you are
                actually entitled to. Every other column is an assumption about a dividend scale
                that can change.
              </p>
              <a class="link-static mt-4 inline-block text-sm" href="/whole-life-insurance/dividends/#how-they-are-declared">How dividends are declared</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     6. COST AGAINST TERM.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">What it costs against term</h2>
      <p class="reveal mt-5 text-slate">
        This is the comparison that decides it for most people, so here it is without softening.
      </p>
    </div>

    <div class="reveal mt-8 max-w-3xl">
      {C.rates_flag("premium comparisons")}
    </div>

    <div class="reveal mt-8 table-scroll table-signature">
      <table class="compare-table" style="min-width:44rem">
        <caption class="sr-only">Whole life insurance compared with 20 year term life insurance</caption>
        <thead>
          <tr>
            <th scope="col"><span class="sr-only">Feature</span></th>
            <th scope="col">Whole life</th>
            <th scope="col">20 year term</th>
          </tr>
        </thead>
        <tbody>
          <tr><th scope="row">Monthly premium, $250,000 at age 40</th><td class="tnum">$--</td><td class="tnum">$--</td></tr>
          <tr><th scope="row">Monthly premium, $250,000 at age 50</th><td class="tnum">$--</td><td class="tnum">$--</td></tr>
          <tr><th scope="row">Coverage ends</th><td>Never</td><td>After 20 years</td></tr>
          <tr><th scope="row">Premium after year 20</th><td>Unchanged</td><td>Rises steeply each year, or coverage stops</td></tr>
          <tr><th scope="row">Cash value at year 20</th><td>Guaranteed schedule in the contract</td><td>None</td></tr>
          <tr><th scope="row">Chance it pays a death benefit</th><td>Effectively certain</td><td>Low, by design</td></tr>
        </tbody>
      </table>
    </div>

    <p class="reveal mt-4 text-micro text-muted max-w-3xl">
      <span class="pill mr-2">Rates last updated: {C.RATES_DATE}</span>
      Source: [CARRIER RATE CARD NAME AND EDITION].
    </p>

    <p class="reveal mt-8 text-slate max-w-3xl">
      A common and reasonable answer is both: a large term policy covering the years your family is
      most exposed, and a smaller whole life policy underneath it that never goes away. We will
      price that combination alongside the single product options.
      Read the longer version in our
      <a class="link" href="/compare/term-vs-whole-life-insurance/">comparison of term and whole life insurance</a>.
    </p>
  </div>
</section>

{legacy_band}

<!-- =====================================================================
     7. WHO IT SUITS AND WHO IT DOES NOT.
     Equal prominence, side by side. Spec section 03.7b: this is the
     strongest E-E-A-T signal on the page and it is not going in a footnote.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Who whole life actually suits</h2>
      <p class="reveal mt-5 text-slate">
        Both halves of this matter equally. If you are on the right hand side, we will say so on
        the phone, and we will say it even though term pays us less.
      </p>
    </div>

    <div class="mt-10 grid lg:grid-cols-2 gap-6">

      <div class="reveal card card-hover h-full">
        <div class="flex items-center gap-3 pb-4 border-b border-rule">
          {icon("circle-check", 26, "shrink-0 text-green")}
          <h3 class="text-h3 !font-display !font-semibold">It genuinely suits you if</h3>
        </div>
        <ul class="mt-6 grid gap-5">
          <li class="flex items-start gap-3">{icon("check", 20, "shrink-0 text-green mt-1")}<span>You are supporting a dependent with a disability who will need help for their whole life.</span></li>
          <li class="flex items-start gap-3">{icon("check", 20, "shrink-0 text-green mt-1")}<span>You have an estate large enough to owe tax, and heirs who would otherwise have to sell something to pay it.</span></li>
          <li class="flex items-start gap-3">{icon("check", 20, "shrink-0 text-green mt-1")}<span>You are a business owner funding a buy sell agreement or covering a key person.</span></li>
          <li class="flex items-start gap-3">{icon("check", 20, "shrink-0 text-green mt-1")}<span>You have already filled your tax advantaged retirement accounts and want a guaranteed, low volatility place for more.</span></li>
          <li class="flex items-start gap-3">{icon("check", 20, "shrink-0 text-green mt-1")}<span>You want a modest policy that certainly pays for a funeral, and you can comfortably afford the premium for life.</span></li>
        </ul>
      </div>

      <div class="reveal card card-hover h-full">
        <div class="flex items-center gap-3 pb-4 border-b border-rule">
          {icon("circle-x", 26, "shrink-0 text-navy")}
          <h3 class="text-h3 !font-display !font-semibold">It does not suit you if</h3>
        </div>
        <ul class="mt-6 grid gap-5">
          <li class="flex items-start gap-3">{icon("arrow-right", 20, "shrink-0 text-navy mt-1")}<span>Your main need is replacing income while the children are at home. Term does that for a fraction of the cost.</span></li>
          <li class="flex items-start gap-3">{icon("arrow-right", 20, "shrink-0 text-navy mt-1")}<span>The premium would be a stretch. A policy you cannot sustain and surrender in year three usually returns less than you paid in.</span></li>
          <li class="flex items-start gap-3">{icon("arrow-right", 20, "shrink-0 text-navy mt-1")}<span>You have an employer match you are not taking, or high interest debt. Both beat this comfortably.</span></li>
          <li class="flex items-start gap-3">{icon("arrow-right", 20, "shrink-0 text-navy mt-1")}<span>You were sold it as an investment or a tax free retirement plan. It is insurance with a savings component, priced as such.</span></li>
          <li class="flex items-start gap-3">{icon("arrow-right", 20, "shrink-0 text-navy mt-1")}<span>You need the largest possible death benefit on a fixed budget. Nothing beats term on that measure.</span></li>
        </ul>
        <p class="mt-6 text-sm text-slate">
          If more than one of these describes you, start with
          <a class="link" href="/term-life-insurance/">term life insurance</a> instead.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     8. UNDERWRITING AND THE GUARANTEED ACCEPTANCE ROUTE.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">
      <div class="lg:col-span-6">
        <h2 class="reveal text-h2">Underwriting</h2>
        <p class="reveal mt-6 text-slate">
          A fully underwritten whole life policy follows the same path as term: application, phone
          interview, database checks, usually a paramedical exam, then medical records and an
          underwriting decision. Three to six weeks is normal, and the waiting is mostly your
          doctor's office rather than the carrier.
        </p>
        <p class="reveal mt-4 text-slate">
          Fully underwritten is also where the best pricing is. If you are in reasonable health it
          is worth the inconvenience, and the difference compounds across a policy you will hold
          for decades.
        </p>
      </div>

      <div class="lg:col-span-5 lg:col-start-8">
        <div class="reveal card !p-0 overflow-hidden">
          {acceptance_media}
          <div class="p-6 md:p-8">
          <h3 class="text-h4">If you cannot qualify</h3>
          <p class="mt-3 text-slate">
            Guaranteed acceptance whole life asks no health questions and turns nobody down within
            the eligible ages. The coverage is small, the premium per dollar is the highest of
            anything we offer, and there is a two or three year waiting period for natural causes.
          </p>
          <p class="mt-4 text-slate">
            It is a real answer for people who have no other one. It should be the last option you
            consider rather than the first, and any agent who leads with it is not working for you.
          </p>
          <a class="btn btn-ghost mt-6" href="/whole-life-insurance/guaranteed-acceptance/#who-it-is-for">Guaranteed acceptance whole life</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

{spokes}

<!-- =====================================================================
     10. FAQ.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">
      <div class="lg:col-span-4">
        <h2 class="reveal text-h2">Whole life questions</h2>
        <p class="reveal mt-5 text-slate">
          Eight things worth knowing before you sign a contract you intend to keep for fifty years.
        </p>
      </div>
      <div class="lg:col-span-7 lg:col-start-6 reveal">
        {faq_html}
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     11. BYLINE.
     ================================================================== -->
<section class="section-tight band">
  <div class="container-ax">
    <div class="reveal">{byline}</div>
  </div>
</section>

<!-- =====================================================================
     12. FINAL SPLIT CTA, at parity again.
     ================================================================== -->
<section class="section-tight border-t border-rule glow">
  <div class="container-ax">
    <div class="grid md:grid-cols-2 gap-6" data-stagger="40">
      <div class="reveal card card-hover">
        <h2 class="text-h3 !font-display !font-semibold">Compare quotes</h2>
        <p class="mt-3 text-slate max-w-md">
          Five answers at the top of this page and a licensed agent comes back with named carriers
          and the guaranteed numbers.
        </p>
        <a class="btn btn-cta mt-6" href="#quote">Go to the quote form</a>
        <p class="mt-3 text-micro text-muted">Free &#183; No obligation &#183; Licensed agents</p>
      </div>

      <div class="reveal card card-hover">
        <h2 class="text-h3 !font-display !font-semibold">Talk it through</h2>
        <p class="mt-3 text-slate max-w-md">
          Whole life has more moving parts than term, and most of them are easier to explain out
          loud than to read.
        </p>
        {C.phone_link("wl_final_call", "btn btn-call mt-6", "Call " + C.PHONE_DISPLAY)}
        <p class="mt-3 text-micro text-muted">{C.HOURS}</p>
      </div>
    </div>
  </div>
</section>
"""
