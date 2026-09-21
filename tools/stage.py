"""Copy the site surface into dist/ for hosting. Everything else stays behind.

The deploy is an allowlist, not a blocklist: a blocklist leaks whatever it forgets,
while a missing allowlist entry breaks a page visibly. The repo root holds things
that must never be served, notably public/ (client hero originals, licence
unconfirmed, referenced by no page), tools/, design-system/ and every .md,
including the launch register. A host serves .md and .py as static files.

    python3 tools/stage.py        # -> dist/

Nothing is generated here. Every .html, assets/site.css and image is committed, so
this is a copy, not a build. Run tools/build.py first if pages changed.
"""
import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "dist")
SKIP = {"dist", "node_modules", ".git", "_proof", "tools", "src", "public",
        "design-system", ".claude", ".agents", "__pycache__"}
# Host control files live under netlify/ in the repo and at the root of the deploy.
CONTROL = "netlify"


def pages(start):
    """Every directory under start that holds an index.html, walked from the root."""
    found = []
    for path, dirs, files in os.walk(start):
        dirs[:] = [d for d in dirs if d not in SKIP and not d.startswith(".")]
        if "index.html" in files and path != start:
            found.append(os.path.relpath(path, start))
            dirs[:] = []          # the whole tree comes with it
    return found


def copy(rel):
    src, dst = os.path.join(ROOT, rel), os.path.join(OUT, rel)
    if os.path.isdir(src):
        shutil.copytree(src, dst)
    else:
        os.makedirs(os.path.dirname(dst) or OUT, exist_ok=True)
        shutil.copy2(src, dst)
    return rel


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    copied = [copy("assets")]
    for name in sorted(os.listdir(ROOT)):
        if name.endswith(".html") or name == "sitemap.xml":
            copied.append(copy(name))
    for page in sorted(pages(ROOT)):
        copied.append(copy(page))
    for name in sorted(os.listdir(os.path.join(ROOT, CONTROL))):
        if name != "edge-functions":
            copied.append(copy(os.path.join(CONTROL, name)))
            shutil.move(os.path.join(OUT, CONTROL, name), os.path.join(OUT, name))
    shutil.rmtree(os.path.join(OUT, CONTROL), ignore_errors=True)

    # assets/img/CREDITS.md is the Unsplash licence record, for us and not for visitors.
    for path, _, files in os.walk(OUT):
        for name in files:
            if name.endswith((".md", ".py", ".cjs")):
                os.remove(os.path.join(path, name))

    html = sum(len([f for f in fs if f.endswith(".html")]) for _, _, fs in os.walk(OUT))
    assert os.path.exists(os.path.join(OUT, "index.html")), "no index.html in dist"
    assert os.path.exists(os.path.join(OUT, "assets", "site.css")), "no site.css in dist"
    leaked = [os.path.relpath(os.path.join(p, f), OUT)
              for p, _, fs in os.walk(OUT) for f in fs
              if f.endswith((".md", ".py", ".cjs"))]
    assert not leaked, "these do not belong in a deploy: %s" % leaked

    print("  dist/         %d entries, %d html pages" % (len(copied), html))
    for rel in copied:
        print("    %s" % rel)


if __name__ == "__main__":
    main()
