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

BRAND = "Apex Insurance Marketing, LLC"

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
def picture(name, sizes, cls="", img_cls="", eager=False, ratio_cls="", alt=None):
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


RATIO_CLASS = {(4, 5): "media-tall", (3, 2): "media-wide", (21, 9): "media-band",
               (16, 9): "media-strip", (4, 3): "media-square-ish"}


def figure(name, sizes, caption=None, cls="", eager=False):
    """Editorial image block. Static frame with a plate-edge hairline; the
    page-level motion in this variation is reveal, stack, and marquee."""
    ratio = RATIO_CLASS[images.IMAGES[name][1]]
    motion = "media " + ratio
    cap = ('<figcaption class="mt-3 text-micro text-muted">%s</figcaption>' % caption) if caption else ""
    return ('<figure class="%s">%s%s</figure>'
            % (cls, picture(name, sizes, cls=motion, img_cls="media-img", eager=eager), cap))


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

      <a href="/" class="shrink-0 rounded-[2px]" aria-label="{BRAND}, home">
        <span class="wordmark">Apex</span>
        <span class="wordmark-sub">Insurance Marketing</span>
      </a>

      <nav class="hidden lg:flex items-center gap-4 xl:gap-7 ml-5 xl:ml-10" aria-label="Primary">
        {links}
      </nav>

      <div class="ml-auto flex items-center gap-2 sm:gap-3">
        <!-- Click-to-call is present at every desktop width. Below 1280 the
             number itself does not fit beside four product-name nav links,
             so the label shortens rather than the CTA disappearing. -->
        {phone_link("header", "hidden lg:inline-flex xl:hidden items-center gap-2 min-h-[48px] px-2 text-ink text-sm font-semibold whitespace-nowrap rounded-[2px] hover:text-navy transition-colors", "Call")}
        {phone_link("header", "hidden xl:inline-flex items-center gap-2 min-h-[48px] px-2 text-ink text-sm font-semibold whitespace-nowrap rounded-[2px] hover:text-navy transition-colors")}
        <a href="/contact/" class="btn btn-cta hidden sm:inline-flex !text-sm !px-5" data-magnetic>Get a Free Quote</a>
        <a href="tel:{PHONE_TEL}" data-cta-location="header_mobile"
           class="lg:hidden inline-flex items-center justify-center w-12 h-12 text-ink rounded-[2px]">
          <span class="sr-only">Call {PHONE_DISPLAY}</span>
          {icon("phone", 24)}
        </a>
        <button type="button" data-nav-toggle aria-expanded="false" aria-controls="site-nav"
                class="lg:hidden inline-flex items-center justify-center w-12 h-12 -mr-2 text-ink rounded-[2px]">
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
        <a href="/contact/" class="btn btn-cta btn-block">Get a Free Quote</a>
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

    return f"""<footer class="site-footer on-navy">
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
      <div class="lg:col-span-3">{col("Legal", legal)}</div>
    </div>

    <div class="mt-14 pt-8 border-t border-white/15 grid gap-4 text-micro leading-relaxed text-white/80 max-w-4xl">
      <!-- [PENDING LEGAL REVIEW] license disclosure wording -->
      <p>
        {BRAND} is a licensed independent insurance agency. Licensed in {STATES} states.
        National Producer Number {NPN}. Agency license numbers by state are listed on our
        <a class="link-static" href="/about/licensing/">licensing page</a>.
      </p>
      <p>
        {BRAND} is not affiliated with, endorsed by, or sponsored by any government agency,
        including the Social Security Administration, Medicare, or the Department of Veterans Affairs.
      </p>
      <p>
        Policies are issued by third party insurance carriers. Coverage, availability, premiums,
        riders, and benefits vary by carrier, state, age, and health. All guarantees are subject to
        the claims paying ability of the issuing carrier. Content on this site is general
        information, not insurance, tax, or legal advice, and is not an offer of coverage.
      </p>
      <p>&#169; 2026 {BRAND}. All rights reserved.</p>
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
                    "streetAddress": "[STREET ADDRESS]",
                    "addressLocality": "[CITY]",
                    "addressRegion": "[STATE]",
                    "postalCode": "[ZIP]",
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
    """Person stub for the agent byline. Fill in before launch."""
    return {
        "@context": "https://schema.org",
        "@type": "Person",
        "@id": DOMAIN + "/about/agents/#agent",
        "name": AGENT_NAME,
        "jobTitle": AGENT_TITLE,
        "url": DOMAIN + "/about/agents/",
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
    for i, (name, path) in enumerate(trail):
        if i:
            parts.append(sep)
        if path:
            parts.append('<a href="%s">%s</a>' % (path, name))
        else:
            parts.append('<span aria-current="page">%s</span>' % name)
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
    return f"""<div class="card" id="byline">
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


