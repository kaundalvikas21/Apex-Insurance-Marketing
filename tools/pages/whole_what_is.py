# -*- coding: utf-8 -*-
"""WHAT IS WHOLE LIFE INSURANCE. Spec P2, template T4. Soft CTA.

The definitional page for the whole life silo. It absorbs "how does whole life
insurance work" and "whole life insurance definition" as H2 sections, so the
silo does not end up with three pages competing for one intent.

CTA weighting for this silo is form and phone at parity with an illustration
request as the tertiary ask, and on a definitional page all three are held
back to a single mid-page block. Someone reading a definition has not decided
anything yet, and the cash value page proves what a hard sell does to this
reader.

The cash-value chart deliberately does NOT appear here. It belongs to
/whole-life-insurance/cash-value/, and duplicating it would give two pages the
same signature object and split the intent.
"""
import chrome as C

PATH = "/whole-life-insurance/what-is-whole-life-insurance/"
OUT = "whole-life-insurance/what-is-whole-life-insurance/index.html"
ACTIVE = "/whole-life-insurance/"
SILO = "whole-life"
TITLE = "What Is Whole Life Insurance? Definition & How It Works | Apex"
OG_TITLE = "What is whole life insurance?"
DESC = ("Whole life insurance is permanent cover with a premium that never rises, a death benefit "
        "that never expires, and a guaranteed cash value. How it works, and who it suits.")

TRAIL = [("Home", "/"), ("Whole Life Insurance", "/whole-life-insurance/"),
         ("What is whole life insurance", None)]

GLOSSARY = [
    ("Face amount", "The death benefit the carrier pays. It does not expire and, on a standard "
                    "policy, it does not change."),
    ("Level premium", "The premium is calculated once, at issue, and is guaranteed never to rise "
                      "for as long as the policy is in force."),
    ("Guaranteed cash value", "A value inside the policy that grows on a schedule printed in the "
                              "contract at issue. You can borrow against it or surrender for it."),
    ("Participating policy", "A policy eligible to receive dividends if the carrier declares them. "
                             "Dividends are never guaranteed."),
    ("Paid up additions", "Small pieces of extra paid up coverage bought with dividends. The "
                          "usual reason a participating policy outgrows its guaranteed column."),
    ("Surrender value", "What the carrier pays if you cancel. Equals the cash value less any "
                        "surrender charge, and in the early years it is often zero."),
    ("Policy loan", "Borrowing against the cash value at a rate set in the contract. Unrepaid "
                    "loans and interest reduce the death benefit."),
    ("Contestability period", "The first two policy years, during which the carrier may review "
                              "the original application before paying a claim."),
]

