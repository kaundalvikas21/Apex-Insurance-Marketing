# -*- coding: utf-8 -*-
"""HOME — brand and triage. Spec section 01.

Job of this page: route three very different visitors to the right silo
without pitching a product. It links to hubs, never to spokes.
"""
from icons import icon
import chrome as C

PATH = "/"
OUT = "index.html"
ACTIVE = "/"
SILO = "site"
TITLE = "Life Insurance Quotes from an Independent Agency | Apex"
OG_TITLE = "Compare life insurance from multiple carriers"
DESC = ("Independent, licensed life insurance agency. Compare term life, whole life, and final "
        "expense coverage from multiple appointed carriers. Free quotes, no obligation.")

FAQ = [
    ("How much life insurance do I actually need?",
     "There is no single right answer, but most households start by covering what would still have "
     "to be paid if the income stopped: the mortgage balance, any other debt, the cost of raising "
     "children to adulthood, and a cushion for the surviving partner. A common starting point is "
     "ten to twelve times annual income, then adjusted up or down for savings, existing employer "
     "coverage, and how long the dependents will actually need support. A licensed agent can walk "
     "through the specific numbers with you at no cost."),
    ("What is the difference between term and whole life insurance?",
     "Term life covers you for a fixed number of years, usually 10 to 30, and pays a death benefit "
     "only if you die during that term. It has no cash value and it is the least expensive way to "
     "buy a large death benefit. Whole life covers you for your entire life, has a guaranteed "
     "premium and a guaranteed cash value that builds over time, and costs significantly more per "
     "dollar of coverage. Term suits temporary obligations. Whole life suits permanent ones."),
    ("Do I have to take a medical exam?",
     "Not always. Many carriers now offer accelerated underwriting for healthy applicants, which "
     "uses prescription history, motor vehicle records, and medical databases instead of a "
     "paramedical exam. Final expense policies are almost always issued on health questions alone "
     "with no exam. Fully underwritten policies that do include an exam usually offer the lowest "
     "premium, so the exam is often worth the inconvenience if you are in good health."),
    ("Can I get life insurance if I have a health condition?",
     "Usually yes, though the premium and the available coverage depend on the condition, how well "
     "it is controlled, and which carrier you apply to. Carriers underwrite the same condition very "
     "differently, which is the main practical argument for using an independent agency: we can "
     "place the application with the carrier that treats your specific situation most favorably "
     "rather than accepting one company's decline as final."),
    ("How much does life insurance cost?",
     "Premium depends on your age, sex, health, tobacco use, the type of policy, the coverage "
     "amount, and the carrier. Age is the single largest factor and it moves against you every "
     "year. Each of our product pages includes a rate table showing sample premiums by age band so "
     "you can see the shape of the pricing before you speak to anyone. Your actual quote comes from "
     "the carrier after underwriting."),
    ("Does it cost more to buy through an agency?",
     "No. Life insurance rates are filed with state insurance departments, so the premium for a "
     "given policy is the same whether you buy it through an independent agency, through a captive "
     "agent, or directly from the carrier. The carrier pays our commission out of that premium. You "
     "never pay Apex a fee."),
]


def schema():
    return [C.org_schema(),
            C.faq_schema(FAQ),
            C.person_schema(PATH)]


# ---------------------------------------------------------------------------
def _path_card(kind, label, headline, fit, body, cta_html):
    return f"""
        <div class="reveal card flex flex-col h-full">
          <p class="text-sm font-medium text-muted">{label}</p>
          <h2 class="mt-1 text-h3-serif">{headline}</h2>
          <p class="mt-3 text-sm text-ink">{fit} <span class="text-muted">{body}</span></p>
          <div class="mt-6 lg:mt-auto lg:pt-6">{cta_html}</div>
        </div>"""


def body():
    return HERO + rest()


# LCP candidate: the one eager image on this page.
hero_media = C.figure("home-hero", "(min-width: 1024px) 38vw, 92vw",
                      cls="reveal", eager=True, duotone=True)


