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

- **Logo** (`tools/logo.py`, "Summit"): designed in house on 2026-09-21 and **not checked against
  registered trademarks**. Commission a trademark search before launch. On the site the wordmark is
  live text in the self-hosted Space Grotesk, which is fine; for print, signage or anywhere the
  font is not available, the wordmark must first be converted to outlines by a designer.
- **Social profiles** (`SOCIAL` in `tools/chrome.py`): Facebook, LinkedIn, YouTube and Instagram
  icons sit in the footer on every page. Each URL is a `[...]` placeholder, and an icon only
  becomes a real link once its URL starts with `http`; until then it renders dimmed and inert, so
  no page can ship a link to a profile that does not exist. Replace the URLs, and delete the row
  for any network the agency does not use.

## 2. Rate tables

**Twelve** tables ship with `$--` in every premium cell and a visible
`[PLACEHOLDER: REPLACE WITH APPOINTED CARRIER RATE CARDS, DATED]` banner above them.
**No invented premium appears anywhere on this site**, which is deliberate: a marked fake number
still gets screenshotted.

| Page | Component | Shape |
|---|---|---|
| `/term-life-insurance/#rates` | `rate_table()` in `tools/pages/term.py` | 7 age bands x 3 coverage columns. Toggles for term length, sex, tobacco. |
| `/final-expense-insurance/#costs` | `rate_table()` in `tools/pages/final_expense.py` | 7 age bands x 2 coverage columns. Toggle for sex. |
| `/whole-life-insurance/` cost section | inline in `tools/pages/whole.py` | Whole life against 20 year term at two ages. |
| `/get-a-quote/` | inline | Sample rates, deliberately **not** gated behind the form. |
| `/term-life-insurance/quotes/` | `chrome.rate_chart()` | T1's sample table, shown before the form rather than after it. |
| `/term-life-insurance/rates/` | `chrome.rate_chart()` | 10 age bands x 5 coverage columns. Toggles for term length, sex, tobacco. Row-level prefill buttons. |
| `/whole-life-insurance/for-seniors/` | `chrome.rate_chart()` | 5 age bands x 3 coverage columns. Toggle for sex. Row-level **click-to-call**, because that page is phone weighted. |
| `/whole-life-insurance/quotes/` | `chrome.rate_chart()` | T1's sample table, shown below the form and not gated. 6 age bands x 4 coverage columns. Toggles for sex and tobacco. Row-level prefill buttons. |
| `/whole-life-insurance/rates/` | `chrome.rate_chart()` | 10 age bands x 5 coverage columns. Toggles for sex and tobacco. Row-level prefill buttons. Coverage columns must stay identical to `whole.quote_form()`'s coverage select. |
| `/whole-life-insurance/guaranteed-acceptance/` | `chrome.rate_chart()` | 7 age bands x 3 coverage columns. Toggle for sex, no tobacco split (the product does not ask). Row-level **click-to-call**. |
| `/final-expense-insurance/quotes/` | `chrome.rate_chart()` | T1's sample table, not gated. 6 age bands x 2 coverage columns. Row-level **click-to-call** inside the age cell, which is how the fe pages stay at three columns. |
| `/final-expense-insurance/cost/` | `chrome.rate_chart()` | The silo's canonical cost grid: 7 age bands x 2 coverage columns. Six built pages route their cost question here, so this is the one to populate first. Row-level **click-to-call**. |

**Integration point.** In every `chrome.rate_chart()` table the toggles currently update the
caption only, and there is a marked comment in `tools/chrome.py` where a dataset keyed by
(toggle state, age band, coverage) should drive the cell values. The final-expense table already
swaps a full `<tbody>` per sex, so copy that pattern once real data exists.

Also replace `[CARRIER RATE CARD NAME AND EDITION]` in the source line under each table.

### 2b. Placeholder tables that are not premiums

Four further tables are structural placeholders. The first two are about **availability** rather
than price; the last two are premium tables added in P3 and ARE covered by the rate card swap in
section 2, but are listed here because neither is a standard `chrome.rate_chart()` grid and so
neither will be caught by looking for one.

| Page | Table | Fill from | Marked |
|---|---|---|---|
| `/term-life-insurance/for-seniors/` | Term lengths commonly issued at ages 60 to 85 | The real issue age and term availability grid, by carrier and state | `[PLACEHOLDER: REPLACE WITH APPOINTED CARRIER ISSUE AGE GRID]` |
| `/whole-life-insurance/calculator/` | No table; the page states on its face that it cannot compute a premium or a cash value | Optional: a dated premium range once rate cards are loaded | `[PLACEHOLDER: NO CARRIER RATE CARDS LOADED]` |
| `/term-life-insurance/10-year-term/` | Renewal schedule: what the premium does in policy years 11 to 15 | The annually renewable term rate scale for the issue age, per carrier. Renewal provisions differ by carrier and state, and some policies do not renew at all | `[PLACEHOLDER: REPLACE WITH APPOINTED CARRIER RATE CARDS, DATED]` |
| `/term-life-insurance/return-of-premium/` | Standard 30 year term vs return of premium at the same death benefit: premium, total paid, refund, net cost | Both rate cards for the same issue age and class, plus the carrier's surrender schedule for the year 15 refund row | `[PLACEHOLDER: REPLACE WITH APPOINTED CARRIER RATE CARDS, DATED]` |

