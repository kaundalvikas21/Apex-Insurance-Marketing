# -*- coding: utf-8 -*-
"""HOME. Spec section 01, reframed to the client outline (see
design-system/pages/home.md).

Order: hero, USP strip, how it works, why us, coverage types, triage, FAQ,
closing pair. One idea per section, plain headings. It links to hubs, never
to spokes.
"""
from icons import icon
import chrome as C

PATH = "/"
OUT = "index.html"
ACTIVE = "/"
SILO = "site"
TITLE = "Life Insurance Quotes from an Independent Agency | Apex"
OG_TITLE = "Compare life insurance from multiple carriers"
DESC = ("Independent, licensed life insurance agency. Compare term life, whole life and final "
        "expense coverage from multiple carriers. Free quotes, no obligation.")

FAQ = [
    ("How much life insurance do I actually need?",
     "There is no single right answer, but most households start by covering what would still have "
     "to be paid if the income stopped: the mortgage balance, any other debt, the cost of raising "
     "children to adulthood, and a cushion for the surviving partner. A common starting point is "
     "ten to twelve times annual income, then adjusted up or down for savings, existing employer "
     "coverage, and how long the dependents will actually need support. A licensed agent can walk "
     "through the specific numbers with you at no cost."),
    ("What is the difference between term and whole life insurance?",
     "Term life covers you for a fixed number of years, usually 10 to 30, and pays a death benefit "
     "only if you die during that term. It has no cash value and it is the least expensive way to "
     "buy a large death benefit. Whole life covers you for your entire life, has a guaranteed "
     "premium and a guaranteed cash value that builds over time, and costs significantly more per "
     "dollar of coverage. Term suits temporary obligations. Whole life suits permanent ones."),
    ("Do I have to take a medical exam?",
     "Not always. Many carriers now offer accelerated underwriting for healthy applicants, which "
     "uses prescription history, motor vehicle records, and medical databases instead of a "
     "paramedical exam. Final expense policies are almost always issued on health questions alone "
     "with no exam. Fully underwritten policies that do include an exam usually offer the lowest "
     "premium, so the exam is often worth the inconvenience if you are in good health."),
    ("Can I get life insurance if I have a health condition?",
     "Usually yes, though the premium and the available coverage depend on the condition, how well "
     "it is controlled, and which carrier you apply to. Carriers underwrite the same condition very "
     "differently, which is the main practical argument for using an independent agency: we can "
     "place the application with the carrier that treats your specific situation most favorably "
     "rather than accepting one company's decline as final."),
    ("How much does life insurance cost?",
     "Premium depends on your age, sex, health, tobacco use, the type of policy, the coverage "
     "amount, and the carrier. Age is the single largest factor and it moves against you every "
     "year. Each of our product pages includes a rate table showing sample premiums by age band so "
     "you can see the shape of the pricing before you speak to anyone. Your actual quote comes from "
     "the carrier after underwriting."),
    ("Does it cost more to buy through an agency?",
     "No. Life insurance rates are filed with state insurance departments, so the premium for a "
     "given policy is the same whether you buy it through an independent agency, through a captive "
     "agent, or directly from the carrier. The carrier pays our commission out of that premium. You "
     "never pay Apex a fee."),
]


def schema():
    return [C.org_schema(),
            C.faq_schema(FAQ),
            C.person_schema(PATH)]


# ---------------------------------------------------------------------------
def _cover_card(name, fig, line, href, anchor, tone=""):
    """One coverage type. `fig` is a spec figure shown as a pill, never a rate."""
    return f"""
        <div class="reveal bento-cell bento-2 card-hover {tone}">
          <div class="flex items-center justify-between gap-3">
            <h3 class="text-h4">{name}</h3>
            <span class="pill">{fig}</span>
          </div>
          <p class="mt-3 text-sm text-slate">{line}</p>
          <div class="mt-5 lg:mt-auto lg:pt-5"><a class="btn-row" href="{href}">{anchor} {icon("arrow-right", 16)}</a></div>
        </div>"""


def _why(name, title, body, extra=""):
    """A raised white-at-8% surface, not a white card: headings stay white and
    the navy-band .step-num rule already handles the icon circle."""
    return f"""
        <div class="reveal bento-3 border border-white/20 bg-white/8 rounded-[12px] p-6 lg:p-7">
          <span class="step-num" aria-hidden="true">{icon(name, 22)}</span>
          <h3 class="mt-4 text-h4 text-white">{title}</h3>
          <p class="mt-2 text-white/82">{body}</p>{extra}
        </div>"""


def body():
    return HERO + rest() + DIALOG


