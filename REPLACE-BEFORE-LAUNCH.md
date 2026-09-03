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
| `FOUNDED` | `[YEAR]` | Year the agency was founded. Shown on `/about/`. Same honesty rule as `YEARS`. |
| `CARRIERS` | `[X]` | Number of carriers with a current, signed appointment. Not carriers in progress. |
| `STREET` / `CITY` / `REGION` / `POSTCODE` | `[STREET ADDRESS]` etc. | The principal office address. Feeds both `/about/` and the `InsuranceAgency` schema, which now read the same constants. |
| `AGENT_SLUG` | `first-last` | URL slug of the agent profile every byline's `Person` node points at. Must match a built profile module. |

Also in `chrome.py`:
- **`org_schema()` postal address** now reads the `STREET` / `CITY` / `REGION` / `POSTCODE`
  constants above, so the address is written once and used by both the schema and `/about/`.
- **`state_options()`** currently lists all 50 states plus DC. Trim it to the states the agency is
  actually licensed in. Offering a state you cannot write in wastes the visitor's time and yours.
- **`person_schema()`** carries a credential stub. Add real licence numbers and years licensed.
  Its `@id` is now `/about/agents/<AGENT_SLUG>/#person`, so every byline's author node resolves to
  a real profile page rather than to the index.

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

The site displays no carrier marks, and no placeholder slots for them. Do not add a carrier logo,
name, or mark to any page until that appointment is active **and** that carrier's brand guidelines
have been checked. The footer's "appointed with multiple carriers" language makes no named or
numeric claim and is fine as-is.

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

---

## 4c. The P0 placeholder tables

Three tables ship as structure with placeholder rows. Each renders a visible `.flag` **above** the
table, so a reader meets the notice before the numbers. Populate them from real records and delete
every row you do not use: a row left in place asserts something untrue.

| Page | Table | Fill from | Marked |
|---|---|---|---|
| `/about/licensing/` | State, agency licence number, type, lines | The agency's current licence records | `[PLACEHOLDER LICENCE TABLE]` |
| `/about/carriers/` | Carrier, appointed for, states | Signed, current carrier appointments only | `[PLACEHOLDER CARRIER LIST]` |
| `/about/agents/first-last/` | State, agent licence number, type, lines | Each agent's own producer licences | `[PLACEHOLDER LICENCE NUMBERS]` |

Also placeholder in the P0 layer:

- **`/about/agents/`** ships three identical placeholder agent cards, marked
  `[PLACEHOLDER ROSTER]` on the page. Replace with the real roster: one card and one profile module
  per licensed agent. Never ship a roster larger than the licensed team.
- **`/about/agents/first-last/`** is a template, marked `[PLACEHOLDER AGENT PROFILE]`. Copy
  `tools/pages/about_agent_profile.py` per agent, change the `AGENT` dict, give each a unique slug,
  and add each module to `PAGES` in `tools/build.py`.
- **`/about/`** carries `FOUNDED`, `NPN`, and the office address in a definition list, flagged as a
  block. Its three trust figures use `count=False` so a placeholder never animates.
- **`/get-a-quote/`** carries a fourth `$--` rate table, subject to section 2 above. It is
  deliberately **not** gated behind the form.
- **No carrier logos anywhere.** Removed sitewide in commit `5fa6bfc`: a carrier mark implies an
  affiliation and an endorsement that an appointment does not grant. Carrier names in text only.

## 5. Reviews

The testimonial slot on the home page is designed, wired, and **hidden**. It is marked
`[REAL ATTRIBUTABLE REVIEWS ONLY - DO NOT FABRICATE]`. To use it, populate `data-reviews-list` and
remove the `hidden` attribute. Zero invented testimonials ship.

`/about/reviews/` is the same decision at page scale. It ships with a real designed empty state and
two hidden slots (`data-reviews-aggregate`, `data-reviews-slot`) ready for a Google Business
Profile feed. **Its `schema()` deliberately emits no `AggregateRating` and no `Review` nodes.** Add
them only when there is a real rating and a real count: an aggregate rating over zero reviews is a
fabricated review expressed in structured data, and it is the form search engines penalise hardest.

---

## 6. Placeholder links

These do not exist yet. All are in the spoke modules, the footer, or contextual body links.

- `/compare/term-vs-whole-life-insurance/`
- 11 term spokes, 9 whole life spokes, 9 final expense spokes

`python3 tools/check.py` crawls every internal link in the built output and fails on anything
broken that is **not** on this list, so removing a line here is how a page graduates.

**Built in the P0 layer** (previously on this list): `/about/`, `/about/agents/`,
`/about/agents/first-last/`, `/about/licensing/`, `/about/carriers/`, `/about/reviews/`,
`/get-a-quote/`, `/legal/privacy/`, `/legal/terms/`, `/legal/disclaimer/`, `/404.html`.

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
- **`/thank-you/`** is `noindex` and now carries the "what to have ready" block and routes back to
  all three hubs. Forms render a designed success state **in place**; that was a deliberate choice,
  and `/get-a-quote/`'s success panel links on to `/thank-you/` rather than redirecting. If you do
  switch to a redirect, point it here and note that the in-place panel is what GA4's `form_submit`
  currently fires against.
- **Header CTA.** "Get a Free Quote" in the header and the mobile panel points at `/get-a-quote/`,
  not `/contact/`. The nav itself is still hubs plus Contact only (spec section 07 rule 6).
- **`/404.html`** is written to the site root, which Netlify, Cloudflare Pages, and GitHub Pages all
  pick up without configuration. On a host that expects something else, re-point `OUT` in
  `tools/pages/not_found.py`.
- **Legal copy** in all three `/legal/` documents is template text carrying a visible
  `[PENDING LEGAL REVIEW]` flag. It is structurally complete, covering TCPA consent, carrier
  sharing, and CCPA / state privacy rights, but the wording is not counsel-approved. The governing
  law, arbitration, and limitation-of-liability sections are explicitly left for counsel to draft.
- **Motion.** `MOTION_INTENSITY` is 5: IntersectionObserver reveal, 40ms bento stagger, count-up
  on spec figures (`[data-count]`, final value already in the HTML), chart draw-in. No scroll-linked
  layer and no animation library. The final-expense page is deliberately exempt from every one of
  these for accessibility reasons documented in MASTER.md section 4. If a future edit adds motion
  there, that exemption is the thing being overridden, not a styling preference.
- **Count-up figures.** Only spec figures carry `data-count` (10/15/20/30 years, $2,000,000,
  40 years, 15 minutes). When `STATES` and `YEARS` get real values, do **not** add `data-count` to
  them without checking the number is one you are happy to see animate on a trust page.
- **Fonts.** Space Grotesk (variable 300 to 700) and Inter (variable) are self-hosted latin subsets
  in `assets/fonts/`, both under the SIL Open Font License, fetched once from Google Fonts. No
  runtime request leaves the domain for type.

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

**Layout rule, enforced by test.** A block may be narrow only if something else occupies the rest
of its row. One 768px card in a 1200px container with 432px of nothing beside it is a defect, not
whitespace. The audit fails any section that leaves more than 20% of its content row empty on the
right, or any two-column row whose columns differ in height by more than 250px. Run it before
shipping a layout change.
