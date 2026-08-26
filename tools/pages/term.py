# -*- coding: utf-8 -*-
"""TERM LIFE HUB. Spec section 02. Form weighted.

Primary CTA is the multi-step quote form, above the fold at 1024 and up.
Click-to-call is present but secondary: it lives in the sticky header.
"""
from icons import icon
import chrome as C

PATH = "/term-life-insurance/"
OUT = "term-life-insurance/index.html"
ACTIVE = PATH
SILO = "term-life"
TITLE = "Term Life Insurance Quotes from Multiple Carriers | Apex"
OG_TITLE = "Compare term life insurance from multiple carriers"
DESC = ("Compare 10, 15, 20, and 30 year term life insurance from multiple appointed carriers. "
        "Free quotes from a licensed independent agency. No obligation.")

FAQ = [
    ("How much term life insurance do I need?",
     "Start with what would still have to be paid if your income stopped: the mortgage balance, "
     "other debt, the cost of raising any children to adulthood, and a cushion for the surviving "
     "partner. Ten to twelve times your annual income is a reasonable starting point, then adjust "
     "for savings and any employer coverage you already have. Buying too little is the more common "
     "mistake, because the premium difference between $500,000 and $750,000 is usually smaller "
     "than people expect."),
    ("What term length should I choose?",
     "Match the term to the obligation, not to a round number. If the mortgage has 22 years left, "
     "a 25 or 30 year term covers it; a 20 year term leaves two years exposed. If the goal is "
     "getting the youngest child to graduation, count the years to that date. A term that ends "
     "before the need does is the most expensive kind of mistake, because replacing it later "
     "means buying at an older age and in whatever health you are in by then."),
    ("What happens when the term ends?",
     "Coverage stops. Most policies allow you to keep it going year by year at an annually "
     "increasing rate, which becomes very expensive very quickly and is meant as a short bridge "
     "rather than a plan. The better option, if it is available on your policy, is conversion: "
     "converting some or all of the term into a permanent policy with no new medical exam."),
    ("Can I convert a term policy to permanent coverage later?",
     "Most term policies from the carriers we work with include a conversion privilege, usually "
     "until a set age or a set number of years into the term. It lets you convert without proving "
     "you are still insurable, which is valuable if your health changes. Conversion rules differ a "
     "lot between carriers, and we will tell you what a policy's conversion terms are before you "
     "apply, not after."),
    ("Do I need a medical exam for term life insurance?",
     "Increasingly, no. Many carriers now use accelerated underwriting for healthy applicants "
     "under a certain age and coverage amount, drawing on prescription history, motor vehicle "
     "records, and medical databases instead of a paramedical exam. If you are in good health and "
     "you are willing to take the exam, fully underwritten policies still tend to offer the lowest "
     "premium."),
    ("Does tobacco use really change the price that much?",
     "Yes. Tobacco rate classes are commonly two to three times the non tobacco premium for the "
     "same coverage. Carriers define tobacco use differently, and a few treat occasional cigar use "
     "or nicotine replacement therapy more favourably than others, so it is worth telling us "
     "exactly what you use rather than answering a plain yes."),
    ("What if I have a health condition?",
     "Apply anyway, and apply through an agency rather than to one carrier. Carriers underwrite the "
     "same condition very differently. A well managed condition that one carrier rates up two "
     "classes may be issued at standard by another. Where a fully underwritten policy is not "
     "realistic, simplified issue and no medical exam options exist at a higher premium."),
    ("How long does it take to get covered?",
     "Accelerated underwriting can produce a decision in a few days, sometimes within 24 hours. "
     "Fully underwritten policies with a paramedical exam usually take three to six weeks, most of "
     "which is waiting for medical records to arrive from your doctor. Nothing is owed and no "
     "coverage is in force until the policy is issued, delivered, and the first premium is paid."),
    ("Is term life insurance worth it if I never claim?",
     "That is what buying insurance means, and it is the outcome you should want. You are not "
     "buying an investment. You are transferring a specific financial risk for a specific period "
     "at a known price, so that if the improbable thing happens, the people who depend on you are "
     "not also dealing with money. If you also want a policy that builds value, that is "
     "<a class=\"link\" href=\"/whole-life-insurance/\">whole life insurance</a>, and it costs "
     "considerably more."),
]

