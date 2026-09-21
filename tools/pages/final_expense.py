# -*- coding: utf-8 -*-
"""FINAL EXPENSE HUB. Spec section 04. Phone first, senior accessibility.

Design constraints on this page override everything else:
  html.fe sets an 18px base, so the whole rem ramp moves up one notch.
  Minimum tap target 56px. Very high contrast. Short paragraphs.
  Reveal-only motion: no translate, no stagger, no CTA lift.
Primary CTA is the phone, repeated after every second section.
"""
from icons import icon
import chrome as C
import forms as F
from forms import ERR

PATH = "/final-expense-insurance/"
OUT = "final-expense-insurance/index.html"
ACTIVE = PATH
SILO = "final-expense"
HTML_CLASS = "fe"
TITLE = "Final Expense Insurance: Cover a Funeral, No Medical Exam | Apex"
OG_TITLE = "Final expense insurance, explained by a licensed agent"
DESC = ("Final expense insurance covers funeral and burial costs for ages 50 to 85. No medical "
        "exam, health questions only. Talk to a licensed independent agent in about 15 minutes.")

FAQ = [
    ("What is final expense insurance?",
     "It is a small whole life insurance policy, usually between $2,000 and $50,000, bought to "
     "cover a funeral, burial or cremation, and the bills that arrive in the weeks after a death. "
     "The premium never rises and the coverage never expires as long as the premium is paid. It is "
     "sometimes sold under the names burial insurance or funeral insurance. Those are the same "
     "product with a different label."),
    ("Do I need a medical exam?",
     "No. Final expense policies are issued on health questions alone. There is no paramedical "
     "exam, no blood work, and no urine sample. The carrier will check your prescription history "
     "and a medical information database, so answer the health questions accurately. An answer "
     "that does not match the records can delay the policy or void a claim later."),
    ("Can I be turned down?",
     "You can be declined for a policy that pays from day one, but there is almost always an "
     "option available. Carriers sort applicants into level benefit, graded benefit, and "
     "guaranteed issue, and the last of those asks no health questions at all. What changes with "
     "poorer health is the premium and whether there is a waiting period, not usually whether you "
     "can get covered."),
    ("What is a waiting period?",
     "Some final expense policies do not pay the full death benefit if you die of natural causes "
     "in the first two or three years. Instead they refund the premiums you paid, usually with "
     "interest added. Accidental death is normally covered in full from the first day. If you "
     "qualify for a level benefit policy, there is no waiting period at all. We will tell you "
     "which one you qualify for before you apply."),
    ("How fast does the money reach my family?",
     "Once the carrier has a certified death certificate and a completed claim form, most final "
     "expense claims are paid within a few business days to two weeks. Many carriers will assign "
     "the benefit directly to a funeral home so the family does not have to pay up front and wait "
     "for reimbursement."),
    ("Can I still get this if I have diabetes, COPD, or heart problems?",
     "In most cases yes. Controlled diabetes is routinely accepted at level rates by several "
     "carriers. COPD, congestive heart failure, and a recent cardiac event more often lead to a "
     "graded benefit or a guaranteed issue policy. Carriers underwrite these conditions very "
     "differently from each other, which is the practical reason to apply through an independent "
     "agency rather than to one company."),
    ("Will the premium go up as I get older?",
     "No. The premium on a final expense whole life policy is locked at the age you buy it and "
     "stays level for the rest of your life. What does change is the price of buying a new policy: "
     "every birthday you wait makes the same coverage cost more."),
    ("Is this the same as pre-paying at a funeral home?",
     "No, and the difference matters. A pre-need contract is money paid to one funeral home for a "
     "named list of goods and services at that home. A final expense policy pays cash to the "
     "person you name as beneficiary, who can spend it at any funeral home, or on a headstone, "
     "unpaid medical bills, or anything else. If you move or change your mind, the policy moves "
     "with you."),
]

