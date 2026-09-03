# -*- coding: utf-8 -*-
"""TERM LIFE COVERAGE CALCULATOR. Spec P1, template T3. Form weighted.

No email wall. The calculator is the page and it works before, during, and
after any decision to talk to us. Gating a needs calculation behind an email
address is the pattern this build is explicitly not using.

The method is shown, not hidden: the derivation table below the inputs is the
calculation, term by term, so the recommendation can be audited rather than
trusted. site.js section 10 drives it.

PROGRESSIVE ENHANCEMENT. The worked example below is authored into the HTML
with its arithmetic already done, so with JavaScript off the page is a complete
and correct derivation rather than a column of zeros. site.js takes over from
the first edit and deliberately does not recompute on load.

# ponytail: the EXAMPLE literals and site.js section 10 must agree. _check()
# below re-derives them at build time and fails the build if they drift. If you
# change the ladder in site.js, change LADDER here too.
"""
import chrome as C
import term
from icons import icon

PATH = "/term-life-insurance/calculator/"
OUT = "term-life-insurance/calculator/index.html"
ACTIVE = "/term-life-insurance/"
SILO = "term-life"
TITLE = "Term Life Insurance Calculator | How Much Coverage Do You Need?"
OG_TITLE = "How much term life insurance do you need?"
DESC = ("Work out how much term life insurance your household needs. Income, debts, and "
        "dependants, with the method shown. No email required.")

# The coverage ladder the quote form's <select> offers. The recommendation has
# to land on it, or assigning the value silently blanks the field.
LADDER = [100000, 250000, 500000, 750000, 1000000, 2000000]

# The worked example. Every figure rendered in the derivation is computed from
# these, so the page cannot ship an example whose arithmetic does not add up.
EX_INCOME, EX_YEARS = 60000, 10
EX_DEBT = 210000
EX_CHILDREN, EX_PERCHILD = 2, 50000
EX_EXISTING = 200000


def _derive(income, years, debt, children, perchild, existing):
    replace = income * years
    education = children * perchild
    raw = replace + debt + education - existing
    # Only recommend a rung when there is a need. Without the raw > 0 guard the
    # first rung always matches a negative need, and a household that is
    # already over covered would be told to buy $100,000.
    rounded = next((rung for rung in LADDER if rung >= raw), LADDER[-1]) if raw > 0 else 0
    return replace, education, raw, rounded


EX_REPLACE, EX_EDUCATION, EX_RAW, EX_ROUNDED = _derive(
    EX_INCOME, EX_YEARS, EX_DEBT, EX_CHILDREN, EX_PERCHILD, EX_EXISTING)


def _check():
    """The one runnable check. Guards the JS-off worked example against a bad
    edit, and guards the recommendation against falling off the quote form's
    coverage ladder."""
    assert EX_REPLACE == 600000, EX_REPLACE
    assert EX_EDUCATION == 100000, EX_EDUCATION
    assert EX_RAW == 710000, EX_RAW
    assert EX_ROUNDED in LADDER, EX_ROUNDED
    assert EX_ROUNDED == 750000, EX_ROUNDED
    # Rounding is UP, never down: never recommend less than the derivation.
    assert EX_ROUNDED >= EX_RAW
    # A household that already has more cover than it needs gets no CTA.
    assert _derive(50000, 5, 0, 0, 0, 900000)[3] == 0


_check()


def money(n):
    return "$" + format(int(n), ",")


def schema():
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("Term Life Insurance", "/term-life-insurance/"),
                           ("Coverage calculator", None)]),
            {
                "@context": "https://schema.org",
                "@type": "SoftwareApplication",
                "name": "Term life insurance coverage calculator",
                "applicationCategory": "FinanceApplication",
                "operatingSystem": "Any modern web browser",
                "url": C.DOMAIN + PATH,
                "description": ("Calculates how much term life insurance a household needs from "
                                "income replacement, debts, dependants, and existing coverage. "
                                "Free, with no registration."),
                "publisher": {"@id": C.DOMAIN + "/#organization"},
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
            },
            C.person_schema(PATH)]


def field(fid, role, label, hint, value, prefix="$"):
    pre = ('<span class="text-muted">%s</span>' % prefix) if prefix else ""
    return f"""<div class="field">
          <label class="field-label" for="{fid}">{label}
            <span class="field-hint block font-normal">{hint}</span>
          </label>
          <input class="input" id="{fid}" name="{role}" type="text" inputmode="numeric"
                 autocomplete="off" value="{value}" data-calc-field="{role}">
        </div>"""


