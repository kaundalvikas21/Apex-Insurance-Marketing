# Deploying the preview

**This site is not cleared to launch.** `REPLACE-BEFORE-LAUNCH.md` is not empty, the TCPA consent
is `[PENDING LEGAL REVIEW]`, `PHONE_DISPLAY` is a fictional number, every rate cell is `$--`, and
`submitLead()` in `assets/site.js` still discards what a visitor types. So the only deploy this
config supports is a **private preview**: password-gated, `noindex`, forms inert.

Everything here is committed and unused until someone creates a Netlify site. Nothing is live.

## What the config does

| File | Job |
|---|---|
| `netlify.toml` | Build command `python3 tools/stage.py`, publish `dist`, edge function on `/*` |
| `tools/stage.py` | Copies the site surface into `dist/`. An allowlist, so `public/`, `tools/`, `design-system/`, `src/` and every `.md` stay out of the deploy |
| `netlify/edge-functions/preview-auth.ts` | HTTP Basic Auth. Netlify's own site password needs a paid plan; this is the free-tier equivalent |
| `netlify/_headers` | `X-Robots-Tag: noindex, nofollow, noarchive` on everything |
| `netlify/robots.txt` | `Disallow: /` |

Nothing is generated at deploy time. Every `.html`, `assets/site.css` and image is committed, so
`stage.py` copies rather than builds. If pages changed, run `python3 tools/build.py` and
`npm run build:css` and commit the output first, exactly as now.

`stage.py` asserts on its own output: no `.md`, `.py` or `.cjs` reaches `dist/`, and
`index.html` and `assets/site.css` must be present. A broken allowlist fails the build instead of
publishing quietly.

## Setting it up, once

1. Netlify: **Add new site → Import an existing project → GitHub →**
   `kaundalvikas21/Apex-Insurance-Marketing`.
2. Set **branch to deploy** to `build/marketing-site-v3-transparent-numbers`. It is not `main`.
3. Leave build command and publish directory **blank**. `netlify.toml` supplies both.
4. **Site configuration → Environment variables**, add two:
   - `PREVIEW_USER`
   - `PREVIEW_PASSWORD`

   Choose the password yourself. Send it to the client separately from the link, and never commit
   it. With either variable missing the edge function denies every request, so a half-finished
   setup keeps the site shut rather than opening it.

## Checking the deploy

Replace `<site>` and the credentials:

```bash
curl -sI https://<site>/                                  # 401
curl -sI -u user:pass https://<site>/ | grep -i robots    # x-robots-tag: noindex, nofollow, noarchive
curl -u  user:pass https://<site>/robots.txt              # Disallow: /

# each of these must be 404
for p in REPLACE-BEFORE-LAUNCH.md CLAUDE.md tools/chrome.py \
         public/coverage_hero/Term_Life_hero.png assets/img/CREDITS.md; do
  printf '%s %s\n' "$p" "$(curl -s -o /dev/null -w '%{http_code}' -u user:pass https://<site>/$p)"
done
```

Then open the home page, a hub and a form page in a browser and confirm the CSS, fonts, images and
the multi-step form work from the CDN.

## Before a real launch, undo all of this

- Delete `netlify/edge-functions/preview-auth.ts` and the `[[edge_functions]]` block, and remove
  `PREVIEW_USER` / `PREVIEW_PASSWORD`.
- Replace `netlify/robots.txt` with an allow rule and a `Sitemap:` line.
- Drop `X-Robots-Tag` from `netlify/_headers`.
- Empty `REPLACE-BEFORE-LAUNCH.md` first. That file's own rule is "Do not publish until this file
  is empty", and it covers the phone number, the licence numbers, all 12 rate tables, the legal
  documents and the CRM wiring.
- Settle two things this config cannot: the **photo licence** (`[CONFIRM LICENCE]`, and note the
  originals in `public/` are in the repo and on GitHub even though they never reach the deploy),
  and whether **forms** should post anywhere, which is a question for counsel before it is a
  question for code.
- Point the domain at the site. Every canonical, `og:url` and JSON-LD `@id` hard-codes
  `https://www.apexinsurancemarketing.com` via `chrome.DOMAIN`, so the live host has to match it or
  that constant has to change.
