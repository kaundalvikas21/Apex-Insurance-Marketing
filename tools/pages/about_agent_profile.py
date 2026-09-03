# -*- coding: utf-8 -*-
"""AGENT PROFILE TEMPLATE. Spec P0.

One reusable profile. Copy this module per real agent, change AGENT, and add
the module name to build.py's PAGES list. The slug in PATH must match the slug
used in about_agents.AGENTS or the index links to a 404.

This page is the reference target for every article byline's author field:
chrome.person_schema() sets its Person @id to this URL, so the Person node the
hub pages emit resolves to a page that actually describes a person. That is the
whole reason the profile carries externally verifiable licence numbers rather
than a biography.
"""
from icons import icon
import chrome as C

# --- The one block to change per agent. ------------------------------------
AGENT = {
    "slug":    C.AGENT_SLUG,
    "name":    C.AGENT_NAME,
    "title":   C.AGENT_TITLE,
    "years":   C.YEARS,
    "npn":     C.NPN,
    # [PLACEHOLDER LICENCE NUMBERS] Externally verifiable via each state's
    # department of insurance producer lookup. Resident state first.
    "licences": [
        ("[STATE]", "[LICENCE NUMBER]", "Resident", "Life"),
        ("[STATE]", "[LICENCE NUMBER]", "Non-resident", "Life"),
        ("[STATE]", "[LICENCE NUMBER]", "Non-resident", "Life"),
    ],
    "lines":   ["Life", "Accident and health, where the state licence includes it"],
    "focus":   "Term life, whole life, and final expense for consumer buyers",
}

PATH = "/about/agents/%s/" % AGENT["slug"]
OUT = "about/agents/%s/index.html" % AGENT["slug"]
ACTIVE = "/about/agents/"
SILO = "site"
TITLE = "%s, %s | Apex Insurance Marketing" % (AGENT["name"], AGENT["title"])
OG_TITLE = "%s, %s" % (AGENT["name"], AGENT["title"])
DESC = ("Licence numbers, states, years licensed, carrier appointments, and how to reach "
        "%s, a licensed life insurance agent at %s." % (AGENT["name"], C.BRAND))


def schema():
    """Person, with the @id chrome.person_schema() points every byline at."""
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("About", "/about/"),
                           ("Our agents", "/about/agents/"), (AGENT["name"], None)]),
            {"@context": "https://schema.org",
             "@type": "Person",
             "@id": C.DOMAIN + PATH + "#person",
             "name": AGENT["name"],
             "jobTitle": AGENT["title"],
             "url": C.DOMAIN + PATH,
             "worksFor": {"@id": C.DOMAIN + "/#organization"},
             "knowsAbout": ["Term life insurance", "Whole life insurance",
                            "Final expense insurance"],
             # [PLACEHOLDER] One credential per state licence held.
             "hasCredential": [
                 {"@type": "EducationalOccupationalCredential",
                  "credentialCategory": "%s Life Insurance Producer License" % kind,
                  "identifier": number,
                  "recognizedBy": {"@type": "Organization",
                                   "name": "%s Department of Insurance" % state}}
                 for state, number, kind, _lines in AGENT["licences"]],
             "mainEntityOfPage": C.DOMAIN + PATH}]


def licence_rows():
    return "\n            ".join(
        '<tr><th scope="row">%s</th><td class="tnum">%s</td><td>%s</td><td>%s</td></tr>'
        % (state, number, kind, lines)
        for state, number, kind, lines in AGENT["licences"])