# One tagline, one supporting line, one CTA, over the client's banner photograph.
# trail=None: the homepage is the one page with no breadcrumb.
HERO = C.page_hero(
    None,
    "Get your family covered.",
    "Life insurance from multiple carriers, compared for you by a licensed, independent agent.",
    extra=C.hero_cta("/get-a-quote/", "Get a free quote"),
    banner="home-banner") + f"""
<!-- USP strip, directly beneath the hero CTA. -->{C.usp_strip([
    ("shield-check", "Licensed in " + C.STATES + " states", "Real licensed agents"),
    ("scale", "Independent agency", "We work for you, not one carrier"),
    ("building", C.YEARS + " years", "Placing life insurance"),
    ("handshake", "Free, no obligation", "You never pay us a fee"),
])}
"""


# The one timed surface on the site. site.js opens it once per session, on this
# page only, and never in senior mode. It carries no form, so there is no
# second TCPA block and nothing for collect() to see.
DIALOG = f"""
<dialog id="review-dialog" class="dialog" data-dialog-timed aria-labelledby="review-dialog-title">
  <form method="dialog">
    <button class="dialog-close" aria-label="Close">{icon("x", 22)}</button>
  </form>
  <h2 id="review-dialog-title" class="text-h3 !font-display !font-semibold">Already have life insurance?</h2>
  <p class="mt-3 text-slate">
    Get a free, no-obligation review from a licensed agent. We check that it still fits and that
    you are not overpaying.
  </p>
  <div class="mt-6 grid gap-3">
    <a href="/free-policy-review/" class="btn btn-cta btn-block" data-dialog-cta>Get my free policy review</a>
    {C.phone_link("review_dialog", "btn btn-ghost btn-block", "Call " + C.PHONE_DISPLAY)}
  </div>
  <p class="mt-4 text-micro text-muted">Free &#183; No obligation &#183; Nothing has to change</p>
</dialog>
"""


def _tile(score, mark, label, hint=""):
    """One quiz answer. `mark` is finished HTML: an icon, or a figure for the
    age question. A <button> with aria-pressed, so the pick is announced and is
    never signalled by colour alone (the check badge appears with it)."""
    sub = f'<span class="triage-opt-hint">{hint}</span>' if hint else ""
    return f"""
              <button type="button" class="triage-opt" data-score="{score}" aria-pressed="false">
                <span class="triage-opt-mark" aria-hidden="true">{mark}</span>
                <span class="triage-opt-text"><span class="triage-opt-label">{label}</span>{sub}</span>
                <span class="triage-opt-check" aria-hidden="true">{icon("check", 14)}</span>
              </button>"""


def _question(heading, tiles):
    return f"""
          <div data-triage-q hidden>
            <h3 data-triage-heading class="quiz-q">{heading}</h3>
            <div class="quiz-grid">{"".join(tiles)}
            </div>
          </div>"""


def _result(key, ico, heading, body, actions, extra=""):
    return f"""
          <div data-triage-result="{key}" hidden class="quiz-result">
            <span class="step-num" aria-hidden="true">{icon(ico, 22)}</span>
            <p class="mt-4"><span class="pill">Your best fit</span></p>
            <h3 class="mt-3 text-h3 !font-display !font-semibold">{heading}</h3>
            <p class="mt-4 text-slate">{body}</p>
            <div class="mt-6 flex flex-wrap items-center justify-center gap-5">
              {actions}
              <button type="button" data-triage-restart class="link text-sm">Start over</button>
            </div>{extra}
          </div>"""


def _fig(text):
    return f'<span class="triage-opt-fig tnum">{text}</span>'


