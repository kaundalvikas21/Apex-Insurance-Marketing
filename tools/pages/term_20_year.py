# -*- coding: utf-8 -*-
"""20 YEAR TERM. Spec P2, template T4, built LEAN.

[VALIDATE VOLUME BEFORE INVESTING IN DEPTH] Spec s10 test 1. The structure
lives in term_length.py, which this page and the 30 year page share.
"""
import chrome as C
import term_length

PATH = "/term-life-insurance/20-year-term/"
OUT = "term-life-insurance/20-year-term/index.html"
ACTIVE = "/term-life-insurance/"
SILO = "term-life"
TITLE = "20-Year Term Life Insurance: Rates & Quotes | Apex"
OG_TITLE = "20 year term life insurance"
DESC = ("Who a 20 year term actually fits, how to check the length against your own dates, and "
        "where to see rates by age. Quotes from multiple carriers, no obligation.")

TRAIL = [("Home", "/"), ("Term Life Insurance", "/term-life-insurance/"),
         ("20 year term", None)]

FAQ = [
    ("How much is a 20-year term life insurance policy?",
     "It depends far more on your age and health than on the twenty. The same policy is a "
     "different order of magnitude at thirty five and at sixty, and tobacco use roughly doubles or "
     "triples it at any age. Our rates page carries the full grid by five year age band and "
     "coverage amount, with a term length toggle, rather than an average that would describe "
     "nobody."),
    ("Is a 20-year term long enough?",
     "It is long enough if the obligations you are insuring end within twenty years. Count the "
     "years left on the mortgage and the years until your youngest child is independent, take the "
     "larger of the two, and compare. If either runs past twenty years, a thirty year term usually "
     "costs less than people expect and removes the decision entirely."),
    ("What happens after 20 years?",
     "The level premium ends. The policy typically continues on an annually renewable basis at a "
     "price that resets to your age at that point and climbs every year afterwards, which is a "
     "bridge rather than a plan. Your more useful option is conversion to a permanent policy with "
     "no new health questions, and that right often expires before the term does."),
    ("Can I cancel a 20-year term policy early?",
     "Yes, at any time, by stopping payment or telling the carrier. There is no surrender charge "
     "and no penalty, because a term policy has no cash value to surrender. You simply stop being "
     "covered, so do not cancel one policy until the replacement is actually in force."),
]

SIBLINGS = [
    ("/term-life-insurance/30-year-term/", "30 year term",
     "The next length up, and when the extra decade is worth it."),
    ("/term-life-insurance/level-term/", "Level term explained",
     "What the twenty years actually guarantees, and what follows."),
    ("/term-life-insurance/what-is-term-life-insurance/", "What term life insurance is",
     "The plain definition, if you are starting from scratch."),
    ("/term-life-insurance/no-medical-exam/", "No medical exam term",
     "Same day options, and what they cost you in class."),
    ("/term-life-insurance/for-seniors/", "Term life after 60",
     "What is still available, and when to stop looking at term."),
    ("/term-life-insurance/10-year-term/", "10 year term",
     "Short obligations, and the trap of the renewal rate."),
]


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    return term_length.render(
        years=20,
        h1="20-Year Term Life Insurance",
        lead='A twenty year term is the most commonly bought length of '
             '<a class="link" href="/term-life-insurance/">term life insurance</a>, and for most '
             'households it is genuinely the right one: it covers a child from primary school to '
             'leaving home, or most of a standard mortgage. It is also the default that people '
             'accept without checking, which is a different thing. This page is the check.',
        fits=[
            ("The common case", "A mortgage with about twenty years left",
             "If you took a thirty year mortgage roughly a decade ago, the arithmetic lines up "
             "almost exactly. The policy and the debt end in the same year, which is the cleanest "
             "reason to choose any term length."),
            ("The family case", "A youngest child around primary school age",
             "Twenty years takes a five year old to twenty five: through school, through most of "
             "university, and into a first job. Past that point, replacing your income for them is "
             "a choice rather than a necessity."),
            ("The bridge case", "Twenty years to a pension or retirement date",
             "If your income stops being the household's dependency the day a pension starts, "
             "insure the gap and not a year more. Buying past the date the need ends is the "
             "commonest way people overpay."),
        ],
        dates_intro="Two dates decide this, and both are things you can look up in ten minutes "
                    "rather than estimate.",
        dates=[
            ("Find the year the mortgage ends",
             "Not the year you would like it to end. Take the payoff date from your statement or "
             "your lender's portal, and subtract this year. If you plan to move rather than pay "
             "it off, use the term of the mortgage you would take next, because the need follows "
             "you rather than the property."),
            ("Find the year your youngest turns twenty two",
             "Or whatever age independence realistically arrives in your family. This is usually "
             "the longer of the two numbers, and it is the one people forget to run."),
            ("Take the larger, then round up rather than down",
             "If the larger number is nineteen, twenty years is right. If it is twenty two, a "
             "thirty year term is right, and the price difference is smaller than the two years "
             "of exposure you would otherwise accept. Rounding down to save a few dollars a month "
             "is buying a policy that expires while the need is still live."),
        ],
        cost_note="A twenty year term is priced across the twenty years of risk that follow the "
                  "issue date, so the two things that move it most are your age today and whether "
                  "you use tobacco. Health class, coverage amount, sex, and state come after "
                  "those, in roughly that order.",
        faq=FAQ,
        siblings=SIBLINGS,
        cta_heading="Price a twenty year term for your age",
        cta_body="Six questions, about two minutes, and a licensed agent comes back with premiums "
                 "from named carriers at a class we can defend. No obligation, and no cost.",
        where="term_20y_mid")
