# -*- coding: utf-8 -*-
"""TERM LIFE HUB. Spec section 02. Form weighted.

Primary CTA is the multi-step quote form, above the fold at 1024 and up.
Click-to-call is present but secondary: it lives in the sticky header.
"""
from icons import icon
import chrome as C
import forms as F
from forms import ERR

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
    return C.acc(q, a, "term-faq")


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

      <div class="reveal mt-8 grid sm:grid-cols-[7fr_4fr_4fr] gap-6 max-w-3xl">
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
      <!-- .reveal sits on the scroll container itself. A transformed wrapper
           around a scrolling table leaks the table's width into the page
           until the section reveals. -->
      <div class="reveal mt-8 table-scroll table-signature">
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

    <p class="reveal mt-4 text-micro text-muted max-w-3xl">
      <span class="pill mr-2">Rates last updated: {C.RATES_DATE}</span>
      Source: [CARRIER RATE CARD NAME AND EDITION].
      Premiums vary by carrier, state, health, build, family history, and tobacco use. A rate table
      is an illustration of shape, not an offer of coverage. Your rate class is decided by the
      carrier after underwriting.
    </p>"""


TERM_LENGTH_FIELD = '''<!-- Set by the rate table's "quote this" buttons. -->
<input type="hidden" name="term_length" value="">'''


COVERAGE_OPTIONS = [
    ("", "Choose an amount"), ("100000", "$100,000"), ("250000", "$250,000"),
    ("500000", "$500,000"), ("750000", "$750,000"), ("1000000", "$1,000,000"),
    ("2000000", "$2,000,000 or more"), ("unsure", "Not sure yet"),
]


def quote_form(form_id, form_name, id_prefix):
    """Two steps, six fields, paired. Step 1 is about the person, step 2 is the
    cover and how to reach them, with the TCPA block above the submit."""
    p = id_prefix
    about = (
        F.row(F.age_field(p + "-age", label="How old are you?",
                          hint="The biggest factor in the price."),
              F.select_field(p + "-state", "state", "Your state",
                             '<option value="">Choose your state</option>\n' + C.state_options(),
                             error="Please choose your state."))
        + F.row(F.radio_group(p + "-sex", "sex", "Sex on your birth certificate",
                              [("female", "Female"), ("male", "Male")],
                              hint="Carriers rate them differently.",
                              error="Choose one so we can price it correctly."),
                F.radio_group(p + "-tob", "tobacco", "Tobacco in the last 12 months?",
                              [("no", "No"), ("yes", "Yes")],
                              hint="Nicotine of any kind.",
                              error="Let us know either way."))
        + F.next_button())
    cover = (
        F.row(F.select_field(p + "-coverage", "coverage", "How much coverage?", COVERAGE_OPTIONS,
                             error="Choose a coverage amount, or pick the closest.",
                             hint="A rough figure is fine."),
              F.phone_field(p + "-phone", hint="One agent calls, once."))
        + F.consent_block(p, C.BRAND, 12)
        + F.submit_block("See my quotes", back=True))
    return f"""
        <form id="{form_id}" class="mt-6" data-ax-form data-steps data-silo="term-life"
              data-form-name="{form_name}" data-success-target="{p}-success" novalidate>

          {F.scaffold(TERM_LENGTH_FIELD, 10)}

          {F.progress(2)}

          {F.step(1, "About you", about, first=True)}
          {F.step(2, "Your cover", cover)}
        </form>

        <div id="{p}-success" class="success">
          <div class="flex items-start gap-3">
            {icon("circle-check", 30, "shrink-0 text-green")}
            <div>
              <h3 class="text-h3 !font-display !font-semibold">Got it</h3>
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
        <label class="choice reveal !min-w-0">
          <input type="radio" name="term-length-explainer" value="{key}"{" checked" if key == "20" else ""}>
          <span class="!min-h-[112px] !flex-col !items-start !gap-1 !p-5 !rounded-[12px]">
            <span class="stat-value" data-count="{key}">{key}</span>
            <span class="text-sm">year term</span>
          </span>
        </label>""" for key, label, _, _ in TERM_LENGTHS)

    term_panels = "".join(f"""
        <div data-panel="{key}"{"" if key == "20" else " hidden"}>
          <div class="grid lg:grid-cols-12 gap-8 lg:gap-10">
            <div class="lg:col-span-6">
              <h3 class="text-h3 !font-display !font-semibold">{label}</h3>
              <p class="mt-4 text-slate">{fits}</p>
            </div>
            <div class="lg:col-span-5 lg:col-start-8 flex flex-col">
              <p class="text-sm font-semibold text-navy">Worth knowing</p>
              <p class="mt-2 text-sm text-muted">{caveat}</p>
              <button type="button" class="btn-row mt-6 self-start" data-prefill='{{"term_length":"{key}"}}'
                      data-prefill-target="term-quote-form">Quote a {label.replace(" years", " year")} term {icon("arrow-right", 16)}</button>
            </div>
          </div>
        </div>""" for key, label, fits, caveat in TERM_LENGTHS)

    home_media = C.figure("term-home", "(min-width: 1024px) 38vw, 92vw",
                          cls="reveal", glow=True)
    underwriting_media = C.figure("term-underwriting", "(min-width: 1024px) 36vw, 92vw",
                                  cls="reveal mt-8")
    # Mid-page banner, roughly 60% scroll depth. Photographed rather than flat
    # navy so the second ask reads as a break, not as another content block.
    no_exam_band = C.banner(
        "term-band",
        "Would rather skip the exam?",
        "Several of our carriers can issue term coverage with no paramedical exam for healthy "
        "applicants, often with a decision in days rather than weeks. It usually costs a little "
        "more, and the coverage limits are lower. Sometimes that trade is worth it.",
        '<a class="btn btn-cta btn-block" href="#quote" data-cta-location="term_band">'
        'Get my term quotes</a>'
        '<a class="btn btn-ghost btn-block mt-3" href="/term-life-insurance/no-medical-exam/#who-qualifies">'
        'No medical exam term life</a>',
        eyebrow="No medical exam")
    spokes = C.spoke_module(
        "Explore term life insurance",
        "Eleven pages covering the parts of term life that need more than a paragraph.",
        SPOKES)
    faq_html = "\n        ".join(_acc(q, a) for q, a in FAQ)
    byline = C.byline()

    # One h1, one line, one button. The form it points at is the next section
    # but one, so the hero can take a photograph (MASTER.md section 8).
    hero = C.page_hero(
        [("Home", "/"), ("Term Life Insurance", None)],
        "Term life insurance, made simple.",
        "The most cover for your money, for exactly as long as your family needs it.",
        extra=C.hero_cta("#quote", "Get my term life quote"),
        banner="term-hero")
    usps = C.usp_strip([
        ("clock", "10, 15, 20 or 30 years", "Pick the term you need"),
        ("shield-check", "Premium locked", "For the whole term"),
        ("stethoscope", "Often no medical exam", "Many applicants skip it"),
        ("scale", "Independent agency", "We compare carriers for you"),
    ])

    how_to_apply = C.steps_section(
        "How to apply",
        "Three steps, and you can stop after any of them.",
        [("list-checks", "About ninety seconds", "Send the six answers",
          "The form on this page, or a phone call if you would rather talk it through. No Social "
          "Security number at this stage."),
         ("search", "Named carriers", "Review named quotes",
          "You get carrier names, premiums, term lengths, and the conversion terms, so you can "
          "compare them against anything else you have been shown."),
         ("circle-check", "We stay with it", "Apply and go through underwriting",
          "We complete the application with you and stay with it until the policy is issued or the "
          "carrier says no. Either way you hear it from us.")],
        cta=("Ready when you are.", "Free, no obligation, and you can stop after any step.",
             '<a href="#quote" class="btn btn-cta">Get my term life quote</a>'))

    return f"""
{hero}
{usps}