def picker(fid, role, label, hint, options, selected):
    opts = "".join('<option value="%s"%s>%s</option>'
                   % (v, " selected" if v == selected else "", t) for v, t in options)
    return f"""<div class="field">
          <label class="field-label" for="{fid}">{label}
            <span class="field-hint block font-normal">{hint}</span>
          </label>
          <select class="select" id="{fid}" name="{role}" data-calc-field="{role}">{opts}</select>
        </div>"""


def body():
    return f"""
<section class="pt-6 pb-10 glow">
  <div class="container-ax">
    {C.crumbs([("Home", "/"), ("Term Life Insurance", "/term-life-insurance/"),
               ("Coverage calculator", None)])}

    <div class="mt-8 max-w-3xl">
      <h1 class="reveal text-h1">How Much Term Life Insurance Do You Need?</h1>
      <p class="reveal mt-5 text-lead text-slate">
        Change the six figures below and the recommendation updates as you type. There is no email
        wall, nothing to submit, and nothing is sent anywhere: the whole calculation happens in
        your browser. It uses the income replacement method, which is the one most
        <a class="link" href="/term-life-insurance/">term life insurance</a> underwriters expect
        to see behind a coverage amount.
      </p>
    </div>
  </div>
</section>


<!-- =====================================================================
     THE CALCULATOR. T3: interactive, no email gate.
     The inputs sit in a <div>, never inside the quote form below. Inside a
     form, collect() would validate them and FormData would post the
     visitor's income and debt to the CRM.
     ================================================================== -->
<section class="pb-14 md:pb-16">
  <div class="container-ax">
    <div data-calc="term_coverage_needs">
      <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">

        <div class="lg:col-span-5">
          <div class="reveal panel">
            <h2 class="text-h3 !font-display !font-semibold">Your numbers</h2>
            <p class="mt-2 text-sm text-muted">
              Prefilled with an example so you can see how it works. Round figures are fine.
            </p>
            <div class="mt-6">
              {field("calc-income", "income", "Your annual income before tax",
                     "What the household would stop receiving.", EX_INCOME)}
              {picker("calc-years", "years", "Years of income to replace",
                      "Until the youngest child is independent, or the partner is at pension age.",
                      [("5", "5 years"), ("10", "10 years"), ("15", "15 years"),
                       ("20", "20 years"), ("25", "25 years"), ("30", "30 years")], str(EX_YEARS))}
              {field("calc-debt", "debt", "Mortgage and other debt",
                     "Balance outstanding, not the monthly payment.", EX_DEBT)}
              {picker("calc-children", "children", "Children who would need support",
                      "Count anyone financially dependent on you.",
                      [(str(n), str(n)) for n in range(0, 7)], str(EX_CHILDREN))}
              {picker("calc-perchild", "perchild", "Set aside per child",
                      "Education and support. Pick the closest.",
                      [("0", "Nothing"), ("25000", "$25,000"), ("50000", "$50,000"),
                       ("100000", "$100,000"), ("150000", "$150,000")], str(EX_PERCHILD))}
              {field("calc-existing", "existing", "Coverage and savings you already have",
                     "Include employer coverage and liquid savings.", EX_EXISTING)}
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
              <caption>Coverage need, term by term.</caption>
              <tbody>
                <tr>
                  <th scope="row">Income to replace</th>
                  <td><span data-calc-out="incomeyear">{money(EX_INCOME)}</span> a year for
                      <span data-calc-out="years">{EX_YEARS}</span> years</td>
                  <td class="tnum" data-calc-out="income">{money(EX_REPLACE)}</td>
                </tr>
                <tr>
                  <th scope="row">Debt cleared</th>
                  <td>Mortgage and other balances, paid off in full</td>
                  <td class="tnum" data-calc-out="debt">{money(EX_DEBT)}</td>
                </tr>
                <tr>
                  <th scope="row">Set aside for children</th>
                  <td><span data-calc-out="children">{EX_CHILDREN}</span> at
                      <span data-calc-out="perchild">{money(EX_PERCHILD)}</span> each</td>
                  <td class="tnum" data-calc-out="education">{money(EX_EDUCATION)}</td>
                </tr>
                <tr>
                  <th scope="row">Less what you already have</th>
                  <td>Existing coverage and savings</td>
                  <td class="tnum" data-calc-out="existing">{money(EX_EXISTING)}</td>
                </tr>
                <tr>
                  <th scope="row">What the household would need</th>
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
              Rounded up rather than down. Buying too little is the more common and more expensive
              mistake, and the premium difference between two neighbouring amounts is usually
              smaller than people expect.
            </p>

            <button type="button" class="btn btn-cta btn-block btn-wrap mt-6"
                    data-calc-cta
                    data-prefill='{{"coverage":"{EX_ROUNDED}"}}'
                    data-prefill-trigger="calculator"
                    data-prefill-target="term-calc-quote-form">
              Get quotes for <span data-calc-out="rounded">{money(EX_ROUNDED)}</span> of coverage
            </button>

            <p class="mt-6 text-slate" data-calc-enough hidden>
              On these numbers you already have more coverage than the calculation asks for. That
              is worth a conversation rather than an application, and a licensed agent will tell
              you so on the phone.
            </p>
          </div>
        </div>

      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     WHAT IT CANNOT ACCOUNT FOR. T3. A calculator that does not say what it
     is blind to is asking to be over trusted.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">What this calculator cannot account for</h2>
      <p class="reveal mt-5 text-slate">
        It is a starting point, and a defensible one. It is not a financial plan, and these are
        the things it is deliberately blind to.
      </p>
    </div>

    <div class="mt-10 bento" data-stagger="40">
      <div class="reveal bento-cell bento-2">
        <h3 class="text-h4">Inflation over the term</h3>
        <p class="mt-3 text-slate">
          The sum is in today's dollars. Over 20 or 30 years the real value of a fixed death
          benefit falls, which argues for the higher of two amounts you are choosing between.
        </p>
      </div>
      <div class="reveal bento-cell bento-cell-tint bento-2">
        <h3 class="text-h4">A surviving partner's own income</h3>
        <p class="mt-3 text-slate">
          If they earn well, you may need less. If they would have to stop work to care for
          children, you need considerably more than this shows.
        </p>
      </div>
      <div class="reveal bento-cell bento-2">
        <h3 class="text-h4">Employer coverage that ends</h3>
        <p class="mt-3 text-slate">
          Group cover usually stops when the job does, and it is rarely portable on good terms.
          Counting it as permanent is the most common error in this calculation.
        </p>
      </div>
      <div class="reveal bento-cell bento-cell-blue bento-2">
        <h3 class="text-h4">Final expenses and taxes</h3>
        <p class="mt-3 text-white/90">
          Funeral costs, medical bills, and any estate or state level tax are not in the sum.
          A death benefit is generally income tax free to the beneficiary, but it is not
          automatically outside an estate.
        </p>
      </div>
      <div class="reveal bento-cell bento-cell-tint bento-2">
        <h3 class="text-h4">Care for a dependent adult</h3>
        <p class="mt-3 text-slate">
          A disabled child or a dependent parent needs a lifetime provision, not a fixed number of
          years, and often permanent coverage rather than term.
        </p>
      </div>
      <div class="reveal bento-cell bento-2">
        <h3 class="text-h4">Business obligations</h3>
        <p class="mt-3 text-slate">
          Key person cover, buy sell agreements, and personally guaranteed business debt are all
          separate calculations, and usually separate policies.
        </p>
      </div>
    </div>

    <p class="reveal mt-8 text-slate max-w-3xl">
      If more than one of these applies to you, the number above is a floor rather than an answer.
      Say so when an agent calls and it will be worked through properly.
    </p>
  </div>
</section>


<!-- =====================================================================
     POST RESULT CTA. The form is on this page so the calculator's button
     can write the computed figure straight into it (site.js section 7
     reads data-prefill at click time).
     ================================================================== -->
<section class="section" id="quote">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">Turn the number into real premiums</h2>
        <p class="reveal mt-5 text-slate">
          A coverage amount on its own does not tell you what it costs. Six questions and a
          licensed agent comes back within {C.SLA} with premiums from named carriers for exactly
          this amount.
        </p>
        <p class="reveal mt-5 text-slate">
          Using the button above fills the coverage amount in for you and skips to what is still
          missing.
        </p>
        <div class="reveal mt-6 pt-6 border-t border-rule">
          <p class="text-slate">Or work through the numbers with a licensed agent.</p>
          <div class="mt-4">{C.phone_link("term_calculator_cta", "btn btn-call")}</div>
          <p class="mt-3 text-micro text-muted">{C.HOURS}</p>
        </div>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <div class="reveal panel">
          {term.quote_form("term-calc-quote-form", "term_calculator_quote", "tcq")}
        </div>
      </div>
    </div>
  </div>
</section>


<section class="section-tight band">
  <div class="container-ax">
    <div class="reveal">{C.byline()}</div>
  </div>
</section>
"""
