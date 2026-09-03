# -*- coding: utf-8 -*-
"""FINAL EXPENSE FOR PARENTS. Spec P3, template T4. FORM WEIGHTED.

The one CTA exception in this silo, and the only page in it that does not set
HTML_CLASS = "fe". Both follow from the same fact: the buyer is the adult child,
typically 30 to 55, not the insured. Spec s05 says standard type sizes are fine
here. The calm register is not, and is kept.

The distinct objections this page has to answer are not the silo's usual ones.
They are legal and relational rather than product ones:

  CONSENT      You cannot insure a parent without their knowledge. There is no
               version of this where you quietly arrange it. Said in the hero.
  OWNERSHIP    Who owns the policy, who is the beneficiary, and why those are
               deliberately two different questions.
  WHO PAYS     The premium can come from you, and what happens to the policy if
               you stop paying it.

The form is FE.callback_form() with its own prefix and form_name, so the GA4
form_submit event distinguishes this page from the hub. It sits beside a phone
CTA rather than replacing it: form weighted means the form gets the amber and
the panel, not that the phone disappears.
"""
import chrome as C
import final_expense as FE

PATH = "/final-expense-insurance/for-parents/"
OUT = "final-expense-insurance/for-parents/index.html"
ACTIVE = "/final-expense-insurance/"
SILO = "final-expense"
TITLE = "Final Expense Insurance for Parents: Buying for Mom or Dad | Apex"
OG_TITLE = "Buying final expense insurance for a parent"
DESC = ("How to buy a final expense policy for your mother or father: the consent they have to "
        "give, who should own it, who pays the premium, and how to raise it without a row.")

TRAIL = [("Home", "/"), ("Final Expense Insurance", "/final-expense-insurance/"),
         ("Buying for a parent", None)]

RULES = [
    ("Consent", "Your parent has to know, and has to sign",
     "There is no lawful way to insure someone without their knowledge. Your parent signs the "
     "application, answers the health questions themselves, and in most cases speaks to the "
     "carrier or the agent directly. If anyone offers to arrange this without their involvement, "
     "end the conversation: that is fraud, and the policy would not pay."),
    ("Insurable interest", "You are allowed to do this, and here is why",
     "A carrier will only issue a policy where the owner would suffer a genuine loss from the "
     "death. A child paying for a parent's funeral qualifies without difficulty. It is one of the "
     "clearest cases there is, and it is not the part of this that will be questioned."),
    ("Ownership and beneficiary", "Two separate decisions, and they should be",
     "The owner controls the policy and pays for it. The beneficiary receives the money. If you "
     "are paying, being the owner protects you from the policy lapsing without your knowledge, and "
     "being the beneficiary means the funds reach the person who will be paying the funeral "
     "director."),
]

STEPS = [
    ("Have the conversation before you get a quote",
     "Not after. The health questions have to be answered by your parent, and a quote based on "
     "your guesses about their medication is not a quote. Starting with the conversation also "
     "avoids the situation where you have done work you then have to undo."),
    ("Agree who owns it and who is the beneficiary",
     "If you are paying the premium, it is usually cleanest for you to be the owner and the "
     "beneficiary, with a clear understanding of what the money is for. If there are several "
     "siblings, decide now which of you it is, and tell the others. This is the decision that "
     "causes arguments later, and it takes ten minutes to settle in advance."),
    ("Get your parent's medication list in front of you",
     "Not the conditions, the medications, with doses. Carriers underwrite final expense largely "
     "from the prescription history, and the difference between a level benefit policy and a "
     "graded one frequently turns on a single drug. Guessing at this wastes an application."),
    ("Apply to the carrier that treats their health best",
     "This is the part an independent agency is actually for. Carriers disagree with each other, "
     "sometimes sharply, about the same condition. The useful question is never whether your "
     "parent qualifies but which carrier they qualify best with, and that is not something you "
     "can determine from any website, ours included."),
]

CONVERSATION = [
    ("Lead with the practical, not the mortal",
     "&quot;I want to make sure I am not making decisions about money in the week after you die&quot; "
     "lands very differently from &quot;have you thought about what happens when you go&quot;. Most "
     "parents are considerably less squeamish about this than their children expect, and are "
     "frequently relieved that somebody has raised it."),
    ("Be specific about what it is and what it costs",
     "A small policy, a fixed premium that never rises, no medical exam, a short list of health "
     "questions, and it exists so the funeral is not paid for out of somebody's savings. Vagueness "
     "reads as a sales pitch even when it is coming from your own child."),
    ("Say clearly who is paying",
     "If you are paying, say so at the start. A great many of these conversations stall because "
     "the parent assumes they are being asked to take on a new bill on a fixed income, and nobody "
     "corrected the assumption."),
    ("Let them say no, and leave it open",
     "Some parents will decline, and a policy taken out over somebody's objection is a policy "
     "somebody resents. It is a reasonable thing to raise again in six months. It is not a "
     "reasonable thing to push through in one call."),
]

