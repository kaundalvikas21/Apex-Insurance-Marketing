# -*- coding: utf-8 -*-
"""IS WHOLE LIFE WORTH IT. Spec P3, template T4. SOFTEST CTA ON THE SITE.

Spec s05 is explicit: sceptical intent, answer it genuinely INCLUDING "often
not", this earns trust and links, it is NOT a sales page.

Three structural decisions follow from that and should not be quietly undone
later by someone optimising conversion:

  1. The answer is "for most households, no" and it is the first sentence.
  2. The section on who it is NOT for comes BEFORE the section on who it is
     for. A page that leads with the case for and buries the case against is
     a sales page wearing a balanced headline, and this reader can tell.
  3. There is no amber button, no form, and no inline_cta() anywhere on the
     page. The single ask is a text link inside a card near the end, and it
     offers a document rather than a call.

The byline is placed directly under the hero rather than only at the foot,
because on this page the identity of the person making the argument is part of
the argument. That is the deviation recorded in
design-system/pages/whole-is-it-worth-it.md.

No invented rate of return, no cost figure that is not `$--`, and no carrier
named. The critics' numbers and ours would both be arguments rather than
evidence.
"""
import chrome as C
import compare

PATH = "/whole-life-insurance/is-it-worth-it/"
OUT = "whole-life-insurance/is-it-worth-it/index.html"
ACTIVE = "/whole-life-insurance/"
SILO = "whole-life"
TITLE = "Is Whole Life Insurance Worth It? An Honest Look | Apex"
OG_TITLE = "Is whole life insurance worth it?"
DESC = ("For most households, no. Here is who whole life genuinely does suit, what the critics "
        "get right and wrong, and how to check it for yourself. Written by a licensed agent.")

TRAIL = [("Home", "/"), ("Whole Life Insurance", "/whole-life-insurance/"),
         ("Is it worth it?", None)]

NOT_FOR = [
    ("You have a temporary need and a permanent budget problem",
     "A mortgage and young children are a need with an end date. Insuring them with permanent "
     "coverage means buying far less death benefit than the same money would buy in term, at "
     "exactly the point in life when the family is most exposed. Being underinsured in a policy "
     "that lasts forever is worse than being adequately insured in one that expires."),
    ("You have not filled your tax advantaged accounts",
     "If there is unused room in an employer match, a retirement account, or a health savings "
     "account, that room is almost always the better home for the money. A permanent policy is a "
     "reasonable thing to consider after those are full. It is a poor substitute for them."),
    ("You are being sold it as an investment",
     "It is not one, and the language used to sell it that way is the clearest warning sign in "
     "this industry. If the pitch leans on the non guaranteed columns, on a dividend history, or "
     "on being your own bank, the proposal is being judged on the wrong axis and you should ask "
     "to see it judged on the guaranteed columns instead."),
    ("There is a real chance you will not keep it",
     "Whole life is punishing to abandon. The early years go mostly to acquisition costs, so a "
     "policy surrendered in the first several years commonly returns a small fraction of what was "
     "paid in. If the premium is at the edge of affordable, or your income is variable, the "
     "honest question is not whether whole life is good but whether you will still be paying for "
     "it in year eight."),
]

FOR = [
    ("The permanent need", "Someone will depend on your money after you are old",
     "A child with a disability who will need support for their whole life, a dependent adult, or "
     "a special needs trust that has to be funded whenever you die rather than only if you die "
     "young. Term expires. This need does not."),
    ("The estate case", "There will be a bill at death that has to be paid in cash",
     "Estate taxes, a business buy sell agreement, or an illiquid estate where the heirs would "
     "otherwise have to sell the farm, the building, or the company to settle it. The policy is "
     "buying liquidity at a known price rather than growth."),
    ("The behaviour case", "The forced structure is the feature, honestly assessed",
     "Some people accumulate reliably inside a contract with a bill attached and not at all "
     "outside one. If that is genuinely true of you, and you can afford the premium for decades, "
     "the guaranteed component is worth more to you than a theoretically better outcome you would "
     "not have achieved. This argument is real, and it is also the one most often used to sell "
     "policies to people it does not describe."),
]

RIGHT_WRONG = [
    ("What the critics get right",
     "The cost per dollar of death benefit is several times that of term, and for a household with "
     "temporary needs that is the whole ballgame. Early surrender is brutal and is not adequately "
     "explained at the point of sale. Illustrations are routinely presented on their non "
     "guaranteed columns. Commissions on these policies are large and front loaded, which is a "
     "real conflict of interest and one you should assume is present in any conversation about "
     "them, including this one. And &quot;buy term and invest the difference&quot; does beat whole "
     "life for most people over most periods, provided the difference actually gets invested."),
    ("What the critics get wrong",
     "The comparison is usually run against an investor who never panics, never stops "
     "contributing, and never pays tax on a rebalance, which describes very few real households. "
     "The guaranteed cash value floor is treated as worthless when for some people it is the "
     "reason the money survives a bad decade. Permanent needs are dismissed as edge cases when "
     "they are ordinary in families with a dependent who will never be independent. And the "
     "argument frequently assumes the buyer has retirement account room left, which is a fact "
     "about the buyer rather than about the product."),
]

