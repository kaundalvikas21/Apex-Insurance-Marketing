# -*- coding: utf-8 -*-
"""AGENT INDEX. Spec P0.

A grid of agent cards. Three placeholder agents, clearly marked as placeholders
on the page rather than only in a comment, because this is exactly the page a
visitor uses to check we are real people.

Every card links to a profile carrying licence numbers a visitor can verify
against their own state's department of insurance. That verifiability is the
point of the page; the photographs are not.
"""
from icons import icon
import chrome as C

PATH = "/about/agents/"
OUT = "about/agents/index.html"
ACTIVE = PATH
SILO = "site"
TITLE = "Our Licensed Agents | Apex Insurance Marketing"
OG_TITLE = "The licensed agents at Apex Insurance Marketing"
DESC = ("The licensed life insurance agents at Apex Insurance Marketing, with state licence "
        "numbers you can verify, years licensed, and the carriers each is appointed with.")

# [PLACEHOLDER ROSTER] One entry per real agent before launch. `slug` becomes
# the profile URL and must match the module that builds that profile.
AGENTS = [
    {"slug": C.AGENT_SLUG, "name": C.AGENT_NAME, "title": C.AGENT_TITLE,
     "states": C.STATES, "years": C.YEARS,
     "line": "Term life, whole life, and final expense"},
    {"slug": C.AGENT_SLUG, "name": C.AGENT_NAME, "title": C.AGENT_TITLE,
     "states": C.STATES, "years": C.YEARS,
     "line": "Final expense and simplified issue whole life"},
    {"slug": C.AGENT_SLUG, "name": C.AGENT_NAME, "title": C.AGENT_TITLE,
     "states": C.STATES, "years": C.YEARS,
     "line": "Term life and high face amount underwriting"},
]


def schema():
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("About", "/about/"), ("Our agents", None)]),
            {"@context": "https://schema.org", "@type": "ItemList",
             "@id": C.DOMAIN + PATH + "#agents",
             "name": "Licensed agents at " + C.BRAND,
             "itemListElement": [
                 {"@type": "ListItem", "position": i + 1,
                  "url": C.DOMAIN + PATH + a["slug"] + "/"}
                 for i, a in enumerate(AGENTS)]}]


def card(a):
    return f"""<li class="reveal">
          <a href="{PATH}{a['slug']}/" class="tile !items-stretch">
            <span class="flex items-start gap-4">
              <!-- [REAL AGENT PHOTO REQUIRED] A stock portrait here would present
                   a stranger as a named licensed agent. MASTER.md s7. -->
              <span class="avatar-slot shrink-0" aria-hidden="true">
                {icon("user-check", 26)}
                <span>Agent<br>photo</span>
              </span>
              <span>
                <span class="block text-h4 text-ink">{a['name']}</span>
                <span class="block mt-1 text-micro text-muted">{a['title']}</span>
              </span>
            </span>
            <span class="block mt-5 pt-5 border-t border-rule text-sm text-muted">
              <span class="block">Licensed in <span class="tnum">{a['states']}</span> states</span>
              <span class="block mt-1"><span class="tnum">{a['years']}</span> years licensed</span>
              <span class="block mt-1">{a['line']}</span>
            </span>
            <span class="mt-5 inline-flex items-center gap-2 text-sm font-semibold text-navy">
              Licence numbers and appointments {icon("arrow-right", 16)}
            </span>
          </a>
        </li>"""


def body():
    return f"""
<section class="pt-6 pb-14 md:pb-16 glow">
  <div class="container-ax">
    {C.crumbs([("Home", "/"), ("About", "/about/"), ("Our agents", None)])}

    <div class="mt-8 max-w-3xl">
      <h1 class="reveal text-h1">Our licensed agents</h1>
      <p class="reveal mt-5 text-lead text-slate">
        Every agent below holds an individual state licence, and every licence number is published
        on their profile so you can check it with your state's department of insurance instead of
        taking our word for it.
      </p>
    </div>

    <div class="reveal mt-8 max-w-3xl">
      {C.flag("The three cards below are placeholders. Replace with the real roster before "
              "launch: one card and one profile page per licensed agent, each with that agent's "
              "own name, photograph, licence numbers, and carrier appointments. Do not ship a "
              "roster that is larger than the licensed team.", "PLACEHOLDER ROSTER")}
    </div>

    <ul class="mt-10 grid sm:grid-cols-2 lg:grid-cols-3 gap-4" data-stagger="40">
      {"".join(card(a) for a in AGENTS)}
    </ul>
  </div>
</section>


<section class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">How to check a licence</h2>
        <p class="reveal mt-5 text-slate">
          You do not have to trust a number printed on our own website, and you should not have
          to. Every state publishes a lookup.
        </p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        {C.step(1, "Take the licence number from the agent's profile",
                "Each profile lists the licence number per state, alongside the lines that licence authorises.")}
        <div class="mt-8">
          {C.step(2, "Search your state's department of insurance lookup",
                  "Every state runs a public producer lookup. Search by licence number, or by the agent's name.")}
        </div>
        <div class="mt-8">
          {C.step(3, "Check the status, the lines, and the state",
                  "A licence can be active in one state and lapsed in another. If what you find does not match what we published, tell us and do not buy until it is resolved.")}
        </div>
        <a class="link-static mt-8 inline-block text-sm" href="/about/licensing/">Our agency licence numbers by state</a>
      </div>
    </div>
  </div>
</section>


<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-8 items-center">
      <div class="lg:col-span-7">
        <h2 class="reveal text-h2">Talk to one of them</h2>
        <p class="reveal mt-4 text-slate max-w-2xl">
          Calling gets you an agent directly. The form gets you one within {C.SLA}, with the
          comparison already done.
        </p>
      </div>
      <div class="lg:col-span-4 lg:col-start-9 grid gap-3">
        {C.phone_link("agents_footer", "btn btn-call btn-block", "Call " + C.PHONE_DISPLAY)}
        <a href="/get-a-quote/" class="btn btn-ghost btn-block">Get a free quote</a>
      </div>
    </div>
  </div>
</section>"""
