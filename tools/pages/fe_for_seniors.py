# -*- coding: utf-8 -*-
"""FINAL EXPENSE FOR SENIORS. Spec P2, template T4. PHONE FIRST.

Senior accessibility rules from the hub apply in full: html.fe, so 18px body
and Inter throughout on main; no glow, no stagger, no count-up, no lift;
tables capped at three columns; 56px tap targets; large phone CTAs repeated
after every second section.

The page absorbs the over-70 and over-80 variants as H2 sections rather than
spawning two thin pages that would compete with this one and with each other.
Each of those sections answers the question the query is really asking, which
is not "am I too old" but "what changes for me".

No banner band: MASTER.md s8 puts one of those on each product HUB, not on the
spokes. The conversion re-asks here are flat navy call bands.
"""
import chrome as C
import final_expense as FE

PATH = "/final-expense-insurance/for-seniors/"
OUT = "final-expense-insurance/for-seniors/index.html"
ACTIVE = "/final-expense-insurance/"
SILO = "final-expense"
HTML_CLASS = "fe"
TITLE = "Final Expense Insurance for Seniors, Ages 50 to 85 | Apex"
OG_TITLE = "Final expense insurance for seniors"
DESC = ("Final expense insurance for ages 50 to 85. What changes at 70 and at 80, what the health "
        "questions decide, and how to find out what you qualify for in about fifteen minutes.")

TRAIL = [("Home", "/"), ("Final Expense Insurance", "/final-expense-insurance/"),
         ("For seniors", None)]

FAQ = [
    ("What is the best age to buy final expense insurance?",
     "The best age is the youngest age at which you are certain you want it, because the premium "
     "is set from your age when the policy is issued and never rises after that. Someone who buys "
     "at sixty two pays a lower premium for the rest of their life than the same person buying at "
     "seventy. There is no benefit to waiting and there is a real risk in it, because health "
     "changes can move you from a full benefit policy to a graded one."),
    ("Can I get final expense insurance at 80?",
     "Yes. Most of our appointed carriers write to eighty five, and a few go higher. What narrows "
     "at eighty is the range of face amounts and the number of carriers who will pay the full "
     "benefit from day one rather than after a waiting period. Both of those depend on your health "
     "answers rather than your age alone, which is why it is worth a call rather than an "
     "assumption."),
    ("Is there a medical exam?",
     "No. Final expense is health questions only, usually between five and fifteen of them, "
     "answered on a call. The carrier also checks your prescription history. There is no blood "
     "work, no urine sample, and nobody comes to your home."),
    ("How much coverage do most people buy?",
     "Enough to cover a funeral or cremation and the bills that arrive in the weeks afterwards. "
     "The right amount is the one your family would actually face, and it varies enormously by "
     "state and by what you want. We will walk through the parts of that cost with you rather "
     "than quote you a figure from a national average that may not resemble your area."),
    ("Will my premium or my coverage change as I get older?",
     "No. This is whole life insurance, so the premium is fixed for life and the coverage does not "
     "reduce or expire as long as the premium is paid. If anyone offers you a policy where the "
     "premium rises with age or the benefit falls after a certain birthday, that is a different "
     "product and you should have us look at it before you sign."),
]


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def band(heading, intro, points, cls="section"):
    """One age band section. Large type, short lines, no motion beyond reveal."""
    items = "".join('<li class="reveal">%s</li>' % p for p in points)
    return f"""<section class="{cls}">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">{heading}</h2>
        <p class="reveal mt-5 text-slate">{intro}</p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <ul class="grid gap-5 text-slate">{items}</ul>
      </div>
    </div>
  </div>
</section>"""


