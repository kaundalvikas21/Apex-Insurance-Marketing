# -*- coding: utf-8 -*-
"""ABOUT. Spec P0.

Google's Who / How / Why framework, answered in that order and in plain
English, because this page is the one a cautious buyer opens before they trust
a rate table. Editorial column plus a trust bento.

None of the trust figures count up: every one of them is a placeholder, and
MASTER.md section 4 forbids animating a number we do not have.
"""
from icons import icon
import chrome as C

PATH = "/about/"
OUT = "about/index.html"
ACTIVE = PATH
SILO = "site"
TITLE = "About Apex Insurance Marketing | An Independent Life Insurance Agency"
OG_TITLE = "About Apex Insurance Marketing"
DESC = ("Who we are, how an independent life insurance agency gets paid, what we do and do not "
        "do, and why this site exists. Licensed agents, multiple appointed carriers.")

FAQ = [
    ("Does it cost more to buy through an agency?",
     "No. The premium is set by the carrier and filed with your state's department of insurance. "
     "It is the same whether you buy through us, through another agency, or direct from the "
     "carrier. What changes is whether anyone compared the carriers for you first."),
    ("Are you an insurance company?",
     "No. We are a licensed independent agency. Policies are issued by third party carriers, and "
     "every guarantee depends on the claims paying ability of the carrier that issues it, not on us."),
    ("Do you sell my details to other agencies?",
     "No. Your details go to the carriers we quote for you and nowhere else. We do not operate as "
     "a lead generator and we do not sell, rent, or share your contact information with other "
     "agencies."),
]


def schema():
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("About", None)]),
            {"@context": "https://schema.org", "@type": "AboutPage",
             "@id": C.DOMAIN + PATH + "#page",
             "name": "About " + C.BRAND,
             "url": C.DOMAIN + PATH,
             "about": {"@id": C.DOMAIN + "/#organization"},
             "publisher": {"@id": C.DOMAIN + "/#organization"}},
            C.faq_schema(FAQ),
            C.person_schema(PATH)]


def _do(kind, items):
    """Two plain lists. The 'do not' column is the same size and weight as the
    'do' column, because a page that hides its limits is doing marketing."""
    good = kind == "do"
    ico = icon("circle-check" if good else "circle-x", 20,
               "shrink-0 mt-0.5 " + ("text-green" if good else "text-muted"))
    rows = "".join('<li class="flex items-start gap-3"><span>%s</span>'
                   '<span class="text-slate">%s</span></li>' % (ico, t) for t in items)
    return '<ul class="mt-6 grid gap-4">%s</ul>' % rows


