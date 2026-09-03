# -*- coding: utf-8 -*-
"""CARRIERS. Spec P0.

Which carriers we hold appointments with, plus the statement of independence
and what that independence actually buys the visitor.

No logo grid. Commit 5fa6bfc removed carrier logo placeholders sitewide: a
carrier's mark on our page implies an affiliation and an endorsement neither of
us has agreed to, which on a YMYL page is a real regulatory risk rather than a
design preference. Carrier names in text, in a table, with the appointment
stated plainly.
"""
from icons import icon
import chrome as C

PATH = "/about/carriers/"
OUT = "about/carriers/index.html"
ACTIVE = PATH
SILO = "site"
TITLE = "Carriers We Are Appointed With | Apex Insurance Marketing"
OG_TITLE = "The carriers Apex Insurance Marketing compares"
DESC = ("The life insurance carriers Apex Insurance Marketing holds appointments with, what an "
        "appointment means, and why being owned by none of them is what makes a comparison possible.")

# [PLACEHOLDER CARRIER LIST] One row per carrier the agency actually holds a
# current appointment with. Names only, no logos, no ratings we cannot source.
CARRIERS = [
    ("[CARRIER NAME]", "Term life, whole life", "[STATES]"),
    ("[CARRIER NAME]", "Whole life, final expense", "[STATES]"),
    ("[CARRIER NAME]", "Final expense, guaranteed acceptance", "[STATES]"),
    ("[CARRIER NAME]", "Term life", "[STATES]"),
    ("[CARRIER NAME]", "Term life, whole life, final expense", "[STATES]"),
]

FAQ = [
    ("Does an appointment mean the carrier endorses you?",
     "No. An appointment is a carrier authorising us to sell its products and to be paid a "
     "commission for doing so. It is not a partnership, an endorsement, or a rating of us by "
     "them. We are not owned by, affiliated with, or a subsidiary of any carrier on this page."),
    ("Are these all the carriers on the market?",
     "No, and that is worth being blunt about. We can only quote carriers we hold an appointment "
     "with, so our comparison is a comparison of our shelf, not of the whole market. It is wider "
     "than a captive agent's shelf of one, and it is narrower than every carrier that exists."),
    ("How do you decide which carrier to recommend?",
     "Price for your age, state, and health, then whether that carrier is likely to accept you, "
     "then the policy terms that matter for what you are covering, such as conversion options on "
     "term or the waiting period on a final expense policy. Commission does not enter it, and we "
     "explain how we are paid on our about page."),
]


def schema():
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("About", "/about/"), ("Carriers", None)]),
            C.faq_schema(FAQ),
            C.person_schema(PATH)]


def rows():
    return "\n            ".join(
        '<tr><th scope="row">%s</th><td>%s</td><td>%s</td></tr>' % r for r in CARRIERS)


