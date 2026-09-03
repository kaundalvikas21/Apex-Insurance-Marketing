# -*- coding: utf-8 -*-
"""Site-wide constants and shared chrome for Apex Insurance Marketing.

Every placeholder value lives here so REPLACE-BEFORE-LAUNCH.md has one
address to point at. Nothing invented is presented as verified fact.
"""
import json

import images
from icons import icon

# --- PLACEHOLDERS. See REPLACE-BEFORE-LAUNCH.md -----------------------------
PHONE_DISPLAY = "(555) 018-0199"          # [PLACEHOLDER PHONE]
PHONE_TEL     = "+15550180199"            # [PLACEHOLDER PHONE]
HOURS         = "Mon to Fri, 8am to 7pm CT · Sat 9am to 2pm CT"   # [SET REAL HOURS]
STATES        = "[X]"                     # [PLACEHOLDER STATE COUNT]
NPN           = "[NPN]"                   # [PLACEHOLDER NATIONAL PRODUCER NUMBER]
YEARS         = "[X]"                     # [PLACEHOLDER YEARS IN BUSINESS]
AGENT_NAME    = "[Agent Name]"            # [PLACEHOLDER AGENT]
AGENT_TITLE   = "Licensed Life Insurance Agent"
REVIEW_DATE   = "[DATE]"                  # [PLACEHOLDER REVIEW DATE]
RATES_DATE    = "[DATE]"                  # [PLACEHOLDER RATE CARD DATE]
SLA           = "[X business hours]"      # [SET HONEST SLA]
DOMAIN        = "https://www.apexinsurancemarketing.com"
FOUNDED       = "[YEAR]"                  # [PLACEHOLDER YEAR FOUNDED]
CARRIERS      = "[X]"                     # [PLACEHOLDER APPOINTED CARRIER COUNT]
STREET        = "[STREET ADDRESS]"        # [PLACEHOLDER BUSINESS ADDRESS]
CITY          = "[CITY]"                  # [PLACEHOLDER BUSINESS ADDRESS]
REGION        = "[STATE]"                 # [PLACEHOLDER BUSINESS ADDRESS]
POSTCODE      = "[ZIP]"                   # [PLACEHOLDER BUSINESS ADDRESS]
# The agent profile every byline points its author node at. One profile page
# exists as a template; add a module per real agent and give each its own slug.
AGENT_SLUG    = "first-last"              # [PLACEHOLDER AGENT PROFILE SLUG]

BRAND = "Apex Insurance Marketing, LLC"

# The three legal documents cross-link to each other, which is the one place on
# the site where sideways linking between non-silo pages is correct: someone
# reading the privacy policy is often looking for the disclaimer.
LEGAL_SIBLINGS = [
    ("/legal/privacy/", "Privacy policy", "What we collect, why, and the rights you have over it."),
    ("/legal/terms/", "Terms of use", "The terms you accept by using this site."),
    ("/legal/disclaimer/", "Disclaimer", "What this site is, and what it is not."),
]

NAV = [
    ("/term-life-insurance/",          "Term Life Insurance"),
    ("/whole-life-insurance/",         "Whole Life Insurance"),
    ("/final-expense-insurance/",      "Final Expense Insurance"),
    ("/contact/",                      "Contact"),
]


def phone_link(location, cls="", label=None, size=20, wrap_num=True):
    """Click-to-call. data-cta-location feeds the GA4 call_click event."""
    text = label if label else PHONE_DISPLAY
    num = ('<span class="tnum">%s</span>' % text) if wrap_num else text
    return ('<a href="tel:%s" data-cta-location="%s" class="%s">%s%s</a>'
            % (PHONE_TEL, location, cls, icon("phone", size, "shrink-0"), num))


# ---------------------------------------------------------------------------
# IMAGERY
# See design-system/MASTER.md section 8. Manifest lives in tools/images.py.
# ---------------------------------------------------------------------------
def picture(name, sizes, cls="", img_cls="", eager=False, alt=None):
    """<picture> with AVIF then WebP then <img>.

    Every <img> carries explicit width and height so the box is reserved before
    the bytes arrive and the image cannot shift the layout. `sizes` must match
    the real rendered column width per breakpoint, or mobile downloads a
    desktop file for nothing.

    eager=True marks the one LCP candidate on a page. Everything else is lazy.
    """
    spec = images.IMAGES[name]
    widths = spec[2]
    text = spec[4] if alt is None else alt
    largest = widths[-1]
    w, h = largest, images.height_for(name, largest)

    def srcset(fmt):
        return ", ".join("/assets/img/%s-%d.%s %dw" % (name, x, fmt, x) for x in widths)

    loading = ('loading="eager" fetchpriority="high"' if eager
               else 'loading="lazy" decoding="async"')
    # A decorative image is hidden from assistive tech rather than announced as
    # an unnamed graphic.
    a11y = 'alt=""' if not text else 'alt="%s"' % text.replace('"', "&quot;")

    return f"""<picture class="{cls}">
      <source type="image/avif" srcset="{srcset('avif')}" sizes="{sizes}">
      <source type="image/webp" srcset="{srcset('webp')}" sizes="{sizes}">
      <img src="/assets/img/{name}-{widths[0]}.webp" width="{w}" height="{h}"
           {a11y} {loading} class="{img_cls}">
    </picture>"""


