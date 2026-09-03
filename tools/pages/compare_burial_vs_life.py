# -*- coding: utf-8 -*-
"""BURIAL INSURANCE VS LIFE INSURANCE. Spec P3, template T5 SIMPLIFIED. NEUTRAL.

Spec s05: low volume, high clarifying value. Its job is routing confused
traffic into the right silo, and both CTAs go to HUBS rather than to quote
pages, because a reader who is still asking this question has not yet decided
which product they want and should not be dropped into a form.

Simplified T5: the table is the standard three column comparison but the worked
cost section is short and structural, because the honest answer to "which costs
more" is "they are different sizes, so the question is wrong". Saying that
clearly is more useful than a cost model.

Neutral page, so both two-path buttons are .btn-cta and neither product is
recommended over the other in the copy.
"""
import chrome as C
import compare

PATH = "/compare/burial-insurance-vs-life-insurance/"
OUT = "compare/burial-insurance-vs-life-insurance/index.html"
ACTIVE = "/"
SILO = "compare"
TITLE = "Burial Insurance vs Life Insurance: What's the Difference? | Apex"
OG_TITLE = "Burial insurance vs life insurance"
DESC = ("Burial insurance is life insurance. It is a small permanent policy sized for a funeral. "
        "How it differs from a full sized policy, and which one your situation calls for.")

TRAIL = [("Home", "/"), ("Compare", None), ("Burial insurance vs life insurance", None)]

COLS = ["Burial insurance", "Full sized life insurance"]

ROWS = [
    ("Typical coverage", ["$2,000 to $50,000", "$100,000 to $2,000,000 and above"]),
    ("What it is bought for",
     ["A funeral or cremation and the bills that follow a death.",
      "Replacing an income, clearing a mortgage, or keeping a household solvent."]),
    ("How long it lasts",
     ["Your whole life. It does not expire.",
      "A fixed term for term policies, or your whole life for permanent ones."]),
    ("Medical exam",
     ["No. A short list of health questions and a prescription check.",
      "Often, though many carriers now waive it for healthy applicants."]),
    ("Typical age at purchase",
     ["50 to 85.", "25 to 60 for term. Any age for permanent."]),
    ("How long it takes to arrange",
     ["Frequently one phone call, and coverage can start quickly.",
      "Days to several weeks, depending on underwriting."]),
    ("Premium over time",
     ["Fixed for life by the contract.",
      "Level during the term, then rising steeply, or level for life on a permanent policy."]),
    ("What it is called elsewhere",
     ["Final expense insurance, funeral insurance, sometimes simplified issue whole life.",
      "Term life insurance, whole life insurance, universal life insurance."]),
]

WINS = [
    ("Burial insurance fits", "Nobody depends on your income any more",
     "<p>The children are independent, the mortgage is gone or nearly gone, and the thing you "
     "actually want to prevent is your family paying for a funeral out of savings or a credit "
     "card. That is a specific, bounded cost, and a small permanent policy sized to it is exactly "
     "the right instrument.</p>"
     "<p class='mt-3'>It is also the practical answer when health or age would make a large policy "
     "expensive or unavailable, because the underwriting is a short list of questions rather than "
     "an exam.</p>"),
    ("Full sized life insurance fits", "Somebody would struggle if your income stopped",
     "<p>A partner who could not cover the mortgage alone, children who are not yet independent, a "
     "business that owes money you personally guaranteed. The amount needed here is a multiple of "
     "an annual income, not the cost of a funeral, and a burial policy would not come close.</p>"
     "<p class='mt-3'>If that describes you, buy the larger policy first. A funeral is comfortably "
     "covered by a policy that is large enough to replace an income; the reverse is not true.</p>"),
]

CHECKS = [
    "Ask whether anyone's monthly bills would become unpayable if your income stopped tomorrow. If "
    "yes, you are looking for full sized life insurance, whatever else you also buy.",
    "Ask what you already have. Employer coverage frequently ends when the job does, so count it "
    "separately from anything you own outright.",
    "Get a real local funeral price rather than a national average. Funeral homes must provide a "
    "general price list on request, and two calls gives you a number that describes your area.",
    "Check whether the policy you are being shown has a waiting period, and what happens if you "
    "die during it. This is the single most common unpleasant surprise in the small policy market.",
    "If you are told a policy is guaranteed acceptance, ask what it costs against a policy with "
    "health questions. Answering the questions is usually worth real money.",
    "Decide who the beneficiary is and tell them the policy exists. A policy nobody knows about is "
    "the most common way any of this fails.",
]

