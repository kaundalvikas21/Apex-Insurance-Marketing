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
     "before the need does is the most expensive kind of mistake. Replacing it later means "
     "buying at an older age, in whatever health you are in by then."),
    ("What happens when the term ends?",
     "Coverage stops. Most policies allow you to keep it going year by year at an annually "
     "increasing rate. That becomes very expensive very quickly, and it is meant as a short "
     "bridge. The better option, if it is available on your policy, is conversion: "
     "converting some or all of the term into a permanent policy with no new medical exam."),
    ("Can I convert a term policy to permanent coverage later?",
     "Most term policies from the carriers we work with include a conversion privilege, usually "
     "until a set age or a set number of years into the term. It lets you convert without proving "
     "you are still insurable, which is valuable if your health changes. Conversion rules differ a "
     "lot between carriers, and we will tell you what a policy's conversion terms are before you "
     "apply."),
    ("Do I need a medical exam for term life insurance?",
     "Increasingly, no. Many carriers now use accelerated underwriting for healthy applicants "
     "under a certain age and coverage amount. It draws on prescription history, motor vehicle "
     "records, and medical databases instead of a paramedical exam. If you are in good health and "
     "you are willing to take the exam, fully underwritten policies still tend to offer the lowest "
     "premium."),
    ("Does tobacco use really change the price that much?",
     "Yes. Tobacco rate classes are commonly two to three times the non tobacco premium for the "
     "same coverage. Carriers define tobacco use differently, and a few treat occasional cigar use "
     "or nicotine replacement therapy more favorably than others. Tell us exactly what you use "
     "rather than answering a plain yes."),
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
     "at a known price. If the improbable thing happens, the people who depend on you are "
     "not also dealing with money. If you also want a policy that builds value, that is "
     "whole life insurance, and it costs "
     "considerably more."),
]

SPOKES = [
    ("/term-life-insurance/quotes/", "Term life insurance quotes", "What we need from you and how quickly a quote comes back."),
    ("/term-life-insurance/rates/", "Term life insurance rates", "Full rate tables by age, term length, and coverage."),
    ("/term-life-insurance/calculator/", "Coverage calculator", "Work out how much coverage your household needs."),
    ("/term-life-insurance/what-is-term-life-insurance/", "What term life insurance is", "The plain definition, with the fine print left in."),
    ("/term-life-insurance/for-seniors/", "Term life for seniors", "What is still available after 60, and what it costs."),
    ("/term-life-insurance/level-term/", "Level term life insurance", "Why a level premium matters and when it stops being level."),
    ("/term-life-insurance/10-year-term/", "10 year term life insurance", "Short obligations, and the trap of the renewal rate."),
    ("/term-life-insurance/20-year-term/", "20 year term life insurance", "The most common choice, and who it fits."),
    ("/term-life-insurance/30-year-term/", "30 year term life insurance", "Long mortgages and young children."),
    ("/term-life-insurance/no-medical-exam/", "No medical exam term life", "Accelerated and simplified issue, and what they cost."),
    ("/term-life-insurance/return-of-premium/", "Return of premium term life", "How it works, and why we rarely recommend it."),
]

AGE_BANDS = [("30 to 34", "32"), ("35 to 39", "37"), ("40 to 44", "42"), ("45 to 49", "47"),
             ("50 to 54", "52"), ("55 to 59", "57"), ("60 to 65", "62")]
COVERAGE_COLS = [("$250,000", "250000"), ("$500,000", "500000"), ("$1,000,000", "1000000")]

TERM_LENGTHS = [
    ("10", "10 years", "A short, specific obligation: the last stretch of a mortgage, a business loan, or the years until a pension starts.",
     "Cheapest per year of coverage, and the renewal rate at the end is steep. Only choose this if the need ends then."),
    ("15", "15 years", "A mid length gap. Common for people who started a family later or refinanced part way through a mortgage.",
     "Often only slightly more than a 10 year term, and it buys five more years of certainty."),
    ("20", "20 years", "The most common choice. It covers a child from elementary school to leaving home, or most of a standard mortgage.",
     "A sound default, but check it against your own dates before you choose it."),
    ("30", "30 years", "A new 30 year mortgage, or very young children, or a much younger partner who would rely on the income.",
     "Costs meaningfully more than 20 years, and for a 30 year old it is often still less than people assume."),
]


