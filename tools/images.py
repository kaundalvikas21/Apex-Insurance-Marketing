# -*- coding: utf-8 -*-
"""Image manifest and downloader.

Art direction (design-system/MASTER.md section 8): documentary, no eye contact
with the camera, no posed joy. These are environmental photographs. None of them
depicts a customer, an agent, or a claim, and nothing on the site is captioned
to suggest otherwise.

Source: Unsplash. The Unsplash Licence permits commercial use and does not
require attribution. Every file is downloaded and served locally; nothing
hotlinks to the CDN at runtime.

The CDN does the resizing and encoding for us, so this project needs no
sharp / ImageMagick / Pillow dependency:

    https://images.unsplash.com/photo-<id>?w=<w>&h=<h>&fit=crop&fm=<avif|webp>&q=<q>

Run:  python3 tools/images.py --fetch
"""
import os
import sys
import urllib.request

CDN = "https://images.unsplash.com/photo-%s?w=%d&h=%d&fit=crop&crop=%s&fm=%s&q=%d"
OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")
FORMATS = ("avif", "webp")

# name -> (unsplash id, aspect w:h, [widths], crop anchor, alt text)
# Alt text describes what is literally shown. It never implies the person is a
# client, an agent, or connected to a policy.
IMAGES = {
    # 4:3 with a centre crop is the only framing that keeps all three people.
    # Entropy and a portrait ratio both cut the grandfather out entirely.
    "home-hero": (
        "1761839258803-21515f43190c", (4, 3), [480, 800, 1200], "center",
        "An older man and two children preparing food together at a kitchen counter."),
    # Hands over spread paperwork, shot dark. The comparison work this section
    # describes, and dark enough that the scrim has an easy job.
    # Fetched but not placed in Variation 3: the independence band has no photo under its text.
    "home-independence": (
        "1635859890085-ec8cb5466806", (3, 2), [640, 1024, 1440], "center",
        ""),  # decorative: sits behind copy in the navy band
    # Sits beside the copy about mortgages and children at home, so it is
    # doing work rather than decorating a gap. 3:2, not a 21:9 band.
    "term-home": (
        "1760229090663-fe14715d4efe", (3, 2), [520, 800, 1100], "center",
        "A two storey house behind mature trees."),
    "term-underwriting": (
        "1631815584191-0ed1723f0ead", (4, 3), [520, 800, 1100], "center",
        "A blood pressure cuff being fitted to someone's upper arm during a routine check."),
    "whole-permanence": (
        "1601041597271-71988152f98b", (3, 2), [640, 1024, 1440], "center",
        "The front porch and door of an older brick house."),
    "whole-acceptance": (
        "1624889229800-7ca4c6c0d52b", (16, 9), [480, 760, 1040], "center",
        ""),  # decorative: chairs outside a house at dusk
    "fe-quiet": (
        "1762126242240-cafa01fb1351", (3, 2), [640, 1024, 1440], "center",
        "A person sitting in an armchair looking out through a large window."),
    "fe-hands": (
        "1775049728396-d641f91f6c62", (16, 9), [640, 1024, 1440], "center",
        "An older person's hands resting one over the other."),
    # --- Mid-page banner bands (21:9). CRO: these are conversion re-asks, not
    # heroes. Each reuses a photo that appears on no other section of the same
    # page, so nothing repeats within one scroll.
    "term-band": (
        "1635859890085-ec8cb5466806", (21, 9), [800, 1440, 1920], "center",
        ""),  # decorative: hands over spread paperwork, sits behind band copy
    "whole-band": (
        "1761839258803-21515f43190c", (21, 9), [800, 1440, 1920], "center",
        ""),  # decorative: an older man and two children at a kitchen counter
    "fe-band": (
        "1631651693480-97f1132e333d", (21, 9), [800, 1440, 1920], "center",
        ""),  # decorative: a pen and printed forms on a wooden table
    "contact-desk": (
        "1631651693480-97f1132e333d", (3, 2), [560, 900, 1240], "center",
        "A pen and printed forms laid out on a wooden table."),

    # --- VISUAL_DENSITY 7 -------------------------------------------------
    # Fourteen slots added so every page carries photography rather than five.
    # Same art direction as above and no relaxation of it: no eye contact, no
    # posed joy, nobody who could be read as a client or an agent. Every one of
    # these was viewed before its alt text was written, and the alt describes
    # only what is literally in the frame.
    #
    # None of the fourteen contains a person. That is deliberate rather than
    # incidental: these pages carry death benefits and health questions, and a
    # stranger's face beside that copy is exactly what section 7 rules 1 and 2
    # exist to prevent. Rooms, tables, paths and doors carry the same warmth
    # and make no claim about anybody.

    # Term. Desks and daylight: term is the silo people research at a table.
    "term-desk": (
        "1776161562542-e8bc41b3b78a", (4, 3), [520, 800, 1100], "center",
        "A notepad, a pen, reading glasses, and binder clips on a wooden desk."),
    "term-window": (
        "1527377761-f99968ed8a7f", (3, 2), [520, 800, 1100], "center",
        "Window light falling across a carpeted floor beside a wooden shutter."),
    "term-table": (
        "1614597445336-8a67e9314d91", (4, 3), [520, 800, 1100], "center",
        "A kitchen island with stools, seen past a dining table."),
    "term-notebook": (
        "1620287920810-3f5b9746380c", (3, 2), [520, 800, 1100], "center",
        "A closed journal and a pen resting on an open ruled notebook."),

    # Whole life. Thresholds and things that stay put, because the product's
    # whole claim is permanence.
    "whole-ledger": (
        "1772396867158-e26d9e6256b2", (3, 2), [520, 800, 1100], "center",
        "An open notebook with handwriting and a pen on a dark wooden table."),
    "whole-arbor": (
        "1563714193017-5a5fb60bc02b", (4, 3), [520, 800, 1100], "center",
        "A brick path leading through a vine covered wooden arbour into a garden."),
    "whole-porch": (
        "1590165609277-12902bf83876", (4, 3), [520, 800, 1100], "center",
        "Two rocking chairs on the porch of a white clapboard house."),

    # Final expense. Quiet, domestic, and never funereal. The register is calm
    # rather than sombre: this silo's readers are being sold fear elsewhere.
    "fe-chairs": (
        "1765073505002-bd37f69b20ff", (4, 3), [520, 800, 1100], "center",
        "Two wooden chairs on a timber porch in late afternoon light."),
    "fe-kitchen": (
        "1609210885099-6ba41569c6dc", (4, 3), [520, 800, 1100], "center",
        "Hydrangeas in a glass jug on a kitchen worktop."),
    "fe-letters": (
        "1637597384611-0c33cef6ec03", (3, 2), [520, 800, 1100], "center",
        "Several handwritten postcards laid overlapping on a dark surface."),
    "fe-garden-door": (
        "1544137171-9f5cf7b0fafa", (4, 3), [520, 800, 1100], "center",
        "Wooden double doors on a white garden building, with roses on either side."),
    "fe-path": (
        "1579847621287-31060b612d1d", (3, 2), [520, 800, 1100], "center",
        "A garden path between frosted borders on a winter morning."),

    # Neutral. The compare pages belong to no silo, and /about/ is not a
    # product page, so neither takes a silo's photograph.
    "compare-garden": (
        "1713383658268-6b9bd03beb19", (4, 3), [520, 800, 1100], "center",
        "A tree and clipped shrubs in a green garden."),
    "about-desk": (
        "1761322572550-967ea8c0bfd9", (3, 2), [520, 800, 1100], "center",
        "An open blank notebook, a pen, and two pencils on a wooden desk."),
}

