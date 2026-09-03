# -*- coding: utf-8 -*-
"""WHOLE LIFE CALCULATOR. Spec P2, template T3. No email gate.

WHAT THIS CALCULATOR HONESTLY IS. The page title carries "premium and cash
value", and this calculator computes neither, on purpose. A premium needs a
carrier rate card and a health class, and a cash value column needs a carrier
illustration. We have neither, and inventing them would be the same fabrication
as printing a rate (MASTER.md s7). So the tool sizes the PERMANENT NEED, the
page says plainly why the other two numbers cannot be produced in a browser,
and the request for a real illustration is the CTA.

ENGINE REUSE. site.js section 10 already implements exactly this arithmetic:
two multiplied terms plus a flat term, minus existing coverage, rounded UP to a
coverage ladder. Rather than write a second calculator, this page reuses that
one with a different ladder (data-calc-ladder, added for this page) and maps the
roles to whole life's questions:

    debt      -> funeral, final bills, and debts left behind   (flat term)
    children  -> people you want to leave something to         (count)
    perchild  -> amount for each of them                       (each)
    existing  -> permanent coverage already in force           (subtracted)

The `income` and `years` roles are simply absent from the markup. num() returns
0 for a missing field, so their product drops out of the sum.

# ponytail: role names are site.js's, not this page's. The visible labels carry
# the meaning. If a third silo ever needs a genuinely different formula, that is
# the point to make the engine data driven, not before.
"""
import chrome as C
import term_calculator as T
import whole
from term_calculator import money

PATH = "/whole-life-insurance/calculator/"
OUT = "whole-life-insurance/calculator/index.html"
ACTIVE = "/whole-life-insurance/"
SILO = "whole-life"
TITLE = "Whole Life Insurance Calculator | Premium & Cash Value | Apex"
OG_TITLE = "Whole life insurance calculator"
DESC = ("Work out how much permanent coverage you need, with the method shown. No email required, "
        "and an honest account of why a premium and a cash value cannot be calculated in a browser.")

TRAIL = [("Home", "/"), ("Whole Life Insurance", "/whole-life-insurance/"),
         ("Calculator", None)]

# Whole life's coverage ladder, matching the options on whole.quote_form()'s
# coverage select. A recommendation that is not on this list would silently
# blank the field when the prefill assigns it.
LADDER = [25000, 50000, 100000, 250000, 500000]

# The worked example, rendered into the HTML with its arithmetic already done so
# the page is complete and correct with JavaScript off.
EX_FINAL = 25000       # funeral, final medical and estate bills, and debts
EX_PEOPLE, EX_EACH = 2, 25000
EX_EXISTING = 10000


def _derive(final, people, each, existing):
    legacy = people * each
    raw = final + legacy - existing
    rounded = next((rung for rung in LADDER if rung >= raw), LADDER[-1]) if raw > 0 else 0
    return legacy, raw, rounded


EX_LEGACY, EX_RAW, EX_ROUNDED = _derive(EX_FINAL, EX_PEOPLE, EX_EACH, EX_EXISTING)


def _check():
    """The one runnable check. It guards the JS-off worked example against a bad
    edit, and guards the recommendation against falling off the quote form's
    coverage ladder, which would silently blank the field."""
    assert EX_LEGACY == 50000, EX_LEGACY
    assert EX_RAW == 65000, EX_RAW
    assert EX_ROUNDED in LADDER, EX_ROUNDED
    assert EX_ROUNDED == 100000, EX_ROUNDED
    # Rounding is UP, never down.
    assert EX_ROUNDED >= EX_RAW
    # Already covered means no CTA and no recommendation, not the bottom rung.
    assert _derive(5000, 0, 0, 90000)[2] == 0
    # Above the top rung, the honest answer is the top rung, not zero.
    assert _derive(900000, 0, 0, 0)[2] == LADDER[-1]
    # The ladder written into the markup must be the one this module derives on.
    assert LADDER_ATTR == ",".join(str(n) for n in LADDER)