def schema():
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("Term Life Insurance", None)]),
            C.faq_schema(FAQ),
            C.person_schema(PATH)]


def _acc(q, a):
    return C.acc(q, a, "term-faq")


def rate_table():
    """The shared rate table (chrome.rate_chart). Each row prefills the quote
    form with its age and $500,000, plus whatever the toggles are set to."""
    return C.rate_chart(
        "term-rates", [label for label, _ in COVERAGE_COLS],
        [(band, {"age": mid, "coverage": "500000"}) for band, mid in AGE_BANDS],
        [("Term length", "term-rate-length", [("20", "20 years"), ("10", "10 years"), ("30", "30 years")], "term_length"),
         ("Sex", "term-rate-sex", [("female", "Female"), ("male", "Male")], "sex"),
         ("Tobacco", "term-rate-tobacco", [("no", "No"), ("yes", "Yes")], "tobacco")],
        "Monthly premium by age band and coverage amount.",
        row_cta="prefill", prefill_target="term-quote-form", min_width="48rem",
        toggle_grid="grid sm:grid-cols-[7fr_4fr_4fr] gap-6 max-w-3xl",
        note="Source: [CARRIER RATE CARD NAME AND EDITION]. Premiums vary by carrier, state, "
             "health, build, family history, and tobacco use. A rate table is an illustration of "
             "shape, not an offer of coverage. Your rate class is decided by the carrier after "
             "underwriting.")


TERM_LENGTH_FIELD = '''<!-- Set by the rate table's "quote this" buttons. -->
<input type="hidden" name="term_length" value="">'''


COVERAGE_OPTIONS = [
    ("", "Choose an amount"), ("100000", "$100,000"), ("250000", "$250,000"),
    ("500000", "$500,000"), ("750000", "$750,000"), ("1000000", "$1,000,000"),
    ("2000000", "$2,000,000 or more"), ("unsure", "Not sure yet"),
]


def quote_form(form_id, form_name, id_prefix, coverage=True):
    """Two steps. Step 1 is about the person, step 2 is how to reach them, with
    the TCPA block above the submit.

    `coverage=False` drops the coverage select, which is the September 2026
    shortening: an agent can ask it on the call, and the field's own hint said
    a rough figure was fine. It stays True only where a rate row or the
    calculator prefills `coverage` into this form, because [data-prefill]
    writes by field name and would silently drop the amount the visitor just
    picked.
    """
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
        (F.row(F.select_field(p + "-coverage", "coverage", "How much coverage?", COVERAGE_OPTIONS,
                              error="Choose a coverage amount, or pick the closest.",
                              hint="A rough figure is fine."),
               F.phone_field(p + "-phone", hint="One agent calls, once."))
         if coverage else
         F.phone_field(p + "-phone", hint="One agent calls, once. We ask what you want to cover "
                                          "on that call."))
        + F.consent_block(p, C.BRAND, 12)
        + F.submit_block("See my quotes", back=True))
    return f"""
        <form id="{form_id}" class="mt-6" data-ax-form data-steps data-silo="term-life"
              data-form-name="{form_name}" data-success-target="{p}-success" novalidate>

          {F.scaffold(TERM_LENGTH_FIELD, 10)}

          {F.progress(2)}

          {F.step(1, "About you", about, first=True)}
          {F.step(2, "Your coverage" if coverage else "How to reach you", cover)}
        </form>

        <div id="{p}-success" class="success">
          <div class="flex items-start gap-3">
            {icon("circle-check", 30, "shrink-0 text-green")}
            <div>
              <h3 class="text-h3 !font-display !font-semibold">Got it</h3>
              <p class="mt-3 text-slate">
                A licensed agent is comparing our appointed carriers for your age, state, and
                coverage amount now. You will hear from us within {C.SLA}, and the quote comes with
                the carrier names on it.
              </p>
              <div class="mt-5">
                {C.phone_link("term_success", "btn btn-call", "Or call " + C.PHONE_DISPLAY)}
              </div>
            </div>
          </div>
        </div>"""


