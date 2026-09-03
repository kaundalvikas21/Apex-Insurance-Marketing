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