def body():
    hero_cta = """<div class="reveal mt-8">
        %s
        <p class="mt-3 text-sm text-muted">%s</p>
      </div>""" % (C.phone_link("fe_seniors_hero", "btn btn-call btn-xl", "Call " + C.PHONE_DISPLAY, 26),
                   C.HOURS)

    return f"""
{C.page_hero(
    TRAIL,
    "Final Expense Insurance for Seniors",
    'Final expense insurance is a small whole life policy, written from age fifty to eighty five, '
    'bought to cover a funeral and the bills that follow. There is no medical exam. The premium '
    'never rises and the coverage never expires. This page explains what changes between fifty and '
    'eighty five, because it is not your age that decides what you can buy, it is your health '
    'answers. Everything on this page is <a class="link" '
    'href="/final-expense-insurance/">final expense insurance</a>.',
    extra=hero_cta, glow=False)}


<!-- =====================================================================
     WHAT YOU GET. Three cells, plain language, no motion beyond reveal.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">What you are actually buying</h2>
    </div>

    <div class="mt-10 bento">
      <div class="reveal bento-cell bento-cell-blue bento-2">
        <h3 class="text-h4 text-white">A fixed premium</h3>
        <p class="mt-3 text-white/90">
          Set from your age and health answers when the policy is issued. It never rises, at any
          age, for as long as you pay it.
        </p>
      </div>
      <div class="reveal bento-cell bento-2">
        <h3 class="text-h4">Coverage that does not expire</h3>
        <p class="mt-3 text-slate">
          There is no term to outlive. The policy is in force until you die, as long as the
          premium has been paid.
        </p>
      </div>
      <div class="reveal bento-cell bento-cell-tint bento-2">
        <h3 class="text-h4">Money your family can use</h3>
        <p class="mt-3 text-slate">
          Paid to the person you name, usually within days of the claim. They decide how it is
          spent. It is not held by a funeral home.
        </p>
      </div>
    </div>
  </div>
</section>


{band("If you are 50 to 69",
      "This is the easiest band to buy in, and the one where waiting costs the most.",
      ["Most applicants qualify for a full benefit policy, which means the whole amount is payable "
       "from the first day rather than after a waiting period.",
       "Health conditions that are being treated and are stable are commonly accepted here, "
       "including high blood pressure, controlled diabetes, and high cholesterol.",
       "The premium you lock in now is the premium you pay at eighty. Buying nine years early "
       "means paying a fifty nine year old's rate for the rest of your life.",
       "If you still have a mortgage or people depending on your income, look at term life "
       "insurance for that part first. This product is for the funeral, not the income."],
      cls="section")}


{band("If you are 70 to 79",
      "Still straightforward for most people. What changes is that the health questions start "
      "doing more of the work, and the differences between carriers get wider.",
      ["Full benefit policies remain widely available. Whether you qualify depends on your "
       "answers and your prescriptions, not on your age.",
       "A recent hospital stay, a new diagnosis, or a change of medication in the last twelve "
       "months is the sort of thing that moves an application from one carrier to another. It is "
       "usually not a decline, it is a different carrier.",
       "Face amounts start to narrow at the top end. For most people in this band that is not a "
       "constraint, because the amount needed for a funeral has not changed.",
       "This is the band where being appointed with several carriers stops being a nicety. The "
       "same set of answers can produce very different outcomes at two companies."],
      cls="section band-surface")}


{FE.call_band(
    "Find out what you qualify for in about fifteen minutes",
    "A licensed agent will ask the health questions over the phone and tell you which carriers "
    "will write you and whether there is a waiting period. There is no application and no "
    "obligation.",
    "fe_seniors_band_1")}


{band("If you are 80 to 85",
      "Coverage is still available, and this is the band where the honest answers matter most.",
      ["Most carriers write to eighty five. Some stop at eighty, and a small number go beyond "
       "eighty five. Which of those applies to you depends on your state as well as your age.",
       "Waiting periods become more common. A graded or modified policy pays a return of your "
       "premiums plus interest if you die from illness in the first two years, and pays the full "
       "amount for an accident from day one.",
       "A waiting period is not a reason to give up. It is a reason to check whether a full "
       "benefit carrier will still take you, which is a fifteen minute conversation rather than a "
       "guess.",
       "Face amounts are smaller in this band. For a funeral and final bills that is usually "
       "sufficient, and we would rather tell you the real ceiling than let you find it during an "
       "application."],
      cls="section")}


<!-- =====================================================================
     WHAT THE HEALTH QUESTIONS DECIDE. The section that reframes the
     page: age is not the variable people think it is.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2">Your answers matter more than your age</h2>
      <p class="reveal mt-5 text-slate">
        Every carrier asks a short list of health questions. The answers put you into one of three
        outcomes. Age moves the premium; the questions decide which outcome you are in.
      </p>
    </div>

    <div class="reveal mt-10 table-scroll table-signature">
      <table class="rate-table" style="min-width:0">
        <caption>The three outcomes, and what each one pays.</caption>
        <thead>
          <tr>
            <th scope="col">Outcome</th>
            <th scope="col">What it pays</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">Level benefit</th>
            <td>The full amount from day one. The most common outcome, at every age in this range.</td>
          </tr>
          <tr>
            <th scope="row">Graded or modified</th>
            <td>A reduced amount, or your premiums back with interest, if death is from illness in
                the first two years. Full amount for an accident from day one.</td>
          </tr>
          <tr>
            <th scope="row">Guaranteed acceptance</th>
            <td>No health questions at all. A two year waiting period is standard, and the cost per
                thousand is the highest of any policy.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p class="reveal mt-6 text-slate max-w-3xl">
      Which one you land in is worth knowing before you apply, and it takes one call to find out.
      If you have been told you need a waiting period, read
      <a class="link" href="/final-expense-insurance/no-waiting-period/">burial insurance with no
      waiting period</a> first: it is more often avoidable than people are told.
    </p>
  </div>
</section>


<!-- =====================================================================
     THE ASK. Phone first, with the four field form as the secondary.
     ================================================================== -->
<section class="section band-surface" id="talk">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">

      <div class="lg:col-span-6">
        <h2 class="reveal text-h2">Talk to a licensed agent</h2>
        <p class="reveal mt-5 text-slate">
          The fastest way to get a real answer is a phone call. We will ask your age, your state,
          and the health questions, and then tell you what you qualify for and what it costs.
          Nothing is submitted anywhere while we talk.
        </p>
        <div class="reveal mt-8">
          {C.phone_link("fe_seniors_footer", "btn btn-call btn-xl", "Call " + C.PHONE_DISPLAY, 26)}
          <p class="mt-3 text-sm text-muted">{C.HOURS}</p>
        </div>
        <p class="reveal mt-8 text-slate">
          If you would rather see what it costs before you speak to anyone, the cost by age is on
          <a class="link" href="/final-expense-insurance/cost/">final expense insurance cost</a>.
        </p>
      </div>

      <div class="lg:col-span-5 lg:col-start-8">
        <div class="reveal panel">
          {FE.callback_form("fes", "fe_seniors_callback")}
        </div>
      </div>
    </div>
  </div>
</section>


{C.spoke_module(
    "More about final expense insurance",
    "Every page in this section is written for the same reader.",
    [("/final-expense-insurance/burial-insurance/", "Burial insurance",
      "The same product under the name people search for."),
     ("/final-expense-insurance/funeral-insurance/", "Funeral insurance",
      "What it covers, and how it compares with pre paying."),
     ("/final-expense-insurance/quotes/", "Get a quote",
      "What we need from you, and how fast an answer comes back."),
     ("/final-expense-insurance/what-is-final-expense-insurance/", "What it is",
      "The plain definition, with the fine print left in."),
     ("/final-expense-insurance/for-parents/", "Coverage for a parent",
      "Buying a policy on a parent, and the consent it needs."),
     ("/final-expense-insurance/cremation-insurance/", "Cremation insurance",
      "What cremation costs, and how much coverage fits.")])}


{C.faq_section("Questions about final expense after 50", FAQ, "fe-seniors-faq", size=24)}


{C.byline_section()}
"""
