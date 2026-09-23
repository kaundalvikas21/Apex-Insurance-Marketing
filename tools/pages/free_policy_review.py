# -*- coding: utf-8 -*-
"""FREE POLICY REVIEW. A checkup of coverage the visitor already owns.

Rebuilt September 2026 from the client team's "unbiased review" artifact. The
page's claim is that a review can end with "keep what you have", so it says how
Apex is paid before it asks for anything, prints what the agent will and will
not do. The disclosure and the form share one section: the disclosure in the
sticky left column, read first, the form beside it, and "never cancel
first" under the form, next to the button it applies to.

The hero is the client's banner photograph. The USP strip separates it from the
form section, so the photograph is never beside the form (MASTER.md section 8).

YMYL note: replacing a life policy is regulated and can hurt the policyholder.
The page never promises a saving, and "never cancel first" renders visibly,
twice, flagged for legal review. "Many reviews end with keep" stays a flagged
placeholder until there is a measured figure behind it.
"""
import chrome as C
import forms as F

PATH = "/free-policy-review/"
OUT = "free-policy-review/index.html"
ACTIVE = PATH
SILO = "site"
TITLE = "Free Life Insurance Policy Review | Apex"
OG_TITLE = "Is your life insurance still right for you?"
DESC = ("A free, no-obligation review of the life insurance you already own, by a licensed "
        "independent agent. Wherever you bought it, and a plain answer even when it is: keep it.")

TRAIL = [("Home", "/"), ("Free Policy Review", None)]

LEAD = ("A free review by a licensed agent, wherever you bought it, with a plain answer "
        "even when that answer is to keep what you have.")

FAQ = [
    ("How do you make money if the review is free?",
     "A carrier pays us a commission if you buy a policy through us. If your review ends with "
     "you keeping what you already have, we are paid nothing for it. You never pay us a fee "
     "either way. We would rather tell you that up front than have you wonder."),
    ("Is the review really free?",
     "Yes. There is no fee, no charge later, and no obligation to buy anything."),
    ("Do I need to have bought my policy from Apex?",
     "No. Most policies we review were bought somewhere else: through another agent, through an "
     "employer, or directly from an insurance company."),
    ("Will I be pushed to switch policies?",
     "No. If your policy still fits, we say so and the review ends there. If a change would "
     "help, we explain why and you decide. If it ever does lead to replacing a policy, state "
     "replacement rules apply and you get the required written notice before any application "
     "is taken."),
    ("Do you need my policy number or Social Security number?",
     "No. We do not ask for either on this form, and an agent does not need them to review "
     "your coverage. If you ever get a call asking for those to \"verify\" a free review, it is "
     "not us."),
    ("When should I review my life insurance?",
     "After any big change in your life, or roughly once a year otherwise. Sooner if you hold a "
     "term policy and have never checked its conversion deadline."),
    ("Can you help me convert a term policy to permanent coverage?",
     "Often, yes, but only inside the window your policy allows. Many term policies let you "
     "convert without a new medical exam before a deadline written into the contract. Checking "
     "that window is one of the first things we look at."),
    ("How long does it take?",
     "Starting takes a few minutes. After you send the form, a licensed agent calls you within "
     + C.SLA + ". Have your policy or your latest statement ready if you can."),
]

WILL = [
    "Read what you actually have, including the parts nobody walked you through.",
    "Tell you plainly when your coverage is already right.",
    "Say which carriers would likely accept you today, and which would not.",
    "Put the comparison in writing if you want it.",
    "Tell you when the honest answer is to stay exactly where you are.",
]
WONT = [
    "Ask you to cancel anything before new coverage is approved and in force.",
    "Charge you a fee, now or later.",
    "Sell, share, or rent your details to another agency.",
    "Read you a script, or call you again after you say no.",
    "Call ourselves financial planners. We are licensed insurance agents.",
]


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ)]


def _card(title, body, tone=""):
    return f"""
        <div class="reveal bento-cell bento-3 {tone}">
          <h3 class="text-h4">{title}</h3>
          <p class="mt-2 text-sm text-slate">{body}</p>
        </div>"""


def _covers(title, lead, points, tone=""):
    items = "".join(
        '<li class="flex items-start gap-2">%s<span>%s</span></li>'
        % (C.icon("check", 18, "shrink-0 text-navy mt-0.5"), p) for p in points)
    return f"""
        <div class="reveal bento-cell bento-2 {tone}">
          <h3 class="text-h4">{title}</h3>
          <p class="mt-2 text-sm text-slate">{lead}</p>
          <ul class="mt-4 grid gap-2 text-sm text-slate">{items}</ul>
        </div>"""


