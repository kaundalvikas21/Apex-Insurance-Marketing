# -*- coding: utf-8 -*-
"""FUNERAL INSURANCE. Spec P2, template T4, built LEAN. PHONE FIRST.

[PENDING SERP OVERLAP TEST] Spec s10 test 3. This is the third naming variant
for one product, after final expense and burial insurance. The likeliest
outcome per the spec is that it folds into the final expense hub as a section
and this path is redirected, so the page is built to be consolidation ready:

  * One distinctive section that does not exist anywhere else in the silo, the
    comparison against a pre-need plan bought at a funeral home. If this page
    is folded, that section is what moves; everything else is already covered.
  * No rate table. Cost routes to /final-expense-insurance/cost/.
  * No invented funeral cost figures. We do not publish an average, and the
    page says why rather than borrowing one from a survey we cannot cite.

Senior accessibility rules apply in full (html.fe), tables capped at three
columns including the row header.
"""
import chrome as C
import final_expense as FE

PATH = "/final-expense-insurance/funeral-insurance/"
OUT = "final-expense-insurance/funeral-insurance/index.html"
ACTIVE = "/final-expense-insurance/"
SILO = "final-expense"
HTML_CLASS = "fe"
TITLE = "Funeral Insurance: What It Covers and What It Costs | Apex"
OG_TITLE = "Funeral insurance, explained"
DESC = ("Funeral insurance is a small whole life policy that pays your family cash to cover a "
        "funeral. What it covers, how it differs from a pre-paid plan, and what decides the cost.")

TRAIL = [("Home", "/"), ("Final Expense Insurance", "/final-expense-insurance/"),
         ("Funeral insurance", None)]

# Row header plus two columns: the senior table cap is three columns total.
VERSUS = [
    ("Who holds the money",
     "An insurance carrier, regulated as an insurer in your state.",
     "The funeral home, or a trust or insurance policy it arranges."),
    ("What your family receives",
     "Cash, paid to the person you name. They decide how it is spent.",
     "Goods and services from that funeral home, as listed in the contract."),
    ("If you move away",
     "Nothing changes. The policy follows you and pays anywhere.",
     "Depends entirely on the contract. Transfers are often possible and often cost something."),
    ("If the funeral costs less than expected",
     "Your family keeps the difference.",
     "Usually nothing is returned. The plan buys what it lists."),
    ("If prices rise before then",
     "The benefit is a fixed amount and does not rise with prices.",
     "A guaranteed plan locks the price of the listed items. This is its real advantage."),
    ("If the funeral home closes or is sold",
     "Not affected.",
     "Depends on how the money was held and on your state's rules. Ask before you sign."),
]

FAQ = [
    ("What is funeral insurance?",
     "It is a small whole life insurance policy bought to cover a funeral and the bills that "
     "follow. It is the same product sold under the names final expense insurance and burial "
     "insurance. There is no medical exam, only health questions, the premium never rises, and "
     "the coverage does not expire. The money is paid in cash to the person you name, not to a "
     "funeral home."),
    ("How much funeral insurance do I need?",
     "Enough to cover what your family would actually face, which depends on your state, on "
     "whether you want a burial or a cremation, and on what you would want included. We do not "
     "publish an average figure, because averages in this category are usually borrowed from "
     "surveys that do not describe any particular funeral. A better approach is to call two "
     "funeral homes near you and ask for their general price list, which they are required to "
     "give you, then insure that number plus a margin for the bills that arrive afterwards."),
    ("Is funeral insurance worth it?",
     "It is worth it if your family would otherwise have to find the money quickly, from savings "
     "or from a credit card, at the worst possible moment. It is not worth it if you already have "
     "liquid savings set aside for this and the discipline to leave them alone, or if you already "
     "hold permanent life insurance that covers it. The honest test is whether the money would "
     "actually be there, in cash, within a week."),
    ("Can I be turned down for funeral insurance?",
     "You can be declined for a policy that pays the full benefit from day one, and in that case "
     "a graded policy or a guaranteed acceptance policy is normally still available. Outright "
     "decline from every option is uncommon within the issue ages. Which carriers will take you "
     "depends on your health answers, and they disagree with each other more than people expect."),
]


