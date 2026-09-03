# Apex Insurance Marketing — Design System
## Variation 3: "Transparent Numbers" (Data-Forward Clarity + Bento)

**Design read:** the same trust-first consumer insurance hub for three age cohorts, read this time
as a page of numbers rather than a page of prose. Light, data-forward clarity: crisp white cards on
a cool near-white field, soft blue ambient glows, bento grids wherever a section is fact-dense, and
tables as the visual signature (the spec is table-heavy: rate charts, comparisons, cost-by-age, so
the tables are designed rather than tolerated). Space Grotesk display over Inter body, tabular
numerals everywhere, self-hosted.

**Dials:** `DESIGN_VARIANCE: 5` · `MOTION_INTENSITY: 5` · `VISUAL_DENSITY: 7`

**Skill precedence, as briefed:** ui-ux-pro-max wins on structure, accessibility, and the finance
anti-patterns (no purple or pink gradients, no neon, no dark mode); design-taste-frontend wins on
layout discipline (bento cell count, adjacency, eyebrow budget, hero economy); the spec's compliance
rules win over both. The brief's font choice (Space Grotesk + Inter) and Lucide icons override the
skills' generic font and icon bans.

Single source of truth for the build: five approved pages, the P0 trust layer, the P1 money
pages, the P2 cluster pages, and the P3 support layer, forty two in all. `src/input.css` implements every token
here; if the two disagree, this file is wrong and gets updated, not the other way around.

**Decisions carried from the client conversation, not to be reverted:**
- Rate and cost cells stay `$--`. No invented premium, even a marked one, because a marked fake
  number still gets screenshotted. Tables get their weight from structure, controls, and type.
- Photography began as Variation 1's set in eight slots across five pages. **Superseded:** the
  client asked for photography on every page, so the manifest is twenty six slots and twenty nine
  of the forty two pages carry one. The art direction did not move, and section 8 lists the
  thirteen pages that still carry none and why. Fourteen slots were added; none contains a person.
- No duotone. Photography under text is confined to the three `.banner-band` hubs, which are
  scrimmed and are the only text-over-photography on the site.

---

## 1. Palette

| Token | Hex | Role |
|---|---|---|
| `--color-navy` | `#0B3B8C` | Deep Blue. Dark bands, nav text, links, phone CTA fill, blue bento cell. |
| `--color-navy-700` | `#1E6AE1` | Bright Blue. Icons, strokes, focus ring, chart value line, progress fill. Text only at 18px and up. |
| `--color-navy-050` | `#E8F0FC` | Table header fill, tinted bento cell, tinted band, pills. |
| `--color-ink` | `#0A1F44` | Headlines, stat figures, and the amber CTA label. |
| `--color-slate` | `#334155` | Body text. |
| `--color-muted` | `#5B6B82` | Secondary text, captions, stat labels. |
| `--color-cream` | `#F4F7FB` | Page field (cool near-white). |
| `--color-surface` | `#FFFFFF` | Cards, bento cells, panels, table rows. |
| `--color-gold` | `#F5A623` | Amber. **CTA ONLY.** |
| `--color-gold-700` | `#DC941B` | CTA hover. |
| `--color-green` | `#1F7A5C` | Positive / included states (check icons, success). |
| `--color-rule` | `#D9E2EF` | 1px borders, row rules. |
| `--color-border-strong` | `#7B8CA0` | Form input borders (3:1 per WCAG 1.4.11). |
| `--color-flag` | `#8A6D1F` | Placeholder / pending-review notice text. |

### The amber rule (non-negotiable)
Amber appears in exactly three CSS rules: `.btn-cta`, `.btn-cta:hover`, and `.skip-link`. Nowhere
else. Not on icons, not on pills, not on chart lines, not on hover states of non-CTA elements.
Verified by `grep -o "var(--color-gold" assets/site.css | wc -l` = 3.

