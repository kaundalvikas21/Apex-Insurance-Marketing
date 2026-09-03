# -*- coding: utf-8 -*-
"""404. Spec pre-launch checklist: never dead-end.

Written at the root as /404.html, which is the convention Netlify, Cloudflare
Pages, and GitHub Pages all pick up without configuration. If the site moves to
a host that wants something else, this is the one file to re-point.

Every route out is a route someone might actually have wanted: the three hubs,
the quote form, and the phone. No breadcrumb, because this page has no place in
the tree to describe.
"""
from icons import icon
import chrome as C

PATH = "/404.html"
OUT = "404.html"
ACTIVE = PATH
SILO = "site"
ROBOTS = "noindex, follow"
TITLE = "Page not found | Apex Insurance Marketing"
OG_TITLE = "Page not found"
DESC = "That page does not exist. Here is where to find what you were probably looking for."

DESTINATIONS = [
    ("/term-life-insurance/", "Term life insurance",
     "Cover for a set number of years. Usually the cheapest way to cover a mortgage or children at home."),
    ("/whole-life-insurance/", "Whole life insurance",
     "Cover for life, with a level premium and cash value that builds inside the policy."),
    ("/final-expense-insurance/", "Final expense insurance",
     "A smaller policy for a funeral and final bills. No medical exam."),
]


def schema():
    return [C.org_schema()]


def body():
    tiles = "".join(f"""
        <li class="reveal">
          <a href="{href}" class="tile">
            <span class="text-h4 text-ink">{title}</span>
            <span class="mt-2 text-sm text-muted">{desc}</span>
          </a>
        </li>""" for href, title, desc in DESTINATIONS)

    return f"""
<section class="pt-16 pb-14 md:pt-20 md:pb-16 glow">
  <div class="container-ax">
    <div class="max-w-2xl">
      <p class="eyebrow">Error 404</p>
      <h1 class="mt-3 text-h1">That page is not here</h1>
      <p class="mt-5 text-lead text-slate">
        The link may be old, or we may have moved something. Nothing is wrong with your browser
        and nothing is wrong with your details. Below is everything this site actually contains.
      </p>
      <div class="mt-8 flex flex-wrap gap-3">
        <a href="/get-a-quote/" class="btn btn-cta">Get a free quote</a>
        {C.phone_link("404_primary", "btn btn-call", "Call " + C.PHONE_DISPLAY)}
      </div>
    </div>

    <h2 class="reveal mt-16 text-h2">The three things we do</h2>
    <ul class="mt-8 grid sm:grid-cols-2 lg:grid-cols-3 gap-4" data-stagger="40">{tiles}
    </ul>
  </div>
</section>


<section class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">Or you were looking for</h2>
        <p class="reveal mt-5 text-slate">
          The pages people most often arrive at a broken link from.
        </p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <ul class="grid gap-4">
          {"".join('''<li class="reveal flex items-start gap-3">%s
            <div>
              <a class="link" href="%s">%s</a>
              <p class="mt-1 text-slate">%s</p>
            </div>
          </li>''' % (icon(ico, 22, "shrink-0 text-navy mt-1"), href, label, note) for ico, href, label, note in [
            ("users", "/about/", "About Apex Insurance Marketing",
             "Who we are, how we are paid, and what we do not do."),
            ("shield-check", "/about/licensing/", "Licensing by state",
             "Our licence numbers, so you can check them with your own state."),
            ("phone", "/contact/", "Contact us",
             "A phone number that reaches a licensed agent, and a form if you would rather write."),
          ])}
        </ul>
      </div>
    </div>
  </div>
</section>"""