SPOKES = [
    ("/final-expense-insurance/burial-insurance/", "Burial insurance",
     "The same product under the name people search for most."),
    ("/final-expense-insurance/quotes/", "Final expense quotes",
     "What we need from you and how fast a quote comes back."),
    ("/final-expense-insurance/cost/", "Final expense cost by age",
     "How premium moves between ages 50 and 85."),
    ("/final-expense-insurance/for-seniors/", "Final expense for seniors",
     "What changes after 70, and what still does not."),
    ("/final-expense-insurance/no-waiting-period/", "Policies with no waiting period",
     "Which carriers pay in full from day one and who qualifies."),
    ("/final-expense-insurance/funeral-insurance/", "Funeral insurance",
     "How this compares with pre paying at a funeral home."),
    ("/final-expense-insurance/what-is-final-expense-insurance/", "What final expense insurance is",
     "The plain definition, with the fine print left in."),
    ("/final-expense-insurance/for-parents/", "Coverage for a parent",
     "Buying a policy on a parent, and the consent it needs."),
    ("/final-expense-insurance/cremation-insurance/", "Cremation insurance",
     "What cremation actually costs and how much coverage fits."),
]


def schema():
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("Final Expense Insurance", None)]),
            C.faq_schema(FAQ),
            C.person_schema(PATH)]


# --- Repeating phone band. Spec: after every second section. ---------------
def call_band(heading, sub, where, photo=None):
    # photo= turns the flat navy band into a photographed banner. Used once,
    # on the middle band: three photo bands on one page would stop reading as
    # a break and start reading as wallpaper.
    if photo:
        return C.banner(photo, heading, sub,
                        C.phone_link(where, "btn btn-call btn-xl btn-block !bg-white !text-navy",
                                     "Call " + C.PHONE_DISPLAY, 26)
                        + '<p class="mt-3 text-sm text-white/75 text-center">%s</p>' % C.HOURS)
    return f"""
<section class="section-tight band-navy on-navy">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-8 items-center">
      <div class="lg:col-span-7">
        <h2 class="reveal text-h3 !font-display !font-semibold text-white">{heading}</h2>
        <p class="reveal mt-3 text-white/85">{sub}</p>
      </div>
      <div class="lg:col-span-5 reveal">
        {C.phone_link(where, "btn btn-call btn-xl btn-block !bg-white !text-navy", "Call " + C.PHONE_DISPLAY, 26)}
        <p class="mt-3 text-sm text-white/75 text-center">{C.HOURS}</p>
      </div>
    </div>
  </div>
</section>"""


def _acc(q, a):
    return C.acc(q, a, "fe-faq", 24)


# --- Rate table -----------------------------------------------------------
AGE_BANDS = ["50 to 54", "55 to 59", "60 to 64", "65 to 69", "70 to 74", "75 to 79", "80 to 85"]
# Three columns at most on this page (senior readability). The full coverage
# range is described in the scale above the table.
COVERAGE_COLS = ["$10,000", "$25,000"]


def rate_rows(sex):
    rows = []
    for band in AGE_BANDS:
        cells = "".join('<td class="tnum">$--</td>' for _ in COVERAGE_COLS)
        # The row-level call CTA sits under the age label so the table stays at
        # three columns.
        call = C.phone_link("rate_table_" + sex, "btn-row mt-2", "Get this quoted", 18)
        rows.append(f'<tr><th scope="row"><span class="block">{band}</span>{call}</th>{cells}</tr>')
    return "\n            ".join(rows)


def rate_table():
    heads = "".join('<th scope="col" class="tnum">%s</th>' % c for c in COVERAGE_COLS)
    return f"""
      <div data-panels="fe-rates">
      <div class="reveal mt-8 flex flex-wrap items-end gap-6">
        <fieldset>
          <legend class="field-label">Show premiums for</legend>
          <div class="choice-row">
            <label class="choice">
              <input type="radio" name="fe-rate-sex" value="female" checked>
              <span>Female</span>
            </label>
            <label class="choice">
              <input type="radio" name="fe-rate-sex" value="male">
              <span>Male</span>
            </label>
          </div>
        </fieldset>
        <p class="text-sm text-muted">Non tobacco, level benefit. Tobacco rates are higher.</p>
      </div>

      <div class="reveal mt-6 table-scroll table-signature">
        <table class="rate-table" style="min-width:0">
          <caption>
            Monthly premium by age band and coverage amount.
            <span data-panel-caption>Showing female.</span>
          </caption>
          <thead>
            <tr>
              <th scope="col">Age at application</th>
              {heads}
            </tr>
          </thead>
          <tbody data-panel="female">
            {rate_rows("female")}
          </tbody>
          <tbody data-panel="male" hidden>
            {rate_rows("male")}
          </tbody>
        </table>
      </div>

      </div>

      <p class="reveal mt-4 text-sm text-muted">
        <span class="pill mr-2">Rates last updated: {C.RATES_DATE}</span>
        Source: [CARRIER RATE CARD NAME AND EDITION].
        Premiums vary by carrier, state, health, and tobacco use, and are not an offer of coverage.
      </p>"""