FAQ = [
    ("What is whole life insurance in simple terms?",
     "It is life insurance that does not expire, at a price that does not change, with a savings "
     "component built into the contract. You pay a fixed premium for as long as you live or until "
     "the policy is paid up. The carrier guarantees to pay a death benefit whenever you die, and "
     "guarantees a schedule of cash values you can borrow against or take by cancelling. It costs "
     "several times what term insurance costs for the same death benefit, and those three "
     "guarantees are what the difference buys."),
    ("How does whole life insurance work?",
     "Your premium is set at issue using your age, health, and the face amount, and it is designed "
     "to be level for life, which means you overpay relative to the risk in the early years and "
     "underpay in the later ones. The overpayment is held in the policy as cash value and grows at "
     "a guaranteed rate. When you die, the carrier pays the face amount. On most standard "
     "policies the cash value is not paid in addition to it: it is the mechanism that funds it."),
    ("Is whole life insurance worth it?",
     "It is worth it when you have a need that does not expire and a budget that can carry a "
     "permanent premium without displacing something more important. It is poor value when it is "
     "bought instead of adequate term coverage, or as a substitute for retirement saving in an "
     "account with better tax treatment and lower costs. The honest test is whether you would "
     "still want the policy if the cash value grew slowly, because on the guaranteed column, in "
     "the early years, it does."),
    ("What is the difference between whole life and term life insurance?",
     "Term covers a fixed number of years and builds nothing. Whole life covers your entire life "
     "and builds a guaranteed cash value. For the same death benefit at the same age, whole life "
     "costs many times more, which is why most households insure a mortgage and an income with "
     "term and use whole life, if at all, for something permanent and smaller."),
    ("Can you cash out a whole life policy?",
     "Yes, in two ways, and both have consequences. You can borrow against the cash value, which "
     "keeps the policy alive but reduces the death benefit by any loan and interest outstanding. "
     "Or you can surrender the policy, which ends the coverage and pays you the surrender value, "
     "with any gain above the premiums you paid taxed as ordinary income. Surrendering in the "
     "first several years frequently returns less than you paid in."),
]


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    glossary_rows = "\n            ".join(
        '<tr><th scope="row">%s</th><td>%s</td></tr>' % (t, d) for t, d in GLOSSARY)

    return f"""
{C.page_hero(
    TRAIL,
    "What Is Whole Life Insurance?",
    'Whole life insurance is permanent coverage: the premium is fixed for life, the death benefit '
    'never expires, and the policy builds a guaranteed cash value you can borrow against. Those '
    'three guarantees are the entire product, and they are why '
    '<a class="link" href="/whole-life-insurance/">whole life insurance</a> costs several times '
    'what the same death benefit costs as term. Whether that is worth paying depends on whether '
    'you have a need that never ends.')}


<!-- =====================================================================
     HOW IT WORKS. Absorbs the "how does whole life insurance work"
     intent as an H2 rather than a second page.
     ================================================================== -->
{C.prose(
    "How whole life insurance works",
    C.step(1, "The premium is calculated once and never recalculated",
           "At issue, from your age, health, sex, and the face amount. It is deliberately higher "
           "than the cost of insuring you at that age, because it has to stay level through the "
           "decades when insuring you gets genuinely expensive.")
    + '<div class="mt-8">' + C.step(2, "The overpayment becomes cash value",
           "The excess in the early years is held inside the policy and credited with guaranteed "
           "interest on a schedule printed in your contract. Early on, most of your premium is "
           "paying acquisition costs and the cost of insurance, which is why the first few years "
           "build very little.")
    + '</div><div class="mt-8">' + C.step(3, "The cash value quietly funds the later years",
           "As you age, the real cost of insuring you passes the premium you are paying. The "
           "accumulated cash value covers the difference. This is the mechanism, and it is why on "
           "a standard policy the cash value is not paid on top of the death benefit.")
    + '</div><div class="mt-8">' + C.step(4, "The carrier pays whenever you die",
           "There is no term to outlive and no renewal to survive. As long as the premium has "
           "been paid or the policy is paid up, a claim gets paid.",
           "Some designs are paid up after a set number of years or at a set age. Others are "
           "designed to be paid for life. That choice changes the premium substantially.")
    + '</div>',
    intro="Four mechanics, and the third one is the part almost nobody is told.")}


<!-- =====================================================================
     THE DEFINITION, absorbed as a glossary table. Signature object.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">The definition, in the contract's own words</h2>
      <p class="reveal mt-5 text-slate">
        A whole life illustration is a dense document, and almost all of the density is these eight
        terms. If you can read this table you can read the illustration.
      </p>
    </div>

    <div class="reveal mt-10 table-scroll table-signature">
      <table class="rate-table" style="min-width:36rem">
        <caption>Standard whole life vocabulary and what each word does.</caption>
        <thead>
          <tr>
            <th scope="col">Term</th>
            <th scope="col">What it means</th>
          </tr>
        </thead>
        <tbody>
            {glossary_rows}
        </tbody>
      </table>
    </div>

    <p class="reveal mt-6 text-slate max-w-3xl">
      One column on every illustration is guaranteed and every other column is an assumption. When
      we send you one, the guaranteed column is the one we talk about first.
    </p>
  </div>
</section>


<!-- =====================================================================
     WHERE THE PREMIUM GOES. Three cells with the mandated variation.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">Where your premium actually goes</h2>
      <p class="reveal mt-5 text-slate">
        Three destinations, in a proportion that changes every year of the policy's life. Knowing
        the split is what makes the early years make sense.
      </p>
    </div>

    <div class="mt-10 bento" data-stagger="40">
      <div class="reveal bento-cell bento-cell-blue bento-2">
        <p class="eyebrow text-white/80">Every year</p>
        <h3 class="mt-2 text-h4 text-white">The cost of insurance</h3>
        <p class="mt-3 text-white/90">
          What it costs the carrier to carry the risk of your death this year. Small when you are
          young, and the reason a level premium has to start high.
        </p>
      </div>
      <div class="reveal bento-cell bento-2">
        <p class="eyebrow">Front loaded</p>
        <h3 class="mt-2 text-h4">Expenses and commission</h3>
        <p class="mt-3 text-slate">
          Underwriting, issue, administration, and the agent's compensation, concentrated in the
          first year or two. This is the honest reason a policy surrendered in year three returns
          so little.
        </p>
      </div>
      <div class="reveal bento-cell bento-cell-tint bento-2">
        <p class="eyebrow">What is left</p>
        <h3 class="mt-2 text-h4">Cash value</h3>
        <p class="mt-3 text-slate">
          The remainder, credited at the guaranteed rate. Modest at first and compounding
          afterwards, which is why whole life rewards decades and punishes second thoughts.
        </p>
      </div>
    </div>

    <p class="reveal mt-8 text-slate max-w-3xl">
      The mechanics of that third cell, including borrowing, surrender, and the tax treatment, have
      a page of their own: <a class="link" href="/whole-life-insurance/cash-value/">how whole life
      cash value works</a>.
    </p>
  </div>
</section>


{C.inline_cta(
    "See what a policy would actually look like",
    "A licensed agent can price this for your age and send a full illustration with the guaranteed "
    "and non guaranteed columns side by side, and the carrier named. Ask for the illustration and "
    "we will send it whether or not you apply.",
    "whole_what_is_mid", "/whole-life-insurance/quotes/", "Get whole life quotes")}


<!-- =====================================================================
     WHO IT SUITS. Equal weight both ways, per MASTER.md's note on the
     whole life hub's section 7b.
     ================================================================== -->
<section class="section band-surface">
  <div class="container-ax">
    <div class="grid lg:grid-cols-2 gap-8 lg:gap-10 items-start">

      <div class="reveal card">
        <h2 class="text-h3 !font-display !font-semibold">When whole life is the right product</h2>
        <ul class="mt-5 grid gap-4 text-slate">
          <li>A dependant who will need support for their whole life, not for twenty years.</li>
          <li>A funeral and final bills you want covered whenever they arrive.</li>
          <li>An estate likely to owe tax or need liquidity at settlement.</li>
          <li>A business buy sell agreement or a key person the business cannot replace cheaply.</li>
          <li>A deliberate choice to hold a portion of your savings somewhere guaranteed and
              uncorrelated, made with your eyes open about the cost.</li>
        </ul>
        <p class="mt-5 text-slate">
          Every one of those needs is permanent. That is the only test that matters here.
        </p>
      </div>

      <div class="reveal card">
        <h2 class="text-h3 !font-display !font-semibold">When it is the wrong one</h2>
        <ul class="mt-5 grid gap-4 text-slate">
          <li>You have a mortgage and young children and are not yet adequately insured. Buy the
              coverage first, with term, and consider permanent afterwards.</li>
          <li>The premium would displace an employer retirement match, or high interest debt
              repayment. Both beat this comfortably.</li>
          <li>You are being sold it as an investment. It is insurance with a guaranteed savings
              component, and it should be compared with that framing.</li>
          <li>There is a real chance you would cancel within ten years. Early surrender is where
              this product does the most financial damage.</li>
        </ul>
        <p class="mt-5 text-slate">
          The comparison worth reading before you decide is
          <a class="link" href="/compare/term-vs-whole-life-insurance/">term life against whole
          life</a>, with the cost over thirty years worked through.
        </p>
      </div>
    </div>
  </div>
</section>


{C.spoke_module(
    "Keep reading in this section",
    "Everything below is whole life. Each page assumes you have read this one.",
    [("/whole-life-insurance/rates/", "Whole life rates",
      "Premium by age and coverage amount, from current rate cards."),
     ("/whole-life-insurance/calculator/", "Whole life calculator",
      "Size the permanent need before you price it."),
     ("/whole-life-insurance/for-seniors/", "Whole life for seniors",
      "What is available after 65, and what it is actually for."),
     ("/whole-life-insurance/guaranteed-acceptance/", "Guaranteed acceptance",
      "No health questions, and exactly what that costs you."),
     ("/whole-life-insurance/dividends/", "Dividends explained",
      "How they are declared, and why they are never guaranteed."),
     ("/whole-life-insurance/is-it-worth-it/", "Is whole life worth it?",
      "The case for and against, side by side.")])}


{C.faq_section("Common questions about whole life insurance", FAQ, "whole-what-is-faq")}


{C.byline_section()}
"""