### 2c. Two flags that are deliberate and must NOT be "fixed"

- `/final-expense-insurance/funeral-insurance/` and `/final-expense-insurance/burial-insurance/` both
  carry `[NO AVERAGE PUBLISHED, ON PURPOSE]`. We do not print an average funeral or burial cost. Figures in this category are national survey averages that
  describe no particular funeral. Do not replace this with a number from a survey we cannot cite.
- `/whole-life-insurance/cash-value/` carries `[GENERAL INFORMATION ONLY]` over its tax section.
  That is a permanent caveat, not a placeholder. It stays after launch.

---

## 3. Legal and compliance

- **TCPA consent wording** is marked `[PENDING LEGAL REVIEW]` in an HTML comment above all five
  consent blocks. Counsel must approve it and confirm it satisfies current one-to-one consent
  rules. The mechanics are already correct and enforced in code: separate checkbox, never
  pre-ticked, never bundled with another statement, sits immediately above the submit button, and
  submission is blocked until it is checked.
- **Footer licence disclosure** is marked `[PENDING LEGAL REVIEW]`. It currently states the agency
  is licensed, gives the state count and NPN, and links to `/about/licensing/`.
- **Free policy review replacement warning** (`/free-policy-review/`, under "What your review
  covers") renders as a visible `[PENDING LEGAL REVIEW]` flag. State replacement rules differ, so
  counsel must approve the wording. The same page carries a sixth consent block (form
  `policy_review`, silo `site`) in its own two-step form (`free_policy_review.review_form()`).
  The "never cancel first" aside in "How we get paid" is a second flagged copy of the same rule.
- **Free policy review "many reviews end with keep" figure** (`/free-policy-review/`, "How we get
  paid"). Visible `[PLACEHOLDER]`: replace with a real measured ratio or delete the sentence. Do
  not estimate it.
- **Free policy review document upload** (`/free-policy-review/`, form step 2, visible `[DEV]`
  flag). A declarations page is personal information. Before launch it needs encryption at rest,
  a retention limit, privacy policy coverage, and a multipart CRM post: `site.js` sends only
  `has_attachment`, never the file or its name.
- **"Unbiased opinion" USP tile** (`/free-policy-review/`, the strip under the hero, added at the
  client's request September 2026). The sub-line is the page's own FAQ answer restated, "Many
  reviews end with: keep what you have", and the same page discloses that the carrier pays the
  commission (since September 2026 a full "How we get paid" section plus a "We will / We will
  not" pledge, from the client team's artifact). Counsel should read the tile and the disclosure together: an unbiased claim with
  nothing behind it is a compliance problem, not a copy preference.
- **Homepage popup copy** (`DIALOG` in `tools/pages/home.py`) says a review checks "that you are
  not overpaying". It promises no saving, but counsel should read it with the page above.
- The **government-affiliation disclaimer** and the **carrier / guarantees disclaimer** are in the
  footer on all six pages and are not placeholders, but should still be read by counsel.

---

## 4. Carrier logos

The site displays no carrier marks, and no placeholder slots for them. Do not add a carrier logo,
name, or mark to any page until that appointment is active **and** that carrier's brand guidelines
have been checked. The footer's "appointed with multiple carriers" language makes no named or
numeric claim and is fine as-is.

## 4b. Photography

- **`[CONFIRM LICENCE]` Hero banners.** `term-hero`, `whole-hero`, `fe-hero`, `home-banner`,
  `contact-banner` and `review-banner` were supplied by the client team on 2026-09-21 (`public/`), not pulled from Unsplash, so they are not in
  the credits table below. Confirm the licence covers commercial web use and, if they are
  AI-generated or stock with model releases, record which. They show identifiable people: they are
  lifestyle images and must never be captioned or implied to be Apex agents or clients. That matters
  most for `contact-banner`: a woman in a headset beside the heading "Talk to a licensed agent"
  reads as one of ours. Either confirm that is acceptable to compliance, or replace it with a
  photograph of a real, named Apex agent who has consented. The same question applies, less
  sharply, to `review-banner` (a woman in a blazer walking a man through a document).

Twenty six slots, all from Unsplash, all downloaded and served locally from `assets/img/`.
`assets/img/CREDITS.md` lists every file, its source, and its alt text. The manifest is
`tools/images.py`; `python3 tools/images.py --fetch` is idempotent.

Twelve slots are the original set. **Fourteen were added** when photography was extended from five
pages to twenty nine. Every one of the fourteen was viewed before its alt text was written, and
**none of them contains a person**, which keeps the clearance work below confined to the original
twelve.

**These are placeholders too.** Two things need doing before launch:

1. **Model releases.** The Unsplash Licence permits commercial use without attribution, but it does
   **not** convey a model release for identifiable people, and it does not clear trademarks visible
   in a frame. **Five slots show identifiable people, and all five are from the original twelve:**
   `home-hero`, `home-independence`, `term-underwriting`, `fe-quiet`, `fe-hands`.
   Have counsel confirm the exposure is acceptable for an insurance advertiser in your states, or
   replace them with owned or Getty/Stocksy licensed photography.

   The fourteen added slots (`term-desk`, `term-window`, `term-table`, `term-notebook`,
   `whole-ledger`, `whole-arbor`, `whole-porch`, `fe-chairs`, `fe-kitchen`, `fe-letters`,
   `fe-garden-door`, `fe-path`, `compare-garden`, `about-desk`) show rooms, tables, paths and
   doors. No faces, so no model release is in question for them. Check them for visible trademarks
   and for legible handwriting: `fe-letters` and `whole-ledger` both show writing, and it should be
   confirmed as illegible or replaced.
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

**Thirteen pages deliberately carry no photograph.** They are listed with their reasons in
`design-system/MASTER.md` section 8. Do not "finish the job" by adding images to them: each one is
either a form, a rate table, a testimonial page, the agent avatar slot, or a utility page.

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

### 5b. Client video testimonials (September 2026)

`chrome.testimonials()` renders three empty 9:16 `[data-video-slot]` frames with a visible
`[CLIENT VIDEO TESTIMONIALS PENDING]` flag, on every page except legal, 404, thank-you and
`/about/reviews/`. `chrome.byline_section()` now emits it plus the compact `author_line()`. To
launch, swap each slot for the `<video>` in the comment inside it, then remove the flag.

- **Captions are required** (`<track kind="captions">`), and a poster image, `preload="none"`.
- **FTC 16 CFR 255 and the 2024 fake-review rule.** If a person on screen is a paid creator,
  an actor, or anyone other than a real client describing their own experience, say so on
  screen. A real client who was paid or given anything must have that disclosed. UGC made to
  order is not a client testimonial unless the speaker is a client.
- No written quotes, names without consent, stars, or `Review`/`AggregateRating` schema.

---

## 6. Placeholder links

**None. Every internal link on the site resolves to a built page.** `check.py`'s `UNBUILT` set is
empty, which is what proves it: the crawl now fails on any broken internal link with nothing
exempted.

`python3 tools/check.py` crawls every internal link in the built output and fails on anything
broken that is **not** in its `UNBUILT` set. Adding a path to that set is how a link is allowed to
exist before its page does; removing it is how a page graduates. This section and that set are
meant to be edited in the same commit, in both directions.

**Built in the P0 layer** (previously on this list): `/about/`, `/about/agents/`,
`/about/agents/first-last/`, `/about/licensing/`, `/about/carriers/`, `/about/reviews/`,
`/get-a-quote/`, `/legal/privacy/`, `/legal/terms/`, `/legal/disclaimer/`, `/404.html`.

**Built in the P1 layer:** `/term-life-insurance/quotes/`, `/term-life-insurance/rates/`,
`/term-life-insurance/calculator/`, `/whole-life-insurance/quotes/`,
`/whole-life-insurance/rates/`, `/whole-life-insurance/guaranteed-acceptance/`,
`/final-expense-insurance/burial-insurance/`, `/final-expense-insurance/quotes/`,
`/final-expense-insurance/cost/`, `/compare/term-vs-whole-life-insurance/`.

**Built in the P2 layer:** `/term-life-insurance/what-is-term-life-insurance/`,
`/term-life-insurance/for-seniors/`, `/term-life-insurance/level-term/`,
`/term-life-insurance/20-year-term/`, `/term-life-insurance/30-year-term/`,
`/term-life-insurance/no-medical-exam/`,
`/whole-life-insurance/what-is-whole-life-insurance/`, `/whole-life-insurance/calculator/`,
`/whole-life-insurance/for-seniors/`, `/whole-life-insurance/cash-value/`,
`/final-expense-insurance/for-seniors/`, `/final-expense-insurance/no-waiting-period/`,
`/final-expense-insurance/funeral-insurance/`.

**Built in the P3 layer:** `/term-life-insurance/10-year-term/`,
`/term-life-insurance/return-of-premium/`, `/whole-life-insurance/dividends/`,
`/whole-life-insurance/is-it-worth-it/`,
`/final-expense-insurance/what-is-final-expense-insurance/`,
`/final-expense-insurance/for-parents/`, `/final-expense-insurance/cremation-insurance/`,
`/compare/whole-life-vs-universal-life/`, `/compare/burial-insurance-vs-life-insurance/`.

Two URLs differ from the P3 brief and match what the already-built pages link to, which is the
binding constraint: `/whole-life-insurance/is-it-worth-it/` (brief said
`is-whole-life-insurance-worth-it`) and `/final-expense-insurance/cremation-insurance/` (brief said
`cremation`). Five built pages already pointed at the shorter forms.

**No contextual link points at an anchor that does not exist.** The link crawl in `check.py`
strips the fragment, so it cannot catch a missing anchor: this section is the only guard, and any
new deep link must be added to the resolved list below in the commit that creates it.

Resolved in the P1 completion pass: the whole life hub's guaranteed acceptance card points at
`/whole-life-insurance/guaranteed-acceptance/#who-it-is-for`, and that anchor now exists as an
`sr-only` div immediately above the "Who it is for" section of the built page. Do not rename it.

Resolved in P3: the whole life hub's dividends card points at
`/whole-life-insurance/dividends/#how-they-are-declared`, and that anchor now exists immediately
above the "How a dividend is declared" section of the built page. Do not rename it.

Resolved in P2: the term hub's no-exam teaser points at
`/term-life-insurance/no-medical-exam/#who-qualifies`, and that anchor now exists on the routes
section of the built page.

Those anchors exist because spec section 07 allows one link per target per page: the spoke module
owns the canonical page link, so contextual teasers deep-link to the relevant section instead.
Same reason the home page triage results point at `#quote`, `#rates`, and `#costs`.

---

## 7. Wiring

- **CRM endpoint.** `assets/site.js` has a single integration point marked
  `>>> WIRE TO CRM ENDPOINT HERE <<<` in `submitLead()`. It currently logs the payload and resolves.
  Replace the body with a `fetch()` and keep the returned promise: the success state, the error
  state, and the `form_submit` event all hang off it. The payload already carries every answer plus
  `tcpa_consent`, `source_url`, `silo`, `form_name`, `submitted_at`, and `submission_id`.
  `submission_id` is one UUID per form load and is re-sent unchanged when a visitor presses "Try
  again" after a failed submit, so the endpoint **must dedupe on it**. `phone` arrives formatted,
  `(555) 018-0199`: strip non-digits server side. The front end gives up after 15 seconds and never
  retries on its own, because a lead POST is not idempotent.
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
- **`sitemap.xml`** is generated by `tools/build.py` on a full build (not on a single-page build)
  from `PAGES`. A page is omitted if its module is not written yet, if it carries a `noindex`
  `ROBOTS` value (`/thank-you/`, `/404.html`), or if its path is in `SITEMAP_EXCLUDE`. The only
  `robots.txt` is `netlify/robots.txt`, which says `Disallow: /` because the preview must not be
  indexed; replace it with an allow rule plus a `Sitemap:` line when the domain is settled.
- **Hosting is configured for a locked-down preview, and that configuration is itself a
  placeholder.** `netlify.toml`, `tools/stage.py`, `netlify/_headers` and `netlify/robots.txt` give a `noindex`
  header, `Disallow: /` and a publish directory that excludes `public/`, `tools/`, `design-system/`
  and every `.md`. There is **no password gate**: the preview is open to anyone with the link, so
  the link is the only control. **`DEPLOY.md`** is
  the runbook and lists what to undo before a real launch. No Netlify site has been created; none
  should be until the rest of this file is empty.
- **`/compare/whole-life-vs-universal-life/` is built but held back.** Spec section 05 makes this
  page conditional on Apex actually being able to place universal life, because a page that ranks
  for a product we cannot write generates leads that cannot be served. Until the appointments are
  confirmed it is in `SITEMAP_EXCLUDE`, nothing on the site links to it, and its universal life CTA
  goes to `/contact/` rather than a quote form. To publish: confirm the appointments, delete the
  `[CONFIRM UL CARRIER APPOINTMENTS BEFORE PUBLISHING]` comment in
  `tools/pages/compare_whole_vs_ul.py`, remove the path from `SITEMAP_EXCLUDE`, add the contextual
  link from `/whole-life-insurance/`, and point the universal life CTA somewhere real.
- **`/compare/burial-insurance-vs-life-insurance/` currently has one inbound link**, from
  `/final-expense-insurance/what-is-final-expense-insurance/`. Its job is routing confused traffic,
  so it wants a second from the final expense hub's spoke module. That is a one-line change to an
  approved page and was deliberately left for sign-off rather than made here.
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
