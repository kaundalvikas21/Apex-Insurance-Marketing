# -*- coding: utf-8 -*-
"""BURIAL INSURANCE WITH NO WAITING PERIOD. Spec P2, template T4. PHONE FIRST.

The sharpest objection in the category, and the easiest page on this site to
get wrong. The compliance line, which is load bearing rather than decorative:

    NEVER claim that immediate coverage is universally available.

So the qualification is in the first two sentences of the hero, not in a
footnote, and it is repeated as a visible notice above the table that shows
which policies pay from day one. Every sentence about qualifying is written as
"depends on your health answers and the carrier", never as "you will qualify".

Senior accessibility rules apply in full (html.fe). Tables are capped at three
columns including the row header, which is why the "who qualifies" material is
prose beneath the table rather than a fourth column.
"""
import chrome as C
import final_expense as FE

PATH = "/final-expense-insurance/no-waiting-period/"
OUT = "final-expense-insurance/no-waiting-period/index.html"
ACTIVE = "/final-expense-insurance/"
SILO = "final-expense"
HTML_CLASS = "fe"
TITLE = "Burial Insurance With No Waiting Period | Apex"
OG_TITLE = "Burial insurance with no waiting period"
DESC = ("Some burial insurance policies pay the full benefit from day one. Whether you qualify "
        "depends on your health answers and the carrier. What decides it, and how to find out.")

TRAIL = [("Home", "/"), ("Final Expense Insurance", "/final-expense-insurance/"),
         ("No waiting period", None)]