FUNERAL_COST = """<p class="reveal text-slate">
        Four things decide the premium: your age when the policy is issued, the amount of
        coverage, whether you use tobacco, and your answers to the health questions. It is fixed
        for life from that point, so the age in that list is the age you buy at, not the age you
        reach.
      </p>
      <p class="reveal mt-5 text-slate">
        The full picture by age lives on one page and is kept current in one place:
        <a class="link" href="/final-expense-insurance/cost/">final expense insurance cost</a>.
      </p>
      <p class="reveal mt-5 text-slate">
        If you have been told you need a waiting period, or you want to know whether you can
        avoid one, read
        <a class="link" href="/final-expense-insurance/no-waiting-period/">burial insurance with
        no waiting period</a> before you apply anywhere.
      </p>"""


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    versus_rows = "\n          ".join(
        '<tr><th scope="row">%s</th><td>%s</td><td>%s</td></tr>' % r for r in VERSUS)

    hero_cta = """<div class="reveal mt-8">
        %s
        <p class="mt-3 text-sm text-muted">%s</p>
      </div>""" % (C.phone_link("fe_funeral_hero", "btn btn-call btn-xl",
                                "Call " + C.PHONE_DISPLAY, 26), C.HOURS)

    return f"""
<!-- =====================================================================
     [PENDING SERP OVERLAP TEST] Spec section 10, test 3.
     Funeral insurance, burial insurance, and final expense insurance are
     three names for one product. Before investing further here, confirm
     whether this query returns a distinct result set from the hub and
     from /final-expense-insurance/burial-insurance/. If it does not, fold
     this page into the hub as a section, keep the pre-need comparison
     table below, and 301 this path.
     ================================================================== -->

{C.page_hero(
    TRAIL,
    "Funeral Insurance",
    'Funeral insurance is a small whole life policy that pays your family a cash sum to cover a '
    'funeral and the bills that follow. It is the same product as burial insurance and as '
    '<a class="link" href="/final-expense-insurance/">final expense insurance</a>: three names, '
    'one contract, no medical exam. The one thing worth knowing before you read further is that '
    'it is insurance rather than a pre-paid funeral plan, and those two are genuinely different '
    'things.',
    extra=hero_cta, glow=False)}


<!-- =====================================================================
     WHAT IT COVERS. Components, not prices. We do not publish an average
     funeral cost, and the page says so rather than borrowing one.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">What the money is used for</h2>
        <p class="reveal mt-5 text-slate">
          The benefit is paid in cash to the person you name, so it can be used for anything. In
          practice it goes on some combination of these.
        </p>
        <div class="reveal mt-6">
          {C.flag("We do not publish an average funeral cost on this site. Figures quoted in this "
                  "category are usually national survey averages that describe no particular "
                  "funeral, and they vary enormously by state and by what is chosen. Ask two "
                  "funeral homes near you for their general price list, which they are required "
                  "to provide, and use those numbers.", "NO AVERAGE PUBLISHED, ON PURPOSE")}
        </div>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <ul class="grid gap-5 text-slate">
          <li class="reveal">The funeral director's basic services fee, which is charged on every
              arrangement regardless of what else is chosen.</li>
          <li class="reveal">Transfer of the body, embalming or refrigeration, and use of the
              facilities for a viewing or a service.</li>
          <li class="reveal">A casket or an urn, and a burial vault where the cemetery requires
              one.</li>
          <li class="reveal">Cemetery costs, which are separate from the funeral home: the plot,
              opening and closing the grave, and a marker.</li>
          <li class="reveal">Cremation fees, if that is the choice, which are normally lower than
              burial but are not nothing.</li>
          <li class="reveal">The bills that arrive afterwards: outstanding medical accounts, a
              final month of rent or utilities, travel for family, and probate costs.</li>
        </ul>
        <p class="reveal mt-6 text-slate">
          That last line is the one people leave out, and it is often a meaningful share of the
          total.
        </p>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     THE DISTINCTIVE SECTION. Insurance against a pre-need plan. This is
     the material that would survive a consolidation of this page.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2">Funeral insurance against a pre-paid plan</h2>
      <p class="reveal mt-5 text-slate">
        A pre-need plan is bought from a funeral home and buys a specific funeral from that funeral
        home. Funeral insurance is bought from an insurance carrier and pays your family cash. Both
        are legitimate. They fail in different ways, and that is what the table is for.
      </p>
    </div>

    <div class="reveal mt-8 table-scroll table-signature">
      <table class="compare-table" style="min-width:0">
        <caption class="sr-only">
          Funeral insurance compared with a pre-need plan bought from a funeral home.
        </caption>
        <thead>
          <tr>
            <th scope="col"><span class="sr-only">Feature</span></th>
            <th scope="col">Funeral insurance</th>
            <th scope="col">Pre-paid plan</th>
          </tr>
        </thead>
        <tbody>
          {versus_rows}
        </tbody>
      </table>
    </div>

    <p class="reveal mt-6 text-slate max-w-3xl">
      The honest summary: a pre-paid plan can lock a price, which insurance cannot, and insurance
      gives your family cash and freedom, which a plan does not. Some people sensibly do both, and
      hold a smaller policy alongside a plan. We sell one of these and not the other, so treat that
      summary accordingly and ask the funeral home the same questions you would ask us.
    </p>
  </div>
</section>


{FE.call_band(
    "Ask a licensed agent what this would cost you",
    "About fifteen minutes on the phone. You will hear what you qualify for, what it costs, and "
    "whether there is a waiting period. There is no application and no obligation.",
    "fe_funeral_band_1")}


<!-- =====================================================================
     COST. Routed rather than duplicated: this page is lean by design.
     ================================================================== -->
{C.prose("What it costs", FUNERAL_COST,
         intro="What the premium depends on, and where the figures by age are kept.")}


<!-- =====================================================================
     THE ASK. Phone first, short form secondary.
     ================================================================== -->
<section class="section band-surface" id="talk">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">

      <div class="lg:col-span-6">
        <h2 class="reveal text-h2">Talk it through with a licensed agent</h2>
        <p class="reveal mt-5 text-slate">
          We will ask your age, your state, and the health questions, then tell you which carriers
          would write you and what the premium would be. If you already have a pre-paid plan, say
          so, because it changes what you need rather than ruling this out.
        </p>
        <div class="reveal mt-8">
          {C.phone_link("fe_funeral_footer", "btn btn-call btn-xl", "Call " + C.PHONE_DISPLAY, 26)}
          <p class="mt-3 text-sm text-muted">{C.HOURS}</p>
        </div>
      </div>

      <div class="lg:col-span-5 lg:col-start-8">
        <div class="reveal panel">
          {FE.callback_form("fefu", "fe_funeral_callback")}
        </div>
      </div>
    </div>
  </div>
</section>


{C.spoke_module(
    "More about final expense insurance",
    "The same product, and the pages this one deliberately defers to.",
    [("/final-expense-insurance/for-seniors/", "Final expense after 50",
      "What changes at 70 and at 80, and what does not."),
     ("/final-expense-insurance/burial-insurance/", "Burial insurance",
      "The same product under the name people search for most."),
     ("/final-expense-insurance/what-is-final-expense-insurance/", "What it is",
      "The plain definition, with the fine print left in."),
     ("/final-expense-insurance/cremation-insurance/", "Cremation insurance",
      "What cremation costs, and how much coverage fits."),
     ("/final-expense-insurance/quotes/", "Get a quote",
      "What we need from you, and how fast an answer comes back."),
     ("/final-expense-insurance/for-parents/", "Coverage for a parent",
      "Buying a policy on a parent, and the consent it needs.")])}


{C.faq_section("Questions about funeral insurance", FAQ, "fe-funeral-faq", size=24)}


{C.byline_section()}
"""