def banner(name, heading, sub, cta_html, eyebrow=None):
    """Full-bleed photo band carrying one heading and one CTA.

    CRO placement rules, and the reason this is not a hero image:
      * Never above the fold. The top of a service page belongs to the H1 and
        the quote form; a banner there pushes the form down and costs form
        starts.
      * Never between the hero CTA and the trust strip. Measured on this site
        at 433 to 491px of added gap, which breaks the proximity the strip is
        there to provide.
      * It sits at roughly 55 to 70 percent scroll depth, after the page has
        made its case, as the second conversion ask for a reader who is now
        warm. Height comes from the copy, not from a 21:9 box, so the band
        costs about one screen third rather than a full screen.

    The photograph is decorative and is scrimmed. All meaning lives in the
    text, which is why every band image carries empty alt.
    """
    eye = ('<p class="eyebrow">%s</p>' % eyebrow) if eyebrow else ""
    return f"""
<section class="banner-band on-navy">
  {picture(name, "100vw", cls="banner-media", img_cls="banner-img")}
  <div class="container-ax banner-content section-tight">
    <div class="reveal grid lg:grid-cols-12 gap-6 lg:gap-10 items-center">
      <div class="lg:col-span-7">
        {eye}
        <p class="text-h2 !font-display !font-bold text-white">{heading}</p>
        <p class="mt-4 text-white/85 max-w-2xl">{sub}</p>
      </div>
      <div class="lg:col-span-4 lg:col-start-9">{cta_html}</div>
    </div>
  </div>
</section>"""


RATIO_CLASS = {(4, 5): "media-tall", (3, 2): "media-wide", (21, 9): "media-band",
               (16, 9): "media-strip", (4, 3): "media-square-ish"}


def figure(name, sizes, caption=None, cls="", eager=False, glow=False):
    """Editorial image block. glow=True paints the soft blue ambient glow
    behind the plate. No scroll-linked motion in this variation."""
    ratio = RATIO_CLASS[images.IMAGES[name][1]]
    media = "media " + ratio
    cap = ('<figcaption class="mt-3 text-micro text-muted">%s</figcaption>' % caption) if caption else ""
    return ('<figure class="%s%s">%s%s</figure>'
            % (cls, " glow" if glow else "", picture(name, sizes, cls=media, img_cls="media-img", eager=eager), cap))


# ---------------------------------------------------------------------------
# HEADER
# ---------------------------------------------------------------------------
def header(active):
    links = "".join(
        '<a class="nav-link" href="%s"%s>%s</a>'
        % (href, ' aria-current="page"' if href == active else "", label)
        for href, label in NAV
    )
    panel_links = "".join(
        '<a class="block py-3 text-ink text-base font-medium border-b border-rule" href="%s"%s>%s</a>'
        % (href, ' aria-current="page"' if href == active else "", label)
        for href, label in NAV
    )
    return f"""<a class="skip-link" href="#main">Skip to main content</a>
<div data-header-sentinel aria-hidden="true" style="height:1px"></div>

<header class="site-header" data-header>
  <div class="container-ax">
    <div class="header-inner">

      <a href="/" class="shrink-0 rounded-lg" aria-label="{BRAND}, home">
        <span class="wordmark">Apex</span>
        <span class="wordmark-sub">Insurance Marketing</span>
      </a>

      <nav class="hidden lg:flex items-center gap-3 xl:gap-7 ml-4 xl:ml-10" aria-label="Primary">
        {links}
      </nav>

      <div class="ml-auto flex items-center gap-2 sm:gap-3">
        <!-- Click-to-call is present at every desktop width. Below 1280 the
             number itself does not fit beside four product-name nav links,
             so the label shortens rather than the CTA disappearing. -->
        {phone_link("header", "hidden lg:inline-flex xl:hidden items-center gap-2 min-h-[48px] px-2 text-navy text-sm font-semibold whitespace-nowrap rounded-lg hover:text-navy-700 transition-colors", "Call")}
        {phone_link("header", "hidden xl:inline-flex items-center gap-2 min-h-[48px] px-2 text-navy text-sm font-semibold whitespace-nowrap rounded-lg hover:text-navy-700 transition-colors")}
        <a href="/get-a-quote/" class="btn btn-cta hidden sm:inline-flex !text-sm !px-4 xl:!px-5">Get a Free Quote</a>
        <a href="tel:{PHONE_TEL}" data-cta-location="header_mobile"
           class="lg:hidden inline-flex items-center justify-center w-12 h-12 text-navy rounded-lg">
          <span class="sr-only">Call {PHONE_DISPLAY}</span>
          {icon("phone", 24)}
        </a>
        <button type="button" data-nav-toggle aria-expanded="false" aria-controls="site-nav"
                class="lg:hidden inline-flex items-center justify-center w-12 h-12 -mr-2 text-navy rounded-lg">
          <span class="sr-only">Open menu</span>
          {icon("menu", 24)}
        </button>
      </div>
    </div>
  </div>

  <div id="site-nav" data-nav-panel hidden class="lg:hidden nav-panel">
    <div class="container-ax py-4">
      <nav aria-label="Primary, mobile">{panel_links}</nav>
      <div class="mt-5 grid gap-3">
        {phone_link("header_mobile_panel", "btn btn-ghost btn-block", "Call " + PHONE_DISPLAY)}
        <a href="/get-a-quote/" class="btn btn-cta btn-block">Get a Free Quote</a>
      </div>
    </div>
  </div>
</header>"""


