# -*- coding: utf-8 -*-
"""GET A QUOTE, DETAILS. Stage 2 of the two-stage quote (see get_a_quote.py).

Optional. Offered in /get-a-quote/'s success panel, modelled on AccuQuote's
quote form: one topic per step, the questions that actually move a rate.
Opens prefilled from stage 1 ([data-handoff-fill] in site.js) and carries
quick_submission_id so the CRM can join it to the first lead. Works
standalone too, which is why it still asks for contact details at the end.

noindex: it is a continuation, not a landing page.

BRANCHING. Step 1's product enables one of three coverage steps. Those steps
hold only selects, so no radio name is shared across branches (check.py).
Skipped from AccuQuote: date of birth (age is already asked; the date
validator is 50+ only) and the "we recommend" interstitial (the home triage
quiz does that job).
"""
import chrome as C
import forms as F
from get_a_quote import product_choices

PATH = "/get-a-quote/details/"
OUT = "get-a-quote/details/index.html"
ACTIVE = "/get-a-quote/"
SILO = "site"
ROBOTS = "noindex, follow"
TITLE = "Your Quote Details | Apex Insurance Marketing"
DESC = ("A few more questions so a licensed agent can call with sharper life insurance "
        "quotes. About two minutes, optional, no obligation.")

REASONS = [("family", "Protect my family"), ("debt", "Cover a mortgage or debt"),
           ("income", "Replace my income"), ("final-expenses", "Pay final expenses"),
           ("other", "Something else")]
PROTECT = [("partner", "Spouse or partner"), ("children", "Children"),
           ("parent", "A parent"), ("other", "Someone else")]
TOBACCO = [("never", "Never used tobacco or nicotine"),
           ("quit-5plus", "Quit more than 5 years ago"),
           ("quit-1to5", "Quit 1 to 5 years ago"),
           ("quit-under1", "Quit less than a year ago"),
           ("cigarettes", "Smoke cigarettes"),
           ("cigars-pipe", "Smoke cigars or a pipe"),
           ("other-nicotine", "Vape, chew, patch, or nicotine gum")]
HEALTH = [("excellent", "Excellent"), ("good", "Good"),
          ("fair", "Fair"), ("poor", "Poor")]
TERM_LENGTHS = ["10", "15", "20", "25", "30", "35", "40"]


def money(n):
    return "${:,}".format(n)


def coverage(field_id, amounts, top):
    opts = [("", "Choose an amount")] + [(str(a), money(a)) for a in amounts] \
        + [(str(top), money(top) + " or more"), ("unsure", "Not sure yet")]
    return F.select_field(field_id, "coverage", "How much coverage?", opts,
                          error="Choose an amount, or Not sure yet.")


def col_group(group_id, name, legend, options, error, inner=None):
    """A stacked radio column, for sets too long for one .choice-row. `inner`
    replaces the generated options (the product cards)."""
    opts = inner or "".join(
        '\n<label class="choice choice-block"><input type="radio" name="%s" value="%s" required>'
        '<span>%s</span></label>' % (name, v, t) for v, t in options)
    return ('<div class="field" data-error="%s">\n'
            '<span class="field-label" id="%s-label">%s</span>\n'
            '<div class="choice-col mt-3" role="group" aria-labelledby="%s-label">%s\n</div>\n'
            '<p class="field-error">%s<span></span></p>\n</div>'
            % (error, group_id, legend, group_id, opts, F.ERR))


def schema():
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("Get a quote", "/get-a-quote/"),
                           ("Your details", None)])]


