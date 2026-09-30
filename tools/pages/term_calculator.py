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
        "dependents, with the method shown. No email required.")

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
                                "income replacement, debts, dependents, and existing coverage. "
                                "Free, with no registration."),
                "publisher": {"@id": C.DOMAIN + "/#organization"},
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
            },
            C.person_schema(PATH)]


def field(fid, role, label, hint, value, prefix="$"):
    """A calculator amount: label, the control with a visible $ adornment, the
    hint under it (as on every form). Comma formatted; site.js strips the
    commas before it reads the number."""
    pre = ('<span class="calc-adorn" aria-hidden="true">%s</span>' % prefix) if prefix else ""
    return f"""<div class="field">
          <label class="field-label" for="{fid}">{label}</label>
          <div class="relative">{pre}<input class="input{' calc-money' if prefix else ''}" id="{fid}" name="{role}" type="text" inputmode="numeric"
                 autocomplete="off" value="{format(int(value), ',')}" placeholder="Amount in dollars"
                 data-calc-field="{role}"></div>
          <p class="field-hint">{hint}</p>
        </div>"""


def picker(fid, role, label, hint, options, selected):
    opts = "".join('<option value="%s"%s>%s</option>'
                   % (v, " selected" if v == selected else "", t) for v, t in options)
    return f"""<div class="field">
          <label class="field-label" for="{fid}">{label}</label>
          <select class="select" id="{fid}" name="{role}" data-calc-field="{role}">{opts}</select>
          <p class="field-hint">{hint}</p>
        </div>"""


def pair(a, b):
    """Two short calculator controls side by side from 16rem of panel width."""
    return '<div class="field-row field-row-tight">\n%s\n%s\n</div>' % (a, b)


def calc_hero(trail, h1, lead):
    """One line of lead, then three chips for what the visitor worries about:
    who sees the numbers."""
    chips = "".join(
        '<li class="calc-chip">%s<span>%s</span></li>' % (icon(name, 16, "shrink-0 text-navy"), text)
        for name, text in (("mail", "No email"), ("shield-check", "Nothing leaves your browser"),
                           ("list-checks", "Method shown in full")))
    return f"""
<section class="pt-6 pb-8 glow">
  <div class="container-ax">
    {C.crumbs(trail)}

    <div class="mt-8 max-w-3xl">
      <h1 class="reveal text-h1">{h1}</h1>
      <p class="reveal mt-5 text-lead text-slate">{lead}</p>
      <ul class="reveal mt-6 flex flex-wrap gap-2">{chips}</ul>
    </div>
  </div>
</section>"""


def calc_bar(parts, existing):
    """The live composition bar. parts: [(role, label, value)], one segment
    each, in order. Widths are rendered here from the worked example so the
    bar is right with JavaScript off; site.js section 10 rewrites them on edit
    ([data-calc-bar]). The striped overlay from the right is what existing
    coverage already pays for. Hidden from assistive tech: the line list under
    it carries the same numbers as text."""
    gross = sum(v for _, _, v in parts)
    pct = lambda v: "%.2f%%" % (100 * v / gross if gross else 0)
    segs = "".join('<span class="calc-seg calc-seg-%d" data-calc-bar="%s" style="width:%s"></span>'
                   % (i, role, pct(v)) for i, (role, _, v) in enumerate(parts, 1))
    legend = "".join('<li class="flex items-center gap-1.5"><span class="calc-dot calc-seg-%d"></span>%s</li>'
                     % (i, label) for i, (_, label, _) in enumerate(parts, 1))
    return f"""<div class="mt-6" aria-hidden="true">
              <div class="calc-bar">{segs}<span class="calc-covered" data-calc-bar="existing" style="width:{pct(min(existing, gross))}"></span></div>
              <ul class="mt-3 flex flex-wrap gap-x-5 gap-y-1 text-micro text-muted">{legend}<li class="flex items-center gap-1.5"><span class="calc-dot calc-dot-covered"></span>Already covered</li></ul>
            </div>"""


def result_card(rounded, bar, target, enough):
    """The answer first: the figure, what it is made of, and the one button."""
    return f"""<div class="reveal card calc-result">
            <p class="text-sm font-semibold text-navy">Your recommended coverage</p>
            <p class="mt-1" aria-live="polite">
              <span class="stat-value" data-calc-out="rounded">{money(rounded)}</span>
            </p>
            <p class="mt-1 text-sm text-muted">Rounded up to the next amount carriers quote.</p>
            {bar}
            <button type="button" class="btn btn-cta btn-block btn-wrap mt-6"
                    data-calc-cta
                    data-prefill='{{"coverage":"{rounded}"}}'
                    data-prefill-trigger="calculator"
                    data-prefill-target="{target}">
              <span>Get quotes for <span data-calc-out="rounded">{money(rounded)}</span> of coverage</span>
            </button>
            <p class="mt-6 text-slate" data-calc-enough hidden>{enough}</p>
          </div>"""


def breakdown(heading, sub, rows, total_label, total, note):
    """The method, line by line. rows: [(label, detail_html, out_role, value,
    minus)]. Two columns, so nothing wraps into a third."""
    lines = "".join(f"""
              <div class="calc-line">
                <dt><span class="font-semibold text-ink">{label}</span><span class="block mt-0.5 text-sm text-muted">{detail}</span></dt>
                <dd class="tnum">{"&#8722;" if minus else ""}<span data-calc-out="{role}">{money(value)}</span></dd>
              </div>""" for label, detail, role, value, minus in rows)
    return f"""<div class="reveal mt-10">
            <h2 class="text-h3 !font-display !font-semibold">{heading}</h2>
            <p class="mt-2 text-sm text-muted">{sub}</p>
            <dl class="mt-4">{lines}
              <div class="calc-line calc-total">
                <dt>{total_label}</dt>
                <dd class="tnum"><span data-calc-out="raw">{money(total)}</span></dd>
              </div>
            </dl>
            <p class="mt-4 text-sm text-muted">{note}</p>
          </div>"""