# The quiz. It is deliberately NOT the FAQ's shape: centred, one wide card, a
# progress bar, and answers as tiles rather than rows. Scores live in the
# markup next to the copy they belong to. Results link to a different section
# of each hub, so no target on this page is linked twice (spec section 07).
TRIAGE = f"""
<!-- =====================================================================
     TRIAGE. Three questions, no email wall.
     ================================================================== -->
<section id="triage" class="section band">
  <div class="container-ax">
    <div class="max-w-2xl mx-auto text-center">
      <h2 class="reveal text-h2">Not sure which one you need?</h2>
      <p class="reveal mt-5 text-slate">
        Three quick questions. No email, no phone number, and nothing is sent anywhere.
      </p>
    </div>

    <div class="quiz panel reveal" data-triage>

      <div data-triage-head>
        <div class="progress-track" aria-hidden="true">
          <span class="progress-seg" data-triage-seg></span>
          <span class="progress-seg" data-triage-seg></span>
          <span class="progress-seg" data-triage-seg></span>
        </div>
        <div class="flex items-center justify-between gap-4 text-sm text-muted">
          <p data-triage-progress class="font-medium"></p>
          <p>About 30 seconds</p>
        </div>
      </div>

      <noscript>
        <p class="mt-6 text-slate">This short quiz needs JavaScript. The three cards above describe
        each type of coverage, and a licensed agent can talk you through them.</p>
      </noscript>
{_question("What is the money mainly for?", [
    _tile("term:3", icon("users", 24), "Replace my income", "While my family still depends on it"),
    _tile("whole:3,final:1", icon("heart", 24), "Leave something behind", "No matter when I die"),
    _tile("final:3", icon("banknote", 24), "Cover my funeral", "And the bills that come with it"),
])}
{_question("How old are you?", [
    _tile("term:3", _fig("&lt;45"), "Under 45"),
    _tile("term:2,whole:2", _fig("45+"), "45 to 59"),
    _tile("final:3,whole:1", _fig("60+"), "60 or older"),
])}
{_question("Which matters more to you?", [
    _tile("term:3,final:1", icon("trending-up", 24), "The lowest premium", "For the most coverage"),
    _tile("whole:3,final:2", icon("shield-check", 24), "Coverage that never ends", "It cannot expire or be canceled"),
    _tile("final:3", icon("stethoscope", 24), "No medical exam", "Approved on health questions"),
])}

      <button type="button" data-triage-back hidden class="quiz-back">{icon("arrow-left", 16)}Back</button>
{_result("term", "clock", "Start with term life insurance",
    "You are describing a temporary obligation with a large price tag. Term buys the most coverage "
    "per dollar for exactly as long as that obligation lasts, then it ends. If the need turns out "
    "to be permanent, most term policies can be converted later without a new medical exam.",
    '<a class="btn btn-cta" href="/term-life-insurance/#quote">Get my term life quote</a>')}
{_result("whole", "shield-check", "Look at whole life insurance",
    "You want the policy to still be there whenever it is needed, which term cannot promise. Whole "
    "life costs considerably more per dollar of death benefit, so the honest next step is a written "
    "illustration you can read at your own pace, not a rushed application.",
    '<a class="btn btn-cta" href="/whole-life-insurance/#quote">Get my whole life quote</a>')}
{_result("final", "heart", "Final expense insurance is probably the fit",
    "You need a smaller policy, issued on health questions rather than a medical exam, that pays "
    "quickly and covers a funeral and the bills around it. This is almost always faster to arrange "
    "by phone than by form.",
    C.phone_link("triage_result_final", "btn btn-call", "Call " + C.PHONE_DISPLAY),
    extra='''
            <p class="mt-4 text-micro text-muted">
              Or read what
              <a class="link" href="/final-expense-insurance/#costs">final expense insurance costs by age</a>.
            </p>''')}
    </div>

    <p class="reveal mt-6 text-center text-sm text-muted">
      Want the longer version? Read our
      <a class="link" href="/compare/term-vs-whole-life-insurance/">comparison of term and whole life insurance</a>.
    </p>
  </div>
</section>"""


def _acc(q, a):
    return C.acc(q, a, "home-faq")