HERO = f"""
<!-- =====================================================================
     HERO. Triage, not pitch. Three paths, each carrying its own silo's
     CTA weighting per spec section 09.
     ================================================================== -->
<section class="section-tight pt-10 md:pt-12 lg:pt-14">
  <div class="container-ax">

    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-center">
      <div class="lg:col-span-7">
        <h1 class="reveal text-h1">Cover the people who depend on you.</h1>
        <p class="reveal mt-4 ital-line max-w-xl">Honest guidance for the people you love most.</p>
        <p class="reveal mt-4 text-lead text-ink max-w-xl">
          Apex is an independent, licensed life insurance agency. We compare multiple carriers and
          tell you plainly what fits your family.
        </p>
        <p class="reveal mt-4 text-sm text-muted">
          Not sure which of the three you need?
          <a class="link" href="#triage">Answer three questions</a>
          and we will point you to the right one.
        </p>
      </div>

      <div class="lg:col-span-5 lg:col-start-8">
        {hero_media}
      </div>
    </div>

    <div class="mt-10 lg:mt-12 grid lg:grid-cols-3 gap-6" data-stagger>
      {_path_card(
        "term", "Coverage for a set period",
        "Term life insurance",
        "Best if you want the largest death benefit for the lowest premium while you still have a mortgage or children at home.",
        "Typically ages 30 to 55. Coverage for 10, 15, 20, or 30 years.",
        '<a href="/term-life-insurance/" class="btn btn-cta btn-block">Get term life quotes</a>'
        '<p class="mt-3 text-micro text-muted">Free &#183; No obligation &#183; Licensed agents</p>')}
      {_path_card(
        "whole", "Lifetime coverage plus cash value",
        "Whole life insurance",
        "Best if you want coverage that never expires, a premium that never rises, and a guaranteed cash value you can borrow against.",
        "Typically ages 40 to 65. Coverage for life.",
        '<div class="grid gap-2">'
        '<a href="/whole-life-insurance/" class="btn btn-cta btn-block">Explore whole life</a>'
        + C.phone_link("home_hero_whole", "btn btn-ghost btn-block", "Talk to an agent")
        + '</div><p class="mt-3 text-micro text-muted">Free &#183; No obligation &#183; Licensed agents</p>')}
      {_path_card(
        "final", "Cover funeral costs, ages 50 to 85",
        "Final expense insurance",
        "Best if you want a smaller policy that covers a funeral and final bills, with health questions instead of a medical exam.",
        "Most people set this up over the phone in about fifteen minutes.",
        C.phone_link("home_hero_final", "btn btn-call btn-block", "Call " + C.PHONE_DISPLAY)
        + f'<p class="mt-3 text-micro text-muted">{C.HOURS}</p>')}
    </div>

  </div>
</section>

<!-- Trust strip, directly beneath the hero CTAs and inside the same viewport. -->
<section class="border-y border-rule bg-surface">
  <div class="container-ax py-6">
    <div class="flex flex-wrap items-center justify-between gap-x-8 gap-y-3 trust-strip">
      <span class="inline-flex items-center gap-2 text-forest font-semibold">
        {icon("shield-check", 18, "shrink-0 text-forest")}Licensed in {C.STATES} states
      </span>
      <span class="inline-flex items-center gap-2">
        {icon("scale", 18, "shrink-0")}Independent. We work for you, not for one carrier.
      </span>
      <span class="inline-flex items-center gap-2">
        {icon("building", 18, "shrink-0")}{C.YEARS} years placing life insurance
      </span>
    </div>

    <div class="mt-6 pt-6 border-t border-rule">
      <p class="text-micro font-semibold uppercase tracking-[0.1em] text-muted">Carriers we are appointed with</p>
      <!-- [PLACEHOLDER - REPLACE WITH APPOINTED CARRIER LOGOS. Do not display a
           carrier mark until the appointment is active and the carrier's brand
           guidelines have been checked.] -->
      <div class="mt-4 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
        <div class="logo-slot">Carrier logo 1</div>
        <div class="logo-slot">Carrier logo 2</div>
        <div class="logo-slot">Carrier logo 3</div>
        <div class="logo-slot">Carrier logo 4</div>
        <div class="logo-slot">Carrier logo 5</div>
        <div class="logo-slot">Carrier logo 6</div>
      </div>
    </div>
  </div>
</section>
"""


def _acc(q, a):
    """Native <details>. Keyboard and screen-reader behavior comes free and
    cannot be broken by a JavaScript error on a YMYL page."""
    return ('<details class="acc" name="home-faq">'
            '<summary>%s<span class="acc-icon">%s</span></summary>'
            '<div class="acc-body"><p class="text-ink">%s</p></div>'
            '</details>') % (q, icon("plus", 22), a)


