# -*- coding: utf-8 -*-
"""THANK YOU stub. Noindex. Kept minimal on purpose: it is a confirmation
page, not a place to sell anything else."""
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
        <h2 class="text-h3">What happens now</h2>
        <ol class="mt-6 grid gap-5">
          <li class="flex items-start gap-3">
            {icon("user-check", 22, "shrink-0 text-ink mt-1")}
            <span>A licensed agent reads what you sent. Not a receptionist, and not an
            automated quote engine.</span>
          </li>
          <li class="flex items-start gap-3">
            {icon("search", 22, "shrink-0 text-ink mt-1")}
            <span>We check your details against the carriers we are appointed with, including
            the ones that would decline, so the comparison is honest.</span>
          </li>
          <li class="flex items-start gap-3">
            {icon("phone", 22, "shrink-0 text-ink mt-1")}
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

      <p class="mt-10 text-sm text-muted">
        <a class="link" href="/">Back to the home page</a>
      </p>
    </div>
  </div>
</section>
"""