FAQ = [
    ("Is there burial insurance with no waiting period?",
     "Yes, these policies exist and they are common. They are called level benefit or immediate "
     "benefit policies, and they pay the full amount from the first day the policy is in force. "
     "Whether you can be issued one depends on your answers to the carrier's health questions and "
     "on which carrier you apply to, not on your age alone. Nobody can tell you that you qualify "
     "before those questions have been asked, and anyone who does is guessing."),
    ("How do I know if I qualify for immediate coverage?",
     "By answering the health questions, which takes about fifteen minutes on the phone and does "
     "not commit you to anything. Carriers disagree with each other about the same conditions, "
     "sometimes sharply, so the useful question is not whether you qualify but which carrier you "
     "qualify with. That is what an independent agency is for."),
    ("What happens if I die during a waiting period?",
     "On a typical graded or modified policy, if death is from an illness within the waiting "
     "period, usually two years, the carrier returns the premiums you paid plus interest rather "
     "than paying the face amount. If death is from an accident, the full amount is normally paid "
     "from day one. The exact terms differ by carrier and are written in the policy, so read that "
     "section or ask us to read it to you before you sign."),
    ("Which health conditions usually mean a waiting period?",
     "The ones carriers treat as recent or unstable rather than chronic and managed. A recent "
     "cancer diagnosis or treatment, congestive heart failure, oxygen use, dialysis, an organ "
     "transplant, a recent stroke or heart attack, dementia, and residence in a nursing home are "
     "the usual reasons a full benefit policy is not offered. Many chronic conditions that are "
     "treated and stable, including high blood pressure, controlled diabetes, and high "
     "cholesterol, frequently do not."),
    ("Is a policy with a waiting period still worth buying?",
     "Often yes, if a full benefit policy is genuinely not available to you. The coverage is real, "
     "the premium never rises, and accidental death is normally covered from day one. It is worth "
     "buying only after a licensed agent has checked whether a full benefit carrier would take "
     "you, because the difference in what your family receives during those two years is the whole "
     "point of asking."),
]


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    hero_cta = """<div class="reveal mt-8">
        %s
        <p class="mt-3 text-sm text-muted">%s</p>
      </div>""" % (C.phone_link("fe_nowait_hero", "btn btn-call btn-xl",
                                "Call " + C.PHONE_DISPLAY, 26), C.HOURS)

    return f"""
{C.page_hero(
    TRAIL,
    "Burial Insurance With No Waiting Period",
    'Many burial insurance policies do pay the full benefit from the first day, and they are not '
    'rare. Whether you can be issued one depends on your answers to the health questions and on '
    'which carrier you apply to, so no honest page can promise you immediate coverage before those '
    'questions have been asked. What this page can do is tell you exactly what decides it, and '
    'what happens if the answer turns out to be no. All of this is '
    '<a class="link" href="/final-expense-insurance/">final expense insurance</a>, sold under the '
    'name burial insurance.',
    extra=hero_cta, glow=False)}


<!-- =====================================================================
     WHAT A WAITING PERIOD IS. First section, because half the visitors
     arriving here have been told they need one and do not know what it
     means.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">What a waiting period is, and why carriers use one</h2>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <p class="reveal text-slate">
          A waiting period is the first stretch of a policy, almost always two years, during which
          the carrier will not pay the full death benefit if death is caused by illness. Instead it
          returns the premiums you paid, usually with interest added. Death from an accident is
          normally covered in full from the first day.
        </p>
        <p class="reveal mt-5 text-slate">
          Carriers use it for one reason. Final expense underwriting is a short list of questions
          and a prescription check rather than an exam, so when a carrier cannot get comfortable
          with the answers, the waiting period is what lets it say yes instead of no. Without it,
          the honest alternative for those applicants would be a decline.
        </p>
        <p class="reveal mt-5 text-slate">
          That is worth holding onto. A waiting period is not a penalty aimed at you, and it is not
          evidence that you have been sold something bad. It is the mechanism that keeps coverage
          available to people who would otherwise have none.
        </p>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     WHICH POLICIES PAY FROM DAY ONE. Three columns including the row
     header, per the senior table cap. The compliance notice sits ABOVE
     the table, so a reader meets it before the answer.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2">Which policies pay the full benefit from day one</h2>
      <p class="reveal mt-5 text-slate">
        Three kinds of policy are sold in this category. Only the first pays the full amount from
        the first day for any cause of death.
      </p>
      <div class="reveal mt-6">
        {C.flag("Availability is not universal and cannot be promised in advance. Which of these "
                "three you can be issued depends on your answers to the carrier's health "
                "questions, your prescription history, your state, and which carriers we are "
                "appointed with there. Nothing on this page is an offer of coverage or a "
                "guarantee of acceptance.", "IMPORTANT")}
      </div>
    </div>

    <div class="reveal mt-8 table-scroll table-signature">
      <table class="rate-table" style="min-width:0">
        <caption>What each kind of policy pays in the first two years.</caption>
        <thead>
          <tr>
            <th scope="col">Kind of policy</th>
            <th scope="col">Death from illness in the first two years</th>
            <th scope="col">Death from an accident</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row"><span class="block">Level benefit</span>
              <span class="block text-sm text-muted">Also called immediate or first day coverage</span>
            </th>
            <td>The full amount, from the first day the policy is in force.</td>
            <td>The full amount, from the first day.</td>
          </tr>
          <tr>
            <th scope="row"><span class="block">Graded or modified</span>
              <span class="block text-sm text-muted">Offered when some answers give a carrier pause</span>
            </th>
            <td>A reduced percentage of the amount, or your premiums returned with interest.
                Which of the two depends on the carrier.</td>
            <td>The full amount, from the first day.</td>
          </tr>
          <tr>
            <th scope="row"><span class="block">Guaranteed acceptance</span>
              <span class="block text-sm text-muted">No health questions asked at all</span>
            </th>
            <td>Your premiums returned with interest. A two year wait is standard.</td>
            <td>The full amount, from the first day.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p class="reveal mt-6 text-slate max-w-3xl">
      Most people who ask us about waiting periods are eligible for the first row. The assumption
      that they belong in the third row is the single most expensive mistake made in this category,
      because guaranteed acceptance costs the most per thousand dollars of coverage and carries the
      waiting period the applicant was trying to avoid.
    </p>
  </div>
</section>


{FE.call_band(
    "The only way to know is to answer the questions",
    "About fifteen minutes on the phone with a licensed agent. You will hear which carriers would "
    "issue you a full benefit policy and which would not. No application is submitted and there is "
    "no obligation.",
    "fe_nowait_band_1")}


<!-- =====================================================================
     THE QUESTIONS THAT DECIDE IT.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">The health questions that decide it</h2>
        <p class="reveal mt-5 text-slate">
          Every carrier asks a version of these. They are short, they are specific, and they are
          the whole of the underwriting.
        </p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <ul class="grid gap-5 text-slate">
          <li class="reveal">Have you been treated for, or advised to have treatment for, any of a
              named list of conditions in the last one, two, or five years. The window differs by
              carrier and this is where they disagree most.</li>
          <li class="reveal">Do you currently use oxygen, a wheelchair for a medical reason,
              dialysis, or receive care in a nursing home or from hospice.</li>
          <li class="reveal">Have you been hospitalised, or had a change to your medication, in the
              last twelve months.</li>
          <li class="reveal">What prescriptions do you take. The carrier checks this against a
              prescription database, so the answer needs to be complete.</li>
          <li class="reveal">Height, weight, and tobacco use.</li>
        </ul>
        <p class="reveal mt-6 text-slate">
          Answer all of them accurately. A policy issued on an inaccurate answer can be contested
          in the first two years, which produces exactly the outcome a waiting period would have
          produced, and does so as a surprise to your family.
        </p>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     WHAT USUALLY MEANS A WAIT, AND WHAT USUALLY DOES NOT.
     Two cards, equal weight, because the second one is the part people
     do not expect.
     ================================================================== -->
<section class="section band-surface">
  <div class="container-ax">
    <div class="grid lg:grid-cols-2 gap-8 lg:gap-10 items-start">

      <div class="reveal card">
        <h2 class="text-h3 !font-display !font-semibold">Usually means a waiting period</h2>
        <ul class="mt-5 grid gap-4 text-slate">
          <li>A cancer diagnosis or treatment within the last one to three years.</li>
          <li>Congestive heart failure, or a stroke or heart attack in the recent past.</li>
          <li>Oxygen use for a lung condition, or dialysis for kidney failure.</li>
          <li>An organ transplant, or being on a waiting list for one.</li>
          <li>Dementia or Alzheimer's disease, or residence in a nursing home.</li>
          <li>Insulin started before a certain age, or diabetic complications.</li>
        </ul>
        <p class="mt-5 text-slate">
          Even here, carriers differ on the length of the look back window. A condition that is
          three years past at one carrier may be inside the window at another.
        </p>
      </div>

      <div class="reveal card">
        <h2 class="text-h3 !font-display !font-semibold">Usually does not</h2>
        <ul class="mt-5 grid gap-4 text-slate">
          <li>High blood pressure that is treated and stable.</li>
          <li>Type 2 diabetes controlled with tablets or diet.</li>
          <li>High cholesterol.</li>
          <li>Arthritis, thyroid conditions, acid reflux, and most joint replacements.</li>
          <li>Depression or anxiety that is treated and stable.</li>
          <li>A cancer that was treated and is many years in the past.</li>
        </ul>
        <p class="mt-5 text-slate">
          Being on several medications is not by itself a reason for a waiting period. What matters
          is what they are for, how long you have taken them, and whether anything changed
          recently.
        </p>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     WHAT HAPPENS IF YOU DIE DURING A GRADED PERIOD. The question people
     are too uncomfortable to ask, answered plainly.
     ================================================================== -->
<section class="section band-navy on-navy">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2 text-white">If you die during a waiting period</h2>
      <p class="reveal mt-5 text-white/85">
        Your family does not get nothing. That is the fear, and it is not what the contract says.
      </p>
    </div>

    <div class="mt-10 grid md:grid-cols-3 gap-8 max-w-5xl">
      <div class="reveal">
        <h3 class="text-h4 text-white">From an accident</h3>
        <p class="mt-3 text-white/85">
          The full face amount is normally paid from the first day, with no waiting period applied.
          This is standard across the category.
        </p>
      </div>
      <div class="reveal">
        <h3 class="text-h4 text-white">From an illness</h3>
        <p class="mt-3 text-white/85">
          The carrier returns the premiums you paid, commonly with interest added, or pays a
          reduced percentage of the face amount. Which of the two is written in your policy.
        </p>
      </div>
      <div class="reveal">
        <h3 class="text-h4 text-white">After the waiting period</h3>
        <p class="mt-3 text-white/85">
          The full amount, for any cause. The waiting period applies once, at the start, and never
          returns.
        </p>
      </div>
    </div>

    <p class="reveal mt-10 max-w-3xl text-white/85">
      Ask for the exact wording before you sign, and ask us to read it with you. The difference
      between a return of premium with interest and a reduced percentage of the face amount is
      real money to your family, and it is decided by which carrier the application went to.
    </p>
  </div>
</section>


<!-- =====================================================================
     THE ASK. Phone first, short form secondary.
     ================================================================== -->
<section class="section" id="talk">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">

      <div class="lg:col-span-6">
        <h2 class="reveal text-h2">Find out in one call</h2>
        <p class="reveal mt-5 text-slate">
          A licensed agent will ask the health questions and tell you which of our appointed
          carriers would issue you a policy that pays from day one. If none would, we will say so
          and explain what is available instead. Either way you will know, rather than guess.
        </p>
        <div class="reveal mt-8">
          {C.phone_link("fe_nowait_footer", "btn btn-call btn-xl", "Call " + C.PHONE_DISPLAY, 26)}
          <p class="mt-3 text-sm text-muted">{C.HOURS}</p>
        </div>
        <p class="reveal mt-8 text-slate">
          If no health questions at all is what you are looking for, that is a different product
          with its own trade offs, covered on
          <a class="link" href="/whole-life-insurance/guaranteed-acceptance/">guaranteed acceptance
          whole life</a>.
        </p>
      </div>

      <div class="lg:col-span-5 lg:col-start-8">
        <div class="reveal panel">
          {FE.callback_form("fenw", "fe_no_waiting_callback")}
        </div>
      </div>
    </div>
  </div>
</section>


{C.spoke_module(
    "More about final expense insurance",
    "Every page in this section is written for the same reader.",
    [("/final-expense-insurance/for-seniors/", "Final expense after 50",
      "What changes at 70 and at 80, and what does not."),
     ("/final-expense-insurance/burial-insurance/", "Burial insurance",
      "The same product under the name people search for."),
     ("/final-expense-insurance/cost/", "What it costs",
      "How the premium moves between ages 50 and 85."),
     ("/final-expense-insurance/quotes/", "Get a quote",
      "What we need from you, and how fast an answer comes back."),
     ("/final-expense-insurance/what-is-final-expense-insurance/", "What it is",
      "The plain definition, with the fine print left in."),
     ("/final-expense-insurance/funeral-insurance/", "Funeral insurance",
      "What it covers, and how it compares with pre paying.")])}


{C.faq_section("Questions about waiting periods", FAQ, "fe-nowait-faq", size=24)}


{C.byline_section()}
"""