# Open Graph share image per page: which manifest entry to use.
OG_FOR_PAGE = {
    "/": "home-hero",
    "/term-life-insurance/": "term-home",
    "/whole-life-insurance/": "whole-permanence",
    "/final-expense-insurance/": "fe-quiet",
    "/contact/": "contact-desk",
    "/thank-you/": "contact-desk",
    # P0 layer. These pages reuse the existing set rather than adding photography:
    # an about or legal page has no documentary photograph to earn, and a share
    # card is not a reason to fetch one.
    "/get-a-quote/": "contact-desk",
    "/about/": "home-hero",
    "/about/agents/": "contact-desk",
    "/about/agents/first-last/": "contact-desk",
    "/about/licensing/": "contact-desk",
    "/about/carriers/": "contact-desk",
    "/about/reviews/": "contact-desk",
    "/legal/privacy/": "contact-desk",
    "/legal/terms/": "contact-desk",
    "/legal/disclaimer/": "contact-desk",
    "/404.html": "home-hero",
    # P1 money pages. They reuse the existing set: MASTER.md section 8 fixes
    # the photography at Variation 1's, and a share card is not a reason to
    # fetch a tenth photograph.
    "/term-life-insurance/quotes/": "term-home",
    "/term-life-insurance/rates/": "term-home",
    "/term-life-insurance/calculator/": "term-home",
    "/whole-life-insurance/quotes/": "whole-permanence",
    "/whole-life-insurance/rates/": "whole-permanence",
    "/whole-life-insurance/guaranteed-acceptance/": "whole-permanence",
    "/final-expense-insurance/burial-insurance/": "fe-quiet",
    "/final-expense-insurance/quotes/": "fe-quiet",
    "/final-expense-insurance/cost/": "fe-quiet",
    "/compare/term-vs-whole-life-insurance/": "home-hero",
    # P2 cluster pages. Same reasoning as P1: the photography set is fixed at
    # Variation 1's, so each silo's cluster shares its hub's share card.
    "/term-life-insurance/what-is-term-life-insurance/": "term-home",
    "/term-life-insurance/for-seniors/": "term-home",
    "/term-life-insurance/level-term/": "term-home",
    "/term-life-insurance/20-year-term/": "term-home",
    "/term-life-insurance/30-year-term/": "term-home",
    "/term-life-insurance/no-medical-exam/": "term-home",
    "/whole-life-insurance/what-is-whole-life-insurance/": "whole-permanence",
    "/whole-life-insurance/calculator/": "whole-permanence",
    "/whole-life-insurance/for-seniors/": "whole-permanence",
    "/whole-life-insurance/cash-value/": "whole-permanence",
    "/final-expense-insurance/for-seniors/": "fe-quiet",
    "/final-expense-insurance/no-waiting-period/": "fe-quiet",
    "/final-expense-insurance/funeral-insurance/": "fe-quiet",
    # P3 support pages. Same reasoning again: the photography set is fixed at
    # Variation 1's, so each page shares its silo's share card. The two compare
    # pages are neutral and take the home card rather than either silo's.
    "/term-life-insurance/10-year-term/": "term-home",
    "/term-life-insurance/return-of-premium/": "term-home",
    "/whole-life-insurance/dividends/": "whole-permanence",
    "/whole-life-insurance/is-it-worth-it/": "whole-permanence",
    "/final-expense-insurance/what-is-final-expense-insurance/": "fe-quiet",
    "/final-expense-insurance/for-parents/": "fe-quiet",
    "/final-expense-insurance/cremation-insurance/": "fe-quiet",
    "/compare/whole-life-vs-universal-life/": "home-hero",
    "/compare/burial-insurance-vs-life-insurance/": "home-hero",
}
OG_SIZE = (1200, 630)


