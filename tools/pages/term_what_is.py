# -*- coding: utf-8 -*-
"""WHAT IS TERM LIFE INSURANCE. Spec P2, template T4. Soft single CTA.

The definitional page for the term silo. It absorbs "how does term life
insurance work" and "term life insurance definition" as H2 sections rather
than spawning two more pages that would compete with this one.

Two structural decisions worth keeping:

  * The answer is the first two sentences, before any section. Someone who
    lands here from a definition query has one question, and making them
    scroll past a hero to reach it is why so many of these pages lose.
  * The "what it does not do" section is the same size as the "what it does"
    section. A definition page that only sells is not a definition page.

Cross silo movement is via /compare/ only (spec s07 rule 3), so the single
outbound link to whole life goes to the comparison page, not to that hub.
"""
import chrome as C

PATH = "/term-life-insurance/what-is-term-life-insurance/"
OUT = "term-life-insurance/what-is-term-life-insurance/index.html"
ACTIVE = "/term-life-insurance/"
SILO = "term-life"
TITLE = "What Is Term Life Insurance? A Plain-English Guide | Apex"
OG_TITLE = "What is term life insurance?"
DESC = ("Term life insurance pays a fixed benefit if you die within a set number of years. What it "
        "covers, what happens when the term ends, and where it stops being the right tool.")

TRAIL = [("Home", "/"), ("Term Life Insurance", "/term-life-insurance/"),
         ("What is term life insurance", None)]

FAQ = [
    ("What is term life insurance in simple terms?",
     "It is a contract with an insurance company that runs for a fixed number of years. You pay a "
     "premium every month or every year. If you die during those years, the company pays the "
     "people you named a lump sum, income tax free in almost every case. If you are still alive "
     "when the years run out, the contract ends and nobody gets anything. That last sentence is "
     "the part that makes it cheap."),
    ("How does term life insurance work if I die?",
     "Your beneficiary contacts the carrier and files a claim with a certified copy of the death "
     "certificate. The carrier verifies the policy was in force and that the application was "
     "answered truthfully, then pays the face amount as a lump sum, usually within a few weeks. "
     "Deaths in the first two policy years fall inside the contestability period, which means the "
     "carrier can review the original application before paying. Nothing about that is unusual, "
     "and an accurate application is what makes it a formality."),
    ("What happens when a term life policy expires?",
     "Coverage stops. Most policies then let you renew year by year at a sharply higher price "
     "that climbs every year, which is a bridge rather than a plan. The more useful right is "
     "conversion: turning some or all of the coverage into a permanent policy without answering "
     "any new health questions. Conversion rights have deadlines, and they are the single most "
     "overlooked feature in the contract."),
    ("Do I get my money back at the end of a term policy?",
     "No, not with a standard term policy, and that is the trade. You are buying a defined "
     "outcome for a defined window at the lowest price the market offers. There is a product "
     "called return of premium term that refunds the premiums if you outlive the term, and it "
     "costs considerably more for the same death benefit. We will price it if you ask, and we "
     "will also show you what the difference buys elsewhere."),
    ("Is term life insurance worth it if I never claim?",
     "Most term policies never pay a claim, which is exactly what you should want to happen. You "
     "are not buying an investment, you are buying the removal of one specific risk from your "
     "household for a period when other people depend on your income. Judged that way, an unused "
     "policy is a policy that did its job."),
]