SPOKES = [
    ("/term-life-insurance/quotes/", "Term life insurance quotes", "What we need from you and how quickly a quote comes back."),
    ("/term-life-insurance/rates/", "Term life insurance rates", "Full rate tables by age, term length, and coverage."),
    ("/term-life-insurance/calculator/", "Coverage calculator", "Work out how much cover your household actually needs."),
    ("/term-life-insurance/what-is-term-life-insurance/", "What term life insurance is", "The plain definition, with the fine print left in."),
    ("/term-life-insurance/for-seniors/", "Term life for seniors", "What is still available after 60, and what it costs."),
    ("/term-life-insurance/level-term/", "Level term life insurance", "Why a level premium matters and when it stops being level."),
    ("/term-life-insurance/10-year-term/", "10 year term life insurance", "Short obligations, and the trap of the renewal rate."),
    ("/term-life-insurance/20-year-term/", "20 year term life insurance", "The most common choice, and who it actually fits."),
    ("/term-life-insurance/30-year-term/", "30 year term life insurance", "Long mortgages and young children."),
    ("/term-life-insurance/no-medical-exam/", "No medical exam term life", "Accelerated and simplified issue, and what they cost."),
    ("/term-life-insurance/return-of-premium/", "Return of premium term life", "How it works, and why we rarely recommend it."),
]

AGE_BANDS = [("30 to 34", "32"), ("35 to 39", "37"), ("40 to 44", "42"), ("45 to 49", "47"),
             ("50 to 54", "52"), ("55 to 59", "57"), ("60 to 65", "62")]
COVERAGE_COLS = [("$250,000", "250000"), ("$500,000", "500000"), ("$1,000,000", "1000000")]

TERM_LENGTHS = [
    ("10", "10 years", "A short, specific obligation: the last stretch of a mortgage, a business loan, or the years until a pension starts.",
     "Cheapest per year of cover, and the renewal rate at the end is brutal. Only choose this if the need genuinely ends."),
    ("15", "15 years", "A mid length gap. Common for people who started a family later or refinanced part way through a mortgage.",
     "Often only slightly more than a 10 year term, and it buys five more years of certainty."),
    ("20", "20 years", "The most common choice. It covers a child from primary school to leaving home, or most of a standard mortgage.",
     "The default for a reason, but check it against your actual dates rather than choosing it because it is the default."),
    ("30", "30 years", "A new 30 year mortgage, or very young children, or a much younger partner who would rely on the income.",
     "Costs meaningfully more than 20 years, and for a 30 year old it is often still less than people assume."),
]


def schema():
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("Term Life Insurance", None)]),
            C.faq_schema([(q, a.replace('<a class="link" href="/whole-life-insurance/">', '')
                                 .replace('</a>', '')) for q, a in FAQ]),
            C.person_schema(PATH)]


def _acc(q, a):
    return ('<details class="acc" name="term-faq">'
            '<summary>%s<span class="acc-icon">%s</span></summary>'
            '<div class="acc-body"><p class="text-slate">%s</p></div>'
            '</details>') % (q, icon("plus", 22), a)