def body():
    return f"""
<section class="pt-6 pb-14 md:pb-16 glow">
  <div class="container-ax">
    {C.crumbs([("Home", "/"), ("About", "/about/"), ("Carriers", None)])}

    <div class="mt-8 grid lg:grid-cols-12 gap-10 lg:gap-8 items-center">
      <div class="lg:col-span-6">
      <h1 class="reveal text-h1">The carriers we compare</h1>
      <p class="reveal mt-5 text-lead text-slate">
        We are appointed with <span class="tnum">{C.CARRIERS}</span> life insurance carriers and
        owned by none of them. That is the entire mechanism behind a comparison: an agency that
        answers to one carrier can only ever recommend that carrier.
      </p>
      </div>
      <div class="lg:col-span-5 lg:col-start-8">{C.figure("contact-desk", C.MEDIA_SIZES, eager=True)}</div>
    </div>

    <div class="mt-12 bento" data-stagger="40">
      <div class="reveal bento-cell bento-cell-blue bento-3">
        <p class="eyebrow text-white/80">Independence</p>
        <h2 class="mt-3 text-h3 !font-display !font-semibold text-white">Not owned by any carrier</h2>
        <p class="mt-4 text-white/85">
          {C.BRAND} is an independent agency. No carrier holds an ownership stake in us, sets our
          sales quotas, or requires us to lead with its product. No carrier on this page endorses
          us, and we do not claim otherwise anywhere on this site.
        </p>
      </div>
      <div class="reveal bento-cell bento-3">
        <p class="eyebrow">What that buys you</p>
        <p class="mt-4 text-slate">
          One set of answers priced against several carriers at once, including the ones likely to
          decline you, so you find that out before an application rather than after one. And an
          agent who can say a carrier is wrong for you without it costing them their job.
        </p>
      </div>
    </div>
  </div>
</section>


<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Current appointments</h2>
      <p class="reveal mt-5 text-slate">
        Names, the products each carrier is appointed for, and where. An individual agent's
        appointments can be narrower than the agency's, so their profile lists their own.
      </p>
    </div>

    <div class="reveal mt-8 max-w-3xl">
      {C.flag("Every row below is a placeholder. Populate from current, signed carrier "
              "appointments only. Do not list a carrier we are in the process of appointing "
              "with, and do not add carrier logos: a carrier mark on our page implies an "
              "affiliation and an endorsement that no appointment grants.",
              "PLACEHOLDER CARRIER LIST")}
    </div>

    <div class="reveal mt-8 table-scroll table-signature">
      <table class="rate-table" style="min-width:36rem">
        <caption>Carriers {C.BRAND} holds a current appointment with.</caption>
        <thead>
          <tr>
            <th scope="col">Carrier</th>
            <th scope="col">Appointed for</th>
            <th scope="col">States</th>
          </tr>
        </thead>
        <tbody>
            {rows()}
        </tbody>
      </table>
    </div>

    <p class="reveal mt-4 text-micro text-muted max-w-3xl">
      <span class="pill mr-2">Reviewed: {C.REVIEW_DATE}</span>
      Appointments change. Availability of a given carrier also varies by state, age, and product.
      Policies are issued by the carrier, not by {C.BRAND}, and every guarantee depends on the
      claims paying ability of the issuing carrier.
    </p>
  </div>
</section>


<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">How an appointment actually works</h2>
        <p class="reveal mt-5 text-slate">
          Worth understanding, because it is the difference between a comparison and a sales pitch
          with extra steps.
        </p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        {C.step(1, "The carrier authorises the agency",
                "It vets us, contracts us, and files the appointment with the state. Until that is done we cannot quote or sell that carrier's products at all.")}
        <div class="mt-8">
          {C.step(2, "We quote across everyone we hold",
                  "Your age, state, health, and coverage amount go to each appointed carrier's rate structure, and the answers come back different, because carriers price risk differently.")}
        </div>
        <div class="mt-8">
          {C.step(3, "The carrier issues and pays the claim",
                  "We place the policy; the carrier owns it. Your premium goes to them, your claim is paid by them, and the guarantees rest on their financial strength rather than on ours.")}
        </div>
      </div>
    </div>
  </div>
</section>


<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">What we will not claim</h2>
    </div>
    <ul class="mt-8 grid md:grid-cols-3 gap-4" data-stagger="40">
      {"".join('''<li class="reveal card">
        <span class="flex items-start gap-3">%s<span class="text-slate">%s</span></span>
      </li>''' % (icon("circle-x", 20, "shrink-0 mt-0.5 text-muted"), t) for t in [
        "That we search every carrier on the market. We search the ones we are appointed with, which is not the same thing.",
        "That any carrier here endorses, partners with, or recommends us. An appointment is a sales authorisation, nothing more.",
        "A financial strength rating for any carrier that we have not sourced and dated from the rating agency itself.",
      ])}
    </ul>
  </div>
</section>


{C.faq_section("Questions about carriers and appointments", FAQ, "carriers-faq")}


<section class="section-tight band-surface hairline">
  <div class="container-ax">{C.byline()}</div>
</section>


<section class="section band-navy on-navy">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-8 items-center">
      <div class="lg:col-span-7">
        <h2 class="reveal text-h2 text-white">See what they quote for you</h2>
        <p class="reveal mt-4 text-white/85 max-w-2xl">
          The carrier names come back on the quote, not just a number. That is how you check the
          comparison happened.
        </p>
      </div>
      <div class="lg:col-span-4 lg:col-start-9 grid gap-3">
        <a href="/get-a-quote/" class="btn btn-cta btn-block">Get a free quote</a>
        {C.phone_link("carriers_footer", "btn btn-ghost btn-block", "Call " + C.PHONE_DISPLAY)}
      </div>
    </div>
  </div>
</section>"""
