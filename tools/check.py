#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pre-launch checks over the BUILT html. No dependencies, no browser.

Run after tools/build.py. It asserts the things a reviewer would otherwise
have to click through, and the structural contract assets/site.js relies on:

  forms      hidden source_url / silo / form_name, honeypot, exactly one TCPA
             consent per form, and a success panel that actually exists
  branching  every data-step-for names a real product option, and no radio
             name is reused across two branches (site.js validates a radio
             group by querying the whole form, so a shared name would attach
             the error to whichever fieldset came first in the DOM, possibly
             a hidden one)
  seo        self-canonical, one h1, visible breadcrumb plus BreadcrumbList on
             every page below root
  links      every internal href resolves to a file that exists
  compliance no em-dash, no emoji, amber confined to its three CSS rules

    python3 tools/build.py && python3 tools/check.py
"""
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://www.apexinsurancemarketing.com"

# Spokes and compare pages are not built yet. The hubs link down to them on
# purpose, so those links are expected to be dead until the spoke phase.
# REPLACE-BEFORE-LAUNCH.md section 6 is the register. Anything NOT matching
# this is a genuine broken link and fails the check.
UNBUILT = re.compile(r"^/(compare/"
                     r"|term-life-insurance/.+"
                     r"|whole-life-insurance/.+"
                     r"|final-expense-insurance/.+)")

problems = []
notes = []


def fail(page, msg):
    problems.append("%s: %s" % (page, msg))


class Forms(HTMLParser):
    """Collects each <form data-ax-form> with its inputs and fieldsets."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.forms = []
        self.stack = []          # open fieldsets, innermost last
        self.cur = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "form" and "data-ax-form" in a:
            self.cur = {"attrs": a, "inputs": [], "steps": [], "consents": 0}
            self.forms.append(self.cur)
        elif tag == "fieldset" and self.cur is not None:
            step = {"attrs": a, "names": set()}
            self.cur["steps"].append(step)
            self.stack.append(step)
        elif tag in ("input", "select", "textarea") and self.cur is not None:
            self.cur["inputs"].append(a)
            if "data-consent" in a:
                self.cur["consents"] += 1
            if a.get("type") == "radio" and self.stack:
                self.stack[-1]["names"].add(a.get("name"))

    def handle_endtag(self, tag):
        if tag == "fieldset" and self.stack:
            self.stack.pop()
        elif tag == "form":
            self.cur = None
            self.stack = []


def check_page(rel, html, built):
    page = rel

    # --- head -------------------------------------------------------------
    canon = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    if not canon:
        fail(page, "no canonical")
    path = "/" + rel.replace("index.html", "")
    if rel == "404.html":
        path = "/404.html"
    if canon and canon.group(1) != DOMAIN + path:
        fail(page, "canonical %s does not self-reference %s" % (canon.group(1), path))

    h1 = re.findall(r"<h1[ >]", html)
    if len(h1) != 1:
        fail(page, "expected exactly 1 <h1>, found %d" % len(h1))

    # --- breadcrumbs ------------------------------------------------------
    root_or_utility = path in ("/", "/404.html", "/thank-you/")
    visible = 'class="crumbs"' in html
    listed = "BreadcrumbList" in html
    if root_or_utility:
        if visible or listed:
            notes.append("%s: has breadcrumbs; root and utility pages normally omit them" % page)
    else:
        if not visible:
            fail(page, "no visible breadcrumb")
        if not listed:
            fail(page, "no BreadcrumbList schema")

    # --- schema parses ----------------------------------------------------
    for blob in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            json.loads(blob)
        except ValueError as e:
            fail(page, "invalid JSON-LD: %s" % e)

    # --- banned -----------------------------------------------------------
    for bad in ("—", "&mdash;"):
        if bad in html:
            fail(page, "em-dash present")
    if re.search(r"[\U0001F300-\U0001FAFF☀-➿]", html):
        fail(page, "emoji in markup; Lucide SVG only")

    # --- forms ------------------------------------------------------------
    p = Forms()
    p.feed(html)
    for form in p.forms:
        fid = form["attrs"].get("id") or form["attrs"].get("data-form-name", "?")
        names = [i.get("name") for i in form["inputs"]]
        for required in ("source_url", "silo", "form_name", "company_website"):
            if required not in names:
                fail(page, "form %s missing hidden field %s" % (fid, required))
        if form["consents"] != 1:
            fail(page, "form %s has %d TCPA consent boxes, expected exactly 1"
                 % (fid, form["consents"]))
        for i in form["inputs"]:
            if "data-consent" in i and "checked" in i:
                fail(page, "form %s ships a pre-ticked consent box" % fid)
        target = form["attrs"].get("data-success-target")
        if target and ('id="%s"' % target) not in html:
            fail(page, "form %s success target #%s does not exist" % (fid, target))

        # --- branching ----------------------------------------------------
        branches = {i.get("value") for i in form["inputs"] if "data-step-branch" in i}
        owned = [s for s in form["steps"] if s["attrs"].get("data-step-for")]
        if owned and not branches:
            fail(page, "form %s has data-step-for but no data-step-branch control" % fid)
        for s in owned:
            owner = s["attrs"]["data-step-for"]
            if owner not in branches:
                fail(page, "form %s: data-step-for=%r matches no product option" % (fid, owner))
        seen = {}
        for s in owned:
            for n in s["names"]:
                if n in seen and seen[n] != s["attrs"]["data-step-for"]:
                    fail(page, "form %s: radio name %r used in two branches (%s and %s); "
                               "validateRadioGroup would target the wrong fieldset"
                         % (fid, n, seen[n], s["attrs"]["data-step-for"]))
                seen[n] = s["attrs"]["data-step-for"]
        if branches:
            segs = html.count("data-progress-seg")
            shared = len([s for s in form["steps"]
                          if "data-step" in s["attrs"] and not s["attrs"].get("data-step-for")])
            per = {}
            for s in owned:
                per[s["attrs"]["data-step-for"]] = per.get(s["attrs"]["data-step-for"], 0) + 1
            longest = shared + (max(per.values()) if per else 0)
            if segs < longest:
                fail(page, "form %s: %d progress segments for a %d step branch"
                     % (fid, segs, longest))

    # --- internal links ---------------------------------------------------
    for href in set(re.findall(r'href="(/[^"#?]*)', html)):
        if href.startswith("/assets/"):
            continue
        if UNBUILT.match(href):
            continue
        target = href.lstrip("/")
        candidates = [target, os.path.join(target, "index.html")]
        if not any(c in built for c in candidates):
            fail(page, "link to %s but no such page is built" % href)


def main():
    built = set()
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in
                       ("node_modules", ".git", "tools", "src", "design-system", "assets")]
        for f in filenames:
            if f.endswith(".html"):
                built.add(os.path.relpath(os.path.join(dirpath, f), ROOT).replace(os.sep, "/"))

    for rel in sorted(built):
        with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
            check_page(rel, fh.read(), built)

    css = os.path.join(ROOT, "assets", "site.css")
    if os.path.exists(css):
        n = open(css, encoding="utf-8").read().count("var(--color-gold")
        if n != 3:
            problems.append("site.css: amber appears in %d rules, must be exactly 3" % n)

    print("  checked %d pages" % len(built))
    for n in notes:
        print("  note   %s" % n)
    for p in problems:
        print("  FAIL   %s" % p)
    print("\n  %s" % ("%d problem(s)" % len(problems) if problems else "all checks passed"))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
