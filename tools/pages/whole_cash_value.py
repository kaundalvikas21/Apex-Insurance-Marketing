# -*- coding: utf-8 -*-
"""WHOLE LIFE CASH VALUE. Spec P2, template T4. SOFT CTA ONLY.

The audience is financially literate and is comparing this against investing
the difference. The spec is explicit that hard selling this reader loses them,
so there is no amber button on the page, no form, and one soft ask near the
end: see an illustration for your age.

The buy term and invest the difference section is written to be genuinely
balanced rather than balanced-looking. If it reads as a rebuttal it has failed,
because this reader has already heard the rebuttal and can tell.

The cash-value chart is whole.cash_value_chart() reused verbatim. It is the
silo's signature object and this is its canonical home; a second, richer chart
here would give two pages competing signature objects for one intent. It
carries no dollar amounts, is labelled illustrative on its face, and its draw-in
collapses under prefers-reduced-motion like every other motion on the site.

Tax copy is general information with a named caveat, not advice.
"""
import chrome as C
import whole

PATH = "/whole-life-insurance/cash-value/"
OUT = "whole-life-insurance/cash-value/index.html"
ACTIVE = "/whole-life-insurance/"
SILO = "whole-life"
TITLE = "Whole Life Insurance Cash Value: How It Works | Apex"
OG_TITLE = "How whole life cash value works"
DESC = ("What cash value is, how guaranteed and non guaranteed growth differ, what borrowing "
        "really costs, the tax treatment, and an honest look at investing the difference instead.")

TRAIL = [("Home", "/"), ("Whole Life Insurance", "/whole-life-insurance/"),
         ("Cash value", None)]

COLUMNS = [
    ("Where it comes from",
     "A schedule printed in your contract at issue.",
     "Dividends the carrier declares each year from its actual mortality, expense, and investment "
     "experience."),
    ("Is it promised",
     "Yes. Contractually, for every policy year, at issue.",
     "No. Never. A dividend can be reduced or not paid at all, and carriers have done both."),
    ("How it behaves early",
     "Very little in the first few years. Acquisition costs come out first.",
     "Usually nothing at all for the first year or two, then small."),
    ("What it does over decades",
     "Compounds steadily and predictably. Modest.",
     "Historically the larger part of the growth on a participating policy, usually reinvested as "
     "paid up additions."),
    ("What to plan on",
     "This column, and only this column.",
     "Treat as upside. If the plan only works on this column, the plan does not work."),
]

