# -*- coding: utf-8 -*-
"""LEVEL TERM LIFE INSURANCE. Spec P2, template T4. Form weighted.

Definitional with product framing. The search intent is almost always one of
two things: someone reading the word on an illustration and wanting to know
what it promises, or someone whose level period is ending and who has just met
the post level premium.

The page is built around the second reader, because that is the one with a
decision to make. The signature object is a two column table setting the level
period against what follows it, which is the whole product in one screen.
"""
import chrome as C

PATH = "/term-life-insurance/level-term/"
OUT = "term-life-insurance/level-term/index.html"
ACTIVE = "/term-life-insurance/"
SILO = "term-life"
TITLE = "Level Term Life Insurance: Fixed Premiums Explained | Apex"
OG_TITLE = "Level term life insurance, explained"
DESC = ("Level term means the premium and the death benefit are fixed for the whole term. What "
        "stays level, what happens the day it stops, and how to read your own policy.")

TRAIL = [("Home", "/"), ("Term Life Insurance", "/term-life-insurance/"),
         ("Level term", None)]

# The product's whole shape, in one table. Nothing here is a price, so nothing
# here is a placeholder.
PERIODS = [
    ("Your premium",
     "Fixed. The same figure every year for the full level period.",
     "Recalculated every year from your current age, and it climbs steeply."),
    ("Your death benefit",
     "Fixed at the face amount you bought.",
     "Usually the same face amount, though some contracts reduce it."),
    ("New health questions",
     "None. Underwriting happened once, before the policy was issued.",
     "None, which is the point of the renewal right and also why it is priced the way it is."),
    ("How long you can keep it",
     "The full term you chose: 10, 15, 20, or 30 years.",
     "Year by year, typically to a contract age in the eighties or nineties."),
    ("What most people do",
     "Pay it and forget it.",
     "Let it lapse, convert it, or replace it. Doing nothing is the expensive option."),
]

