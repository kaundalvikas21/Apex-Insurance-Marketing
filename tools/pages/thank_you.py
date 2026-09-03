# -*- coding: utf-8 -*-
"""THANK YOU. Noindex. A confirmation page, not a place to sell anything else,
so the only additions to it are things the visitor needs before the call:
what to have ready, and a way out that is not the browser back button.

It stays deliberately short. The three product links at the end exist because a
confirmation page with one link to the home page is a dead end for anyone who
landed here still unsure which product they asked about.
"""
from icons import icon
import chrome as C

PATH = "/thank-you/"
OUT = "thank-you/index.html"
ACTIVE = "/contact/"
SILO = "contact"
ROBOTS = "noindex, follow"
TITLE = "Thank you | Apex Insurance Marketing"
DESC = ("We have your message. A licensed agent at Apex Insurance Marketing will review it "
        "and be in touch. Here is exactly what happens next.")


def schema():
    return [C.org_schema()]


def body():
    return f"""
<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <div class="flex items-start gap-4">
        {icon("circle-check", 40, "shrink-0 text-green mt-1")}
        <div>
          <h1 class="text-h1">Thank you</h1>
          <p class="mt-5 text-lead text-slate">
            We have your message and a licensed agent will be in touch within {C.SLA}.
          </p>
        </div>
      </div>

      <div class="mt-12 card">
        <h2 class="text-h3 !font-display !font-semibold">What happens now</h2>
        <ol class="mt-6 grid gap-5">
          <li class="flex items-start gap-3">
            {icon("user-check", 22, "shrink-0 text-navy mt-1")}
            <span>A licensed agent reads what you sent. Not a receptionist, and not an
            automated quote engine.</span>
          </li>
          <li class="flex items-start gap-3">
            {icon("search", 22, "shrink-0 text-navy mt-1")}
            <span>We check your details against the carriers we are appointed with, including
            the ones that would decline, so the comparison is honest.</span>
          </li>
          <li class="flex items-start gap-3">
            {icon("phone", 22, "shrink-0 text-navy mt-1")}
            <span>We contact you within {C.SLA} with named carriers and real numbers. Nobody
            else calls you, because your details go nowhere else.</span>
          </li>
        </ol>

        <div class="mt-8 pt-8 border-t border-rule">
          <p class="text-slate">In a hurry? Calling is faster than waiting for us.</p>
          <div class="mt-4">
            {C.phone_link("thank_you", "btn btn-call", "Call " + C.PHONE_DISPLAY)}
          </div>
          <p class="mt-3 text-micro text-muted">{C.HOURS}</p>
        </div>
      </div>

      <!-- WHAT TO HAVE READY. The call goes faster and the quote comes back
           more accurate when these are to hand. Nothing here is a document we
           need sent; it is all things the agent will simply ask. -->
      <div class="mt-8 card">
        <h2 class="text-h3 !font-display !font-semibold">What to have ready for the call</h2>
        <p class="mt-3 text-slate">
          None of this needs sending anywhere. It just makes the call shorter, and it is the
          difference between a rough number and one you can rely on.
        </p>
        <ul class="mt-6 grid gap-5">
          {"".join('''<li class="flex items-start gap-3">%s
            <div>
              <p class="font-semibold text-navy">%s</p>
              <p class="mt-1 text-slate">%s</p>
            </div>
          </li>''' % (icon(ico, 22, "shrink-0 text-navy mt-1"), h, b) for ico, h, b in [
            ("calculator", "Roughly what you are trying to cover",
             "A mortgage balance, years of income, childcare, a funeral. An approximate number is fine; the agent will help you sharpen it."),
            ("stethoscope", "Any conditions and medications",
             "Names of prescriptions and rough dates of diagnosis. This is what decides which carriers will take you, and it is better said up front than found in underwriting."),
            ("users", "Family history, if you know it",
             "Parents or siblings with heart disease or cancer before 60. Several carriers rate this and several do not, which is exactly the kind of difference comparing finds."),
            ("file-text", "Any policy you already have",
             "Through work or bought privately. Sometimes the right answer is to keep what you have and add to it rather than replace it."),
          ])}
        </ul>
        <p class="mt-6 text-micro text-muted">
          You will not be asked for a Social Security number, bank details, or a payment card on
          this call.
        </p>
      </div>

      <!-- No dead end. Three routes back in, one per product, plus home. -->
      <div class="mt-8">
        <h2 class="text-h4">While you wait</h2>
        <ul class="mt-4 grid sm:grid-cols-3 gap-4">
          {"".join('''<li><a href="%s" class="tile">
            <span class="text-h4 text-ink">%s</span>
            <span class="mt-2 text-sm text-muted">%s</span>
          </a></li>''' % t for t in [
            ("/term-life-insurance/", "Term life", "How term is priced, and what happens when it ends."),
            ("/whole-life-insurance/", "Whole life", "The three guarantees, and the cash value question."),
            ("/final-expense-insurance/", "Final expense", "What it covers, and the waiting period to check for."),
          ])}
        </ul>
        <p class="mt-6 text-sm text-muted">
          <a class="link" href="/">Back to the home page</a>
        </p>
      </div>
    </div>
  </div>
</section>
"""