FAQ = [
    ("Is burial insurance the same as life insurance?",
     "Yes. Burial insurance is life insurance, specifically a small permanent policy underwritten "
     "with health questions instead of a medical exam and sized for a funeral. It is also sold as "
     "final expense insurance and funeral insurance, and those three names describe the same "
     "thing. When people ask this question they usually mean the difference between it and a large "
     "policy, and that difference is size and purpose rather than category."),
    ("Which is better, burial insurance or life insurance?",
     "Neither, in the abstract. They answer different questions. If someone depends on your income "
     "you need a policy sized to replace that income, and a burial policy will not do it. If "
     "nobody does, and the concern is a funeral bill landing on your children, a large policy is "
     "more coverage than the situation calls for and you would be paying for it every month. The "
     "question is not which is better but which describes your household."),
    ("Is burial insurance more expensive than regular life insurance?",
     "Per thousand dollars of coverage, yes, usually noticeably so, because there is no medical "
     "exam and the carrier is accepting more uncertainty. In total monthly cost, no, because the "
     "policy is a fraction of the size. That is why comparing the two on premium alone is "
     "misleading in both directions, and why the useful comparison is per thousand of coverage at "
     "the same age."),
    ("Can I have both?",
     "Yes, and it is common. A term policy covering the years the family is dependent, with a "
     "small permanent policy underneath it that never expires, is a sensible structure. The "
     "permanent one is still there after the term one ends, which is usually the point. Whether "
     "it is worth doing depends on the premium for both together, which is a conversation rather "
     "than a rule."),
    ("Do I need burial insurance if I already have life insurance?",
     "Probably not, if the existing policy is large enough and will still be in force when you "
     "die. Two things catch people out: employer provided coverage usually ends with the job, and "
     "a term policy expires on a date, frequently before the funeral it was supposed to help pay "
     "for. Check what you actually own and when it ends before buying anything else."),
]


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    return compare.render(
        trail=TRAIL,
        h1="Burial Insurance vs Life Insurance",
        lead='Burial insurance is life insurance. It is a small permanent policy, usually between '
             '$2,000 and $50,000, underwritten with health questions instead of a medical exam and '
             'sized to cover a funeral and the bills that follow. A full sized life insurance '
             'policy is bought to replace an income or clear a mortgage, and is measured in '
             'hundreds of thousands. The whole of the difference is size and purpose, so the only '
             'question that matters is whether anybody currently depends on your income.',
        table_heading="The two, side by side",
        table_intro="Everything in this table follows from one distinction: one policy is sized "
                    "for a funeral and the other for a household.",
        table_caption="Burial insurance compared with full sized life insurance on coverage, "
                      "purpose, underwriting, and cost over time",
        table_cols=COLS,
        table_rows=ROWS,
        table_min_width="44rem",
        table_note="Product names, coverage limits, and underwriting differ by carrier and by "
                   "state. This table describes the two categories, not any specific policy.",
        cost_heading="Which one costs more",
        cost_intro="The honest answer is that the question is asked the wrong way round, and "
                   "answering it as asked is how people end up with the wrong policy.",
        cost_blocks="""
        <p class="reveal text-slate">
          A burial policy costs less per month than a full sized policy, because it is a small
          fraction of the size. That is the comparison most people make, and on its own it is
          almost meaningless.
        </p>
        <p class="reveal mt-5 text-slate">
          Per thousand dollars of coverage, a burial policy costs noticeably more. There is no
          medical exam, the underwriting is a short questionnaire, and the carrier prices that
          uncertainty in. You are paying a premium for convenience and for access, which is a
          reasonable thing to pay for when access is the constraint, and a poor thing to pay for
          when it is not.
        </p>
        <p class="reveal mt-5 text-slate">
          So the real comparison is not between two premiums. It is between two situations. A
          household that still depends on an earner needs an amount of coverage that only a full
          sized policy provides, and buying three burial policies to get there would cost far more
          than one term policy. A household where nobody depends on the income needs a funeral
          covered, and buying a large policy to do that means paying every month for coverage that
          is not doing anything.
        </p>
        <p class="reveal mt-5 text-slate">
          Both silos publish their own rate tables, with the carrier rate card and its date named
          on the page, so you can see the actual numbers rather than take that on trust:
          <a class="link" href="/final-expense-insurance/cost/">what final expense insurance
          costs</a> and <a class="link" href="/term-life-insurance/rates/">term life insurance
          rates by age</a>.
        </p>""",
        wins_heading="Which one your situation calls for",
        wins_intro="One question decides this, and it is not about age, health, or budget. It is "
                   "about whether anybody's monthly bills currently depend on your income.",
        wins=WINS,
        checklist_heading="Six things to settle first",
        checklist_intro="Work through these before you speak to anybody, including us. Most of "
                        "them take one phone call or one look at a statement.",
        checklist_items=CHECKS,
        paths_heading="Where to go from here",
        paths_intro="Both routes go to the section of the site that covers that product properly, "
                    "not to a form. If you are still deciding, that is the right place to be.",
        paths=[
            ("If nobody depends on your income",
             "Final expense and burial insurance: small permanent coverage sized for a funeral, no "
             "medical exam, a premium fixed for life. The hub covers what it is, what it costs, "
             "and which policies pay from day one.",
             "/final-expense-insurance/", "Go to final expense insurance"),
            ("If somebody does",
             "Term and whole life insurance: coverage sized to replace an income or clear a "
             "mortgage. The term hub carries the rate tables and a calculator that sizes the "
             "amount before you price anything.",
             "/term-life-insurance/", "Go to term life insurance"),
        ],
        faq_heading="Questions about the difference",
        faq=FAQ,
        faq_group="cmp-burial-life-faq")
