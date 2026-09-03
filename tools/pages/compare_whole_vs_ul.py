# -*- coding: utf-8 -*-
"""WHOLE LIFE VS UNIVERSAL LIFE. Spec P3, template T5. NEUTRAL.

*** DO NOT PUBLISH WITHOUT READING THE PROLOGUE COMMENT IN body(). ***

Spec s05 attaches a condition to this page: write it only if the agency can
actually place universal life. It is registered in build.py PAGES and built, and
it is deliberately EXCLUDED FROM THE SITEMAP (see build.py SITEMAP_EXCLUDE)
until the appointments are confirmed. Nothing on the built site links to it for
the same reason.

The universal life path in the two-path CTA routes to /contact/ rather than to a
quote page, because there is no universal life silo on this site and pretending
otherwise would generate exactly the leads the spec condition exists to prevent.

No dollar figure appears anywhere on this page. Universal life outcomes depend
on a credited rate and a cost of insurance schedule that we have no rate cards
for, and an illustrative number here would be a projection presented as a
comparison.
"""
import chrome as C
import compare

PATH = "/compare/whole-life-vs-universal-life/"
OUT = "compare/whole-life-vs-universal-life/index.html"
ACTIVE = "/"
SILO = "compare"
TITLE = "Whole Life vs Universal Life Insurance | Apex"
OG_TITLE = "Whole life vs universal life insurance"
DESC = ("Whole life guarantees the premium, the cash value, and the death benefit. Universal life "
        "trades those guarantees for flexibility. Which one that suits, side by side.")

TRAIL = [("Home", "/"), ("Compare", None), ("Whole life vs universal life", None)]

GATE = """<!-- =====================================================================
     [CONFIRM UL CARRIER APPOINTMENTS BEFORE PUBLISHING - spec s05]

     Spec section 05 attaches a condition to this page: publish it only if
     Apex can actually place universal life. If it ranks and we cannot
     write the product, it generates leads that cannot be served, which is
     worse than not having the page.

     Until that is confirmed:
       - the path is EXCLUDED from sitemap.xml (build.py SITEMAP_EXCLUDE),
       - no page on the built site links to it,
       - the universal life route in the two-path CTA goes to /contact/
         rather than to a quote form.

     To publish: confirm the appointments, delete this comment, remove the
     path from SITEMAP_EXCLUDE in tools/build.py, add the contextual link
     from /whole-life-insurance/, and point the universal life CTA at a
     real destination.
     ================================================================== -->"""

COLS = ["Whole life", "Universal life"]

ROWS = [
    ("The premium", []),
    ("Is it fixed",
     ["Yes. Set at issue and contractually level for life. It cannot rise.",
      "No. There is a target premium, but you can pay more, less, or skip, within limits."]),
    ("What flexibility costs you",
     ["Nothing. There is no flexibility to price.",
      "Underpaying draws on the account value. Sustained underpayment is the single commonest way "
      "these policies fail."]),

    ("The cash value", []),
    ("How it grows",
     ["At a guaranteed rate written into the contract, plus any dividend the carrier declares.",
      "At a rate the carrier credits, above a guaranteed minimum floor. The credited rate moves."]),
    ("Is the schedule guaranteed",
     ["Yes. Every policy year's guaranteed value is printed in the contract at issue.",
      "No. Only the minimum floor is. The illustrated values assume the current credited rate "
      "continues."]),

    ("The death benefit", []),
    ("Is it guaranteed for life",
     ["Yes, as long as the premium is paid, and the premium cannot change.",
      "Only if the policy is funded well enough to sustain the rising cost of insurance, or if it "
      "carries a no lapse guarantee rider."]),
    ("Can you change the amount",
     ["Not upward. Reductions are usually possible.",
      "Yes, within limits, and increases usually require new underwriting."]),

    ("How it can go wrong", []),
    ("The main failure mode",
     ["You cannot afford the premium and surrender early, losing most of what you paid in the "
      "first several years.",
      "The credited rate falls or the cost of insurance rises, the account value is exhausted, and "
      "the policy demands a large catch up premium or lapses. Frequently decades in, at the worst "
      "possible age."]),
    ("What protects you",
     ["The contract. There is nothing to monitor.",
      "An in force illustration requested from the carrier every year or two, and acting on it. "
      "This is real, ongoing work."]),
]

