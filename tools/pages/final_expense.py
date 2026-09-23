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
TITLE = "Final Expense Insurance: Cover a Funeral, No Medical Exam | Apex"
OG_TITLE = "Final expense insurance, explained by a licensed agent"
DESC = ("Final expense insurance covers funeral and burial costs for ages 50 to 85. No medical "
        "exam, health questions only. Talk to a licensed independent agent.")

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
     "No. A pre-need contract is money paid to one funeral home for a "
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
     "What cremation costs and how much coverage fits."),
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
                        + '<a class="btn btn-ghost btn-block mt-3" href="#fe-quote">'
                          'Get coverage now</a>'
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
    return C.acc(q, a, "fe-faq")


# --- Rate table -----------------------------------------------------------
AGE_BANDS = ["50 to 54", "55 to 59", "60 to 64", "65 to 69", "70 to 74", "75 to 79", "80 to 85"]
# The three benefit types. Facts are the ones this page already states; the
# premium order is the one "highest of the three" implies.
WAITING = [
    ("level", "Best case", "circle-check", "Level benefit",
     "The full amount is payable from day one, whatever the cause.",
     "None", "Yes", "The full amount", "Lowest of the three",
     "Offered to applicants in reasonable health for their age. This is what we try for first."),
    ("graded", "Middle", "hourglass", "Graded benefit",
     "A percentage of the benefit at first, rising each year until the full amount applies.",
     "Two or three years", "Yes", "A percentage, rising each year", "In between",
     "Accidental death is normally covered in full from day one."),
    ("gi", "Last resort", "circle-alert", "Guaranteed issue",
     "Nobody is turned down. In exchange there is a wait before the full benefit applies.",
     "Two or three years", "None", "Your premiums back, usually with interest", "Highest of the three",
     "For when health rules out the other two."),
]

# Who gets which benefit type. Tones and icons match WAITING, row for row.
QUALIFY = [
    ("level", "Most people", "circle-check", "Usually accepted at level rates",
     "Full benefit from day one, no waiting period.",
     "Level benefit", "None",
     "Controlled high blood pressure, controlled type 2 diabetes, high cholesterol, arthritis, "
     "a cancer in remission beyond the carrier's look back period."),
    ("graded", "Some people", "hourglass", "Often a graded benefit",
     "A percentage in the first two or three years, then the full amount.",
     "Graded benefit", "Two or three years",
     "COPD, a heart attack or stroke in the last two years, insulin started before age 50, "
     "chronic kidney disease."),
    ("gi", "Nobody turned down", "circle-alert", "Usually guaranteed issue",
     "No health questions. A two or three year waiting period applies.",
     "Guaranteed issue", "Two or three years",
     "Currently in a nursing home, receiving hospice or dialysis, an active cancer diagnosis, "
     "oxygen use for a lung condition."),
]

# The coverage bands. key doubles as the value "Quote this amount" writes into
# the quote form's hidden coverage field.
TIERS = [
    ("2000-8000", "$2,000 to $8,000",
     "A cremation, a simple service, and the last few bills. Enough that nobody has to reach "
     "for a credit card at the funeral home."),
    ("8000-20000", "$8,000 to $20,000",
     "A traditional burial with a service, and room for what comes after it: the headstone, "
     "the outstanding medical bills, the catering nobody planned for."),
    ("20000-50000", "$20,000 to $50,000",
     "The funeral, and something left for whoever is still here. Often a spouse whose household "
     "income drops in the same week."),
]

# Three columns at most on this page (senior readability). The full coverage
# range is described in the scale above the table.
COVERAGE_COLS = ["$10,000", "$25,000"]


def rate_table():
    """The shared rate table (chrome.rate_chart), phone weighted: each row's
    "Quote this" is a call."""
    return C.rate_chart(
        "fe-rates", COVERAGE_COLS, [(band, None) for band in AGE_BANDS],
        [("Show premiums for", "fe-rate-sex", [("female", "Female"), ("male", "Male")], None)],
        "Monthly premium by age band and coverage amount.",
        row_cta="call", cta_location="rate_table",
        aside="Non tobacco, level benefit. Tobacco rates are higher.",
        note="Source: [CARRIER RATE CARD NAME AND EDITION]. Premiums vary by carrier, state, "
             "health, and tobacco use, and are not an offer of coverage.")