# ---------------------------------------------------------------------------
# FOOTER
# Note on internal linking: the footer deliberately does NOT repeat the three
# hub links or /contact/. Those live in the primary nav. Spec section 07
# requires one link per target per page.
# ---------------------------------------------------------------------------
def footer():
    company = [
        ("/about/",          "About Apex"),
        ("/about/agents/",   "Our licensed agents"),
        ("/about/licensing/", "Licensing and appointments"),
    ]
    legal = [
        ("/legal/privacy/",    "Privacy policy"),
        ("/legal/terms/",      "Terms of use"),
        ("/legal/disclaimer/", "Disclaimer"),
    ]
    def col(title, items):
        rows = "".join('<li><a class="footer-link" href="%s">%s</a></li>' % (h, t) for h, t in items)
        return (f'<div><h2 class="text-white text-micro font-semibold uppercase tracking-[0.12em] '
                f'!font-sans">{title}</h2><ul class="mt-4 grid gap-2.5">{rows}</ul></div>')

    return f"""<footer class="site-footer band-navy on-navy">
  <div class="container-ax py-16 lg:py-20">

    <div class="grid gap-10 md:grid-cols-2 lg:grid-cols-12 lg:gap-8">

      <div class="lg:col-span-4">
        <span class="wordmark">Apex</span>
        <span class="wordmark-sub">Insurance Marketing</span>
        <p class="mt-5 text-sm text-white/80 max-w-sm">
          An independent life insurance agency. We are appointed with multiple carriers,
          which means we compare them for you instead of selling you one company's product.
        </p>
        <div class="mt-6">
          {phone_link("footer", "btn btn-ghost", "Call " + PHONE_DISPLAY)}
          <p class="mt-3 text-micro text-white/72">{HOURS}</p>
        </div>
      </div>

      <div class="lg:col-span-3 lg:col-start-6">{col("Company", company)}</div>
      <div class="lg:col-span-3 lg:col-start-10">{col("Legal", legal)}</div>
    </div>

    <!-- The disclosures sit on the same 12 tracks as the columns above rather
         than in a max-w-4xl block whose right edge lines up with nothing. -->
    <div class="mt-14 pt-8 border-t border-white/15 grid gap-8 lg:grid-cols-12 lg:gap-8 text-micro leading-relaxed text-white/80">
      <!-- [PENDING LEGAL REVIEW] license disclosure wording -->
      <p class="lg:col-span-4">
        {BRAND} is a licensed independent insurance agency. Licensed in {STATES} states.
        National Producer Number {NPN}. Agency license numbers by state are listed on our
        <a class="link-static" href="/about/licensing/">licensing page</a>.
      </p>
      <p class="lg:col-span-4">
        {BRAND} is not affiliated with, endorsed by, or sponsored by any government agency,
        including the Social Security Administration, Medicare, or the Department of Veterans Affairs.
      </p>
      <p class="lg:col-span-4">
        Policies are issued by third party insurance carriers. Coverage, availability, premiums,
        riders, and benefits vary by carrier, state, age, and health. All guarantees are subject to
        the claims paying ability of the issuing carrier. Content on this site is general
        information, not insurance, tax, or legal advice, and is not an offer of coverage.
      </p>
      <p class="lg:col-span-12">&#169; 2026 {BRAND}. All rights reserved.</p>
    </div>
  </div>
</footer>"""


# ---------------------------------------------------------------------------
# SCHEMA
# ---------------------------------------------------------------------------
def org_schema():
    """Organization + InsuranceAgency, sitewide, linked by @id."""
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Organization",
                "@id": DOMAIN + "/#organization",
                "name": BRAND,
                "alternateName": "Apex Insurance Marketing",
                "url": DOMAIN + "/",
                "telephone": PHONE_TEL,
                "description": ("Independent, licensed life insurance agency helping consumers "
                                "compare term life, whole life, and final expense coverage from "
                                "multiple appointed carriers."),
                "areaServed": {"@type": "Country", "name": "United States"},
                "contactPoint": [{
                    "@type": "ContactPoint",
                    "telephone": PHONE_TEL,
                    "contactType": "sales",
                    "areaServed": "US",
                    "availableLanguage": "English"
                }]
            },
            {
                "@type": "InsuranceAgency",
                "@id": DOMAIN + "/#agency",
                "name": BRAND,
                "url": DOMAIN + "/",
                "telephone": PHONE_TEL,
                "parentOrganization": {"@id": DOMAIN + "/#organization"},
                "knowsAbout": ["Term life insurance", "Whole life insurance",
                               "Final expense insurance", "Burial insurance"],
                # [PLACEHOLDER] Replace with the real business address before launch.
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": STREET,
                    "addressLocality": CITY,
                    "addressRegion": REGION,
                    "postalCode": POSTCODE,
                    "addressCountry": "US"
                }
            },
            {
                "@type": "WebSite",
                "@id": DOMAIN + "/#website",
                "url": DOMAIN + "/",
                "name": BRAND,
                "publisher": {"@id": DOMAIN + "/#organization"}
            }
        ]
    }


def breadcrumbs(trail):
    """trail: [(name, path)] including Home. Path None for the current page."""
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            dict({"@type": "ListItem", "position": i + 1, "name": name},
                 **({"item": DOMAIN + path} if path else {}))
            for i, (name, path) in enumerate(trail)
        ]
    }


def faq_schema(items):
    """items: [(question, answer_plaintext)]"""
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in items
        ]
    }