CHECKS = [
    "Name the need, and say whether it has an end date. If it has one, price term for that "
    "length first and compare against it rather than in the abstract.",
    "Confirm every tax advantaged account with unused room is full before permanent coverage "
    "is on the table at all.",
    "Look only at the guaranteed columns of the illustration and ask whether the policy still "
    "makes sense. If it does not, the answer is no, whatever the other columns show.",
    "Ask what the policy returns if you surrender it in year three, year five, and year ten. "
    "Get those numbers in writing from the illustration, not from a conversation.",
    "Ask, in plain words, what the agent is paid on this policy and how that compares with what "
    "they would be paid on the equivalent term policy. A straight answer is a good sign.",
    "Ask yourself whether you will still be paying this premium in year fifteen if your income "
    "drops. If the answer is uncertain, buy less of it or buy none of it.",
]

FAQ = [
    ("Is whole life insurance a good investment?",
     "No, and it is not sold as one by anyone being careful with language. It is insurance with a "
     "guaranteed savings component attached, and the guarantees are paid for with a much higher "
     "premium than term. Judged as an investment against ordinary alternatives it usually looks "
     "poor, because the comparison is against something it is not trying to be. Judged as "
     "permanent coverage with a contractual floor, it is a reasonable product for a small number "
     "of situations."),
    ("Why do financial advisers say to avoid whole life?",
     "Mostly because the majority of people who are pitched it have a temporary need, unused "
     "retirement account room, and a real chance of surrendering the policy early. On those facts "
     "the advice is correct and we would give the same advice. The blanket version of it is less "
     "correct, because permanent needs do exist and are not rare in families with a dependent who "
     "will never be independent."),
    ("Is whole life insurance ever worth it?",
     "Yes, in specific circumstances: a dependency that outlives you, an estate that will owe cash "
     "at death, a business agreement that has to be funded, or an honest assessment that you will "
     "accumulate inside a contract and not outside one. Those are real situations rather than "
     "sales constructs. What matters is whether one of them describes you, and that is a question "
     "with a genuine no available."),
    ("What is the biggest downside of whole life insurance?",
     "The cost, and specifically what the cost does to the amount of coverage you can afford. A "
     "household that would have bought adequate term instead buys a fraction of the death benefit "
     "in whole life, and if the earner dies during the years the children are at home, that "
     "difference is the entire consequence. The second biggest downside is the early surrender "
     "penalty, which turns a change of circumstances into a large realised loss."),
    ("Should I cancel my whole life policy?",
     "Not on the strength of a web page, including this one. If the policy has been in force for "
     "many years the worst of the acquisition cost is already behind you, and surrendering can "
     "crystallise a loss and a possible tax event while leaving you uninsured at an older age. "
     "There are also options between keeping it and cancelling it, including reducing the death "
     "benefit or making it paid up. Get the in force illustration first and have someone read it "
     "with you, and be aware that an agency paid to sell you a replacement has an interest in the "
     "answer."),
]

SIBLINGS = [
    ("/whole-life-insurance/what-is-whole-life-insurance/", "What whole life insurance is",
     "The definition and the mechanics, before the argument."),
    ("/whole-life-insurance/cash-value/", "How cash value works",
     "Guaranteed growth, loans, surrender, and the tax treatment."),
    ("/whole-life-insurance/dividends/", "Dividends explained",
     "Why the non guaranteed columns are not a forecast."),
    ("/whole-life-insurance/calculator/", "Whole life calculator",
     "Size the permanent need, with the method shown."),
    ("/whole-life-insurance/guaranteed-acceptance/", "Guaranteed acceptance",
     "No health questions, and what that costs you."),
    ("/whole-life-insurance/for-seniors/", "Whole life for seniors",
     "Where the arithmetic changes after 65."),
]


