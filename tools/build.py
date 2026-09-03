#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembles the static HTML pages from tools/pages/*.py.

The committed .html files are the deliverable. This script exists so the
header, footer, and legal boilerplate are authored once instead of six times.
Run it after editing anything in tools/, then run the CSS build.

    python3 tools/build.py && npm run build:css
"""
import importlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "pages"))

import chrome  # noqa: E402
import images  # noqa: E402

PAGES = [
    # The five approved pages, plus the P0 trust and conversion layer (spec s06).
    "home", "final_expense", "term", "whole", "contact",
    "get_a_quote", "thank_you",
    "about", "about_agents", "about_agent_profile",
    "about_licensing", "about_carriers", "about_reviews",
    "legal_privacy", "legal_terms", "legal_disclaimer",
    "not_found",
    # P1 money pages (spec s02/s03/s04 spokes plus the neutral compare page).
    "term_quotes", "term_rates", "term_calculator",
    "whole_quotes", "whole_rates", "whole_guaranteed_acceptance",
    "fe_burial_insurance", "fe_quotes", "fe_cost",
    "compare_term_vs_whole",
    # P2 cluster pages (spec s02/s03/s04 informational spokes, template T4,
    # plus the whole life calculator on T3).
    "term_what_is", "term_for_seniors", "term_level",
    "term_20_year", "term_30_year", "term_no_exam",
    "whole_what_is", "whole_calculator", "whole_for_seniors", "whole_cash_value",
    "fe_for_seniors", "fe_no_waiting_period", "fe_funeral_insurance",
    # P3 support pages (spec s02/s03/s04 objection and E-E-A-T spokes, template
    # T4, plus the two neutral compare pages on T5).
    "term_10_year", "term_rop",
    "whole_dividends", "whole_worth_it",
    "fe_what_is", "fe_for_parents", "fe_cremation",
    "compare_whole_vs_ul", "compare_burial_vs_life",
]

# Paths kept out of sitemap.xml. A noindex page does not belong in a sitemap,
# and /compare/whole-life-vs-universal-life/ is held back by a spec condition:
# it is published only once UL carrier appointments are confirmed. Removing a
# line here is how a page enters the sitemap.
SITEMAP_EXCLUDE = frozenset([
    "/compare/whole-life-vs-universal-life/",   # [CONFIRM UL APPOINTMENTS, spec s05]
])


TEMPLATE = """<!doctype html>
<html lang="en"{html_class}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{domain}{path}">
{robots}<meta name="theme-color" content="#0B3B8C">

<script>document.documentElement.className += " js";</script>

<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/space-grotesk-300-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Apex Insurance Marketing">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{domain}{path}">
<meta property="og:image" content="{domain}{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{og_title}">
<meta name="twitter:card" content="summary_large_image">

{schema}
</head>
<body{silo_attr}>

{header}

<main id="main">
{body}
</main>

{footer}

<script src="/assets/site.js" defer></script>
</body>
</html>
"""


def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def build(name):
    mod = importlib.import_module(name)
    html_class = getattr(mod, "HTML_CLASS", "")
    robots = getattr(mod, "ROBOTS", None)
    silo = getattr(mod, "SILO", "")

    out = TEMPLATE.format(
        html_class=(' class="%s"' % html_class) if html_class else "",
        title=esc(mod.TITLE),
        desc=esc(mod.DESC),
        og_title=esc(getattr(mod, "OG_TITLE", mod.TITLE)),
        domain=chrome.DOMAIN,
        path=mod.PATH,
        og_image="/assets/img/og-%s.jpg" % images.OG_FOR_PAGE[mod.PATH],
        robots=('<meta name="robots" content="%s">\n' % robots) if robots else "",
        schema=chrome.jsonld(*mod.schema()),
        silo_attr=(' data-silo="%s"' % silo) if silo else "",
        header=chrome.header(getattr(mod, "ACTIVE", mod.PATH)),
        body=mod.body(),
        footer=chrome.footer(),
    )

    # Guardrail: em-dash is banned in rendered copy (design-system MASTER.md s7).
    for bad in ("\u2014", "&#8212;", "&mdash;"):
        if bad in out:
            line = out[:out.index(bad)].count("\n") + 1
            raise SystemExit("BUILD FAILED: em-dash (%s) in %s near line %d"
                             % (bad, mod.OUT, line))

    target = os.path.join(ROOT, mod.OUT)
    os.makedirs(os.path.dirname(target), exist_ok=True) if os.path.dirname(target) else None
    with open(target, "w", encoding="utf-8") as f:
        f.write(out)
    return mod.OUT, len(out)


def sitemap():
    """Every indexable built page, one <url> each.

    A page is excluded if it carries a noindex ROBOTS value (/thank-you/, the
    404) or if its path is in SITEMAP_EXCLUDE. Nothing else is filtered: a page
    that is built and indexable belongs here.
    """
    urls = []
    for name in PAGES:
        try:
            mod = importlib.import_module(name)
        except ModuleNotFoundError:
            continue
        if "noindex" in (getattr(mod, "ROBOTS", "") or ""):
            continue
        if mod.PATH in SITEMAP_EXCLUDE or mod.PATH.endswith(".html"):
            continue
        urls.append("  <url><loc>%s%s</loc></url>" % (chrome.DOMAIN, mod.PATH))

    doc = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(urls) + "\n</urlset>\n")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(doc)
    return len(urls)


if __name__ == "__main__":
    wanted = sys.argv[1:] or PAGES
    for name in wanted:
        try:
            path, size = build(name)
        except ModuleNotFoundError:
            print("  skip   %s (not written yet)" % name)
            continue
        print("  build  %-46s %6.1f KB" % (path, size / 1024.0))

    if not sys.argv[1:]:
        print("\n  sitemap.xml    %d urls" % sitemap())
