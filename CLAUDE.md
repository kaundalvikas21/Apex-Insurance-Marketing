# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## The one thing to know first

**Never edit a `.html` file.** Every `.html` in this repo is generated output, committed as the
deliverable. Editing one is silently reverted by the next build. A page is a **Python module** in
`tools/pages/`.

Likewise, **never edit `assets/site.css`** — it is minified Tailwind output built from
`src/input.css`.

## Commands

```bash
python3 tools/build.py                  # assemble every page in PAGES -> committed .html
python3 tools/build.py term_rates       # assemble ONE page (fastest inner loop)
npm run build:css                       # src/input.css -> assets/site.css (minified)
npm run dev:css                         # same, watching
python3 tools/check.py                  # the test suite. Run after every build.
npm run serve                           # python3 -m http.server 8080
python3 tools/images.py --fetch         # idempotent; downloads any missing image derivative
npm run build                           # images --fetch + build.py + build:css
```

Normal loop after changing anything in `tools/` or `src/`:

```bash
python3 tools/build.py && npm run build:css && python3 tools/check.py
```

There is no test framework and no linter. `tools/check.py` is the test suite: it crawls the built
HTML and asserts the compliance and structural contract. It must print `all checks passed`, except
for `link to X but no such page is built` failures naming pages genuinely not written yet.

`node --check assets/site.js` is the only syntax check for the JS.

## Architecture

### The assembler

`tools/build.py` holds the entire `<head>`/`<body>` template as one string. For each name in its
`PAGES` list it imports `tools/pages/<name>.py`, calls `mod.body()` and `mod.schema()`, and writes
`mod.OUT`. The template exists so the header, footer, and legal boilerplate are authored once
rather than twenty-seven times.

A page module must define:

```python
PATH   = "/term-life-insurance/rates/"          # canonical path; key into images.OG_FOR_PAGE
OUT    = "term-life-insurance/rates/index.html"
ACTIVE = "/term-life-insurance/"                # which nav item gets aria-current
SILO   = "term-life"                            # -> <body data-silo>, feeds every GA4 event
TITLE  = "..."
DESC   = "..."
def schema(): return [C.org_schema(), C.breadcrumbs([...]), ...]   # list of dicts -> JSON-LD
def body():   return "...html..."
```

Optional: `OG_TITLE`, `ROBOTS`, `HTML_CLASS` (`"fe"` switches the whole page to the senior
accessibility mode).

Adding a page = write the module + add its name to `PAGES` in `tools/build.py` + add its `PATH` to
`OG_FOR_PAGE` in `tools/images.py`. **Omitting the `OG_FOR_PAGE` entry raises `KeyError` at build
time.** Only reuse an OG slot that has a real `assets/img/og-<slot>.jpg` on disk.

### The shared layer

- `tools/chrome.py` — every shared partial and **every placeholder constant** (`PHONE_DISPLAY`,
  `AGENT_NAME`, `RATES_DATE`, `NPN`, `SLA`, …). One address for the launch swap. Provides
  `header`, `footer`, `crumbs`, `byline`, `acc`/`faq_section`, `spoke_module`, `step`, `stat`,
  `banner`, `picture`/`figure`, `legal_doc`, `flag`/`rates_flag`, `state_options`,
  `rate_chart`, `post_submit_section`, `no_obligation_section`, and the schema builders
  (`org_schema`, `breadcrumbs`, `faq_schema`, `person_schema`, `jsonld`).
- `tools/forms.py` — form primitives. The compliance-critical parts (hidden `source_url`/`silo`/
  `form_name`, honeypot, TCPA consent block) are authored once here so a copy cannot drift.
  Every helper takes `indent`, the column its block sits at in the caller's f-string.
- `tools/icons.py` — inlined Lucide paths. A name not in the dict is a build-time `KeyError`.
  Copy path data verbatim from lucide-static.
- `tools/images.py` — the image manifest and `OG_FOR_PAGE`. The Unsplash CDN does the resizing, so
  there is no sharp/Pillow dependency.

### The behaviour layer

`assets/site.js` is one vanilla IIFE, no dependencies, loaded `defer`. Everything is progressive
enhancement: every page is readable and every link works with this file blocked.

It binds by **data attribute at parse time and never re-scans**, so markup injected later is not
picked up (the delegated `call_click` handler on `document` is the exception). Rather than writing
new JS, check whether one of these contracts already covers what you need:

| Contract | Does |
|---|---|
| `[data-ax-form]` | Fills the hidden fields, blur validation, TCPA gate, honeypot, GA4, success panel |
| `[data-steps]` + `[data-step]` + `[data-step-next/back]` | Multi-step forms; `[data-step-branch]`/`[data-step-for]` add branching via `fieldset.disabled` |
| `[data-prefill]` (JSON) + `data-prefill-target` | Writes values into a form by field name, fires `form_start`, scrolls, jumps to the first empty field. **Read at click time**, so the attribute can be rewritten at runtime |
| `[data-panels]` + `[data-panel]` | One checked radio shows one panel; `[data-panel-caption]` auto-writes "Showing female, 20 years." |
| `.reveal`, `[data-stagger]`, `[data-count]` | IntersectionObserver reveal, stagger, count-up |
| `[data-calc]` + `data-calc-field`/`-out`/`-cta` | The coverage calculator (section 10) |

