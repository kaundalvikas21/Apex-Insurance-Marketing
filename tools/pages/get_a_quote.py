# -*- coding: utf-8 -*-
"""GET A QUOTE. Spec P0, template T1. Stage 1 of the two-stage quote.

The form is the page. Everything below it exists to answer the objections that
stop someone finishing it, in the order they occur: what will you ask me, what
happens after I submit, why do quotes differ, what do the numbers look like,
and what do you do with my details.

TWO STAGES (client request, 2026-09-29, modelled on AccuQuote's quote form):

    stage 1  here. Name, age, email, phone, type of insurance. One screen, and
             it sends the lead, so the agent has a contact even if the
             visitor stops here.
    stage 2  /get-a-quote/details/. Optional, offered in the success panel:
             reason, dependants, health, tobacco, coverage. Opens prefilled
             from stage 1 via [data-handoff] (site.js) and is linked to this
             lead by quick_submission_id.

The form keeps id="quote-form" and form_name master_quote, so the rate table's
"quote this row" prefill and GA4 history both carry over.
"""
from icons import icon
import chrome as C
import forms as F

PATH = "/get-a-quote/"
OUT = "get-a-quote/index.html"
ACTIVE = PATH
SILO = "site"
TITLE = "Get a Free Life Insurance Quote | Apex Insurance Marketing"
OG_TITLE = "Get a free life insurance quote"
DESC = ("Compare term life, whole life and final expense quotes from multiple carriers. "
        "Free, no obligation, no medical exam or Social Security number for a quote.")

PRODUCTS = [
    ("term", "Term life", "Coverage for a set number of years. Usually the cheapest way to cover a mortgage or children at home."),
    ("whole", "Whole life", "Coverage for life, with a level premium and cash value that builds."),
    ("final-expense", "Final expense", "A smaller policy for a funeral and final bills. No medical exam."),
]

AGE_BANDS = [("30 to 39", "35"), ("40 to 49", "45"), ("50 to 59", "55"),
             ("60 to 69", "65"), ("70 to 79", "75")]

FAQ = [
    ("Do I have to take a medical exam to get a quote?",
     "No. A quote needs your age, state, sex, and whether you use tobacco. An exam only ever "
     "comes up later, at the application stage, and plenty of the policies we place do not "
     "require one at all."),
    ("Will you ask for my Social Security number?",
     "Not for a quote. It is needed on an application, because the carrier uses it to order "
     "your prescription and motor vehicle history. Nobody needs it to tell you what a "
     "policy costs. If a site asks for it before showing you a price, leave."),
    ("How many people will call me?",
     "One. A licensed agent from this agency, once, within " + C.SLA + ". We are not a lead "
     "generator: your details are not sold, rented, or passed to other agencies. You will "
     "not get the six calls in ten minutes that a comparison site produces."),
    ("What if I change my mind?",
     "Nothing happens. There is no obligation at any stage, no fee, and no policy until you "
     "sign an application and the carrier issues it. Tell us to stop contacting you and we will."),
]


def schema():
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("Get a quote", None)]),
            {"@context": "https://schema.org", "@type": "Service",
             "@id": C.DOMAIN + PATH + "#service",
             "name": "Life insurance quote comparison",
             "serviceType": "Life insurance brokerage",
             "provider": {"@id": C.DOMAIN + "/#organization"},
             "areaServed": {"@type": "Country", "name": "United States"},
             "audience": {"@type": "Audience", "audienceType": "Consumers seeking life insurance"},
             "offers": {"@type": "Offer", "price": "0",
                        "priceCurrency": "USD",
                        "description": "Quotes and comparison are free and carry no obligation."}},
            C.faq_schema(FAQ)]