def rate_table():
    heads = "".join('<th scope="col" class="tnum">%s</th>' % label for label, _ in COVERAGE_COLS)
    rows = []
    for band, mid_age in AGE_BANDS:
        cells = "".join('<td class="tnum">$--</td>' for _ in COVERAGE_COLS)
        prefill = '{"age":"%s","coverage":"500000"}' % mid_age
        btn = ('<button type="button" class="btn-row" data-prefill=\'%s\' '
               'data-prefill-target="term-quote-form">Quote this %s</button>'
               % (prefill, icon("arrow-right", 16)))
        rows.append('<tr><th scope="row">%s</th>%s<td>%s</td></tr>' % (band, cells, btn))
    body = "\n            ".join(rows)

    def toggle(legend, name, options, prefill_name):
        opts = "".join(
            '<label class="choice"><input type="radio" name="%s" value="%s"%s '
            'data-prefill-name="%s"><span>%s</span></label>'
            % (name, value, " checked" if i == 0 else "", prefill_name, label)
            for i, (value, label) in enumerate(options))
        return ('<fieldset><legend class="field-label">%s</legend>'
                '<div class="choice-row">%s</div></fieldset>' % (legend, opts))

    return f"""
    <div data-panels="term-rates">

      <div class="mt-8 grid sm:grid-cols-3 gap-6 max-w-3xl">
        {toggle("Term length", "term-rate-length", [("20", "20 years"), ("10", "10 years"), ("30", "30 years")], "term_length")}
        {toggle("Sex", "term-rate-sex", [("female", "Female"), ("male", "Male")], "sex")}
        {toggle("Tobacco", "term-rate-tobacco", [("no", "No"), ("yes", "Yes")], "tobacco")}
      </div>

      <!-- INTEGRATION POINT: every cell below is a structural placeholder.
           When the carrier rate cards arrive, populate the cells from the
           dataset keyed by (term length, sex, tobacco, age band, coverage)
           and have the toggles above rewrite them. Until then the toggles
           update the caption only, and nothing on this page can be mistaken
           for a real quoted premium. -->
      <div class="mt-8 table-scroll">
        <table class="rate-table" style="min-width:48rem">
          <caption>
            Monthly premium by age band and coverage amount.
            <span data-panel-caption></span>
          </caption>
          <thead>
            <tr>
              <th scope="col">Age at application</th>
              {heads}
              <th scope="col"><span class="sr-only">Get a quote for this row</span></th>
            </tr>
          </thead>
          <tbody>
            {body}
          </tbody>
        </table>
      </div>
    </div>

    <p class="mt-4 text-micro text-muted max-w-3xl">
      Rates last updated: {C.RATES_DATE}. Source: [CARRIER RATE CARD NAME AND EDITION].
      Premiums vary by carrier, state, health, build, family history, and tobacco use. A rate table
      is an illustration of shape, not an offer of coverage. Your rate class is decided by the
      carrier after underwriting.
    </p>"""


