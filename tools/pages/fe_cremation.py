# -*- coding: utf-8 -*-
"""CREMATION INSURANCE. Spec P3, template T4. PHONE FIRST. SHORT BY DESIGN.

Spec s05: short, genuinely useful, phone CTA. The whole value of this page is
one piece of arithmetic the reader cannot easily get elsewhere: a cremation
costs materially less than a burial, so the coverage amount that fits is
smaller, and most people arriving here are about to be quoted for a burial sized
policy they do not need.

That means the page's job is partly to talk the reader DOWN in coverage, which
is why it is short and why there is no rate table on it. It routes pricing to
/final-expense-insurance/cost/, which is a money page and should receive links
rather than send them (spec s07 rule 7).

No cremation cost figure is printed. Regional variation in this category is
large enough that a national average would be actively misleading, and the page
instead tells the reader exactly how to get a real local number in two phone
calls. Senior accessibility rules apply in full (html.fe).
"""
import chrome as C

PATH = "/final-expense-insurance/cremation-insurance/"
OUT = "final-expense-insurance/cremation-insurance/index.html"
ACTIVE = "/final-expense-insurance/"
SILO = "final-expense"
HTML_CLASS = "fe"
TITLE = "Final Expense Insurance for Cremation Costs | Apex"
OG_TITLE = "Insurance for cremation costs"
DESC = ("A cremation costs less than a burial, so the policy that covers it is smaller. How to "
        "size one honestly, and how to get a real price for your own area in two calls.")

TRAIL = [("Home", "/"), ("Final Expense Insurance", "/final-expense-insurance/"),
         ("Cremation insurance", None)]

SIZING = [
    ("Call two crematories or funeral homes near you and ask for the general price list",
     "They are required to give it to you, and you do not have to explain why you want it. Ask "
     "specifically for the direct cremation price and the price of a cremation with a service, "
     "because the gap between those two is often larger than people expect and it is the main "
     "thing that decides your number."),
    ("Add the things the price list leaves out",
     "The urn if you want a particular one, the death certificates, which are charged per copy and "
     "you will need several, transport if the death happens away from home, and any venue or "
     "catering if there is a gathering. This is usually a smaller number than the cremation "
     "itself, but it is not nothing."),
    ("Add a margin for the bills that follow, then stop",
     "Medical balances, the last utility accounts, and the filings a death generates. Once you "
     "have that total, buy that much coverage and not more. Rounding up to the next round number "
     "sounds harmless and is how people end up paying for years for coverage they chose in a "
     "moment rather than sized."),
]

DIFFERENCE = [
    ("The coverage amount is smaller", "A direct cremation is the least expensive option most "
     "funeral homes offer, and a cremation with a service still normally costs well below a "
     "burial with a plot and a headstone. The policy that covers it is correspondingly smaller, "
     "and a smaller policy costs less every month for the rest of your life."),
    ("The policy is otherwise identical", "There is no separate cremation insurance product. It "
     "is an ordinary final expense policy, sized for a cremation. Any agent presenting cremation "
     "insurance as its own special contract is describing a marketing name, and you should ask "
     "them what is different about it, because the answer is nothing."),
    ("The money is not tied to the cremation", "It is a life insurance payment to a person you "
     "name. If they end up choosing a burial after all, or if the cremation costs less than you "
     "planned, they keep the difference. Nothing about the policy obliges anybody to cremate "
     "you."),
]

FAQ = [
    ("Is there such a thing as cremation insurance?",
     "Not as a separate contract. What is sold under that name is an ordinary final expense life "
     "insurance policy sized for a cremation rather than a burial. That distinction matters "
     "because it means you should compare it against every other final expense policy on price "
     "and carrier, not treat it as a specialist product with its own rules."),
    ("How much insurance do I need for a cremation?",
     "Less than you would need for a burial, and the honest answer for your area comes from two "
     "phone calls rather than from a website. Ask two local funeral homes or crematories for their "
     "general price list, which they must provide, and add the death certificates, the urn if you "
     "want a specific one, and a margin for the bills that arrive afterwards. Buy that amount."),
    ("Is cremation insurance cheaper than burial insurance?",
     "The premium is lower because the coverage amount is lower, not because the product is "
     "different. Per thousand dollars of coverage, the rate is the same. So the saving is real, "
     "and it comes entirely from buying a policy sized to what you actually plan to do."),
    ("What if my family chooses a burial instead?",
     "They can. The policy pays a cash amount to the beneficiary you named, and nobody supervises "
     "how it is spent. If they choose a burial, they will simply have to find the difference, "
     "which is worth telling them about while you are alive rather than leaving them to discover "
     "it. If you think a burial is a real possibility, size the policy for the burial."),
    ("Can I buy this if I am already in poor health?",
     "Usually yes. Final expense underwriting is a short list of health questions and a "
     "prescription check rather than an exam, and most people are approved. Carriers disagree with "
     "each other about the same conditions, so if one declines, another may not. If no carrier "
     "will write a standard policy, guaranteed acceptance coverage with a waiting period is "
     "normally still available, and we will tell you plainly which of those you are looking at."),
]

