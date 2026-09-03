# -*- coding: utf-8 -*-
"""FINAL EXPENSE QUOTES. Spec P1, template T1, INVERTED. PHONE FIRST.

T1 says the form is the page. In this silo that is wrong, and the spec says so:
final expense is phone weighted everywhere, and the buyer is 60 to 85. So the
hero's primary action is a full width click-to-call at the fe button scale, and
the four field callback form sits beside it as the secondary.

Everything else about T1 is kept, because the objections it answers are the
same ones: what you need to hand, what actually happens after you press the
button, what the numbers roughly look like before you give us anything, and
what we do with what you send.

The sample cost table is deliberately NOT gated and stays at three columns,
with the row level click-to-call inside the age cell, which is what
rate_chart's "call" mode exists for.

Senior accessibility rules apply in full (html.fe).
"""
import chrome as C
import final_expense as FE
from icons import icon

PATH = "/final-expense-insurance/quotes/"
OUT = "final-expense-insurance/quotes/index.html"
ACTIVE = "/final-expense-insurance/"
SILO = "final-expense"
HTML_CLASS = "fe"
TITLE = "Final Expense Insurance Quotes | Free, No Obligation"
OG_TITLE = "Get final expense insurance quotes"
DESC = ("Get free final expense insurance quotes from multiple appointed carriers. No medical "
        "exam, no obligation, and no policy until you sign. One call, about fifteen minutes.")

AGE_BANDS = [("50 to 59", None), ("60 to 64", None), ("65 to 69", None), ("70 to 74", None),
             ("75 to 79", None), ("80 to 85", None)]

FAQ = [
    ("How long does it take to get a quote?",
     "One call, about fifteen minutes. We ask your age, your state, the coverage amount you have "
     "in mind, and a short list of health questions, and you hear what carriers would offer "
     "before you hang up. If you use the form instead, a licensed agent calls you back within " +
     C.SLA + "."),
    ("Do I have to take a medical exam?",
     "No. Final expense is sold on health questions and a prescription check rather than an exam. "
     "Nobody visits your home, nobody takes blood, and there is no appointment to keep. Answer "
     "the questions honestly: they are verified against prescription records, and a surprise "
     "there costs you the policy rather than just the rate."),
    ("Is this a real quote or an estimate?",
     "What you get on the call is a quoted premium from a named carrier, based on your answers. "
     "The final premium is confirmed by the carrier when it reviews the application. We tell you "
     "which carrier, which health class, and whether any waiting period applies, so you can see "
     "exactly what would change the number."),
    ("Do I have to buy anything?",
     "No. There is no fee for the quote and no policy until you sign an application and a carrier "
     "issues it. You can stop at any point, including after you have applied and been approved."),
    ("Will my details be sold to other agencies?",
     "No. Your details go to the licensed agent who quotes you and to the carriers we quote on "
     "your behalf. We are an agency, not a lead generator, so there is nothing for us to gain by "
     "selling them and we do not. You will not get six calls from six companies."),
]


def schema():
    return [
        C.org_schema(),
        C.breadcrumbs([("Home", "/"), ("Final Expense Insurance", "/final-expense-insurance/"),
                       ("Quotes", None)]),
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": "Final expense insurance quotes",
            "serviceType": "Final expense life insurance brokerage",
            "provider": {"@id": C.DOMAIN + "/#agency"},
            "areaServed": {"@type": "Country", "name": "United States"},
            "description": ("Free, no obligation final expense insurance quotes compared across "
                            "multiple appointed carriers by a licensed independent agency. No "
                            "medical exam."),
            "url": C.DOMAIN + PATH,
            # [PLACEHOLDER] No Offer node and no price. We do not have carrier
            # rate cards yet, and a price in structured data is a price claim.
        },
    ]


def hand_item(label, why):
    return f"""<li class="reveal flex items-start gap-3">
          {icon("circle-check", 22, "shrink-0 text-green mt-1")}
          <span><span class="font-semibold text-ink">{label}.</span>
          <span class="text-slate">{why}</span></span>
        </li>"""


