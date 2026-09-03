# -*- coding: utf-8 -*-
"""TERM LIFE FOR SENIORS. Spec P2, template T4. PHONE WEIGHTED.

The exception in this silo. Everything else under /term-life-insurance/ is
form first; this page leads with the phone, because the honest answer for a
sixty eight year old depends on facts a six field form cannot collect.

The page is also the silo's one honest off ramp. Term genuinely stops being
the right product somewhere between the late sixties and the mid seventies,
and the sanctioned route out (spec s07 rule 3: cross silo movement via a hub
or a /compare/ page) is a link to the final expense hub. Sending an
unqualified visitor into a term quote form instead would produce a lead that
cannot be written and a phone call nobody enjoys.

No invented issue ages: the availability table says "commonly", carries a
visible flag, and is to be replaced with the real appointed carrier grid.
"""
import chrome as C

PATH = "/term-life-insurance/for-seniors/"
OUT = "term-life-insurance/for-seniors/index.html"
ACTIVE = "/term-life-insurance/"
SILO = "term-life"
TITLE = "Term Life Insurance for Seniors Over 60 | Rates & Options | Apex"
OG_TITLE = "Term life insurance for seniors over 60"
DESC = ("What term life insurance is still available after 60, what it costs, where issue ages "
        "stop, and when a small permanent policy is the better answer. Talk to a licensed agent.")

TRAIL = [("Home", "/"), ("Term Life Insurance", "/term-life-insurance/"),
         ("For seniors", None)]

# Availability, not price. Structural placeholder: carriers differ, and the
# real grid comes from the appointed carrier list.
AVAILABILITY = [
    ("60 to 64", "Widely available", "Widely available", "Widely available", "Limited"),
    ("65 to 69", "Widely available", "Widely available", "Limited", "Not offered"),
    ("70 to 74", "Widely available", "Limited", "Rare", "Not offered"),
    ("75 to 79", "Limited", "Rare", "Not offered", "Not offered"),
    ("80 and over", "Rare", "Not offered", "Not offered", "Not offered"),
]