FAQ = [
    ("Can I buy life insurance for my parent?",
     "Yes, and it is common. You need two things: your parent's knowledge and signature, and an "
     "insurable interest, which as their child paying for a funeral you plainly have. What you "
     "cannot do is arrange it without them. They sign the application, they answer the health "
     "questions, and in most cases they speak to the agent or the carrier directly."),
    ("Can I buy life insurance for my parent without them knowing?",
     "No. Not through us, and not lawfully through anyone. An application requires the insured "
     "person's signature and their own answers to the health questions, and a policy obtained "
     "without them would be void, which means it would not pay at the point it was needed. Anyone "
     "who tells you otherwise is proposing insurance fraud."),
    ("Who should own the policy, me or my parent?",
     "If you are paying the premium, usually you. As owner you receive the notices, so the policy "
     "cannot lapse without your knowing, and you control the beneficiary designation. Your parent "
     "is still the insured and still has to consent to everything. If your parent is paying and "
     "wants control of it, they should own it. There is no single right answer, only a decision "
     "worth making deliberately rather than by default."),
    ("Who should be the beneficiary?",
     "Whoever is going to be handing money to the funeral director. If that is you, name yourself. "
     "Naming the estate instead is the common mistake: it can delay the funds through probate for "
     "months, which defeats the point of buying the policy. If there are several siblings sharing "
     "the cost, name one of you and agree in writing what happens to any remainder."),
    ("What happens if I stop paying the premium?",
     "The policy lapses after a grace period, usually about thirty days, and the coverage ends. On "
     "a policy that has been in force a while there may be a small cash value that can keep it "
     "going briefly, but you should not rely on that. If you are the owner, the notices come to "
     "you, which is the main practical reason for you to be the owner. If your circumstances "
     "change, call the carrier before it lapses: reducing the coverage is almost always available "
     "and is far better than losing it."),
    ("Can my parent still get coverage with health problems?",
     "Usually. Final expense underwriting is a short list of health questions and a prescription "
     "check rather than a medical exam, and most applicants are approved. Carriers disagree with "
     "each other about the same conditions, so a decline from one is not a decline from all. If no "
     "carrier will write a standard policy, guaranteed acceptance coverage with a waiting period "
     "is normally still available, and we will tell you plainly which of the two you are looking "
     "at rather than let you find out at claim time."),
]

SIBLINGS = [
    ("/final-expense-insurance/what-is-final-expense-insurance/", "What it is",
     "The plain definition, worth reading before the conversation."),
    ("/final-expense-insurance/funeral-insurance/", "Funeral insurance",
     "The same product under another name, and what it covers."),
    ("/final-expense-insurance/no-waiting-period/", "No waiting period",
     "Which policies pay from day one, and what decides it."),
    ("/final-expense-insurance/for-seniors/", "For seniors",
     "What is available at 60, at 70, and at 80."),
    ("/final-expense-insurance/burial-insurance/", "Burial insurance",
     "The same product under the name most people search for."),
    ("/final-expense-insurance/cremation-insurance/", "Cremation insurance",
     "Sizing it for a cremation, which costs less."),
]


def schema():
    return [C.org_schema(), C.breadcrumbs(TRAIL), C.faq_schema(FAQ), C.person_schema(PATH)]


