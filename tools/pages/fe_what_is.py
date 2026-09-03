# -*- coding: utf-8 -*-
"""WHAT IS FINAL EXPENSE INSURANCE. Spec P3, template T4. PHONE FIRST.

The definitional entry point for the silo. Senior accessibility rules apply in
full (html.fe): body at least 18px, tap targets at least 48px, no motion beyond
the opacity reveal, no glow, and every table capped at three columns including
the row header.

This page is deliberately calm and short on structure. Somebody arriving on it
does not yet know what the product is called, so it defines the thing, names
every other name it is sold under, says plainly what it is not, and routes.
"""
import chrome as C

PATH = "/final-expense-insurance/what-is-final-expense-insurance/"
OUT = "final-expense-insurance/what-is-final-expense-insurance/index.html"
ACTIVE = "/final-expense-insurance/"
SILO = "final-expense"
HTML_CLASS = "fe"
TITLE = "What Is Final Expense Insurance? | Apex"
OG_TITLE = "What is final expense insurance?"
DESC = ("Final expense insurance is a small permanent life insurance policy, usually $2,000 to "
        "$50,000, bought to cover a funeral and the bills that follow. What it is, and what it is not.")

TRAIL = [("Home", "/"), ("Final Expense Insurance", "/final-expense-insurance/"),
         ("What it is", None)]

FACTS = [
    ("How much coverage", "Usually $2,000 to $50,000",
     "Enough for a funeral or cremation and the bills that arrive in the weeks after a death. "
     "Not enough to replace an income, and it is not meant to."),
    ("How long it lasts", "Your whole life",
     "It is permanent coverage. As long as the premium is paid, it does not expire and cannot be "
     "cancelled by the carrier because of your age or your health."),
    ("What it costs", "A premium that never rises",
     "The price is set by your age and health when the policy is issued, and it is fixed for life "
     "by the contract. It does not go up as you get older."),
]

NOT = [
    ("It is not a funeral plan or a prepaid funeral",
     "A prepaid funeral is a contract with a funeral home for specific goods and services. Final "
     "expense insurance is a life insurance policy that pays money to a person you name, and that "
     "person decides what to do with it. If you want a specific funeral arranged in advance, you "
     "want a funeral home. If you want your family to have money and choices, you want this."),
    ("It is not burial insurance, exactly, but the names are used for the same thing",
     "Burial insurance, funeral insurance, and final expense insurance almost always describe the "
     "same product. Carriers and agents use whichever name their market uses. There is no "
     "difference in the contract, and anyone who tells you one is better than another is "
     "describing marketing, not coverage. If what you are actually weighing up is this "
     'against a full sized policy, that is a different question and '
     '<a class="link" href="/compare/burial-insurance-vs-life-insurance/">burial insurance '
     'compared with life insurance</a> answers it.'),
    ("It is not guaranteed acceptance unless it says so",
     "Most final expense policies ask a short list of health questions and check a prescription "
     "history, and most people are approved. A guaranteed acceptance policy asks no questions at "
     "all, always has a waiting period, and costs considerably more for the same coverage. They "
     "are different products, and the questions are usually worth answering."),
    ("It is not a way to leave money to your family",
     "Or at least, that is not what it is sized for. The amount is set against a funeral and the "
     "bills that follow it. If your goal is to leave a meaningful inheritance or replace income "
     "someone depends on, that is a larger policy and a different conversation, and we will tell "
     "you so rather than sell you three of these."),
]

COVERS = [
    ("Funeral or cremation", "The service, the casket or urn, the plot or the scattering, the "
     "funeral director's charges, and the transport."),
    ("Medical bills left behind", "Deductibles, co-pays, and the balances that arrive after a "
     "final hospital stay, which frequently outlast the person."),
    ("Small debts and the paperwork", "A credit card balance, the last utility bills, and the "
     "several hundred dollars of certified copies, filings, and legal fees that a death "
     "generates."),
    ("Anything else, honestly", "It is a life insurance payment made to a person, not a voucher. "
     "Your beneficiary can spend it on the mortgage, on travel to the funeral, or on nothing at "
     "all. Nobody supervises it."),
]

FAQ = [
    ("What is final expense insurance?",
     "It is a small permanent life insurance policy, usually between $2,000 and $50,000, bought so "
     "that a funeral and the bills that follow a death do not fall on the family. There is no "
     "medical exam. You answer a short list of health questions, the premium is fixed for life, "
     "and the coverage does not expire. Most policies are arranged in a single phone call."),
    ("What is the difference between final expense and life insurance?",
     "Final expense insurance is life insurance. It is a category of it, defined by being small, "
     "permanent, and underwritten with health questions instead of a medical exam. When people ask "
     "this question they usually mean the difference between it and a large term policy, which is "
     "size and purpose: term replaces an income for a fixed number of years, final expense covers "
     "a funeral for the rest of your life."),
    ("How much final expense insurance do I need?",
     "Enough for a funeral in your area plus a margin for the bills that follow. Funeral costs "
     "vary considerably by region and by what you choose, so the sensible way to size it is to "
     "call two funeral homes near you, ask for their general price list, which they are required "
     "to provide, and add a few thousand dollars. That is a more reliable number than any national "
     "average."),
    ("Who should buy final expense insurance?",
     "Usually someone between 50 and 85 who does not have a large policy already, does not have "
     "savings set aside for a funeral, and does not want the cost to land on their children. It is "
     "also frequently the right product for someone whose health would make a larger policy "
     "expensive or unavailable. If you have substantial savings earmarked for this, you may not "
     "need it at all, and we will say so."),
    ("Can I be turned down for final expense insurance?",
     "For a standard policy with health questions, yes, though it is uncommon and usually relates "
     "to recent serious illness, nursing home residence, or hospice care. Carriers disagree with "
     "each other about the same conditions, so a decline from one carrier is not a decline from "
     "all of them. If no carrier will offer a standard policy, guaranteed acceptance coverage with "
     "a waiting period is normally still available."),
]