def _pledge(title, points, mark, tone):
    items = "".join(
        '<li class="flex items-start gap-3">%s<span>%s</span></li>'
        % (C.icon(mark, 20, "shrink-0 mt-0.5 " + tone), p) for p in points)
    return f"""
      <div class="reveal card">
        <h3 class="text-h3 !font-display !font-semibold">{title}</h3>
        <ul class="mt-5 grid gap-3 text-slate">{items}</ul>
      </div>"""


def review_form():
    """Two steps: the policy first, contact details second. Step 1 is what lets
    the agent read something real before calling. Nothing leaves the browser
    until the submit on step 2."""
    policy = (
        F.text_field("pr-insurer", "insurer", "Who is the policy with?",
                     hint="Not sure is a fine answer. The agent can work it out with you.",
                     required=False, placeholder="Insurance company name")
        + F.row(
            F.select_field("pr-type", "policy_type", "What kind of policy?",
                           [("unsure", "Not sure"), ("term", "Term life"), ("whole", "Whole life"),
                            ("universal", "Universal life"), ("final-expense", "Final expense or burial"),
                            ("employer", "Through my employer")], required=False),
            F.select_field("pr-amount", "coverage_amount", "Coverage amount",
                           [("unsure", "Not sure"), ("under-25k", "Under $25,000"),
                            ("25k-100k", "$25,000 to $100,000"), ("100k-500k", "$100,000 to $500,000"),
                            ("over-500k", "Over $500,000")], required=False))
        + F.row(
            F.text_field("pr-year", "year_issued", "Year you took it out",
                         hint="Roughly is fine.", required=False, inputmode="numeric",
                         maxlength="4", placeholder="e.g. 2015"),
            F.text_field("pr-premium", "monthly_premium", "What you pay a month",
                         hint="Optional.", required=False, inputmode="decimal",
                         maxlength="8", placeholder="Dollars a month"), tight=True)
        + F.select_field("pr-changed", "life_change", "Has anything changed since you bought it?",
                         [("none", "Nothing has changed, I just want it checked"),
                          ("family", "A new child, grandchild, marriage or divorce"),
                          ("home-debt", "A new home, or new debt"),
                          ("income", "Retired, or a change in income"),
                          ("term-ending", "The term is ending, or I was told it converts")],
                         required=False)
        + f"""
<p class="mt-2 flex items-start gap-2 text-sm text-slate">{C.icon("shield-check", 18, "shrink-0 text-navy mt-0.5")}<span><span class="font-semibold text-navy">What we do not ask for.</span> Your policy number, Social Security number, or bank details. An agent does not need them to review your coverage.</span></p>
<div class="mt-5">{F.next_button()}</div>
<p class="mt-3 text-micro text-muted">No contact details yet. Nothing is sent until step 2.</p>""")
    reach = (
        F.row(F.age_field("pr-age"),
              F.select_field("pr-state", "state", "Your state",
                             '<option value="">Choose your state</option>\n' + C.state_options(),
                             error="Please choose your state."))
        + F.row(F.phone_field("pr-phone", label="Your phone number"),
                F.select_field("pr-time", "call_time", "Best time to call",
                               [("any", "Any time during business hours"), ("morning", "Morning"),
                                ("afternoon", "Afternoon"), ("evening", "Early evening")],
                               required=False))
        + F.file_field("pr-pages", "policy_pages", "Your policy pages, if you have them handy",
                       hint="Optional. The declarations page is the useful one. Skip it and the "
                            "agent will ask on the call instead.")
        + C.flag("This upload handles personal information. Encryption at rest, a retention "
                 "limit and privacy policy coverage are required before it goes live.", "DEV")
        + F.consent_block("pr", C.BRAND, 12)
        + F.submit_block("Request my free review", back=True))
    return f"""
          <div class="panel-head">
            <h2 class="text-h3 !font-display !font-semibold">Request your free policy review</h2>
            <p class="mt-3 text-slate">Two short steps, about five minutes. Tell us about the policy you have, so the agent reads something real before they call.</p>
          </div>

          <form class="mt-6" data-ax-form data-steps data-silo="site" data-form-name="policy_review"
                data-success-target="pr-success" novalidate>

            {F.scaffold(indent=12)}

            {F.progress(2)}

            {F.step(1, "Your policy", policy, first=True)}
            {F.step(2, "Where to reach you", reach)}
          </form>

          {F.success_panel("pr-success", "We have your details",
              '''<p class="mt-3 text-slate">
                   A licensed agent will read what you sent and call you within %s. Nothing changes
                   on your policy because you asked.
                 </p>''' % C.SLA,
              C.phone_link("pr_success", "btn btn-call btn-block", "Or call " + C.PHONE_DISPLAY, 22),
              icon_size=32, indent=10)}"""