`submitLead()` is the single CRM integration point, marked `>>> WIRE TO CRM ENDPOINT HERE <<<`.
It currently `console.log`s and resolves. Validators available via `data-validate`: `email`,
`phone`, `age` (18–85), `ageSenior` (50–85), `name`.

Set `window.AX_DEBUG = true` in the console to log every GA4 event. Events: `form_start`,
`form_submit`, `call_click`, `calculator_complete`, `triage_complete`. **Never put PII or personal
financial detail in an event payload.**

### The design system

`design-system/MASTER.md` is the source of truth for tokens, type, grid, motion, and component
contracts. `src/input.css` implements it. **If the two disagree, MASTER.md is right and
`input.css` gets fixed, not the other way around.** `design-system/pages/*.md` record per-page
deviations only, and exist only for pages that actually deviate.

`REPLACE-BEFORE-LAUNCH.md` is the launch register: every placeholder, and the list of internal
links pointing at pages not yet built. It is meant to be edited in the same commit as
`tools/check.py`'s `UNBUILT` set.

## Enforced rules (these fail the build or the check)

- **No em-dash anywhere in rendered copy.** `tools/build.py` fails with a line number, entity forms
  included. Use a comma, colon, period, or middot.
- **Amber (`--color-gold`) appears in exactly 3 CSS rules** — `.btn-cta`, `.btn-cta:hover`,
  `.skip-link`. `check.py` counts them. Adding a fourth fails the check.
- **Exactly one TCPA `[data-consent]` per form**, never pre-ticked, immediately above submit; and
  the hidden `source_url` / `silo` / `form_name` / `company_website` fields must be present. Always
  emit them with `forms.scaffold()` and `forms.consent_block()`.
- **Radio `name` must be unique per branch** in a branching form. `validateRadioGroup()` queries
  the whole form by name, so a shared name attaches the error to the wrong (possibly hidden)
  fieldset.
- Self-canonical, exactly one `<h1>`, and a visible `.crumbs` plus `BreadcrumbList` on every page
  below root.
- No emoji; Lucide inline SVG only.
- Every internal link must resolve, unless the path is listed in `check.py`'s `UNBUILT` set.
  Deleting a line from that set is how a page graduates.

## Content rules (YMYL insurance site; these are deliberate, not oversights)

- **Rate and cost cells are `$--`.** No invented premium, even a marked one, because a marked fake
  number still gets screenshotted. Rate tables get their weight from structure and type. Always put
  `chrome.rates_flag()` above the table and a dated "Rates last updated" pill beneath.
- No invented rates, reviews, carrier names, dollar claims, or agent photographs. Placeholders
  render **visibly on the page** via `chrome.flag()`, not only in an HTML comment, because the
  person who has to replace one is usually looking at the page.
- `chrome.stat(..., count=False)` for any placeholder figure. Count-up is only for real spec
  figures, never a `[X]` or a rate.
- Calculators and rate tables are **never** email-gated.
- Legal and TCPA copy is `[PENDING LEGAL REVIEW]` and says so on the page.

## Internal linking

1. Every spoke links **up** to its hub once in the first 150 words, exact anchor = the hub term
   ("term life insurance"), never "click here".
2. Spokes link sideways only within their own silo; cross-silo movement only via `/compare/` or the
   hubs.
3. One link per target per page. This is why the footer deliberately omits the hub links and
   `/contact/` (they are in the nav), and why contextual teasers deep-link to a section anchor when
   the spoke module already owns the canonical link.
4. Global nav stays hubs + Contact. Do not add spokes.
5. Money pages should receive more internal links than they send.

The breadcrumb link to a hub plus the mandated first-150-words hub link is the one accepted
duplicate: both are required, one by `check.py` and one by the linking rules.

## Gotchas that cost real time

- **f-string braces.** Page `body()` methods are one big f-string. Inside a `{...}` replacement
  field the content is plain Python, so a dict literal is written `{"age": mid}`, **not** `{{...}}`
  — the doubled form builds a `set` of `dict` and raises `unhashable type`.
- **`.reveal` goes ON the `.table-scroll` element**, never on a wrapper around it. A transformed
  wrapper leaks the table's width into the page until the section reveals.
- **`<details name=...>` accordion groups must be unique per page**, or two FAQ sets close each
  other. `chrome.acc()` takes the group as an argument for this reason.
- `.rate-table` has `min-width: 40rem`. A narrow table needs an inline
  `style="min-width:26rem"` override, which is the existing house workaround.
- `collect()` uses `input.matches(':disabled')`, not `.disabled`, so controls inside a
  `<fieldset disabled>` are correctly skipped. Do not "fix" this.
- `.field-error` holds an icon plus a `<span>`; JS writes into the span so the icon survives.
- Calculator-style inputs must sit **outside** any `<form>`, or `collect()` validates them and
  `FormData` posts them to the CRM.
- `<html class="fe">` (final expense) rescopes the type ramp on `main`, not `html`, so the shared
  header and footer stay at sitewide scale. That mode is static: no count-up, no row cascade, no
  lift, no glow. It is an accessibility decision, not a style one.

## Other agent configs

A Codex config exists at `~/.codex`. To pull anything from it into Claude Code, reply `/import` to
scan and list what is importable, then `/import --yes=<digest>` to apply it. Do not read those
files directly.