def body():
    # No parallax and no wipe: this page is exempt from transform-based motion.
    # One h1, one line, one button, and the button is the phone. No glow: fe.
    hero = C.page_hero(
        [("Home", "/"), ("Final Expense Insurance", None)],
        "Final expense insurance. Paid for by you, not by them.",
        "A small whole life policy for your funeral and the bills that follow it, paid now so "
        "nobody has to find the money the week after.",
        extra='''<div class="reveal mt-8 grid gap-3 max-w-md">
        %s
        <a href="#fe-quote" class="btn btn-cta btn-xl btn-block">Get coverage now</a>
        <p class="mt-3 text-slate">%s</p>
      </div>''' % (C.phone_link("fe_hero_primary", "btn btn-call btn-xl", "Call " + C.PHONE_DISPLAY, 28), C.HOURS),
        banner="fe-hero")
    usps = C.usp_strip([
        ("users", "Ages 50 to 85", "Accepted"),
        ("stethoscope", "No medical exam", "Health questions only"),
        ("shield-check", "Premium locked for life", "It never goes up"),
        ("banknote", "$2,000 to $50,000", "Sized for a funeral, not an income"),
    ])
    # Team rewrite, September 2026: the reason to buy, in the reader's words,
    # beside the quote form (the team's layout). It is #fe-quote: the hero's
    # "Get coverage now" and the comparison's "get a quote online" land here.
    form_after = f"""<p class="mt-2 text-sm text-muted">No payment details, and nothing is taken unless you are approved and say yes.</p>
            <p class="mt-5 pt-5 border-t border-rule text-sm text-slate">Rather just talk to someone?
              {C.phone_link("fe_form_call", "link font-semibold inline-flex items-center gap-1 whitespace-nowrap", size=16)}</p>"""
    hero_form = quote_form(
        "fe_hero", "fe_hero_quote", "Get your quote",
        "Five questions. A licensed agent calls you back with real numbers.",
        form_id="fe-quote-form", after=form_after)
    wait_cards = "".join(f"""
      <li class="reveal card wp-card wp-{tone} flex flex-col">
        <span class="wp-rank">{rank}</span>
        <div class="mt-4 flex items-center gap-3">
          {icon(ico, 26, "shrink-0 wp-icon")}
          <h3 class="text-h4">{name}</h3>
        </div>
        <p class="mt-3 text-slate">{summary}</p>
        <dl class="wp-facts">
          <div><dt>Waiting period</dt><dd>{wait}</dd></div>
          <div><dt>Health questions</dt><dd>{questions}</dd></div>
          <div><dt>If you die of natural causes early</dt><dd>{early}</dd></div>
          <div><dt>Premium</dt><dd>{premium}</dd></div>
        </dl>
        <p class="mt-auto pt-5 text-sm text-muted">{who}</p>
      </li>""" for tone, rank, ico, name, summary, wait, questions, early, premium, who in WAITING)
    qualify_cards = "".join(f"""
      <li class="reveal card wp-card wp-{tone} flex flex-col">
        <span class="wp-rank">{rank}</span>
        <div class="mt-4 flex items-center gap-3">
          {icon(ico, 26, "shrink-0 wp-icon")}
          <h3 class="text-h4">{title}</h3>
        </div>
        <p class="mt-3 text-slate">{means}</p>
        <dl class="wp-facts">
          <div><dt>Usual result</dt><dd>{result}</dd></div>
          <div><dt>Waiting period</dt><dd>{wait}</dd></div>
        </dl>
        <details class="status-more mt-auto pt-3">
          <summary>Example conditions{icon("chevron-down", 20, "status-chev")}</summary>
          <p class="mt-2 text-sm text-slate">{conditions}</p>
        </details>
      </li>""" for tone, rank, ico, title, means, result, wait, conditions in QUALIFY)
    tier_cards = "".join(f"""
      <li class="reveal card flex flex-col">
        <h3 class="text-h4 tnum">{label}</h3>
        <p class="mt-3 text-slate">{desc}</p>
        <div class="mt-auto pt-6">
          <button type="button" class="btn btn-ghost btn-block"
                  data-prefill='{{"coverage":"{key}"}}' data-prefill-target="fe-quote-form"
                  data-prefill-trigger="coverage_band">Quote this amount</button>
        </div>
      </li>""" for key, label, desc in TIERS)
    week_after = f"""<section id="fe-quote" class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">

      <div class="lg:col-span-6">
        <h2 class="reveal text-h2">So the week after is about you, not about money</h2>
        <p class="reveal mt-6 text-lead text-slate">
          A funeral has to be paid for before it happens. Someone chooses the casket or the urn,
          the service, the plot. Someone is handed the total and asked how they would like to
          settle it.
        </p>
        <p class="reveal mt-5 text-slate">
          If there is no policy, that someone is your partner, your son, or your sister, three
          days after losing you.
        </p>
        <p class="reveal mt-5 text-slate">
          A final expense policy moves that decision to today, while you are still the one making
          it. You choose the amount. You pay a fixed premium. When the time comes the money goes to
          the person you name, in cash, and they decide what it covers: the funeral, the last
          medical bills, the flight for a grandchild who lives too far away.
        </p>
        <p class="reveal mt-5 text-slate">
          It is a small policy. What it does is keep that week about you, instead of about money.
        </p>

        <div class="reveal mt-8 card">
          <p class="font-semibold text-navy">Worth knowing before you sign</p>
          <p class="mt-2 text-slate">
            Not every final expense policy pays in full from the first day. Some carry a waiting
            period of two or three years. Which one you are offered depends on your health, and
            you should know which you are signing before you sign it.
          </p>
          <a class="link-static mt-3 inline-block text-sm" href="#waiting-periods">How the three policy types differ</a>
        </div>

        <div class="reveal mt-8 flex flex-wrap gap-3">
          {C.phone_link("fe_story_call", "btn btn-call", "Call " + C.PHONE_DISPLAY, 22)}
          <a href="#how-to-apply" class="btn btn-ghost">See what the call involves</a>
        </div>
        <p class="reveal mt-3 text-sm text-muted">{C.HOURS}</p>
      </div>

      <!-- The form rides beside the story on desktop: the story is the longer
           column. Six columns, not five, so the panel clears the 26rem
           container query and date of birth pairs with state, as in the
           team's layout. -->
      <div class="lg:col-span-6 lg:col-start-7">
        <div class="sticky-col">
          <div class="panel reveal">
            {hero_form}
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""
    call_band_1 = call_band(
        "Would you rather just ask someone?",
        "A licensed agent can answer the health questions with you and tell you what you qualify for.",
        "fe_repeat_1")
    call_band_2 = call_band(
        "Not sure which type of policy you need?",
        "Tell us your age and what you want to cover. We will tell you which one fits.",
        "fe_repeat_2", photo="fe-band")
    # Sits directly under "How to apply. One call, about fifteen minutes." Its
    # copy deliberately does not restate that heading: the section above has
    # already covered the how, so this band only removes the last reason to
    # put the call off.
    call_band_3 = call_band(
        "You do not need anything ready to start",
        "Nothing to print, nothing to mail, no exam to schedule. If one of the four things above is "
        "missing, call anyway and we will work around it.",
        "fe_repeat_3")
    spokes = C.spoke_module(
        "Final expense insurance guides",
        "Nine short articles on the questions people ask most often about this coverage.",
        SPOKES)
    call_faq = C.phone_link("fe_faq", "btn btn-call", "Call " + C.PHONE_DISPLAY, 22)
    byline = C.byline_section("section")
    faq_html = "\n        ".join(_acc(q, a) for q, a in FAQ)

    how_to_apply = C.steps_section(
        "How to apply. One call, about fifteen minutes.",
        "There is no paperwork to mail and nothing to print. Have these four things nearby and the "
        "call goes quickly.",
        [("file-text", None, "Your date of birth and address",
          "Exactly as they appear on your driver's license or state ID."),
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
        cls="section band", label="Item")

    return f"""
{hero}
{usps}