def body():
    usps = C.usp_strip([
        ("scale", "Independent agency", "Appointed with several carriers, employed by none"),
        ("user-check", "Paid only if you buy", "So \"keep it\" is an answer we can give"),
        ("handshake", "Free, no obligation", "You never pay us a fee, now or later"),
        ("clock", "Reply within " + C.SLA, "From a named agent, not an auto-responder"),
    ])

    # The disclosure and the ask share one section: how we are paid on the
    # left, read first, and the form beside it, so the reader never has to
    # take the "keep it" promise on trust from a screen away.
    paid = (
        C.qa("A carrier pays us only when you buy",
             "Apex is a licensed insurance agency. A carrier pays us a commission when someone "
             "buys a policy through us. If your review ends with you keeping the policy you "
             "already have, we are paid nothing.", cls="mt-8")
        + C.qa("Keeping it is a common ending",
               "Many of our reviews end exactly that way, and we say so plainly when they do.",
               cls="mt-6")
        + '<div class="reveal mt-4">%s</div>' % C.flag(
            "Replace with the real measured figure, for example \"about X in Y reviews end with "
            "no change\", or delete this sentence. Do not estimate it.")
        + C.qa("No single product to push",
               "We are independent: appointed with several carriers, employed by none. A policy "
               "someone was talked into is a complaint, a chargeback, and a lapse nine months "
               "later. Leaving you in coverage that already works is the better outcome for us "
               "too. And there is no script: if your coverage is right, we say so.", cls="mt-6"))

    form = f"""
<section class="section band" id="review-form">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">
      <div class="lg:col-span-5">
        <div class="sticky-col">
          <h2 class="reveal text-h2">How we get paid, and why we will still tell you to keep what you have</h2>
          <p class="reveal mt-5 text-slate">We should say this before you fill anything in.</p>
          {paid}
          <div class="reveal mt-6">{C.phone_link("policy_review_form", "btn btn-call", "Or call " + C.PHONE_DISPLAY)}</div>
          <p class="reveal mt-3 text-micro text-muted">{C.HOURS}</p>
        </div>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <div class="reveal panel">
          {review_form()}
        </div>
        <div class="reveal mt-8 px-1">
          <p class="font-semibold text-navy">The one rule we repeat on every call: never cancel first.</p>
          <p class="mt-2 text-sm text-slate">Whatever we discuss, do not cancel or stop paying an existing policy until new coverage has been approved and is in force. A gap in coverage is the one outcome a review should never produce.</p>
          <p class="mt-3 text-sm text-muted">A policy review is not financial, tax, or legal advice. We are licensed insurance agents, not financial planners.</p>
          <div class="mt-4">{C.flag("Replacement and advice wording to be approved by counsel.", "PENDING LEGAL REVIEW")}</div>
        </div>
      </div>
    </div>
  </div>
</section>"""

    # The same milestone line as term's "How underwriting works" (C.timeline).
    what = C.prose(
        "What is a free policy review?",
        C.timeline([
            ("What it is", "A checkup for coverage you already own",
             "A licensed agent looks at how your policy works today. You find out what it "
             "covers, how long it lasts, and what it costs you."),
            ("Who it is for", "You do not have to be our customer",
             "Most policies we review were bought somewhere else. We review them the same way."),
            ("How we talk", "Plain English, start to finish",
             "No jargon and no sales script. Ask anything, as many times as you need."),
            ("The outcome", "Nothing has to change",
             "The review is there to give you a clear picture. If your policy is right for you, "
             "we say so and you keep it."),
        ]),
        intro="A fresh look at your life insurance, with no cost and no pressure.")

    clock = C.ask_strip(
        "One item on that list has a deadline",
        "Term conversion windows close. If you hold a term policy and have never checked yours, "
        "ask sooner rather than later.",
        '<a href="#review-form" class="btn btn-ghost">Check my policy</a>')

    # The same connected stepper as the homepage and the hubs' "How to apply".
    steps = C.steps_section(
        "How the free policy review works",
        "Three steps, no pressure.",
        [("file-text", "A few minutes", "Share your policy",
          "Tell us the basics about the coverage you have now. A recent statement helps, but it is "
          "not required, and we never need your policy number."),
         ("search", "We do the work", "We review it with fresh eyes",
          "A licensed agent checks how it fits your life today and explains it plainly, including "
          "any gaps or extra costs."),
         ("circle-check", "Your decision", "Talk through options, only if you want to",
          "If something could be better, we walk you through it. If not, you keep what you have "
          "and we say so.")],
        cta=("Ready when you are.", "Asking for a review does not affect your existing policy.",
             '<a href="#review-form" class="btn btn-cta">Request my free review</a>'),
        cls="section band")

    return f"""{C.page_hero(TRAIL, "Is your life insurance still right for you?", LEAD,
             extra=f"""<div class="reveal mt-8 grid gap-3 max-w-xs">
        <a href="#review-form" class="btn btn-cta btn-block">Request my free review</a>
        {C.phone_link("policy_review_hero", "btn btn-call btn-block", "Call " + C.PHONE_DISPLAY)}
      </div>
      <p class="reveal mt-3 text-micro text-muted">Free &#183; No obligation &#183; We never ask for your policy number</p>""",
             banner="review-banner")}
{usps}
{form}
{what}