### Verified contrast pairs (computed, not eyeballed)
| Pair | Ratio | Verdict |
|---|---|---|
| **Ink on amber** (primary CTA label) | **8.0:1** | AAA |
| Ink on amber-700 (CTA hover) | 6.4:1 | AA |
| White on amber | 2.0:1 | **Fails. Never used.** |
| Slate on white / on field | 10.4:1 / 9.6:1 | AAA |
| Slate on navy-050 (tinted cell) | 9.0:1 | AAA |
| Muted on white / on field / on navy-050 | 5.4:1 / 5.1:1 | AA |
| Ink on white / on navy-050 | 16.3:1 / 14.2:1 | AAA |
| Navy on white / on field | 10.4:1 / 9.7:1 | AAA |
| Navy-700 on white / on field | 5.0:1 / 4.7:1 | AA (used at 18px+ and for non-text only) |
| Navy-700 on navy-050 | 4.3:1 | **Fails for small text.** Eyebrows are navy, not navy-700, for this reason. |
| White on navy (bands, blue cells, phone CTA) | 10.4:1 | AAA |
| White at 80% on navy (footer legal) | 6.5:1 | AA |
| Flag on flag-050 | 4.5:1 | AA |
| Border-strong on white | 3.4:1 | Passes 1.4.11 for inputs |

Primary CTA is **ink text on amber fill**, never white on amber.

### Focus
Default focus ring: 3px bright blue, 2px offset, 4px radius. On navy surfaces (`.on-navy`,
`.bento-cell-blue`) the ring flips to white. A checked segmented choice gets an ink ring so the
ring is visible against its own navy fill. Never `outline: none` without a replacement.

---

## 2. Typography

Self-hosted latin-subset woff2 in `/assets/fonts/`, `font-display: swap`. No Google Fonts request:
one fewer third party on pages that collect PII, and one fewer render-blocking origin.

- **Display / H1 / H2 / stat figures / table heads / eyebrows:** Space Grotesk (variable 300 to
  700, used at 600). A geometric grotesque with a slightly technical voice: reads as a well-made
  statement, which is the register a page of numbers wants. Not Fraunces, not Inter-for-everything.
- **Body / UI / H3 and below:** Inter (variable 100 to 900).
- **Tabular numerals everywhere.** `font-variant-numeric: tabular-nums` is set on `body`, not per
  table, because every figure on this site ends up in a column or beside another figure sooner or
  later, and proportional digits jitter. Both faces carry the `tnum` feature.

### Ramp (base 16px)
| Token | Size | Line height | Face |
|---|---|---|---|
| `text-display` | clamp 2.5rem to 3.75rem | 1.02 | Space Grotesk 600 |
| `text-h1` | clamp 2.25rem to 3.25rem | 1.06 | Space Grotesk 600 |
| `text-h2` | clamp 1.75rem to 2.5rem | 1.12 | Space Grotesk 600 |
| `text-h3` | 1.375rem | 1.3 | Inter 600 (Space Grotesk where marked `!font-display`) |
| `text-h4` | 1.125rem | 1.4 | Inter 600 |
| `text-lead` | 1.1875rem | 1.6 | Inter 400 |
| `text-body` | 1rem | 1.65 | Inter 400 |
| `text-sm` | 0.875rem | 1.55 | Inter 400 |
| `text-micro` | 0.8125rem | 1.5 | Inter 500 |

`.stat-value` is `text-h2` in Space Grotesk at line-height 1; `.stat-value-lg` is `text-display`.
Measure caps at 68ch for body copy, 20ch for display headlines.

### Final-expense override
`<html class="fe">` redefines the type tokens **on `main`**, not on `html`. Inside the page content
the ramp moves up a notch: body 18px, lead 21px, h3 24px, and the `sm` and `micro` steps collapse
into the body size so nothing on that page renders below 18px. **Inter throughout on that page**:
headings, stat figures, table heads, and step numerals all drop the display face, because the
display face is a style choice and this page does not make style choices.

Scoping to `main` keeps the shared header and footer at the sitewide scale. Minimum tap target
rises to 56px, paragraph max-width drops to 58ch, tables stay at three columns.

---

## 3. Grid and spacing