FAQ = [
    ("Can you get term life insurance at 70?",
     "Usually yes, most commonly as a ten year term and sometimes fifteen, and the number of "
     "carriers willing to write it drops sharply. Whether it is a good idea is a separate "
     "question from whether it is possible. At seventy, a ten year term leaves you uninsured at "
     "eighty, which is the age at which cover is hardest to replace. If the need genuinely ends "
     "within ten years, that is fine. If it does not, a small permanent policy usually serves you "
     "better even though the premium per thousand looks worse."),
    ("What is the oldest age you can buy term life insurance?",
     "Most carriers stop issuing new term somewhere between 75 and 80, and the few that go higher "
     "restrict it to short terms and modest face amounts. There is no single industry cutoff, "
     "which is exactly why this is worth one phone call rather than an afternoon of comparison "
     "sites. We can tell you in a few minutes which of our appointed carriers will still write "
     "your age in your state."),
    ("Is term life insurance worth it for a senior?",
     "It is worth it when there is a specific obligation with an end date: a mortgage with eleven "
     "years left, a business loan, a spouse who needs your pension bridged until theirs starts, or "
     "a co signed debt. It is poor value when the purpose is a funeral or a legacy, because those "
     "needs do not expire and term does. The test is not your age, it is whether the need has a "
     "date on it."),
    ("Do I need a medical exam to get term life insurance at 65?",
     "Often, yes, and it usually works in your favour. Accelerated underwriting programmes that "
     "skip the exam are mostly built around younger applicants and smaller face amounts, so above "
     "sixty the fully underwritten route with a paramedical exam frequently produces a better "
     "class and a lower premium. If your health makes an exam a bad bet, say so at the start and "
     "we will aim you at the carriers that are kindest about it."),
    ("What if I am declined for term life insurance?",
     "A decline is not the end of the conversation, and it does not follow you the way people "
     "fear. Guaranteed acceptance and simplified issue permanent policies ask few or no health "
     "questions and are written specifically for applicants term carriers will not take. The face "
     "amounts are smaller and the cost per thousand is higher, and for a funeral and final bills "
     "that is usually the right trade."),
]


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    rows = "\n            ".join(
        '<tr><th scope="row">%s</th>%s</tr>'
        % (band, "".join('<td>%s</td>' % v for v in vals))
        for band, *vals in [list(r) for r in AVAILABILITY])

    hero_cta = """<div class="reveal mt-8 flex flex-wrap items-center gap-4">
        %s
        <p class="text-micro text-muted">%s</p>
      </div>""" % (C.phone_link("term_seniors_hero", "btn btn-call"), C.HOURS)

    return f"""
{C.page_hero(
    TRAIL,
    "Term Life Insurance for Seniors Over 60",
    'After sixty, <a class="link" href="/term-life-insurance/">term life insurance</a> is still '
    'available and still sensible, but only for a need with an end date on it. Premiums rise '
    'steeply through this decade, the number of carriers willing to write you shrinks every few '
    'years, and most stop issuing new term somewhere between seventy five and eighty. This page '
    'says plainly what is still available, what it costs, and when a small permanent policy is the '
    'better buy.',
    extra=hero_cta)}


<!-- =====================================================================
     AVAILABILITY. The honest answer to "can I still get this", first,
     because it is the question that brought the visitor here.
     ================================================================== -->
<section class="pb-14 md:pb-16">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2">What is still available, by age</h2>
      <p class="reveal mt-5 text-slate">
        Availability, not price. A cell that says limited means a handful of our carriers will
        consider it, usually with tighter health requirements and a lower maximum face amount.
      </p>
      <div class="reveal mt-6">
        {C.flag("This grid is a structural placeholder describing the general shape of the market. "
                "Replace it with the real issue age and term availability grid for the appointed "
                "carrier list, by state, before this page goes live.",
                "PLACEHOLDER: REPLACE WITH APPOINTED CARRIER ISSUE AGE GRID")}
      </div>
    </div>

    <div class="reveal mt-8 table-scroll table-signature">
      <table class="rate-table" style="min-width:44rem">
        <caption>New term policies commonly issued at each age, by term length.</caption>
        <thead>
          <tr>
            <th scope="col">Age at application</th>
            <th scope="col">10 year</th>
            <th scope="col">15 year</th>
            <th scope="col">20 year</th>
            <th scope="col">30 year</th>
          </tr>
        </thead>
        <tbody>
            {rows}
        </tbody>
      </table>
    </div>

    <p class="reveal mt-4 text-micro text-muted max-w-3xl">
      <span class="pill mr-2">Reviewed: {C.REVIEW_DATE}</span>
      Issue ages, maximum face amounts, and available term lengths vary by carrier and by state,
      and change without much notice. This is a description of the market, not an offer of coverage.
    </p>

    <p class="reveal mt-8 text-slate max-w-3xl">
      For what the premium itself does across these ages, the full grid is on our
      <a class="link" href="/term-life-insurance/rates/">term life insurance rates</a> page, which
      runs to age seventy four by five year bands.
    </p>
  </div>
</section>


<!-- =====================================================================
     THE COST CURVE. Why waiting is expensive, without a single
     invented number.
     ================================================================== -->
{C.prose(
    "Why the price moves so fast in this decade",
    C.qa("The premium tracks one year of risk at a time",
         "Term pricing is built from the chance of a claim during the term. That chance is small "
         "and flat through your thirties and forties, and it starts bending upward in the late "
         "fifties. By the mid sixties each additional year of age costs meaningfully more than the "
         "one before it, which is why a chart of term rates looks like a hockey stick rather than "
         "a ramp.")
    + C.qa("A longer term compounds the same effect",
           "A twenty year term bought at sixty five is priced across ages sixty five to eighty "
           "five, and the back half of that window is where nearly all the risk sits. That is the "
           "real reason twenty and thirty year terms disappear from the grid above, rather than "
           "any rule about how old you are.", "mt-8")
    + C.qa("Health class matters more than it used to",
           "At thirty five, the gap between preferred and standard is real but modest. At "
           "sixty eight it is large, and the carriers disagree with each other far more than they "
           "did about the same applicant thirty years earlier. This is the age at which shopping "
           "several carriers stops being tidy and starts being worth actual money.", "mt-8")
    + C.qa("Waiting a year is not free",
           "The same policy bought a year later costs more for its entire term, and a year is also "
           "long enough for a diagnosis to change which carriers will take you at all. If you are "
           "going to buy, the cheapest day is the first one you are sure.", "mt-8"),
    intro="Three forces, all pulling the same way. None of them is a sales tactic, and all of "
          "them are visible in any carrier's rate card.",
    cls="section band")}


{C.inline_cta(
    "Fifteen minutes on the phone will settle this",
    "Tell a licensed agent your age, your state, and roughly what your health looks like. You will "
    "get a straight answer about which carriers will write you and whether term is even the right "
    "product, before you fill in anything.",
    "term_seniors_mid", "/term-life-insurance/quotes/", "Or start a quote online",
    phone_first=True)}


<!-- =====================================================================
     THE TWO CASES. Equal prominence, per the design system's rule
     that a "does not suit" section matches its opposite.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-2 gap-8 lg:gap-10 items-start">

      <div class="reveal card">
        <h2 class="text-h3 !font-display !font-semibold">When term is right after 60</h2>
        <ul class="mt-5 grid gap-4 text-slate">
          <li>A mortgage or a business loan with a known payoff date inside the term.</li>
          <li>A spouse who would need your income bridged until their own pension or Social
              Security starts.</li>
          <li>A co signed debt, a private loan, or a lease you have personally guaranteed.</li>
          <li>Children or grandchildren you are supporting through a defined period of education.</li>
          <li>An existing term policy running out, where a conversion right may be worth more than
              a new application.</li>
        </ul>
        <p class="mt-5 text-slate">
          What all five have in common is a date. If you can name the year the need ends, term is
          almost certainly the cheapest way to cover it.
        </p>
      </div>

      <div class="reveal card">
        <h2 class="text-h3 !font-display !font-semibold">When it is the wrong tool</h2>
        <ul class="mt-5 grid gap-4 text-slate">
          <li>The purpose is a funeral, burial, or cremation and the bills that follow.</li>
          <li>You want to leave something behind whenever that happens, not only if it happens
              within ten years.</li>
          <li>Your health means term carriers are likely to decline or heavily rate you.</li>
          <li>The amount you need is small, where term's per policy costs work against you.</li>
          <li>You are over seventy five, where the grid above has largely run out.</li>
        </ul>
        <p class="mt-5 text-slate">
          In every one of those cases the need has no expiry date, and buying a product that does
          expire is how people end up uninsured at exactly the age they cannot replace it.
        </p>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     THE OFF RAMP. Cross silo, via the hub, which is the sanctioned
     route (spec s07 rule 3). Deliberately generous rather than grudging.
     ================================================================== -->
<section class="section band-navy on-navy">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-6">
        <h2 class="reveal text-h2 text-white">If term is not the answer for you</h2>
        <p class="reveal mt-5 text-white/85">
          We would rather tell you that on this page than after an application. For a funeral,
          final bills, and a modest amount left behind, the product built for the job is a small
          permanent policy, sold under the name
          <a class="link !text-white" href="/final-expense-insurance/">final expense insurance</a>.
        </p>
        <p class="reveal mt-5 text-white/85">
          It is whole life, so the premium never rises and the coverage never ends. Face amounts
          typically run from a few thousand up to around fifty thousand, underwriting is health
          questions rather than an exam, and issue ages run to eighty five with most carriers.
        </p>
      </div>
      <div class="lg:col-span-5 lg:col-start-8">
        <div class="reveal card">
          <h3 class="text-h4 !text-ink">Not sure which side of the line you are on?</h3>
          <p class="mt-3 text-slate">
            The question that decides it is whether the need has an end date. A licensed agent can
            work through that with you in one call, and will say so if the answer is that you do
            not need to buy anything today.
          </p>
          <div class="mt-5">
            {C.phone_link("term_seniors_offramp", "btn btn-call btn-block")}
          </div>
          <p class="mt-3 text-micro text-muted text-center">{C.HOURS}</p>
        </div>
      </div>
    </div>
  </div>
</section>


{C.spoke_module(
    "Also in term life insurance",
    "The pages most people read next when they are weighing this at sixty or above.",
    [("/term-life-insurance/what-is-term-life-insurance/", "What term life insurance is",
      "The plain definition, and what happens when a term ends."),
     ("/term-life-insurance/no-medical-exam/", "No medical exam term life",
      "When skipping the exam helps, and when it costs you a class."),
     ("/term-life-insurance/level-term/", "Level term life insurance",
      "What stays level, and what the renewal rate does after."),
     ("/term-life-insurance/calculator/", "Coverage calculator",
      "Size the obligation before you price it."),
     ("/term-life-insurance/20-year-term/", "20 year term",
      "The most common length, checked against real dates."),
     ("/term-life-insurance/30-year-term/", "30 year term",
      "When the extra decade is worth what it costs.")])}


{C.faq_section("Questions seniors ask about term life", FAQ, "term-seniors-faq")}


{C.byline_section()}
"""
