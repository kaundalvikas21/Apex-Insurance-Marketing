# -*- coding: utf-8 -*-
"""FINAL EXPENSE COST BY AGE. Spec P1, template T2, INVERTED. PHONE FIRST.

The silo's cost page. Six built pages route their cost question here rather
than answering it themselves, which is the whole reason this page is lean on
definitions and dense on price behaviour: it is the one place the figures are
kept, so it is the one place that has to be right.

T2 says the chart is the page and it comes first. That is kept. What is
inverted is the CTA: the row level action is a click-to-call inside the age
cell rather than a prefill button, because there is no form on this page to
prefill and because the silo is phone weighted. That is exactly what
rate_chart's "call" mode exists for, and it is also how the table stays inside
the three column senior cap.

Every cell is `$--` by decision (MASTER.md line 23). The sex toggle drives the
caption, not the numbers, until the carrier rate cards land.

Senior accessibility rules apply in full (html.fe).
"""
import chrome as C
import final_expense as FE

PATH = "/final-expense-insurance/cost/"
OUT = "final-expense-insurance/cost/index.html"
ACTIVE = "/final-expense-insurance/"
SILO = "final-expense"
HTML_CLASS = "fe"
TITLE = "Final Expense Insurance Cost by Age (2026 Chart) | Apex"
OG_TITLE = "What final expense insurance costs by age"
DESC = ("What final expense insurance costs between 50 and 85, what moves the premium, and how "
        "to bring a quoted price down without leaving anything off the application.")

TRAIL = [("Home", "/"), ("Final Expense Insurance", "/final-expense-insurance/"),
         ("What it costs", None)]

AGE_BANDS = [("50 to 54", None), ("55 to 59", None), ("60 to 64", None), ("65 to 69", None),
             ("70 to 74", None), ("75 to 79", None), ("80 to 85", None)]
COVERAGE_COLS = ["$10,000", "$25,000"]

FAQ = [
    ("How much does final expense insurance cost per month?",
     "It depends on four things: your age when the policy is issued, how much coverage you buy, "
     "whether you use tobacco, and your answers to the health questions. That is why this page is "
     "a chart rather than a single figure. What is fair to say is the shape. The premium rises "
     "steadily with age and rises sharply after about seventy five, it roughly tracks the "
     "coverage amount, and once it is set it never moves again for as long as the policy is in "
     "force."),
    ("Does the premium go up as I get older?",
     "No. That is the defining feature of the product and the main reason people buy it at this "
     "age. The premium is calculated once, from your age and health at the time the policy is "
     "issued, and it is guaranteed not to rise. What rises is the price of buying a new policy "
     "later, which is a different thing and is the real cost of waiting."),
    ("Why is the price so much higher at 80 than at 60?",
     "Because the carrier is pricing the years between now and a claim, and at eighty there are "
     "fewer of them. It is the same coverage doing the same job, collected over a shorter time. "
     "This is also why the advice to buy the amount you can carry rather than the largest amount "
     "you qualify for gets more important with every year."),
    ("How much does tobacco use add?",
     "Commonly a meaningful step up in premium for the same coverage, and you carry the "
     "difference for the rest of your life rather than for a term. Most carriers ask about the "
     "last twelve months. A few will reconsider the class after a documented period without "
     "nicotine, which is worth asking about rather than assuming."),
    ("Can I lower the price I have been quoted?",
     "Usually, and there are five legitimate ways to try, all of them on this page. None of them "
     "involves leaving something off an application. Answering a health question wrongly is not a "
     "discount, it is a reason for the carrier to contest the claim, and the person who pays for "
     "that is your family."),
    ("Is it worth buying at 80?",
     "Sometimes yes and sometimes no, and we will say which on the call rather than in a "
     "brochure. It is worth it when your family would otherwise have to find the money quickly "
     "and the premium fits comfortably in your budget. It is not worth it when the premium would "
     "strain a fixed income, because a policy that lapses at eighty five has cost you every "
     "payment and paid nothing back."),
]