### The row rule
A block may be narrow **only if something else occupies the rest of its row.** No section may
leave more than 20% of its content row empty on the right, and no two-column row may differ in
column height by more than 250px.

Swiss 12 column. Container `max-width: 1200px`, gutter 24px, 32px at 1024 and up. **Declared in
px, not rem**, so the final-expense type bump cannot widen the grid. Breakpoints tested:
**375 / 768 / 1024 / 1440**.

Spacing scale (4px base): `4 8 12 16 24 32 40 48 64 80 96 128`.
Section rhythm at `VISUAL_DENSITY 7`: `py-18` mobile, `py-24` at 768, `py-26` at 1024. A notch
tighter than Variation 1 because the sections carry more structure and less air.

### Bento
`.bento` is a six-track grid with a 16px gap. Cells span 2, 3, 4, or 6 tracks (`.bento-2` etc.),
collapse to two-up at 768 and one-up below. **Exactly as many cells as there is real content**: a
three-item section is three `.bento-2` cells, a chart section is a `.bento-4` chart beside a
`.bento-2` stat. No grid is padded with a blank tile, and no grid exceeds six cells. At least one
cell in every grid carries visual variation: `.bento-cell-tint` (navy-050) or `.bento-cell-blue`
(navy fill, white text), so a grid is never six white cards in a row.

### Surfaces
One shadow system, blue-tinted so it reads as ambient light rather than dirt:
`--shadow-card` on cards, cells, tiles, and signature tables; `--shadow-panel` on the hero form
panels; `--shadow-lift` on hover. Every card also keeps a 1px `--color-rule` border so it still has
an edge on a white-on-white screen.

Corner radius: **two values.** `12px` on cards, cells, tables, and media; `8px` on buttons, inputs,
choices, and pills-that-are-not-pills. Pills and step numerals are `999px`. Nothing else.

### Glow
`.glow` paints two soft radial blue gradients behind a section (`::before`, `z-index: -1`,
`pointer-events: none`, horizontally clipped to the section so it can never widen the page). It is
used on the hero of every page except final expense, and on at most one more section per page.
Decorative only; every text surface still sits on a solid card or the solid field.

### Glass
Exactly one glass surface: the sticky header, and only once it is stuck. `rgb(255 255 255 / .86)`
plus `backdrop-filter: blur(10px)` and a 1px rule. It is solid white before scrolling, solid white
under `prefers-reduced-transparency`, and solid white where `backdrop-filter` is unsupported. Nav
text is slate and navy on that surface and was measured against the lightest hero pixel.

---

## 4. Motion (MOTION_INTENSITY 5)

`IntersectionObserver` reveal for everything; no scroll-linked layer, no animation library, no
`scroll` listener anywhere in the codebase. Variation 1's parallax and mask-wipe layer was removed,
not disabled.

| Pattern | Spec | Applies to |
|---|---|---|
| Section reveal | opacity 0 to 1 + translateY 12px to 0, 480ms `cubic-bezier(.22,1,.36,1)` | Every section |
| Stagger | `data-stagger` step in ms, capped at 6 children: **40ms on bento grids**, 60ms on lists | Bento grids, card rows, spoke grids |
| **Count-up** | `[data-count]` figures count from 0 to the value over 900ms, cubic ease-out, `Intl` formatted with prefix and suffix | Stat figures that are **spec figures** (10 / 15 / 20 / 30 years, $2,000,000, 40 years, 15 minutes). Never a `[X]` placeholder, never a rate. |
| Row cascade | 34ms per row, opacity + translateY 6px | Rate and comparison table rows |
| Chart draw-in | `stroke-dashoffset`, 1.4s, fill and marker fade after | Cash-value chart |
| Card lift | translateY(-3px) + `--shadow-lift` + blue border, 220ms | `.card-hover`, `.tile` |
| CTA hover | translateY(-2px) + tinted shadow, 180ms | Buttons |
| Link underline | grows from left, 180ms ease-out | Body links |
| Accordion | height via `interpolate-size: allow-keywords`, 240ms | FAQ |
| Form step change | 240ms crossfade, focus moves to the first field | Term multi-step form |

