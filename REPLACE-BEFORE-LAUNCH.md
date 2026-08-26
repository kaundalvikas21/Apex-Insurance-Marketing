# Replace before launch

Nothing on this site invents a fact. Every unknown is a marked placeholder, and every placeholder
is listed here. **Do not publish until this file is empty.**

Most values live in exactly one place: **`tools/chrome.py`**, at the top under
`--- PLACEHOLDERS ---`. Change them there and run `python3 tools/build.py` to push the change
through all six pages.

---

## 1. Business facts (`tools/chrome.py`)

| Constant | Current placeholder | What it needs |
|---|---|---|
| `PHONE_DISPLAY` / `PHONE_TEL` | `(555) 018-0199` | The real tracked number. `555-01xx` is a reserved fictional range and will not connect. Appears in every click-to-call and in the schema. |
| `HOURS` | Mon to Fri 8am to 7pm CT, Sat 9am to 2pm CT | The hours a licensed agent actually answers. |
| `STATES` | `[X]` | Number of states the agency is licensed in. |
| `NPN` | `[NPN]` | National Producer Number. |
| `YEARS` | `[X]` | Years in business. If the honest answer is under three, cut the claim rather than round it up. |
| `AGENT_NAME` | `[Agent Name]` | The agent who reviews the pages. Byline and `Person` schema. |
| `REVIEW_DATE` | `[DATE]` | Date each hub was last reviewed. Print the real one and keep it current. |
| `RATES_DATE` | `[DATE]` | Date of the carrier rate cards the tables are built from. |
| `SLA` | `[X business hours]` | **[SET HONEST SLA]** The response time you can hold to on a Friday afternoon, not the best case. |
| `DOMAIN` | apexinsurancemarketing.com | The live domain. Feeds canonicals, Open Graph, and schema `@id`s. |

Also in `chrome.py`:
- **`org_schema()` postal address** is `[STREET ADDRESS]` / `[CITY]` / `[STATE]` / `[ZIP]`.
- **`state_options()`** currently lists all 50 states plus DC. Trim it to the states the agency is
  actually licensed in. Offering a state you cannot write in wastes the visitor's time and yours.
- **`person_schema()`** carries a credential stub. Add real licence numbers and years licensed.

---

## 2. Rate tables

Three tables ship with `$--` in every premium cell and a visible
`[PLACEHOLDER: REPLACE WITH APPOINTED CARRIER RATE CARDS, DATED]` banner above them.
**No invented premium appears anywhere on this site**, which is deliberate: a marked fake number
still gets screenshotted.

| Page | Component | Shape |
|---|---|---|
| `/term-life-insurance/#rates` | `rate_table()` in `tools/pages/term.py` | 7 age bands x 3 coverage columns. Toggles for term length, sex, tobacco. |
| `/final-expense-insurance/#costs` | `rate_table()` in `tools/pages/final_expense.py` | 7 age bands x 4 coverage columns. Toggle for sex. |
| `/whole-life-insurance/` cost section | inline in `tools/pages/whole.py` | Whole life against 20 year term at two ages. |

**Term table integration point.** The toggles currently update the caption only. There is a marked
comment in `term.py` where the dataset keyed by (term length, sex, tobacco, age band, coverage)
should drive the cell values. The final-expense table already swaps a full `<tbody>` per sex, so
copy that pattern once real data exists.

Also replace `[CARRIER RATE CARD NAME AND EDITION]` in the source line under each table.

---

## 3. Legal and compliance

- **TCPA consent wording** is marked `[PENDING LEGAL REVIEW]` in an HTML comment above all five
  consent blocks. Counsel must approve it and confirm it satisfies current one-to-one consent
  rules. The mechanics are already correct and enforced in code: separate checkbox, never
  pre-ticked, never bundled with another statement, sits immediately above the submit button, and
  submission is blocked until it is checked.
- **Footer licence disclosure** is marked `[PENDING LEGAL REVIEW]`. It currently states the agency
  is licensed, gives the state count and NPN, and links to `/about/licensing/`.
- The **government-affiliation disclaimer** and the **carrier / guarantees disclaimer** are in the
  footer on all six pages and are not placeholders, but should still be read by counsel.

---

## 4. Carrier logos

Two logo strips (`/` and `/term-life-insurance/`) render six dashed `Carrier logo N` slots.
Do not put a carrier mark on the site until the appointment is active **and** that carrier's brand
guidelines have been checked. Each strip carries a `[PLACEHOLDER ...]` comment.

## 4b. Photography

Nine photographs, all from Unsplash, all downloaded and served locally from `assets/img/`.
`assets/img/CREDITS.md` lists every file, its source, and its alt text. The manifest is
`tools/images.py`; `python3 tools/images.py --fetch` is idempotent.

**These are placeholders too.** Two things need doing before launch:

1. **Model releases.** The Unsplash Licence permits commercial use without attribution, but it does
   **not** convey a model release for identifiable people, and it does not clear trademarks visible
   in a frame. Five of the nine images show identifiable people:
   `home-hero`, `home-independence`, `term-underwriting`, `fe-quiet`, `fe-hands`.
   Have counsel confirm the exposure is acceptable for an insurance advertiser in your states, or
   replace them with owned or Getty/Stocksy licensed photography.
2. **They are stock.** Other sites use these exact frames. Commissioned photography of the real
   agency is the upgrade, and the layout will take it without changes as long as the aspect ratios
   in `tools/images.py` are preserved.

Art direction, if you are replacing them: documentary, no eye contact with the camera, no posed
joy. See `design-system/MASTER.md` section 8. The two rules with no exceptions:

- **No photograph of a person beside the agent byline.** That slot is a marked placeholder on every
  hub (`.avatar-slot`, "[REAL AGENT PHOTO REQUIRED]") and must be filled with a photograph of the
  actual named licensed agent or left as a placeholder. A stock face there presents a stranger as
  your agent.
- **No image captioned or positioned to imply the person shown is a customer.**

Open Graph share cards (`assets/img/og-*.jpg`) are derived from the same photographs and inherit
the same obligations.

## 5. Reviews

The testimonial slot on the home page is designed, wired, and **hidden**. It is marked
`[REAL ATTRIBUTABLE REVIEWS ONLY - DO NOT FABRICATE]`. To use it, populate `data-reviews-list` and
remove the `hidden` attribute. Zero invented testimonials ship.

---

## 6. Placeholder links

These do not exist yet. All are in the spoke modules, the footer, or contextual body links.

- `/about/`, `/about/agents/`, `/about/licensing/`
- `/legal/privacy/`, `/legal/terms/`, `/legal/disclaimer/`
- `/compare/term-vs-whole-life-insurance/`
- 11 term spokes, 9 whole life spokes, 9 final expense spokes

**Three contextual links point at section anchors on spoke pages that do not exist yet.** Create
these anchors when the spoke is built, or the link will land at the top of the page:

| Link on | Target |
|---|---|
| Term hub, no-exam teaser | `/term-life-insurance/no-medical-exam/#who-qualifies` |
| Whole life hub, dividends card | `/whole-life-insurance/dividends/#how-they-are-declared` |
| Whole life hub, guaranteed acceptance card | `/whole-life-insurance/guaranteed-acceptance/#who-it-is-for` |

Those anchors exist because spec section 07 allows one link per target per page: the spoke module
owns the canonical page link, so contextual teasers deep-link to the relevant section instead.
Same reason the home page triage results point at `#quote`, `#rates`, and `#costs`.

---

## 7. Wiring

- **CRM endpoint.** `assets/site.js` has a single integration point marked
  `>>> WIRE TO CRM ENDPOINT HERE <<<` in `submitLead()`. It currently logs the payload and resolves.
  Replace the body with a `fetch()` and keep the returned promise: the success state, the error
  state, and the `form_submit` event all hang off it. The payload already carries every answer plus
  `tcpa_consent`, `source_url`, `silo`, `form_name`, and `submitted_at`.
- **GA4.** Events fire into `window.dataLayer` with a guard, so nothing breaks without a container.
  Install GTM or gtag and map: `form_start`, `form_submit`, `call_click`, `triage_complete`.
  A `calculator_complete` stub is exposed as `window.axTrack('calculator_complete', {...})` for the
  calculator spokes.
  Note: `form_submit` deliberately carries **no personal data** into the dataLayer, only
  `form_name`, `silo`, `page_path`, and `source_url`. Keep it that way.
- **Consent / analytics.** Decide whether GA4 needs a consent banner in your states before adding it.
- **`/thank-you/`** is stubbed and `noindex`. Forms currently render a success state in place. If
  you switch to a redirect, point it here.
- **Motion.** `MOTION_INTENSITY` is 5. Scroll-driven effects use `animation-timeline: view()`
  behind `@supports`, and browsers without it fall back to the IntersectionObserver reveal, so
  nothing breaks and nothing is required. The final-expense page is deliberately exempt from every
  transform-based effect for accessibility reasons documented in MASTER.md section 4. If a future
  edit adds motion there, that exemption is the thing being overridden, not a styling preference.

---

## 8. Editing the site

```bash
python3 tools/images.py --fetch                          # download images (idempotent, skips existing)
python3 tools/build.py                                   # regenerate all six HTML pages
npx tailwindcss -i ./src/input.css -o ./assets/site.css --minify   # or: npm run build:css
```

The committed `.html` files are the deliverable. `tools/` exists so the header, footer, and legal
boilerplate are authored once instead of six times: edit `tools/chrome.py` or `tools/pages/*.py`,
then rebuild. The build fails if an em-dash reaches the rendered output.

Design tokens are documented in `design-system/MASTER.md` and implemented in `src/input.css`.
If the two ever disagree, MASTER.md is the spec.