def body():
    # No parallax and no wipe: this page is exempt from transform-based motion.
    # One h1, one line, one button, and the button is the phone. No glow: fe.
    hero = C.page_hero(
        [("Home", "/"), ("Final Expense Insurance", None)],
        "Final expense insurance, made simple.",
        "A small whole life policy for funeral costs and final bills. No medical exam, and the "
        "premium never goes up.",
        extra='''<div class="reveal mt-8">
        %s
        <p class="mt-3 text-slate">%s</p>
      </div>''' % (C.phone_link("fe_hero_primary", "btn btn-call btn-xl", "Call " + C.PHONE_DISPLAY, 28), C.HOURS),
        banner="fe-hero")
    usps = C.usp_strip([
        ("users", "Ages 50 to 85", "Accepted"),
        ("stethoscope", "No medical exam", "Health questions only"),
        ("shield-check", "Premium locked for life", "It never goes up"),
        ("banknote", "$2,000 to $50,000", "Sized for final bills"),
    ])
    hands_media = C.figure("fe-hands", "(min-width: 1024px) 44vw, 92vw", cls="reveal mt-10")
    call_band_1 = call_band(
        "Would you rather just ask someone?",
        "A licensed agent can answer the health questions with you and tell you what you qualify for.",
        "fe_repeat_1")
    call_band_2 = call_band(
        "Not sure which of the three you need?",
        "Tell us your age and what you are trying to cover, and we will say so plainly.",
        "fe_repeat_2", photo="fe-band")
    # Sits directly under "How to apply. One call, about fifteen minutes." Its
    # copy deliberately does not restate that heading: the section above has
    # already covered the how, so this band only removes the last reason to
    # put the call off.
    call_band_3 = call_band(
        "You do not need anything ready to start",
        "Nothing to print, nothing to post, no exam to book. If one of the four things above is "
        "missing, call anyway and we will work around it.",
        "fe_repeat_3")
    spokes = C.spoke_module(
        "Explore final expense insurance",
        "The nine questions people ask most often about this coverage, each answered in full on "
        "its own page.",
        SPOKES)
    call_faq = C.phone_link("fe_faq", "btn btn-call", "Call " + C.PHONE_DISPLAY, 22)
    byline = C.byline()
    faq_html = "\n        ".join(_acc(q, a) for q, a in FAQ)

    how_to_apply = C.steps_section(
        "How to apply. One call, about fifteen minutes.",
        "There is no paperwork to post and nothing to print. Have these four things nearby and the "
        "call goes quickly.",
        [("file-text", None, "Your date of birth and address",
          "Exactly as they appear on your driver licence or state ID."),
         ("stethoscope", None, "Your medications",
          "The bottles are easiest. Names and doses are what the carrier asks for."),
         ("users", None, "Your beneficiary",
          "The full name and date of birth of whoever should receive the money."),
         ("banknote", None, "Your bank details",
          "Premiums are paid by monthly bank draft. Nothing is taken until the policy is approved.")],
        after='''
    <p class="reveal mt-10 text-slate max-w-3xl">
      Many carriers give a decision on the call. Some take a few days. Either way you will know
      what you have been offered, including any waiting period, before you agree to anything.
    </p>''',
        cls="section band", fe=True, label="Item")

    return f"""
{hero}
{usps}

<!-- =====================================================================
     GET IN TOUCH. Phone first, with the four field call-back form as the
     secondary. Moved out of the hero so the hero can stay one line and one
     button.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">

      <div class="lg:col-span-5">
        <div class="sticky-col">
          <h2 class="reveal text-h2">Speak to a licensed agent</h2>
          <p class="reveal mt-5 text-slate">
            Most calls take about fifteen minutes. There is no medical exam. You answer health
            questions instead.
          </p>
          <div class="reveal mt-6">
            {C.phone_link("fe_contact_primary", "btn btn-call btn-xl btn-block sm:!w-auto", "Call " + C.PHONE_DISPLAY, 28)}
            <p class="mt-3 text-slate">{C.HOURS}</p>
          </div>

        <div class="reveal mt-8 pt-8 border-t border-rule">
          <h3 class="text-h4">What happens when you get in touch</h3>
          <ol class="mt-4 grid gap-3">
            <li class="flex items-start gap-3">
              <span class="text-navy font-semibold tnum shrink-0">1.</span>
              <span>A licensed agent picks up, or reads your form. Not a call centre.</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="text-navy font-semibold tnum shrink-0">2.</span>
              <span>We ask the health questions and compare our carriers with you.</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="text-navy font-semibold tnum shrink-0">3.</span>
              <span>You hear what you qualify for, what it costs, and whether there is a waiting period. Then you decide, in your own time.</span>
            </li>
          </ol>
        </div>

        </div>
      </div>

      <!-- Secondary CTA. Four fields, one step, no scrolling inside the form. -->
      <div class="lg:col-span-6 lg:col-start-7">
        <div class="panel reveal">
          {callback_form("fe_hero", "fe_hero_callback")}
        </div>
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     2. COVERAGE AMOUNTS as a simple visual scale.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">How much coverage people usually buy</h2>
      <p class="reveal mt-5 text-slate">
        Final expense policies run from about $2,000 to about $50,000. Most people buy somewhere in
        the middle, because they are covering a funeral rather than replacing an income.
      </p>
    </div>

    <div class="reveal mt-10 card">
      <div class="flex items-baseline justify-between text-sm font-semibold text-navy tnum">
        <span>$2,000</span>
        <span>$50,000</span>
      </div>
      <div class="mt-3 h-4 w-full bg-navy-050 border border-rule rounded-full overflow-hidden">
        <div class="h-full bg-navy-700 rounded-full" style="margin-left:12%;width:34%"></div>
      </div>
      <p class="mt-3 text-sm text-navy font-semibold">
        The shaded band is roughly $8,000 to $20,000, where most policies we place land.
      </p>
      <div class="mt-8 pt-8 border-t border-rule grid sm:grid-cols-3 gap-6">
        <div>
          <p class="text-h3 !font-display !font-semibold text-navy tnum">$2,000 to $8,000</p>
          <p class="mt-2 text-slate">Cremation, a simple service, and a few outstanding bills.</p>
        </div>
        <div>
          <p class="text-h3 !font-display !font-semibold text-navy tnum">$8,000 to $20,000</p>
          <p class="mt-2 text-slate">A traditional burial with a service, plus room for the bills that follow.</p>
        </div>
        <div>
          <p class="text-h3 !font-display !font-semibold text-navy tnum">$20,000 to $50,000</p>
          <p class="mt-2 text-slate">A funeral plus something left over for a spouse or an adult child.</p>
        </div>
      </div>
    </div>

    <p class="reveal mt-5 text-sm text-muted max-w-3xl">
      Funeral costs vary widely by region and by what a family chooses. Ask a local funeral home
      for its current general price list before you settle on an amount. We can also walk through
      it with you on the phone.
    </p>
  </div>
</section>

<!-- =====================================================================
     3. WHAT IT COSTS BY AGE. Placeholder rate table with call CTAs.
     ================================================================== -->
<section id="costs" class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">What it costs by age</h2>
      <p class="reveal mt-5 text-slate">
        Age is the biggest factor in the price, and it moves against you every year. Health,
        tobacco use, your state, and the carrier decide the rest.
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
     4. NO MEDICAL EXAM.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">
      <div class="lg:col-span-6">
        <h2 class="reveal text-h2">No medical exam. Health questions instead.</h2>
        <p class="reveal mt-6 text-slate">
          Nobody comes to your house. There is no blood draw and no urine sample. The application
          asks a list of yes or no health questions, and an agent can go through them with you on
          the phone in a few minutes.
        </p>
        <p class="reveal mt-4 text-slate">
          The carrier does check two things electronically: your prescription history and a shared
          medical information database. So answer the questions honestly. An answer that does not
          match those records can delay your policy, or give the carrier grounds to refuse a claim
          later, which is the one outcome nobody wants.
        </p>
      </div>

      <div class="lg:col-span-5 lg:col-start-8">
        <div class="reveal card">
          <h3 class="text-h3 !font-display !font-semibold">The kind of thing you will be asked</h3>
          <ul class="mt-5 grid gap-4">
            <li class="flex items-start gap-3">{icon("circle-check", 24, "shrink-0 text-green mt-0.5")}<span>Have you used tobacco in the last twelve months?</span></li>
            <li class="flex items-start gap-3">{icon("circle-check", 24, "shrink-0 text-green mt-0.5")}<span>Are you in a nursing home or receiving hospice care?</span></li>
            <li class="flex items-start gap-3">{icon("circle-check", 24, "shrink-0 text-green mt-0.5")}<span>Have you been treated for cancer, heart failure, or kidney disease?</span></li>
            <li class="flex items-start gap-3">{icon("circle-check", 24, "shrink-0 text-green mt-0.5")}<span>Do you use oxygen equipment to help you breathe?</span></li>
          </ul>
          <p class="mt-6 text-sm text-muted">
            A yes does not automatically mean no. It usually means a different carrier or a
            different type of policy.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>

{call_band_1}

<!-- =====================================================================
     5. WAITING PERIODS. The section most competitors bury.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Waiting periods, said plainly</h2>
      <p class="reveal mt-5 text-slate">
        Some of these policies pay in full from the first day. Some do not. Which one you are
        offered depends on your health, and you should know which you are signing before you sign it.
      </p>
    </div>

    <div class="mt-10 grid md:grid-cols-3 gap-6">
      <div class="reveal card">
        <div class="flex items-center gap-3">
          {icon("circle-check", 26, "shrink-0 text-green")}
          <h3 class="text-h4">Level benefit</h3>
        </div>
        <p class="mt-4 text-slate">
          No waiting period. The full amount is payable from day one, whatever the cause.
        </p>
        <p class="mt-4 text-sm text-muted">
          Offered to applicants in reasonable health for their age. This is what we try for first.
        </p>
      </div>

      <div class="reveal card">
        <div class="flex items-center gap-3">
          {icon("hourglass", 26, "shrink-0 text-navy")}
          <h3 class="text-h4">Graded benefit</h3>
        </div>
        <p class="mt-4 text-slate">
          Pays a percentage of the benefit if you die of natural causes in the first two or three
          years, rising each year until the full amount applies.
        </p>
        <p class="mt-4 text-sm text-muted">
          Accidental death is normally covered in full from day one.
        </p>
      </div>

      <div class="reveal card">
        <div class="flex items-center gap-3">
          {icon("circle-alert", 26, "shrink-0 text-navy")}
          <h3 class="text-h4">Guaranteed issue</h3>
        </div>
        <p class="mt-4 text-slate">
          No health questions at all, and nobody is turned down. In exchange there is a two or three
          year waiting period, and the premium is the highest of the three.
        </p>
        <p class="mt-4 text-sm text-muted">
          If you die of natural causes during the wait, the carrier returns your premiums, usually
          with interest.
        </p>
      </div>
    </div>

    <p class="reveal mt-8 text-slate max-w-3xl">
      If an agent will not tell you plainly which of these three you are being sold, that is worth
      noticing. We tell you before the application goes in, in writing if you want it that way.
    </p>
  </div>
</section>

<!-- =====================================================================
     6. HOW IT DIFFERS FROM TERM AND WHOLE LIFE.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">How this differs from term and whole life</h2>
      <p class="reveal mt-5 text-slate">
        Final expense is a whole life policy. It is smaller, easier to qualify for, and priced for
        a different job.
      </p>
    </div>

    <div class="reveal mt-10 table-scroll table-signature">
      <!-- Three columns, one per product. Each fact is a group row above its
           three cells, so the table never needs a fourth column. -->
      <table class="compare-table" style="min-width:0">
        <caption class="sr-only">Final expense compared with term life and whole life insurance</caption>
        <thead>
          <tr>
            <th scope="col">Final expense</th>
            <th scope="col">Term life</th>
            <th scope="col">Whole life</th>
          </tr>
        </thead>
        <tbody>
          <tr><th scope="rowgroup" colspan="3">Typical coverage</th></tr>
          <tr><td class="tnum">$2,000 to $50,000</td><td class="tnum">$100,000 and up</td><td class="tnum">$25,000 and up</td></tr>
          <tr><th scope="rowgroup" colspan="3">Medical exam</th></tr>
          <tr><td>Never</td><td>Often</td><td>Usually</td></tr>
          <tr><th scope="rowgroup" colspan="3">Typical age</th></tr>
          <tr><td>50 to 85</td><td>30 to 55</td><td>40 to 65</td></tr>
          <tr><th scope="rowgroup" colspan="3">How long it lasts</th></tr>
          <tr><td>For life</td><td>10 to 30 years</td><td>For life</td></tr>
          <tr><th scope="rowgroup" colspan="3">What it is for</th></tr>
          <tr><td>A funeral and final bills</td><td>Replacing income</td><td>A lifelong need or an estate</td></tr>
          <tr><th scope="rowgroup" colspan="3">Time to get covered</th></tr>
          <tr><td>Often the same day</td><td>Three to six weeks</td><td>Three to six weeks</td></tr>
        </tbody>
      </table>
    </div>

    <p class="reveal mt-6 text-slate max-w-3xl">
      If you are under 60 and in good health and you want a larger amount, look at
      <a class="link" href="/term-life-insurance/">term life insurance</a> first. It buys far more
      coverage for the same money, and we will tell you so on the phone.
    </p>
  </div>
</section>

{call_band_2}

<!-- =====================================================================
     7. WHO QUALIFIES.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">Who qualifies</h2>
        <p class="reveal mt-6 text-slate">
          Almost everyone between 50 and 85 can get a final expense policy of some kind. Health
          decides the price and whether there is a waiting period, not usually whether you can be
          covered at all.
        </p>
        <p class="reveal mt-4 text-slate">
          Carriers rate the same condition very differently from each other. That is the whole
          practical argument for applying through an independent agency instead of to one company
          and taking its answer as final.
        </p>
      </div>

      <div class="lg:col-span-6 lg:col-start-7">
        <dl class="reveal grid gap-6">
          <div class="pb-6 border-b border-rule">
            <dt class="text-h4 text-navy">Usually accepted at level rates</dt>
            <dd class="mt-2 text-slate">Controlled high blood pressure, controlled type 2 diabetes, high cholesterol, arthritis, a cancer in remission beyond the carrier's look back period.</dd>
          </div>
          <div class="pb-6 border-b border-rule">
            <dt class="text-h4 text-navy">Often a graded benefit</dt>
            <dd class="mt-2 text-slate">COPD, a heart attack or stroke in the last two years, insulin started before age 50, chronic kidney disease.</dd>
          </div>
          <div>
            <dt class="text-h4 text-navy">Usually guaranteed issue</dt>
            <dd class="mt-2 text-slate">Currently in a nursing home, receiving hospice or dialysis, an active cancer diagnosis, oxygen use for a lung condition.</dd>
          </div>
        </dl>
        <p class="reveal mt-6 text-sm text-muted">
          These groupings are typical of the carriers we are appointed with. Each carrier has its
          own health questions and its own look back periods, so treat this as a guide and let us
          check your specific situation.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- 8. HOW TO APPLY. The homepage stepper, as a numbered checklist of the
     four things to have nearby. No CTA strip: call_band_3 is the next thing
     on the page and already carries the ask. -->
{how_to_apply}

{call_band_3}

{spokes}

<!-- =====================================================================
     10. FAQ.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">
      <div class="lg:col-span-4">
        <h2 class="reveal text-h2">Questions people ask us</h2>
        <p class="reveal mt-5 text-slate">
          If yours is not here, ask it on the phone. There is no script.
        </p>
        <div class="reveal mt-6">
          {call_faq}
        </div>
      </div>
      <div class="lg:col-span-7 lg:col-start-6 reveal">
        {faq_html}
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     11. BYLINE. Spec section 09.5.
     ================================================================== -->
<section class="section-tight band">
  <div class="container-ax">
    <div class="reveal">
      {byline}
    </div>
  </div>
</section>

<!-- =====================================================================
     12. FINAL: phone CTA and the short form, side by side.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-2 gap-10 lg:gap-16 items-start">

      <div class="reveal">
        <h2 class="text-h2">Talk it through</h2>
        <p class="mt-5 text-slate">
          Fifteen minutes on the phone will tell you what you qualify for, what it costs, and
          whether there is a waiting period. No obligation to buy at the end of it.
        </p>
        <div class="mt-8">
          {C.phone_link("fe_final_primary", "btn btn-call btn-xl btn-block", "Call " + C.PHONE_DISPLAY, 28)}
        </div>
        <p class="mt-4 text-slate">{C.HOURS}</p>
        <p class="mt-6 text-sm text-muted">
          You will reach a licensed agent, not a call centre queue and not a lead form that gets
          sold on to six other agencies.
        </p>

        <div class="mt-8 pt-8 border-t border-rule">
          <h3 class="text-h4">What you will know by the end of the call</h3>
          <ul class="mt-4 grid gap-3">
            <li class="flex items-start gap-3">{icon("circle-check", 24, "shrink-0 text-green mt-0.5")}<span>Which carriers will accept you, and which will not.</span></li>
            <li class="flex items-start gap-3">{icon("circle-check", 24, "shrink-0 text-green mt-0.5")}<span>What the premium is, and that it will never rise.</span></li>
            <li class="flex items-start gap-3">{icon("circle-check", 24, "shrink-0 text-green mt-0.5")}<span>Whether your policy would have a waiting period, and how long.</span></li>
          </ul>
        </div>

        {hands_media}
      </div>

      <div class="reveal">
        <div class="panel">
          {callback_form("fe_footer", "fe_footer_callback", heading="Or leave your number", intro="Four details. We call you back.")}
        </div>
      </div>
    </div>
  </div>
</section>
"""