The count-up target is written into the HTML, so with JavaScript off, in print, and before the
observer fires the figure is simply there. Nothing ticks up to a placeholder.

**Deliberately absent.** Scroll-progress bar (a scroll cue). Pinned scroll-scrubbed sequences.
Parallax. Marquees.

### Reduced motion
`prefers-reduced-motion: reduce` collapses everything to opacity at 1ms, disables lift and
cascade, draws the chart fully, leaves every count-up at its final value, and forces every reveal
visible so no content can be trapped invisible. Verified in the browser: zero hidden reveals.

### Final-expense exemption
`.fe main` opts out of every pattern above except the opacity reveal: no translate, no stagger, no
count-up (`countUp()` returns early on `html.fe`), no row cascade, no lift, no glow, no chart.
Static, calm, large. This is an accessibility decision, not a stylistic one.

---

## 5. Component contracts

| Component | Contract |
|---|---|
| `.btn-cta` | Amber fill, ink text, 600 weight, min-height 48px, 8px radius. The only amber thing. |
| `.btn-call` | Navy fill, white text, phone icon, min-height 48px. `.btn-xl` 64/72px for final expense. |
| `.btn-ghost` | White fill, navy text, 1px navy rule. Tertiary only. |
| `.btn-row` | Row-level action inside tables and cells, 44px, navy outline. 48px inside `.fe main`. |
| `.card` / `.bento-cell` | White fill, 1px rule, 12px radius, `--shadow-card`, 24 to 32px pad. `.bento-cell-tint` and `.bento-cell-blue` are the variation cells. |
| `.panel` | The hero form panels. `--shadow-panel`. |
| `.stat` | `.stat-value` (display face, tabular) over `.stat-label` (muted). Holds `data-count` only when the figure is a spec figure. Rendered by `chrome.stat()`. |
| `.pill` | Navy-050 chip for dated lines ("Rates last updated") and column tags. Never amber. |
| `.table-signature` | Modifier on `.table-scroll`: card shadow, so the table reads as the section's object. |
| `.rate-table` / `.compare-table` | Tabular nums, navy-050 header in the display face, **one rule per row boundary** (top border on every row after the first, never top and bottom), first column sticky on phones. `th[colspan]` renders as a group row (final expense comparison). |
| `.acc` | Each `<details>` is its own card row; hover and open states lift it. Native keyboard behavior. |
| `.field` | Label above input, 48px input, border-strong, blue focus ring. The error line is **always in the layout** and only toggles `visibility`. |
| `.site-header` | Solid white; glass only when `.is-stuck`. Wordmark navy, nav slate with a bright-blue underline. |
| `.flag` | Visible placeholder notice. Left rule in `--color-flag`. Renders on the page, not only in comments. |
| `chrome.page_hero()` | T4's top: breadcrumb, one H1, and the answer in the first two sentences. The lead is HTML because it carries the mandated hub up-link. `glow=False` on every final-expense page. |
| `chrome.inline_cta()` | The single mid-page CTA on an informational page. One ask offered two ways; `phone_first` decides which one carries the amber. Never an interstitial. |
| `chrome.prose()` | Heading and lead on the left, substance on the right. What keeps a long informational page off the single centred column section 7 bans. `media=` puts a figure under the lead and `sticky=` (default on) parks the column, which is how the left side stops leaving a dead half-row. Sticky needs no fe branching: `.fe main .sticky-col` is already static. |
| `chrome.page_hero()` `media=` | Splits the hero into 6 / 5-from-8 and carries the page's one eager image. Absent it, the hero is the unchanged `max-w-3xl` single column. |
| `chrome.faq_section()` `center=` | Default on. An accordion has no second column, so the block is centred rather than stranding 40% of the row. Heading text is centred; the question rows stay left aligned. |
| `.sticky-col` | Goes on an **inner div** inside a full-height grid item, and the grid must not be `items-start`. On the grid item itself under `items-start` the column is content height and never travels. |
| `chrome.qa()` | One heading-and-paragraph pair inside a `prose()` column. Used where a page absorbs a secondary search intent as an H3 rather than a page. |
| `chrome.byline_section()` | The byline in its own band. Closes every editorial page. Placed directly under the hero as well on `/whole-life-insurance/is-it-worth-it/`. |
| `compare.render()` | T5's whole body. Section order is fixed, only the copy is passed in. |
| `compare.table()` | The side-by-side `.compare-table` inside `.table-scroll.table-signature`. A row with an empty cell list becomes a `th[colspan]` group row. |
| `compare.checklist()` | Lucide `check` plus a statement per row, `data-stagger="40"`. Statements the reader answers about themselves, never a scored quiz: a quiz needs a threshold and there is no honest one. |
| `compare.two_path()` | T5's close. One card per product, both `.btn-cta`, each routing into that product's own silo. |