FAQ = [
    ("What does level term life insurance mean?",
     "It means two numbers are locked for the whole term: what you pay and what the policy pays "
     "out. A twenty year level term bought today costs the same in year nineteen as in year one, "
     "and pays the same face amount whichever year the claim falls in. Almost every term policy "
     "sold in the United States today is level term, so if an illustration does not say "
     "otherwise, this is what you are looking at."),
    ("Does a level term premium ever increase?",
     "Not during the level period. It can increase the day after it ends, and that increase is "
     "usually dramatic, because the renewal premium is recalculated from your age at that point "
     "with no health underwriting in your favour. The two things that can interrupt a level "
     "premium earlier are a policy loan on a rider and a change you request yourself, such as "
     "adding coverage."),
    ("What is the difference between level term and decreasing term?",
     "The death benefit. Level term pays the same amount in year one and year twenty. Decreasing "
     "term starts at a face amount and steps down over the term, usually tracking a mortgage "
     "balance. Decreasing term is cheaper for the same starting amount and is a poor fit for "
     "anything except a single amortising debt, which is why it is now uncommon outside "
     "mortgage protection products."),
    ("What happens at the end of a level term period?",
     "The level guarantee ends, not necessarily the policy. Most contracts become annually "
     "renewable at a price that resets to your current age and rises every year after that. You "
     "can keep paying it, convert some or all of the coverage to a permanent policy with no new "
     "medical questions if your conversion right has not expired, or let it lapse. Which of those "
     "is right depends almost entirely on your health at that moment."),
    ("Is level term the same as guaranteed level term?",
     "Read the illustration rather than the brochure. A guaranteed level premium cannot change "
     "during the term under any circumstance. A small number of older or non guaranteed designs "
     "quote a current premium alongside a higher guaranteed maximum, which means the carrier may "
     "raise it toward that maximum. We quote guaranteed level term unless you ask us not to, and "
     "we will point out the difference if a carrier's product does not work that way."),
]


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    rows = "\n            ".join(
        '<tr><th scope="row">%s</th><td>%s</td><td>%s</td></tr>' % r for r in PERIODS)

    return f"""
{C.page_hero(
    TRAIL,
    "Level Term Life Insurance",
    'Level term means the premium and the death benefit are both fixed for the entire term you '
    'buy. Twenty years in, you pay what you paid in year one and the policy pays what it promised '
    'in year one. Nearly every '
    '<a class="link" href="/term-life-insurance/">term life insurance</a> policy sold today is '
    'level term, so the word is less a product choice than a description of what you are already '
    'being quoted. What matters is what happens the day the level period ends.')}


<!-- =====================================================================
     THE SIGNATURE OBJECT. The whole product in one table: the level
     period beside what follows it.
     ================================================================== -->
<section class="pb-14 md:pb-16">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2">The level period, and everything after it</h2>
      <p class="reveal mt-5 text-slate">
        Most of what people misunderstand about term insurance lives in the gap between these two
        columns. The left column is what you bought. The right column is what you own the moment
        it ends, unless you have done something about it.
      </p>
    </div>

    <div class="reveal mt-8 table-scroll table-signature">
      <table class="compare-table" style="min-width:46rem">
        <caption class="sr-only">
          What changes at the end of a level term period.
        </caption>
        <thead>
          <tr>
            <th scope="col"><span class="sr-only">Feature</span></th>
            <th scope="col">During the level term</th>
            <th scope="col">After the level term</th>
          </tr>
        </thead>
        <tbody>
            {rows}
        </tbody>
      </table>
    </div>

    <p class="reveal mt-6 text-slate max-w-3xl">
      The right hand column is not a penalty and it is not a trick. Renewal without health
      questions is a valuable right for someone whose health has collapsed, and it is priced as
      though everyone using it is exactly that person. If your health is fine, it is the most
      expensive coverage you will ever be offered.
    </p>
  </div>
</section>


<!-- =====================================================================
     WHAT LEVEL ACTUALLY GUARANTEES. Three cells with the required
     variation: white, blue, tinted.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">What the guarantee covers, precisely</h2>
      <p class="reveal mt-5 text-slate">
        Three things are locked and one thing is not. Knowing which is which is most of what this
        page is for.
      </p>
    </div>

    <div class="mt-10 bento" data-stagger="40">
      <div class="reveal bento-cell bento-cell-blue bento-2">
        <h3 class="text-h4 text-white">The premium is locked</h3>
        <p class="mt-3 text-white/90">
          Contractually guaranteed for the full term on the products we quote. Not a current rate
          that the carrier may revise, an actual guarantee in the contract.
        </p>
      </div>
      <div class="reveal bento-cell bento-2">
        <h3 class="text-h4">The death benefit is locked</h3>
        <p class="mt-3 text-slate">
          The face amount does not erode, does not index, and does not reduce as you age. What you
          bought is what gets paid.
        </p>
      </div>
      <div class="reveal bento-cell bento-cell-tint bento-2">
        <h3 class="text-h4">Your insurability is locked</h3>
        <p class="mt-3 text-slate">
          Once issued, the carrier cannot re underwrite you or cancel the policy because your
          health changed. Only non payment ends it.
        </p>
      </div>
      <div class="reveal bento-cell bento-6">
        <p class="eyebrow">Not locked</p>
        <h3 class="mt-2 text-h4">What the coverage costs after the term ends</h3>
        <p class="mt-3 text-slate">
          This is the one number the guarantee says nothing about, and it is the number that
          surprises people. The renewal premium is set from your attained age and rises every year
          from there. It is a bridge for a few months while you sort something out, and treating it
          as a plan is how a household ends up paying many times over for coverage it could have
          converted years earlier. If you already hold a term policy, find out today which year
          your level period ends and when your conversion right expires. Those two dates are worth
          more than any quote on this site.
        </p>
      </div>
    </div>
  </div>
</section>


{C.inline_cta(
    "Get a guaranteed level premium quoted",
    "We quote guaranteed level term by default and tell you the conversion deadline before you "
    "buy, not fifteen years later. Six questions, and a licensed agent comes back with named "
    "carriers.",
    "term_level_mid", "/term-life-insurance/quotes/", "Get term life quotes")}


<!-- =====================================================================
     PRODUCT FRAMING. Level against the two things people confuse it
     with, in prose rather than a second table.
     ================================================================== -->
{C.prose(
    "Level term, decreasing term, and annually renewable term",
    C.qa("Level term",
         "Fixed premium, fixed death benefit, for a fixed number of years. The default, and the "
         "right default. It suits any need where the amount does not shrink neatly, which is most "
         "of them once children and income are in the picture.")
    + C.qa("Decreasing term",
           "The face amount steps down over the term, usually to follow a mortgage balance. "
           "Cheaper for the same starting figure, and rigid: if you refinance, move, or overpay, "
           "the policy does not follow. It is mostly sold attached to a loan, and a level policy "
           "for the same monthly outlay is nearly always the more useful object.", "mt-8")
    + C.qa("Annually renewable term",
           "One year of coverage that renews each year at a higher price with no new health "
           "questions. This is what a level policy turns into when its level period ends. Bought "
           "deliberately from the start, it is cheap in year one and indefensible by year ten.",
           "mt-8")
    + C.qa("Return of premium term",
           "Level term with a rider that refunds the premiums if you outlive the term. The refund "
           "is real, and so is the extra cost of the rider for every year you pay it. We will "
           "quote it beside a plain level policy so you can see the difference rather than being "
           "told about it.", "mt-8"),
    intro="Three products share the word term and behave nothing alike. A fourth is level term "
          "with a rider bolted on.")}


<!-- =====================================================================
     PRACTICAL. What to do with an existing policy. High utility, and
     the reason this page earns links.
     ================================================================== -->
<section class="section band-navy on-navy">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2 text-white">How to read your own policy in five minutes</h2>
      <p class="reveal mt-5 text-white/85">
        Find the policy schedule, which is usually the second or third page of the contract and is
        also the page your carrier's online portal shows first. Four things are on it.
      </p>
    </div>

    <div class="mt-10 grid md:grid-cols-2 gap-8 lg:gap-10 max-w-5xl" data-stagger="60">
      <div class="reveal">
        <h3 class="text-h4 text-white">The level period end date</h3>
        <p class="mt-3 text-white/85">
          Sometimes printed as a date, sometimes as a policy year. Add the term length to the issue
          date if it is not stated outright.
        </p>
      </div>
      <div class="reveal">
        <h3 class="text-h4 text-white">The conversion expiry</h3>
        <p class="mt-3 text-white/85">
          Often earlier than the end of the term, and often expressed as an age rather than a year.
          This is the deadline that costs people the most.
        </p>
      </div>
      <div class="reveal">
        <h3 class="text-h4 text-white">The guaranteed maximum premium</h3>
        <p class="mt-3 text-white/85">
          If there is a column of numbers rising after the level period, that is the renewal
          schedule. It tells you exactly what year the policy stops being worth keeping.
        </p>
      </div>
      <div class="reveal">
        <h3 class="text-h4 text-white">The rate class you were issued at</h3>
        <p class="mt-3 text-white/85">
          Preferred plus, preferred, standard plus, standard, or a rating. If your health has
          improved since, a reconsideration is often available without a new policy.
        </p>
      </div>
    </div>

    <p class="reveal mt-10 max-w-3xl text-white/85">
      Bring those four to a phone call and a licensed agent can tell you in a few minutes whether
      to convert, replace, or leave it alone. We do not charge for that and we will say leave it
      alone when that is the answer.
    </p>
    <div class="reveal mt-6">
      {C.phone_link("term_level_policy_review", "btn btn-call !bg-white !text-navy")}
    </div>
  </div>
</section>


{C.spoke_module(
    "Related pages in term life",
    "Level term is the shape of the product. These pages cover the length, the price, and the "
    "underwriting.",
    [("/term-life-insurance/20-year-term/", "20 year term",
      "The most common level period, and how to check it fits."),
     ("/term-life-insurance/30-year-term/", "30 year term",
      "When the extra decade of guarantee is worth its price."),
     ("/term-life-insurance/rates/", "Term rates by age",
      "What a level premium actually costs, by age and amount."),
     ("/term-life-insurance/what-is-term-life-insurance/", "What term life insurance is",
      "The plain definition, if you are starting from scratch."),
     ("/term-life-insurance/no-medical-exam/", "No medical exam term",
      "Faster underwriting, and what it does to your class."),
     ("/term-life-insurance/for-seniors/", "Term life after 60",
      "Where a level premium stops being the cheap option.")])}


{C.faq_section("Questions about level term", FAQ, "term-level-faq")}


{C.byline_section()}
"""