def body():
    # "What happens after you submit": numbered, one step per line, spaced so
    # it reads as four steps rather than one dense paragraph.
    after_steps = "".join(
        f'''<li class="flex items-start gap-3"><span class="shrink-0 grid place-items-center w-7 h-7 rounded-full bg-surface border border-rule text-sm font-semibold text-navy tnum" aria-hidden="true">{n}</span><span class="pt-0.5">{text}</span></li>'''
        for n, text in enumerate([
            "A licensed agent reads it. Every submission. No quote engine, no lead broker.",
            f"We run your details past the {C.CARRIERS} carriers we're appointed with.",
            f"You get named carriers and real premiums within {C.SLA}, on a call to the number you give us.",
            "If nothing fits, we tell you that, and where to look instead.",
        ], 1))
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
        "Want to skip the medical exam?",
        "Several of our carriers can issue term coverage with no paramedical exam for healthy "
        "applicants, often with a decision in days rather than weeks. It usually costs a little "
        "more, and the coverage limits are lower. Sometimes that trade is worth it.",
        '<a class="btn btn-cta btn-block" href="#quote" data-cta-location="term_band">'
        'Get my term life quote</a>'
        '<a class="btn btn-ghost btn-block mt-3" href="/term-life-insurance/no-medical-exam/#who-qualifies">'
        'No medical exam term life</a>',
        eyebrow="No medical exam")
    spokes = C.spoke_module(
        "Term life insurance guides",
        "Eleven short articles, each on one part of term life.",
        SPOKES)
    faq_html = "\n        ".join(_acc(q, a) for q, a in FAQ)
    byline = C.byline_section("section")

    # One h1, one line, one button. The form it points at is the next section
    # but one, so the hero can take a photograph (MASTER.md section 8).
    hero = C.page_hero(
        [("Home", "/"), ("Term Life Insurance", None)],
        "Term life insurance, made simple.",
        "The most coverage for your money, for exactly as long as your family needs it.",
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
        [("list-checks", "About ninety seconds", "Answer six questions",
          "The form on this page, or a phone call if you would rather talk it through. No Social "
          "Security number at this stage."),
         ("search", "Named carriers", "Compare the quotes",
          "You get carrier names, premiums, term lengths, and the conversion terms, so you can "
          "compare them against anything else you have been shown."),
         ("circle-check", "We stay with it", "Apply and go through underwriting",
          "We complete the application with you and stay with it until the policy is issued or the "
          "carrier says no. Either way you hear it from us.")],
        cta=("Ready when you are.", "Free, with no obligation.",
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
          <p class="reveal mt-5 text-slate">
            Six questions, about ninety seconds. No payment details, no credit check.
          </p>

          <p class="reveal mt-6 preflight">
            {icon("list-checks", 20, "shrink-0 text-navy mt-0.5")}
            <span><span class="font-semibold text-navy">You'll need:</span> your age, your state,
            tobacco use, and a phone number. Nothing else.</span>
          </p>

          <div class="reveal mt-8 pt-8 border-t border-rule">
            <p class="font-semibold text-navy">What happens after you submit</p>
            <ol class="mt-4 grid gap-4 text-slate">
              {after_steps}
            </ol>
          </div>
        </div>
      </div>

      <div class="lg:col-span-6 lg:col-start-7">
        <div class="panel reveal">
          {quote_form("term-quote-form", "term_hero_quote", "th")}
        </div>

        <ul class="reveal mt-8 px-1 grid gap-3 text-sm text-slate">
          <li class="flex items-start gap-3">{icon("shield-check", 18, "shrink-0 text-navy mt-0.5")}<span>Your details stay with us. Not sold, not shared with other agencies or lead buyers.</span></li>
          <li class="flex items-start gap-3">{icon("badge-check", 18, "shrink-0 text-navy mt-0.5")}<span>Licensed in {C.STATES} states. {C.BRAND}, NPN {C.NPN}.</span></li>
          <li class="flex items-start gap-3">{icon("circle-check", 18, "shrink-0 text-navy mt-0.5")}<span>No obligation. One agent calls you, once, and nobody else does.</span></li>
        </ul>

        <p class="reveal mt-6 px-1 pt-6 border-t border-rule text-sm text-slate">
          <span class="font-semibold text-navy">Rather talk it through?</span>
          Call {C.phone_link("term_form_side", "link font-semibold inline-flex items-center gap-1 whitespace-nowrap", size=16)},
          <span class="text-muted">{C.HOURS}.</span>
        </p>
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
          years. It builds no cash value and it ends when the term does. That is why it costs so
          much less than permanent coverage.
        </p>
        <p class="reveal mt-5 text-slate">
          For most households that number is the years left on the mortgage, or the years until
          the youngest child is independent, whichever runs longer.
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
          <h3 class="text-h3 !font-display !font-semibold">When term life is not the right fit</h3>
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
          The last one points toward final expense insurance, compared below.
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

{C.ask_strip("Ready to get a term life quote?", "Six questions, about ninety seconds.", '<a href="#quote" class="btn btn-cta">Get my term life quote</a>')}

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
        {C.timeline([
            ('Day 1',
             'Application',
             'We complete it with you, by phone or electronically. Twenty to thirty minutes, including the health and lifestyle questions.'),
            ('Day 1 to 5',
             'Phone interview and database checks',
             'The carrier confirms your answers and pulls your prescription history, motor vehicle record, and medical information database file.'),
            ('Day 3 to 10, if required',
             'The medical exam',
             'A paramedical examiner comes to your home or office. Height, weight, blood pressure, a blood sample, and a urine sample. Around twenty minutes. It is free and you do not arrange it yourself.'),
            ('Week 2 to 5',
             'Medical records and review',
             "This is the slow part, and it is your doctor's office rather than the carrier. An underwriter then assigns a rate class."),
            ('Week 3 to 6',
             'Offer, and your decision',
             'If the rate class is worse than we quoted, we say so and tell you what it means in dollars. You can accept, ask us to shop it elsewhere, or walk away.')])}

        <p class="reveal mt-8 pt-6 border-t border-rule text-sm text-muted">
          Nothing is owed and no coverage is in force until the policy is issued, delivered, and the
          first premium is paid.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- The three products side by side. Shared with the other two hubs. -->
{C.product_compare(
    "term", "How term life differs from whole life and final expense",
    "Term life is the cheapest way to cover a fixed number of years. The other two last for "
    "life and cost more for it.",
    '<a href="#quote" class="btn btn-cta btn-block">Get my term life quote</a>',
    "Free, no obligation &#183; or call " + C.phone_link("term_compare", "link inline-flex items-center gap-1 whitespace-nowrap", size=14),
    cls="section")}

<!-- =====================================================================
     6. NO EXAM TEASER.
     ================================================================== -->
{no_exam_band}

<!-- 8. HOW TO APPLY. The same connected stepper as the homepage. -->
{how_to_apply}


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

<!-- Guides, laid out as blog posts. After the FAQ by client request. -->
{spokes}

<!-- =====================================================================
     11. BYLINE.
     ================================================================== -->
{byline}

<!-- =====================================================================
     12. FINAL FORM CTA.
     ================================================================== -->
<section class="section glow">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5 reveal">
        <h2 class="text-h2">Get your quotes</h2>
        <p class="mt-5 text-slate">
          Five questions, about ninety seconds. A licensed agent replies with named carriers and
          real premiums. Your details are never sold, and nobody else calls you.
        </p>
        <p class="mt-6 text-sm text-muted">
          Want to talk it through first? The number is in the header of every page, and you
          will reach a licensed agent.
        </p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7 reveal">
        <div class="panel">
          <div class="panel-head">
            <h3 class="text-h3 !font-display !font-semibold">Start your quote</h3>
          </div>
          {quote_form("term-quote-form-footer", "term_footer_quote", "tf", coverage=False)}
        </div>
      </div>
    </div>
  </div>
</section>
"""