Icons: **Lucide only**, inlined as SVG, 1.5px stroke, 20px or 24px, `aria-hidden="true"` with the
meaning carried by adjacent text.

---

## 6. Per-page overrides

See `design-system/pages/*.md` for the full per-page notes. In brief:

**Home.** Triage, not pitch. Hero: h1, lead, one link line, photo, and the three product paths as
a three-cell bento (middle cell tinted). The comparison section is a four-cell bento: three product
stat cells (white, tinted, blue) over a full-width signature comparison table.

**Term hub.** Form-weighted; the three-step form is the hero's right panel. "What it covers" ends
in a three-cell bento led by a blue coverage-range stat. Term lengths are four segmented stat cells
(`10 / 15 / 20 / 30`) that count up and drive the explainer panel. The rate table is the page's
signature object, with its toggles above it and a dated pill beneath.

**Whole-life hub.** Dual CTA at parity. The three guarantees are a white / blue / tinted bento.
The cash-value chart sits in a `.bento-4` beside a tinted `.bento-2` stat (40 years). Section 7b
("who this does not suit") keeps identical prominence to 7a.

**Final-expense hub.** Phone-first, Inter throughout, static. Cost table cut to three columns
(`Age | $10,000 | $25,000`) with the row-level call CTA inside the age cell. The three-product
comparison is a three-column table with group rows so it never needs a fourth column.

**Contact.** Split layout; "what happens next" is a three-cell bento (white, tinted, blue).