WORTH_COST = """<p class="reveal text-slate">
        The honest version of the cost comparison is a large multiple, not a small markup: for the
        same death benefit at the same age, whole life costs several times what term costs, and
        the multiple grows with the length of term you compare against. That is the number that
        decides this for most people, and it is the reason the answer at the top of this page is
        what it is.
      </p>
      <p class="reveal mt-5 text-slate">
        We are not printing a specific multiple, and we are not printing a projected return for
        the money you would have saved. Whichever numbers we picked would be doing the arguing,
        and we would be picking them knowing which way we wanted the comparison to fall. The
        figures that mean anything are the ones on
        <a class="link" href="/whole-life-insurance/rates/">whole life rates by age</a> and
        <a class="link" href="/term-life-insurance/">term life insurance</a> rate cards for your
        own age and health, quoted side by side.
      </p>
      <p class="reveal mt-5 text-slate">
        If you want that comparison run, we will run it and show you both, including in the cases
        where it makes the whole life policy look bad. There is a
        <a class="link" href="/compare/term-vs-whole-life-insurance/">detailed comparison of term
        and whole life</a> if you want the structural version first.
      </p>"""


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    not_for = "".join(
        (('<div class="mt-8">%s</div>' if i else "%s") % C.step(i + 1, t, b))
        for i, (t, b) in enumerate(NOT_FOR))

    for_cells = ""
    for i, (eyebrow, title, text) in enumerate(FOR):
        variant = ["bento-cell-blue", "", "bento-cell-tint"][i]
        navy = i == 0
        for_cells += f"""
      <div class="reveal bento-cell {variant} bento-2">
        <p class="eyebrow{' text-white/80' if navy else ''}">{eyebrow}</p>
        <h3 class="mt-2 text-h4{' text-white' if navy else ''}">{title}</h3>
        <p class="mt-3 {'text-white/90' if navy else 'text-slate'}">{text}</p>
      </div>"""

    rw = "".join(C.qa(h, b, "" if i == 0 else "mt-8") for i, (h, b) in enumerate(RIGHT_WRONG))

    return f"""
{C.page_hero(
    TRAIL,
    "Is Whole Life Insurance Worth It? An Honest Look",
    'For most households, no. The premium buys a fraction of the death benefit the same money '
    'would buy in term, and the majority of people who are pitched '
    '<a class="link" href="/whole-life-insurance/">whole life insurance</a> have a need with an '
    'end date, unused room in a retirement account, or a real chance of giving the policy up early. '
    'For a smaller number of households it is genuinely the right product, for reasons that have '
    'nothing to do with returns. This page is about telling those two groups apart, and we sell '
    'the product, which is a conflict of interest you should hold in mind while reading it.',
    media=C.figure("whole-porch", C.MEDIA_SIZES, eager=True))}


<!-- =====================================================================
     THE BYLINE, PLACED HIGH. Deviation from the standard T4 order,
     recorded in design-system/pages/whole-is-it-worth-it.md. On a page
     whose argument is "here is the case against the thing we sell", who
     is making the argument is part of the argument, and burying that at
     the foot would be the wrong call.
     ================================================================== -->
{C.byline_section(cls="section-tight")}


{C.prose("Who whole life is not for", not_for,
         intro="This comes first on purpose. Four situations, and between them they cover most of "
               "the people who are shown a whole life proposal. If one of these is you, the answer "
               "is no and you can stop reading here.",
         cls="section band")}


<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Who it genuinely is for</h2>
      <p class="reveal mt-5 text-slate">
        Three situations. All three are ordinary rather than exotic, and none of them is about
        beating an index. If one of these describes you, whole life is worth taking seriously and
        we will help you price it properly.
      </p>
    </div>
    <div class="mt-10 bento" data-stagger="40">{for_cells}
    </div>
  </div>
</section>


{C.prose("What the critics get right, and wrong", rw,
         intro="The case against whole life is largely correct, and repeating that here costs us "
               "nothing we should not be paying. The parts of it that are overstated are worth "
               "naming too, because a reader who believes the strong version will also dismiss the "
               "situations where the product is the right answer.",
         cls="section band")}


{C.prose("What it costs, and why we will not print a number", WORTH_COST,
         intro="The comparison that decides this for most people, and why there is no dollar "
               "figure on this page.")}


<section class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">Six checks before you sign anything</h2>
        <p class="reveal mt-5 text-slate">
          Run these against any whole life proposal, including one of ours. An agency that objects
          to any of them has told you something useful.
        </p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
{compare.checklist(CHECKS)}
      </div>
    </div>
  </div>
</section>


<!-- The softest CTA on the site. No amber, no form, no button hierarchy:
     one text link offering a document. Spec s05. -->
<section class="section-tight">
  <div class="container-ax">
    <div class="reveal card measure">
      <h2 class="text-h4">If you want the comparison run properly</h2>
      <p class="mt-3 text-slate">
        We will put a term quote and a whole life illustration for your age next to each other, with
        the guaranteed columns shown separately, and tell you which one we would buy in your
        position. Frequently that is the term policy. We will send it either way, and there is no
        call attached unless you ask for one.
      </p>
      <div class="mt-5 flex flex-wrap items-center gap-4">
        <a class="link-static inline-flex items-center gap-2"
           href="/whole-life-insurance/quotes/">Ask for both, side by side
           {C.icon("arrow-right", 18)}</a>
        {C.phone_link("whole_worth_it_soft", "link-static inline-flex items-center gap-2 text-sm",
                      "or call " + C.PHONE_DISPLAY, 18)}
      </div>
    </div>
  </div>
</section>


{C.spoke_module("Related pages in whole life",
                "The mechanics behind the argument, and the numbers it turns on.", SIBLINGS)}


{C.faq_section("Questions people actually ask about this", FAQ, "whole-worth-faq")}
"""