def person_schema(page_url):
    """Person node for the agent byline.

    @id points at the agent's own profile page, which is the reference target
    every article byline resolves to. Pointing it at the index would make four
    pages assert an author that is not a person.
    """
    return {
        "@context": "https://schema.org",
        "@type": "Person",
        "@id": DOMAIN + "/about/agents/" + AGENT_SLUG + "/#person",
        "name": AGENT_NAME,
        "jobTitle": AGENT_TITLE,
        "url": DOMAIN + "/about/agents/" + AGENT_SLUG + "/",
        "worksFor": {"@id": DOMAIN + "/#organization"},
        # [PLACEHOLDER] Add real credentials, state license numbers, and years licensed.
        "hasCredential": {
            "@type": "EducationalOccupationalCredential",
            "credentialCategory": "Resident Life Insurance Producer License",
            "recognizedBy": {"@type": "Organization", "name": "[STATE] Department of Insurance"}
        },
        "mainEntityOfPage": DOMAIN + page_url
    }


def jsonld(*objs):
    return "\n".join(
        '<script type="application/ld+json">%s</script>' % json.dumps(o, indent=None, separators=(",", ":"))
        for o in objs
    )


# ---------------------------------------------------------------------------
# SHARED PAGE PARTS (hubs and contact)
# ---------------------------------------------------------------------------
STATES_LIST = [
    ("AL","Alabama"),("AK","Alaska"),("AZ","Arizona"),("AR","Arkansas"),("CA","California"),
    ("CO","Colorado"),("CT","Connecticut"),("DE","Delaware"),("DC","District of Columbia"),
    ("FL","Florida"),("GA","Georgia"),("HI","Hawaii"),("ID","Idaho"),("IL","Illinois"),
    ("IN","Indiana"),("IA","Iowa"),("KS","Kansas"),("KY","Kentucky"),("LA","Louisiana"),
    ("ME","Maine"),("MD","Maryland"),("MA","Massachusetts"),("MI","Michigan"),("MN","Minnesota"),
    ("MS","Mississippi"),("MO","Missouri"),("MT","Montana"),("NE","Nebraska"),("NV","Nevada"),
    ("NH","New Hampshire"),("NJ","New Jersey"),("NM","New Mexico"),("NY","New York"),
    ("NC","North Carolina"),("ND","North Dakota"),("OH","Ohio"),("OK","Oklahoma"),("OR","Oregon"),
    ("PA","Pennsylvania"),("RI","Rhode Island"),("SC","South Carolina"),("SD","South Dakota"),
    ("TN","Tennessee"),("TX","Texas"),("UT","Utah"),("VT","Vermont"),("VA","Virginia"),
    ("WA","Washington"),("WV","West Virginia"),("WI","Wisconsin"),("WY","Wyoming"),
]


def state_options():
    # [PLACEHOLDER] Trim this list to the states the agency is actually
    # licensed in before launch. Offering a state we cannot write in wastes
    # the visitor's time and ours.
    return "".join('<option value="%s">%s</option>' % (a, n) for a, n in STATES_LIST)


def crumbs(trail):
    """Visible breadcrumb. trail: [(name, path or None)]."""
    sep = icon("chevron-right", 14, "text-muted shrink-0")
    parts = []
    last = len(trail) - 1
    for i, (name, path) in enumerate(trail):
        if i:
            parts.append(sep)
        if path:
            parts.append('<a href="%s">%s</a>' % (path, name))
        else:
            # aria-current marks the current page, so only the final crumb can
            # carry it. An unlinked intermediate crumb (a section with no index
            # page) is plain text.
            parts.append('<span%s>%s</span>'
                         % (' aria-current="page"' if i == last else "", name))
    return ('<nav class="crumbs" aria-label="Breadcrumb"><ol class="contents">%s</ol></nav>'
            % "".join('<li class="contents" aria-hidden="true">%s</li>' % p if p.startswith('<svg')
                      else '<li class="contents">%s</li>' % p
                      for p in parts))


def byline():
    """Spec section 09.5. Appears on every hub.

    Two columns at full container width. As a single narrow card it left an
    identical 368px dead gutter on all three hubs; as two columns the row is
    full and each column still breaks at a readable measure.
    """
    return f"""<div class="card">
      <div class="grid lg:grid-cols-12 gap-8 lg:gap-10 items-start">

        <div class="lg:col-span-5 flex items-start gap-5">
          <!-- [REAL AGENT PHOTO REQUIRED]
               This slot stays a placeholder on purpose. A stock photograph here
               would present a stranger as the named licensed agent, which is the
               same fabrication as an invented testimonial. See MASTER.md s7. -->
          <div class="avatar-slot shrink-0" aria-hidden="true">
            {icon("user-check", 26)}
            <span>Agent<br>photo</span>
          </div>
          <div>
            <!-- Spec section 09.5 requires this exact construction:
                 "Written by [Agent Name], Licensed Agent, Reviewed [date]". -->
            <p class="text-h4">Written by {AGENT_NAME}, {AGENT_TITLE}</p>
            <p class="mt-3 text-micro text-muted">
              Reviewed {REVIEW_DATE}<br>
              Licensed in {STATES} states<br>
              National Producer Number {NPN}
            </p>
          </div>
        </div>

        <div class="lg:col-span-7">
          <p class="text-slate">
            This page is written and kept current by a licensed agent who places these policies.
            Where a figure comes from a carrier rate card, the card and its date are named on the
            page. Where something depends on your state or your health, we say so instead of
            rounding it off.
          </p>
          <p class="mt-4 text-slate">
            If you find something here that is out of date or wrong, tell us and we will correct it
            and change the review date. That is the whole point of printing one.
          </p>
          <a class="link-static mt-5 inline-block text-sm" href="/about/agents/">About our licensed agents</a>
        </div>
      </div>
    </div>"""