**P0 pages.** The trust and conversion layer: `/about/` and its four children, `/get-a-quote/`,
the three `/legal/` documents, `/thank-you/`, and `/404.html`. They inherit this file without
deviation except where a page doc exists (`get-a-quote`, `about-agent-profile`, `about-licensing`,
`legal`). Three rules run across all of them. Placeholder trust figures render with
`C.stat(..., count=False)`, because section 4 bans count-up on a number we do not have and every
figure on `/about/` is one. Placeholder tables (licensing, carriers, the agent's licences) put the
`.flag` above the table, so a reader meets the notice before the number. And `/about/reviews/`
emits no `AggregateRating` while the review count is zero: an aggregate rating over no reviews is
a fabricated review expressed in structured data.

**P1 money pages.** `/term-life-insurance/quotes/`, `/rates/`, and `/calculator/`. T1 puts the
form above the fold and the sample rate table **before** it, never behind it. T2 puts the chart
first and hosts the quote form further down purely because row-level prefill needs a target in the
same document. T3 ships its worked example already computed into the HTML, so with JavaScript off
the derivation is complete rather than a column of zeros.

**P2 cluster pages.** Thirteen informational spokes on T4, plus the whole life calculator on T3.
They inherit this file without deviation except where a page doc exists (`term-no-medical-exam`,
`whole-calculator`, `whole-cash-value`). Six rules run across all of them.

1. **The answer is the first two sentences**, inside `chrome.page_hero()`, before any section. The
   mandated hub up-link lives in that lead, which is the only placement that satisfies both spec
   s07 rule 1 and "answer the question first".
2. **One mid-page CTA**, `chrome.inline_cta()`, never an interstitial. The exception is
   `/term-life-insurance/no-medical-exam/`, which the spec treats as near-money.
3. **One link per target per page.** A page's spoke module may not repeat a target the body already
   links. Where a contextual link and the module both want one page, the module keeps the canonical
   bare link and the contextual one deep-links to an anchor. The breadcrumb plus the mandated
   up-link is the one accepted duplicate.
4. **The "does not suit" section matches its opposite in size.** Applied on the two what-is pages,
   both seniors pages, and the cash value page.
5. **A white card inside a `.band-navy` needs `!text-ink` on its heading.** `.band-navy h3` is a
   descendant selector, so an unqualified heading there renders white on white.
6. **Every table is a placeholder about price or a statement about behaviour**, never a mix. A
   behaviour table (underwriting routes, what a waiting period pays) carries no `$--` and no rate
   flag; a price table carries both, plus the dated pill.

**P3 support pages.** Seven objection and E-E-A-T spokes on T4, plus two neutral compare pages on
T5. The T4 seven inherit the six rules above without exception. Three deviations are recorded as
page docs (`whole-is-it-worth-it`, `fe-for-parents`, `compare`), and they exist because on these
pages the layout is carrying an editorial position:

- `/whole-life-insurance/is-it-worth-it/` puts `chrome.byline_section()` **directly under the
  hero** as well as ending without one, has no amber anywhere, and orders "who it is not for"
  before "who it is for". A page arguing the case against the thing we sell has to show who is
  making the argument before the argument, and leading with the case for would make it a sales page
  with a balanced headline.
- `/final-expense-insurance/for-parents/` is the only final expense page that does **not** set
  `HTML_CLASS = "fe"`, and the only one that is form weighted. Both follow from the buyer being the
  adult child rather than the insured. The calm register is kept; the type scale is not.
- The two `/compare/` pages set `SILO = "compare"` and `ACTIVE = "/"`. No silo owns them, which is
  what makes them the one legal cross-silo route under spec s07 rule 3.

**T5, the comparison template** (`tools/pages/compare.py`). Section order is fixed by the spec and
is not parameterised: hero carrying the answer in three sentences, side-by-side `.compare-table` as
the signature object, worked cost over time, where each one wins as a two-cell bento, decision
checklist, two-path CTA, FAQ, byline. A row in the table with an empty cell list renders as a
`th[colspan]` group row. Both buttons in `compare.two_path()` are `.btn-cta`: on a neutral page,
giving one the amber and the other a ghost outline is a recommendation disguised as a layout
decision, and readers can tell.

**Per-silo CTA weighting on the spokes.** Term is form first, except `/for-seniors/` which is phone
first. Whole life is form and phone at parity with an illustration request as the tertiary ask,
except `/for-seniors/` which is phone first and `/cash-value/` which is soft CTA only and carries no
amber at all. Final expense is phone first throughout, with the four-field
`final_expense.callback_form()` as the secondary.

---

## 7. Banned

No purple or pink gradients. No neon. No dark mode. No emoji as icons. No section-number eyebrows
(`01 / Coverage`). No scroll cues. No centered-everything pages: one centred section, such as the
FAQ block, is not a centred page and is not what this bans. No Fraunces. No amber outside the
three CTA rules. No `border-top` plus `border-bottom` on the same table row. No bento cell without
content. No count-up on a placeholder or a rate. No glass except the stuck header.
No em-dash anywhere in rendered copy: use a comma, a colon, a period, or a middot separator.
`tools/build.py` fails the build if one appears, entity forms included.
No invented rates, reviews, carrier names, or dollar claims. Rate cells are `$--` by decision.

**Photography.** Posed joy at the camera is banned. Two rules with no exceptions:

1. **No photograph of a person beside the agent byline.** Bylines use a marked placeholder avatar.
2. **No image captioned or positioned to imply the person shown is a customer.**

Eyebrow budget per page: `ceil(sectionCount / 3)`. Eyebrows are navy, display face, and used only
inside bento cells to name the cell.

---

## 8. Imagery

### Art direction
Documentary, no eye contact with the camera. Hands, backs, thresholds, kitchen tables, a window,
a porch. Photographs here are atmospheric and evidence nothing, so none may be positioned to
suggest it does: no photo beside a testimonial, a rate, a claim statistic, or the agent byline.

### Sourcing and licensing
Unsplash, downloaded and served locally. Nothing hotlinks at runtime. The Unsplash Licence does
**not** convey a model release, so identifiable people must be cleared or replaced before launch.
`assets/img/CREDITS.md` records every file; `REPLACE-BEFORE-LAUNCH.md` tracks the swap. The
manifest lives in `tools/images.py`; `python3 tools/images.py --fetch` is idempotent.

### Delivery
`<picture>` with AVIF, then WebP, then `<img>`; explicit `width` and `height`; `sizes` matched to
the real column; exactly one `loading="eager"` + `fetchpriority="high"` per page; descriptive
`alt` or `alt=""` when decorative.

### Placement at `VISUAL_DENSITY 7`
Twenty nine of the forty two pages carry a photograph, all in 12px-radius plates with a 1px inset
hairline, some with the blue `.glow` behind them. A T4 page carries **at most two**: the hero
figure, which is that page's one eager image, and one rail figure in a `prose()` left column.

**A final expense page may carry three.** `.fe main .sticky-col` is `position: static`, so an fe
page cannot close a dead half-row with the rail the way every other page does, and it spends a
photograph instead. That is the whole cost of the fe motion exemption, and it is worth paying.

No image goes near the triage widget, any rate table, the comparison tables, the cash-value chart,
the FAQ accordions, the spoke grids, or any byline. **A hero counts as near** when one of those is
the section immediately below it, which is why the quote, rates and calculator pages have no hero
photograph.

**The thirteen pages with no photograph.** Each is a decision, and each should stay one:

| Page | Why |
|---|---|
| term quotes, term rates, both calculators | a form, a rate table or the calculator sits directly under the hero |
| get-a-quote, about/licensing | ruled out by their own page docs |
| about/reviews | a page about testimonials, and no photo goes beside one |
| about/agents/&lt;slug&gt; | leads with the marked placeholder avatar; section 7 rule 1 |
| legal privacy, terms, disclaimer, 404, thank-you | utility pages |

None of them is left with a dead row: they close it with the `.sticky-col` rail instead.

**No photo is placed twice on one page.** `tools/check.py` enforces that, the one-eager-image
rule, and the row rule in section 3.

### Banner bands (`.banner-band`, one per product hub)

The only text-over-photography on the site. Each product hub carries exactly one, built by
`chrome.banner()`: full-bleed photo, navy scrim, one heading, one paragraph, one primary CTA with
one secondary beneath it.

Placement is a CRO rule, not a taste call:

* **Never above the fold.** The top of a hub belongs to the H1 and the quote form. A banner there
  pushes the form down and costs form starts.
* **Never between the hero CTA and the trust strip.** Measured on this site at 433 to 491px of
  added gap, which destroys the proximity the strip exists to provide.
* **At roughly 55 to 70 percent scroll depth**, replacing what was already a flat navy CTA band, so
  the page gains a photograph without gaining a section. Term takes the no-exam band, whole life
  takes a new band after the cash-value proof, final expense takes the middle of its three call
  bands. One photo band per page: three would read as wallpaper rather than as a break.
* **Height comes from the copy, not from the 21:9 crop.** A true 21:9 band at 1440 is 617px of
  scroll for one sentence.

Scrim: `linear-gradient(100deg, rgb(6 33 79 / .95), .90 at 52%, .74)`, flat at `.92` below 1024
where the copy crosses the whole frame. It hangs off `.banner-media::after`, not off
`.banner-band::before` — a `::before` on the band is its first child and paints *under* the
`<picture>`, which leaves bright photographs unscrimmed and the white copy unreadable.

Every banner photo is decorative and carries empty `alt`. All meaning is in the text. No banner
photo repeats a photo used elsewhere on the same page.
