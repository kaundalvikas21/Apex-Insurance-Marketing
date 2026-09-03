# -*- coding: utf-8 -*-
"""TERM LIFE QUOTES. Spec P1, template T1. Form weighted.

The highest value non-head page in the build. The form IS the page: it is the
hero's right panel, above the fold at 1024, and every section below it exists
to answer one objection in the order it occurs.

The sample rate table sits BELOW the form and is deliberately NOT gated.
Showing indicative numbers before asking for details raises completion; hiding
them behind the form is the pattern this agency is trying not to be.

The form itself is term.quote_form(), which is already parameterised and
already serves the hub twice. Writing a fourth variant of the same three step
form would be four places for the TCPA wording to drift apart.
"""
import chrome as C
import term
from icons import icon

PATH = "/term-life-insurance/quotes/"
OUT = "term-life-insurance/quotes/index.html"
ACTIVE = "/term-life-insurance/"
SILO = "term-life"
TITLE = "Term Life Insurance Quotes | Free, No Obligation"
OG_TITLE = "Get term life insurance quotes from multiple carriers"
DESC = ("Get free term life insurance quotes from multiple appointed carriers. No obligation, "
        "no fee, and no policy until you sign. Takes about two minutes.")

FAQ = [
    ("How long does it take to get a quote?",
     "The form takes about two minutes. A licensed agent calls you back within " + C.SLA +
     " with named carriers and real premiums. If you would rather have it in writing first, say "
     "so on the call and we will email the comparison instead."),
    ("Is this a real quote or an estimate?",
     "What comes back from us is a quoted premium from a named carrier at an assumed rate class, "
     "which is as close to real as anything can be before underwriting. The final premium is set "
     "by the carrier after it reviews your health, your build, your family history, and in most "
     "states your driving record. We tell you which assumptions we used, so you can see what "
     "would move the number."),
    ("Do I have to buy anything?",
     "No. There is no fee for the quote and no policy until you sign an application and a carrier "
     "issues it. You can stop at any point, including after you have applied and been approved."),
    ("Will my details be sold to other agencies?",
     "No. Your details go to the licensed agent who quotes you and to the carriers we quote on "
     "your behalf. We are an agency, not a lead generator, so there is nothing for us to gain by "
     "selling them and we do not."),
]


def schema():
    return [
        C.org_schema(),
        C.breadcrumbs([("Home", "/"), ("Term Life Insurance", "/term-life-insurance/"),
                       ("Quotes", None)]),
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": "Term life insurance quotes",
            "serviceType": "Term life insurance brokerage",
            "provider": {"@id": C.DOMAIN + "/#agency"},
            "areaServed": {"@type": "Country", "name": "United States"},
            "description": ("Free, no obligation term life insurance quotes compared across "
                            "multiple appointed carriers by a licensed independent agency."),
            "url": C.DOMAIN + PATH,
            # [PLACEHOLDER] No Offer node and no price. We do not have carrier
            # rate cards yet, and a price in structured data is a price claim.
        },
    ]


def hand_item(label, why):
    return f"""<li class="reveal flex items-start gap-3">
          {icon("circle-check", 20, "shrink-0 text-green mt-1")}
          <span><span class="font-semibold text-ink">{label}.</span>
          <span class="text-slate">{why}</span></span>
        </li>"""


