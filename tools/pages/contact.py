# -*- coding: utf-8 -*-
"""CONTACT. Spec P0. Split layout: the phone on the left, the form on the right.

Neither side is the loser here. Someone who wants to talk should not have to
scroll past a form, and someone who would rather write should not have to hunt.
"""
from icons import icon
import chrome as C
import forms as F

PATH = "/contact/"
OUT = "contact/index.html"
ACTIVE = PATH
SILO = "contact"
TITLE = "Contact Apex Insurance Marketing | Talk to a Licensed Agent"
OG_TITLE = "Talk to a licensed independent life insurance agent"
DESC = ("Call or message a licensed independent life insurance agent about term life, whole life, "
        "or final expense coverage. Free, no obligation.")

ERR = icon("circle-alert", 16, "shrink-0 mt-px")


def schema():
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("Contact", None)])]


def body():
    # One h1, one line, one button. Calling is the fastest route, so the button
    # is the phone; the form is the section under the strip.
    hero = C.page_hero(
        [("Home", "/"), ("Contact", None)],
        "Talk to a licensed agent.",
        "Call us or send a message. Either way you reach a real licensed agent.",
        extra='''<div class="reveal mt-8">
        %s
        <p class="mt-3 text-micro text-muted">%s</p>
      </div>''' % (C.phone_link("contact_hero", "btn btn-call", "Call " + C.PHONE_DISPLAY), C.HOURS),
        banner="contact-banner")
    usps = C.usp_strip([
        ("user-check", "Licensed agents", "Real people, not a chatbot"),
        ("clock", "Reply within " + C.SLA, "From a real person"),
        ("shield-check", "Never sold on", "Your details stay with us"),
        ("handshake", "Free, no obligation", "You never pay us a fee"),
    ])

    fields = (
        F.row(F.text_field("ct-name", "name", "Your name", autocomplete="name", validate="name",
                           error="Please tell us your name."),
              F.phone_field("ct-phone", label="Phone"))
        + F.row(F.text_field("ct-email", "email", "Email", type="email", autocomplete="email",
                             validate="email", error="Enter a valid email address."),
                F.select_field("ct-interest", "interest", "What is it about?",
                               [("", "Choose one"), ("term-life", "Term life insurance"),
                                ("whole-life", "Whole life insurance"),
                                ("final-expense", "Final expense insurance"),
                                ("not-sure", "I am not sure which I need"),
                                ("existing-policy", "A policy I already have"),
                                ("other", "Something else")],
                               error="Pick the closest one. We can change it on the call."))
        + F.textarea_field("ct-message", "message", "Anything else?",
                           hint="Optional. A health condition, a deadline, a quote from elsewhere."))

    return f"""
{hero}
{usps}

<section id="message" class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">

      <!-- LEFT: phone first, then what actually happens on the call. -->
      <div class="lg:col-span-5">
       <div class="sticky-col">

        <div class="reveal card">
          <h2 class="text-h3 !font-display !font-semibold">Call us</h2>
          <div class="mt-5">
            {C.phone_link("contact_primary", "btn btn-call btn-block !min-h-[64px] !text-lead", C.PHONE_DISPLAY, 24)}
          </div>
          <p class="mt-4 text-sm text-slate">{C.HOURS}</p>
          <p class="mt-1 text-sm text-muted">
            Outside those hours, leave a message or use the form and we will call you back.
          </p>
        </div>

        <div class="reveal mt-8">
          <h2 class="text-h3 !font-display !font-semibold">What to expect on the call</h2>
          <ul class="mt-6 grid gap-5">
            <li class="flex items-start gap-3">
              {icon("clock", 22, "shrink-0 text-navy mt-1")}
              <div>
                <p class="font-semibold text-navy">Ten to twenty minutes</p>
                <p class="mt-1 text-slate">Shorter if you already know what you want.</p>
              </div>
            </li>
            <li class="flex items-start gap-3">
              {icon("list-checks", 22, "shrink-0 text-navy mt-1")}
              <div>
                <p class="font-semibold text-navy">Questions, then options</p>
                <p class="mt-1 text-slate">Age, state, health, and what you want to cover. No Social Security number, no credit check.</p>
              </div>
            </li>
            <li class="flex items-start gap-3">
              {icon("handshake", 22, "shrink-0 text-navy mt-1")}
              <div>
                <p class="font-semibold text-navy">No pressure to decide on the call</p>
                <p class="mt-1 text-slate">If you do not need it, we will say so.</p>
              </div>
            </li>
          </ul>
        </div>

       </div>
      </div>

      <!-- RIGHT: the form. -->
      <div class="lg:col-span-6 lg:col-start-7">
        <div class="panel reveal">
          <h2 class="text-h3 !font-display !font-semibold">Send us a message</h2>
          <p class="mt-2 text-sm text-muted">
            A licensed agent reads every one of these. We reply within {C.SLA}.
          </p>

          <form class="mt-6" data-ax-form data-silo="contact"
                data-form-name="contact_general" data-success-target="contact-success" novalidate>

            {F.scaffold(indent=12)}

            {fields}

            {F.consent_block("ct", C.BRAND, 12)}

            {F.submit_block("Send message")}
          </form>

          <!-- Designed success state, rendered in place. Never a browser dialog.
               In production this may instead redirect to /thank-you/, which is
               stubbed and noindexed. -->
          <div id="contact-success" class="success">
            <div class="flex items-start gap-3">
              {icon("circle-check", 32, "shrink-0 text-green")}
              <div>
                <h3 class="text-h3 !font-display !font-semibold">Message received</h3>
                <p class="mt-3 text-slate">
                  A licensed agent will read it and get back to you within {C.SLA}. If it is
                  urgent, calling is faster.
                </p>
                <div class="mt-5 flex flex-wrap items-center gap-5">
                  {C.phone_link("contact_success", "btn btn-call", "Call " + C.PHONE_DISPLAY)}
                  <a class="link text-sm" href="/thank-you/">What happens next</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Licence disclosure as a full-width strip. It was the bottom card of a
     column before, which both buried it and unbalanced the hero. -->
<section class="section-tight border-y border-rule bg-surface">
  <div class="container-ax">
    <div class="reveal grid lg:grid-cols-12 gap-8 lg:gap-10 items-start">
      <div class="lg:col-span-5 flex items-start gap-3">
        {icon("shield-check", 26, "shrink-0 text-navy mt-1")}
        <h2 class="text-h3 !font-display !font-semibold">Licensed, and independent of every carrier</h2>
      </div>
      <div class="lg:col-span-7">
        <p class="text-slate">
          {C.BRAND} is a licensed independent insurance agency, licensed in {C.STATES} states,
          National Producer Number {C.NPN}. We are appointed with multiple carriers and we are not
          owned by any of them, which is what lets us take your application somewhere else when the
          first carrier prices your health history badly.
        </p>
        <a class="link-static mt-4 inline-block text-sm" href="/about/licensing/">See our licensing by state</a>
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     WHAT HAPPENS NEXT.
     ================================================================== -->
{C.steps_section("What happens next",
    "Three things, in this order.",
    [("mail", None, "You send it",
      "Your message goes to our agency inbox. It is not sold, shared, or passed to a lead broker."),
     ("user-check", None, "A licensed agent reads it",
      "A person, with a licence number, who can actually place the policy. Not a receptionist "
      "taking a message."),
     # [SET HONEST SLA] Replace with the response time the agency can actually
     # hold to, including on a Friday afternoon.
     ("phone", None, "We contact you",
      "Within " + C.SLA + ", by whichever of phone or email you seem to prefer. If we are going "
      "to be slower than that, we will tell you rather than let it drift.")],
    cls="section-tight band")}

<!-- =====================================================================
     MINI FAQ.
     ================================================================== -->
<section class="section-tight">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">
      <div class="lg:col-span-4">
        <h2 class="reveal text-h2">Before you get in touch</h2>
        <p class="reveal mt-5 text-slate">The three things people ask us first.</p>
        <p class="reveal mt-6 text-sm text-muted">Anything else is quicker to ask out loud.</p>
        <div class="reveal mt-4">{C.phone_link("contact_faq", "btn btn-ghost", "Call " + C.PHONE_DISPLAY)}</div>
      </div>
      <div class="lg:col-span-7 lg:col-start-6 reveal">
        <details class="acc" name="contact-faq">
          <summary>Is this free?<span class="acc-icon">{icon("plus", 22)}</span></summary>
          <div class="acc-body"><p class="text-slate">
            Yes. Quotes, comparisons, and the conversation cost you nothing. If you buy a policy,
            the carrier pays us a commission out of the premium you would have paid anyway, because
            life insurance rates are filed with state regulators and are the same wherever you buy.
            You never pay Apex a fee.
          </p></div>
        </details>
        <details class="acc" name="contact-faq">
          <summary>Am I obligated to buy anything?<span class="acc-icon">{icon("plus", 22)}</span></summary>
          <div class="acc-body"><p class="text-slate">
            No. Asking for a quote commits you to nothing, and neither does completing an
            application. Nothing is owed and no coverage exists until a policy is issued, delivered,
            and the first premium is paid. You can stop at any point without explaining why.
          </p></div>
        </details>
        <details class="acc" name="contact-faq">
          <summary>Who will contact me?<span class="acc-icon">{icon("plus", 22)}</span></summary>
          <div class="acc-body"><p class="text-slate">
            A licensed agent from {C.BRAND}, and nobody else. We do not sell, rent, or share your
            details with other agencies, lead buyers, or marketing partners. You will not start
            getting calls from numbers you do not recognise, which is what happens on comparison
            sites that sell the same enquiry to several agencies at once.
          </p></div>
        </details>
      </div>
    </div>
  </div>
</section>
"""