SIBLINGS = [
    ("/final-expense-insurance/funeral-insurance/", "Funeral insurance",
     "The same product under another name, and what it covers."),
    ("/final-expense-insurance/burial-insurance/", "Burial insurance",
     "The same product under the name most people search for."),
    ("/final-expense-insurance/for-seniors/", "For seniors",
     "What is available at 60, at 70, and at 80."),
    ("/final-expense-insurance/no-waiting-period/", "No waiting period",
     "Which policies pay from day one, and what decides it."),
    ("/final-expense-insurance/cremation-insurance/", "Cremation insurance",
     "What a cremation costs, and how much coverage fits."),
    ("/final-expense-insurance/for-parents/", "Buying for a parent",
     "How it works when the policy is for your mother or father."),
]


SIZING_IT = """<p class="text-slate">
        Start with what a funeral actually costs where you live, not with a national figure.
        Funeral homes are required to give you a general price list if you ask for one, and two
        calls will give you a real number for your area rather than an average that describes
        nowhere.
      </p>
      <p class="mt-5 text-slate">
        Then add a margin for the bills that arrive afterwards: the medical balances, the last
        utility accounts, and the certified copies and filings a death generates. Most people
        land somewhere between ten and twenty thousand dollars, but the number that matters is
        yours.
      </p>
      <p class="mt-5 text-slate">
        The premium for each amount is set out on
        <a class="link" href="/final-expense-insurance/cost/">what final expense insurance
        costs</a>, by age band and coverage amount, with the carrier rate card and its date named
        on the page.
      </p>"""


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    hero_cta = """<div class="mt-8">
        %s
        <p class="mt-3 text-sm text-muted">%s</p>
      </div>""" % (C.phone_link("fe_whatis_hero", "btn btn-call btn-xl",
                                "Call " + C.PHONE_DISPLAY, 26), C.HOURS)

    facts = ""
    for i, (eyebrow, title, text) in enumerate(FACTS):
        variant = ["bento-cell-blue", "", "bento-cell-tint"][i]
        navy = i == 0
        facts += f"""
      <div class="bento-cell {variant} bento-2">
        <p class="eyebrow{' text-white/80' if navy else ''}">{eyebrow}</p>
        <h3 class="mt-2 text-h4{' text-white' if navy else ''}">{title}</h3>
        <p class="mt-3 {'text-white/90' if navy else 'text-slate'}">{text}</p>
      </div>"""

    covers = "".join(
        '<tr><th scope="row">%s</th><td>%s</td></tr>' % c for c in COVERS)

    nots = "".join(C.qa(h, b, "" if i == 0 else "mt-10") for i, (h, b) in enumerate(NOT))

    return f"""
{C.page_hero(
    TRAIL,
    "What Is Final Expense Insurance?",
    'Final expense insurance is a small permanent life insurance policy, usually between $2,000 '
    'and $50,000, bought so that a funeral and the bills that follow a death do not fall on your '
    'family. There is no medical exam: you answer a short list of health questions, the premium is '
    'fixed for life, and the coverage never expires. It is the same thing sold under the names '
    'burial insurance and funeral insurance, and it is all '
    '<a class="link" href="/final-expense-insurance/">final expense insurance</a>.',
    extra=hero_cta, glow=False,
    media=C.figure("fe-garden-door", C.MEDIA_SIZES, eager=True))}


<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="text-h2">The three things that define it</h2>
      <p class="mt-5 text-slate">
        Everything else about the product follows from these. If a policy you are shown does not
        have all three, it is something different and should be called something different.
      </p>
    </div>
    <div class="mt-10 bento">{facts}
    </div>
  </div>
</section>


<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="text-h2">What the money is normally used for</h2>
      <p class="mt-5 text-slate">
        The policy pays a single cash amount to the person you name. Nobody directs how it is
        spent. These are simply the things it usually goes on.
      </p>
    </div>

    <!-- Two columns including the row header. The senior accessibility rules
         cap these tables at three; this one needs two. -->
    <div class="mt-10 table-scroll table-signature">
      <table class="compare-table" style="min-width:26rem">
        <caption class="sr-only">What a final expense insurance payout is normally used for</caption>
        <thead>
          <tr>
            <th scope="col">What it goes on</th>
            <th scope="col">What that includes</th>
          </tr>
        </thead>
        <tbody>
          {covers}
        </tbody>
      </table>
    </div>
  </div>
</section>


{C.prose("What it is not", nots,
         intro="Four things this product gets confused with. Two of them are sold hard by people "
               "who rely on the confusion.")}


{C.inline_cta(
    "Ask a licensed agent what it would cost you",
    "One call, about fifteen minutes, and no commitment. We will ask your age, your state, and a "
    "short list of health questions, then tell you what carriers would actually offer you. If we "
    "think you do not need this, we will tell you that instead.",
    "fe_whatis_mid", "/final-expense-insurance/quotes/", "Or request a call back",
    phone_first=True, fe=True)}


{C.prose("How much coverage to buy", SIZING_IT,
         intro="Three steps, in this order. The first one is the only one most people "
               "skip, and it is the one that decides the number.",
         media=C.figure("fe-chairs", C.MEDIA_SIZES))}


{C.spoke_module("Related pages in final expense",
                "The rest of the silo, in the order most people need it.", SIBLINGS)}


{C.faq_section("Common questions", FAQ, "fe-whatis-faq", size=24)}


{C.byline_section()}
"""
