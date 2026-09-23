# -*- coding: utf-8 -*-
"""WHOLE LIFE QUOTES. Spec P1, template T1. Form and phone at equal weight.

T1 says the form is the page, and it is. What differs from the term version is
the weighting: the whole life silo puts the phone level with the form rather
than a step below it, because this product is bought after a conversation far
more often than term is. So the hero is a genuine two panel split, and the
phone block is a `.panel` rather than a rule and a link.

The tertiary "request an illustration" ask that the silo specifies is already
inside whole.quote_form(): the hidden `request_type` field plus the
[data-prefill-note] block. It is a form state, not a fourth link, which also
keeps this page inside spec s07 rule 4.

The sample rate table sits BELOW the form and is deliberately NOT gated.

The form itself is whole.quote_form(), already parameterised and already
serving the hub and the calculator. A third copy of the same five fields would
be a third place for the TCPA wording to drift.
"""
import chrome as C
import whole
from icons import icon

PATH = "/whole-life-insurance/quotes/"
OUT = "whole-life-insurance/quotes/index.html"
ACTIVE = "/whole-life-insurance/"
SILO = "whole-life"
TITLE = "Whole Life Insurance Quotes | Free, No Obligation"
OG_TITLE = "Get whole life insurance quotes and illustrations"
DESC = ("Free whole life insurance quotes from multiple appointed carriers, with the "
        "guaranteed numbers shown separately. No fee and no obligation.")

FAQ = [
    ("How long does it take to get a whole life quote?",
     "The form takes about two minutes. A licensed agent calls you back within " + C.SLA +
     " with named carriers and real premiums. A full illustration is the document that shows "
     "the guaranteed and non guaranteed columns year by year. It takes longer because the "
     "carrier produces it. Ask for one on the call and we will order it."),
    ("What is the difference between a quote and an illustration?",
     "A quote is a premium for a coverage amount. An illustration is the carrier's own multi page "
     "document showing what that policy does over its whole life. It shows the premium, "
     "guaranteed cash value, projected cash value, and the death benefit, year by year. The guaranteed columns are the "
     "only ones the carrier is contractually bound to. Read those first, and treat everything "
     "beside them as a projection."),
    ("Do I have to buy anything?",
     "No. There is no fee for the quote or the illustration, and no policy until you sign an "
     "application and a carrier issues it. You can stop at any point, including after you have "
     "applied and been approved."),
    ("Is whole life the right product for me?",
     "Often it is not, and we would rather say so on the call than sell you one. Whole life costs "
     "several times what the same death benefit costs as term. That gap is only worth paying "
     "if the need is permanent. If what you need is thirty years of coverage while a mortgage "
     "is paid down, we will tell you that and quote you term instead."),
    ("Will my details be sold to other agencies?",
     "No. Your details go to the licensed agent who quotes you and to the carriers we quote on "
     "your behalf. We are an agency, not a lead generator, so there is nothing for us to gain by "
     "selling them and we do not."),
]


