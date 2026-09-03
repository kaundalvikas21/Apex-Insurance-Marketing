# -*- coding: utf-8 -*-
"""GET A QUOTE. Spec P0, template T1. The master quote form.

The form is the page. Everything below it exists to answer the objections that
stop someone finishing it, in the order they occur: what will you ask me, what
happens after I submit, why do quotes differ, what do the numbers look like,
and what do you do with my details.

BRANCHING. Step 1 picks the product and the following steps adapt to that
silo's shipped pattern:

    term life       three-step, six fields   (matches the term hub)
    whole life      single step, five fields (matches the whole life hub)
    final expense   short, four fields       (matches the final expense hub)

Mechanically the form holds every branch at once and disables the ones that do
not apply. A disabled <fieldset> is native: collect() in site.js already skips
disabled inputs and FormData already drops them, so a submitted payload only
ever contains the chosen branch. Nothing here needed new validation code.

RADIO NAMES are unique per branch (term_sex, term_tobacco, wl_sex) rather than
shared. site.js validates a radio group by querying the whole form for the
name, so two branches sharing `sex` would attach the error message to whichever
fieldset came first in the DOM, which may be the hidden one. The CRM reads
`product` first and then that branch's keys.

CONSENT is one block on the shared final step, not one per branch. initForm()
binds a single [data-consent] per form, and one consent block is also the
correct reading of the rule: the visitor consents once, immediately above the
submit button they actually press.
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
DESC = ("Compare term life, whole life, and final expense quotes from multiple carriers. "
        "Free, no obligation, no medical exam to get a quote, and no Social Security number.")

PRODUCTS = [
    ("term", "Term life", "Cover a set number of years. Usually the cheapest way to cover a mortgage or children at home."),
    ("whole", "Whole life", "Cover for life, with a level premium and cash value that builds."),
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
     "your prescription and motor vehicle history, but nobody needs it to tell you what a "
     "policy costs. If a site asks for it before showing you a price, leave."),
    ("How many people will call me?",
     "One. A licensed agent from this agency, once, within " + C.SLA + ". We are not a lead "
     "generator: your details are not sold, rented, or passed to other agencies, so you will "
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
    opts = "".join(f"""
              <label class="choice choice-block">
                <input type="radio" name="product" value="{value}" required data-step-branch>
                <span>
                  <span class="block font-semibold">{label}</span>
                  <span class="block mt-1 text-micro font-normal choice-note">{desc}</span>
                </span>
              </label>""" for value, label, desc in PRODUCTS)
    return opts


def quote_form():
    return f"""
        <form id="quote-form" class="mt-6" data-ax-form data-steps data-silo="site"
              data-form-name="master_quote" data-success-target="quote-success" novalidate>

          {F.scaffold(indent=10)}

          <div class="progress-track" aria-hidden="true">
            <span class="progress-seg is-done" data-progress-seg></span>
            <span class="progress-seg" data-progress-seg></span>
            <span class="progress-seg" data-progress-seg></span>
            <span class="progress-seg" data-progress-seg></span>
          </div>
          <p class="text-micro font-semibold text-muted" data-progress-label aria-live="polite">Step 1</p>

          <!-- STEP 1. Shared. Choosing here enables one branch and disables
               the other two. -->
          <fieldset class="step is-active mt-5" data-step="1"
                    data-error="Pick the one closest to what you are after. We can change it on the call.">
            <legend class="field-label">What are you looking for?</legend>
            <div class="choice-col mt-3" role="group">{product_choices()}
            </div>
            <p class="field-error">{F.ERR}<span></span></p>
            <button type="button" class="btn btn-cta btn-block mt-5" data-step-next>Continue</button>
            <p class="mt-3 text-micro text-muted">
              Not sure? Pick the closest. Or
              {C.phone_link("quote_step1", "link-static inline-flex items-center gap-1.5", "call " + C.PHONE_DISPLAY, 16, False)}
              and we will work it out with you.
            </p>
          </fieldset>

          <!-- ============ TERM BRANCH. Three steps, six fields. ============ -->
          <fieldset class="step mt-5" data-step="2" data-step-for="term">
            <legend class="sr-only">Term life, step 2: your age and sex</legend>
            {F.text_field("q-term-age", "age", "How old are you?",
                          hint="Age is the single biggest factor in the price.",
                          inputmode="numeric", validate="age",
                          error="Enter an age between 18 and 85.", indent=12)}
            {F.radio_group("q-term-sex", "term_sex", "Sex as shown on your birth certificate",
                           [("female", "Female"), ("male", "Male")],
                           hint="Carriers rate male and female applicants differently.",
                           error="Choose one so we can price it correctly.", indent=12)}
            <div class="flex gap-3">
              <button type="button" class="btn btn-ghost" data-step-back>Back</button>
              <button type="button" class="btn btn-cta grow" data-step-next>Continue</button>
            </div>
          </fieldset>

          <fieldset class="step mt-5" data-step="3" data-step-for="term">
            <legend class="sr-only">Term life, step 3: state, coverage, and tobacco</legend>
            {F.select_field("q-term-state", "state", "What state do you live in?",
                            '<option value="">Choose your state</option>\n' + C.state_options(),
                            error="Please choose your state.", indent=12)}
            {F.select_field("q-term-coverage", "coverage", "How much coverage?", [
                ("", "Choose an amount"), ("100000", "$100,000"), ("250000", "$250,000"),
                ("500000", "$500,000"), ("750000", "$750,000"), ("1000000", "$1,000,000"),
                ("2000000", "$2,000,000 or more"), ("unsure", "Not sure yet")],
                error="Choose a coverage amount, or pick the closest.", indent=12)}
            {F.radio_group("q-term-tob", "term_tobacco",
                           "Have you used tobacco or nicotine in the last 12 months?",
                           [("no", "No"), ("yes", "Yes")],
                           error="Let us know either way.", indent=12)}
            <div class="flex gap-3">
              <button type="button" class="btn btn-ghost" data-step-back>Back</button>
              <button type="button" class="btn btn-cta grow" data-step-next>Continue</button>
            </div>
          </fieldset>

          <!-- ============ WHOLE LIFE BRANCH. One step, five fields. ======== -->
          <fieldset class="step mt-5" data-step="2" data-step-for="whole">
            <legend class="sr-only">Whole life: age, sex, state, and coverage</legend>
            <div class="grid sm:grid-cols-2 gap-x-4">
              {F.text_field("q-wl-age", "age", "Your age", inputmode="numeric", validate="age",
                            error="Enter an age between 18 and 85.", indent=14)}
              {F.select_field("q-wl-state", "state", "Your state",
                              '<option value="">Choose your state</option>\n' + C.state_options(),
                              error="Please choose your state.", indent=14)}
            </div>
            {F.radio_group("q-wl-sex", "wl_sex", "Sex as shown on your birth certificate",
                           [("female", "Female"), ("male", "Male")],
                           error="Choose one so we can price it correctly.", indent=12)}
            {F.select_field("q-wl-coverage", "coverage", "How much coverage?", [
                ("", "Choose an amount"), ("25000", "$25,000"), ("50000", "$50,000"),
                ("100000", "$100,000"), ("250000", "$250,000"),
                ("500000", "$500,000 or more"), ("unsure", "Not sure yet")],
                error="Choose a coverage amount, or pick the closest.", indent=12)}
            <div class="flex gap-3">
              <button type="button" class="btn btn-ghost" data-step-back>Back</button>
              <button type="button" class="btn btn-cta grow" data-step-next>Continue</button>
            </div>
          </fieldset>

          <!-- ============ FINAL EXPENSE BRANCH. Short, four fields. ======== -->
          <fieldset class="step mt-5" data-step="2" data-step-for="final-expense">
            <legend class="sr-only">Final expense: your name, age, and state</legend>
            {F.text_field("q-fe-name", "name", "Your name", autocomplete="name",
                          validate="name", error="Please tell us your name.", indent=12)}
            <div class="grid sm:grid-cols-2 gap-x-4">
              {F.text_field("q-fe-age", "age", "Your age", inputmode="numeric", validate="age",
                            error="Enter an age between 18 and 85.", indent=14)}
              {F.select_field("q-fe-state", "state", "Your state",
                              '<option value="">Choose your state</option>\n' + C.state_options(),
                              error="Please choose your state.", indent=14)}
            </div>
            <div class="flex gap-3">
              <button type="button" class="btn btn-ghost" data-step-back>Back</button>
              <button type="button" class="btn btn-cta grow" data-step-next>Continue</button>
            </div>
          </fieldset>

          <!-- ============ FINAL STEP. Shared, so consent is asked once,
               immediately above the button the visitor actually presses. ==== -->
          <fieldset class="step mt-5" data-step="4">
            <legend class="sr-only">Last step: how to reach you</legend>
            {F.text_field("q-phone", "phone", "Best number to reach you",
                          hint="One licensed agent calls once. Your number goes nowhere else.",
                          type="tel", autocomplete="tel", validate="phone",
                          error="Enter a 10 digit phone number.", indent=12)}
            {F.text_field("q-email", "email", "Email",
                          hint="Optional. Only used to send the written comparison.",
                          type="email", autocomplete="email", validate="email",
                          error="Enter a valid email address.", required=False, indent=12)}

            {F.consent_block("q", C.BRAND, 12)}

            <div class="flex gap-3">
              <button type="button" class="btn btn-ghost" data-step-back>Back</button>
              <button type="submit" class="btn btn-cta grow">See my quotes</button>
            </div>
            <p class="field-error" data-form-error>{F.ERR}<span></span></p>
          </fieldset>

          <p class="mt-4 text-micro text-muted">
            Free &#183; No obligation &#183; Licensed agents &#183; We never sell your details on
          </p>
        </form>

        {F.success_panel("quote-success", "Got it",
            '''<p class="mt-3 text-slate">
                 A licensed agent is comparing our appointed carriers for what you told us. You
                 will hear from us within %s, and the quote comes back with the carrier names on
                 it, not just a number.
               </p>''' % C.SLA,
            '''%s
               <a class="link text-sm ml-5" href="/thank-you/">What happens next</a>'''
            % C.phone_link("quote_success", "btn btn-call", "Or call " + C.PHONE_DISPLAY),
            icon_size=30, indent=8)}"""


def rate_rows():
    rows = []
    for band, mid in AGE_BANDS:
        prefill = '{"age":"%s"}' % mid
        btn = ('<button type="button" class="btn-row" data-prefill=\'%s\' '
               'data-prefill-target="quote-form">Quote this %s</button>'
               % (prefill, icon("arrow-right", 16)))
        rows.append('<tr><th scope="row">%s</th>'
                    '<td class="tnum">$--</td><td class="tnum">$--</td><td class="tnum">$--</td>'
                    '<td>%s</td></tr>' % (band, btn))
    return "\n            ".join(rows)


def body():
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
            "We tell you which carriers are likely to decline you before you apply, not after.",
          ])}
        </ul>

        <div class="reveal card mt-8">
          <h2 class="text-h4">Would rather just talk?</h2>
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
          <h2 class="text-h3 !font-display !font-semibold">Start your quote</h2>
          <p class="mt-2 text-sm text-muted">Takes about a minute. Nothing is charged and nothing is binding.</p>
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
      <h2 class="reveal text-h2">What you need to hand</h2>
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
            "Your age and the state you live in.",
            "Sex as shown on your birth certificate, because carriers rate it differently.",
            "Whether you have used tobacco or nicotine in the last 12 months.",
            "Roughly how much cover you want, or that you are not sure yet.",
            "A phone number a licensed agent can reach you on.",
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
            "Your full medical history. We ask about the conditions that actually move a rate.",
          ])}
        </ul>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     WHAT HAPPENS AFTER SUBMIT. Honest call expectation, per T1.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">What happens after you submit</h2>
        <p class="reveal mt-5 text-slate">
          Written out because "we will be in touch" is not an answer, and because the gap between
          what a form promises and what actually happens is where most of the distrust in this
          industry comes from.
        </p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        {C.step(1, "You get one call, from one agency",
                "A licensed agent from Apex, within " + C.SLA + ". Not a call centre, not an automated quote engine, and not six agencies who bought your details, because we do not sell them.",
                "If you would rather we emailed first, say so in the call and we will.")}
        <div class="mt-8">
          {C.step(2, "Ten to twenty minutes on the phone",
                  "Enough to confirm what you sent, ask the two or three health questions that actually move a rate, and understand what you are trying to cover. Longer if you want to work through the numbers.")}
        </div>
        <div class="mt-8">
          {C.step(3, "Named carriers and real premiums",
                  "Carrier names, premiums, and the terms that matter, so you can compare them against anything else you have been shown. Including, where it applies, which carriers would decline you and why.")}
        </div>
        <div class="mt-8">
          {C.step(4, "You decide, or you do not",
                  "There is no policy until you sign an application and a carrier issues it. If you decide against it, you owe nothing and we stop contacting you when you ask.")}
        </div>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     WHY QUOTES DIFFER. The objection that makes people distrust every
     number they have already been given.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Why two carriers quote you differently</h2>
      <p class="reveal mt-5 text-slate">
        The same person, on the same day, gets materially different prices from different
        carriers. That is not a mistake, and it is the entire reason comparing is worth the call.
      </p>
    </div>

    <ul class="mt-10 grid md:grid-cols-3 gap-4" data-stagger="40">
      {"".join('''<li class="reveal card">
        <p class="text-h4">%s</p>
        <p class="mt-3 text-slate">%s</p>
      </li>''' % (h, b) for h, b in [
        ("They price risk from different books",
         "Each carrier sets rates from its own claims experience. One carrier's data may say a condition matters less than another's does, so the same health history lands in a different rate class."),
        ("They specialise",
         "Some carriers are lenient on controlled diabetes, others on a family history of cancer, others on private aviation. A carrier that is expensive for most people can be the cheapest for you."),
        ("Underwriting depth varies",
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
      <h2 class="reveal text-h2">What these usually cost</h2>
      <p class="reveal mt-5 text-slate">
        Nothing on this page is gated. The table below is here before the form on purpose, because
        you should be able to see the shape of the numbers before you give anyone your phone number.
      </p>
    </div>

    <div class="reveal mt-8 max-w-3xl">{C.rates_flag("premiums")}</div>

    <div class="reveal mt-8 table-scroll table-signature">
      <table class="rate-table" style="min-width:44rem">
        <caption>Indicative monthly premium by age, non-tobacco, for a representative policy in each product.</caption>
        <thead>
          <tr>
            <th scope="col">Age at application</th>
            <th scope="col" class="tnum">Term life, $250,000</th>
            <th scope="col" class="tnum">Whole life, $25,000</th>
            <th scope="col" class="tnum">Final expense, $10,000</th>
            <th scope="col"><span class="sr-only">Start a quote for this age</span></th>
          </tr>
        </thead>
        <tbody>
            {rate_rows()}
        </tbody>
      </table>
    </div>

    <p class="reveal mt-4 text-micro text-muted max-w-3xl">
      <span class="pill mr-2">Rates last updated: {C.RATES_DATE}</span>
      Source: [CARRIER RATE CARD NAME AND EDITION].
      Premiums vary by carrier, state, health, build, family history, and tobacco use. A rate table
      is an illustration of shape, not an offer of coverage. Your rate class is decided by the
      carrier after underwriting.
    </p>
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
          <h2 class="reveal text-h2">What we do with what you send</h2>
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


{C.faq_section("Before you start", FAQ, "quote-faq")}


<section class="section band-navy on-navy">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-8 items-center">
      <div class="lg:col-span-7">
        <h2 class="reveal text-h2 text-white">Would rather talk it through?</h2>
        <p class="reveal mt-4 text-white/85 max-w-2xl">
          A call gets you the same licensed agent and the same comparison, and you can ask the
          awkward questions as they come up. {C.HOURS}.
        </p>
      </div>
      <div class="lg:col-span-4 lg:col-start-9">
        {C.phone_link("quote_footer", "btn btn-ghost btn-block", "Call " + C.PHONE_DISPLAY)}
      </div>
    </div>
  </div>
</section>"""