LADDER_ATTR = ",".join(str(n) for n in LADDER)
_check()


def schema():
    return [C.org_schema(),
            C.breadcrumbs(TRAIL),
            {
                "@context": "https://schema.org",
                "@type": "SoftwareApplication",
                "name": "Whole life insurance coverage calculator",
                "applicationCategory": "FinanceApplication",
                "operatingSystem": "Any modern web browser",
                "url": C.DOMAIN + PATH,
                "description": ("Calculates how much permanent life insurance a household needs "
                                "from final expenses, debts, intended bequests, and existing "
                                "permanent coverage. Free, with no registration."),
                "publisher": {"@id": C.DOMAIN + "/#organization"},
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
            },
            C.person_schema(PATH)]


def body():
    return f"""
<section class="pt-6 pb-10 glow">
  <div class="container-ax">
    {C.crumbs(TRAIL)}

    <div class="mt-8 max-w-3xl">
      <h1 class="reveal text-h1">Whole Life Insurance Calculator</h1>
      <p class="reveal mt-5 text-lead text-slate">
        Change the four figures below and the recommendation updates as you type. There is no email
        wall and nothing is submitted: the calculation happens in your browser and is not sent
        anywhere. It sizes the permanent need that
        <a class="link" href="/whole-life-insurance/">whole life insurance</a> exists to cover,
        which is the number a carrier illustration has to start from.
      </p>
    </div>
  </div>
</section>


<!-- =====================================================================
     THE CALCULATOR. T3: interactive, no email gate.
     The inputs sit in a <div>, never inside the quote form below. Inside a
     form, collect() would validate them and FormData would post the
     visitor's finances to the CRM.
     ================================================================== -->
<section class="pb-14 md:pb-16">
  <div class="container-ax">
    <div data-calc="whole_life_permanent_need" data-calc-ladder="{LADDER_ATTR}">
      <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">

        <div class="lg:col-span-5">
          <div class="reveal panel">
            <h2 class="text-h3 !font-display !font-semibold">Your numbers</h2>
            <p class="mt-2 text-sm text-muted">
              Prefilled with an example so you can see how it works. Round figures are fine.
            </p>
            <div class="mt-6">
              {T.field("wlcalc-final", "debt", "Funeral, final bills, and debts",
                       "What would still have to be paid after you die.", EX_FINAL)}
              {T.picker("wlcalc-people", "children", "People you want to leave something to",
                        "Count anyone you intend to receive a share.",
                        [(str(n), str(n)) for n in range(0, 7)], str(EX_PEOPLE))}
              {T.picker("wlcalc-each", "perchild", "Amount for each of them",
                        "A bequest, not income replacement. Pick the closest.",
                        [("0", "Nothing"), ("10000", "$10,000"), ("25000", "$25,000"),
                         ("50000", "$50,000"), ("100000", "$100,000")], str(EX_EACH))}
              {T.field("wlcalc-existing", "existing", "Permanent coverage you already have",
                       "Whole life or final expense policies only. Not term.", EX_EXISTING)}
            </div>
            <p class="mt-2 text-micro text-muted">
              Nothing here is stored, sent, or associated with you.
            </p>
          </div>
        </div>

        <div class="lg:col-span-6 lg:col-start-7">
          <h2 class="reveal text-h2">How the figure is worked out</h2>
          <p class="reveal mt-5 text-slate">
            The method, not a black box. Every line below is one term of the sum, and it updates
            with your numbers.
          </p>

          <div class="reveal mt-8 table-scroll table-signature">
            <table class="rate-table" style="min-width:26rem">
              <caption>Permanent coverage need, term by term.</caption>
              <tbody>
                <tr>
                  <th scope="row">Final expenses and debts</th>
                  <td>Funeral, final medical and estate bills, outstanding balances</td>
                  <td class="tnum" data-calc-out="debt">{money(EX_FINAL)}</td>
                </tr>
                <tr>
                  <th scope="row">Left to the people you name</th>
                  <td><span data-calc-out="children">{EX_PEOPLE}</span> at
                      <span data-calc-out="perchild">{money(EX_EACH)}</span> each</td>
                  <td class="tnum" data-calc-out="education">{money(EX_LEGACY)}</td>
                </tr>
                <tr>
                  <th scope="row">Less permanent coverage in force</th>
                  <td>Existing whole life or final expense policies</td>
                  <td class="tnum" data-calc-out="existing">{money(EX_EXISTING)}</td>
                </tr>
                <tr>
                  <th scope="row">What would still be needed</th>
                  <td></td>
                  <td class="tnum" data-calc-out="raw">{money(EX_RAW)}</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="reveal mt-8 card">
            <p class="text-sm text-muted">Rounded up to the next amount carriers quote</p>
            <p class="mt-2" aria-live="polite">
              <span class="stat-value" data-calc-out="rounded">{money(EX_ROUNDED)}</span>
            </p>
            <p class="mt-4 text-slate">
              Rounded up rather than down. With a permanent policy the amount is fixed for life,
              so buying slightly short is a decision you cannot cheaply revisit at eighty.
            </p>

            <button type="button" class="btn btn-cta btn-block btn-wrap mt-6"
                    data-calc-cta
                    data-prefill='{{"coverage":"{EX_ROUNDED}"}}'
                    data-prefill-trigger="calculator"
                    data-prefill-target="whole-calc-quote-form">
              Get quotes for <span data-calc-out="rounded">{money(EX_ROUNDED)}</span> of coverage
            </button>

            <p class="mt-6 text-slate" data-calc-enough hidden>
              On these numbers your existing permanent coverage already exceeds what the
              calculation asks for. That is worth a conversation rather than an application, and a
              licensed agent will tell you so on the phone.
            </p>
          </div>
        </div>

      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     WHY NO PREMIUM AND NO CASH VALUE. The compliance-driven honesty
     section, and the one that makes the page title truthful.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">Why this tool does not show you a premium</h2>
        <p class="reveal mt-5 text-slate">
          Because it cannot know one, and a calculator that produces a number it cannot know is
          worse than one that admits the gap.
        </p>
        <div class="reveal mt-6">
          {C.flag("No premium, cash value, or dividend figure appears on this page. When the "
                  "appointed carrier rate cards are loaded, a premium range may be shown here, "
                  "dated and sourced. Until then this tool sizes the need only.",
                  "PLACEHOLDER: NO CARRIER RATE CARDS LOADED")}
        </div>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        {C.qa("A premium needs a health class",
              "Whole life is medically underwritten, and the same 58 year old can be quoted "
              "several classes apart at two carriers. Until a carrier has read your answers, any "
              "premium is a guess with a dollar sign in front of it.")}
        {C.qa("A cash value column needs a carrier illustration",
              "Guaranteed cash values are printed in the contract and differ by carrier, age, "
              "policy design, and how the policy is funded. Non guaranteed columns depend on a "
              "dividend scale that no calculator can predict and that the carrier itself does not "
              "promise. We will send you a real illustration with the guaranteed column shown "
              "separately, which is the only version worth planning on.", "mt-8")}
        {C.qa("What this does tell you",
              "The face amount. That is the input every illustration starts from, and getting it "
              "right is worth more than any premium estimate: a policy sized correctly at a "
              "slightly worse price beats a policy sized wrongly at the best price on the market.",
              "mt-8")}
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     WHAT IT CANNOT ACCOUNT FOR. T3. A calculator that does not say what
     it is blind to is asking to be over trusted.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">What this calculator cannot account for</h2>
      <p class="reveal mt-5 text-slate">
        It is a subtraction, and a subtraction cannot see any of the following. Each one is a
        reason to treat the figure as a starting point rather than an answer.
      </p>
    </div>

    <div class="mt-10 bento" data-stagger="40">
      <div class="reveal bento-cell bento-cell-blue bento-2">
        <h3 class="text-h4 text-white">Inflation over decades</h3>
        <p class="mt-3 text-white/90">
          A permanent policy may pay in forty years. A fixed face amount does not index, and what
          feels sufficient today buys less then. This is the strongest argument for rounding up.
        </p>
      </div>
      <div class="reveal bento-cell bento-2">
        <h3 class="text-h4">Your estate's actual position</h3>
        <p class="mt-3 text-slate">
          State estate and inheritance taxes, probate costs, and business interests all change what
          liquidity an estate needs. Ask an estate attorney, not a web page.
        </p>
      </div>
      <div class="reveal bento-cell bento-cell-tint bento-2">
        <h3 class="text-h4">A dependant with lifelong needs</h3>
        <p class="mt-3 text-slate">
          Funding a special needs trust is a different calculation entirely, and it usually
          produces a larger number than this one. It is worth doing properly.
        </p>
      </div>
      <div class="reveal bento-cell bento-3">
        <h3 class="text-h4">Whether you can carry the premium for life</h3>
        <p class="mt-3 text-slate">
          This is the constraint that most often decides the real face amount. A permanent premium
          you cannot sustain becomes a lapsed policy, and a lapse in the early years is where whole
          life does the most financial damage. If the number above is more than the budget will
          bear, buy less of it permanently rather than more of it briefly.
        </p>
      </div>
      <div class="reveal bento-cell bento-3">
        <h3 class="text-h4">Whether some of this should be term</h3>
        <p class="mt-3 text-slate">
          Needs that end, such as a mortgage or years of income replacement, do not belong in a
          permanent policy. The honest comparison is on
          <a class="link" href="/compare/term-vs-whole-life-insurance/">term life against whole
          life</a>, including the cost of each over thirty years.
        </p>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     THE FORM. The prefill target for the CTA above, with the phone at
     parity beside it, per this silo's CTA weighting.
     ================================================================== -->
<section class="section band-surface" id="quote">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">Turn the figure into a real illustration</h2>
        <p class="reveal mt-5 text-slate">
          Five questions. A licensed agent comes back within {C.SLA} with premiums from named
          carriers for the amount above, and a full illustration showing the guaranteed and non
          guaranteed columns side by side rather than blended into one number.
        </p>
        <p class="reveal mt-5 text-slate">
          If you used the button above, the coverage amount is already filled in.
        </p>
        <div class="reveal mt-6 pt-6 border-t border-rule">
          <p class="text-slate">Or talk it through first. This is a product worth asking about.</p>
          <div class="mt-4">{C.phone_link("whole_calc_form", "btn btn-call")}</div>
          <p class="mt-3 text-micro text-muted">{C.HOURS}</p>
        </div>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <div class="reveal panel">
          {whole.quote_form("whole-calc-quote-form", "whole_calculator_quote", "wlc")}
        </div>
      </div>
    </div>
  </div>
</section>


{C.spoke_module(
    "Related pages in whole life",
    "Sizing the need is the first step. These cover the mechanics and the price.",
    [("/whole-life-insurance/what-is-whole-life-insurance/", "What whole life insurance is",
      "The definition, the mechanics, and where the premium goes."),
     ("/whole-life-insurance/cash-value/", "How cash value works",
      "Growth, borrowing, surrender, and the tax treatment."),
     ("/whole-life-insurance/rates/", "Whole life rates",
      "Premium by age and coverage amount, from current rate cards."),
     ("/whole-life-insurance/for-seniors/", "Whole life for seniors",
      "What is available after 65, and what it is for."),
     ("/whole-life-insurance/guaranteed-acceptance/", "Guaranteed acceptance",
      "No health questions, and exactly what that costs."),
     ("/whole-life-insurance/is-it-worth-it/", "Is whole life worth it?",
      "The case for and against, side by side.")])}


{C.byline_section()}
"""