def schema():
    return [
        C.org_schema(),
        C.breadcrumbs([("Home", "/"), ("Whole Life Insurance", "/whole-life-insurance/"),
                       ("Quotes", None)]),
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": "Whole life insurance quotes",
            "serviceType": "Whole life insurance brokerage",
            "provider": {"@id": C.DOMAIN + "/#agency"},
            "areaServed": {"@type": "Country", "name": "United States"},
            "description": ("Free, no obligation whole life insurance quotes and carrier "
                            "illustrations compared across multiple appointed carriers by a "
                            "licensed independent agency."),
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
     HERO. T1, with the whole life silo's CTA parity: two panels of equal
     width. The form does not get the wide column and the phone does not get
     a footnote. Neither outranks the other.

     No photograph. MASTER.md section 8: an image beside a form is a reason
     to look away from it.
     ================================================================== -->
<section class="pt-6 pb-14 md:pb-16 glow">
  <div class="container-ax">
    {C.crumbs([("Home", "/"), ("Whole Life Insurance", "/whole-life-insurance/"), ("Quotes", None)])}

    <div class="mt-8 max-w-3xl">
      <h1 class="reveal text-h1">Get Whole Life Insurance Quotes</h1>
      <p class="reveal mt-5 text-lead text-slate">
        Answer five questions. A licensed agent comes back with real prices for
        <a class="link" href="/whole-life-insurance/">whole life insurance</a> at your age, with
        the carrier named on each one. Guaranteed numbers are kept apart from projected ones. It
        is free, and you are not committed to anything.
      </p>
    </div>

    <div class="mt-10 grid lg:grid-cols-12 gap-8 items-stretch">

      <div class="lg:col-span-6">
        <div class="reveal panel h-full">
          <h2 class="text-h3 !font-display !font-semibold">Start your quote</h2>
          <p class="mt-2 text-sm text-muted">
            Nothing here is a credit check, and none of it affects your credit score.
          </p>
          {whole.quote_form("wl-quotes-form", "whole_quotes_page", "wq")}
        </div>
      </div>

      <div class="lg:col-span-6">
        <div class="reveal panel h-full" id="call">
          <h2 class="text-h3 !font-display !font-semibold">Or talk it through first</h2>
          <p class="mt-3 text-slate">
            Whole life has more moving parts than term. Most people we place it for asked their
            questions out loud before they filled anything in.
            The same licensed agent answers either way.
          </p>
          <div class="mt-6">
            {C.phone_link("whole_quotes_hero", "btn btn-call btn-block")}
          </div>
          <p class="mt-3 text-micro text-muted">{C.HOURS}</p>

          <ul class="mt-8 pt-8 border-t border-rule grid gap-3">
            <li class="flex items-start gap-2.5">{icon("circle-check", 20, "shrink-0 text-green mt-1")}<span class="text-sm">Guaranteed columns read to you first</span></li>
            <li class="flex items-start gap-2.5">{icon("circle-check", 20, "shrink-0 text-green mt-1")}<span class="text-sm">Multiple carriers compared</span></li>
            <li class="flex items-start gap-2.5">{icon("circle-check", 20, "shrink-0 text-green mt-1")}<span class="text-sm">We will say if term suits you better</span></li>
            <li class="flex items-start gap-2.5">{icon("circle-check", 20, "shrink-0 text-green mt-1")}<span class="text-sm">No fee, and no obligation to buy</span></li>
          </ul>
        </div>
      </div>

    </div>
  </div>
</section>


{C.usp_strip([("shield-check", "Licensed in " + C.STATES + " states", "Real licensed agents"), ("scale", "Independent agency", "We compare carriers for you"), ("file-text", "Carrier named", "Guaranteed column shown"), ("handshake", "Never sold", "Your details stay with us")])}


<!-- =====================================================================
     WHAT YOU NEED TO HAND. T1.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">What you need to get a quote</h2>
        <p class="reveal mt-5 text-slate">
          Almost nothing. You are not applying yet, so we do not ask for anything an application
          would.
        </p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <ul class="grid gap-4" data-stagger="60">
          {hand_item("Your age", "Your age at application, not your birthday. On a permanent policy it sets the premium you keep paying for the rest of your life, so a year of waiting is not free.")}
          {hand_item("Your state", "Carriers are licensed state by state, and the same policy is not priced identically everywhere.")}
          {hand_item("Roughly how much coverage", "A round number is fine. Whole life is usually bought in smaller amounts than term. If you have no idea, our calculator sizes the permanent part of the need.")}
          {hand_item("A number we can reach you at", "One licensed agent calls once. It goes nowhere else.")}
          {hand_item("Whether you want a full illustration", "Select that on the form and we will order the carrier's own document, with the guaranteed and projected columns side by side.")}
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
     "A licensed agent from Apex, within " + C.SLA + ". Not a call center, not an automated quote "
     "engine, and not six agencies who bought your details, because we do not sell them.",
     "If you would rather we emailed first, say so on the call and we will."),
    ("Fifteen to thirty minutes on the phone",
     "Longer than a term call, because there is more to say. We cover what the guarantees "
     "guarantee and what the cash value does in the early years. We also cover what you give up "
     "by putting the money here rather than somewhere else.", None),
    ("Named carriers, real premiums, and the guaranteed columns",
     "Carrier names, premiums, and the guaranteed cash value and death benefit, kept visibly "
     "apart from anything projected. If a number in front of you is a projection, we will say "
     "so.", None),
    ("You decide whether to apply",
     "There is no policy until you sign an application and a carrier issues it. If term "
     "suits you better, that is what we will tell you, and you owe nothing "
     "either way.", None),
], intro="Written out step by step.")}


{C.ask_strip("Ready to start?", "Five questions, and one licensed agent replies.", '<a href="#wl-quotes-form" class="btn btn-cta">Back to the form</a>')}