def acc(q, a, group, size=22):
    """One FAQ row. Native <details>, so keyboard and screen-reader behaviour
    comes free and cannot be broken by a JavaScript error on a YMYL page.

    `group` is the <details name> that makes the set single-open. It must be
    unique per page, or two accordions on one page close each other.
    Final expense passes size=24 with the rest of its larger scale.
    """
    return ('<details class="acc" name="%s">'
            '<summary>%s<span class="acc-icon">%s</span></summary>'
            '<div class="acc-body"><p class="text-slate">%s</p></div>'
            '</details>') % (group, q, icon("plus", size), a)


def faq_section(heading, items, group, intro=None, size=22, cls="section", center=True):
    """Heading plus accordion list. `items` is [(question, answer_html)] and is
    the same list that should be passed to faq_schema(), so the visible copy and
    the structured data can never disagree.

    An accordion has no second column and never will, so left aligning it in a
    1200px container leaves 40 percent of the row empty, which MASTER.md
    section 3 forbids. Centring the block is the fix. Only the heading is
    centred text: the question rows stay left aligned, because centred rows in
    a list are harder to scan. This is one centred section, not the centred
    page section 7 bans.
    """
    rows = "\n      ".join(acc(q, a, group, size) for q, a in items)
    lead = ('<p class="reveal mt-5 text-slate">%s</p>' % intro) if intro else ""
    head_cls = "max-w-2xl mx-auto text-center" if center else "max-w-2xl"
    list_cls = "max-w-3xl mx-auto" if center else "max-w-3xl"
    return f"""<section class="{cls}">
  <div class="container-ax">
    <div class="{head_cls}">
      <h2 class="reveal text-h2">{heading}</h2>
      {lead}
    </div>
    <div class="mt-10 grid gap-3 {list_cls}" data-stagger="60">
      {rows}
    </div>
  </div>
</section>"""


def spoke_module(heading, intro, spokes):
    """Visible in-page module linking DOWN to every spoke in the silo.
    spokes: [(href, anchor_text, one_line_description)]"""
    items = "".join(f"""
        <li class="reveal">
          <a href="{href}" class="tile">
            <span class="text-h4 text-ink">{text}</span>
            <span class="mt-2 text-sm text-muted">{desc}</span>
          </a>
        </li>""" for href, text, desc in spokes)
    return f"""<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">{heading}</h2>
      <p class="reveal mt-5 text-slate">{intro}</p>
    </div>
    <ul class="mt-10 grid sm:grid-cols-2 lg:grid-cols-3 gap-4" data-spoke-module data-stagger="40">{items}
    </ul>
  </div>
</section>"""


def step(n, title, body, note=None):
    """Numbered step. Numeral in the display face, tabular."""
    extra = ('<p class="mt-2 text-micro text-muted">%s</p>' % note) if note else ""
    return f"""<div class="reveal flex items-start gap-4">
      <span class="step-num tnum" aria-hidden="true">{n}</span>
      <div>
        <h3 class="text-h4">{title}</h3>
        <p class="mt-2 text-slate">{body}</p>{extra}
      </div>
    </div>"""


def stat(value, label, prefix="", suffix="", count=True, cls=""):
    """A figure with a label. `value` must be a spec figure (10, 30, 2000,
    50000, 15), never a placeholder. count=False renders it static, which is
    also what html.fe and reduced motion get regardless."""
    text = "%s%s%s" % (prefix, format(value, ",") if isinstance(value, int) else value, suffix)
    attrs = ""
    if count and isinstance(value, int):
        attrs = ' data-count="%d"' % value
        if prefix: attrs += ' data-count-prefix="%s"' % prefix
        if suffix: attrs += ' data-count-suffix="%s"' % suffix
    return (f'<div class="stat {cls}"><span class="stat-value"{attrs}>{text}</span>'
            f'<span class="stat-label">{label}</span></div>')