<!-- =====================================================================
     THE QUOTE FORM. Directly under the strip, and still #quote: the hero
     button, the banner, and the homepage triage all land here.
     ================================================================== -->
<section id="quote" class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">

      <div class="lg:col-span-5">
        <div class="sticky-col">
          <h2 class="reveal text-h2">Get your term life quotes</h2>
          <p class="reveal mt-5 text-slate">Six questions, about ninety seconds.</p>

          <div class="reveal mt-8 pt-8 border-t border-rule">
            <p class="text-sm font-semibold text-navy">What happens after you submit</p>
            <ol class="mt-3 grid gap-2 text-sm text-slate">
              <li>1. A licensed agent reads it. No automated quote engine, no lead broker.</li>
              <li>2. We run your details past our appointed carriers.</li>
              <li>3. We come back within {C.SLA} with named carriers and real premiums.</li>
              <li>4. If nothing fits, we tell you that too.</li>
            </ol>
          </div>
          <p class="reveal mt-6 inline-flex items-center gap-2 text-sm text-muted">
            {icon("shield-check", 18, "shrink-0 text-navy")}Your details are never sold to other agencies
          </p>
        </div>
      </div>

      <div class="lg:col-span-6 lg:col-start-7">
        <div class="panel reveal">
          {quote_form("term-quote-form", "term_hero_quote", "th")}
        </div>
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     2. WHAT IT COVERS, AND WHO IT DOES NOT SUIT.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-center">
      <div class="lg:col-span-7">
        <h2 class="reveal text-h2">What term life insurance covers</h2>
        <p class="reveal mt-5 text-lead text-slate">
          Term life pays a lump sum to the people you name if you die during a fixed number of
          years. It builds no cash value and it ends when the term does, which is exactly why it
          costs so much less than permanent coverage.
        </p>
        <p class="reveal mt-5 text-slate">
          For most households the fixed number of years is not arbitrary. It is the years left on
          the mortgage, or the years until the youngest child is independent, whichever runs longer.
        </p>
      </div>
      <div class="lg:col-span-5">
        {home_media}
      </div>
    </div>

    <div class="mt-14 bento" data-stagger="40">
      <div class="reveal bento-cell bento-2 bento-cell-blue">
        <p class="eyebrow">Coverage range</p>
        <div class="mt-4">{C.stat(2000000, "typical top of the range our carriers write", prefix="$")}</div>
        <p class="mt-4 text-sm text-white/85">
          From $100,000 up. The premium difference between $500,000 and $750,000 is usually smaller
          than people expect, which is why buying too little is the common mistake.
        </p>
        <p class="mt-auto pt-5 text-micro text-white/70">Ranges vary by carrier, state, age, and health. Not an offer of coverage.</p>
      </div>

      <div class="reveal bento-cell bento-2">
        <div class="flex items-center gap-3">
          {icon("circle-check", 24, "shrink-0 text-green")}
          <h3 class="text-h3 !font-display !font-semibold">Who term life fits</h3>
        </div>
        <ul class="mt-6 grid gap-4">
          <li class="flex items-start gap-3">{icon("check", 20, "shrink-0 text-green mt-1")}<span>You have a mortgage, or children who are not yet independent, or both.</span></li>
          <li class="flex items-start gap-3">{icon("check", 20, "shrink-0 text-green mt-1")}<span>Someone would struggle financially if your income stopped.</span></li>
          <li class="flex items-start gap-3">{icon("check", 20, "shrink-0 text-green mt-1")}<span>You want the largest death benefit your budget will stretch to.</span></li>
          <li class="flex items-start gap-3">{icon("check", 20, "shrink-0 text-green mt-1")}<span>The need has a foreseeable end date, even a distant one.</span></li>
        </ul>
      </div>

      <div class="reveal bento-cell bento-2">
        <div class="flex items-center gap-3">
          {icon("circle-x", 24, "shrink-0 text-navy")}
          <h3 class="text-h3 !font-display !font-semibold">When to look at something else</h3>
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
        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4" data-stagger="40">{term_cards}
        </div>
      </fieldset>

      <div class="mt-8 card">{term_panels}
      </div>
    </div>
  </div>