<!-- =====================================================================
     WHY QUOTES DIFFER BETWEEN CARRIERS. T1's objection section, written for
     a product where the illustration, not the premium, is what varies most.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Why whole life quotes differ between carriers</h2>
      <p class="reveal mt-5 text-slate">
        This is why an independent agency is worth using on a permanent policy. Two
        illustrations for the same person can look far apart. Most of that gap is in assumptions
        rather than in guarantees.
      </p>
    </div>

    <div class="mt-10 bento" data-stagger="40">
      <div class="reveal bento-cell bento-2">
        <h3 class="text-h4">The guarantees differ less than the projections</h3>
        <p class="mt-3 text-slate">
          Guaranteed columns are close together across carriers, because they are priced off the
          same conservative assumptions. The spread opens up in the projected columns, and those
          are the ones nobody is bound to.
        </p>
      </div>
      <div class="reveal bento-cell bento-cell-tint bento-2">
        <h3 class="text-h4">Dividend scales are not promises</h3>
        <p class="mt-3 text-slate">
          A mutual carrier illustrates at its current dividend scale. That scale has moved before
          and will move again. An illustration run at today's scale is a snapshot, not a forecast,
          and two carriers can be equally honest and still show different pictures.
        </p>
      </div>
      <div class="reveal bento-cell bento-cell-blue bento-2">
        <h3 class="text-h4">Carriers want different customers</h3>
        <p class="mt-3 text-white/90">
          Underwriting classes, minimum coverage amounts, and issue ages vary. The cheapest policy
          you can be approved for beats the cheapest one on paper. Which carrier that is depends
          on your health rather than on any rate chart.
        </p>
      </div>
    </div>

    <p class="reveal mt-8 text-slate max-w-3xl">
      We are appointed with {C.CARRIERS} carriers and we do not have a house favorite. That is
      the useful thing an agency can offer here: the comparison, with the names on it and the
      guaranteed columns pointed out first.
    </p>
  </div>
</section>


<!-- =====================================================================
     SAMPLE RATES. Deliberately NOT gated behind the form (T1). Sits below
     the form so it cannot push it down the page.

     Coverage columns match whole.quote_form()'s coverage select exactly. A
     row button that prefills an amount the select does not offer would
     silently blank the field.
     ================================================================== -->
<section class="section" id="rates">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Whole life premiums by age and coverage</h2>
      <p class="reveal mt-5 text-slate">
        Shown before you fill anything in. The structure below is what a real rate
        chart looks like; the numbers arrive when our carrier rate cards do.
      </p>
    </div>

    <div class="reveal mt-8 max-w-3xl">
      {C.rates_flag("premiums")}
    </div>

    {C.rate_chart(
        panels_id="whole-quote-rates",
        cols=["$25,000", "$50,000", "$100,000", "$250,000"],
        rows=[("45 to 49", {"age": "47", "coverage": "100000"}),
              ("50 to 54", {"age": "52", "coverage": "100000"}),
              ("55 to 59", {"age": "57", "coverage": "100000"}),
              ("60 to 64", {"age": "62", "coverage": "50000"}),
              ("65 to 69", {"age": "67", "coverage": "50000"}),
              ("70 to 74", {"age": "72", "coverage": "25000"})],
        toggles=[("Sex", "wq-rate-sex", [("female", "Female"), ("male", "Male")], "sex"),
                 ("Tobacco", "wq-rate-tobacco", [("no", "No"), ("yes", "Yes")], "tobacco")],
        caption="Monthly premium for a level, participating whole life policy by age band and "
                "coverage amount.",
        row_cta="prefill",
        prefill_target="wl-quotes-form",
        min_width="42rem",
        toggle_grid="grid sm:grid-cols-2 gap-6 max-w-lg")}

    <p class="reveal mt-8 text-slate max-w-3xl">
      A fuller chart, with more age bands and coverage amounts, is on the
      <a class="link" href="/whole-life-insurance/rates/">whole life insurance rates</a> page.
      Not sure how much permanent coverage to ask for? The
      <a class="link" href="/whole-life-insurance/calculator/">whole life calculator</a> sizes it
      from your final expenses, your debts, and who you want to leave something to.
    </p>
  </div>
</section>


{C.no_obligation_section(
    short_version="Your details go to the licensed agent who quotes you and to the carriers we "
                  "quote on your behalf. They are not sold, rented, or passed to other agencies "
                  "or lead buyers.",
    no_obligation="Submitting this form buys nothing and commits you to nothing. There is no fee "
                  "for the quote or for a carrier illustration, and no policy until you sign an "
                  "application and a carrier issues it.",
    stopping_contact="Ask us to stop and we stop, on the call or in writing. Consent to be called "
                     "is separate from the form and is never a condition of getting a quote. "
                     "Full detail is in our "
                     "<a class=\"link-static\" href=\"/legal/privacy/\">privacy policy</a>.")}


{C.faq_section("Whole life quote questions", FAQ, "whole-quotes-faq")}


{C.testimonials()}

{C.closing_band("whole-band", "Ready when you are",
    "Five questions, or one call. Either way you reach a licensed agent.",
    "whole_quotes_close", quote=("#wl-quotes-form", "Back to the form"))}"""
