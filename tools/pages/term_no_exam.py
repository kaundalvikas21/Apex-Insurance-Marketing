# -*- coding: utf-8 -*-
"""NO MEDICAL EXAM TERM LIFE. Spec P2, template T4, treated as near-money.

High intent objection page: the visitor has usually already decided to buy and
is looking for a reason not to be examined. So the CTA rhythm is denser than a
standard T4 and the form and the phone carry equal weight, per the spec's per
silo weighting note for this page.

The form is on the page rather than one link away. Three separate links to
/term-life-insurance/quotes/ would break spec s07 rule 4 (one link per target
per page), and an objection page that answers the objection and then asks the
reader to navigate somewhere else to act on it is throwing away the intent it
just earned. term.quote_form() is reused verbatim, which is the same pattern
/term-life-insurance/rates/ uses.

Compliance note: nothing here promises approval, and the "same day" section
says plainly that same day means a decision, not always an approval.
"""
import chrome as C
import term

PATH = "/term-life-insurance/no-medical-exam/"
OUT = "term-life-insurance/no-medical-exam/index.html"
ACTIVE = "/term-life-insurance/"
SILO = "term-life"
TITLE = "No Medical Exam Term Life Insurance | Same-Day Options | Apex"
OG_TITLE = "No medical exam term life insurance"
DESC = ("Three ways to buy term life insurance without a paramedical exam, what each one costs "
        "you, and who should still take the exam. Decisions in as little as a day.")

TRAIL = [("Home", "/"), ("Term Life Insurance", "/term-life-insurance/"),
         ("No medical exam", None)]

# The three routes. Nothing in this table is a price, so nothing in it is a
# placeholder; every cell is a description of how a programme behaves.
ROUTES = [
    ("What the carrier does instead",
     "Reads prescription, motor vehicle, and claims databases, plus a long application. An "
     "algorithm decides whether an exam is needed.",
     "A short set of yes or no health questions, answered on a call or a form. A human "
     "underwriter reviews them.",
     "Asks nothing about your health at all."),
    ("Typical decision time",
     "Minutes to a few days.",
     "Same day to about a week.",
     "Same day."),
    ("Coverage amounts it reaches",
     "Full term amounts, into the millions at younger ages.",
     "Moderate. Commonly capped well below fully underwritten limits.",
     "Small. Built for final expenses rather than income replacement."),
    ("What it costs you",
     "Usually nothing. Priced at the same rate classes as a fully underwritten policy.",
     "A class or two, sometimes more. You pay for the carrier's uncertainty.",
     "The most per thousand of coverage of any life product, and a waiting period is normal."),
    ("Who it suits",
     "Healthy applicants under roughly sixty who would have passed the exam anyway.",
     "People with a manageable condition, or who genuinely cannot face an exam.",
     "People who have been declined elsewhere, and who need a funeral covered rather than an "
     "income replaced."),
]