{week_after}

<!-- "Speak to a licensed agent" was removed here (September 2026): its call
     button, form and three steps all repeat elsewhere on the page. -->

<!-- =====================================================================
     2. COVERAGE AMOUNTS as a simple visual scale.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">How much coverage people usually buy</h2>
      <p class="reveal mt-5 text-slate">
        Pick the amount by what the week will actually cost, not by what sounds like a round
        number. Most people land in the middle, because this is covering a funeral, not replacing
        an income.
      </p>
    </div>

    <!-- The scale: where most policies land, before the three bands. -->
    <div class="reveal mt-10 max-w-3xl">
      <div class="flex items-baseline justify-between text-sm font-semibold text-navy tnum">
        <span>$2,000</span>
        <span>$50,000</span>
      </div>
      <div class="mt-3 h-3 w-full bg-navy-050 border border-rule rounded-full overflow-hidden">
        <div class="h-full bg-navy-700 rounded-full" style="margin-left:12%;width:34%"></div>
      </div>
      <p class="mt-3 text-sm text-navy font-semibold">
        The shaded band is roughly $8,000 to $20,000, where most policies we place land.
      </p>
    </div>

    <!-- Three bands, one card each. "Quote this amount" sets the quote form's
         coverage select and scrolls there, so the agent calls already knowing
         the figure. -->
    <ul class="mt-8 grid md:grid-cols-3 gap-6" data-stagger="40">{tier_cards}
    </ul>

    <div class="reveal mt-6 max-w-3xl">
      <p class="text-sm font-semibold text-navy">Before you settle on a figure</p>
      <p class="mt-2 text-sm text-slate">
        Ask a local funeral home for its general price list. Under the FTC's Funeral Rule, if you
        ask in person they have to give you an itemized list to keep, and you do not have to be
        buying anything. That list is a better guide than any national average. We are happy to
        walk through it with you on the phone.
      </p>
    </div>
  </div>