WINS = [
    ("Whole life wins", "When you want the decision to be over",
     "<p>If the point of buying permanent coverage is that it is settled, whole life is the "
     "product that delivers that. The premium cannot rise, the cash value schedule is printed at "
     "issue, and there is nothing to review, monitor, or fund correctly for the next forty years. "
     "You are paying for the absence of homework, and for some buyers that is precisely the "
     "thing worth paying for.</p>"
     "<p class='mt-3'>It is also the better answer when the coverage backs an obligation that "
     "cannot be allowed to fail: a special needs trust, a buy sell agreement, or an estate tax "
     "bill.</p>"),
    ("Universal life wins", "When the premium has to be able to move",
     "<p>If your income is irregular, or the policy needs to absorb a bad year without lapsing, "
     "the flexibility is genuinely valuable rather than a sales feature. Business owners with "
     "uneven cash flow and people funding a policy alongside a variable income are the clearest "
     "cases.</p>"
     "<p class='mt-3'>It can also be the cheaper route to a guaranteed death benefit where a no "
     "lapse guarantee rider is used deliberately and funded to its own schedule, which is a "
     "different product decision from buying universal life for its cash value.</p>"),
]

CHECKS = [
    "Say out loud whether you will actually request and read an in force illustration every year "
    "or two for the next several decades. If not, universal life is carrying a risk you are not "
    "going to manage.",
    "Ask for the whole life illustration's guaranteed columns and judge the policy on those alone. "
    "If it only works on the non guaranteed columns, it does not work.",
    "Ask for the universal life illustration run at the guaranteed minimum credited rate and the "
    "maximum cost of insurance, not just at the current assumptions. Carriers can produce this and "
    "it is the number that matters.",
    "Ask what happens at age 85 and at age 95 under both. Permanent coverage that lapses at 88 was "
    "not permanent coverage.",
    "Check whether the universal life policy carries a no lapse guarantee, what funding schedule "
    "keeps it in force, and what happens to it if you pay late even once.",
    "Confirm every tax advantaged account with unused room is full before either of these is on "
    "the table.",
]

