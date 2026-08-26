# -*- coding: utf-8 -*-
"""CONTACT. Spec P0. Split layout: the phone on the left, the form on the right.

Neither side is the loser here. Someone who wants to talk should not have to
scroll past a form, and someone who would rather write should not have to hunt.
"""
from icons import icon
import chrome as C

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
    return f"""
<section class="pt-6 pb-14 md:pb-16">
  <div class="container-ax">
    {C.crumbs([("Home", "/"), ("Contact", None)])}

    <div class="mt-8 max-w-3xl">
      <h1 class="reveal text-h1">Contact Apex</h1>
      <p class="reveal mt-5 text-lead text-slate">
        You will reach a licensed agent. Not a call centre, not a lead form that gets sold on to
        six other agencies, and not a chatbot pretending to be a person.
      </p>
    </div>

    <div class="mt-12 grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">

      <!-- LEFT: phone first, then what actually happens on the call. -->
      <div class="lg:col-span-5">

        <div class="reveal card">
          <h2 class="text-h3 !font-display !font-bold">Call us</h2>
          <div class="mt-5">
            {C.phone_link("contact_primary", "btn btn-call btn-block !min-h-[64px] !text-lead", C.PHONE_DISPLAY, 24)}
          </div>
          <p class="mt-4 text-sm text-slate">{C.HOURS}</p>
          <p class="mt-1 text-sm text-muted">
            Outside those hours, leave a message or use the form and we will call you back.
          </p>
        </div>

        <div class="reveal mt-8">
          <h2 class="text-h3 !font-display !font-bold">What to expect on the call</h2>
          <ul class="mt-6 grid gap-5">
            <li class="flex items-start gap-3">
              {icon("clock", 22, "shrink-0 text-navy mt-1")}
              <div>
                <p class="font-semibold text-navy">Ten to twenty minutes</p>
                <p class="mt-1 text-slate">Longer if you want to work through the numbers, shorter if you already know what you want.</p>
              </div>
            </li>
            <li class="flex items-start gap-3">
              {icon("list-checks", 22, "shrink-0 text-navy mt-1")}
              <div>
                <p class="font-semibold text-navy">Questions, then options</p>
                <p class="mt-1 text-slate">Your age, state, health, and what you are trying to cover. No Social Security number and no credit check to get a quote.</p>
              </div>
            </li>
            <li class="flex items-start gap-3">
              {icon("handshake", 22, "shrink-0 text-navy mt-1")}
              <div>
                <p class="font-semibold text-navy">No pressure to decide on the call</p>
                <p class="mt-1 text-slate">If the honest answer is that you do not need what you called about, we will say so.</p>
              </div>
            </li>
          </ul>
        </div>

        <div class="reveal mt-8 card">
          <div class="flex items-start gap-3">
            {icon("shield-check", 24, "shrink-0 text-navy mt-0.5")}
            <div>
              <h2 class="text-h4">Licensed and independent</h2>
              <p class="mt-3 text-slate">
                {C.BRAND} is a licensed independent insurance agency, licensed in {C.STATES}
                states, National Producer Number {C.NPN}. We are appointed with multiple carriers
                and we are not owned by any of them.
              </p>
              <a class="link-static mt-4 inline-block text-sm" href="/about/licensing/">See our licensing by state</a>
            </div>
          </div>
        </div>
      </div>

      <!-- RIGHT: the form. -->
      <div class="lg:col-span-6 lg:col-start-7">
        <div class="panel reveal">
          <h2 class="text-h3 !font-display !font-bold">Send us a message</h2>
          <p class="mt-2 text-sm text-muted">
            A licensed agent reads every one of these. We reply within {C.SLA}.
          </p>

          <form class="mt-6" data-ax-form data-silo="contact"
                data-form-name="contact_general" data-success-target="contact-success" novalidate>

            <input type="hidden" name="source_url" value="">
            <input type="hidden" name="silo" value="">
            <input type="hidden" name="form_name" value="">
            <div aria-hidden="true" style="position:absolute;left:-9999px">
              <label>Company website<input type="text" name="company_website" tabindex="-1" autocomplete="off"></label>
            </div>

            <div class="field">
              <label class="field-label" for="ct-name">Your name</label>
              <input class="input" id="ct-name" name="name" type="text" autocomplete="name"
                     required data-validate="name" data-error="Please tell us your name.">
              <p class="field-error">{ERR}<span></span></p>
            </div>

            <div class="grid sm:grid-cols-2 gap-x-4">
              <div class="field">
                <label class="field-label" for="ct-email">Email</label>
                <input class="input" id="ct-email" name="email" type="email" autocomplete="email"
                       required data-validate="email" data-error="Enter a valid email address.">
                <p class="field-error">{ERR}<span></span></p>
              </div>
              <div class="field">
                <label class="field-label" for="ct-phone">Phone</label>
                <input class="input" id="ct-phone" name="phone" type="tel" autocomplete="tel"
                       required data-validate="phone" data-error="Enter a 10 digit phone number.">
                <p class="field-error">{ERR}<span></span></p>
              </div>
            </div>

            <div class="field">
              <label class="field-label" for="ct-interest">What are you interested in?</label>
              <select class="select" id="ct-interest" name="interest" required
                      data-error="Pick the closest one. We can change it on the call.">
                <option value="">Choose one</option>
                <option value="term-life">Term life insurance</option>
                <option value="whole-life">Whole life insurance</option>
                <option value="final-expense">Final expense insurance</option>
                <option value="not-sure">I am not sure which I need</option>
                <option value="existing-policy">A policy I already have</option>
                <option value="other">Something else</option>
              </select>
              <p class="field-error">{ERR}<span></span></p>
            </div>

            <div class="field">
              <label class="field-label" for="ct-message">Anything else?
                <span class="field-hint block font-normal">Optional. Health conditions, a deadline, a number you have been quoted elsewhere.</span>
              </label>
              <textarea class="input" id="ct-message" name="message" rows="4"></textarea>
              <p class="field-error">{ERR}<span></span></p>
            </div>

            <!-- TCPA consent. Separate, unchecked, immediately above submit.
                 [PENDING LEGAL REVIEW] Wording must be approved by counsel and
                 matched to current TCPA one-to-one consent rules before launch. -->
            <div class="consent">
              <input type="checkbox" id="ct-consent" name="tcpa_consent" value="yes" data-consent>
              <label class="consent-text" for="ct-consent">
                I agree that {C.BRAND} may call and text me at the number above about life
                insurance, including with an automatic telephone dialing system or a prerecorded
                voice. I understand this consent is not a condition of purchase and that message
                and data rates may apply.
              </label>
              <p class="field-error">{ERR}<span></span></p>
            </div>

            <button type="submit" class="btn btn-cta btn-block">Send message</button>
            <p class="field-error" data-form-error>{ERR}<span></span></p>
            <p class="mt-3 text-micro text-muted">
              Free &#183; No obligation &#183; Licensed agents &#183; We never sell your details on
            </p>
          </form>

          <!-- Designed success state, rendered in place. Never a browser dialog.
               In production this may instead redirect to /thank-you/, which is
               stubbed and noindexed. -->
          <div id="contact-success" class="success">
            <div class="flex items-start gap-3">
              {icon("circle-check", 32, "shrink-0 text-green")}
              <div>
                <h3 class="text-h3 !font-display !font-bold">Message received</h3>
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

<!-- =====================================================================
     WHAT HAPPENS NEXT.
     ================================================================== -->
<section class="section-tight band">
  <div class="container-ax">
    <h2 class="reveal text-h2">What happens next</h2>
    <div class="mt-10 grid md:grid-cols-3 gap-10 md:gap-8" data-stagger>
      <div class="reveal">
        <div class="flex items-baseline gap-3 pb-4 border-b border-navy">
          <span class="text-h3 !font-display !font-bold text-navy tnum">1</span>
          <h3 class="text-h4">You send it</h3>
        </div>
        <p class="mt-5 text-slate">
          Your message goes to our agency inbox. It is not sold, shared, or passed to a lead broker.
        </p>
      </div>
      <div class="reveal">
        <div class="flex items-baseline gap-3 pb-4 border-b border-navy">
          <span class="text-h3 !font-display !font-bold text-navy tnum">2</span>
          <h3 class="text-h4">A licensed agent reads it</h3>
        </div>
        <p class="mt-5 text-slate">
          A person, with a licence number, who can actually place the policy. Not a receptionist
          taking a message.
        </p>
      </div>
      <div class="reveal">
        <div class="flex items-baseline gap-3 pb-4 border-b border-navy">
          <span class="text-h3 !font-display !font-bold text-navy tnum">3</span>
          <h3 class="text-h4">We contact you</h3>
        </div>
        <p class="mt-5 text-slate">
          Within {C.SLA}, by whichever of phone or email you seem to prefer.
        </p>
        <p class="mt-3 text-sm text-muted">
          <!-- [SET HONEST SLA] Replace with the response time the agency can
               actually hold to, including on a Friday afternoon. -->
          If we are going to be slower than that, we will tell you rather than let it drift.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- =====================================================================
     MINI FAQ.
     ================================================================== -->
<section class="section-tight">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8">
      <div class="lg:col-span-4">
        <h2 class="reveal text-h2">Before you get in touch</h2>
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