</section>

<!-- =====================================================================
     3. WHAT IT COSTS BY AGE. Placeholder rate table with call CTAs.
     ================================================================== -->
<section id="costs" class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Final expense insurance cost by age</h2>
      <p class="reveal mt-5 text-slate">
        Age is the biggest factor in the price. The older you are when you apply, the more it
        costs. Health, tobacco use, your state, and the carrier decide the rest.
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
          asks a list of yes or no health questions. An agent can go through them with you on
          the phone in a few minutes.
        </p>
        <p class="reveal mt-4 text-slate">
          The carrier does check two things electronically: your prescription history and a shared
          medical information database. So answer the questions honestly. An answer that does not
          match those records can delay your policy, or give the carrier grounds to refuse a claim
          later, which is exactly the outcome this policy exists to prevent.
        </p>
      </div>

      <div class="lg:col-span-5 lg:col-start-8">
        <div class="reveal card">
          <h3 class="text-h3 !font-display !font-semibold">Health questions you may be asked</h3>
          <ul class="mt-5 grid gap-4">
            <li class="flex items-start gap-3">{icon("circle-check", 24, "shrink-0 text-green mt-0.5")}<span>Have you used tobacco in the last twelve months?</span></li>
            <li class="flex items-start gap-3">{icon("circle-check", 24, "shrink-0 text-green mt-0.5")}<span>Are you in a nursing home or receiving hospice care?</span></li>
            <li class="flex items-start gap-3">{icon("circle-check", 24, "shrink-0 text-green mt-0.5")}<span>Have you been treated for cancer, heart failure, or kidney disease?</span></li>
            <li class="flex items-start gap-3">{icon("circle-check", 24, "shrink-0 text-green mt-0.5")}<span>Do you use oxygen equipment to help you breathe?</span></li>
          </ul>
          <p class="mt-6 text-sm text-muted">
            Answering yes does not automatically mean you are turned down. It usually means a
            different carrier or a different type of policy.
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
<div id="waiting-periods" class="sr-only" aria-hidden="true"></div>
<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Waiting periods explained</h2>
      <p class="reveal mt-5 text-slate">
        Some of these policies pay in full from the first day. Some do not. Which one you are
        offered depends on your health, and you should know which you are signing before you sign it.
      </p>
    </div>

    <!-- Scannable: every card carries the same four facts in the same order,
         so the three read across as a comparison. Rank and top rule say
         which is which before a word is read. -->
    <ul class="mt-10 grid md:grid-cols-3 gap-6" data-stagger="40">{wait_cards}
    </ul>

    <p class="reveal mt-8 text-slate max-w-3xl">
      An agent should tell you plainly which of these three you are being sold. We tell you before
      the application goes in, in writing if you want it.
    </p>
  </div>