def detail_form():
    states = '<option value="">Choose your state</option>\n' + C.state_options()
    need = (
        col_group("d-product", "product", "What are you looking for?", None,
                  "Pick the one closest to what you are after.", inner=product_choices())
        + col_group("d-reason", "reason", "What is the main reason?", REASONS,
                    "Choose the closest reason.")
        + F.next_button())
    who = (
        F.radio_group("d-protect", "protect", "Who are you most hoping to protect?", PROTECT,
                      error="Choose the closest.")
        + F.select_field("d-children", "children", "Children under 18",
                         [("", "Choose")] + [(n, n) for n in ["0", "1", "2", "3", "4+"]],
                         error="Choose a number, 0 is fine.")
        + F.next_button(back=True))
    about = (
        F.row(F.age_field("d-age"),
              F.select_field("d-state", "state", "Your state", states,
                             error="Please choose your state."))
        + F.radio_group("d-sex", "sex", "Sex on your birth certificate",
                        [("female", "Female"), ("male", "Male")],
                        hint="Carriers rate them differently.",
                        error="Choose one so we can price it correctly.")
        + F.select_field("d-tobacco", "tobacco", "Tobacco or nicotine",
                         [("", "Choose the closest")] + TOBACCO,
                         error="Let us know either way.")
        + F.radio_group("d-health", "health", "How would you rate your health?", HEALTH,
                        hint="Your honest guess. The agent checks the details that matter.",
                        error="Choose the closest.")
        + F.next_button(back=True))
    term = (
        F.row(F.select_field("d-term-length", "term_length", "For how many years?",
                             [("", "Choose a length")] + [(y, y + " years") for y in TERM_LENGTHS],
                             hint="Until the youngest is grown or the mortgage is paid.",
                             error="Choose a length, or pick the closest."),
              coverage("d-term-cov", range(100000, 1000001, 100000), 2000000))
        + F.next_button(back=True))
    whole = (coverage("d-wl-cov", [25000, 50000, 100000, 250000], 500000)
             + F.next_button(back=True))
    final = (coverage("d-fe-cov", [5000, 10000, 15000, 20000, 25000, 35000], 50000)
             + F.next_button(back=True))
    reach = (
        F.row(F.text_field("d-name", "name", "Your name", autocomplete="name", validate="name",
                           error="Enter your name."),
              F.phone_field("d-phone"), tight=True)
        + F.text_field("d-email", "email", "Email", type="email", autocomplete="email",
                       validate="email", error="Enter a valid email address.")
        + F.consent_block("d", C.BRAND, 12)
        + F.submit_block("Send my details", back=True))
    return f"""
        <form id="detail-form" class="mt-6" data-ax-form data-steps data-handoff-fill
              data-silo="site" data-form-name="detailed_quote"
              data-success-target="detail-success" novalidate>

          {F.scaffold('<input type="hidden" name="quick_submission_id">', indent=10)}

          {F.progress(5)}

          {F.step(1, "What you need", need, first=True)}
          {F.step(2, "Who it protects", who)}
          {F.step(3, "About you", about)}
          {F.step(4, "Coverage", term, owner="term")}
          {F.step(4, "Coverage", whole, owner="whole")}
          {F.step(4, "Coverage", final, owner="final-expense")}
          {F.step(5, "How to reach you", reach)}
        </form>

        {F.success_panel("detail-success", "Thanks, that is everything",
            '''<p class="mt-3 text-slate">
                 The agent now has what they need to price this properly. You will hear from us
                 within %s, with carrier names on every quote.
               </p>''' % C.SLA,
            '''%s
               <a class="link text-sm inline-block mt-4 sm:mt-0 sm:ml-5" href="/thank-you/">What happens next</a>'''
            % C.phone_link("detail_success", "btn btn-call", "Or call " + C.PHONE_DISPLAY),
            icon_size=30, indent=8)}"""


def body():
    return f"""
<section class="pt-6 pb-14 md:pb-16 glow">
  <div class="container-ax">
    {C.crumbs([("Home", "/"), ("Get a quote", "/get-a-quote/"), ("Your details", None)])}

    <div class="mt-8 grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">

      <div class="lg:col-span-5">
        <h1 class="reveal text-h1">A few more questions</h1>
        <p class="reveal mt-5 text-lead text-slate">
          Optional, and about two minutes. The more the agent knows before the call, the closer
          the first quote is to the price you will actually pay.
        </p>

        <div class="reveal card mt-8">
          <h2 class="text-h4">Prefer to talk?</h2>
          <p class="mt-2 text-sm text-slate">
            The agent can ask all of this on the call instead.
          </p>
          <div class="mt-4">
            {C.phone_link("detail_sidebar", "btn btn-call btn-block", C.PHONE_DISPLAY, 22)}
          </div>
          <p class="mt-3 text-micro text-muted">{C.HOURS}</p>
        </div>
      </div>

      <div class="lg:col-span-6 lg:col-start-7">
        <div class="panel reveal">
          <div class="panel-head">
            <h2 class="text-h3 !font-display !font-semibold">Your quote details</h2>
            <p class="mt-2 text-sm text-muted">Five short steps. Nothing is charged and nothing is binding.</p>
          </div>
          {detail_form()}
        </div>
      </div>
    </div>
  </div>
</section>"""