REST = """
<!-- =====================================================================
     TRIAGE. Three questions, no email wall. Scores live in the markup next
     to the copy they belong to.
     ================================================================== -->
<section id="triage" class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">

      <div class="lg:col-span-4">
        <h2 class="reveal text-h2">Not sure which one you need?</h2>
        <p class="reveal mt-5 text-ink">
          Three questions, about thirty seconds. No email address, no phone number, and nothing is
          submitted anywhere. You get a recommendation and a link, and you are free to ignore both.
        </p>
        <p class="reveal mt-5 text-sm text-muted">
          Want the longer version? Read our
          <a class="link" href="/compare/term-vs-whole-life-insurance/">comparison of term and whole life insurance</a>.
        </p>
      </div>

      <div class="lg:col-span-7 lg:col-start-6">
        <div class="panel reveal" data-triage>

          <p data-triage-progress class="text-sm font-medium text-muted"></p>

          <div data-triage-q hidden>
            <h3 data-triage-heading class="mt-2 text-h3-serif">What is the money mainly for?</h3>
            <div class="mt-6 grid gap-2.5">
              <button type="button" class="triage-opt" data-score="term:3">Replacing my income while my family still depends on it</button>
              <button type="button" class="triage-opt" data-score="whole:3,final:1">Leaving something behind no matter when I die</button>
              <button type="button" class="triage-opt" data-score="final:3">Covering my funeral and the bills that come with it</button>
            </div>
          </div>

          <div data-triage-q hidden>
            <h3 data-triage-heading class="mt-2 text-h3-serif">How old are you?</h3>
            <div class="mt-6 grid gap-2.5">
              <button type="button" class="triage-opt" data-score="term:3">Under 45</button>
              <button type="button" class="triage-opt" data-score="term:2,whole:2">45 to 59</button>
              <button type="button" class="triage-opt" data-score="final:3,whole:1">60 or older</button>
            </div>
          </div>

          <div data-triage-q hidden>
            <h3 data-triage-heading class="mt-2 text-h3-serif">Which matters more to you?</h3>
            <div class="mt-6 grid gap-2.5">
              <button type="button" class="triage-opt" data-score="term:3,final:1">The lowest premium for the most coverage</button>
              <button type="button" class="triage-opt" data-score="whole:3,final:2">Coverage that cannot expire or be cancelled</button>
              <button type="button" class="triage-opt" data-score="final:3">Getting approved without a medical exam</button>
            </div>
          </div>

          <!-- Results link to a different section of each hub, so no target on
               this page is linked twice. See spec section 07. -->
          <div data-triage-result="term" hidden>
            <p class="text-sm text-muted">Based on your answers</p>
            <h3 class="mt-1 text-h3-serif">Start with term life insurance</h3>
            <p class="mt-4 text-ink">
              You are describing a temporary obligation with a large price tag. Term buys the most
              coverage per dollar for exactly as long as that obligation lasts, then it ends. If the
              need turns out to be permanent, most term policies can be converted later without a
              new medical exam.
            </p>
            <div class="mt-6 flex flex-wrap items-center gap-5">
              <a class="btn btn-cta" href="/term-life-insurance/#quote">Start a term life quote</a>
              <button type="button" data-triage-restart class="link text-sm">Start over</button>
            </div>
          </div>

          <div data-triage-result="whole" hidden>
            <p class="text-sm text-muted">Based on your answers</p>
            <h3 class="mt-1 text-h3-serif">Look at whole life insurance</h3>
            <p class="mt-4 text-ink">
              You want the policy to still be there whenever it is needed, which term cannot promise.
              Whole life costs considerably more per dollar of death benefit, so the honest next step
              is a written illustration you can read at your own pace, not a rushed application.
            </p>
            <div class="mt-6 flex flex-wrap items-center gap-5">
              <a class="btn btn-cta" href="/whole-life-insurance/#quote">See whole life options</a>
              <button type="button" data-triage-restart class="link text-sm">Start over</button>
            </div>
          </div>

          <div data-triage-result="final" hidden>
            <p class="text-sm text-muted">Based on your answers</p>
            <h3 class="mt-1 text-h3-serif">Final expense insurance is probably the fit</h3>
            <p class="mt-4 text-ink">
              You need a smaller policy, issued on health questions rather than a medical exam, that
              pays quickly and covers a funeral and the bills around it. This is almost always
              faster to arrange by phone than by form.
            </p>
            <div class="mt-6 flex flex-wrap items-center gap-5">
              {call_triage}
              <button type="button" data-triage-restart class="link text-sm">Start over</button>
            </div>
            <p class="mt-4 text-micro text-muted">
              Or read what
              <a class="link" href="/final-expense-insurance/#costs">final expense insurance costs by age</a>.
            </p>
          </div>

        </div>
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     HOW WE WORK. Honest expectation setting, not a funnel diagram.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">How working with us actually goes</h2>
      <p class="reveal mt-5 text-ink">
        Three steps. None of them obligates you to buy anything, and you can stop after any one
        of them.
      </p>
    </div>

    <div class="mt-12 grid md:grid-cols-3 gap-10 md:gap-8" data-stagger>
      {steps_how}
    </div>
  </div>
</section>

<!-- =====================================================================
     INDEPENDENCE + COMMISSION DISCLOSURE. Plain English, on purpose.
     ================================================================== -->
<section class="section band-forest on-forest">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-12 lg:gap-8">

      <div class="lg:col-span-7">
        <h2 class="reveal text-h2">Why it matters that we are independent</h2>
        <p class="reveal mt-6 text-lead text-white/88">
          A captive agent works for one insurance company and can only sell you that company's
          products. We are appointed with several, so when one carrier prices your health history
          badly, we can take the same application somewhere that treats it better.
        </p>

        <h3 class="reveal mt-10 text-h4 text-white">How we get paid, in plain English</h3>
        <p class="reveal mt-4 text-white/82">
          The carrier pays us a commission out of your premium when a policy is issued. You never
          pay Apex a fee, and buying through us does not raise your premium, because life insurance
          rates are filed with state insurance departments and are the same wherever you buy them.
        </p>
        <p class="reveal mt-4 text-white/82">
          Commission rates are not identical across carriers or products, and whole life pays
          considerably more than term. That is a genuine conflict of interest. The way we manage it
          is by showing you the full comparison, including the cheaper option that pays us less, and
          by putting the reasoning in writing so you can check it against anything else you read.
        </p>
      </div>

      <div class="lg:col-span-4 lg:col-start-9">
        <div class="reveal card">
          <p class="text-sm text-white/70">Written and reviewed by</p>
          <p class="mt-2 text-h4 text-white">{agent}</p>
          <p class="mt-1 text-sm text-white/70">{agent_title}</p>
          <p class="mt-5 text-sm text-white/82">
            Every page on this site is written or reviewed by a licensed agent before it is
            published, and the review date is printed on the page.
          </p>
          <a class="link-static mt-5 inline-block text-sm" href="/about/agents/">Meet our licensed agents</a>
        </div>

        <!-- [REAL ATTRIBUTABLE REVIEWS ONLY - DO NOT FABRICATE]
             The slot is designed and wired. It stays hidden until real,
             attributable, consented reviews exist. Remove the hidden
             attribute and populate data-reviews-list at that point. -->
        <div class="reveal mt-6 rounded-card border border-dashed border-white/30 p-6" data-reviews-slot hidden>
          <p class="text-sm text-white/70">What clients say</p>
          <div data-reviews-list></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     THE THREE PRODUCTS AT A GLANCE. Facts, not another pitch. Each CTA
     points at a different section, so no target is linked twice.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">The three products, side by side</h2>
      <p class="reveal mt-5 text-ink">
        Most people only ever need one of these. The differences that actually decide it are in
        this table.
      </p>
    </div>

    <div class="reveal mt-10 table-scroll">
      <table class="compare-table" style="min-width:46rem">
        <caption class="sr-only">Comparison of term life, whole life, and final expense insurance</caption>
        <thead>
          <tr>
            <th scope="col"><span class="sr-only">Feature</span></th>
            <th scope="col">Term life</th>
            <th scope="col">Whole life</th>
            <th scope="col">Final expense</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">How long it lasts</th>
            <td>10, 15, 20, or 30 years</td>
            <td>Your whole life</td>
            <td>Your whole life</td>
          </tr>
          <tr>
            <th scope="row">Typical coverage</th>
            <td class="tnum">$100,000 to $2,000,000</td>
            <td class="tnum">$25,000 to $500,000</td>
            <td class="tnum">$2,000 to $50,000</td>
          </tr>
          <tr>
            <th scope="row">Medical exam</th>
            <td>Often, sometimes waived</td>
            <td>Usually</td>
            <td>No. Health questions only</td>
          </tr>
          <tr>
            <th scope="row">Builds cash value</th>
            <td>No</td>
            <td>Yes, guaranteed</td>
            <td>Yes, modest</td>
          </tr>
          <tr>
            <th scope="row">Premium over time</th>
            <td>Level during the term, then rises steeply</td>
            <td>Level for life</td>
            <td>Level for life</td>
          </tr>
          <tr>
            <th scope="row">Who it usually suits</th>
            <td>Ages 30 to 55 with a mortgage or children at home</td>
            <td>Ages 40 to 65 with a lifelong need or an estate to settle</td>
            <td>Ages 50 to 85 covering a funeral</td>
          </tr>
        </tbody>
        <tfoot>
          <tr>
            <td></td>
            <td><a class="btn-row" href="/term-life-insurance/#rates">Term rates by age</a></td>
            <td><a class="btn-row" href="/whole-life-insurance/#cash-value">How cash value builds</a></td>
            <td>{call_table}</td>
          </tr>
        </tfoot>
      </table>
    </div>

    <p class="reveal mt-5 text-micro text-muted max-w-3xl">
      Coverage ranges are typical of the carriers we are appointed with. They vary by carrier,
      state, age, and health, and they are not an offer of coverage.
    </p>
  </div>
</section>

<!-- =====================================================================
     FAQ. Native details elements, plus FAQPage schema in the head.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">

      <div class="lg:col-span-4">
        <h2 class="reveal text-h2">Common questions</h2>
        <p class="reveal mt-5 text-ink">
          The six we are asked most often, answered the way we would answer them on the phone.
        </p>
        <p class="reveal mt-6 text-sm text-muted">
          Still stuck? Call and ask. There is no script and no obligation.
        </p>
        <div class="reveal mt-4">{call_faq}</div>
      </div>

      <div class="lg:col-span-7 lg:col-start-6 reveal">
        {faq_html}
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     FINAL CTA, split by intent. Spec section 01.8.
     ================================================================== -->
<section class="section-tight">
  <div class="container-ax">
    <div class="grid md:grid-cols-2 gap-6" data-stagger>

      <div class="reveal card">
        <h2 class="text-h3-serif">Ready for quotes</h2>
        <p class="mt-3 text-ink max-w-md">
          Send us the basics and a licensed agent comes back with what our carriers will actually
          offer you, usually the same business day.
        </p>
        <a class="btn btn-cta mt-6" href="/contact/">Get a free quote</a>
        <p class="mt-3 text-micro text-muted">Free &#183; No obligation &#183; Licensed agents</p>
      </div>

      <div class="reveal card">
        <h2 class="text-h3-serif">Prefer to talk</h2>
        <p class="mt-3 text-ink max-w-md">
          Most of these questions are faster to answer out loud. You will reach a licensed agent,
          not a queue.
        </p>
        {call_final}
        <p class="mt-3 text-micro text-muted">{hours}</p>
      </div>
    </div>
  </div>
</section>
"""