SIBLINGS = [
    ("/final-expense-insurance/for-parents/", "Buying for a parent",
     "How it works when the policy is for your mother or father."),
    ("/final-expense-insurance/what-is-final-expense-insurance/", "What it is",
     "The plain definition, if you are starting from scratch."),
    ("/final-expense-insurance/funeral-insurance/", "Funeral insurance",
     "The same product under another name, and what it covers."),
    ("/final-expense-insurance/burial-insurance/", "Burial insurance",
     "Sizing for a burial instead, which costs more."),
    ("/final-expense-insurance/no-waiting-period/", "No waiting period",
     "Which policies pay from day one, and what decides it."),
    ("/final-expense-insurance/for-seniors/", "For seniors",
     "What is available at 60, at 70, and at 80."),
]


TELL_THEM = """<p class="text-slate">
        Tell whoever you are naming as beneficiary that the policy exists, roughly what it is
        for, and where the paperwork is. A policy nobody knows about is a policy nobody claims,
        and this is by some distance the commonest way final expense coverage fails to do its
        job.
      </p>
      <p class="mt-5 text-slate">
        Tell them you want a cremation, too, and that the policy is sized for one. It is an
        uncomfortable conversation and it takes about four minutes, and it is the difference
        between your family knowing what you wanted and guessing at it in the worst week of their
        lives.
      </p>
      <p class="mt-5 text-slate">
        Premiums by age and coverage amount are on
        <a class="link" href="/final-expense-insurance/cost/">what final expense insurance
        costs</a>, with the carrier rate card and its date named on the page.
      </p>"""


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    hero_cta = """<div class="mt-8">
        %s
        <p class="mt-3 text-sm text-muted">%s</p>
      </div>""" % (C.phone_link("fe_cremation_hero", "btn btn-call btn-xl",
                                "Call " + C.PHONE_DISPLAY, 26), C.HOURS)

    diff = ""
    for i, (title, text) in enumerate(DIFFERENCE):
        variant = ["bento-cell-blue", "", "bento-cell-tint"][i]
        navy = i == 0
        diff += f"""
      <div class="bento-cell {variant} bento-2">
        <h3 class="text-h4{' text-white' if navy else ''}">{title}</h3>
        <p class="mt-3 {'text-white/90' if navy else 'text-slate'}">{text}</p>
      </div>"""

    sizing = "".join(
        (('<div class="mt-10">%s</div>' if i else "%s") % C.step(i + 1, t, b))
        for i, (t, b) in enumerate(SIZING))

    return f"""
{C.page_hero(
    TRAIL,
    "Final Expense Insurance for Cremation Costs",
    'There is no separate cremation insurance policy. What is sold under that name is ordinary '
    '<a class="link" href="/final-expense-insurance/">final expense insurance</a>, sized for a '
    'cremation instead of a burial. Because a cremation costs materially less, the policy is '
    'smaller and the premium is lower, and the single most useful thing this page can do is stop '
    'you buying more coverage than you actually need.',
    extra=hero_cta, glow=False)}


<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="text-h2">What is different, and what is not</h2>
      <p class="mt-5 text-slate">
        One thing changes. Two things do not, and both of them are worth knowing before you speak
        to anybody about this.
      </p>
    </div>
    <div class="mt-10 bento">{diff}
    </div>
  </div>
</section>


{C.prose("How to size it in two phone calls",
         sizing,
         intro="We are not printing a cremation cost figure on this page. What a cremation costs "
               "varies enough between one part of the country and another that a national average "
               "would point you at the wrong number, and this is a case where fifteen minutes of "
               "your own research beats anything we could publish.",
         cls="section band")}


{C.inline_cta(
    "Ask what that amount would cost you a month",
    "One call, about fifteen minutes. Tell us the coverage amount you arrived at, your age and "
    "your state, and answer a short list of health questions, and we will tell you what carriers "
    "would actually offer. If the amount you have picked looks higher than you need, we will say "
    "so.",
    "fe_cremation_mid", "/final-expense-insurance/quotes/", "Or request a call back",
    phone_first=True, fe=True)}


{C.prose("Before you buy anything", TELL_THEM,
         intro="Two conversations, both short. Both are easier now than they will be "
               "for the people who have to guess.",
         media=C.figure("fe-letters", C.MEDIA_SIZES))}


{C.spoke_module("Related pages in final expense",
                "The same product under its other names, and what it costs.", SIBLINGS)}


{C.faq_section("Common questions", FAQ, "fe-cremation-faq", size=24)}


{C.byline_section()}
"""