def quote_form(form_id, form_name, id_prefix):
    """Three steps, six fields, progress indicator, TCPA on the final step."""
    return f"""
        <form id="{form_id}" class="mt-6" data-ax-form data-steps data-silo="term-life"
              data-form-name="{form_name}" data-success-target="{id_prefix}-success" novalidate>

          <input type="hidden" name="source_url" value="">
          <input type="hidden" name="silo" value="">
          <input type="hidden" name="form_name" value="">
          <!-- Set by the rate table's "quote this" buttons. -->
          <input type="hidden" name="term_length" value="">
          <div aria-hidden="true" style="position:absolute;left:-9999px">
            <label>Company website<input type="text" name="company_website" tabindex="-1" autocomplete="off"></label>
          </div>

          <div class="progress-track" aria-hidden="true">
            <span class="progress-seg is-done" data-progress-seg></span>
            <span class="progress-seg" data-progress-seg></span>
            <span class="progress-seg" data-progress-seg></span>
          </div>
          <p class="text-micro font-semibold text-muted" data-progress-label aria-live="polite">Step 1 of 3</p>

          <!-- STEP 1 -->
          <fieldset class="step is-active mt-5" data-step="1">
            <legend class="sr-only">Step 1 of 3: your age</legend>
            <div class="field">
              <label class="field-label" for="{id_prefix}-age">How old are you?
                <span class="field-hint block font-normal">Age is the single biggest factor in the price.</span>
              </label>
              <input class="input" id="{id_prefix}-age" name="age" type="text" inputmode="numeric"
                     autocomplete="off" required data-validate="age"
                     data-error="Enter an age between 18 and 85.">
              <p class="field-error"><svg class="shrink-0 mt-px" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 8v4"/><path d="M12 16h.01"/></svg><span></span></p>
            </div>
            <button type="button" class="btn btn-cta btn-block" data-step-next>Continue</button>
          </fieldset>

          <!-- STEP 2 -->
          <fieldset class="step mt-5" data-step="2">
            <legend class="sr-only">Step 2 of 3: sex and state</legend>
            <div class="field" data-error="Choose one so we can price it correctly.">
              <span class="field-label" id="{id_prefix}-sex-label">Sex as shown on your birth certificate
                <span class="field-hint block font-normal">Carriers rate male and female applicants differently.</span>
              </span>
              <div class="choice-row" role="group" aria-labelledby="{id_prefix}-sex-label">
                <label class="choice"><input type="radio" name="sex" value="female" required><span>Female</span></label>
                <label class="choice"><input type="radio" name="sex" value="male" required><span>Male</span></label>
              </div>
              <p class="field-error"><svg class="shrink-0 mt-px" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 8v4"/><path d="M12 16h.01"/></svg><span></span></p>
            </div>
            <div class="field">
              <label class="field-label" for="{id_prefix}-state">What state do you live in?</label>
              <select class="select" id="{id_prefix}-state" name="state" required
                      data-error="Please choose your state.">
                <option value="">Choose your state</option>
                {C.state_options()}
              </select>
              <p class="field-error"><svg class="shrink-0 mt-px" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 8v4"/><path d="M12 16h.01"/></svg><span></span></p>
            </div>
            <div class="flex gap-3">
              <button type="button" class="btn btn-ghost" data-step-back>Back</button>
              <button type="button" class="btn btn-cta grow" data-step-next>Continue</button>
            </div>
          </fieldset>

          <!-- STEP 3 -->
          <fieldset class="step mt-5" data-step="3">
            <legend class="sr-only">Step 3 of 3: coverage, tobacco, and how to reach you</legend>
            <div class="field">
              <label class="field-label" for="{id_prefix}-coverage">How much coverage?</label>
              <select class="select" id="{id_prefix}-coverage" name="coverage" required
                      data-error="Choose a coverage amount, or pick the closest.">
                <option value="">Choose an amount</option>
                <option value="100000">$100,000</option>
                <option value="250000">$250,000</option>
                <option value="500000">$500,000</option>
                <option value="750000">$750,000</option>
                <option value="1000000">$1,000,000</option>
                <option value="2000000">$2,000,000 or more</option>
                <option value="unsure">Not sure yet</option>
              </select>
              <p class="field-error"><svg class="shrink-0 mt-px" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 8v4"/><path d="M12 16h.01"/></svg><span></span></p>
            </div>
            <div class="field" data-error="Let us know either way.">
              <span class="field-label" id="{id_prefix}-tob-label">Have you used tobacco or nicotine in the last 12 months?</span>
              <div class="choice-row" role="group" aria-labelledby="{id_prefix}-tob-label">
                <label class="choice"><input type="radio" name="tobacco" value="no" required><span>No</span></label>
                <label class="choice"><input type="radio" name="tobacco" value="yes" required><span>Yes</span></label>
              </div>
              <p class="field-error"><svg class="shrink-0 mt-px" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 8v4"/><path d="M12 16h.01"/></svg><span></span></p>
            </div>
            <div class="field">
              <label class="field-label" for="{id_prefix}-phone">Best number to reach you</label>
              <input class="input" id="{id_prefix}-phone" name="phone" type="tel" autocomplete="tel"
                     required data-validate="phone" data-error="Enter a 10 digit phone number.">
              <p class="field-error"><svg class="shrink-0 mt-px" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 8v4"/><path d="M12 16h.01"/></svg><span></span></p>
            </div>

            <!-- TCPA consent. Separate, unchecked, immediately above submit.
                 [PENDING LEGAL REVIEW] Wording must be approved by counsel and
                 matched to current TCPA one-to-one consent rules before launch. -->
            <div class="consent">
              <input type="checkbox" id="{id_prefix}-consent" name="tcpa_consent" value="yes" data-consent>
              <label class="consent-text" for="{id_prefix}-consent">
                I agree that {C.BRAND} may call and text me at the number above about life
                insurance, including with an automatic telephone dialing system or a prerecorded
                voice. I understand this consent is not a condition of purchase and that message
                and data rates may apply.
              </label>
              <p class="field-error"><svg class="shrink-0 mt-px" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 8v4"/><path d="M12 16h.01"/></svg><span></span></p>
            </div>

            <div class="flex gap-3">
              <button type="button" class="btn btn-ghost" data-step-back>Back</button>
              <button type="submit" class="btn btn-cta grow">See my quotes</button>
            </div>
            <p class="field-error" data-form-error><svg class="shrink-0 mt-px" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 8v4"/><path d="M12 16h.01"/></svg><span></span></p>
          </fieldset>

          <p class="mt-4 text-micro text-muted">
            Free &#183; No obligation &#183; Licensed agents &#183; We never sell your details on
          </p>
        </form>

        <div id="{id_prefix}-success" class="success">
          <div class="flex items-start gap-3">
            {icon("circle-check", 30, "shrink-0 text-green")}
            <div>
              <h3 class="text-h3 !font-display !font-bold">Got it</h3>
              <p class="mt-3 text-slate">
                A licensed agent is comparing our appointed carriers for your age, state, and
                coverage amount now. You will hear from us within {C.SLA}, and the quote comes with
                the carrier names on it, not just a number.
              </p>
              <div class="mt-5">
                {C.phone_link("term_success", "btn btn-call", "Or call " + C.PHONE_DISPLAY)}
              </div>
            </div>
          </div>
        </div>"""