def legal_doc(heading, standfirst, sections, updated=None):
    """The shared /legal/ page body: a sticky table of contents beside numbered
    sections at a readable measure.

    `sections` is [(id, title, body_html)]. Every section gets an id so a
    section can be linked to directly, which is what people actually do with a
    privacy policy: they arrive looking for one clause.

    Legal copy on this site is [PENDING LEGAL REVIEW] and says so on the page
    rather than only in a comment. A policy a visitor cannot rely on should not
    look like one they can.
    """
    toc = "".join('<li><a class="footer-link !text-slate hover:!text-navy" href="#%s">'
                  '<span class="tnum">%d.</span> %s</a></li>' % (sid, i + 1, title)
                  for i, (sid, title, _body) in enumerate(sections))
    blocks = "".join(f"""
        <section id="{sid}" class="scroll-mt-28 pt-10 first:pt-0">
          <h2 class="text-h3 !font-display !font-semibold">
            <span class="tnum text-muted">{i + 1}.</span> {title}
          </h2>
          <div class="mt-4 grid gap-4 text-slate">{bodyhtml}</div>
        </section>""" for i, (sid, title, bodyhtml) in enumerate(sections))

    return f"""
<section class="pt-6 pb-14 md:pb-16">
  <div class="container-ax">
    {crumbs([("Home", "/"), (heading, None)])}

    <div class="mt-8 max-w-3xl">
      <h1 class="text-h1">{heading}</h1>
      <p class="mt-5 text-lead text-slate">{standfirst}</p>
      <p class="mt-5">
        <span class="pill mr-2">Last updated: {updated or REVIEW_DATE}</span>
        <span class="text-micro text-muted">{BRAND}</span>
      </p>
    </div>

    <div class="mt-8 max-w-3xl">
      {flag("This document is template copy and has not been reviewed by counsel. It must be "
            "replaced with language approved for the states the agency is licensed in, covering "
            "TCPA consent, CCPA and state privacy rights, and the agency's actual data practices, "
            "before this site goes live.", "PENDING LEGAL REVIEW")}
    </div>

    <div class="mt-12 grid lg:grid-cols-12 gap-10 lg:gap-12">

      <nav class="lg:col-span-3" aria-label="On this page">
        <div class="sticky-col">
          <h2 class="text-micro font-semibold uppercase tracking-[0.12em] text-muted">On this page</h2>
          <ul class="mt-4 grid gap-2.5 text-sm">{toc}</ul>
        </div>
      </nav>

      <div class="lg:col-span-8 lg:col-start-5 measure grid divide-y divide-rule">{blocks}
      </div>
    </div>
  </div>
</section>


<section class="section-tight band">
  <div class="container-ax">
    <div class="grid md:grid-cols-3 gap-4">
      {"".join('<a class="tile" href="%s"><span class="text-h4 text-ink">%s</span>'
               '<span class="mt-2 text-sm text-muted">%s</span></a>' % t for t in LEGAL_SIBLINGS
               if t[1] != heading)}
    </div>
  </div>
</section>"""


def flag(text, token="PLACEHOLDER"):
    """Visible placeholder notice. MASTER.md s5: a flag renders on the page, not
    only in an HTML comment, because the person who has to replace it is usually
    looking at the page rather than the source."""
    return '<p class="flag">[%s] %s</p>' % (token, text)


def rates_flag(what):
    """Visible placeholder notice for any rate component. Rule 6."""
    return flag(f'The {what} below are structural placeholders. No premium shown here is a real, '
                f'quoted, or offered rate. Populate from current carrier rate cards and update the '
                f'date line before this page goes live.',
                "PLACEHOLDER: REPLACE WITH APPOINTED CARRIER RATE CARDS, DATED")


# ---------------------------------------------------------------------------
# T2: THE RATE CHART
# Generalised from the term hub's rate_table() so the three P1 rate pages
# (term rates, whole life rates, final expense cost) share one implementation.
#
# The hubs deliberately keep their own copies. They are approved and signed
# off, and refactoring them onto this would risk changing their rendered output
# for no visible gain.
#
# Every cell is `$--` by decision (MASTER.md s7): no invented premium, even a
# marked one, because a marked fake number still gets screenshotted. The
# toggles therefore drive the caption only. When the carrier rate cards arrive,
# populate the cells from a dataset keyed by (toggle state, age band, coverage)
# and have the toggles rewrite them.
# ---------------------------------------------------------------------------
def rate_chart(panels_id, cols, rows, toggles, caption, row_cta=None,
               prefill_target=None, cta_location="rate_row", min_width="0",
               note=None, top_margin="mt-8", toggle_grid="flex flex-wrap items-end gap-6",
               aside=None):
    """One signature rate table with its toggles above and a dated line beneath.

    cols      [column label]. Coverage amounts, already formatted.
    rows      [(band_label, prefill_dict_or_None)].
    toggles   [(legend, radio_name, [(value, label)], prefill_name_or_None)].
              The first option of each is checked.
    row_cta   None, "prefill", or "call".
              "prefill" adds a trailing cell per row whose button writes the
              row's numbers into `prefill_target` (site.js section 7), merging
              in whatever the toggles above are currently set to.
              "call" puts a click-to-call under the age label INSIDE the row
              header, which is how the final expense pages stay at three
              columns. Phone weighted silos use this.
    aside     optional paragraph rendered beside the toggles.
    """
    def toggle(legend, name, options, prefill_name):
        opts = "".join(
            '<label class="choice"><input type="radio" name="%s" value="%s"%s%s>'
            '<span>%s</span></label>'
            % (name, value, " checked" if i == 0 else "",
               (' data-prefill-name="%s"' % prefill_name) if prefill_name else "", label)
            for i, (value, label) in enumerate(options))
        return ('<fieldset><legend class="field-label">%s</legend>'
                '<div class="choice-row">%s</div></fieldset>' % (legend, opts))

    toggle_html = "".join(toggle(*t) for t in toggles)
    if aside:
        toggle_html += '<p class="text-sm text-muted">%s</p>' % aside

    heads = "".join('<th scope="col" class="tnum">%s</th>' % c for c in cols)
    if row_cta == "prefill":
        heads += '<th scope="col"><span class="sr-only">Get a quote for this row</span></th>'

    body_rows = []
    for band, prefill in rows:
        cells = "".join('<td class="tnum">$--</td>' for _ in cols)
        if row_cta == "call":
            # Under the age label, not in its own column: a fourth column would
            # break the three column ceiling the senior pages are held to.
            head = ('<th scope="row"><span class="block">%s</span>%s</th>'
                    % (band, phone_link(cta_location, "btn-row mt-2", "Get this quoted", 18)))
            body_rows.append("<tr>%s%s</tr>" % (head, cells))
        elif row_cta == "prefill":
            btn = ('<button type="button" class="btn-row" data-prefill=\'%s\' '
                   'data-prefill-target="%s">Quote this %s</button>'
                   % (json.dumps(prefill, separators=(",", ":")), prefill_target,
                      icon("arrow-right", 16)))
            body_rows.append('<tr><th scope="row">%s</th>%s<td>%s</td></tr>' % (band, cells, btn))
        else:
            body_rows.append('<tr><th scope="row">%s</th>%s</tr>' % (band, cells))
    body = "\n            ".join(body_rows)

    tail = note or ("Source: [CARRIER RATE CARD NAME AND EDITION]. Premiums vary by carrier, "
                    "state, health, and tobacco use. A rate table is an illustration of shape, "
                    "not an offer of coverage.")

    return f"""
    <div data-panels="{panels_id}">

      <div class="reveal {top_margin} {toggle_grid}">
        {toggle_html}
      </div>

      <!-- INTEGRATION POINT: every cell below is a structural placeholder.
           Populate from the carrier rate cards keyed by (toggle state, age
           band, coverage) and have the toggles above rewrite them. Until then
           the toggles update the caption only, and nothing here can be
           mistaken for a real quoted premium. -->
      <!-- .reveal sits on the scroll container itself. A transformed wrapper
           around a scrolling table leaks the table's width into the page
           until the section reveals. -->
      <div class="reveal mt-6 table-scroll table-signature">
        <table class="rate-table" style="min-width:{min_width}">
          <caption>
            {caption}
            <span data-panel-caption></span>
          </caption>
          <thead>
            <tr>
              <th scope="col">Age at application</th>
              {heads}
            </tr>
          </thead>
          <tbody>
            {body}
          </tbody>
        </table>
      </div>
    </div>

    <p class="reveal mt-4 text-micro text-muted max-w-3xl">
      <span class="pill mr-2">Rates last updated: {RATES_DATE}</span>
      {tail}
    </p>"""


