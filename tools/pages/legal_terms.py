# -*- coding: utf-8 -*-
"""TERMS OF USE. Spec P0. [PENDING LEGAL REVIEW] throughout."""
import chrome as C

PATH = "/legal/terms/"
OUT = "legal/terms/index.html"
ACTIVE = PATH
SILO = "site"
TITLE = "Terms of Use | Apex Insurance Marketing"
OG_TITLE = "Terms of use"
DESC = ("The terms that apply to your use of the Apex Insurance Marketing website, including "
        "what the content is and is not, and the limits of what we promise.")

P = lambda t: "<p>%s</p>" % t
UL = lambda items: "<ul class='grid gap-2 list-disc pl-5'>%s</ul>" % "".join(
    "<li>%s</li>" % i for i in items)

SECTIONS = [
    ("acceptance", "Accepting these terms", P(
        "By using this website you accept these terms. If you do not accept them, please do not "
        "use the site. The site is operated by %s, a licensed independent insurance agency."
        % C.BRAND)),

    ("what-this-site-is", "What this site is", P(
        "An information and quote request service. Using it does not create an insurance policy, "
        "an offer of coverage, or a binding agreement of any kind. Coverage exists only when a "
        "carrier issues a policy after you have completed an application and it has been "
        "approved, and not before.") + P(
        "Nothing on this site is insurance, tax, legal, or investment advice. It is general "
        "information, written for a general audience, and your situation may differ from every "
        "assumption behind it.")),

    ("eligibility", "Who may use it", P(
        "You must be at least 18 and legally able to enter into a contract. You must live in a "
        "state where we hold an active licence for us to place a policy for you; those states "
        "are listed on our <a class='link-static' href='/about/licensing/'>licensing page</a>.")),

    ("your-information", "Information you give us", P(
        "You agree that the information you submit is accurate and is yours to submit. Insurance "
        "applications are underwritten on the answers given, and an inaccurate answer can cause a "
        "carrier to rescind a policy or decline a claim. That consequence sits with the "
        "applicant, not with us, which is why it is worth being exact even where it is "
        "inconvenient.") + P(
        "How we handle what you send is described in our "
        "<a class='link-static' href='/legal/privacy/'>privacy policy</a>.")),

    ("rates-and-figures", "Rates, figures, and illustrations", P(
        "Premiums, rate tables, cost comparisons, and calculator outputs on this site are "
        "illustrations. They are not quotes, not offers, and not guarantees. An actual premium is "
        "set by a carrier after underwriting, and it depends on your age, state, health, build, "
        "family history, tobacco use, and the carrier's own rules.") + P(
        "Where a figure comes from a carrier rate card, the card and its date are named beside "
        "it. Where a figure is a placeholder awaiting real data, it is marked as one on the page.")),

    ("intellectual-property", "Content and intellectual property", P(
        "The text, design, and code of this site belong to %s or are used with permission. You "
        "may read, print, and share pages for your own use. You may not republish, scrape, or "
        "resell the content." % C.BRAND) + P(
        "Carrier names, where they appear, are the trademarks of those carriers. Their appearance "
        "indicates an appointment to sell their products and nothing more: no carrier endorses, "
        "sponsors, or is affiliated with us.")),

    ("third-party-links", "Links to other sites", P(
        "Where we link to a carrier, a state department of insurance, or another third party, we "
        "do not control that site and are not responsible for its content or its privacy "
        "practices. We link to state regulators specifically so that you can check us against a "
        "source that is not us.")),

    ("disclaimers-liability", "Disclaimers and limits of liability", P(
        "The site is provided as it is. We work to keep it accurate and current, and we publish a "
        "review date so you can see when we last checked, but we do not warrant that every page "
        "is free of error or continuously available.") + P(
        "[PENDING LEGAL REVIEW] The limitation of liability, indemnity, and warranty disclaimer "
        "language for this section must be drafted by counsel and checked against the consumer "
        "protection rules of every state the agency is licensed in. Several states limit what "
        "can be disclaimed, and an unenforceable clause is worse than a narrower one that holds.")),

    ("governing-law", "Governing law and disputes", P(
        "[PENDING LEGAL REVIEW] Governing law, venue, and any dispute resolution or arbitration "
        "provision must be selected by counsel. Do not publish an arbitration clause without "
        "confirming it is enforceable for consumers in the relevant states.")),

    ("changes-contact", "Changes and contact", P(
        "We may update these terms. The date at the top of this page shows when they last "
        "changed, and continuing to use the site after a change means you accept it.") + P(
        "Questions: call %s, or write to %s, %s, %s %s."
        % (C.PHONE_DISPLAY, C.STREET, C.CITY, C.REGION, C.POSTCODE))),
]


def schema():
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("Terms of use", None)])]


def body():
    return C.legal_doc(
        "Terms of use",
        "The terms that apply when you use this site, including what a quote is, what it is not, "
        "and where our responsibility ends.",
        SECTIONS)