</section>

<!-- =====================================================================
     6. HOW IT DIFFERS FROM TERM AND WHOLE LIFE.
     ================================================================== -->
{C.product_compare(
    "fe", "How this differs from term and whole life",
    "Final expense is a whole life policy. It is smaller, easier to qualify for, and priced for "
    "a different job.",
    C.phone_link("fe_compare", "btn btn-call btn-block whitespace-nowrap", "Call " + C.PHONE_DISPLAY, 20),
    'Licensed agent, no hold queue &#183; <a class="link" href="#fe-quote">or get a quote online</a>',
    after="""
    <p class="reveal mt-6 text-slate max-w-3xl">
      If you are under 60 and in good health and you want a larger amount, look at term life
      insurance first. It buys far more coverage for the same money, and we will tell you so on
      the phone.
    </p>""")}

{call_band_2}

<!-- =====================================================================
     7. WHO QUALIFIES.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Who qualifies for final expense insurance</h2>
      <p class="reveal mt-5 text-slate">
        Almost everyone between 50 and 85 can get a final expense policy of some kind. Health
        decides the price and whether there is a waiting period, not usually whether you can be
        covered at all.
      </p>
    </div>

    <!-- Same three tones, ranks and fact rows as the waiting-period cards
         above, so "which group am I in" and "what that means" read as one
         system. The example conditions stay folded (native <details>): on a
         phone, three open lists were most of this section's height. -->
    <ul class="mt-10 grid md:grid-cols-3 gap-6" data-stagger="40">{qualify_cards}
    </ul>

    <p class="reveal mt-8 text-slate max-w-3xl">
      Carriers rate the same condition very differently from each other. That is the practical
      argument for applying through an independent agency instead of to one company and taking
      its answer as final. These groupings are typical of the carriers we are appointed with, so
      treat them as a guide and let us check your specific situation.
    </p>
  </div>
</section>

<!-- 8. HOW TO APPLY. The homepage stepper, as a numbered checklist of the
     four things to have nearby. No CTA strip: call_band_3 is the next thing
     on the page and already carries the ask. -->
<div id="how-to-apply" class="sr-only" aria-hidden="true"></div>
{how_to_apply}

{call_band_3}


<!-- =====================================================================
     10. FAQ.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">
      <div class="lg:col-span-4">
        <h2 class="reveal text-h2">Common questions about final expense insurance</h2>
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

<!-- Guides, laid out as blog posts. After the FAQ by client request. -->
{spokes}

<!-- =====================================================================
     11. BYLINE. Spec section 09.5.
     ================================================================== -->
{byline}

<!-- =====================================================================
     12. FINAL: phone CTA and the short form, side by side.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-2 gap-10 lg:gap-16 items-center">

      <div class="reveal">
        <h2 class="text-h2">Fifteen minutes now spares them later</h2>
        <p class="mt-5 text-lead text-slate">
          One unhurried call, and you will know where you stand. What you qualify for, what it
          costs, and whether there is a waiting period.
        </p>
        <p class="mt-4 text-slate">
          No obligation, and nothing is taken unless you say yes. If final expense is not right
          for you, we will say so.
        </p>

        <div class="mt-8">
          {C.phone_link("fe_final_primary", "btn btn-call btn-xl btn-block sm:!w-auto", "Call " + C.PHONE_DISPLAY, 28)}
          <p class="mt-3 text-sm text-muted">{C.HOURS}</p>
        </div>

        <!-- The four answers the call gives, as short scannable points. -->
        <div class="mt-10 rounded-[12px] bg-navy-050 p-6">
          <h3 class="text-h4">By the end of the call, you will know</h3>
          <ul class="mt-5 grid sm:grid-cols-2 gap-x-6 gap-y-4">
            <li class="flex items-start gap-3">{icon("circle-check", 22, "shrink-0 text-green mt-0.5")}<span>Which carriers will accept you</span></li>
            <li class="flex items-start gap-3">{icon("circle-check", 22, "shrink-0 text-green mt-0.5")}<span>Your premium, locked for life</span></li>
            <li class="flex items-start gap-3">{icon("circle-check", 22, "shrink-0 text-green mt-0.5")}<span>Whether there is a waiting period</span></li>
            <li class="flex items-start gap-3">{icon("circle-check", 22, "shrink-0 text-green mt-0.5")}<span>Who receives the money, and how</span></li>
          </ul>
        </div>
      </div>

      <div class="reveal">
        <div class="panel">
          {quote_form("fe_footer", "fe_footer_quote", "Or leave your number",
                      "Five questions. A licensed agent calls you back with real numbers.")}
        </div>
      </div>
    </div>
  </div>