# ---------------------------------------------------------------------------
# T1: THE TWO MANDATED SECTIONS
# Template T1 requires an honest post-submit expectation and a no-obligation /
# data-handling statement before the FAQ. Both appear on all three quote pages,
# so they are authored once here rather than three times.
# ---------------------------------------------------------------------------
def post_submit_section(steps, heading="What happens after you submit", intro=None,
                        cls="section", media=None, sticky=True):
    """T1's honest call expectation. steps: [(title, body, note_or_None)].

    `media` and `sticky` behave as in prose(): the left column must not leave a
    dead half row beside a long step list.
    """
    lead = ('<p class="reveal mt-5 text-slate">%s</p>' % intro) if intro else ""
    art = ('<div class="reveal mt-8">%s</div>' % media) if media else ""
    blocks = "".join(
        ('<div class="mt-8">%s</div>' % step(i + 1, *s)) if i else step(i + 1, *s)
        for i, s in enumerate(steps))
    inner = f"""<h2 class="reveal text-h2">{heading}</h2>
        {lead}
        {art}"""
    col = ('<div class="sticky-col">%s</div>' % inner) if sticky else inner
    align = "" if sticky else " items-start"
    return f"""<section class="{cls}">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8{align}">
      <div class="lg:col-span-5">
        {col}
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        {blocks}
      </div>
    </div>
  </div>
</section>"""


def no_obligation_section(short_version, no_obligation, stopping_contact,
                          heading="What we do with what you send", cls="section band",
                          intro=None, media=None, sticky=True):
    """T1's data-handling block: the last real objection before the FAQ.

    Three panes, because there are exactly three things a visitor wants to know
    at this point: where their details go, what submitting commits them to, and
    how to make it stop. The privacy policy link lives in the third pane, which
    is the only place on a quote page that link is earned.
    """
    lead = ('<p class="reveal mt-5 text-slate">%s</p>' % intro) if intro else ""
    art = ('<div class="reveal mt-8">%s</div>' % media) if media else ""
    inner = f"""<h2 class="reveal text-h2">{heading}</h2>
        {lead}
        {art}"""
    col = ('<div class="sticky-col">%s</div>' % inner) if sticky else inner
    align = "" if sticky else " items-start"
    return f"""<section class="{cls}">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8{align}">
      <div class="lg:col-span-5">
        {col}
      </div>
      <div class="lg:col-span-6 lg:col-start-7 bento" data-stagger="40">
        <div class="reveal bento-cell bento-cell-blue bento-6">
          <p class="eyebrow text-white/80">The short version</p>
          <p class="mt-3 text-white/90">{short_version}</p>
        </div>
        <div class="reveal bento-cell bento-3">
          <p class="eyebrow">No obligation</p>
          <p class="mt-3 text-slate">{no_obligation}</p>
        </div>
        <div class="reveal bento-cell bento-cell-tint bento-3">
          <p class="eyebrow">Stopping contact</p>
          <p class="mt-3 text-slate">{stopping_contact}</p>
        </div>
      </div>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------------------
# T4: THE INFORMATIONAL / CLUSTER TEMPLATE
# Thirteen P2 cluster pages share one top and one mid-page CTA. Both were being
# copied out of term_rates.py by hand, which is how a breadcrumb and an H1 drift
# apart across a silo. Authored once here instead.
# ---------------------------------------------------------------------------
def page_hero(trail, h1, lead, extra="", glow=True, pb="pb-10", media=None):
    """T4's top: breadcrumb, one H1, and the direct answer in the first two
    sentences.

    `lead` is HTML rather than text because it carries the mandated up-link to
    the silo hub (spec s07 rule 1: first 150 words, exact anchor = the hub
    term). Putting it in the lead is the only placement that satisfies both the
    word count and "answer the question first".

    glow=False on every final expense page: `.fe main` opts out of the ambient
    glow along with the rest of the motion layer.
    """
    g = " glow" if glow else ""
    ex = ("\n      " + extra) if extra else ""
    copy = f"""<h1 class="reveal text-h1">{h1}</h1>
      <p class="reveal mt-5 text-lead text-slate">{lead}</p>{ex}"""
    if media:
        # The hero photograph is the page's one eager image, so the block splits
        # rather than sitting under the lead: the same 6 / 5-from-8 split the
        # home hero already uses.
        block = f"""<div class="mt-8 grid lg:grid-cols-12 gap-10 lg:gap-8 items-center">
      <div class="lg:col-span-6">
        {copy}
      </div>
      <div class="lg:col-span-5 lg:col-start-8">{media}</div>
    </div>"""
    else:
        block = f"""<div class="mt-8 max-w-3xl">
      {copy}
    </div>"""
    return f"""