def height_for(name, width):
    aw, ah = IMAGES[name][1]
    return round(width * ah / aw)


def variants(name):
    """[(width, height, fmt, filename)] for every derivative of one image."""
    _id, _ratio, widths, _crop, _alt = IMAGES[name]
    out = []
    for w in widths:
        for fmt in FORMATS:
            out.append((w, height_for(name, w), fmt, "%s-%d.%s" % (name, w, fmt)))
    return out


def fetch():
    os.makedirs(OUT_DIR, exist_ok=True)
    credits = ["# Image credits and licensing", "",
               "Every file here was downloaded from Unsplash and is served locally. Nothing on the",
               "site hotlinks to the Unsplash CDN.", "",
               "The Unsplash Licence grants a free, irrevocable, worldwide, non-exclusive right to",
               "use these photographs commercially without permission or attribution. It does not",
               "permit compiling them to build a competing service, and it does not transfer any",
               "release for identifiable people or trademarks visible in a photograph.", "",
               "**Before launch**, confirm with counsel that a model release is not required for the",
               "images showing identifiable people, or replace them with owned or Getty/Stocksy",
               "licensed photography. See REPLACE-BEFORE-LAUNCH.md.", "",
               "| Slot | Unsplash photo | Aspect | Widths | Alt text |",
               "|---|---|---|---|---|"]

    total = 0
    for name in IMAGES:
        pid, (aw, ah), widths, crop, alt = IMAGES[name]
        for w, h, fmt, fname in variants(name):
            url = CDN % (pid, w, h, crop, fmt, 72)
            path = os.path.join(OUT_DIR, fname)
            if os.path.exists(path):
                total += os.path.getsize(path)
                continue
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            with open(path, "wb") as f:
                f.write(data)
            total += len(data)
            print("  %-34s %6.1f KB" % (fname, len(data) / 1024.0))

        credits.append("| `%s` | [photo-%s](https://images.unsplash.com/photo-%s) | %d:%d | %s | %s |"
                       % (name, pid, pid, aw, ah, ", ".join(str(w) for w in widths),
                          alt or "_decorative, empty alt_"))

    # Open Graph derivatives.
    credits += ["", "## Open Graph", "", "Each page's share card reuses the slot below at 1200x630.", "",
                "| Page | Slot |", "|---|---|"]
    for page, name in OG_FOR_PAGE.items():
        pid = IMAGES[name][0]
        fname = "og-%s.jpg" % name
        path = os.path.join(OUT_DIR, fname)
        if not os.path.exists(path):
            url = CDN % (pid, OG_SIZE[0], OG_SIZE[1], "center", "jpg", 76)
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            with open(path, "wb") as f:
                f.write(data)
            total += len(data)
            print("  %-34s %6.1f KB" % (fname, len(data) / 1024.0))
        credits.append("| `%s` | `%s` |" % (page, name))

    with open(os.path.join(OUT_DIR, "CREDITS.md"), "w") as f:
        f.write("\n".join(credits) + "\n")

    print("\n  %d files, %.1f MB on disk" % (len(os.listdir(OUT_DIR)) - 1, total / 1048576.0))


if __name__ == "__main__":
    if "--fetch" in sys.argv:
        fetch()
    else:
        print(__doc__)
