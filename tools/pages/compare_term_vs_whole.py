# -*- coding: utf-8 -*-
"""TERM LIFE VS WHOLE LIFE. Spec P1, template T5. NEUTRAL.

The most linked page in the build after the hubs: home, both product hubs, and
five spokes point here. It is the sanctioned cross silo route under spec s07
rule 3, which is why it carries SILO = "compare" and ACTIVE = "/" and why
neither product's CTA weighting applies to it.

Both two-path buttons are .btn-cta. Giving one product the amber and the other
a ghost outline on a page titled "X vs Y" is a recommendation disguised as a
layout decision, and readers can tell. See design-system/pages/compare.md.

No dollar figure appears anywhere on this page. The cost gap between these two
products is the single most important fact on it, and it is also the one we
cannot print until the carrier rate cards land. So the page states the shape
and links the two $-- rate pages rather than inventing a multiple, which is
also what /whole-life-insurance/is-it-worth-it/ does with the same number.
"""
import chrome as C
import compare

PATH = "/compare/term-vs-whole-life-insurance/"
OUT = "compare/term-vs-whole-life-insurance/index.html"
ACTIVE = "/"
SILO = "compare"
TITLE = "Term vs Whole Life Insurance: Which One Do You Need? | Apex"
OG_TITLE = "Term life vs whole life insurance"
DESC = ("Term life covers a period and costs less. Whole life covers your whole life and builds "
        "cash value. Side by side on premium, cash value, and how each one ends.")

TRAIL = [("Home", "/"), ("Compare", None), ("Term vs whole life", None)]

COLS = ["Term life", "Whole life"]

ROWS = [
    ("What you are buying", []),
    ("How long the coverage lasts",
     ["A chosen period: commonly 10, 15, 20, or 30 years. It then expires.",
      "Your whole life, as long as the premium is paid. It does not expire."]),
    ("What happens at the end",
     ["The policy ends. Most term policies never pay a claim, and that is the design rather than "
      "a failure.",
      "The policy pays. That certainty is most of what the extra premium buys."]),
    ("Can you keep it later",
     ["Sometimes. A convertible policy can be turned into permanent coverage without new health "
      "questions, up to a deadline in the contract.",
      "There is nothing to keep it past. It is already permanent."]),

    ("The cost", []),
    ("Premium for the same death benefit",
     ["The lowest cost per dollar of coverage of any life product.",
      "Several times the term premium for the same face amount. Not a markup, a different "
      "product."]),
    ("Can the premium rise",
     ["Not during the level term. At the end of the term it renews annually and rises steeply "
      "every year.",
      "No. It is fixed in the contract at issue and cannot be raised."]),
    ("What you can afford",
     ["Large amounts. This is how a young family insures a full income replacement need.",
      "Smaller amounts for the same money, which is why permanent policies are usually sized to a "
      "specific bounded job."]),

    ("The cash value", []),
    ("Is there any",
     ["No. A term policy has no cash value and no surrender value at any point.",
      "Yes, guaranteed, with a schedule printed in the contract at issue."]),
    ("What it does early on",
     ["Not applicable.",
      "Very little. The first several years build slowly, and surrendering in that window "
      "normally returns less than you paid in."]),
    ("Can you borrow against it",
     ["No.",
      "Yes, and an unpaid loan reduces the death benefit. A policy can collapse under one, which "
      "is the failure mode worth knowing about."]),

    ("How it goes wrong", []),
    ("The main failure mode",
     ["You outlive the term, still need coverage, and are now older and possibly uninsurable. "
      "Missing the conversion deadline is the expensive version of this.",
      "You cannot sustain the premium and surrender early, losing most of what you paid in the "
      "first several years."]),
    ("What protects you",
     ["Matching the term to the obligation, and converting before the deadline if the need turns "
      "out to be permanent.",
      "Buying an amount you can carry through a bad year rather than the largest one you qualify "
      "for."]),
]