def body():
    rules = ""
    for i, (eyebrow, title, text) in enumerate(RULES):
        variant = ["bento-cell-blue", "", "bento-cell-tint"][i]
        navy = i == 0
        rules += f"""
      <div class="reveal bento-cell {variant} bento-2">
        <p class="eyebrow{' text-white/80' if navy else ''}">{eyebrow}</p>
        <h3 class="mt-2 text-h4{' text-white' if navy else ''}">{title}</h3>
        <p class="mt-3 {'text-white/90' if navy else 'text-slate'}">{text}</p>
      </div>"""

    steps = "".join(
        (('<div class="mt-8">%s</div>' if i else "%s") % C.step(i + 1, t, b))
        for i, (t, b) in enumerate(STEPS))

    conversation = "".join(
        C.qa(h, b, "" if i == 0 else "mt-8") for i, (h, b) in enumerate(CONVERSATION))

    return f"""
{C.page_hero(
    TRAIL,
    "Final Expense Insurance for Parents",
    'You can buy a <a class="link" href="/final-expense-insurance/">final expense insurance</a> '
    'policy on your mother or father, and a great many people do. One thing is not negotiable: '
    'your parent has to know about it and sign the application themselves, because a policy taken '
    'out without them is void and would not pay. Beyond that, the decisions are who owns it, who '
    'receives the money, and who pays the premium, and this page is about getting all three right '
    'before you apply.')}


<!-- =====================================================================
     THE FORM. The one CTA exception in this silo (spec s09): the buyer
     here is the adult child, typically 30 to 55, so the form takes the
     amber and the panel. The phone stays beside it rather than being
     dropped, because a decision about a parent's health frequently
     produces a question a form cannot take.
     ================================================================== -->
<section class="section-tight">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-8 lg:gap-10 items-start">
      <div class="lg:col-span-6">
        <div class="reveal panel">
          {FE.callback_form(
              "fe-parents", "fe_for_parents_callback",
              heading="Ask us what it would cost for your parent",
              intro="Leave four details and a licensed agent will call you. We will talk you "
                    "through the health questions, tell you which carriers treat your parent's "
                    "situation best, and say plainly if a waiting period is likely.")}
        </div>
      </div>
      <div class="lg:col-span-5 lg:col-start-8">
        <h2 class="reveal text-h3 !font-display !font-semibold">Or call and ask first</h2>
        <p class="reveal mt-3 text-slate">
          Plenty of people call before they have spoken to their parent, to find out what they
          would be proposing. That is a sensible order to do it in, and there is nothing to sign.
        </p>
        <div class="reveal mt-6">
          {C.phone_link("fe_parents_hero", "btn btn-call btn-block",
                        "Call " + C.PHONE_DISPLAY, 22)}
          <p class="mt-3 text-micro text-muted">{C.HOURS}</p>
        </div>
        <div class="reveal mt-8 card">
          <h3 class="text-h4">Have this ready if you can</h3>
          <ul class="mt-4 grid gap-3">
            <li class="flex items-start gap-3">{C.icon("check", 20, "shrink-0 mt-1 text-green")}
              <span class="text-slate">Your parent's age and the state they live in.</span></li>
            <li class="flex items-start gap-3">{C.icon("check", 20, "shrink-0 mt-1 text-green")}
              <span class="text-slate">Their medication list, with doses if you have it.</span></li>
            <li class="flex items-start gap-3">{C.icon("check", 20, "shrink-0 mt-1 text-green")}
              <span class="text-slate">Roughly what a funeral costs where they live.</span></li>
            <li class="flex items-start gap-3">{C.icon("check", 20, "shrink-0 mt-1 text-green")}
              <span class="text-slate">Whether you or they will be paying the premium.</span></li>
          </ul>
          <p class="mt-4 text-micro text-muted">
            None of it is required to have a first conversation. It just makes the answers real
            rather than approximate.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>


<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">The three rules that govern this</h2>
      <p class="reveal mt-5 text-slate">
        Insuring another adult is more constrained than insuring yourself, and for good reasons.
        None of the constraints is difficult, but the first one is absolute.
      </p>
    </div>
    <div class="mt-10 bento" data-stagger="40">{rules}
    </div>
  </div>
</section>


{C.prose("How to actually do it", steps,
         intro="Four steps, in this order. Doing them out of order is what produces a wasted "
               "application or an awkward second conversation.")}


{C.prose("How to raise it without a row", conversation,
         intro="This is the part people find hard, and it is worth more than any product detail "
               "on this page. The conversation usually goes better than the version of it you are "
               "dreading.",
         cls="section band")}


<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">If several of you are sharing the cost</h2>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <p class="reveal text-slate">
          One policy with one owner is almost always simpler than several small policies, one per
          sibling. Pick the sibling who will be dealing with the funeral director, make them the
          owner and the beneficiary, and settle in writing between yourselves who contributes what
          and what happens to any money left over after the funeral is paid for.
        </p>
        <p class="reveal mt-5 text-slate">
          Write it down even though it feels excessive. The policy will probably pay out fifteen or
          twenty years from now, in a week when nobody is at their best, and a short note agreed
          while everyone is calm is worth a great deal then.
        </p>
        <p class="reveal mt-5 text-slate">
          Naming the estate as beneficiary instead, to be split automatically, is the tempting
          shortcut and it is usually a mistake: it can tie the money up in probate for months, and
          the funeral bill arrives in days. Premiums by age and coverage amount are on
          <a class="link" href="/final-expense-insurance/cost/">what final expense insurance
          costs</a>, and if you would rather start in writing than on a call, the
          <a class="link" href="/final-expense-insurance/quotes/">final expense quote page</a>
          takes the same details.
        </p>
      </div>
    </div>
  </div>
</section>


{C.spoke_module("Related pages in final expense",
                "Worth reading before the conversation, and before you apply.", SIBLINGS)}


{C.faq_section("Questions about insuring a parent", FAQ, "fe-parents-faq")}


{C.byline_section()}
"""