def body():
    term_cards = "".join(f"""
        <label class="choice reveal !flex-none">
          <input type="radio" name="term-length-explainer" value="{key}"{" checked" if key == "20" else ""}>
          <span class="!min-h-[64px] !text-h4 !font-semibold">{label}</span>
        </label>""" for key, label, _, _ in TERM_LENGTHS)

    term_panels = "".join(f"""
        <div data-panel="{key}"{"" if key == "20" else " hidden"}>
          <h3 class="text-h3 !font-display !font-bold">{label}</h3>
          <p class="mt-4 text-slate">{fits}</p>
          <p class="mt-4 text-sm text-muted">{caveat}</p>
          <button type="button" class="btn-row mt-6" data-prefill='{{"term_length":"{key}"}}'
                  data-prefill-target="term-quote-form">Quote a {label.replace(" years", " year")} term {icon("arrow-right", 16)}</button>
        </div>""" for key, label, fits, caveat in TERM_LENGTHS)

    band_media = C.picture("term-band", "100vw",
                           cls="media media-band media-wipe media-parallax !rounded-none",
                           img_cls="media-img")
    underwriting_media = C.figure("term-underwriting", "(min-width: 1024px) 30vw, 92vw",
                                  cls="reveal mt-8", parallax=True)
    spokes = C.spoke_module(
        "Explore term life insurance",
        "Eleven pages covering the parts of term life that need more than a paragraph.",
        SPOKES)
    faq_html = "\n        ".join(_acc(q, a) for q, a in FAQ)
    byline = C.byline()

    return f"""
<!-- =====================================================================
     HERO. Form weighted per spec section 09. The quote form is the hero's
     right column and is above the fold from 1024 up.
     ================================================================== -->
<section class="pt-6 pb-14 md:pb-16">
  <div class="container-ax">
    {C.crumbs([("Home", "/"), ("Term Life Insurance", None)])}

    <div class="mt-8 grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">

      <div class="lg:col-span-6">
        <h1 class="reveal text-h1">Term Life Insurance</h1>
        <p class="reveal mt-5 text-lead text-slate max-w-xl">
          The most coverage per dollar, for exactly as long as your family needs it. We compare our
          appointed carriers and show you the real numbers, including the carrier names.
        </p>

        <ul class="reveal mt-8 grid sm:grid-cols-2 gap-x-8 gap-y-3">
          <li class="flex items-start gap-2.5">{icon("circle-check", 20, "shrink-0 text-green mt-1")}<span class="text-sm">10, 15, 20, and 30 year terms</span></li>
          <li class="flex items-start gap-2.5">{icon("circle-check", 20, "shrink-0 text-green mt-1")}<span class="text-sm">Many applicants skip the medical exam</span></li>
          <li class="flex items-start gap-2.5">{icon("circle-check", 20, "shrink-0 text-green mt-1")}<span class="text-sm">Premium locked for the whole term</span></li>
          <li class="flex items-start gap-2.5">{icon("circle-check", 20, "shrink-0 text-green mt-1")}<span class="text-sm">Independent. We compare, we do not push one carrier</span></li>
        </ul>

        <div class="reveal mt-8 pt-8 border-t border-rule">
          <p class="text-sm font-semibold text-navy">What happens after you submit</p>
          <ol class="mt-3 grid gap-2 text-sm text-slate">
            <li>1. A licensed agent reads it. No automated quote engine, no lead broker.</li>
            <li>2. We run your details past our appointed carriers.</li>
            <li>3. We come back within {C.SLA} with named carriers and real premiums.</li>
            <li>4. If nothing fits, we tell you that too.</li>
          </ol>
        </div>
      </div>

      <div class="lg:col-span-5 lg:col-start-8" id="quote">
        <div class="panel reveal">
          <h2 class="text-h3 !font-display !font-bold">Get your term life quotes</h2>
          <p class="mt-2 text-sm text-muted">Six questions, about ninety seconds.</p>
          {quote_form("term-quote-form", "term_hero_quote", "th")}
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Trust strip, within one viewport of the form CTA. -->
<section class="border-y border-rule bg-surface">
  <div class="container-ax py-6">
    <div class="flex flex-wrap items-center gap-x-8 gap-y-3 trust-strip">
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

<!-- Editorial band. Purely atmospheric, so the alt text is empty and the
     image is hidden from assistive tech rather than narrated. -->
<section aria-hidden="true">
  {band_media}
</section>

<!-- =====================================================================
     2. WHAT IT COVERS, AND WHO IT DOES NOT SUIT.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">What term life insurance covers</h2>
      <p class="reveal mt-5 text-lead text-slate">
        Term life pays a lump sum to the people you name if you die during a fixed number of years.
        It builds no cash value and it ends when the term does, which is exactly why it costs so
        much less than permanent coverage.
      </p>
    </div>

    <div class="mt-12 grid lg:grid-cols-2 gap-8">
      <div class="reveal card">
        <div class="flex items-center gap-3">
          {icon("circle-check", 24, "shrink-0 text-green")}
          <h3 class="text-h3 !font-display !font-bold">Who term life fits</h3>
        </div>
        <ul class="mt-6 grid gap-4">
          <li class="flex items-start gap-3">{icon("check", 20, "shrink-0 text-green mt-1")}<span>You have a mortgage, or children who are not yet independent, or both.</span></li>
          <li class="flex items-start gap-3">{icon("check", 20, "shrink-0 text-green mt-1")}<span>Someone would struggle financially if your income stopped.</span></li>
          <li class="flex items-start gap-3">{icon("check", 20, "shrink-0 text-green mt-1")}<span>You want the largest death benefit your budget will stretch to.</span></li>
          <li class="flex items-start gap-3">{icon("check", 20, "shrink-0 text-green mt-1")}<span>The need has a foreseeable end date, even a distant one.</span></li>
        </ul>
      </div>

      <div class="reveal card">
        <div class="flex items-center gap-3">
          {icon("circle-x", 24, "shrink-0 text-navy")}
          <h3 class="text-h3 !font-display !font-bold">When to look at something else</h3>
        </div>
        <ul class="mt-6 grid gap-4">
          <li class="flex items-start gap-3">{icon("arrow-right", 20, "shrink-0 text-navy mt-1")}<span>You want coverage that cannot expire, for estate or legacy reasons.</span></li>
          <li class="flex items-start gap-3">{icon("arrow-right", 20, "shrink-0 text-navy mt-1")}<span>You are supporting a dependent who will need help for their whole life.</span></li>
          <li class="flex items-start gap-3">{icon("arrow-right", 20, "shrink-0 text-navy mt-1")}<span>You want a guaranteed cash value you can borrow against.</span></li>
          <li class="flex items-start gap-3">{icon("arrow-right", 20, "shrink-0 text-navy mt-1")}<span>You are over 65 and mainly want to cover a funeral.</span></li>
        </ul>
        <p class="mt-6 text-sm text-slate">
          The first three point toward
          <a class="link" href="/compare/term-vs-whole-life-insurance/">a comparison of term and whole life</a>.
          The last one points toward
          <a class="link" href="/final-expense-insurance/">final expense insurance</a>.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     3. TERM LENGTHS. Interactive selector.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">How long should the term be?</h2>
      <p class="reveal mt-5 text-slate">
        Match the term to the obligation. Pick a length to see who it suits and where it goes wrong.
      </p>
    </div>

    <div class="mt-10" data-panels="term-lengths">
      <fieldset>
        <legend class="sr-only">Choose a term length</legend>
        <div class="choice-row max-w-2xl">{term_cards}
        </div>
      </fieldset>

      <div class="mt-8 card max-w-3xl">{term_panels}
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     4. WHAT IT COSTS.
     ================================================================== -->
<section id="rates" class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">What term life insurance costs</h2>
      <p class="reveal mt-5 text-slate">
        Age, sex, tobacco use, term length, and coverage amount set the shape of the price. Your
        health and build set the rest, and only the carrier can decide that.
      </p>
    </div>

    <div class="reveal mt-8 max-w-3xl">
      {C.rates_flag("premiums")}
    </div>

    <div class="reveal">
      {rate_table()}
    </div>
  </div>
</section>

<!-- =====================================================================
     5. UNDERWRITING TIMELINE.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">
      <div class="lg:col-span-4">
        <div class="sticky-col">
          <h2 class="reveal text-h2">How underwriting works</h2>
          <p class="reveal mt-5 text-slate">
            Underwriting is the carrier deciding what risk you are and pricing it. Here is the whole
            process, including the part where you wait.
          </p>
          {underwriting_media}
          <p class="reveal mt-5 text-sm text-muted">
            Nothing is owed and no coverage is in force until the policy is issued, delivered, and
            the first premium is paid.
          </p>
        </div>
      </div>

      <div class="lg:col-span-7 lg:col-start-6">
        <ol class="reveal relative border-l border-rule pl-8 grid gap-8">
          <li class="relative">
            <span class="absolute -left-[41px] top-1 w-4 h-4 bg-navy rounded-full ring-4 ring-navy-050"></span>
            <p class="text-sm font-semibold text-muted">Day 1</p>
            <h3 class="mt-1 text-h4">Application</h3>
            <p class="mt-2 text-slate">We complete it with you, by phone or electronically. Twenty to thirty minutes, including the health and lifestyle questions.</p>
          </li>
          <li class="relative">
            <span class="absolute -left-[41px] top-1 w-4 h-4 bg-navy rounded-full ring-4 ring-navy-050"></span>
            <p class="text-sm font-semibold text-muted">Day 1 to 5</p>
            <h3 class="mt-1 text-h4">Phone interview and database checks</h3>
            <p class="mt-2 text-slate">The carrier confirms your answers and pulls your prescription history, motor vehicle record, and medical information database file.</p>
          </li>
          <li class="relative">
            <span class="absolute -left-[41px] top-1 w-4 h-4 bg-navy rounded-full ring-4 ring-navy-050"></span>
            <p class="text-sm font-semibold text-muted">Day 3 to 10, if required</p>
            <h3 class="mt-1 text-h4">The medical exam</h3>
            <p class="mt-2 text-slate">A paramedical examiner comes to your home or office. Height, weight, blood pressure, a blood sample, and a urine sample. Around twenty minutes. It is free and you do not arrange it yourself.</p>
          </li>
          <li class="relative">
            <span class="absolute -left-[41px] top-1 w-4 h-4 bg-navy rounded-full ring-4 ring-navy-050"></span>
            <p class="text-sm font-semibold text-muted">Week 2 to 5</p>
            <h3 class="mt-1 text-h4">Medical records and review</h3>
            <p class="mt-2 text-slate">This is the slow part, and it is your doctor's office rather than the carrier. An underwriter then assigns a rate class.</p>
          </li>
          <li class="relative">
            <span class="absolute -left-[41px] top-1 w-4 h-4 bg-navy rounded-full ring-4 ring-navy-050"></span>
            <p class="text-sm font-semibold text-muted">Week 3 to 6</p>
            <h3 class="mt-1 text-h4">Offer, and your decision</h3>
            <p class="mt-2 text-slate">If the rate class is worse than we quoted, we say so and tell you what it means in money. You can accept, ask us to shop it elsewhere, or walk away.</p>
          </li>
        </ol>
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     6. NO EXAM TEASER.
     ================================================================== -->
<section class="section-tight">
  <div class="container-ax">
    <div class="reveal card max-w-4xl flex flex-col md:flex-row md:items-center gap-6 md:gap-10">
      <div class="grow">
        <h2 class="text-h3 !font-display !font-bold">Would rather skip the exam?</h2>
        <p class="mt-3 text-slate">
          Several of our carriers can issue term coverage with no paramedical exam for healthy
          applicants, often with a decision in days rather than weeks. It usually costs a little
          more, and the coverage limits are lower. Sometimes that trade is worth it.
        </p>
      </div>
      <a class="btn btn-ghost shrink-0" href="/term-life-insurance/no-medical-exam/#who-qualifies">No medical exam term life</a>
    </div>
  </div>
</section>

<!-- =====================================================================
     7. CARRIERS.
     ================================================================== -->
<section class="section-tight band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-8 items-center">
      <div class="lg:col-span-4">
        <h2 class="reveal text-h3 !font-display !font-bold">Carriers we are appointed with</h2>
        <p class="reveal mt-3 text-slate">
          We hold appointments with multiple carriers, so a decline from one is the start of the
          conversation rather than the end of it.
        </p>
      </div>
      <div class="lg:col-span-7 lg:col-start-6">
        <!-- [PLACEHOLDER - REPLACE WITH APPOINTED CARRIER LOGOS. Do not display
             a carrier mark until the appointment is active and the carrier's
             brand guidelines have been checked.] -->
        <div class="reveal grid grid-cols-2 sm:grid-cols-3 gap-3">
          <div class="logo-slot">Carrier logo 1</div>
          <div class="logo-slot">Carrier logo 2</div>
          <div class="logo-slot">Carrier logo 3</div>
          <div class="logo-slot">Carrier logo 4</div>
          <div class="logo-slot">Carrier logo 5</div>
          <div class="logo-slot">Carrier logo 6</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     8. HOW TO APPLY.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">How to apply</h2>
      <p class="reveal mt-5 text-slate">Three steps, and you can stop after any of them.</p>
    </div>
    <div class="mt-12 grid md:grid-cols-3 gap-10 md:gap-8" data-stagger>
      <div class="reveal">
        <div class="flex items-baseline gap-3 pb-4 border-b border-navy">
          <span class="text-h3 !font-display !font-bold text-navy tnum">1</span>
          <h3 class="text-h4">Send the six answers</h3>
        </div>
        <p class="mt-5 text-slate">The form at the top of this page, or a phone call if you would rather talk it through. No Social Security number at this stage.</p>
      </div>
      <div class="reveal">
        <div class="flex items-baseline gap-3 pb-4 border-b border-navy">
          <span class="text-h3 !font-display !font-bold text-navy tnum">2</span>
          <h3 class="text-h4">Review named quotes</h3>
        </div>
        <p class="mt-5 text-slate">You get carrier names, premiums, term lengths, and the conversion terms, so you can compare them against anything else you have been shown.</p>
      </div>
      <div class="reveal">
        <div class="flex items-baseline gap-3 pb-4 border-b border-navy">
          <span class="text-h3 !font-display !font-bold text-navy tnum">3</span>
          <h3 class="text-h4">Apply and go through underwriting</h3>
        </div>
        <p class="mt-5 text-slate">We complete the application with you and stay with it until the policy is issued or the carrier says no. Either way you hear it from us.</p>
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
        <h2 class="reveal text-h2">Term life questions</h2>
        <p class="reveal mt-5 text-slate">Nine things people ask before they apply.</p>
        <p class="reveal mt-6 text-sm text-muted">
          If yours is not here, put it in the form and we will answer it in the reply.
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
    <div class="reveal max-w-3xl">{byline}</div>
  </div>
</section>

<!-- =====================================================================
     12. FINAL FORM CTA.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5 reveal">
        <h2 class="text-h2">Get your quotes</h2>
        <p class="mt-5 text-slate">
          Six answers, about ninety seconds, and a licensed agent comes back with named carriers
          and real premiums. Nothing is sold on and nobody else calls you.
        </p>
        <p class="mt-6 text-sm text-muted">
          Would rather talk it through first? The number is in the header of every page, and you
          will reach a licensed agent rather than a queue.
        </p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7 reveal">
        <div class="panel">
          <h3 class="text-h3 !font-display !font-bold">Start your quote</h3>
          {quote_form("term-quote-form-footer", "term_footer_quote", "tf")}
        </div>
      </div>
    </div>
  </div>
</section>
"""