def product_choices():
    """The three products as described cards, with data-step-branch. Used by
    the detailed form's first step (get_a_quote_details.py)."""
    opts = "".join(f"""
              <label class="choice choice-block">
                <input type="radio" name="product" value="{value}" required data-step-branch>
                <span>
                  <span class="block font-semibold">{label}</span>
                  <span class="block mt-1 text-micro font-normal choice-note">{desc}</span>
                </span>
              </label>""" for value, label, desc in PRODUCTS)
    return opts


def quote_form(form_id="quote-form", form_name="master_quote", p="q", product=True):
    """The quick quote. Also embedded on home (its own section, and the quiz's
    last step), so ids derive from `form_id` and `p`. `product=False` swaps the
    radio group for a hidden field the quiz fills with its recommendation."""
    success = "quote-success" if form_id == "quote-form" else f"{form_id}-success"
    choose = (F.radio_group(f"{p}-product", "product", "Type of insurance",
                            [(v, l) for v, l, _ in PRODUCTS],
                            hint="Not sure? Pick the closest. The agent can change it.",
                            error="Pick the one closest to what you are after.")
              if product else "")
    extra = "" if product else '<input type="hidden" name="product" value="" data-triage-product>'
    fields = (
        F.row(F.text_field(f"{p}-name", "name", "Your name", autocomplete="name", validate="name",
                           error="Enter your name."),
              F.age_field(f"{p}-age", hint="The biggest factor in the price."))
        + F.row(F.text_field(f"{p}-email", "email", "Email", type="email", autocomplete="email",
                             validate="email", error="Enter a valid email address."),
                F.phone_field(f"{p}-phone", hint="One agent calls, once."))
        + choose
        + F.consent_block(p, C.BRAND, 10)
        + F.submit_block("Get my free quote"))
    return f"""
        <form id="{form_id}" class="mt-6" data-ax-form data-handoff data-silo="site"
              data-form-name="{form_name}" data-success-target="{success}" novalidate>

          {F.scaffold(extra, indent=10)}

          {fields}
        </form>

        {F.success_panel(success, "Got it",
            '''<p class="mt-3 text-slate">
                 A licensed agent will call within %s with quotes from our appointed carriers,
                 carrier names on them.
               </p>
               <p class="mt-3 text-slate">
                 Want sharper numbers on that call? A few more questions about your health and
                 the coverage you want takes about two minutes. Your answers so far are kept.
               </p>''' % C.SLA,
            '''<a class="btn btn-cta" href="/get-a-quote/details/">Answer a few more questions</a>
               <a class="link text-sm inline-block mt-4 sm:mt-0 sm:ml-5" href="/thank-you/">What happens next</a>''',
            icon_size=30, indent=8)}"""