</section>
"""


# --- The hub's quote form: the team's five questions ------------------------
COVERAGE_OPTIONS = ([("unsure", "Not sure yet, help me decide")]
                    + [(key, label) for key, label, _ in TIERS])


def quote_form(prefix, form_name, heading, intro, form_id="", after=""):
    """The team's five-question form (September 2026), in both of the hub's
    placements so the two cannot drift. The coverage values are TIERS keys:
    the coverage cards' "Quote this amount" buttons prefill this select."""
    fields = (
        F.row(F.text_field(prefix + "-dob", "dob", "Date of birth", type="date",
                           autocomplete="bday", validate="dobSenior",
                           error="Enter your date of birth. Final expense is for ages 50 to 85."),
              F.select_field(prefix + "-state", "state", "Your state",
                             '<option value="">Choose your state</option>\n' + C.state_options(),
                             error="Please choose your state."))
        + F.select_field(prefix + "-coverage", "coverage", "Coverage you have in mind",
                         COVERAGE_OPTIONS)
        + F.radio_group(prefix + "-tob", "tobacco", "Tobacco in the last twelve months?",
                        [("no", "No"), ("yes", "Yes")], error="Let us know either way.")
        + F.phone_field(prefix + "-phone", label="Your phone number"))
    return callback_form(prefix, form_name, heading=heading, intro=intro, form_id=form_id,
                         submit="Get my quote", fields=fields, after=after)


# --- The three field callback form -----------------------------------------
# Extracted for the final expense SPOKES, which are phone first with a short
# form as the secondary ask and would otherwise each hand-copy this block.
# The hub uses it too, twice: its two inline copies were folded in during the
# September 2026 forms pass, when every form changed shape anyway.
def callback_form(prefix, form_name, heading="Prefer we call you?",
                  intro="Leave three details and a licensed agent will call you back.",
                  silo="final-expense", senior=True, submit="Request a call back", after="",
                  form_id="", fields=None):
    """Three fields, one step, no scrolling inside the form. The name went in
    the September 2026 shortening pass: the agent asks for it in the first five
    seconds of the call, so it was a field the form did not need to carry.

    `prefix` must be unique per page, not per site: it namespaces every id in
    the block, including the TCPA consent checkbox and the success panel.

    `silo` and `senior` exist for the one caller outside this silo, the free
    policy review page, which takes any adult age rather than 50 to 85.
    """
    fields = fields or (
        F.row(F.age_field(prefix + "-age", senior=senior),
              F.select_field(prefix + "-state", "state", "Your state",
                             '<option value="">Choose your state</option>\n' + C.state_options(),
                             error="Please choose your state."))
        + F.phone_field(prefix + "-phone", label="Your phone number"))
    return f"""
          <h2 class="text-h3 !font-display !font-semibold">{heading}</h2>
          <p class="mt-3 text-slate">{intro}</p>

          <form{f' id="{form_id}"' if form_id else ""} class="mt-6" data-ax-form data-silo="{silo}"
                data-form-name="{form_name}" data-success-target="{prefix}-success" novalidate>

            {F.scaffold(indent=12)}

            {fields}

            {F.consent_block(prefix, C.BRAND, 12)}

            {F.submit_block(submit)}
            {after}

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