def rest():
    return REST.format(
        steps_how="".join([
            C.step(1, "Tell us the basics",
                   "Your age, your state, whether you use tobacco, roughly what you are trying to cover, "
                   "and the broad strokes of your health. About five minutes by phone or by form.",
                   "We do not ask for a Social Security number or run a credit check in order to quote you."),
            C.step(2, "We compare our carriers",
                   "We run your details against the carriers we are appointed with and come back with what "
                   "each one is likely to offer, including the ones that would decline you.",
                   "Same day for most quotes. If a carrier needs more detail before it will commit, we say "
                   "so rather than guessing on its behalf."),
            C.step(3, "You apply, if it fits",
                   "We submit the application and stay with it through underwriting. If the carrier comes "
                   "back with a different rate class than we quoted, you hear it from us before you accept "
                   "anything.",
                   "Simplified issue policies can be approved the same day. Fully underwritten policies "
                   "usually take three to six weeks."),
        ]),
        call_triage=C.phone_link("triage_result_final", "btn btn-call", "Call " + C.PHONE_DISPLAY),
        call_table=C.phone_link("compare_table_final", "btn-row", "Call about final expense"),
        call_faq=C.phone_link("faq_inline", "btn btn-ghost", "Call " + C.PHONE_DISPLAY),
        call_final=C.phone_link("final_cta_split", "btn btn-call mt-6", "Call " + C.PHONE_DISPLAY),
        agent=C.AGENT_NAME,
        agent_title=C.AGENT_TITLE,
        hours=C.HOURS,
        faq_html="\n          ".join(_acc(q, a) for q, a in FAQ),
    )