def body():
    return f"""{calc_hero([("Home", "/"), ("Term Life Insurance", "/term-life-insurance/"),
               ("Coverage calculator", None)],
          "How Much Term Life Insurance Do You Need?",
          'Work out how much <a class="link" href="/term-life-insurance/">term life insurance</a> '
          'your household needs. The answer updates as you type.')}


<!-- =====================================================================
     THE CALCULATOR. T3: interactive, no email gate.
     The inputs sit in a <div>, never inside the quote form below. Inside a
     form, collect() would validate them and FormData would post the
     visitor's income and debt to the CRM.
     ================================================================== -->
<section class="pb-14 md:pb-16">
  <div class="container-ax">
    <div data-calc="term_coverage_needs">
      <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">

        <div class="lg:col-span-5">
          <div class="sticky-col">
          <div class="reveal panel">
            <div class="panel-head">
              <h2 class="text-h3 !font-display !font-semibold">Your numbers</h2>
              <p class="mt-2 text-sm text-muted">
                Prefilled with an example so you can see how it works. Round figures are fine.
              </p>
            </div>
            <div class="mt-6">
              {pair(field("calc-income", "income", "Annual income", "Before tax.", EX_INCOME),
                    picker("calc-years", "years", "Years to replace", "Until the youngest is independent.",
                           [("5", "5 years"), ("10", "10 years"), ("15", "15 years"),
                            ("20", "20 years"), ("25", "25 years"), ("30", "30 years")], str(EX_YEARS)))}
              {field("calc-debt", "debt", "Mortgage and debts",
                     "The balance you owe, not the monthly payment.", EX_DEBT)}
              {pair(picker("calc-children", "children", "Children", "Anyone who depends on you.",
                           [(str(n), str(n)) for n in range(0, 7)], str(EX_CHILDREN)),
                    picker("calc-perchild", "perchild", "Per child", "Education and support.",
                           [("0", "Nothing"), ("25000", "$25,000"), ("50000", "$50,000"),
                            ("100000", "$100,000"), ("150000", "$150,000")], str(EX_PERCHILD)))}
              {field("calc-existing", "existing", "Already covered",
                     "Existing life insurance, employer coverage and savings.", EX_EXISTING)}
            </div>
            <p class="mt-2 text-micro text-muted">
              Nothing here is stored, sent, or associated with you.
            </p>
          </div>
          </div>
        </div>

        <div class="lg:col-span-6 lg:col-start-7">
          {result_card(EX_ROUNDED,
                       calc_bar([("income", "Income", EX_REPLACE), ("debt", "Debts", EX_DEBT),
                                 ("education", "Children", EX_EDUCATION)], EX_EXISTING),
                       "term-calc-quote-form",
                       "On these numbers you already have more coverage than the calculation asks "
                       "for. That is worth a conversation rather than an application, and a "
                       "licensed agent will tell you so on the phone.")}

          {breakdown("How we calculate your coverage amount",
                     "The income replacement method, which most term life underwriters expect to "
                     "see behind a coverage amount. Every line updates with your numbers.",
                     [("Income to replace",
                       '<span data-calc-out="incomeyear">%s</span> a year for <span data-calc-out="years">%s</span> years'
                       % (money(EX_INCOME), EX_YEARS), "income", EX_REPLACE, False),
                      ("Debt to pay off", "Mortgage and other balances, in full", "debt", EX_DEBT, False),
                      ("Set aside for children",
                       '<span data-calc-out="children">%s</span> at <span data-calc-out="perchild">%s</span> each'
                       % (EX_CHILDREN, money(EX_PERCHILD)), "education", EX_EDUCATION, False),
                      ("Less what you already have", "Existing coverage and savings", "existing",
                       EX_EXISTING, True)],
                     "What the household would need", EX_RAW,
                     "We round up because buying too little is the more common and more expensive "
                     "mistake. The premium difference between two neighboring amounts is usually "
                     "smaller than people expect.")}
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
        It is a sound starting point, not a financial plan. These are the things it leaves out
        on purpose.
      </p>
    </div>

    <div class="mt-10 bento" data-stagger="40">
      <div class="reveal bento-cell bento-2">
        <h3 class="text-h4">Inflation over the term</h3>
        <p class="mt-3 text-slate">
          The sum is in today's dollars. Over 20 or 30 years the real value of a fixed death
          benefit falls. That is a reason to pick the higher of two amounts you are considering.
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
          Group coverage usually stops when the job does, and you can rarely take it with you on
          good terms.
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
          A disabled child or a dependent parent needs support for life, not for a fixed number of
          years. That often means permanent coverage rather than term.
        </p>
      </div>
      <div class="reveal bento-cell bento-2">
        <h3 class="text-h4">Business obligations</h3>
        <p class="mt-3 text-slate">
          Key person coverage, buy sell agreements, and personally guaranteed business debt are all
          separate calculations, and usually separate policies.
        </p>
      </div>
    </div>

    <p class="reveal mt-8 text-slate max-w-3xl">
      If more than one of these applies to you, the number above is a minimum, not a final answer.
      Tell the agent when they call and they will work through it with you.
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
    <div class="form-first grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">Get quotes for your coverage amount</h2>
        <p class="reveal mt-5 text-slate">
          A coverage amount does not tell you what it costs. Answer six questions and a licensed
          agent replies within {C.SLA} with premiums from named carriers for this amount.
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


{C.byline_section()}
"""