def body():
    return f"""
<!-- =====================================================================
     HERO. T1 inverted for the silo's phone weighting: the call is the
     primary action and the four field form is the secondary. No glow and
     no photograph, per the fe rules and per T1.
     ================================================================== -->
<section class="pt-6 pb-14 md:pb-16">
  <div class="container-ax">
    {C.crumbs([("Home", "/"), ("Final Expense Insurance", "/final-expense-insurance/"),
               ("Quotes", None)])}

    <div class="mt-8 max-w-3xl">
      <h1 class="reveal text-h1">Get Final Expense Insurance Quotes</h1>
      <p class="reveal mt-5 text-lead text-slate">
        One call, about fifteen minutes, and you will know what
        <a class="link" href="/final-expense-insurance/">final expense insurance</a> would cost
        you and which carriers would take you. There is no medical exam and no obligation. If you
        would rather we called you, leave four details in the form and a licensed agent will ring
        back.
      </p>
    </div>

    <div class="mt-10 grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">

      <div class="lg:col-span-6">
        <div class="reveal card">
          <h2 class="text-h3 !font-display !font-semibold">Call and get an answer today</h2>
          <p class="mt-4 text-slate">
            You will speak to a licensed agent, not a call centre. Have your age, your state, and
            the medications you take to hand and that is all we need to price it.
          </p>
          <div class="mt-8">
            {C.phone_link("fe_quotes_hero", "btn btn-call btn-xl btn-block",
                          "Call " + C.PHONE_DISPLAY, 26)}
            <p class="mt-3 text-sm text-muted">{C.HOURS}</p>
          </div>

          <ul class="mt-8 pt-8 border-t border-rule grid gap-4">
            <li class="flex items-start gap-3">{icon("circle-check", 22, "shrink-0 text-green mt-1")}<span>No medical exam, ever</span></li>
            <li class="flex items-start gap-3">{icon("circle-check", 22, "shrink-0 text-green mt-1")}<span>Multiple carriers compared, not one</span></li>
            <li class="flex items-start gap-3">{icon("circle-check", 22, "shrink-0 text-green mt-1")}<span>One agency calls you, not six</span></li>
            <li class="flex items-start gap-3">{icon("circle-check", 22, "shrink-0 text-green mt-1")}<span>No fee, and no obligation to buy</span></li>
          </ul>
        </div>
      </div>

      <div class="lg:col-span-5 lg:col-start-8" id="quote">
        <div class="reveal panel">
          {FE.callback_form(
              "feq", "fe_quotes_page",
              heading="Or ask us to call you",
              intro="Leave four details and a licensed agent will call you back within " +
                    C.SLA + ". Nothing here is a credit check, and none of it affects your "
                    "credit score.")}
        </div>
      </div>

    </div>
  </div>
</section>


<section class="border-y border-rule bg-surface">
  <div class="container-ax py-6">
    <div class="flex flex-wrap items-center justify-between gap-x-8 gap-y-3 trust-strip">
      <span class="inline-flex items-center gap-2 text-navy font-semibold">{icon("shield-check", 22)}Licensed in {C.STATES} states</span>
      <span class="inline-flex items-center gap-2">{icon("handshake", 22, "text-navy-700")}Independent, appointed with {C.CARRIERS} carriers</span>
      <span class="inline-flex items-center gap-2">{icon("clock", 22, "text-navy-700")}Reply within {C.SLA}</span>
      <span class="inline-flex items-center gap-2">{icon("file-text", 22, "text-navy-700")}No fee, ever</span>
    </div>
  </div>
</section>


<!-- =====================================================================
     WHAT YOU NEED TO HAND. T1.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">What you need to hand</h2>
        <p class="reveal mt-5 text-slate">
          Four things, and you probably know three of them without looking. You are not applying
          yet, so we are not asking for anything an application would ask for.
        </p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <ul class="grid gap-5">
          {hand_item("Your age", "Your age at application, not your birthday. It is the biggest single factor in the premium, and the premium is then fixed for life.")}
          {hand_item("Your state", "Carriers are licensed state by state, and the same policy is not priced identically everywhere.")}
          {hand_item("Roughly how much coverage", "A round number is fine. Most policies in this category are written between ten and twenty five thousand dollars.")}
          {hand_item("The medications you take", "The bottle labels are enough. This is what decides which carriers will write you at the best rate, and it is the question people most often guess at.")}
        </ul>
        <p class="reveal mt-6 text-slate">
          We do not ask for your Social Security number or your bank details to give you a quote.
          Those are asked for on an application, after you have decided, and not before. Anyone
          who asks for them first is doing something else.
        </p>
      </div>
    </div>
  </div>
</section>


{C.post_submit_section([
    ("You get one call, from one agency",
     "A licensed agent from Apex, within " + C.SLA + ". Not a call centre, not an automated quote "
     "engine, and not six agencies who bought your details, because we do not sell them.",
     "If a call is difficult for you, tell us on the form and we will write instead."),
    ("About fifteen minutes on the phone",
     "We confirm what you sent, ask the health questions the carriers ask, and go through which "
     "companies would write you. You can stop the call at any point.", None),
    ("Named carriers, real premiums, and any waiting period",
     "You hear the carrier name, the monthly premium, and whether the policy pays in full from "
     "day one or has a waiting period. That last part is the one that gets left out elsewhere, "
     "and it is the one that matters most.", None),
    ("You decide, or you do not",
     "There is no policy until you sign an application and a carrier issues it. If you decide "
     "against it, you owe nothing and we stop contacting you when you ask.", None),
], intro="Written out because \"we will be in touch\" is not an answer, and because the gap "
         "between what a form promises and what actually happens is where most of the distrust "
         "in this industry comes from.",
   media=C.figure("fe-path", C.MEDIA_SIZES))}


<!-- =====================================================================
     WHY QUOTES DIFFER. T1's objection section. Static cards: no bento
     cascade on an fe page.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2">Why two carriers quote the same person differently</h2>
      <p class="reveal mt-5 text-slate">
        This is the whole reason to use an independent agency rather than ring one company. The
        carriers are not working from one price list. They disagree about who they want to insure,
        and on this product they disagree loudly.
      </p>
    </div>

    <div class="mt-10 grid md:grid-cols-3 gap-6">
      <div class="card">
        <h3 class="text-h4">Their health questions differ</h3>
        <p class="mt-3 text-slate">
          A condition that is a straight decline at one carrier is a standard acceptance at
          another. There is no common list, which is why the answer to "will anyone take me" is
          almost always yes, at some price.
        </p>
      </div>
      <div class="card">
        <h3 class="text-h4">Waiting periods are not standard</h3>
        <p class="mt-3 text-slate">
          Two carriers can look at the same health history and one offers a policy that pays in
          full from day one while the other offers a graded one. That difference is worth more
          than a few dollars of premium.
        </p>
      </div>
      <div class="card">
        <h3 class="text-h4">They price age bands differently</h3>
        <p class="mt-3 text-slate">
          A carrier that wants more seventy year olds prices that band sharply and prices the rest
          ordinarily. Which band you are in changes who is cheapest for you.
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
     SAMPLE COSTS. Deliberately NOT gated (T1). Three columns including the
     row header, with the click-to-call inside the age cell.
     ================================================================== -->
<section class="section" id="rates">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2">Rough shape of the premiums</h2>
      <p class="reveal mt-5 text-slate">
        Shown before you tell us anything, not after. The structure below is what a real cost
        chart looks like; the numbers arrive when our carrier rate cards do.
      </p>
      <div class="reveal mt-6">
        {C.rates_flag("premiums")}
      </div>
    </div>

    {C.rate_chart(
        panels_id="fe-quote-rates",
        cols=["$10,000", "$25,000"],
        rows=AGE_BANDS,
        toggles=[("Show premiums for", "feq-rate-sex",
                  [("female", "Female"), ("male", "Male")], None)],
        caption="Monthly premium by age band and coverage amount.",
        row_cta="call",
        cta_location="fe_quotes_rate_row",
        min_width="26rem",
        top_margin="mt-8",
        aside="Non tobacco, level benefit. Tobacco rates are higher.")}

    <p class="reveal mt-8 text-slate max-w-3xl">
      The fuller picture, including what moves the premium and how to bring one down, is on
      <a class="link" href="/final-expense-insurance/cost/">what final expense insurance costs</a>.
      If you have been told you need a waiting period, read
      <a class="link" href="/final-expense-insurance/no-waiting-period/">burial insurance with no
      waiting period</a> before you apply anywhere.
    </p>
  </div>
</section>


{C.no_obligation_section(
    short_version="Your details go to the licensed agent who quotes you and to the carriers we "
                  "quote on your behalf. They are not sold, rented, or passed to other agencies "
                  "or lead buyers.",
    no_obligation="Asking for a quote buys nothing and commits you to nothing. There is no fee, "
                  "no charge, and no policy until you sign an application and a carrier issues it.",
    stopping_contact="Ask us to stop and we stop, on the call or in writing. Consent to be called "
                     "is separate from the form and is never a condition of getting a quote. "
                     "Full detail is in our "
                     "<a class=\"link-static\" href=\"/legal/privacy/\">privacy policy</a>.")}


{C.faq_section("Before you call", FAQ, "fe-quotes-faq", size=24)}
"""