<section class="pt-6 {pb}{g}">
  <div class="container-ax">
    {crumbs(trail)}

    {block}
  </div>
</section>"""


def inline_cta(heading, body, where, href, cta_label, phone_first=False,
               cls="section-tight band", fe=False, note=None):
    """T4's single mid-page CTA. One ask, offered two ways, never an interstitial.

    `phone_first` decides which of the two carries the amber, per the per-silo
    CTA weighting: term and whole life lead with the form, final expense and the
    two senior spokes lead with the phone. Exactly one of these per
    informational page, so the reader meets the ask once rather than being
    interrupted by it.
    """
    if phone_first:
        primary = phone_link(where, "btn btn-call btn-block" + (" btn-xl" if fe else ""),
                             "Call " + PHONE_DISPLAY, 26 if fe else 20)
        secondary = ('<a class="btn btn-ghost btn-block mt-3" href="%s">%s</a>'
                     % (href, cta_label))
    else:
        primary = '<a class="btn btn-cta btn-block" href="%s">%s</a>' % (href, cta_label)
        secondary = phone_link(where, "btn btn-ghost btn-block mt-3",
                               "Or call " + PHONE_DISPLAY)
    return f"""<section class="{cls}">
  <div class="container-ax">
    <div class="reveal card">
      <div class="grid lg:grid-cols-12 gap-8 lg:gap-10 items-center">
        <div class="lg:col-span-7">
          <h2 class="text-h3 !font-display !font-semibold">{heading}</h2>
          <p class="mt-3 text-slate">{body}</p>
        </div>
        <div class="lg:col-span-4 lg:col-start-9">
          {primary}
          {secondary}
          <p class="mt-3 text-micro text-muted text-center">{note or HOURS}</p>
        </div>
      </div>
    </div>
  </div>
</section>"""


def byline_section(cls="section-tight band"):
    """The byline in its own band. Every editorial page ends with this."""
    return f"""<section class="{cls}">
  <div class="container-ax">
    <div class="reveal">{byline()}</div>
  </div>
</section>"""


def prose(heading, blocks, intro=None, cls="section", aside=None, media=None, sticky=True):
    """A structured explainer section: heading and optional lead on the left,
    the substance on the right. The two column split is what keeps a long
    informational page off a single centred column, which section 7 bans.

    `blocks` is finished HTML for the right hand column.

    `media` is finished HTML, normally a figure(), placed under the lead. It is
    what stops a short left column leaving a dead half row beside a long right
    one, which MASTER.md section 3 forbids.

    `sticky` parks the left column against the header while the right column
    scrolls, which solves the same dead row where a photograph would sit beside
    a rate table and section 8 bans one. It needs no final expense branching:
    `.fe main .sticky-col` is already `position: static`, so an fe page takes
    the static column and the image without a second code path.

    Sticky only travels if the grid item is full height, so the rail goes on an
    inner div and the grid drops `items-start`. `.sticky-col` on the grid item
    itself under `items-start` is content height and never moves.
    """
    lead = ('<p class="reveal mt-5 text-slate">%s</p>' % intro) if intro else ""
    side = ('<div class="reveal mt-6 pt-6 border-t border-rule">%s</div>' % aside) if aside else ""
    art = ('<div class="reveal mt-8">%s</div>' % media) if media else ""
    inner = f"""<h2 class="reveal text-h2">{heading}</h2>
        {lead}
        {art}
        {side}"""
    if sticky:
        col = '<div class="sticky-col">%s</div>' % inner
        align = ""
    else:
        col = inner
        align = " items-start"
    return f"""<section class="{cls}">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8{align}">
      <div class="lg:col-span-5">
        {col}
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        {blocks}
      </div>
    </div>
  </div>
</section>"""


def qa(question, answer, cls=""):
    """One heading-and-paragraph pair inside a prose() right column. Used where
    a page absorbs a secondary search intent as an H3 rather than a page."""
    return f"""<div class="reveal {cls}">
        <h3 class="text-h4">{question}</h3>
        <p class="mt-3 text-slate">{answer}</p>
      </div>"""
