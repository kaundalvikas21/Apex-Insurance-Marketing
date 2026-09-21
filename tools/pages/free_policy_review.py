# -*- coding: utf-8 -*-
"""FREE POLICY REVIEW. A checkup of cover the visitor already owns.

The hero is the client's banner photograph. The form sits six sections down,
so the no-image-beside-a-form rule (MASTER.md section 8) is not in play. The
callback form is borrowed from the final expense silo rather than copied.

YMYL note: replacing a life policy is regulated and can hurt the policyholder.
The page never promises a saving, and the "do not cancel anything first"
warning renders visibly, flagged for legal review.
"""
import chrome as C
import final_expense as FE

PATH = "/free-policy-review/"
OUT = "free-policy-review/index.html"
ACTIVE = PATH
SILO = "site"
TITLE = "Free Life Insurance Policy Review | Apex"
OG_TITLE = "Is your life insurance still right for you?"
DESC = ("A free, no-obligation review of the life insurance you already own, by a licensed "
        "independent agent. Wherever you bought it. Nothing has to change.")

TRAIL = [("Home", "/"), ("Free Policy Review", None)]

LEAD = "Get a free, no-obligation policy review from a licensed agent, wherever you bought it."

FAQ = [
    ("Is the review really free?",
     "Yes. There is no charge and no obligation. If you later buy a policy through us, the "
     "insurance company pays our commission out of the premium. You never pay Apex a fee."),
    ("Do I need to have bought my policy from Apex?",
     "No. We review policies bought anywhere: through another agent, through an employer, or "
     "directly from an insurance company."),
    ("Will I be pushed to switch policies?",
     "No. Many reviews end with us telling you to keep exactly what you have. If we think a change "
     "could help, we explain why in writing and the decision is yours."),
    ("When should I review my life insurance?",
     "Once a year is a sensible habit, and any time something big changes: marriage, divorce, a "
     "new child or grandchild, a new home, a new job, or new debt."),
    ("Can you help me convert a term policy to permanent coverage?",
     "Often, yes. Many term policies let you convert to permanent coverage without a new medical "
     "exam, but usually only before a deadline written into the policy. A review is a good time "
     "to find out whether yours has that option and when it ends."),
    ("How long does it take?",
     "Starting takes a few minutes. After you send the form, a licensed agent calls you within "
     + C.SLA + ". Have your policy or your latest statement ready if you can."),
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


def body():
    hero_cta = ('<div class="reveal mt-8"><a href="#review-form" class="btn btn-cta">Request my free review</a>'
                '<p class="mt-3 text-micro text-muted">Free &#183; No obligation &#183; Licensed agents</p></div>')

    what = C.prose(
        "What is a free policy review?",
        C.qa("A checkup for coverage you already own",
             "A licensed agent looks at how your policy works today, not how it was sold to you. "
             "You find out what it covers, how long it lasts, and what it costs you.")
        + C.qa("Nothing has to change",
               "The review is there to give you a clear picture. If your policy is right for you, "
               "we say so and you keep it.", cls="mt-8")
        + C.qa("Plain English, start to finish",
               "No jargon and no sales script. Ask anything, as many times as you need.", cls="mt-8"),
        intro="A fresh look at your life insurance, with no cost and no pressure.")

    # The same connected stepper as the homepage and the hubs' "How to apply".
    steps = C.steps_section(
        "How the free policy review works",
        "Three steps, no pressure.",
        [("file-text", "A few minutes", "Share your policy",
          "Tell us the basics about the coverage you have now. A recent statement helps, but it is "
          "not required."),
         ("search", "We do the work", "We review it with fresh eyes",
          "A licensed agent checks how it fits your life today and explains it plainly, including "
          "any gaps or extra costs."),
         ("circle-check", "Your decision", "Talk through options, only if you want to",
          "If something could be better, we walk you through it. If not, you keep what you have.")],
        cta=("Ready when you are.", "Free, no obligation, and nothing has to change.",
             '<a href="#review-form" class="btn btn-cta">Request my free review</a>'),
        cls="section band")

    return f"""{C.page_hero(TRAIL, "Is your life insurance still right for you?", LEAD, extra=hero_cta,
             banner="review-banner")}
{what}

<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">When a review makes sense</h2>
      <p class="reveal mt-5 text-slate">If any of these sound familiar, it is a good time for a fresh look.</p>
    </div>
    <div class="mt-10 bento" data-stagger="40">
      {_card("Your life changed", "Marriage, a new child, a new home, a new job, a divorce, or new debt can all change how much coverage you need.")}
      {_card("It has been a while", "If you have not looked at your policy in a year or more, check that it still does its job.", tone="bento-cell-tint")}
      {_card("You want to pay less", "Prices and your options change over time. A review shows whether a better fit exists. It does not promise one.")}
      {_card("Your options may expire", "Many term policies can be converted to permanent coverage, but only before a set deadline.")}
    </div>
  </div>
</section>

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
      {_covers("Options", "What choices do you have?",
               ["Term and permanent coverage, compared plainly", "Whether your term policy can be converted", "How a change in health affects your choices"])}
    </div>

    <div class="reveal mt-8 max-w-3xl">
      {C.flag("A policy review does not guarantee a lower premium or approval for new coverage. "
              "Never cancel or stop paying for an existing policy until a new one has been approved "
              "and is in force. Apex does not give tax or legal advice.", "PENDING LEGAL REVIEW")}
    </div>
  </div>
</section>

{steps}

<section class="section" id="review-form">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">
      <div class="lg:col-span-5">
        <div class="sticky-col">
          <h2 class="reveal text-h2">Request your free policy review</h2>
          <p class="reveal mt-5 text-slate">
            Leave four details and a licensed agent will call you. Or skip the form and call us now.
          </p>
          <div class="reveal mt-6">{C.phone_link("policy_review_form", "btn btn-call", "Call " + C.PHONE_DISPLAY)}</div>
          <p class="reveal mt-3 text-micro text-muted">{C.HOURS}</p>
        </div>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <div class="reveal panel">
          {FE.callback_form("pr", "policy_review",
              heading="Tell us where to reach you",
              intro="Four details. Nothing here is a credit check.",
              silo="site", senior=False)}
        </div>
      </div>
    </div>
  </div>
</section>

{C.faq_section("Free policy review questions", FAQ, "review-faq", cls="section band")}
"""