def body():
    a = AGENT
    return f"""
<section class="pt-6 pb-14 md:pb-16 glow">
  <div class="container-ax">
    {C.crumbs([("Home", "/"), ("About", "/about/"),
               ("Our agents", "/about/agents/"), (a['name'], None)])}

    <div class="mt-8 grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">

      <div class="lg:col-span-7">
        <h1 class="reveal text-h1">{a['name']}</h1>
        <p class="reveal mt-4 text-lead text-slate">{a['title']}</p>
        <p class="reveal mt-6 text-slate">
          {a['focus']}. Licensed for <span class="tnum">{a['years']}</span> years, with the
          licence numbers below published so you can verify them with the state rather than
          with us.
        </p>

        <div class="reveal mt-8">
          {C.flag("Replace this whole profile with the real agent's details: name, photograph, "
                  "years licensed, National Producer Number, every state licence number, and the "
                  "carriers they are personally appointed with. Copy this module per agent. A "
                  "profile that cannot be verified against a state lookup is worse than no "
                  "profile at all.", "PLACEHOLDER AGENT PROFILE")}
        </div>
      </div>

      <div class="lg:col-span-4 lg:col-start-9">
        <div class="reveal panel">
          <!-- [REAL AGENT PHOTO REQUIRED] Real photograph of the named agent only.
               Never stock, for the same reason we do not print invented reviews. -->
          <div class="avatar-slot avatar-slot-lg mx-auto" aria-hidden="true">
            {icon("user-check", 34)}
            <span>Agent<br>photo</span>
          </div>
          <dl class="mt-6 grid gap-4 text-sm">
            <div class="flex justify-between gap-4 border-t border-rule pt-4">
              <dt class="text-muted">Years licensed</dt><dd class="tnum font-semibold text-ink">{a['years']}</dd>
            </div>
            <div class="flex justify-between gap-4 border-t border-rule pt-4">
              <dt class="text-muted">National Producer Number</dt><dd class="tnum font-semibold text-ink">{a['npn']}</dd>
            </div>
            <div class="flex justify-between gap-4 border-t border-rule pt-4">
              <dt class="text-muted">States licensed</dt><dd class="tnum font-semibold text-ink">{len(a['licences'])}</dd>
            </div>
          </dl>
          <div class="mt-6 grid gap-3">
            {C.phone_link("agent_profile", "btn btn-call btn-block", "Call " + C.PHONE_DISPLAY)}
            <a href="/get-a-quote/" class="btn btn-ghost btn-block">Request a quote</a>
          </div>
          <p class="mt-4 text-micro text-muted">{C.HOURS}</p>
        </div>
      </div>
    </div>
  </div>
</section>


<!-- =====================================================================
     LICENCES. The signature table treatment, because this is the table the
     page exists for.
     ================================================================== -->
<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">State licences</h2>
      <p class="reveal mt-5 text-slate">
        Each number below is a producer licence issued by that state. Search it in the state's
        own producer lookup. If the status there does not match what is published here, tell us
        before you buy anything.
      </p>
    </div>

    <div class="reveal mt-8 table-scroll table-signature">
      <table class="rate-table" style="min-width:36rem">
        <caption>State licences held by {a['name']}, with the lines each authorises.</caption>
        <thead>
          <tr>
            <th scope="col">State</th>
            <th scope="col">Licence number</th>
            <th scope="col">Type</th>
            <th scope="col">Lines authorised</th>
          </tr>
        </thead>
        <tbody>
            {licence_rows()}
        </tbody>
      </table>
    </div>
    <p class="reveal mt-4 text-micro text-muted max-w-3xl">
      <span class="pill mr-2">Reviewed: {C.REVIEW_DATE}</span>
      Licence numbers are verifiable through each state's department of insurance producer
      lookup. Agency level licences are listed separately on our
      <a class="link-static" href="/about/licensing/">licensing page</a>.
    </p>
  </div>
</section>


<section class="section">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">Appointments and lines</h2>
        <p class="reveal mt-5 text-slate">
          An appointment is a carrier authorising an agent to sell its products. It is what makes
          a comparison possible, and it is also the limit of one: nobody can quote a carrier they
          are not appointed with.
        </p>
        <a class="reveal link-static mt-6 inline-block text-sm" href="/about/carriers/">The carriers we are appointed with</a>
      </div>

      <div class="lg:col-span-6 lg:col-start-7 bento" data-stagger="40">
        <div class="reveal bento-cell bento-3">
          <p class="eyebrow">Lines authorised</p>
          <ul class="mt-4 grid gap-3">
            {"".join('<li class="flex items-start gap-3">%s<span class="text-slate">%s</span></li>'
                     % (icon("circle-check", 20, "shrink-0 mt-0.5 text-green"), t) for t in a['lines'])}
          </ul>
        </div>
        <div class="reveal bento-cell bento-cell-tint bento-3">
          <p class="eyebrow">Carrier appointments</p>
          <p class="mt-4 text-slate">
            Held individually, and listed on the carriers page. An agent's appointments can be
            narrower than the agency's, which is why the two lists are published separately.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>


<section class="section band-navy on-navy">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-8 items-center">
      <div class="lg:col-span-7">
        <h2 class="reveal text-h2 text-white">Work with {a['name']}</h2>
        <p class="reveal mt-4 text-white/85 max-w-2xl">
          Ask for them by name when you call, or say so in the form and we will route it.
        </p>
      </div>
      <div class="lg:col-span-4 lg:col-start-9 grid gap-3">
        {C.phone_link("agent_profile_footer", "btn btn-ghost btn-block", "Call " + C.PHONE_DISPLAY)}
        <a href="/get-a-quote/" class="btn btn-cta btn-block">Get a free quote</a>
      </div>
    </div>
  </div>
</section>"""