def body():
    return f"""
<!-- =====================================================================
     HERO. The form is the page (T1). Everything else sits below it.
     ================================================================== -->
<section class="pt-6 pb-14 md:pb-16 glow">
  <div class="container-ax">
    {C.crumbs([("Home", "/"), ("Term Life Insurance", "/term-life-insurance/"), ("Quotes", None)])}

    <div class="mt-8 grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">

      <div class="lg:col-span-6">
        <h1 class="reveal text-h1">Get Term Life Insurance Quotes</h1>
        <p class="reveal mt-5 text-lead text-slate max-w-xl">
          Answer six questions and a licensed agent comes back with premiums from our appointed
          carriers, with the carrier names on them. It is free, it commits you to nothing, and
          it is the fastest way to find out what
          <a class="link" href="/term-life-insurance/">term life insurance</a> would actually
          cost you rather than what a calculator guesses.
        </p>

        <ul class="reveal mt-8 grid sm:grid-cols-2 gap-x-8 gap-y-3">
          <li class="flex items-start gap-2.5">{icon("circle-check", 20, "shrink-0 text-green mt-1")}<span class="text-sm">About two minutes, six questions</span></li>
          <li class="flex items-start gap-2.5">{icon("circle-check", 20, "shrink-0 text-green mt-1")}<span class="text-sm">Multiple carriers compared, not one</span></li>
          <li class="flex items-start gap-2.5">{icon("circle-check", 20, "shrink-0 text-green mt-1")}<span class="text-sm">No fee, and no obligation to buy</span></li>
          <li class="flex items-start gap-2.5">{icon("circle-check", 20, "shrink-0 text-green mt-1")}<span class="text-sm">One agency calls you, not six</span></li>
        </ul>

        <div class="reveal mt-8 pt-8 border-t border-rule">
          <p class="text-slate">
            Would rather say it out loud? A call gets you the same licensed agent and the same
            comparison, and you can ask the awkward questions as they come up.
          </p>
          <div class="mt-4">
            {C.phone_link("term_quotes_hero", "btn btn-call")}
          </div>
          <p class="mt-3 text-micro text-muted">{C.HOURS}</p>
        </div>
      </div>

      <div class="lg:col-span-5 lg:col-start-8" id="quote">
        <div class="reveal panel">
          <h2 class="text-h3 !font-display !font-semibold">Start your quote</h2>
          <p class="mt-2 text-sm text-muted">
            Nothing here is a credit check, and none of it affects your credit score.
          </p>
          {term.quote_form("term-quote-form", "term_quotes_page", "tq")}
        </div>
      </div>

    </div>
  </div>
</section>


<section class="border-y border-rule bg-surface">
  <div class="container-ax py-6">
    <div class="flex flex-wrap items-center justify-between gap-x-8 gap-y-3 trust-strip">
      <span class="inline-flex items-center gap-2 text-navy font-semibold">{icon("shield-check", 20)}Licensed in {C.STATES} states</span>
      <span class="inline-flex items-center gap-2">{icon("handshake", 20, "text-navy-700")}Independent, appointed with {C.CARRIERS} carriers</span>
      <span class="inline-flex items-center gap-2">{icon("clock", 20, "text-navy-700")}Reply within {C.SLA}</span>
      <span class="inline-flex items-center gap-2">{icon("file-text", 20, "text-navy-700")}No fee, ever</span>
    </div>
  </div>
</section>


<!-- =====================================================================
     WHAT YOU NEED TO HAND. T1. Reduces the number of people who start the
     form, hit a question they cannot answer, and abandon it.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">What you need to hand</h2>
        <p class="reveal mt-5 text-slate">
          Almost nothing, which is the point. You are not applying yet, so we are not asking for
          anything an application would ask for.
        </p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <ul class="grid gap-4" data-stagger="60">
          {hand_item("Your age", "The single biggest factor in the price. Your age at application, not your birthday.")}
          {hand_item("Your state", "Carriers are licensed state by state, and the same policy is not priced identically everywhere.")}
          {hand_item("Roughly how much coverage", "A round number is fine. If you have no idea, our coverage calculator works it out from your income and debts, and you can come back.")}
          {hand_item("Whether you have used tobacco or nicotine", "In the last twelve months. Answer honestly: it is verified during underwriting, and a surprise there costs you the policy, not just the rate.")}
          {hand_item("A number we can reach you on", "One licensed agent calls once. It goes nowhere else.")}
        </ul>
        <p class="reveal mt-6 text-slate">
          We do not ask for your Social Security number, your bank details, or your medical
          records to give you a quote. Anyone who does before quoting you is doing something else.
        </p>
      </div>
    </div>
  </div>
</section>


{C.post_submit_section([
    ("You get one call, from one agency",
     "A licensed agent from Apex, within " + C.SLA + ". Not a call centre, not an automated quote "
     "engine, and not six agencies who bought your details, because we do not sell them.",
     "If you would rather we emailed first, say so on the call and we will."),
    ("Ten to twenty minutes on the phone",
     "Enough to confirm what you sent, ask the two or three health questions that actually move a "
     "term rate, and understand what you are trying to cover and for how long.", None),
    ("Named carriers and real premiums",
     "Carrier names, premiums, term lengths, and the conversion terms, so you can compare them "
     "against anything else you have been shown. Including, where it applies, which carriers "
     "would decline you and why.", None),
    ("You decide, or you do not",
     "There is no policy until you sign an application and a carrier issues it. If you decide "
     "against it, you owe nothing and we stop contacting you when you ask.", None),
], intro="Written out because \"we will be in touch\" is not an answer, and because the gap "
         "between what a form promises and what actually happens is where most of the distrust "
         "in this industry comes from.")}


<!-- =====================================================================
     WHY QUOTES DIFFER BETWEEN CARRIERS. T1. The objection that stops people
     trusting any single number they are shown.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Why two carriers quote the same person differently</h2>
      <p class="reveal mt-5 text-slate">
        This is the whole reason an independent agency is worth using. Carriers are not competing
        on one price list. They are competing on who they want to insure, and they disagree.
      </p>
    </div>

    <div class="mt-10 bento" data-stagger="40">
      <div class="reveal bento-cell bento-2">
        <h3 class="text-h4">They weigh the same facts differently</h3>
        <p class="mt-3 text-slate">
          One carrier treats well controlled high blood pressure as a standard risk. Another rates
          it up two classes. Neither is wrong; they are reading different books of claims.
        </p>
      </div>
      <div class="reveal bento-cell bento-cell-tint bento-2">
        <h3 class="text-h4">They want different customers</h3>
        <p class="mt-3 text-slate">
          A carrier that wants more thirty year olds on twenty year terms prices that cell sharply
          and prices the rest ordinarily. Which cell you fall into changes who is cheapest for you.
        </p>
      </div>
      <div class="reveal bento-cell bento-cell-blue bento-2">
        <h3 class="text-h4">Their underwriting programmes differ</h3>
        <p class="mt-3 text-white/90">
          Whether you can skip the medical exam, and at what age and coverage, varies by carrier.
          The cheapest policy you can actually get approved for beats the cheapest one on paper.
        </p>
      </div>
    </div>

    <p class="reveal mt-8 text-slate max-w-3xl">
      We are appointed with {C.CARRIERS} carriers and we do not have a house favourite. That is
      the only useful thing an agency can offer here: the comparison, with the names on it.
    </p>
  </div>
</section>


<!-- =====================================================================
     SAMPLE RATES. Deliberately NOT gated behind the form (T1). Sits below
     the form so it cannot push it down the page.
     ================================================================== -->
<section class="section" id="rates">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Rough shape of term premiums</h2>
      <p class="reveal mt-5 text-slate">
        Shown before you fill anything in, not after. The structure below is what a real rate
        chart looks like; the numbers arrive when our carrier rate cards do.
      </p>
    </div>

    <div class="reveal mt-8 max-w-3xl">
      {C.rates_flag("premiums")}
    </div>

    {C.rate_chart(
        panels_id="term-quote-rates",
        cols=["$250,000", "$500,000", "$1,000,000"],
        rows=[("30 to 34", {"age": "32", "coverage": "500000"}),
              ("35 to 39", {"age": "37", "coverage": "500000"}),
              ("40 to 44", {"age": "42", "coverage": "500000"}),
              ("45 to 49", {"age": "47", "coverage": "500000"}),
              ("50 to 54", {"age": "52", "coverage": "500000"}),
              ("55 to 59", {"age": "57", "coverage": "250000"})],
        toggles=[("Term length", "tq-rate-length",
                  [("20", "20 years"), ("10", "10 years"), ("30", "30 years")], "term_length"),
                 ("Sex", "tq-rate-sex", [("female", "Female"), ("male", "Male")], "sex"),
                 ("Tobacco", "tq-rate-tobacco", [("no", "No"), ("yes", "Yes")], "tobacco")],
        caption="Monthly premium by age band and coverage amount.",
        row_cta="prefill",
        prefill_target="term-quote-form",
        min_width="40rem",
        toggle_grid="grid sm:grid-cols-[7fr_4fr_4fr] gap-6 max-w-3xl")}

    <p class="reveal mt-8 text-slate max-w-3xl">
      A fuller chart, with more age bands and coverage amounts, is on the
      <a class="link" href="/term-life-insurance/rates/">term life insurance rates</a> page. If
      you are not sure how much coverage to ask for, the
      <a class="link" href="/term-life-insurance/calculator/">coverage calculator</a> works it out
      from your income, your debts, and who depends on you.
    </p>
  </div>
</section>


{C.no_obligation_section(
    short_version="Your details go to the licensed agent who quotes you and to the carriers we "
                  "quote on your behalf. They are not sold, rented, or passed to other agencies "
                  "or lead buyers.",
    no_obligation="Submitting this form buys nothing and commits you to nothing. There is no fee, "
                  "no charge, and no policy until you sign an application and a carrier issues it.",
    stopping_contact="Ask us to stop and we stop, on the call or in writing. Consent to be called "
                     "is separate from the form and is never a condition of getting a quote. "
                     "Full detail is in our "
                     "<a class=\"link-static\" href=\"/legal/privacy/\">privacy policy</a>.")}


{C.faq_section("Before you start", FAQ, "term-quotes-faq")}
"""