WINS = [
    ("Term wins", "When the need has an end date",
     "<p>Most people's largest insurance need is temporary and they can name the year it stops: "
     "the mortgage is paid, the youngest child finishes college, the retirement accounts are "
     "large enough to stand alone. Insuring a temporary need with permanent coverage means "
     "buying far less of it than the need requires, which is the most common and most expensive "
     "mistake in this category.</p>"
     "<p class='mt-3'>Term is also what makes a large death benefit affordable at all. A young "
     "family that needs a full income replaced can buy the amount it actually needs on term "
     "premiums and cannot on permanent ones. Being underinsured in a product with guarantees is "
     "worse than being fully insured in one without them.</p>"),
    ("Whole life wins", "When the need never ends, or the money must be there",
     "<p>Some needs do not expire: a funeral and final bills, a lifelong dependant, an estate "
     "that will owe tax and needs liquidity, a business agreement that has to be funded whenever "
     "the death happens. A policy that expires at 75 does not cover any of them, and buying a new "
     "one at 75 is a different price and a different health conversation.</p>"
     "<p class='mt-3'>It also wins when the guarantee itself is the point. The premium cannot "
     "rise, the coverage cannot expire, and there is nothing to monitor or refund correctly for "
     "the next forty years. For some buyers that settled quality is worth the cost gap, and it is "
     "a legitimate reason rather than a rationalisation.</p>"),
]

CHECKS = [
    "Write down the year your need ends. If you can name one, you are looking at term, and the "
    "rest of this page is detail.",
    "Check that any tax advantaged account with unused room is full before permanent life "
    "insurance is being considered as a place to put money.",
    "Work out the death benefit you actually need first, then the product. Choosing the product "
    "first is how people end up with a permanent policy a third the size of the need it was "
    "bought for.",
    "If you are shown a whole life illustration, judge it on the guaranteed columns alone. If it "
    "only works on the non guaranteed columns, it does not work.",
    "Ask whether the term policy is convertible, to what, and by what deadline. That clause is "
    "worth real money and it is routinely left out of a comparison.",
    "Ask the agent how they are paid on each option. The commission difference between these two "
    "products is large, and an agent who will not answer has answered.",
]

FAQ = [
    ("Is term or whole life insurance better?",
     "Neither is better in general, and any page that tells you one of them is has stopped "
     "describing the products. The question that decides it is whether your need has an end date. "
     "If you can name the year the need stops, term is almost always the right answer and the "
     "cheaper one. If the need genuinely never ends, term will expire underneath it and permanent "
     "coverage is what the job requires."),
    ("Why is whole life so much more expensive than term?",
     "Because a term policy is priced on the chance you die during the term, and most people do "
     "not, so most term policies never pay a claim. A whole life policy is priced on the "
     "certainty that it will pay one eventually, plus the guaranteed cash value it is required to "
     "build along the way. You are not paying more for the same thing, you are paying for a "
     "different thing."),
    ("Can I convert term life insurance to whole life later?",
     "Usually yes, if the policy is convertible, and this is one of the most useful clauses in "
     "life insurance. Conversion lets you turn some or all of the coverage into a permanent "
     "policy without answering new health questions, which matters enormously if your health has "
     "changed. It has a deadline, commonly a stated age or a number of years, and missing it is "
     "irreversible. Ask for the conversion terms in writing before you buy, not afterwards."),
    ("Should I buy term and invest the difference?",
     "It is a sound strategy and it beats whole life for most people on the arithmetic, on one "
     "condition that is doing all the work: you actually invest the difference, every month, for "
     "decades, without touching it. Some people do. Many do not, and they end up with neither the "
     "investment nor the permanent coverage. Be honest about which one you are, because the "
     "answer changes the recommendation."),
    ("Can I have both term and whole life?",
     "Yes, and for a lot of households it is the right structure rather than a compromise. A "
     "small permanent policy covers the part of the need that never goes away, and a large term "
     "policy covers the part that ends when the mortgage does. It usually costs less than "
     "insuring the whole need permanently and covers more than insuring it all on term."),
    ("Does whole life insurance ever make sense for a young person?",
     "Sometimes, and the honest version is that it makes sense less often than it is sold. The "
     "clear cases are a lifelong dependant, a family business that needs funding whenever a death "
     "happens, or a genuine need to lock insurability early where health history already suggests "
     "that will be hard. Buying it in your twenties as a savings vehicle is the case that "
     "deserves the most scepticism, because the early years build very little and the money is "
     "hard to get back."),
]