def body():
    # The closing ask. Inset, because a flat navy band here sat directly on the
    # navy footer and read as part of it. The photograph is at the far end of
    # the page from the form, so "no image beside the form" is untouched.
    talk_band = C.banner(
        "term-band",
        "Prefer to talk it through?",
        "A call gets you the same licensed agent and the same comparison, and you can ask the "
        "awkward questions as they come up.",
        C.phone_link("quote_footer", "btn btn-call btn-block !bg-white !text-navy",
                     "Call " + C.PHONE_DISPLAY)
        + '<p class="mt-3 text-sm text-white/75 text-center">%s</p>' % C.HOURS,
        inset=True)

    return f"""
<section class="pt-6 pb-14 md:pb-16 glow">
  <div class="container-ax">
    {C.crumbs([("Home", "/"), ("Get a quote", None)])}

    <div class="mt-8 grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">

      <div class="lg:col-span-5">
        <h1 class="reveal text-h1">Get a free quote</h1>
        <p class="reveal mt-5 text-lead text-slate">
          Answer a few questions and a licensed agent compares our appointed carriers for you.
          No medical exam to get a quote, no Social Security number, and no obligation.
        </p>

        <ul class="reveal mt-8 grid gap-4">
          {"".join('<li class="flex items-start gap-3">%s<span class="text-slate">%s</span></li>'
                   % (icon("circle-check", 20, "shrink-0 mt-0.5 text-green"), t) for t in [
            "One licensed agent calls you once, not six agencies in ten minutes.",
            "Quotes come back with the carrier names on them, so you can check the comparison happened.",
            "We tell you which carriers are likely to decline you before you apply.",
          ])}
        </ul>

        <div class="reveal card mt-8">
          <h2 class="text-h4">Prefer to talk?</h2>
          <p class="mt-2 text-sm text-slate">
            Calling is faster than the form and gets you the same agent.
          </p>
          <div class="mt-4">
            {C.phone_link("quote_sidebar", "btn btn-call btn-block", C.PHONE_DISPLAY, 22)}
          </div>
          <p class="mt-3 text-micro text-muted">{C.HOURS}</p>
        </div>
      </div>

      <!-- The form is the page, so it is the first thing in the reading order
           on desktop's right column and directly under the H1 on mobile. -->
      <div class="lg:col-span-6 lg:col-start-7">
        <div class="panel reveal">
          <div class="panel-head">
            <h2 class="text-h3 !font-display !font-semibold">Start your quote</h2>
            <p class="mt-2 text-sm text-muted">Takes about a minute. Nothing is charged and nothing is binding.</p>
          </div>
          {quote_form()}
        </div>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     WHAT WE WILL ASK. Removing the fear of the unknown before the form,
     for anyone who scrolled instead of starting it.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">What you need for a quote</h2>
      <p class="reveal mt-5 text-slate">
        Less than people expect. Everything below is something you already know without looking
        anything up.
      </p>
    </div>

    <div class="mt-10 bento" data-stagger="40">
      <div class="reveal bento-cell bento-3">
        <p class="eyebrow">We will ask</p>
        <ul class="mt-4 grid gap-3">
          {"".join('<li class="flex items-start gap-3">%s<span class="text-slate">%s</span></li>'
                   % (icon("circle-check", 20, "shrink-0 mt-0.5 text-green"), t) for t in [
            "Your name, age, email, and a phone number a licensed agent can reach you on.",
            "Which kind of insurance you are after: term, whole life, or final expense.",
            "Optional, on the next page: sex as on your birth certificate, health, tobacco, and how much coverage you want. It sharpens the quote.",
          ])}
        </ul>
      </div>
      <div class="reveal bento-cell bento-cell-tint bento-3">
        <p class="eyebrow">We will not ask</p>
        <ul class="mt-4 grid gap-3">
          {"".join('<li class="flex items-start gap-3">%s<span class="text-slate">%s</span></li>'
                   % (icon("circle-x", 20, "shrink-0 mt-0.5 text-muted"), t) for t in [
            "Your Social Security number. That belongs on an application, not a quote.",
            "Your bank or card details. Nothing is charged, at any point, by us.",
            "A medical exam or a doctor's report to produce a quote.",
            "Your full medical history. We ask about the conditions that move a rate.",
          ])}
        </ul>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     WHAT HAPPENS AFTER SUBMIT. Honest call expectation, per T1.
     ================================================================== -->
{C.steps_section("What happens after you submit",
    'Four steps, in order.',
    [("You get one call, from one agency", "A licensed agent from Apex, within " + C.SLA + ". We do not sell your details, so you do not get calls from six agencies who bought them.", "If you would rather we emailed first, say so in the call and we will."),
     ("Ten to twenty minutes on the phone", "Enough to confirm what you sent, ask the two or three health questions that move a rate, and understand what you are trying to cover. Longer if you want to work through the numbers."),
     ("Named carriers and real premiums", "Carrier names, premiums, and the terms that matter, so you can compare them against anything else you have been shown. Including, where it applies, which carriers would decline you and why."),
     ("You decide whether to apply", "There is no policy until you sign an application and a carrier issues it. If you decide against it, you owe nothing and we stop contacting you when you ask.")],
    cls="section")}


<!-- =====================================================================
     WHY QUOTES DIFFER. The objection that makes people distrust every
     number they have already been given.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Why two carriers quote you differently</h2>
      <p class="reveal mt-5 text-slate">
        The same person, on the same day, gets very different prices from different
        carriers. That is normal, and it is the reason comparing is worth the call.
      </p>
    </div>

    <ul class="mt-10 grid md:grid-cols-3 gap-4" data-stagger="40">
      {"".join('''<li class="reveal card">
        <p class="text-h4">%s</p>
        <p class="mt-3 text-slate">%s</p>
      </li>''' % (h, b) for h, b in [
        ("They use different claims data",
         "Each carrier sets rates from its own claims experience. One carrier's data may say a condition matters less than another's does, so the same health history lands in a different rate class."),
        ("They specialize",
         "Some carriers are lenient on controlled diabetes, others on a family history of cancer, others on private aviation. A carrier that is expensive for most people can be the cheapest for you."),
        ("Some check your health more closely",
         "A fully underwritten policy with an exam is usually cheaper than an instant-decision one, because the carrier is pricing with more information and less uncertainty."),
      ])}
    </ul>
  </div>
</section>


<!-- =====================================================================
     SAMPLE RATES. Deliberately NOT behind the form: showing indicative
     numbers before the ask raises completion rather than lowering it.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Sample life insurance rates by age</h2>
      <p class="reveal mt-5 text-slate">
        Nothing on this page is locked behind the form. You should be able to see the shape of
        the numbers before you give anyone your phone number.
      </p>
    </div>

    <div class="reveal mt-8 max-w-3xl">{C.rates_flag("premiums")}</div>

    {C.rate_chart(
        "quote-sample-rates",
        ["Term life, $250,000", "Whole life, $25,000", "Final expense, $10,000"],
        [(band, {"age": mid}) for band, mid in AGE_BANDS], [],
        "Indicative monthly premium by age, non-tobacco, for a representative policy in each product.",
        row_cta="prefill", prefill_target="quote-form", min_width="44rem",
        note="Source: [CARRIER RATE CARD NAME AND EDITION]. Premiums vary by carrier, state, "
             "health, build, family history, and tobacco use. A rate table is an illustration of "
             "shape, not an offer of coverage. Your rate class is decided by the carrier after "
             "underwriting.")}
  </div>
</section>


<!-- =====================================================================
     NO OBLIGATION AND DATA HANDLING. Required by T1, and the last real
     objection before the FAQ.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">
      <div class="lg:col-span-5">
        <div class="sticky-col">
          <h2 class="reveal text-h2">What we do with your details</h2>
          <p class="reveal mt-5 text-slate">Where your details go, what sending them commits you to, and how to stop contact.</p>
        </div>
      </div>
      <div class="lg:col-span-6 lg:col-start-7 bento" data-stagger="40">
        <div class="reveal bento-cell bento-cell-blue bento-6">
          <p class="eyebrow text-white/80">The short version</p>
          <p class="mt-3 text-white/90">
            Your details go to the licensed agent who quotes you and to the carriers we quote on
            your behalf. They are not sold, rented, or passed to other agencies or lead buyers.
          </p>
        </div>
        <div class="reveal bento-cell bento-3">
          <p class="eyebrow">No obligation</p>
          <p class="mt-3 text-slate">
            Submitting this form buys nothing and commits you to nothing. There is no fee, no
            charge, and no policy until you sign an application and a carrier issues it.
          </p>
        </div>
        <div class="reveal bento-cell bento-cell-tint bento-3">
          <p class="eyebrow">Stopping contact</p>
          <p class="mt-3 text-slate">
            Ask us to stop and we stop, on the call or in writing. Consent to be called is separate
            from the form and is never a condition of getting a quote. Full detail is in our
            <a class="link-static" href="/legal/privacy/">privacy policy</a>.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>


{C.faq_section("Common questions about getting a quote", FAQ, "quote-faq")}


{C.testimonials("section band")}

{talk_band}"""