REST = """
<!-- HOW IT WORKS. chrome.steps_section(): a connected 1, 2, 3 ending in the ask. -->
{steps}

<!-- =====================================================================
     WHY US. Four reasons, each one line. The commission detail lives in the
     last FAQ answer.
     ================================================================== -->
<section class="section band-navy on-navy">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Why choose Apex</h2>
      <p class="reveal mt-5 text-lead text-white/88">
        Licensed agents, multiple carriers, and no sales pressure.
      </p>
    </div>

    <div class="mt-10 bento" data-stagger="40">{why_html}
    </div>

    <!-- [REAL ATTRIBUTABLE REVIEWS ONLY - DO NOT FABRICATE]
         The slot is designed and wired. It stays hidden until real,
         attributable, consented reviews exist. Remove the hidden
         attribute and populate data-reviews-list at that point. -->
    <div class="reveal mt-6 border border-dashed border-white/25 rounded-[12px] p-6" data-reviews-slot hidden>
      <p class="text-sm text-white/70">What clients say</p>
      <div data-reviews-list></div>
    </div>
  </div>
</section>

<!-- =====================================================================
     COVERAGE TYPES. One sentence each, then exactly two CTAs.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Which type of life insurance is right for you?</h2>
      <p class="reveal mt-5 text-slate">Three kinds of coverage. Most people only need one.</p>
    </div>

    <div class="mt-10 bento" data-stagger="40">{cover_html}
    </div>

    <div class="reveal mt-10 flex flex-wrap items-center gap-3">
      {call_cover}
      <a href="/get-a-quote/" class="btn btn-cta">Get a free quote</a>
    </div>
    <p class="reveal mt-4 text-sm text-muted">
      Not sure? <a class="link" href="#triage">Answer three questions</a> and we will point you to the right one.
    </p>
  </div>
</section>

{triage}

<!-- =====================================================================
     FAQ. Native details elements, plus FAQPage schema in the head.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">

      <div class="lg:col-span-4">
        <h2 class="reveal text-h2">Most asked life insurance questions</h2>
        <p class="reveal mt-5 text-slate">
          Straight answers to what people ask us most.
        </p>
        <p class="reveal mt-6 text-sm text-muted">
          Still stuck? Call and ask. There is no script and no obligation.
        </p>
        <div class="reveal mt-4">{call_faq}</div>
      </div>

      <div class="lg:col-span-7 lg:col-start-6 reveal">
        {faq_html}
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     FINAL CTA, split by intent. Spec section 01.8.
     ================================================================== -->
<section class="section-tight border-t border-rule glow">
  <div class="container-ax">
    <div class="grid md:grid-cols-2 gap-6" data-stagger="40">

      <div class="reveal card card-hover">
        <h2 class="text-h3 !font-display !font-semibold">Get a free quote online</h2>
        <p class="mt-3 text-slate max-w-md">
          Send us the basics and a licensed agent comes back with what our carriers will actually
          offer you, usually the same business day.
        </p>
        <a class="btn btn-cta mt-6" href="/contact/">Get a free quote</a>
        <p class="mt-3 text-micro text-muted">Free &#183; No obligation &#183; Licensed agents</p>
      </div>

      <div class="reveal card card-hover">
        <h2 class="text-h3 !font-display !font-semibold">Talk to a licensed agent</h2>
        <p class="mt-3 text-slate max-w-md">
          Most of these questions are faster to answer out loud. You will reach a licensed agent,
          not a queue.
        </p>
        {call_final}
        <p class="mt-3 text-micro text-muted">{hours}</p>
      </div>
    </div>
  </div>
</section>
"""


def rest():
    return REST.format(
        steps=C.steps_section(
            "Three simple steps to get covered",
            "No pressure at any step. Stop whenever you like.",
            [("list-checks", "A few minutes", "Tell us about you",
              "Answer a few basics like your age and state. It takes a few minutes."),
             ("search", "We do the work", "We compare plans for you",
              "A licensed agent checks multiple carriers and finds the plans that fit you."),
             ("circle-check", "Your decision", "Choose your plan",
              "Review your options, ask us anything, and pick the one you like. Only if you want to.")],
            cta=("Ready when you are.", "No Social Security number needed for a quote.",
                 '<a href="/get-a-quote/" class="btn btn-cta">Get a free quote</a>')),
        why_html="".join([
            _why("scale", "Independent agency",
                 "We work for you, not for one insurance company. If one carrier prices you badly, "
                 "we take you to another."),
            _why("user-check", "Licensed agents",
                 "You talk to a licensed agent, not a script. Every page here is reviewed by one.",
                 '\n          <a class="link-static mt-4 inline-block text-sm" href="/about/agents/">'
                 'Meet our licensed agents</a>'),
            _why("banknote", "No fee, ever",
                 "The insurance company pays us, not you. You pay the same price as going direct."),
            _why("stethoscope", "No medical exam options",
                 "Many policies ask health questions instead of a medical exam. We tell you up front "
                 "which ones may fit you."),
        ]),
        cover_html="".join([
            _cover_card("Term life insurance", "10 to 30 years",
                        "Affordable coverage for a set number of years. A good fit while you have a "
                        "mortgage or children at home.",
                        "/term-life-insurance/", "Learn about term life"),
            _cover_card("Whole life insurance", "For life",
                        "Coverage that lasts your whole life, with a premium that never rises and cash "
                        "value that builds.",
                        "/whole-life-insurance/", "Learn about whole life", tone="bento-cell-tint"),
            _cover_card("Final expense insurance", "$2,000 to $50,000",
                        "A smaller policy for funeral costs and final bills, ages 50 to 85. Health "
                        "questions, no medical exam.",
                        "/final-expense-insurance/", "Learn about final expense"),
        ]),
        call_cover=C.phone_link("home_coverage", "btn btn-call", "Call " + C.PHONE_DISPLAY),
        triage=TRIAGE,
        call_faq=C.phone_link("faq_inline", "btn btn-ghost", "Call " + C.PHONE_DISPLAY),
        call_final=C.phone_link("final_cta_split", "btn btn-call mt-6", "Call " + C.PHONE_DISPLAY),
        hours=C.HOURS,
        faq_html="\n          ".join(_acc(q, a) for q, a in FAQ),
    )
