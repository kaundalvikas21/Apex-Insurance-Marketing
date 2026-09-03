# -*- coding: utf-8 -*-
"""PRIVACY POLICY. Spec P0.

[PENDING LEGAL REVIEW] throughout. This is structurally complete template copy
covering the disclosures an insurance lead form actually triggers: TCPA consent
for calls and texts, what is shared with carriers, and CCPA / state privacy
rights. Counsel replaces the wording; the structure and the section ids should
survive, because the site links to some of these sections directly.
"""
import chrome as C

PATH = "/legal/privacy/"
OUT = "legal/privacy/index.html"
ACTIVE = PATH
SILO = "site"
TITLE = "Privacy Policy | Apex Insurance Marketing"
OG_TITLE = "Privacy policy"
DESC = ("How Apex Insurance Marketing collects, uses, shares, and protects your personal "
        "information, and the privacy rights you have over it.")

P = lambda t: "<p>%s</p>" % t
UL = lambda items: "<ul class='grid gap-2 list-disc pl-5'>%s</ul>" % "".join(
    "<li>%s</li>" % i for i in items)

SECTIONS = [
    ("who-we-are", "Who this policy covers", P(
        "This policy describes how %s, a licensed independent insurance agency, handles personal "
        "information collected through this website, our forms, and our phone calls. It does not "
        "cover the separate privacy practices of the insurance carriers we submit applications "
        "to. Each carrier has its own policy, and it governs what that carrier does with your "
        "information once an application reaches them." % C.BRAND)),

    ("what-we-collect", "What we collect", P(
        "We collect only what is needed to quote and place insurance, and we collect it because "
        "you gave it to us:") + UL([
            "<strong>Quote information:</strong> age, sex as shown on your birth certificate, "
            "state, tobacco use, coverage amount, and the product you asked about.",
            "<strong>Contact information:</strong> your name, phone number, and email address "
            "where you provided one.",
            "<strong>Health information</strong> you choose to share so we can identify which "
            "carriers are likely to accept you.",
            "<strong>Technical information:</strong> the page you submitted from (recorded as a "
            "source URL with every form), and standard analytics such as pages viewed and "
            "approximate location by region.",
        ]) + P(
            "We do not ask for your Social Security number, bank details, or payment card to "
            "produce a quote. A Social Security number is needed by the carrier at the "
            "application stage, not by us to price a policy.")),

    ("how-we-use-it", "How we use it", P("To do the thing you asked us to do:") + UL([
        "Produce quotes from the carriers we are appointed with.",
        "Contact you about those quotes by phone, text, or email, within the consent you gave.",
        "Submit an application to a carrier, if you decide to apply.",
        "Meet our record keeping obligations as a licensed insurance producer.",
    ]) + P(
        "We do not use your information to build advertising profiles, and we do not sell it. "
        "[PENDING LEGAL REVIEW] Confirm this against the agency's actual analytics and "
        "advertising stack before launch, including whether any tag constitutes a sale or share "
        "under state law.")),

    ("tcpa", "Consent to be contacted (TCPA)", P(
        "The consent checkbox above every submit button on this site is separate, is never "
        "pre-ticked, and is not a condition of getting a quote or buying a policy. By ticking it "
        "you agree that %s may call and text the number you gave us about life insurance, "
        "including using an automatic telephone dialing system or a prerecorded voice. Message "
        "and data rates may apply." % C.BRAND) + P(
        "You can withdraw that consent at any time: tell the agent on the call, reply STOP to a "
        "text, or contact us using the details below. Withdrawing consent does not affect a "
        "policy already in force.") + P(
        "[PENDING LEGAL REVIEW] This section must be checked against current TCPA one-to-one "
        "consent requirements and against the consent language rendered on the forms, which is "
        "authored once in tools/forms.py.")),

    ("who-we-share-with", "Who we share it with", P(
        "A short and closed list:") + UL([
            "<strong>Insurance carriers</strong> we are appointed with, to obtain quotes and "
            "submit applications on your behalf.",
            "<strong>Service providers</strong> who operate our systems, such as our customer "
            "relationship system, under contracts that limit them to that purpose.",
            "<strong>Regulators and law enforcement</strong> where we are legally required to.",
        ]) + P(
            "<strong>We do not sell, rent, or trade your personal information, and we are not a "
            "lead generator.</strong> Your details are not passed to other agencies or to lead "
            "buyers. This is the difference between submitting a form here and submitting one to "
            "a comparison site, and it is the reason you get one call rather than six.")),

    ("your-rights", "Your privacy rights", P(
        "Depending on the state you live in, you may have the right to:") + UL([
            "Know what personal information we hold about you and how we obtained it.",
            "Receive a copy of it in a portable format.",
            "Correct information that is inaccurate.",
            "Delete it, subject to the records we are required by insurance law to keep.",
            "Opt out of any sale or sharing of it. We do not sell or share it, so there is "
            "nothing to opt out of, but the right exists and we will confirm that in writing.",
            "Not be discriminated against for exercising any of these rights.",
        ]) + P(
            "To exercise any of them, contact us using the details below. We will verify who you "
            "are before acting, because acting on an unverified request is itself a privacy "
            "failure. [PENDING LEGAL REVIEW] Response deadlines, the authorised agent process, "
            "and any state specific disclosures (California, Colorado, Connecticut, Virginia, and "
            "others) must be completed by counsel for the states the agency is licensed in.")),

    ("retention-security", "How long we keep it, and how it is protected", P(
        "We keep quote and application records for as long as insurance record keeping rules "
        "require, and then dispose of them securely. Access is limited to the licensed agents and "
        "staff who need it to do their job.") + P(
        "No transmission over the internet is perfectly secure, and any site that tells you "
        "otherwise is overstating it. [PENDING LEGAL REVIEW] Describe the actual technical and "
        "organisational measures in place, and the incident notification process, rather than "
        "generic assurances.")),

    ("children", "Children", P(
        "This site is not directed at children and we do not knowingly collect information from "
        "anyone under 18. If you believe a child has given us information, contact us and we will "
        "delete it.")),

    ("changes-contact", "Changes and how to contact us", P(
        "If this policy changes materially we will update the date at the top of this page and, "
        "where the change affects how we contact you, tell you directly.") + P(
        "Questions, requests, or complaints: call %s, or write to %s, %s, %s %s."
        % (C.PHONE_DISPLAY, C.STREET, C.CITY, C.REGION, C.POSTCODE)) + P(
        "You can also raise a concern with your state's department of insurance or attorney "
        "general. Our licence numbers are on our <a class='link-static' "
        "href='/about/licensing/'>licensing page</a>.")),
]


def schema():
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("Privacy policy", None)])]


def body():
    return C.legal_doc(
        "Privacy policy",
        "What we collect, why we collect it, who sees it, and the rights you have over it. "
        "Written to be read rather than to be survived.",
        SECTIONS)
