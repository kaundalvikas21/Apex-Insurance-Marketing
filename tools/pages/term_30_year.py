# -*- coding: utf-8 -*-
"""30 YEAR TERM. Spec P2, template T4, built LEAN.

[VALIDATE VOLUME BEFORE INVESTING IN DEPTH] Spec s10 test 1. Same treatment as
the 20 year page, and the same shared builder in term_length.py.
"""
import chrome as C
import term_length

PATH = "/term-life-insurance/30-year-term/"
OUT = "term-life-insurance/30-year-term/index.html"
ACTIVE = "/term-life-insurance/"
SILO = "term-life"
TITLE = "30-Year Term Life Insurance: Rates & Quotes | Apex"
OG_TITLE = "30 year term life insurance"
DESC = ("Who a 30 year term fits, when the extra decade is worth it, and how to check it "
        "against your own dates. Quotes from multiple carriers, no obligation.")

TRAIL = [("Home", "/"), ("Term Life Insurance", "/term-life-insurance/"),
         ("30 year term", None)]

FAQ = [
    ("How much more does a 30-year term cost than a 20-year term?",
     "Meaningfully more, and the gap widens sharply with age. At thirty the extra decade is often "
     "a modest addition because the added years of risk are still young ones. At fifty the same "
     "ten years land in your seventies, where the risk is concentrated, and the difference stops "
     "being modest. The rates page lets you switch between both lengths, so you can read the "
     "difference for your own age."),
    ("Is a 30-year term worth it?",
     "It is worth it when a need genuinely runs past twenty years: a new thirty year mortgage, a "
     "child under about eight, or a partner much younger than you who would depend on your income. "
     "It is poor value when bought as insurance against uncertainty. You pay for a "
     "decade of coverage during which, in most households, nobody depends on the income anymore."),
    ("What is the maximum age for a 30-year term policy?",
     "Most carriers stop offering thirty year terms somewhere in the mid fifties, because the "
     "policy would otherwise run into the mid eighties. Above that age the grid thins out quickly "
     "and the sensible options become a twenty or a fifteen. Availability varies by carrier and by "
     "state, which is one phone call rather than an afternoon of research."),
    ("Should I buy a 30-year term or two shorter policies?",
     "Layering, meaning a large twenty year policy alongside a smaller thirty year one, is often "
     "cheaper than a single thirty year policy for the whole amount. The part of your "
     "need that ends sooner is only insured for as long as it exists. It also means two policies "
     "and two renewal dates. We will quote it both ways so you can see the difference."),
]

SIBLINGS = [
    ("/term-life-insurance/20-year-term/", "20 year term",
     "The shorter length, and the math that decides between them."),
    ("/term-life-insurance/level-term/", "Level term explained",
     "What the thirty years guarantees, and what follows."),
    ("/term-life-insurance/what-is-term-life-insurance/", "What term life insurance is",
     "The plain definition, if you are starting from scratch."),
    ("/term-life-insurance/no-medical-exam/", "No medical exam term",
     "Faster underwriting, and what it does to your health class."),
    ("/term-life-insurance/for-seniors/", "Term life after 60",
     "What is still available, and when to stop looking at term."),
    ("/term-life-insurance/10-year-term/", "10 year term",
     "Short obligations, and how the price rises at renewal."),
]


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    return term_length.render(
        years=30,
        h1="30-Year Term Life Insurance",
        lead=(
            'A thirty year term is the longest most carriers write. It keeps you covered '
            'past the point where a twenty year term would end.'),
        answer=(
            'It costs meaningfully more than twenty years of the same <a class="link" '
            'href="/term-life-insurance/">term life insurance</a>. For a thirty year '
            'old with a new mortgage and young children, it is frequently still less than '
            'people assume. The question is whether your obligations run that '
            'far.'),
        fits=[
            ("The common case", "A mortgage taken out in the last few years",
             "A thirty year loan signed recently calls for a thirty year term. Matching the two "
             "means the policy and the debt end together. You never have to make this "
             "decision again at an age where it is more expensive."),
            ("The family case", "A child under about eight",
             "Thirty years takes a five year old to thirty five. That is longer than most "
             "households need. So this case is really a child under eight plus a "
             "second reason, usually the mortgage or a partner who left work to raise them."),
            ("The age gap case", "A partner considerably younger than you",
             "If your partner would depend on your income until their own retirement "
             "rather than yours, measure the need from their age, not yours. This is the case "
             "where a thirty year term is most often worth its price."),
        ],
        dates_intro="Thirty years is a long time to pay for, so the test is stricter than for a "
                    "shorter term. Buy it for a date you can name, not for a "
                    "feeling that longer is safer.",
        dates=[
            ("Write down the year each obligation ends",
             "Mortgage payoff, youngest child's independence, any private loan or guarantee, and "
             "the year a pension or Social Security would start replacing your income. Four dates, "
             "most of which you can look up."),
            ("Compare the furthest date against twenty years from today",
             "If everything lands inside twenty years, a thirty year term is paying for a decade "
             "in which nobody depends on you. If one obligation runs past it, the choice is "
             "between the longer term and layering two policies."),
            ("Price the layered version before deciding",
             "A large twenty year policy plus a smaller thirty year one fits a real household's "
             "needs more closely than one flat amount for thirty years. It is often "
             "cheaper. Ask us to quote it both ways, because the saving only shows up when you "
             "see the two side by side."),
        ],
        cost_note="A thirty year term prices thirty years of risk from the issue date, and the "
                  "last ten of those years carry most of it. That is why the gap over a twenty "
                  "year policy is small at thirty and large at fifty. It is also why the same carrier "
                  "can be competitive at one age and uncompetitive at the other.",
        faq=FAQ,
        siblings=SIBLINGS,
        cta_heading="Price twenty and thirty years side by side",
        cta_body="We quote both lengths on the same application, so you can see what the extra "
                 "decade costs. Six questions, and a licensed agent comes "
                 "back with premiums from named carriers.",
        where="term_30y_mid")