def spoke_module(heading, intro, spokes):
    """Visible in-page module linking DOWN to every spoke in the silo.
    spokes: [(href, anchor_text, one_line_description)]"""
    items = "".join(f"""
        <li class="reveal">
          <a href="{href}" class="tile">
            <span class="flex items-start justify-between gap-3">
              <span class="text-h4 text-ink">{text}</span>
              <span class="tile-arrow shrink-0 mt-1 text-ink">{icon("arrow-right", 18)}</span>
            </span>
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


def rates_flag(what):
    """Visible placeholder notice for any rate component. Rule 6."""
    return (f'<p class="flag">[PLACEHOLDER: REPLACE WITH APPOINTED CARRIER RATE CARDS, DATED] '
            f'The {what} below are structural placeholders. No premium shown here is a real, quoted, '
            f'or offered rate. Populate from current carrier rate cards and update the date line '
            f'before this page goes live.</p>')


# ---------------------------------------------------------------------------
# VARIATION 4 COMPONENTS
# ---------------------------------------------------------------------------
def eyebrow(text, cls=""):
    """Uppercase micro-label. Names the topic; never numbers the section."""
    return '<span class="eyebrow %s">%s</span>' % (cls, text)


def step(n, title, body, note=None):
    """Numbered step. Copy-preserving seam for stacks and flat step rows."""
    extra = ('<p class="mt-3 text-sm text-muted">%s</p>' % note) if note else ""
    return f"""<div class="reveal flex items-start gap-5">
      <span class="step-num tnum" aria-hidden="true">{n}</span>
      <div class="min-w-0">
        <h3 class="text-h4 !font-sans">{title}</h3>
        <p class="mt-3 text-slate">{body}</p>
        {extra}
      </div>
    </div>"""


def stack(steps):
    """Sticky-stack storytelling. steps: [(title, body, note|None), ...].

    Card i is pinned while card i+1 arrives; it scales and dims on card
    i+1's view timeline because a stuck element's own timeline stalls.
    The timeline names are inline so the `animation` shorthand in the
    stylesheet cannot reset them. Without animation-timeline support the
    cards simply overlap, which still reads as a deck. Under reduced motion
    and inside .fe main the cards are a plain list.
    """
    n = len(steps)
    scope = ", ".join("--stack-%d" % i for i in range(1, n + 1))
    cards = []
    for i, (title, body, note) in enumerate(steps, 1):
        tl = "--stack-i:%d;view-timeline-name:--stack-%d;" % (i - 1, i)
        if i < n:
            tl += "animation-timeline:--stack-%d;" % (i + 1)
        extra = ('<p class="mt-4 text-sm text-muted measure-tight">%s</p>' % note) if note else ""
        cards.append(f"""
      <li class="stack-card" style="{tl}">
        <div class="grid gap-6 md:grid-cols-12 md:gap-8 items-start">
          <div class="md:col-span-3"><span class="stack-num tnum" aria-hidden="true">{i:02d}</span>
            <span class="sr-only">Step {i}</span></div>
          <div class="md:col-span-9 col-rule">
            <h3 class="text-h3">{title}</h3>
            <p class="mt-5 text-lead text-slate measure-tight">{body}</p>
            {extra}
          </div>
        </div>
      </li>""")
    return '<ol class="stack" style="timeline-scope:%s">%s\n    </ol>' % (scope, "".join(cards))


def marquee(static=False):
    """Carrier logo strip. Exactly one marquee per page; pausable; a static
    wrapped row under reduced motion and on the senior page."""
    # [PLACEHOLDER: CARRIER LOGOS] Do not display a carrier mark until the
    # appointment with that carrier is active and the mark is licensed for
    # use. Six slots, unlabeled on purpose.
    slots = "".join('<div class="logo-slot">Carrier logo<br>[placeholder]</div>' for _ in range(6))
    cls = "marquee marquee-static" if static else "marquee"
    toggle = "" if static else f"""
      <button type="button" class="marquee-toggle" data-marquee-toggle aria-pressed="false">
        <span class="sr-only">Pause carrier logo animation</span>
        <span class="ico-pause">{icon("pause", 18)}</span><span class="ico-play">{icon("play", 18)}</span>
      </button>"""
    return f"""<div class="{cls}" data-marquee aria-label="Appointed carriers">
      <div class="marquee-track">
        <div class="marquee-group">{slots}</div>
        <div class="marquee-group" aria-hidden="true">{slots}</div>
      </div>{toggle}
    </div>"""


def byline_compact():
    """Byline near the top of every hub. Links to the full block in-page so
    /about/agents/ is still linked exactly once per page."""
    return (f'<a class="link-static" href="#byline">Written by {AGENT_NAME}, {AGENT_TITLE}</a>'
            f'<span class="text-muted"> &#183; Reviewed {REVIEW_DATE}</span>')


def rail(byline=True, static_marquee=False):
    """Above-the-fold trust rail: licensing line, independence statement,
    years in business, byline, carrier strip. Sits under every hero CTA."""
    by = f'<p class="mt-4 text-sm">{byline_compact()}</p>' if byline else ""
    return f"""<div class="rail">
      <div class="rail-items">
        <span>{icon("shield-check", 18, "shrink-0 mt-0.5 text-ink")}<span>Licensed in <strong>{STATES} states</strong> &#183; NPN {NPN}</span></span>
        <span>{icon("scale", 18, "shrink-0 mt-0.5 text-ink")}<span><strong>Independent.</strong> We work for you, not one carrier.</span></span>
        <span>{icon("building", 18, "shrink-0 mt-0.5 text-ink")}<span><strong>{YEARS} years</strong> placing policies</span></span>
      </div>
      {by}
      <div class="mt-5">{marquee(static=static_marquee)}</div>
    </div>"""