# --- The four field callback form ------------------------------------------
# Extracted for the final expense SPOKES, which are phone first with a short
# form as the secondary ask and would otherwise each hand-copy this block.
# The hub uses it too, twice: its two inline copies were folded in during the
# September 2026 forms pass, when every form changed shape anyway.
def callback_form(prefix, form_name, heading="Prefer we call you?",
                  intro="Leave four details and a licensed agent will call you back.",
                  silo="final-expense", senior=True):
    """Four fields in two rows, one step, no scrolling inside the form.

    `prefix` must be unique per page, not per site: it namespaces every id in
    the block, including the TCPA consent checkbox and the success panel.

    `silo` and `senior` exist for the one caller outside this silo, the free
    policy review page, which takes any adult age rather than 50 to 85.
    """
    fields = (
        F.row(F.text_field(prefix + "-name", "name", "Your name", autocomplete="name",
                           validate="name", error="Please tell us your name."),
              F.age_field(prefix + "-age", senior=senior))
        + F.row(F.select_field(prefix + "-state", "state", "Your state",
                               '<option value="">Choose your state</option>\n' + C.state_options(),
                               error="Please choose your state."),
                F.phone_field(prefix + "-phone", label="Your phone number")))
    return f"""
          <h2 class="text-h3 !font-display !font-semibold">{heading}</h2>
          <p class="mt-3 text-slate">{intro}</p>

          <form class="mt-6" data-ax-form data-silo="{silo}"
                data-form-name="{form_name}" data-success-target="{prefix}-success" novalidate>

            {F.scaffold(indent=12)}

            {fields}

            {F.consent_block(prefix, C.BRAND, 12)}

            {F.submit_block("Request a call back")}

          </form>

          <div id="{prefix}-success" class="success">
            <div class="flex items-start gap-3">
              {icon("circle-check", 32, "shrink-0 text-green")}
              <div>
                <h3 class="text-h3 !font-display !font-semibold">We have your details</h3>
                <p class="mt-3 text-slate">
                  A licensed agent will call you within {C.SLA}. If you would rather not wait,
                  call us now and we can do it in one go.
                </p>
                <div class="mt-5">
                  {C.phone_link(prefix + "_success", "btn btn-call btn-block",
                                "Call " + C.PHONE_DISPLAY, 22)}
                </div>
              </div>
            </div>
          </div>"""