FAQ = [
    ("What is the main difference between whole life and universal life?",
     "Whole life guarantees the premium, the cash value schedule, and the death benefit at issue, "
     "and none of them can move. Universal life unbundles those pieces so the premium can flex and "
     "the cash value grows at a rate the carrier credits rather than a rate it promises. You are "
     "trading certainty for flexibility, and the trade is real in both directions."),
    ("Is universal life insurance a good idea?",
     "It can be, for someone whose premium genuinely needs to move, or where a no lapse guarantee "
     "rider is being used deliberately to buy a guaranteed death benefit at a lower cost than "
     "whole life. It is a poor idea for someone who buys it, files it, and never looks at it "
     "again, which is unfortunately how a large number of these policies have been sold. The "
     "product requires ongoing attention that whole life does not."),
    ("Can a universal life policy lapse even if I pay the premium?",
     "Yes, and this is the most important sentence on this page. If the credited rate falls or the "
     "internal cost of insurance rises faster than the illustration assumed, the account value can "
     "be consumed even while you pay what you were originally told to pay. The policy then asks "
     "for a much larger premium or lapses. Requesting an in force illustration from the carrier "
     "every year or two is how you catch that while it is still fixable."),
    ("Which is cheaper, whole life or universal life?",
     "Universal life usually shows a lower initial premium for the same death benefit, which is "
     "much of its appeal. Whether it is cheaper over forty years depends on what the carrier "
     "actually credits and charges over those forty years, and nobody knows that in advance. "
     "Comparing the initial premiums is comparing one guaranteed number against one assumed one, "
     "which is not a comparison."),
    ("Should I switch from whole life to universal life?",
     "Very rarely, and not without independent advice from someone who is not paid on the "
     "replacement. Surrendering an established whole life policy can crystallise a loss and a "
     "possible tax event, and you would be giving up guarantees for assumptions at an older age. "
     "Get the in force illustration on what you already have before anyone shows you anything new."),
]


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    return compare.render(
        prologue=GATE,
        trail=TRAIL,
        h1="Whole Life vs Universal Life Insurance",
        lead='Both are permanent life insurance, and both build a cash value, so the choice between '
             'them is not really about either of those things. '
             '<a class="link" href="/whole-life-insurance/">Whole life insurance</a> fixes the '
             'premium, the cash value schedule, and the death benefit in the contract at issue, and '
             'none of them can move afterwards. Universal life unbundles those pieces so the '
             'premium can flex and the cash value grows at a rate the carrier credits rather than '
             'one it guarantees, which buys real flexibility and hands you a policy that has to be '
             'monitored for the rest of your life.',
        table_heading="The two contracts, side by side",
        table_intro="Grouped by the part of the policy each row is about. The rows that decide "
                    "this for most people are in the last group.",
        table_caption="Whole life insurance compared with universal life insurance across premium, "
                      "cash value, death benefit, and failure modes",
        table_cols=COLS,
        table_rows=ROWS,
        table_min_width="48rem",
        table_note="Terms, riders, and guarantees differ substantially by carrier, by policy "
                   "series, and by state. This table describes the two product structures, not any "
                   "specific contract. The policy wording governs.",
        cost_heading="What it costs over time",
        cost_intro="This is where a comparison page normally prints two numbers. We are not going "
                   "to, and the reason is the same reason this decision is difficult.",
        cost_blocks="""
        <p class="reveal text-slate">
          A whole life premium is one number, known at issue, unchanged for life. You can put it in
          a spreadsheet on the day you buy and it will still be right in year forty, and the grid it
          comes from is on <a class="link" href="/whole-life-insurance/rates/">whole life
          rates by age</a>.
        </p>
        <p class="reveal mt-5 text-slate">
          A universal life premium is not a number in the same sense. It is a schedule of payments
          into an account that pays for the insurance out of itself, at a cost that rises with your
          age and is credited with interest at a rate the carrier resets. Its true cost over forty
          years depends on decisions the carrier has not made yet. Putting an illustrative figure
          next to the whole life premium would be comparing a guarantee against an assumption and
          presenting both in the same typeface.
        </p>
        <p class="reveal mt-5 text-slate">
          What you can do, and should insist on, is see the universal life policy illustrated twice:
          once at the current assumptions, and once at the guaranteed minimum credited rate with the
          maximum contractual cost of insurance. Carriers can produce both. The gap between those
          two illustrations is the actual size of the decision you are making, and it is frequently
          much larger than buyers expect.
        </p>
        <p class="reveal mt-5 text-slate">
          For whole life, the equivalent discipline is simpler: read the guaranteed columns and
          ignore the rest. How that works, and why the non guaranteed columns are not a forecast, is
          set out on <a class="link" href="/whole-life-insurance/dividends/">dividends and
          participating policies</a>.
        </p>""",
        wins_heading="Where each one genuinely wins",
        wins_intro="Two situations, and they are not close calls. Most people reading this page "
                   "will recognise themselves in one of them within a sentence or two.",
        wins=WINS,
        checklist_heading="Before you choose either",
        checklist_intro="Six checks. The first one is about you rather than the products, and it "
                        "settles this more often than any of the others.",
        checklist_items=CHECKS,
        checklist_aside='<p class="text-sm text-muted">An agency that resists producing the '
                        'guaranteed minimum illustration has answered a different question than '
                        'the one you asked.</p>',
        paths_heading="Where to go from here",
        paths_intro="Two routes, and we would rather you took the one that fits than the one we "
                    "happen to be better at.",
        paths=[
            ("Whole life: guaranteed premium, guaranteed cash value",
             "We place whole life directly. We will send a current illustration from a named "
             "carrier for your age with the guaranteed columns shown separately, and tell you if "
             "the guarantees alone do not support what is being proposed.",
             "/whole-life-insurance/quotes/", "Request a whole life illustration"),
            ("Universal life: flexible premium, and ongoing responsibility",
             "Universal life is not currently one of our published quote paths. Speak to a "
             "licensed agent about whether it fits and whether we can place it, and if we cannot, "
             "we will say so rather than steer you into something else.",
             "/contact/", "Talk to an agent about universal life"),
        ],
        faq_heading="Questions about whole life and universal life",
        faq=FAQ,
        faq_group="cmp-wl-ul-faq")