</section>

{C.ask_strip("Seen enough to get a quote?", "Six questions, about ninety seconds.", '<a href="#quote" class="btn btn-cta">Get my term life quote</a>')}

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

    <div>
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
      <div class="lg:col-span-5">
        <div class="sticky-col">
          <h2 class="reveal text-h2">How underwriting works</h2>
          <p class="reveal mt-5 text-slate">
            Underwriting is the carrier deciding what risk you are and pricing it. Here is the whole
            process, including the part where you wait.
          </p>
          {underwriting_media}
        </div>
      </div>

      <div class="lg:col-span-7">
        <ol class="reveal relative border-l border-rule pl-8 grid gap-8">
          <li class="relative">
            <span class="absolute -left-[41px] top-1 w-4 h-4 bg-navy-700 rounded-full ring-4 ring-surface"></span>
            <p class="text-sm font-semibold text-muted">Day 1</p>
            <h3 class="mt-1 text-h4">Application</h3>
            <p class="mt-2 text-slate">We complete it with you, by phone or electronically. Twenty to thirty minutes, including the health and lifestyle questions.</p>
          </li>
          <li class="relative">
            <span class="absolute -left-[41px] top-1 w-4 h-4 bg-navy-700 rounded-full ring-4 ring-surface"></span>
            <p class="text-sm font-semibold text-muted">Day 1 to 5</p>
            <h3 class="mt-1 text-h4">Phone interview and database checks</h3>
            <p class="mt-2 text-slate">The carrier confirms your answers and pulls your prescription history, motor vehicle record, and medical information database file.</p>
          </li>
          <li class="relative">
            <span class="absolute -left-[41px] top-1 w-4 h-4 bg-navy-700 rounded-full ring-4 ring-surface"></span>
            <p class="text-sm font-semibold text-muted">Day 3 to 10, if required</p>
            <h3 class="mt-1 text-h4">The medical exam</h3>
            <p class="mt-2 text-slate">A paramedical examiner comes to your home or office. Height, weight, blood pressure, a blood sample, and a urine sample. Around twenty minutes. It is free and you do not arrange it yourself.</p>
          </li>
          <li class="relative">
            <span class="absolute -left-[41px] top-1 w-4 h-4 bg-navy-700 rounded-full ring-4 ring-surface"></span>
            <p class="text-sm font-semibold text-muted">Week 2 to 5</p>
            <h3 class="mt-1 text-h4">Medical records and review</h3>
            <p class="mt-2 text-slate">This is the slow part, and it is your doctor's office rather than the carrier. An underwriter then assigns a rate class.</p>
          </li>
          <li class="relative">
            <span class="absolute -left-[41px] top-1 w-4 h-4 bg-navy-700 rounded-full ring-4 ring-surface"></span>
            <p class="text-sm font-semibold text-muted">Week 3 to 6</p>
            <h3 class="mt-1 text-h4">Offer, and your decision</h3>
            <p class="mt-2 text-slate">If the rate class is worse than we quoted, we say so and tell you what it means in money. You can accept, ask us to shop it elsewhere, or walk away.</p>
          </li>
        </ol>

        <p class="reveal mt-8 pt-6 border-t border-rule text-sm text-muted">
          Nothing is owed and no coverage is in force until the policy is issued, delivered, and the
          first premium is paid.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     6. NO EXAM TEASER.
     ================================================================== -->
{no_exam_band}

<!-- 8. HOW TO APPLY. The same connected stepper as the homepage. -->
{how_to_apply}

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
          If yours is not here, put it in the form and we will answer it in the reply. Or ask
          a licensed agent now.
        </p>
        <div class="reveal mt-4">{C.phone_link("term_faq", "btn btn-ghost", "Call " + C.PHONE_DISPLAY)}</div>
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
     12. FINAL FORM CTA.
     ================================================================== -->
<section class="section glow">
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
          <h3 class="text-h3 !font-display !font-semibold">Start your quote</h3>
          {quote_form("term-quote-form-footer", "term_footer_quote", "tf")}
        </div>
      </div>
    </div>
  </div>
</section>
"""
