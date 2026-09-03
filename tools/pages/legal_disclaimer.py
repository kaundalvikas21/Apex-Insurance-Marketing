# -*- coding: utf-8 -*-
"""DISCLAIMER. Spec P0.

The shortest of the three and the most load bearing: it carries the government
affiliation notice that the shared footer also states on every page, and the
statement that guarantees rest on the carrier rather than on the agency.
"""
import chrome as C

PATH = "/legal/disclaimer/"
OUT = "legal/disclaimer/index.html"
ACTIVE = PATH
SILO = "site"
TITLE = "Disclaimer | Apex Insurance Marketing"
OG_TITLE = "Disclaimer"
DESC = ("What this site is and is not: not advice, not an offer of coverage, and not affiliated "
        "with any government agency.")

P = lambda t: "<p>%s</p>" % t
UL = lambda items: "<ul class='grid gap-2 list-disc pl-5'>%s</ul>" % "".join(
    "<li>%s</li>" % i for i in items)

SECTIONS = [
    ("no-government-affiliation", "Not affiliated with any government agency", P(
        "<strong>%s is not affiliated with, endorsed by, or sponsored by any government agency, "
        "including the Social Security Administration, Medicare, the Department of Veterans "
        "Affairs, or any state or federal program.</strong>" % C.BRAND) + P(
        "We are a private, licensed insurance agency. No communication from us is a government "
        "notice, a benefit determination, or an official mailing. If something you received "
        "appears to come from a government agency and mentions us, it did not come from us, and "
        "we would like to know about it.")),

    ("not-advice", "General information, not advice", P(
        "Everything on this site is general information about life insurance. It is not "
        "insurance, tax, legal, or investment advice, and it is not tailored to your "
        "circumstances, because we do not know them until we speak with you.") + P(
        "For advice on your own situation, speak to a licensed agent, and for tax or legal "
        "questions speak to a professional licensed to answer them. We will tell you when a "
        "question is one of those, rather than answering it anyway.")),

    ("not-an-offer", "Not an offer of coverage", P(
        "Nothing here is an offer to sell or a solicitation to buy insurance in any state where "
        "we are not licensed. Submitting a form does not create coverage. Coverage begins only "
        "when a carrier issues a policy and the conditions of that policy are met.")),

    ("rates-are-illustrations", "Rates and figures are illustrations", P(
        "Premiums shown anywhere on this site are illustrative, are marked as placeholders where "
        "real carrier data has not yet been loaded, and are never a quoted or offered rate. Your "
        "actual premium depends on the carrier's underwriting of you specifically.") + P(
        "Rate tables carry the date they were last updated and the carrier rate card they came "
        "from. If either is missing, treat the number as unverified.")),

    ("carrier-guarantees", "Guarantees depend on the carrier", P(
        "Policies are issued by third party insurance carriers, not by %s. Coverage, "
        "availability, premiums, riders, exclusions, and benefits vary by carrier, state, age, "
        "and health." % C.BRAND) + P(
        "<strong>All guarantees, including death benefits, guaranteed cash value, and level "
        "premiums, are subject to the claims paying ability of the issuing carrier.</strong> They "
        "are not guaranteed by us, and they are not insured by any government agency or deposit "
        "insurance scheme.")),

    ("independence", "Our independence, and its limit", P(
        "We are an independent agency and are not owned by any carrier. We are paid a commission "
        "by the carrier when a policy is issued, which is explained in plain terms on our "
        "<a class='link-static' href='/about/'>about page</a>.") + P(
        "The limit of our independence is worth stating: we can only quote carriers we hold an "
        "appointment with. Our comparison is a comparison of that shelf, not of every carrier in "
        "the market. The carriers on it are listed on our "
        "<a class='link-static' href='/about/carriers/'>carriers page</a>.")),

    ("testimonials", "Reviews and testimonials", P(
        "We publish only real, attributable reviews left by real clients on a platform we do not "
        "control. We do not write, buy, incentivise, or edit reviews, and where we have none yet "
        "we say so rather than filling the space. See our "
        "<a class='link-static' href='/about/reviews/'>reviews page</a>.") + P(
        "Any outcome described on this site is an example, not a promise of a similar result.")),

    ("errors", "Errors", P(
        "We try to keep every page accurate and print a review date so you can see when it was "
        "last checked. If you find something wrong or out of date, tell us: call %s. We will "
        "correct it and change the review date." % C.PHONE_DISPLAY)),
]


def schema():
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("Disclaimer", None)])]


def body():
    return C.legal_doc(
        "Disclaimer",
        "What this site is, what it is not, and where a guarantee actually comes from.",
        SECTIONS)