COST_BLOCKS = """
        <p class="reveal text-slate">
          This is the point where a comparison page normally prints two premiums and a total.
          We are not going to, and the reason is not evasion.
        </p>
        <p class="reveal mt-5 text-slate">
          We hold no carrier rate cards yet, so any figure here would be one we made up. A made up
          number in a comparison is worse than no number, because it does the arguing for you and
          it does it with a fake. Every rate cell on this site is
          <span class="tnum">$--</span> for the same reason, and it will stay that way until real
          rate cards are loaded rather than until it becomes inconvenient.
        </p>
        <p class="reveal mt-5 text-slate">
          What is fair to say is the shape, and the shape is not subtle. For the same death
          benefit at the same age, whole life costs several times what term costs. That gap is
          large enough that it changes what you can afford to insure, which is the real decision
          underneath this page. It is also why the answer is so often term for the big temporary
          need and a small permanent policy beside it, rather than one product for everything.
        </p>
        <p class="reveal mt-5 text-slate">
          When the rate cards land, the numbers will appear on the two pages that own them:
          <a class="link" href="/term-life-insurance/rates/">term life insurance rates by age</a>
          and <a class="link" href="/whole-life-insurance/rates/">whole life insurance rates by
          age</a>. They are kept there rather than reprinted here so there is one place to update
          and one place to be wrong.
        </p>
        <p class="reveal mt-5 text-slate">
          One thing worth adding to any cost comparison you are shown elsewhere: a term premium
          stops when the term does, and a whole life premium usually does not. Comparing thirty
          years of one against a lifetime of the other is comparing two different questions, and
          the honest version of the sum runs to the same end date on both sides.
        </p>"""


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    return compare.render(
        trail=TRAIL,
        h1="Term vs Whole Life Insurance",
        lead='Term life insurance covers you for a set number of years and costs the least per '
             'dollar of coverage. Whole life insurance covers you until you die, cannot expire, '
             'and builds a guaranteed cash value, and it costs several times as much for the same '
             'death benefit. The question that decides between them is not which product is '
             'better, it is whether your need has an end date you can name: if it does, '
             '<a class="link" href="/term-life-insurance/">term life insurance</a> is almost '
             'always the answer, and if it genuinely does not, '
             '<a class="link" href="/whole-life-insurance/">whole life insurance</a> is what the '
             'job requires.',
        table_heading="The two contracts, side by side",
        table_intro="Grouped by the part of the policy each row is about. The rows in the first "
                    "and last groups decide this for most people; the middle two are where the "
                    "arguing usually happens.",
        table_caption="Term life insurance compared with whole life insurance across duration, "
                      "cost, cash value, and failure modes",
        table_cols=COLS,
        table_rows=ROWS,
        table_min_width="46rem",
        table_note="Terms, riders, conversion rights, and guarantees differ substantially by "
                   "carrier, by policy series, and by state. This table describes the two product "
                   "structures, not any specific contract. The policy wording governs.",
        cost_heading="What it costs over time",
        cost_intro="The cost gap is the most important fact on this page and the one we will not "
                   "invent a number for. Here is what we can say, and where the real figures will "
                   "go.",
        cost_blocks=COST_BLOCKS,
        wins_heading="Where each one genuinely wins",
        wins_intro="Two situations, and they are not close calls. Most people reading this page "
                   "will recognise themselves in one of them within a sentence or two.",
        wins=WINS,
        checklist_heading="Before you choose either",
        checklist_intro="Six checks. The first one settles this more often than the other five "
                        "put together, and it takes about a minute.",
        checklist_items=CHECKS,
        checklist_aside='<p class="text-sm text-muted">An agent who will not tell you how they '
                        'are paid on each of these two products has answered a different question '
                        'than the one you asked.</p>',
        paths_heading="Where to go from here",
        paths_intro="Two routes, and we would rather you took the one that fits than the one that "
                    "pays us better. We place both.",
        paths=[
            ("Term life: the most coverage for the money",
             "Six questions and about two minutes. A licensed agent comes back with premiums from "
             "named carriers, and with the conversion terms, so you can see what it would cost to "
             "make the policy permanent later if the need turns out not to end.",
             "/term-life-insurance/quotes/", "Get term life quotes"),
            ("Whole life: coverage that cannot expire",
             "Five questions and about two minutes. You get named carriers and real premiums, "
             "with the guaranteed columns kept visibly apart from the projected ones, and a "
             "straight answer if we think term suits you better.",
             "/whole-life-insurance/quotes/", "Get whole life quotes"),
        ],
        faq_heading="Questions about term and whole life",
        faq=FAQ,
        faq_group="cmp-term-whole-faq")
