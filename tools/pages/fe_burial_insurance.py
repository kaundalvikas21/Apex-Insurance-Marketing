# -*- coding: utf-8 -*-
"""BURIAL INSURANCE. Spec P1, template T4. PHONE FIRST.

*** CONSOLIDATION FLAG. See the comment at the top of body(). ***

This is the fourth naming variant for one product, and the one people actually
search for most, which is why it is a P1 page rather than a P2 one and why six
built pages point at it. The overlap with the hub, with funeral insurance, and
with cremation insurance is real and was flagged in the brief rather than
discovered later.

So it is built consolidation ready, the same way funeral insurance is:

  * One distinctive section that exists nowhere else in the silo, the cemetery
    costs that a burial carries and a cremation does not, and who each of them
    is actually paid to. If this page is ever folded, that section is what
    moves; everything else is already covered somewhere.
  * No rate table. Cost routes to /final-expense-insurance/cost/.
  * No invented funeral or burial cost figures. We do not publish an average,
    and the page says why rather than borrowing one from a survey we cannot
    cite. Same rule as the funeral insurance page.

Senior accessibility rules apply in full (html.fe), tables capped at three
columns including the row header.
"""
import chrome as C
import final_expense as FE

PATH = "/final-expense-insurance/burial-insurance/"
OUT = "final-expense-insurance/burial-insurance/index.html"
ACTIVE = "/final-expense-insurance/"
SILO = "final-expense"
HTML_CLASS = "fe"
TITLE = "Burial Insurance: What It Covers and What It Costs | Apex"
OG_TITLE = "Burial insurance, explained"
DESC = ("Burial insurance is a small whole life policy that pays your family cash for a burial "
        "and the bills that follow. What it covers, what a burial costs that a cremation does "
        "not, and how to size it.")

TRAIL = [("Home", "/"), ("Final Expense Insurance", "/final-expense-insurance/"),
         ("Burial insurance", None)]

# Row header plus two columns: the senior table cap is three columns total.
# A behaviour table, not a price table, so no $-- cells and no rate flag.
BURIAL_COSTS = [
    ("Basic services fee",
     "The funeral home",
     "Charged on every arrangement, burial or cremation. It is the one line nobody avoids."),
    ("Transfer, preparation, and viewing",
     "The funeral home",
     "Embalming is normally expected for an open casket viewing and is often skipped otherwise."),
    ("Casket",
     "The funeral home, or an outside seller",
     "You are allowed to buy one elsewhere and the funeral home must accept it without a fee."),
    ("The plot or grave space",
     "The cemetery",
     "A separate business from the funeral home, with its own price list and its own rules."),
    ("Opening and closing the grave",
     "The cemetery",
     "Frequently the line people have never heard of. It is charged on the day of the burial."),
    ("Outer burial container or vault",
     "The cemetery, usually",
     "Not required by law in most places, but required by most cemeteries as a condition of the "
     "plot."),
    ("Headstone or marker, and its setting fee",
     "A monument dealer and the cemetery",
     "Often bought months later, which is why it is the item most likely to be underfunded."),
]

FAQ = [
    ("What is burial insurance?",
     "It is a small whole life insurance policy bought to cover a burial and the bills that "
     "follow it. It is the same product sold under the names final expense insurance and funeral "
     "insurance. There is no medical exam, only health questions, the premium never rises, and "
     "the coverage does not expire. The money is paid in cash to the person you name, so they can "
     "use it for the funeral home, the cemetery, or anything else."),
    ("How much burial insurance do I need?",
     "Enough to cover what your family would actually face, which depends on your state, on the "
     "cemetery, and on what you would want. We do not publish an average, because averages here "
     "are national survey figures that describe no particular burial and routinely leave the "
     "cemetery out entirely. Call one funeral home and one cemetery near you, ask each for its "
     "price list, add the two together, and insure that plus a margin for the bills that arrive "
     "afterwards."),
    ("Is burial insurance different from final expense insurance?",
     "No. They are the same contract sold under different names, and the name usually reflects "
     "how the policy was marketed rather than anything in the paperwork. If an agent tells you "
     "burial insurance is a distinct product with different rules, ask them to show you where in "
     "the policy that difference appears."),
    ("Does burial insurance pay the funeral home directly?",
     "Only if you arrange for it to. By default the benefit is paid in cash to the beneficiary "
     "you name, and they decide what to do with it. Some people assign part of the benefit to a "
     "funeral home so the bill is settled without the family having to advance the money. That is "
     "a choice you make, not something the policy does on its own."),
    ("Can I be turned down for burial insurance?",
     "You can be declined for a policy that pays the full benefit from day one, and in that case "
     "a graded policy or a guaranteed acceptance policy is normally still available. Outright "
     "decline from every option is uncommon within the issue ages. Which carriers will take you "
     "depends on your health answers, and they disagree with each other more than people expect."),
    ("Should I buy the plot now instead?",
     "Buying a plot in advance is a reasonable thing to do and it is not an alternative to "
     "insurance, because the plot is only one line of the bill. The two work together: the "
     "cemetery holds the space, and the policy pays for everything else on the day. If you have "
     "already bought a plot, say so when we quote you, because it changes the amount you need "
     "rather than whether you need any."),
]