def body():
    return f"""
<section class="pt-6 pb-14 md:pb-16 glow">
  <div class="container-ax">
    {C.crumbs([("Home", "/"), ("About", None)])}

    <div class="mt-8 max-w-3xl">
      <h1 class="reveal text-h1">About Apex Insurance Marketing</h1>
      <p class="reveal mt-5 text-lead text-slate">
        We are an independent life insurance agency. We are appointed with several carriers and we
        compare them for you, which is a different job from selling you one company's product.
      </p>
    </div>

    <!-- TRUST BENTO. Three cells, three real facts, all of them placeholders
         until launch. count=False on every one: MASTER.md s4 bans count-up on a
         figure we do not have, because a number that ticks up reads as measured. -->
    <div class="mt-12 bento" data-stagger="40">
      <div class="reveal bento-cell bento-2">
        <p class="eyebrow">Licensing</p>
        {C.stat(C.STATES, "states we are licensed to write in", count=False, cls="mt-3")}
        <p class="mt-4 text-sm text-muted">
          Every licence number is listed, by state, on our
          <a class="link-static" href="/about/licensing/">licensing page</a>, where you can check
          it against your own state's department of insurance.
        </p>
      </div>
      <div class="reveal bento-cell bento-cell-tint bento-2">
        <p class="eyebrow">Independence</p>
        {C.stat(C.CARRIERS, "carriers we hold appointments with", count=False, cls="mt-3")}
        <p class="mt-4 text-sm text-slate">
          No carrier owns us and none of them sets our quotas, which is the whole reason we can
          tell you when a carrier we represent is the wrong answer for you. The
          <a class="link-static" href="/about/carriers/">carriers we are appointed with</a> are listed.
        </p>
      </div>
      <div class="reveal bento-cell bento-cell-blue bento-2">
        <p class="eyebrow text-white/80">Experience</p>
        {C.stat(C.YEARS, "years placing life insurance", count=False, cls="mt-3")}
        <p class="mt-4 text-sm text-white/85">
          Placing policies, not writing about them. The difference shows up when a carrier comes
          back with a rating you were not expecting.
        </p>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     WHO. The legal entity, in the words a state regulator would use.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">

      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">Who we are</h2>
        <p class="reveal mt-5 text-slate">
          The name on the licence, the address the mail goes to, and the number a regulator would
          use to look us up. If any of it does not match what your state shows, we would rather
          you told us than assumed.
        </p>
      </div>

      <div class="lg:col-span-6 lg:col-start-7">
        <div class="reveal card">
          <dl class="grid sm:grid-cols-2 gap-6">
            <div>
              <dt class="text-micro font-semibold uppercase tracking-[0.12em] text-muted">Legal entity</dt>
              <dd class="mt-2 text-slate">{C.BRAND}</dd>
            </div>
            <div>
              <dt class="text-micro font-semibold uppercase tracking-[0.12em] text-muted">Founded</dt>
              <dd class="mt-2 text-slate tnum">{C.FOUNDED}</dd>
            </div>
            <div>
              <dt class="text-micro font-semibold uppercase tracking-[0.12em] text-muted">National Producer Number</dt>
              <dd class="mt-2 text-slate tnum">{C.NPN}</dd>
            </div>
            <div>
              <dt class="text-micro font-semibold uppercase tracking-[0.12em] text-muted">Lines authorised</dt>
              <dd class="mt-2 text-slate">Life, and where noted by state, accident and health</dd>
            </div>
            <div class="sm:col-span-2">
              <dt class="text-micro font-semibold uppercase tracking-[0.12em] text-muted">Principal office</dt>
              <dd class="mt-2 text-slate">
                {C.STREET}<br>{C.CITY}, {C.REGION} {C.POSTCODE}
              </dd>
            </div>
          </dl>
          {C.flag("Business facts above are placeholders. Replace the entity details, founding "
                  "year, producer number, and address from the agency's filed records before "
                  "this page goes live. Nothing here should be approximate.")}
        </div>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     HOW WE ARE PAID. The question people are too polite to ask.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">How we get paid</h2>
      <p class="reveal mt-5 text-slate">
        Plainly, because you are entitled to know before you take our advice.
      </p>
    </div>

    <div class="mt-10 grid lg:grid-cols-12 gap-8 lg:gap-10 items-start">
      <div class="lg:col-span-7">
        <p class="reveal text-slate">
          The carrier pays us a commission when a policy we placed is issued and you pay the first
          premium. It is a percentage of that premium, it is highest in the first policy year, and
          it comes out of the carrier's own pricing. <strong>You do not pay us a fee, and the
          premium is not higher because you came through us.</strong> Life insurance rates are
          filed with your state, so the same policy from the same carrier costs the same whether
          you buy it here, from another agency, or direct.
        </p>
        <p class="reveal mt-5 text-slate">
          The obvious follow-up is whether that gives us a reason to steer you to the policy that
          pays us most. It would, if nobody named it. So: commission scales with premium, which
          means a bigger or more permanent policy pays us more than a smaller or shorter one. The
          check on that is that you can see the carrier names and the numbers on every quote we
          send, and you can take them somewhere else. We would rather place the right policy and
          keep the client.
        </p>
        <p class="reveal mt-5 text-slate">
          If a carrier ever offered us a bonus to favour their product over a better fit, that is
          the kind of arrangement that has to be disclosed, and we would disclose it here.
        </p>
      </div>

      <div class="lg:col-span-4 lg:col-start-9">
        <div class="reveal card">
          <h3 class="text-h4">What this costs you</h3>
          <p class="mt-3 text-slate">
            Nothing, at any stage. Quotes, the comparison, the application, and help with the
            underwriting are all part of placing the policy.
          </p>
          <p class="mt-4 text-slate">
            If you decide against buying, you owe us nothing and we do not sell your details on.
          </p>
          <div class="mt-6">
            {C.phone_link("about_paid", "btn btn-call btn-block btn-wrap", "Ask us anything: " + C.PHONE_DISPLAY)}
          </div>
        </div>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     WHAT WE DO AND DO NOT DO. Equal weight, deliberately.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">What we do, and what we do not</h2>
      <p class="reveal mt-5 text-slate">
        The second list is the more useful one. If what you need is on it, you will save time by
        going straight to someone who does that work.
      </p>
    </div>

    <div class="mt-10 grid md:grid-cols-2 gap-6">
      <div class="reveal card">
        <h3 class="text-h4">We do</h3>
        {_do("do", [
          "Compare term life, whole life, and final expense quotes across the carriers we are appointed with.",
          "Tell you which carriers are likely to decline you, and why, before you apply.",
          "Complete the application with you and stay with it through underwriting until it is issued or refused.",
          "Explain what a policy does not cover, including graded and waiting period benefits.",
          "Tell you when the honest answer is that you do not need what you called about.",
        ])}
      </div>
      <div class="reveal card">
        <h3 class="text-h4">We do not</h3>
        {_do("dont", [
          "Issue policies or pay claims. Carriers do both, and every guarantee rests on the issuing carrier.",
          "Give tax, legal, or investment advice. For those, use a professional licensed to give it.",
          "Sell annuities, Medicare plans, or employer group benefits.",
          "Sell, rent, or share your contact details with other agencies or lead buyers.",
          "Quote carriers we hold no appointment with, which is why our comparison is a comparison of our shelf, not the whole market.",
        ])}
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     WHY THIS CONTENT EXISTS. Google's third question, answered directly.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">Why this site exists</h2>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <p class="reveal text-slate">
          To be found by people shopping for life insurance, and to earn the call. We are not
          neutral about that and pretending otherwise would be the first dishonest thing on the
          page.
        </p>
        <p class="reveal mt-5 text-slate">
          What follows from it is the standard we hold the writing to. Every page is written or
          reviewed by a licensed agent who places these policies. Where a figure comes from a
          carrier rate card, the card and its date are named. Where the answer depends on your
          state, your age, or your health, we say so instead of rounding it into a promise. We do
          not publish invented premiums, invented reviews, or carrier claims we cannot source,
          because a number that turns out to be decoration costs more trust than it ever buys.
        </p>
        <p class="reveal mt-5 text-slate">
          If you find something here that is out of date or wrong, tell us. We will correct it and
          change the review date on the page.
        </p>
        <a class="reveal link-static mt-6 inline-block text-sm" href="/about/reviews/">How we handle reviews and testimonials</a>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     TEAM PREVIEW. One link to the index; the index owns the profiles.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">The people who answer</h2>
        <p class="reveal mt-5 text-slate">
          Every agent here is individually licensed, and every licence number is published so you
          can verify it with your state rather than take our word for it. When you call, you get
          one of them, not a call centre routing you to whoever is free.
        </p>
        <a class="reveal btn btn-ghost mt-8" href="/about/agents/">Meet our licensed agents</a>
      </div>

      <div class="lg:col-span-6 lg:col-start-7">
        <ul class="reveal grid sm:grid-cols-3 gap-4" data-stagger="40">
          {"".join('''<li class="card text-center">
            <div class="avatar-slot mx-auto" aria-hidden="true">%s<span>Agent<br>photo</span></div>
            <p class="mt-4 text-h4">%s</p>
            <p class="mt-1 text-micro text-muted">Licensed Life Insurance Agent</p>
          </li>''' % (icon("user-check", 26), C.AGENT_NAME) for _ in range(3))}
        </ul>
        <p class="mt-4 text-micro text-muted">
          Three placeholder cards. Replace with the real roster, one profile per agent.
        </p>
      </div>
    </div>
  </div>
</section>


{C.faq_section("Questions people ask before they call", FAQ, "about-faq")}


<section class="section-tight band-surface hairline">
  <div class="container-ax">{C.byline()}</div>
</section>


<section class="section band-navy on-navy">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-8 items-center">
      <div class="lg:col-span-7">
        <h2 class="reveal text-h2 text-white">Ready to see real numbers?</h2>
        <p class="reveal mt-4 text-white/85 max-w-2xl">
          Tell us your age, your state, and roughly what you are trying to cover. A licensed agent
          comes back within {C.SLA} with named carriers and their premiums.
        </p>
      </div>
      <div class="lg:col-span-4 lg:col-start-9 grid gap-3">
        <a href="/get-a-quote/" class="btn btn-cta btn-block">Get a free quote</a>
        {C.phone_link("about_footer", "btn btn-ghost btn-block", "Call " + C.PHONE_DISPLAY)}
      </div>
    </div>
  </div>
</section>"""
