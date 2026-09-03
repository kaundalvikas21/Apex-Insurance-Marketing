# -*- coding: utf-8 -*-
"""GUARANTEED ACCEPTANCE WHOLE LIFE. Spec P1, template T4. PHONE FIRST.

The second phone-first exception in this silo. The reason is not the same as
the seniors page: here the visitor has usually already been declined somewhere,
and the only useful next step is a person telling them whether they actually
need this product or whether a simplified issue carrier would still take them.
A five field form cannot ask that question, and getting it wrong is expensive
for the visitor rather than for us.

*** CONSOLIDATION FLAG. See the comment at the top of body(). ***

`#who-it-is-for` is a contract. The whole life hub's "If you cannot qualify"
card deep-links to it, and check.py strips fragments when it crawls links, so
nothing will catch it if the id is removed. See REPLACE-BEFORE-LAUNCH.md
section 6.

The rate chart uses rate_chart's "call" row CTA rather than the prefill button,
which is what that mode is for on a phone weighted page.
"""
import chrome as C

PATH = "/whole-life-insurance/guaranteed-acceptance/"
OUT = "whole-life-insurance/guaranteed-acceptance/index.html"
ACTIVE = "/whole-life-insurance/"
SILO = "whole-life"
TITLE = "Guaranteed Acceptance Whole Life Insurance | No Health Questions"
OG_TITLE = "Guaranteed acceptance whole life insurance"
DESC = ("Guaranteed acceptance whole life asks no health questions and declines nobody within the "
        "issue ages. What the waiting period pays, what it costs, and when to try something else.")

TRAIL = [("Home", "/"), ("Whole Life Insurance", "/whole-life-insurance/"),
         ("Guaranteed acceptance", None)]

LEAD = (
    "Guaranteed acceptance whole life asks no health questions, orders no medical records, and "
    "turns nobody down inside its issue ages. It is real "
    '<a class="link" href="/whole-life-insurance/">whole life insurance</a>: level premium, '
    "permanent coverage, guaranteed cash value. What you pay for the acceptance is the highest "
    "cost per dollar of coverage of anything we place, plus a waiting period during which a death "
    "from natural causes returns your premiums rather than the face amount. It is a real answer "
    "for people who have no other one, and the wrong answer for anyone who could still pass a "
    "short health questionnaire.")

AGE_BANDS = [("50 to 54", None), ("55 to 59", None), ("60 to 64", None), ("65 to 69", None),
             ("70 to 74", None), ("75 to 79", None), ("80 to 85", None)]
COVERAGE_COLS = ["$5,000", "$10,000", "$25,000"]

# A behaviour table, not a price table: it describes what the contract pays in
# each window. MASTER.md section 6 rule 6, so no $-- cells and no rate flag.
WAITING = [
    ("Death from an accident, any time",
     "Full face amount, from the first day the policy is in force."),
    ("Death from illness or natural causes, policy year 1",
     "Premiums paid returned, normally with interest. Not the face amount."),
    ("Death from illness or natural causes, policy year 2",
     "Premiums paid returned with interest, or in some contracts a stated percentage of the face "
     "amount. Carrier and state dependent."),
    ("Death from illness or natural causes, policy year 3 onward",
     "Full face amount. The waiting period is over and does not come back."),
]