LOWER = """<p class="reveal text-slate">
        Five things worth trying, in the order we would try them. None of them involves leaving
        anything off an application.
      </p>
      <ul class="mt-8 grid gap-6 text-slate">
        <li class="reveal"><span class="font-semibold text-ink">Let us try more than one
            carrier.</span> The same health history can produce a level benefit policy at one
            carrier and a graded one at another. This is the single biggest lever on this page and
            it is the one you cannot pull on your own.</li>
        <li class="reveal"><span class="font-semibold text-ink">Size the policy to the job.</span>
            Work out what the funeral and the bills would actually come to and insure that, rather
            than picking a round number. It is usually a bigger saving than any class change.</li>
        <li class="reveal"><span class="font-semibold text-ink">Ask what each rider costs as a
            line.</span> Accidental death and child riders are added easily and removed just as
            easily. Anything you cannot explain the purpose of back to the agent is a line you can
            probably drop.</li>
        <li class="reveal"><span class="font-semibold text-ink">Pay annually if you can.</span>
            Most carriers charge a modal factor for monthly payment. Paying yearly, or even
            quarterly, is a real discount rather than a sales tactic.</li>
        <li class="reveal"><span class="font-semibold text-ink">Buy sooner rather than
            later.</span> Not a sales line, an arithmetic one. The premium is set by your age at
            issue, so a year of thinking about it costs a year of pricing, permanently.</li>
      </ul>
      <p class="reveal mt-8 text-slate">
        If a waiting period is the thing pushing your price up, read
        <a class="link" href="/final-expense-insurance/no-waiting-period/">burial insurance with no
        waiting period</a> before you accept it. Some carriers will write day one coverage for
        histories that others grade.
      </p>"""


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    return f"""
<section class="pt-6 pb-10">
  <div class="container-ax">
    {C.crumbs(TRAIL)}

    <div class="mt-8 max-w-3xl">
      <h1 class="reveal text-h1">Final Expense Insurance Cost by Age</h1>
      <p class="reveal mt-5 text-lead text-slate">
        The chart below is how the premium for
        <a class="link" href="/final-expense-insurance/">final expense insurance</a> moves between
        fifty and eighty five. The figure in each row is the amount you would pay every month for
        the rest of your life, fixed on the day the policy is issued and never raised afterwards.
        Every row has a button that puts you through to a licensed agent who can price that band
        for your state and your health.
      </p>
    </div>
  </div>
</section>


<!-- =====================================================================
     THE CHART. First real section on the page, per T2. Three columns
     including the row header, with the click-to-call inside the age cell.
     ================================================================== -->
<section class="pb-14 md:pb-16" id="chart">
  <div class="container-ax">
    <div class="reveal max-w-3xl">
      {C.rates_flag("premiums")}
    </div>

    {C.rate_chart(
        panels_id="fe-cost-full",
        cols=COVERAGE_COLS,
        rows=AGE_BANDS,
        toggles=[("Show premiums for", "fec-sex",
                  [("female", "Female"), ("male", "Male")], None)],
        caption="Monthly premium by age band and coverage amount.",
        row_cta="call",
        cta_location="fe_cost_rate_row",
        min_width="26rem",
        top_margin="mt-6",
        aside="Non tobacco, level benefit. Tobacco rates are higher, and a graded or guaranteed "
              "acceptance policy is higher again.")}

    <p class="reveal mt-6 text-slate max-w-3xl">
      Amounts between and above these columns are written every day. Ten and twenty five thousand
      dollars are shown because that is the band most policies in this category fall into, not
      because they are the only options. Below about five thousand dollars few carriers will
      write at all, and above about fifty thousand you are usually better served by a standard
      <a class="link" href="/whole-life-insurance/">whole life insurance</a> policy, which is the
      same contract priced for a larger market.
    </p>
  </div>
</section>


<!-- =====================================================================
     WHAT MOVES THE PRICE. Static cards: no bento cascade on an fe page.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2">What actually moves the price</h2>
      <p class="reveal mt-5 text-slate">
        In rough order of size. The first two are worth more than everything below them put
        together, which is why the chart is built around them.
      </p>
    </div>

    <div class="mt-10 grid md:grid-cols-2 gap-6">
      <div class="card">
        <h3 class="text-h4">Your age when the policy is issued</h3>
        <p class="mt-3 text-slate">
          Not your age when you decide, your age when the carrier issues the policy. It is the
          largest single factor, and it is the only one on this list that gets worse while you
          think about it.
        </p>
      </div>
      <div class="card">
        <h3 class="text-h4">How much coverage you buy</h3>
        <p class="mt-3 text-slate">
          The premium tracks the face amount closely on this product, more closely than it does on
          a large underwritten policy. Halving the coverage roughly halves the payment.
        </p>
      </div>
      <div class="card">
        <h3 class="text-h4">Tobacco and nicotine use</h3>
        <p class="mt-3 text-slate">
          A meaningful step up for the same coverage, carried for life rather than for a term.
          Most carriers look at the last twelve months, and they define tobacco more widely than
          people expect.
        </p>
      </div>
      <div class="card">
        <h3 class="text-h4">Your health answers</h3>
        <p class="mt-3 text-slate">
          They decide which of three things you are offered: a level benefit policy that pays in
          full from day one, a graded policy that pays partially at first, or a guaranteed
          acceptance policy with a full waiting period. The gap between the first and the last is
          large.
        </p>
      </div>
      <div class="card">
        <h3 class="text-h4">Which carrier writes you</h3>
        <p class="mt-3 text-slate">
          Carriers disagree sharply about the same medication and the same diagnosis. Two quotes
          for one person on one day can land a long way apart, and neither company is being
          unreasonable.
        </p>
      </div>
      <div class="card">
        <h3 class="text-h4">How you pay</h3>
        <p class="mt-3 text-slate">
          Monthly payment usually carries a modal factor, so twelve monthly payments cost a little
          more than one annual one. Small next to the items above, and it is real money you can
          keep by asking.
        </p>
      </div>
    </div>
  </div>
</section>


{FE.call_band(
    "Have your band priced properly, in about fifteen minutes",
    "Tell a licensed agent your age, your state, and what you take. You will hear which carriers "
    "would write you, what the premium is, and whether any waiting period applies. No application "
    "and no obligation.",
    "fe_cost_band_1")}


<!-- =====================================================================
     HOW TO LOWER A QUOTED PRICE. T2. Legitimate levers only.
     ================================================================== -->
{C.prose("How to bring a quoted price down", LOWER,
         intro="All of these are legitimate, and the first one is worth more than the other four "
               "together.",
         media=C.figure("fe-quiet", C.MEDIA_SIZES))}


<!-- =====================================================================
     WHY OUR NUMBERS MAY DIFFER FROM YOUR QUOTE. T2. The honesty section
     that stops a cost chart being read as a promise.
     ================================================================== -->
<section class="section band-navy on-navy">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2 text-white">Why your quote may not match this chart</h2>
      <p class="reveal mt-5 text-white/85">
        A cost chart is an illustration of shape. It shows how premiums move between ages and
        coverage amounts. It cannot show what a carrier will decide about you, and any chart that
        claims otherwise is selling you a number it does not have.
      </p>
    </div>
    <div class="mt-10 grid md:grid-cols-3 gap-6">
      <div class="reveal">
        <h3 class="text-h4 text-white">A chart assumes an acceptance</h3>
        <p class="mt-3 text-white/85">
          Usually a level benefit policy for someone in reasonable health. A graded or guaranteed
          acceptance policy is priced above this, and that is a normal outcome rather than a bad
          one.
        </p>
      </div>
      <div class="reveal">
        <h3 class="text-h4 text-white">Carriers differ by state</h3>
        <p class="mt-3 text-white/85">
          Product availability, riders, minimum face amounts, and pricing all vary. The carrier
          that is cheapest in one state may not write in yours at all.
        </p>
      </div>
      <div class="reveal">
        <h3 class="text-h4 text-white">Your medications are read together</h3>
        <p class="mt-3 text-white/85">
          Not one at a time. A combination can move you between offers even when no single item on
          the list would. A chart cannot know any of it.
        </p>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     THE ASK. Phone first, short form secondary.
     ================================================================== -->
<section class="section band-surface" id="talk">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">

      <div class="lg:col-span-6">
        <h2 class="reveal text-h2">Get your own number</h2>
        <p class="reveal mt-5 text-slate">
          A chart cell is a shape. A quote is a price. We will ask your age, your state, and the
          health questions the carriers ask, then tell you which companies would write you, what
          it costs, and whether the policy pays in full from day one.
        </p>
        <div class="reveal mt-8">
          {C.phone_link("fe_cost_footer", "btn btn-call btn-xl", "Call " + C.PHONE_DISPLAY, 26)}
          <p class="mt-3 text-sm text-muted">{C.HOURS}</p>
        </div>
      </div>

      <div class="lg:col-span-5 lg:col-start-8">
        <div class="reveal panel">
          {FE.callback_form("fec", "fe_cost_callback")}
        </div>
      </div>
    </div>
  </div>
</section>


{C.spoke_module(
    "More about final expense insurance",
    "The pages people read either side of this one.",
    [("/final-expense-insurance/burial-insurance/", "Burial insurance",
      "The same product under the name people search for most."),
     ("/final-expense-insurance/what-is-final-expense-insurance/", "What it is",
      "The plain definition, with the fine print left in."),
     ("/final-expense-insurance/for-seniors/", "Final expense after 50",
      "What changes at 70 and at 80, and what does not."),
     ("/final-expense-insurance/cremation-insurance/", "Cremation insurance",
      "What cremation costs, and how much coverage fits."),
     ("/final-expense-insurance/funeral-insurance/", "Funeral insurance",
      "The same contract, and how it differs from a pre-paid plan."),
     ("/final-expense-insurance/quotes/", "Get a quote",
      "What we need from you, and how fast an answer comes back.")])}


{C.faq_section("Questions about the cost", FAQ, "fe-cost-faq", size=24)}


{C.byline_section()}
"""