GLOSSARY = [
    ("Face amount", "The lump sum the carrier pays if you die during the term. Also called the "
                    "death benefit or the coverage amount."),
    ("Term length", "How many years the price and the coverage are locked. Ten, fifteen, twenty, "
                    "and thirty years are the standard set."),
    ("Level premium", "The premium does not change for the whole term. Nearly every modern term "
                      "policy is level, which is why the phrase level term exists."),
    ("Beneficiary", "The person or people who receive the money. Named on the policy, not in your "
                    "will, and payable directly to them."),
    ("Rider", "An optional add on, such as a waiver of premium if you become disabled, or a child "
              "rider. Some cost extra, some are included."),
    ("Conversion right", "The right to swap term coverage for a permanent policy with no new "
                         "medical questions, up to a deadline written in the contract."),
]


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    glossary_rows = "\n            ".join(
        '<tr><th scope="row">%s</th><td>%s</td></tr>' % (t, d) for t, d in GLOSSARY)

    return f"""
{C.page_hero(
    TRAIL,
    "What Is Term Life Insurance?",
    'Term life insurance pays a fixed, tax free lump sum to the people you name if you die within '
    'a set number of years. You choose the number of years and the amount, the price is locked for '
    'the whole period, and when the period ends the coverage ends with it. That last part is the '
    'trade, and it is why '
    '<a class="link" href="/term-life-insurance/">term life insurance</a> costs a fraction of '
    'anything permanent.')}


<!-- =====================================================================
     THE MECHANICS. Absorbs the "how does term life insurance work"
     intent as an H2 rather than a separate competing page.
     ================================================================== -->
{C.prose(
    "How a term policy actually works",
    C.step(1, "You choose an amount and a number of years",
           "Usually enough to clear the mortgage and replace your income for as long as somebody "
           "would need it, over a period that matches the obligation. A thirty year mortgage taken "
           "out last year and a fourteen year old at home are two different answers.")
    + '<div class="mt-8">' + C.step(2, "The carrier underwrites you",
           "Health questions, a prescription and medical records check, often a short paramedical "
           "exam at your home. The result is a rate class, and the rate class sets the price.")
    + '</div><div class="mt-8">' + C.step(3, "The premium locks",
           "From the day the policy is issued, that number does not move for the whole term. Not "
           "if you are diagnosed with something, not if you change jobs, not if rates rise.")
    + '</div><div class="mt-8">' + C.step(4, "One of two things happens",
           "Either you die during the term and the carrier pays your beneficiaries a lump sum, or "
           "you outlive the term and the coverage ends. There is no third outcome and no cash "
           "value building up in the background.",
           "You can stop paying at any time. There is no surrender charge, because there is "
           "nothing to surrender.")
    + '</div>',
    intro="Four moves, in order. Nothing else happens in between, which is the appeal.")}


<!-- =====================================================================
     GLOSSARY. A table, because this is the section people scan rather
     than read, and a table is this design system's signature object.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">The words on a term policy, defined</h2>
      <p class="reveal mt-5 text-slate">
        Six terms cover almost everything you will see on an illustration or an application. If an
        agent uses a word that is not on this list and does not stop to define it, ask.
      </p>
    </div>

    <div class="reveal mt-10 table-scroll table-signature">
      <table class="rate-table" style="min-width:34rem">
        <caption>Standard term life vocabulary and what each word does.</caption>
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
  </div>
</section>


<!-- =====================================================================
     WHAT IT DOES. Three cells, one tinted, one blue: MASTER.md s3
     requires visual variation in every bento.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">What the money is actually for</h2>
      <p class="reveal mt-5 text-slate">
        A death benefit is not a windfall. It is a substitute for a specific stream of money that
        stops when you do, and sizing it is a subtraction problem rather than a guess.
      </p>
    </div>

    <div class="mt-10 bento" data-stagger="40">
      <div class="reveal bento-cell bento-cell-blue bento-2">
        <p class="eyebrow text-white/80">The mortgage</p>
        <p class="mt-3 text-white/90">
          The largest single item for most households, and the one with a fixed end date you can
          look up. Matching the term to the years remaining is the cleanest decision on the page.
        </p>
      </div>
      <div class="reveal bento-cell bento-2">
        <p class="eyebrow">The income</p>
        <p class="mt-3 text-slate">
          What your household would have to replace, for as many years as it would need replacing.
          Not forever: until the youngest child is independent, or until a pension starts.
        </p>
      </div>
      <div class="reveal bento-cell bento-cell-tint bento-2">
        <p class="eyebrow">The bills that arrive anyway</p>
        <p class="mt-3 text-slate">
          Funeral costs, outstanding debts, and several months of ordinary expenses while an estate
          is sorted out. Small next to the other two, and the first thing a family runs into.
        </p>
      </div>
    </div>

    <p class="reveal mt-8 text-slate max-w-3xl">
      Our <a class="link" href="/term-life-insurance/calculator/">coverage calculator</a> does that
      subtraction with the method shown on screen, so you can see how the figure was reached rather
      than being handed one.
    </p>
  </div>
</section>


{C.inline_cta(
    "See what this costs for your age",
    "Six questions, about two minutes, and a licensed agent comes back with premiums from named "
    "carriers rather than a range. No obligation, and no cost either way.",
    "term_what_is_mid", "/term-life-insurance/quotes/", "Get term life quotes")}


<!-- =====================================================================
     THE END OF THE TERM. The fine print people meet fifteen years
     later, put where they can meet it now instead.
     ================================================================== -->
{C.prose(
    "What happens when the term runs out",
    C.qa("You can let it end",
         "If the mortgage is paid, the children are grown, and your partner would be fine on their "
         "own, this is the correct outcome and not a loss. Stop paying and the policy lapses.")
    + C.qa("You can renew, expensively",
           "Almost every term policy is annually renewable after the level period, with no new "
           "health questions. The price resets to your current age and then climbs every single "
           "year. Treat it as a bridge of months, not a plan for years.", "mt-8")
    + C.qa("You can convert, and this is the valuable one",
           "Conversion turns some or all of the term coverage into a permanent policy with no new "
           "medical questions, at your original health class. If your health has changed, this "
           "right is worth more than the policy. It expires, often at a fixed age or after a set "
           "number of policy years, and carriers differ enormously on which permanent products "
           "they will convert into.", "mt-8")
    + C.qa("You can buy a new term policy",
           "Possible, and priced at your new age and new health. Worth comparing against "
           "conversion rather than assuming either one wins.", "mt-8"),
    intro="Three options and a default, and the default is the one most people take without "
          "deciding to.",
    aside='<p class="text-slate">Conversion deadlines are why we ask about them before you '
          'buy, not after. Two policies at the same premium can carry very different conversion '
          'rights, and the difference is invisible on a price comparison.</p>',
    cls="section band-surface")}


<!-- =====================================================================
     THE HONEST LIMITS. Same weight as the section above it.
     Carries the single sanctioned cross-silo link, to /compare/.
     ================================================================== -->
<section class="section band-navy on-navy">
  <div class="container-ax">
    <div class="max-w-3xl">
      <h2 class="reveal text-h2 text-white">Where term life stops being the right tool</h2>
      <p class="reveal mt-5 text-white/85">
        Term is the correct answer for most people buying life insurance for the first time. It is
        not the correct answer for all of them, and an agency that never says so is selling rather
        than advising.
      </p>
    </div>

    <div class="mt-10 grid md:grid-cols-3 gap-6 lg:gap-8 max-w-5xl" data-stagger="60">
      <div class="reveal">
        <h3 class="text-h4 text-white">When the need has no end date</h3>
        <p class="mt-3 text-white/85">
          A dependant with a lifelong disability, a business buy sell agreement, or an estate that
          will owe tax whenever it settles. A twenty year answer does not fit a permanent question.
        </p>
      </div>
      <div class="reveal">
        <h3 class="text-h4 text-white">When you are already past the issue ages</h3>
        <p class="mt-3 text-white/85">
          Most carriers stop writing new term above the mid seventies, and the price well before
          that stops being defensible for a small face amount.
        </p>
      </div>
      <div class="reveal">
        <h3 class="text-h4 text-white">When the amount is small and the purpose is a funeral</h3>
        <p class="mt-3 text-white/85">
          Term is built for six and seven figure obligations. A policy meant to bury someone is a
          different product with different underwriting.
        </p>
      </div>
    </div>

    <p class="reveal mt-10 max-w-3xl text-white/85">
      If a permanent policy might be the better fit, the honest way to decide is side by side:
      <a class="link !text-white" href="/compare/term-vs-whole-life-insurance/">compare term life
      and whole life insurance</a>, including what each one costs over thirty years.
    </p>
  </div>
</section>


{C.spoke_module(
    "Keep reading in this section",
    "Everything below is term life. Each page assumes you have read this one.",
    [("/term-life-insurance/rates/", "Rates by age",
      "The full pricing grid, and the six things that move it."),
     ("/term-life-insurance/level-term/", "Level term explained",
      "What stays level, for how long, and what happens after."),
     ("/term-life-insurance/20-year-term/", "20 year term",
      "The default choice, and how to check it against your dates."),
     ("/term-life-insurance/30-year-term/", "30 year term",
      "Long mortgages, young children, and what the extra decade costs."),
     ("/term-life-insurance/no-medical-exam/", "No medical exam term",
      "Same day approvals, and the trade you make for them."),
     ("/term-life-insurance/for-seniors/", "Term life after 60",
      "What is still available, and when to stop looking at term.")])}


{C.faq_section("Common questions about term life insurance", FAQ, "term-what-is-faq")}


{C.byline_section()}
"""