<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">When a review makes sense</h2>
      <p class="reveal mt-5 text-slate">If any of these sound familiar, it is a good time for a fresh look.</p>
    </div>
    <div class="mt-10 bento" data-stagger="40">
      {_card("Your life changed", "Marriage, a new child, a new home, a new job, a divorce, or new debt can all change how much coverage you need.")}
      {_card("It has been a while", "If you have not looked at your policy in a year or more, check that it still does the job you bought it for.", tone="bento-cell-tint")}
      {_card("You want to pay less", "Prices and your options change over time. A review shows whether a better fit exists. It does not promise one.")}
      {_card("Your options may expire", "Many term policies can be converted to permanent coverage, but only before a set deadline. Miss it and the option is gone.")}
    </div>
  </div>
</section>
{clock}

<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">What your review covers</h2>
      <p class="reveal mt-5 text-slate">The three things that decide whether your coverage still works for your family.</p>
    </div>
    <div class="mt-10 bento" data-stagger="40">
      {_covers("Protection", "Is the coverage still right?",
               ["Is the amount enough for your family today?", "Does it last as long as you need it to?", "Are your beneficiaries up to date?"])}
      {_covers("Cost", "Are you paying more than you need to?",
               ["Is a better fitting policy available?", "Are you paying for overlapping coverage?", "Will your premium rise later?"],
               tone="bento-cell-tint")}
      {_covers("Options", "What choices do you already have?",
               ["Term and permanent coverage, compared plainly", "Whether your term policy can be converted", "How a change in health affects your choices"])}
    </div>

    <div class="reveal mt-8 max-w-3xl">
      {C.flag("A policy review does not guarantee a lower premium or approval for new coverage. "
              "Never cancel or stop paying for an existing policy until a new one has been approved "
              "and is in force. Apex does not give tax or legal advice. If a review leads to "
              "replacing an existing policy, state replacement rules apply and you will receive the "
              "required notice before any application is taken.", "PENDING LEGAL REVIEW")}
    </div>
  </div>
</section>

{steps}

<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">What we will do, and what we will not</h2>
      <p class="reveal mt-5 text-slate">Printed here so you can hold us to it on the call.</p>
    </div>
    <div class="mt-10 grid md:grid-cols-2 gap-6">
      {_pledge("We will", WILL, "check", "text-green")}
      {_pledge("We will not", WONT, "x", "text-danger")}
    </div>
    <p class="reveal mt-6 max-w-3xl text-sm text-muted">
      If we fall short of any of this, tell us, and tell your state insurance department. Our
      license details are in the footer of every page.
    </p>
  </div>
</section>

{C.faq_section("Free policy review questions", FAQ, "review-faq", cls="section band")}

{C.byline_section("section")}

{C.inline_cta(
    "The worst outcome of a review is finding out you were already fine",
    "It costs you nothing, it changes nothing on your existing policy, and it ends with a "
    "licensed agent telling you plainly where you stand.",
    "policy_review_close", "#review-form", "Request my free review")}
"""