SIZING = """<p class="reveal text-slate">
        There is a way to do this that does not involve trusting a number off the internet, and it
        takes about twenty minutes on the telephone.
      </p>
      <ul class="mt-6 grid gap-5 text-slate">
        <li class="reveal">Call one funeral home near you and ask for their general price list.
            They are required to give it to you, over the phone or in writing, and you do not have
            to explain why you want it.</li>
        <li class="reveal">Call the cemetery separately and ask for the price of a plot, the
            opening and closing fee, and whether a vault is required. This is the half people
            forget, and it is a different business with a different bill.</li>
        <li class="reveal">Add a marker, if you want one. Then add a margin for the bills that
            arrive after the funeral: a final month of rent or utilities, outstanding medical
            accounts, and travel for family.</li>
        <li class="reveal">Insure that total. If it is more than you can comfortably afford the
            premium on, insure what you can carry rather than stretching. A smaller policy that
            stays in force beats a larger one that lapses at eighty two.</li>
      </ul>
      <p class="reveal mt-6 text-slate">
        Two numbers you gathered yourself beat any average, because they are the numbers your
        family will actually be handed.
      </p>"""


COST = """<p class="reveal text-slate">
        Four things decide the premium: your age when the policy is issued, the amount of
        coverage, whether you use tobacco, and your answers to the health questions. It is fixed
        for life from that point, so the age in that list is the age you buy at, not the age you
        reach.
      </p>
      <p class="reveal mt-5 text-slate">
        The full picture by age lives on one page and is kept current in one place:
        <a class="link" href="/final-expense-insurance/cost/">what final expense insurance
        costs</a>.
      </p>
      <p class="reveal mt-5 text-slate">
        If you have been told you need a waiting period, or you want to know whether you can avoid
        one, read
        <a class="link" href="/final-expense-insurance/no-waiting-period/">burial insurance with no
        waiting period</a> before you apply anywhere. It is the single most expensive thing to get
        wrong on this product.
      </p>"""


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    cost_rows = "\n          ".join(
        '<tr><th scope="row">%s</th><td>%s</td><td>%s</td></tr>' % r for r in BURIAL_COSTS)

    hero_cta = """<div class="reveal mt-8">
        %s
        <p class="mt-3 text-sm text-muted">%s</p>
      </div>""" % (C.phone_link("fe_burial_hero", "btn btn-call btn-xl",
                                "Call " + C.PHONE_DISPLAY, 26), C.HOURS)

    return f"""
<!-- =====================================================================
     [CONSOLIDATION READY - spec P1 overlap flag]

     Burial insurance, funeral insurance, and final expense insurance are
     three names for one contract. This page carries the name with the most
     search demand, which is why it is P1 and why six built pages link here.

     Before investing further, confirm whether this query returns a distinct
     result set from the hub and from
     /final-expense-insurance/funeral-insurance/. If it does not, the
     intended consolidation is: keep the hub, move the cemetery cost table
     below into it as a section, and 301 this path to
     /final-expense-insurance/#costs.

     Do NOT delete the page to resolve the overlap while seven built pages
     still link to it.
     ================================================================== -->

{C.page_hero(
    TRAIL,
    "Burial Insurance",
    'Burial insurance is a small whole life policy that pays your family a cash sum for a burial '
    'and the bills that follow it. It is the same product as funeral insurance and as '
    '<a class="link" href="/final-expense-insurance/">final expense insurance</a>: three names, '
    'one contract, no medical exam. The thing worth knowing before you read further is that a '
    'burial is billed by two separate businesses, the funeral home and the cemetery, and most '
    'people size a policy having only asked one of them.',
    extra=hero_cta, glow=False,
    media=C.figure("fe-letters", C.MEDIA_SIZES, eager=True))}


<!-- =====================================================================
     THE DISTINCTIVE SECTION. What a burial is billed for and by whom. This
     is the material that would survive a consolidation of this page, and
     it exists nowhere else in the silo.

     A behaviour table, not a price table: MASTER.md section 6 rule 6, so
     no $-- cells and no rate flag. Three columns including the row header.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2">What a burial is billed for, and by whom</h2>
      <p class="reveal mt-5 text-slate">
        This is the part that separates a burial from a cremation, and it is the reason a burial
        policy is normally sized higher. The cemetery is not part of the funeral home. It sends
        its own bill, on its own terms, and nobody warns you about it in advance.
      </p>
      <div class="reveal mt-6">
        {C.flag("We do not publish an average burial cost on this site. Figures quoted in this "
                "category are national survey averages that describe no particular burial, and "
                "most of them leave the cemetery out altogether. Ask one funeral home and one "
                "cemetery near you for their price lists and use those numbers instead.",
                "NO AVERAGE PUBLISHED, ON PURPOSE")}
      </div>
    </div>

    <div class="reveal mt-8 table-scroll table-signature">
      <table class="compare-table" style="min-width:0">
        <caption class="sr-only">
          What each part of a burial is charged for and which business is paid for it.
        </caption>
        <thead>
          <tr>
            <th scope="col">Item</th>
            <th scope="col">Who is paid</th>
            <th scope="col">Worth knowing</th>
          </tr>
        </thead>
        <tbody>
          {cost_rows}
        </tbody>
      </table>
    </div>

    <p class="reveal mt-6 text-slate max-w-3xl">
      If a cremation is what you would rather have, several of these lines disappear and the total
      is normally a good deal lower. That decision changes the amount you should insure, and it is
      covered on
      <a class="link" href="/final-expense-insurance/cremation-insurance/">cremation
      insurance</a>.
    </p>
  </div>
</section>


{FE.call_band(
    "Ask a licensed agent what this would cost you",
    "About fifteen minutes on the phone. You will hear what you qualify for, what it costs, and "
    "whether there is a waiting period. There is no application and no obligation.",
    "fe_burial_band_1")}


<!-- =====================================================================
     HOW TO SIZE IT. The method, rather than a number we cannot stand up.
     ================================================================== -->
{C.prose("How to work out how much you need", SIZING,
         intro="Two phone calls give you a real figure for your town. An average gives you a "
               "figure for nowhere.",
         media=C.figure("fe-hands", C.MEDIA_SIZES))}


<!-- =====================================================================
     WHAT IT DOES NOT DO. Static cells: no .reveal cascade on an fe page.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2">What burial insurance does not do</h2>
      <p class="reveal mt-5 text-slate">
        Three limits worth hearing before you buy rather than after.
      </p>
    </div>

    <div class="mt-10 grid md:grid-cols-3 gap-6">
      <div class="card">
        <h3 class="text-h4">It does not rise with prices</h3>
        <p class="mt-3 text-slate">
          The benefit is a fixed amount. If costs rise over twenty years, the policy pays what it
          says and no more. Some carriers offer an increasing benefit rider at extra cost, and it
          is worth asking what that costs as a line item.
        </p>
      </div>
      <div class="card">
        <h3 class="text-h4">It does not reserve anything</h3>
        <p class="mt-3 text-slate">
          It is not a plot, a casket, or a funeral. It is money. If you want a specific space in a
          specific cemetery held for you, that is bought from the cemetery, and the policy pays
          for everything around it.
        </p>
      </div>
      <div class="card">
        <h3 class="text-h4">It does not pay instantly in every case</h3>
        <p class="mt-3 text-slate">
          A claim on a policy in force for more than two years is normally paid quickly. Inside
          the first two years the carrier can review the application, and a policy sold with a
          waiting period pays differently again.
        </p>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     COST. Routed rather than duplicated.
     ================================================================== -->
{C.prose("What it costs", COST,
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
          would write you and what the premium would be. If you have already bought a plot, say
          so, because it changes the amount you need rather than whether you need any.
        </p>
        <div class="reveal mt-8">
          {C.phone_link("fe_burial_footer", "btn btn-call btn-xl", "Call " + C.PHONE_DISPLAY, 26)}
          <p class="mt-3 text-sm text-muted">{C.HOURS}</p>
        </div>
      </div>

      <div class="lg:col-span-5 lg:col-start-8">
        <div class="reveal panel">
          {FE.callback_form("febu", "fe_burial_callback")}
        </div>
      </div>
    </div>
  </div>
</section>


{C.spoke_module(
    "More about final expense insurance",
    "The same product, and the pages this one deliberately defers to.",
    [("/final-expense-insurance/what-is-final-expense-insurance/", "What it is",
      "The plain definition, with the fine print left in."),
     ("/final-expense-insurance/funeral-insurance/", "Funeral insurance",
      "The same contract, and how it differs from a pre-paid plan."),
     ("/final-expense-insurance/for-seniors/", "Final expense after 50",
      "What changes at 70 and at 80, and what does not."),
     ("/final-expense-insurance/quotes/", "Get a quote",
      "What we need from you, and how fast an answer comes back."),
     ("/final-expense-insurance/for-parents/", "Coverage for a parent",
      "Buying a policy on a parent, and the consent it needs.")])}


{C.faq_section("Questions about burial insurance", FAQ, "fe-burial-faq", size=24)}


{C.byline_section()}
"""