FAQ = [
    ("Can you really get life insurance with no medical exam?",
     "Yes, and for a healthy applicant under about sixty it is now the normal experience rather "
     "than a special product. Accelerated underwriting programmes check prescription, driving, "
     "and claims databases against a detailed application and waive the exam when the picture is "
     "consistent. You still answer full health questions, and the application is still a legal "
     "declaration. What is skipped is the needle, not the honesty."),
    ("Is no exam life insurance more expensive?",
     "It depends which of the three routes you take. Accelerated underwriting is normally priced "
     "at the same rate classes as a fully underwritten policy, so it costs nothing extra. "
     "Simplified issue prices in the carrier's uncertainty and usually costs a class or two more. "
     "Guaranteed issue, where no health question is asked at all, is the most expensive coverage "
     "per thousand dollars sold anywhere, and almost always carries a waiting period."),
    ("How fast can I actually be covered?",
     "With accelerated underwriting, a decision can come the same day and coverage begins once the "
     "policy is issued, delivered, and the first premium is paid. Same day means a same day "
     "decision, not always a same day approval and not always a yes. If the algorithm cannot get "
     "comfortable, the application drops to full underwriting with an exam, which is not a decline "
     "and simply takes longer."),
    ("Will they still check my prescriptions and medical records?",
     "Almost certainly. Every route except guaranteed issue uses a prescription history check, and "
     "most use a motor vehicle record and the industry claims database. Some also pull electronic "
     "health records with your authorisation. Leaving something off the application does not hide "
     "it, and it does give the carrier a reason to contest a claim inside the first two years."),
    ("Should I take the exam if I am offered the choice?",
     "If you are in good health, usually yes. A paramedical exam is free, takes about twenty "
     "minutes at your home or office, and often lands you in a better rate class than an "
     "algorithm will award without it. The exam is worth skipping when speed genuinely matters, "
     "when a needle is a real obstacle for you, or when your readings on the day are likely to be "
     "worse than your record suggests."),
]


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    rows = "\n            ".join(
        '<tr><th scope="row">%s</th><td>%s</td><td>%s</td><td>%s</td></tr>' % r for r in ROUTES)

    hero_cta = """<div class="reveal mt-8 flex flex-wrap items-center gap-3">
        <a class="btn btn-cta" href="#quote">See if you qualify</a>
        %s
        <p class="w-full text-micro text-muted">%s</p>
      </div>""" % (C.phone_link("term_noexam_hero", "btn btn-call"), C.HOURS)

    return f"""
{C.page_hero(
    TRAIL,
    "No Medical Exam Term Life Insurance",
    'Most healthy applicants under about sixty can now buy '
    '<a class="link" href="/term-life-insurance/">term life insurance</a> without a paramedical '
    'exam, at the same price they would have paid with one, with a decision in minutes rather than '
    'weeks. That is real, and it is not the whole story: there are three different ways to skip '
    'the exam and they cost very different amounts. This page tells you which one you are likely '
    'to be offered and what it will cost you.',
    extra=hero_cta)}


<!-- =====================================================================
     THE THREE ROUTES. The page's signature object, and the section that
     stops "no exam" being read as one product.
     ================================================================== -->
<section class="pb-14 md:pb-16 scroll-mt-28" id="who-qualifies">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2">Three ways to skip the exam, and what each one costs</h2>
      <p class="reveal mt-5 text-slate">
        Advertising treats these as one thing. They are not. The left hand column is what most
        healthy people get and it is nearly free; the right hand column is a different product
        sold to a different person for a different reason.
      </p>
    </div>

    <div class="reveal mt-8 table-scroll table-signature">
      <table class="compare-table" style="min-width:52rem">
        <caption class="sr-only">
          Accelerated underwriting, simplified issue, and guaranteed issue compared.
        </caption>
        <thead>
          <tr>
            <th scope="col"><span class="sr-only">Feature</span></th>
            <th scope="col">Accelerated underwriting</th>
            <th scope="col">Simplified issue</th>
            <th scope="col">Guaranteed issue</th>
          </tr>
        </thead>
        <tbody>
            {rows}
        </tbody>
      </table>
    </div>

    <p class="reveal mt-6 text-slate max-w-3xl">
      Guaranteed issue is in the table for completeness, and it is a final expense product rather
      than a term one. If that column is where you are, the coverage is real and the right place
      to read about it is the
      <a class="link" href="/final-expense-insurance/">final expense insurance</a> hub.
    </p>
  </div>
</section>


<!-- =====================================================================
     WHAT SAME DAY MEANS. The honesty section. Compliance: never claim
     immediate coverage is universal.
     ================================================================== -->
{C.prose(
    "What same day actually means",
    C.step(1, "You complete the application",
           "Fifteen to twenty five minutes, on a call or online. Longer than the marketing "
           "suggests, because accelerated programmes ask more questions rather than fewer: the "
           "questions are doing the work the exam used to do.")
    + '<div class="mt-8">' + C.step(2, "The carrier queries the databases",
           "Prescription history, motor vehicle record, and the industry claims exchange, in "
           "minutes. Some carriers also request electronic health records with your permission, "
           "which can add a day or two.")
    + '</div><div class="mt-8">' + C.step(3, "One of three things happens",
           "Approved as applied for, approved at a different class than quoted, or referred to "
           "full underwriting with an exam. A referral is not a decline and it is common: it "
           "means the algorithm found something it will not decide on its own.")
    + '</div><div class="mt-8">' + C.step(4, "Coverage starts when the policy is in force",
           "Issued, delivered, and first premium paid. Not at approval, and not when you submit "
           "the application. A conditional receipt can start limited coverage earlier on some "
           "carriers, and that is worth asking about if the timing matters to you.",
           "If you need coverage in force by a specific date, say so at the start. It changes "
           "which carrier we send you to.")
    + '</div>',
    intro="Same day means a same day decision. It does not mean a guaranteed approval, and no "
          "carrier can promise one before it has read your answers.",
    cls="section band")}


{C.inline_cta(
    "Not sure which route you would land in?",
    "A licensed agent can tell you in a few minutes, from your age, your state, and what you "
    "take. That conversation costs nothing and does not put an application anywhere.",
    "term_noexam_mid", "#quote", "Or answer six questions instead",
    phone_first=True)}


<!-- =====================================================================
     THE TRADE. What skipping the exam costs, and who should not.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-2 gap-8 lg:gap-10 items-start">

      <div class="reveal card">
        <h2 class="text-h3 !font-display !font-semibold">What you give up</h2>
        <ul class="mt-5 grid gap-4 text-slate">
          <li><strong class="text-ink">Coverage ceiling.</strong> Accelerated programmes have limits
              on face amount and age. Above them, the exam comes back whether you want it or not.</li>
          <li><strong class="text-ink">The best rate class.</strong> An algorithm awards the class it
              can defend from data. An exam that shows excellent blood pressure and cholesterol can
              beat it, sometimes by two classes.</li>
          <li><strong class="text-ink">A second opinion on yourself.</strong> A paramedical exam is a
              free set of readings. People do occasionally learn something from it that matters more
              than the policy.</li>
          <li><strong class="text-ink">Nothing at all, quite often.</strong> If you are young and
              healthy and the databases agree with your application, accelerated underwriting costs
              you no money and saves you three weeks.</li>
        </ul>
      </div>

      <div class="reveal card">
        <h2 class="text-h3 !font-display !font-semibold">Who should still take the exam</h2>
        <ul class="mt-5 grid gap-4 text-slate">
          <li>Anyone buying a large face amount, where a single rate class is worth more over the
              term than three weeks of waiting.</li>
          <li>Anyone over roughly sixty, where fully underwritten pricing is usually better and the
              accelerated programmes thin out.</li>
          <li>Anyone whose numbers have genuinely improved since their records were written: a
              current reading beats an old prescription.</li>
          <li>Anyone who has been rated or declined before. A human underwriter can be argued with.
              An algorithm cannot.</li>
        </ul>
        <p class="mt-5 text-slate">
          The exam is free, takes about twenty minutes, and happens at your kitchen table. It is
          worth avoiding for speed or for a real aversion, not out of habit.
        </p>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     THE FORM. Equal weight with the phone beside it, per the spec's
     weighting for this page.
     ================================================================== -->
<section class="section band-surface" id="quote">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">Find out which route you qualify for</h2>
        <p class="reveal mt-5 text-slate">
          Six questions, about two minutes. A licensed agent comes back within {C.SLA} with the
          carriers most likely to waive the exam for your age and health, and the price if they do
          not. We will tell you when taking the exam is the better deal.
        </p>
        <div class="reveal mt-6 pt-6 border-t border-rule">
          <p class="text-slate">Or ask first, and apply later.</p>
          <div class="mt-4">{C.phone_link("term_noexam_form", "btn btn-call")}</div>
          <p class="mt-3 text-micro text-muted">{C.HOURS}</p>
        </div>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <div class="reveal panel">
          {term.quote_form("term-noexam-quote-form", "term_no_exam_quote", "tnx")}
        </div>
      </div>
    </div>
  </div>
</section>


{C.spoke_module(
    "Related pages in term life",
    "Underwriting decides the price. These pages cover what the price then looks like.",
    [("/term-life-insurance/rates/", "Term rates by age",
      "The full grid, and the six levers that move it."),
     ("/term-life-insurance/quotes/", "Get term life quotes",
      "The full quote page, with what to have to hand."),
     ("/term-life-insurance/what-is-term-life-insurance/", "What term life insurance is",
      "The plain definition, with the fine print left in."),
     ("/term-life-insurance/level-term/", "Level term explained",
      "What the premium guarantee covers, and for how long."),
     ("/term-life-insurance/for-seniors/", "Term life after 60",
      "Where the accelerated programmes stop reaching."),
     ("/term-life-insurance/20-year-term/", "20 year term",
      "The most common length, checked against real dates.")])}


{C.faq_section("Questions about no exam term life", FAQ, "term-noexam-faq")}


{C.byline_section()}
"""