FAQ = [
    ("Is guaranteed acceptance life insurance really guaranteed?",
     "Acceptance is guaranteed, within the issue ages and the coverage limits the carrier sets. "
     "There are no health questions, no exam, and no prescription check, so there is no decline. "
     "What is not guaranteed is that the full death benefit is payable immediately: nearly every "
     "one of these policies has a two or three year waiting period for death from natural causes, "
     "and that is the trade you are making for the acceptance."),
    ("What happens if I die during the waiting period?",
     "If the death is accidental, the full face amount is paid from day one. If it is from "
     "illness or natural causes, the carrier returns the premiums you have paid, normally with "
     "interest, rather than the face amount. Some contracts pay a stated percentage of the face "
     "amount in year two instead. Read the schedule page of the policy, not the brochure, and ask "
     "us to read it with you."),
    ("Who is guaranteed acceptance actually for?",
     "Someone inside the issue ages who has been declined for a simplified issue policy, or whose "
     "health history contains something that is a knockout question at every carrier we can "
     "reach: a recent cancer diagnosis, dialysis, oxygen use, an organ transplant, a terminal "
     "diagnosis, or a nursing home admission. If none of those describe you, you are probably "
     "eligible for something cheaper and you should let us check before buying this."),
    ("How much coverage can I get without health questions?",
     "Small amounts, by design. Most carriers write these policies in a band that stops well "
     "short of what a fully underwritten policy would offer, because the carrier is accepting "
     "everyone and has to price for that. The product is built to cover a funeral and the bills "
     "that follow it, not to replace an income or fund an estate."),
    ("Is guaranteed acceptance a rip off?",
     "It is expensive, and being sold one when a cheaper policy would have taken you is the "
     "problem worth naming. The product itself is not dishonest: for someone who genuinely cannot "
     "be underwritten, it is the only permanent coverage available, and a small policy that "
     "actually pays is better than an uninsured funeral. The failure is an agent who leads with "
     "it. Any agent who quotes you this before trying a simplified issue carrier is not working "
     "for you."),
    ("Can I be turned down because of my age?",
     "Yes. Age is the one thing that can make you ineligible, because every carrier sets an issue "
     "age band and stops writing outside it. Bands commonly run from around fifty to around "
     "eighty five, and they vary by carrier and by state. That is a reason to ask early rather "
     "than to assume."),
]


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    waiting_rows = "\n            ".join(
        '<tr><th scope="row">%s</th><td>%s</td></tr>' % r for r in WAITING)

    hero_cta = """<div class="reveal mt-8">
        %s
        <p class="mt-3 text-micro text-muted">%s</p>
      </div>""" % (C.phone_link("whole_ga_hero", "btn btn-call btn-xl",
                                "Call " + C.PHONE_DISPLAY, 26), C.HOURS)

    return f"""
<!-- =====================================================================
     [CONSOLIDATION READY - spec P1 overlap flag]

     This page overlaps deliberately with three others, and the overlap was
     flagged in the brief rather than discovered later:

       - /whole-life-insurance/for-seniors/ carries the three acceptance
         routes and links here for the detail on the third one.
       - /final-expense-insurance/ and its spokes describe the same
         underwriting trade at smaller face amounts under a different name.
       - /final-expense-insurance/no-waiting-period/ is the mirror of this
         page's waiting period section, written for the other silo.

     If search console shows these cannibalising each other, the intended
     consolidation is: keep the two hub-level pages, 301 this path into
     /whole-life-insurance/for-seniors/#acceptance, and move the waiting
     period table there. Nothing here is written to depend on that decision:
     the sections are self contained and the only inbound deep link is the
     hub's, at #who-it-is-for.

     Do NOT delete the page to resolve the overlap while eight built pages
     still link to it.
     ================================================================== -->

{C.page_hero(TRAIL, "Guaranteed Acceptance Whole Life Insurance", LEAD,
             extra=hero_cta,
             media=C.figure("whole-acceptance", C.MEDIA_SIZES, eager=True))}


{C.prose(
    "What you are actually buying",
    """
        <p class="reveal text-slate">
          A small permanent policy with three ordinary whole life guarantees and one unusual
          condition attached. The premium is fixed at issue and cannot be raised. The death
          benefit does not shrink as you age. A guaranteed cash value builds slowly in the
          background. None of that is different from any other whole life contract.
        </p>
        <p class="reveal mt-5 text-slate">
          The unusual condition is at the front. Because the carrier is accepting everyone who
          applies, including people who are already seriously ill, it cannot pay a full claim in
          the first two years without being used as a way of buying a payout on a known diagnosis.
          So it does not. For that window it returns your money instead, and accidental death is
          carved out and paid in full from the first day.
        </p>
        <p class="reveal mt-5 text-slate">
          Everything that makes this product expensive follows from that one sentence. You are not
          paying more because the coverage is better. You are paying more because the carrier is
          not allowed to look at you first.
        </p>""",
    intro="No health questions, no exam, no prescription check, and no decline inside the issue "
          "ages. Here is what that costs and what it buys.",
    media=C.figure("whole-arbor", C.MEDIA_SIZES))}


<!-- =====================================================================
     #who-it-is-for is a CONTRACT. The whole life hub's "If you cannot
     qualify" card deep-links to it. check.py strips fragments when it
     crawls, so nothing else guards this id. Do not rename it.
     ================================================================== -->
<div id="who-it-is-for" class="sr-only" aria-hidden="true"></div>

{C.prose(
    "Who it is for",
    """
        <p class="reveal text-slate">
          One group, and it is smaller than the advertising for this product implies. You are in
          it if you are inside the issue ages and one of these is true.
        </p>
        <ul class="reveal mt-6 grid gap-3">
          <li class="flex items-start gap-2.5"><span class="text-slate">A simplified issue carrier
          has already declined you, and we have tried more than one.</span></li>
          <li class="flex items-start gap-2.5"><span class="text-slate">Your history contains
          something that is a knockout question almost everywhere: a recent cancer diagnosis,
          dialysis, oxygen use at home, an organ transplant, a terminal diagnosis, or a current
          nursing home admission.</span></li>
          <li class="flex items-start gap-2.5"><span class="text-slate">You are unwilling to
          answer health questions at all, and you understand what that decision costs you in
          premium and in the waiting period.</span></li>
        </ul>
        <p class="reveal mt-6 text-slate">
          If none of those describe you, this is not your product yet. The order that protects you
          is simple: fully underwritten first, simplified issue second, this third. Skipping to
          the third because it is the easiest to buy is how people end up paying several times
          what they needed to, with a two year gap they did not know about.
        </p>
        <p class="reveal mt-5 text-slate">
          After roughly sixty five the middle route is where most applicants actually land, and
          the comparison of all three sits on
          <a class="link" href="/whole-life-insurance/for-seniors/">whole life insurance for
          seniors</a>. It is worth reading before you buy anything on this page.
        </p>""",
    intro="Written narrowly on purpose. Most people who arrive here searching for no health "
          "questions can still be underwritten, and would be better off.")}


<!-- =====================================================================
     THE WAITING PERIOD. A behaviour table, not a price table: MASTER.md
     section 6 rule 6, so no $-- cells and no rate flag.
     ================================================================== -->
<section class="section band" id="waiting-period">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2">The waiting period, stated plainly</h2>
      <p class="reveal mt-5 text-slate">
        This is the part that gets skipped in the advertising, and it is the only part that
        matters if the worst happens early. Read it before you read the premium.
      </p>
    </div>

    <div class="reveal mt-8 table-scroll table-signature">
      <table class="rate-table" style="min-width:34rem">
        <caption class="sr-only">
          What a guaranteed acceptance whole life policy pays in each period.
        </caption>
        <thead>
          <tr>
            <th scope="col">When the claim happens</th>
            <th scope="col">What the policy pays</th>
          </tr>
        </thead>
        <tbody>
            {waiting_rows}
        </tbody>
      </table>
    </div>

    <p class="reveal mt-6 text-slate max-w-3xl">
      Two years is the common shape. Three exists, and so does a graded structure that pays a
      rising percentage instead of returning premiums. The differences are real money, they are
      set out on the policy schedule rather than in the brochure, and comparing them across
      carriers is the single most useful thing an agent can do for you on this product.
    </p>
  </div>
</section>


<!-- =====================================================================
     WHAT IT COSTS. Row level click-to-call inside the age cell, which is
     what rate_chart's "call" mode is for on a phone weighted page.
     ================================================================== -->
<section class="section" id="rates">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2">What it costs, by age</h2>
      <p class="reveal mt-5 text-slate">
        Monthly premium for a guaranteed acceptance policy, fixed for life at issue. Every row has
        a button that puts you through to a licensed agent who can price that band for your state
        in a few minutes, and who will tell you first whether you could avoid this product
        altogether.
      </p>
      <div class="reveal mt-6">
        {C.rates_flag("premiums")}
      </div>
    </div>

    {C.rate_chart(
        panels_id="whole-ga-rates",
        cols=COVERAGE_COLS,
        rows=AGE_BANDS,
        toggles=[("Show premiums for", "wga-sex",
                  [("female", "Female"), ("male", "Male")], None)],
        caption="Monthly premium by age band and coverage amount.",
        row_cta="call",
        cta_location="whole_ga_rate_row",
        min_width="40rem",
        top_margin="mt-8",
        aside="No tobacco split: these policies do not ask, which is part of what you are "
              "paying for.")}

    <p class="reveal mt-8 text-slate max-w-3xl">
      Expect the cost per thousand of coverage to be the highest on this site, and expect the
      available face amounts to be the smallest. Both are the same fact seen from two directions.
      The wider grid for underwritten policies is on the
      <a class="link" href="/whole-life-insurance/rates/">whole life insurance rates</a> page, and
      the gap between the two is the price of not being asked any questions.
    </p>
  </div>
</section>


<!-- =====================================================================
     WHEN NOT TO BUY IT. The section this page exists to carry.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">When not to buy this</h2>
        <p class="reveal mt-5 text-slate">
          Four situations where the right answer is something else. An agent who does not raise
          them before selling you this policy has not done the job.
        </p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        {C.step(1, "You have not been declined yet",
                "Being nervous about health questions is not the same as failing them. Simplified "
                "issue carriers differ sharply about what is a knockout, and a decline at one is "
                "not a decline everywhere. Try, and let the carriers answer.")}
        <div class="mt-8">
          {C.step(2, "You expect to live well past the waiting period and can be underwritten",
                  "If you are healthy enough to be quoted at all, the same money buys "
                  "substantially more coverage without a gap at the front. The waiting period is "
                  "only free if you outlive it, and you cannot spend the difference in premium "
                  "you overpaid to get it.")}
        </div>
        <div class="mt-8">
          {C.step(3, "The premium would strain your budget",
                  "A policy that lapses at eighty two because the payment became unaffordable is "
                  "the worst outcome on this page. Buy an amount you can carry through a bad year, "
                  "not the largest one you qualify for.",
                  "Cash value in these policies is small and slow. Do not plan on borrowing from it.")}
        </div>
        <div class="mt-8">
          {C.step(4, "What you actually need is a funeral covered",
                  "Then you are looking for a product built for that job, in that size, from "
                  "carriers who specialise in it. Same contract type, different market, and "
                  "usually a better price for the same face amount.")}
        </div>
      </div>
    </div>
  </div>
</section>


{C.inline_cta(
    "One call tells you whether you need this product at all",
    "Tell a licensed agent your age, your state, and what you take. Before anyone quotes you a "
    "guaranteed acceptance policy we will check whether a simplified issue carrier would still "
    "write you, because that is almost always the cheaper answer. No application, and no "
    "obligation either way.",
    "whole_ga_mid", "/whole-life-insurance/quotes/", "Or start a quote online",
    phone_first=True)}


<!-- =====================================================================
     THE OFF RAMP. Cross silo via the hub, per spec s07 rule 3.
     ================================================================== -->
<section class="section band-navy on-navy">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-6">
        <h2 class="reveal text-h2 text-white">If this is about covering a funeral</h2>
        <p class="reveal mt-5 text-white/85">
          Say so on the call, because it changes which carriers we approach. The product built for
          that job is sold under a different name:
          <a class="link !text-white" href="/final-expense-insurance/">final expense
          insurance</a>. It is the same contract type in a smaller size, and most of it is written
          with a short health questionnaire rather than with no questions at all.
        </p>
        <p class="reveal mt-5 text-white/85">
          That distinction is worth money. A carrier that specialises in ten and fifteen thousand
          dollar policies and is willing to ask three questions will frequently beat a guaranteed
          acceptance premium by a wide margin, for the same face amount, with no waiting period at
          the front. You only find that out by being asked the questions.
        </p>
      </div>
      <div class="lg:col-span-5 lg:col-start-8">
        <div class="reveal card">
          <h3 class="text-h4 !text-ink">The order that protects you</h3>
          <p class="mt-3 text-slate">
            Fully underwritten first, because it is cheapest per thousand. Simplified issue second,
            because it is where most people at these ages actually land. Guaranteed acceptance
            third, and only after the first two have said no. We work that order out loud on the
            call so you can hear which door closed and why.
          </p>
          <div class="mt-5">
            {C.phone_link("whole_ga_offramp", "btn btn-call btn-block")}
          </div>
          <p class="mt-3 text-micro text-muted text-center">{C.HOURS}</p>
        </div>
      </div>
    </div>
  </div>
</section>


{C.spoke_module(
    "Also in whole life insurance",
    "The pages most people read next when they are working out whether they need this policy.",
    [("/whole-life-insurance/what-is-whole-life-insurance/", "What whole life insurance is",
      "The definition and the mechanics, if you are starting fresh."),
     ("/whole-life-insurance/cash-value/", "How cash value works",
      "What it does, and how little it does in a policy this small."),
     ("/whole-life-insurance/dividends/", "Dividends explained",
      "Why these policies rarely pay one."),
     ("/whole-life-insurance/is-it-worth-it/", "Is whole life worth it?",
      "The case for and against, side by side."),
     ("/whole-life-insurance/calculator/", "Whole life calculator",
      "Size the permanent need before you price it.")])}


{C.faq_section("Questions about guaranteed acceptance", FAQ, "whole-ga-faq")}


{C.byline_section()}
"""
