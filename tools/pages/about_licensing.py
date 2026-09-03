# -*- coding: utf-8 -*-
"""LICENSING. Spec P0.

The agency's licence number in every state it is appointed in. The shared
footer's licence disclosure links here from every page on the site, so this is
the page that has to be right.

The table is deliberately the whole page. There is no argument to make here,
only a list to publish.
"""
import chrome as C

PATH = "/about/licensing/"
OUT = "about/licensing/index.html"
ACTIVE = PATH
SILO = "site"
TITLE = "Licensing by State | Apex Insurance Marketing"
OG_TITLE = "Where Apex Insurance Marketing is licensed"
DESC = ("The states Apex Insurance Marketing holds an active insurance producer licence in, with "
        "the agency licence number for each, verifiable through your state's department of insurance.")

# [PLACEHOLDER LICENCE TABLE] One row per state the agency actually holds an
# active licence in. Delete every row that is not real. Publishing a state we
# cannot write in wastes the visitor's time and misstates our footprint.
LICENCES = [
    ("[STATE]", "[LICENCE NUMBER]", "Resident", "Life, accident and health"),
    ("[STATE]", "[LICENCE NUMBER]", "Non-resident", "Life"),
    ("[STATE]", "[LICENCE NUMBER]", "Non-resident", "Life"),
    ("[STATE]", "[LICENCE NUMBER]", "Non-resident", "Life"),
    ("[STATE]", "[LICENCE NUMBER]", "Non-resident", "Life"),
    ("[STATE]", "[LICENCE NUMBER]", "Non-resident", "Life"),
]

FAQ = [
    ("What is the difference between an agency licence and an agent licence?",
     "The agency holds a business entity licence in each state. The individual agent you speak "
     "to holds their own producer licence. Both have to be active in your state for us to place "
     "your policy there. Agency numbers are on this page; agent numbers are on each agent's profile."),
    ("You are not licensed in my state. Can you still help?",
     "Not with placing a policy. A producer can only write business in a state where they hold "
     "an active licence, and the agency needs one too. Call us anyway and we will tell you "
     "straight away rather than taking your details first."),
    ("How do I verify these numbers myself?",
     "Every state department of insurance runs a public producer lookup. Search the licence "
     "number, or the agency name, in the state you live in. If what you find does not match what "
     "is published here, please tell us."),
]


def schema():
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("About", "/about/"), ("Licensing", None)]),
            C.faq_schema(FAQ)]


def rows():
    return "\n            ".join(
        '<tr><th scope="row">%s</th><td class="tnum">%s</td><td>%s</td><td>%s</td></tr>'
        % r for r in LICENCES)


def body():
    return f"""
<section class="pt-6 pb-14 md:pb-16 glow">
  <div class="container-ax">
    {C.crumbs([("Home", "/"), ("About", "/about/"), ("Licensing", None)])}

    <div class="mt-8 max-w-3xl">
      <h1 class="reveal text-h1">Licensing by state</h1>
      <p class="reveal mt-5 text-lead text-slate">
        {C.BRAND} holds an active insurance producer licence in
        <span class="tnum">{C.STATES}</span> states. Every agency licence number is below, so you
        can check it against your own state's department of insurance rather than taking it from us.
      </p>
    </div>

    <div class="reveal mt-8 max-w-3xl">
      {C.flag("Every row below is a placeholder. Populate from the agency's current licence "
              "records, one row per state with an active licence, and delete the rest. A state "
              "listed here that we cannot actually write in is a misstatement of our footprint.",
              "PLACEHOLDER LICENCE TABLE")}
    </div>

    <div class="reveal mt-8 table-scroll table-signature">
      <table class="rate-table" style="min-width:40rem">
        <caption>Agency producer licences held by {C.BRAND}.</caption>
        <thead>
          <tr>
            <th scope="col">State</th>
            <th scope="col">Agency licence number</th>
            <th scope="col">Type</th>
            <th scope="col">Lines authorised</th>
          </tr>
        </thead>
        <tbody>
            {rows()}
        </tbody>
      </table>
    </div>

    <p class="reveal mt-4 text-micro text-muted max-w-3xl">
      <span class="pill mr-2">Reviewed: {C.REVIEW_DATE}</span>
      National Producer Number <span class="tnum">{C.NPN}</span>. Individual agent licence numbers
      are published on each <a class="link-static" href="/about/agents/">agent's profile</a>.
      Licence status can change; if what you find in your state's lookup differs from this page,
      that lookup is authoritative and we want to hear about it.
    </p>
  </div>
</section>


<section class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">
      <div class="lg:col-span-5">
        <div class="sticky-col">
          <h2 class="reveal text-h2">What a licence does and does not tell you</h2>
          <p class="reveal mt-5 text-slate">A licence is a floor rather than a recommendation. Both halves of that are worth knowing.</p>
        </div>
      </div>
      <div class="lg:col-span-6 lg:col-start-7 bento" data-stagger="40">
        <div class="reveal bento-cell bento-3">
          <p class="eyebrow">It tells you</p>
          <p class="mt-4 text-slate">
            That the state has vetted and authorised us to sell life insurance there, that we sat
            the exams, and that we carry the continuing education and bonding the state requires.
          </p>
        </div>
        <div class="reveal bento-cell bento-cell-tint bento-3">
          <p class="eyebrow">It does not tell you</p>
          <p class="mt-4 text-slate">
            Whether the advice is any good. A licence is a floor, not a recommendation. Judge that
            on whether we name the carriers, show the numbers, and tell you when the answer is no.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>


{C.faq_section("Licensing questions", FAQ, "lic-faq", cls="section")}


<section class="section band-navy on-navy">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-8 items-center">
      <div class="lg:col-span-7">
        <h2 class="reveal text-h2 text-white">Check we are licensed where you live</h2>
        <p class="reveal mt-4 text-white/85 max-w-2xl">
          Tell us your state and we will confirm it on the call, before anything else.
        </p>
      </div>
      <div class="lg:col-span-4 lg:col-start-9 grid gap-3">
        {C.phone_link("licensing_footer", "btn btn-ghost btn-block", "Call " + C.PHONE_DISPLAY)}
        <a href="/get-a-quote/" class="btn btn-cta btn-block">Get a free quote</a>
      </div>
    </div>
  </div>
</section>"""