FAQ = [
    ("How does cash value work in a whole life policy?",
     "Your premium is level for life, which means in the early years you pay more than it costs "
     "the carrier to insure you. That excess, after acquisition costs and the cost of insurance, "
     "is credited to a cash value inside the policy and grows at a guaranteed rate set in the "
     "contract. You can borrow against it, or take it by surrendering the policy. On a standard "
     "whole life contract it is not paid in addition to the death benefit: it is the mechanism "
     "that lets the carrier promise a level premium for life."),
    ("How long before a whole life policy builds cash value?",
     "Typically very little in the first two or three years and meaningful amounts from somewhere "
     "in the second decade, though it varies a great deal by carrier and by how the policy is "
     "designed. The reason is that first year costs, including underwriting, issue, and "
     "commission, come out before anything is credited. This is the single most important thing "
     "to understand before buying: whole life punishes early surrender severely, and a policy you "
     "might cancel in year four is a policy you should not buy."),
    ("Do you lose the cash value when you die?",
     "On a standard whole life policy, yes in the sense that your beneficiaries receive the death "
     "benefit rather than the death benefit plus the cash value. That is not the carrier keeping "
     "your money, it is the cash value having done its job of funding the benefit. Some carriers "
     "offer a rider or a policy design where the cash value is added to the death benefit, and it "
     "costs more. If that matters to you, ask for it explicitly, because it is not the default."),
    ("Is a policy loan taxable?",
     "Generally not while the policy stays in force, because a loan is not income. The trap is "
     "what happens if the policy lapses or is surrendered with a loan outstanding: the loan can "
     "then be treated as a distribution, and any gain above the premiums you paid becomes taxable "
     "as ordinary income, in a year when you have already spent the money. Talk to a tax "
     "professional about your own circumstances before relying on any of this."),
    ("Should I buy term and invest the difference instead?",
     "For most households with a mortgage and young children, buying adequate term coverage first "
     "is not optional, it is the base case, and a whole life premium that crowds out that coverage "
     "is the wrong trade. Whether to invest the difference or fund a permanent policy after that "
     "is a genuine question with a real answer on both sides, and it depends on your tax position, "
     "your discipline, whether the need is actually permanent, and how much you value a guarantee "
     "over an expected return. Anyone who tells you one answer always wins is selling something."),
]


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    column_rows = "\n            ".join(
        '<tr><th scope="row">%s</th><td>%s</td><td>%s</td></tr>' % r for r in COLUMNS)

    return f"""
{C.page_hero(
    TRAIL,
    "How Whole Life Insurance Cash Value Works",
    'Cash value is a pot of money inside a permanent policy that grows on a schedule printed in '
    'your contract, which you can borrow against or take by cancelling. It exists because '
    '<a class="link" href="/whole-life-insurance/">whole life insurance</a> charges a level '
    'premium for a risk that rises every year, so the early overpayment has to be held somewhere. '
    'It is a real asset with real constraints, and most of what is written about it oversells one '
    'and ignores the other.',
    media=C.figure("whole-ledger", C.MEDIA_SIZES, eager=True))}


<!-- =====================================================================
     WHAT IT IS. Mechanics first, no chart yet: the chart is easier to
     read once the reader knows what the two lines are.
     ================================================================== -->
{C.prose(
    "What cash value actually is",
    C.qa("It is the by-product of a level premium",
         "Insuring a forty year old for a year is cheap. Insuring an eighty year old for a year is "
         "not. A premium that stays level across both has to be too high at the start and too low "
         "at the end, and the surplus from the first half is what funds the second. That surplus, "
         "credited with interest, is your cash value.")
    + C.qa("It is inside the policy, not beside it",
           "It is not an account you own separately. It is a value the contract attributes to your "
           "policy, and every way of getting at it changes the policy: a loan reduces the death "
           "benefit until repaid, a withdrawal reduces it permanently, and a surrender ends it.",
           "mt-8")
    + C.qa("It is slow at the start by design",
           "First year costs, underwriting, issue, and commission, come out before anything is "
           "credited. A policy surrendered in year three commonly returns less than was paid into "
           "it. This is the fact that decides whether whole life is right for you, and it is the "
           "one most often left to the small print.", "mt-8")
    + C.qa("It is not the death benefit",
           "On a standard policy your beneficiaries receive the face amount, not the face amount "
           "plus the cash value. Designs that pay both exist and cost more. If you want that, ask "
           "for it by name, because it is not what you will be quoted by default.", "mt-8"),
    intro="Four facts, in the order that makes the rest of the page make sense.")}


<!-- =====================================================================
     THE CHART. Shape only, no dollar amounts, labelled illustrative on
     its face. Reused from the hub: this is its canonical home.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">The shape of the first forty years</h2>
      <p class="reveal mt-5 text-slate">
        No dollar amounts, because putting numbers on this axis without a carrier illustration
        behind them would be inventing a projection. The shape, however, is consistent across
        carriers and is the thing worth understanding.
      </p>
    </div>

    <div class="mt-10 bento" data-stagger="40">
      {whole.cash_value_chart()}
      <div class="reveal bento-cell bento-cell-tint bento-2">
        <p class="eyebrow">Reading the chart</p>
        <p class="mt-3 text-slate">
          The gap on the left is not a fee you are being charged. It is acquisition cost plus the
          cost of insuring you, and it is why the crossover exists at all.
        </p>
        <p class="mt-4 text-slate">
          Where that crossover falls is the single most useful number on a real illustration. Ask
          for it explicitly, on the guaranteed column, before you ask about anything else.
        </p>
        <p class="mt-4 text-slate">
          If you cannot see yourself holding the policy well past that point, the honest conclusion
          is that this is not the right product for you, and we would rather say so here.
        </p>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     GUARANTEED VS NON GUARANTEED. The comparison table that stops an
     illustration's best column being read as a promise.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2">Guaranteed growth and non guaranteed growth</h2>
      <p class="reveal mt-5 text-slate">
        Every whole life illustration has at least two columns of cash value. They are not two
        estimates of the same thing. One is a contract and the other is a projection, and the
        difference between them at year thirty is often very large.
      </p>
    </div>

    <div class="reveal mt-8 table-scroll table-signature">
      <table class="compare-table" style="min-width:46rem">
        <caption class="sr-only">
          Guaranteed cash value compared with non guaranteed dividend growth.
        </caption>
        <thead>
          <tr>
            <th scope="col"><span class="sr-only">Feature</span></th>
            <th scope="col">Guaranteed</th>
            <th scope="col">Non guaranteed</th>
          </tr>
        </thead>
        <tbody>
            {column_rows}
        </tbody>
      </table>
    </div>

    <p class="reveal mt-6 text-slate max-w-3xl">
      When we send an illustration, we point at the guaranteed column first and say plainly which
      figures are assumptions. How dividends are declared, and why a long record of paying them is
      still not a promise, is covered on
      <a class="link" href="/whole-life-insurance/dividends/">dividends and participating
      policies</a>.
    </p>
  </div>
</section>


<!-- =====================================================================
     BORROWING. Mechanics and consequences, given equal space, because
     this is where policies quietly fail.
     ================================================================== -->
{C.prose(
    "Borrowing against the cash value",
    C.step(1, "You request a loan from the carrier",
           "No credit check, no approval, no stated purpose. The cash value is the collateral, and "
           "the money usually arrives within days. This genuine flexibility is a large part of why "
           "people value the product.")
    + '<div class="mt-8">' + C.step(2, "Interest accrues from day one",
           "At a rate set in the contract, which may be fixed or variable. It is charged whether "
           "or not you repay, and unpaid interest is usually added to the loan balance, so it "
           "compounds.")
    + '</div><div class="mt-8">' + C.step(3, "The death benefit is reduced while the loan stands",
           "By the loan plus accrued interest. If you die with a loan outstanding, your "
           "beneficiaries receive the face amount less that balance. Nothing is hidden about this, "
           "and almost nobody remembers it.")
    + '</div><div class="mt-8">' + C.step(4, "The policy can collapse under the loan",
           "If the loan and its interest grow to approach the cash value, the carrier will demand "
           "repayment or the policy lapses. A lapse with a loan outstanding is the worst case on "
           "this page: the coverage ends and the gain above the premiums you paid can become "
           "taxable income in that year.",
           "Ask your carrier for an in force illustration once a year if you carry a loan. It is "
           "free and it is the only way to see this coming.")
    + '</div>',
    intro="A policy loan is not a withdrawal and it is not free money. It is a secured loan from "
          "the carrier, and the security is your own death benefit.",
    cls="section band-surface")}


<!-- =====================================================================
     WITHDRAWALS AND SURRENDER.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-2 gap-8 lg:gap-10 items-start">

      <div class="reveal card">
        <h2 class="text-h3 !font-display !font-semibold">Withdrawals</h2>
        <p class="mt-4 text-slate">
          On a participating whole life policy, what is usually described as a withdrawal is the
          surrender of paid up additions: you are selling back small pieces of extra coverage that
          dividends bought. The money is yours, and the death benefit falls permanently by more
          than the amount you take.
        </p>
        <p class="mt-4 text-slate">
          Withdrawals up to the total premiums you have paid are generally received tax free, as a
          return of your own basis. Anything above that is generally taxable. A withdrawal cannot
          usually be repaid, which is the practical difference from a loan.
        </p>
      </div>

      <div class="reveal card">
        <h2 class="text-h3 !font-display !font-semibold">Surrender</h2>
        <p class="mt-4 text-slate">
          Cancelling the policy for its surrender value. The coverage ends, and if you are older or
          in worse health than when you bought it, replacing that coverage will cost considerably
          more or may not be possible at all.
        </p>
        <p class="mt-4 text-slate">
          In the early years the surrender value is often less than the premiums paid, sometimes
          much less. Before surrendering, ask about reduced paid up coverage, which converts the
          policy into a smaller, fully paid up one with no further premiums. It is frequently a
          better outcome than taking the cash, and it is rarely offered unprompted.
        </p>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     TAX. General information with a named caveat and a visible flag.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">How it is taxed</h2>
        <p class="reveal mt-5 text-slate">
          In general terms, under current federal rules, for a policy that is not a modified
          endowment contract. Every one of those qualifications does real work.
        </p>
        <div class="reveal mt-6">
          {C.flag("This section is general information, not tax advice, and it is not written for "
                  "your circumstances. Tax treatment depends on federal and state law, on how the "
                  "policy is funded, and on facts specific to you. Consult a qualified tax "
                  "professional before acting on any of it. Nothing on this site should be relied "
                  "on as tax or legal advice.", "GENERAL INFORMATION ONLY")}
        </div>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        {C.qa("The death benefit",
              "Generally received by beneficiaries free of federal income tax. It can still be "
              "counted in your estate for estate tax purposes if you owned the policy, which is a "
              "different tax and one an estate attorney should look at where the amounts are "
              "large.")}
        {C.qa("Growth inside the policy",
              "Generally not taxed as it accrues. This tax deferral is one of the genuine "
              "structural advantages of the product, and it is also the feature most often "
              "oversold, because the growth being deferred is modest on the guaranteed column.",
              "mt-8")}
        {C.qa("Money you take out",
              "Generally treated as a return of your premiums first and taxed only above that. "
              "Loans are generally not taxable while the policy stays in force, and can become "
              "taxable if it lapses or is surrendered with a loan outstanding.", "mt-8")}
        {C.qa("Modified endowment contracts",
              "If a policy is funded faster than federal limits allow, it becomes a modified "
              "endowment contract, and the tax treatment of loans and withdrawals changes for the "
              "worse and does so permanently. Any agent proposing to overfund a policy should "
              "raise this before you do.", "mt-8")}
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     THE HONEST COMPARISON. This is the section the reader came for.
     If it reads as a rebuttal it has failed.
     ================================================================== -->
<section class="section band-navy on-navy">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2 text-white">Buy term and invest the difference</h2>
      <p class="reveal mt-5 text-white/85">
        This is the strongest argument against whole life and it deserves a straight answer rather
        than a rebuttal. Here is ours, including the part that does not favour us.
      </p>
    </div>

    <div class="mt-10 grid lg:grid-cols-2 gap-8 lg:gap-10 max-w-5xl" data-stagger="60">

      <div class="reveal">
        <h3 class="text-h3 !font-display !font-semibold text-white">Where the argument is right</h3>
        <ul class="mt-5 grid gap-4 text-white/85">
          <li>For the same premium you can buy far more death benefit with term, and during the
              years a young family is most exposed, the amount of coverage matters more than
              anything else on this page.</li>
          <li>A low cost index fund inside a tax advantaged account has historically produced a
              higher expected return than the guaranteed column of a whole life policy, at lower
              cost, with better liquidity.</li>
          <li>Whole life is expensive to exit early, and life is unpredictable. Flexibility has
              real value that an illustration does not price.</li>
          <li>Most whole life sold to households who had no term coverage was sold in the wrong
              order, and that is an industry failure rather than a misunderstanding by the buyer.</li>
        </ul>
      </div>

      <div class="reveal">
        <h3 class="text-h3 !font-display !font-semibold text-white">Where it is incomplete</h3>
        <ul class="mt-5 grid gap-4 text-white/85">
          <li>It assumes the difference actually gets invested, every month, for thirty years,
              without being spent. Measured behaviour says most people do not do this, and a
              strategy that only works with perfect discipline should be priced accordingly.</li>
          <li>It compares an expected return with a guarantee as though they were the same kind of
              number. They are not, and how much you should pay for a guarantee is a preference,
              not an arithmetic error.</li>
          <li>Term ends. If the need does not, the comparison quietly assumes you will be insurable
              later, which is exactly what nobody can promise.</li>
          <li>It ignores the cases where permanence is the point: a lifelong dependant, a business
              agreement, an estate that needs liquidity whenever it settles.</li>
        </ul>
      </div>
    </div>

    <p class="reveal mt-10 max-w-3xl text-white/85">
      Our practical position: insure the temporary need with term first, because it is cheap and
      the exposure is real, and consider a permanent policy for a permanent need afterwards, sized
      to what you can carry for life. If you want the comparison worked through with costs over
      thirty years, that is on
      <a class="link !text-white" href="/compare/term-vs-whole-life-insurance/">term life against
      whole life</a>.
    </p>
  </div>
</section>


<!-- =====================================================================
     THE SOFT CTA. One ask, no amber, no form. Spec: hard selling this
     reader loses them.
     ================================================================== -->
<section class="section-tight">
  <div class="container-ax">
    <div class="reveal card measure">
      <h2 class="text-h4">See an illustration for your own age</h2>
      <p class="mt-3 text-slate">
        The only way to answer any of this for your circumstances is a real illustration from a
        named carrier, with the guaranteed column shown separately. We will send you one whether or
        not you intend to buy anything, and we will point out the crossover year without being
        asked.
      </p>
      <div class="mt-5 flex flex-wrap items-center gap-4">
        <a class="btn btn-ghost" href="/whole-life-insurance/quotes/">Request a policy illustration</a>
        {C.phone_link("whole_cash_value_soft", "link-static inline-flex items-center gap-2 text-sm",
                      "or call " + C.PHONE_DISPLAY, 18)}
      </div>
    </div>
  </div>
</section>


{C.spoke_module(
    "Related pages in whole life",
    "Cash value is one part of the contract. These cover the rest of it.",
    [("/whole-life-insurance/what-is-whole-life-insurance/", "What whole life insurance is",
      "The definition, the mechanics, and where the premium goes."),
     ("/whole-life-insurance/rates/", "Whole life rates",
      "Premium by age and coverage, from current rate cards."),
     ("/whole-life-insurance/calculator/", "Whole life calculator",
      "Size the permanent need, with the method shown."),
     ("/whole-life-insurance/for-seniors/", "Whole life for seniors",
      "What cash value realistically does when bought after 65."),
     ("/whole-life-insurance/is-it-worth-it/", "Is whole life worth it?",
      "The case for and against, side by side."),
     ("/whole-life-insurance/guaranteed-acceptance/", "Guaranteed acceptance",
      "No health questions, and what it costs in cash value.")])}


{C.faq_section("Questions about whole life cash value", FAQ, "whole-cash-faq")}


{C.byline_section()}
"""
