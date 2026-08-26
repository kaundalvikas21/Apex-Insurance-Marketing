# Apex Insurance Marketing — Design System
## Variation 2: "Family Counsel" (Soft UI Evolution)

**Design read:** trust-first consumer insurance hub for three age cohorts, read as a family
advisor's office rather than a call centre. Soft UI Evolution: layered low-opacity shadows,
16 to 24px radii, cream surfaces on an ivory ground, one deep-forest anchor per page, gold used
for nothing but calls to action. Cormorant Garamond display over Montserrat body, self-hosted.

**Dials:** `DESIGN_VARIANCE: 3` · `MOTION_INTENSITY: 4` · `VISUAL_DENSITY: 4`

**Skill precedence, as briefed:** high-end-visual-design wins on surface treatment (shadows,
radii, nested surfaces, spring easing); ui-ux-pro-max wins on structure, accessibility, and the
finance anti-patterns; the spec's compliance rules win over both. Where the three disagree the
resolution is written down in section 9.

Single source of truth for the five-page build. `src/input.css` implements every token here; if the
two disagree, this file is wrong and gets updated, not the other way around.

> The `ui-ux-pro-max --design-system --persist` scaffold for this project recommended a corporate
> navy/orange "Enterprise Gateway" pattern with Varela Round. That is a B2B read of the query and it
> was overruled by the brief, which names the palette and the faces. Its UX checklist is kept and
> applied; its aesthetic recommendation is not.

---

## 1. Palette

| Token | Hex | Role |
|---|---|---|
| `--color-forest` | `#1E3A34` | Primary. Headlines, wordmark, phone CTA fill, the one dark band, footer. |
| `--color-forest-700` | `#2B4B44` | Hover on forest, raised surfaces inside the forest band. |
| `--color-forest-950` | `#10241F` | Text on gold. See the contrast note below. |
| `--color-ink` | `#3A4743` | Body text. Forest-tinted dark grey, not black. |
| `--color-muted` | `#6E5F50` | Secondary text, captions, table sub-labels. Darkened taupe. |
| `--color-taupe` | `#8A7968` | The brief's Warm Taupe. Input borders, large text, icons, decoration. **Not** body or small text. |
| `--color-ivory` | `#FAF7F2` | Page ground. |
| `--color-surface` | `#FFFDFA` | Cards, panels, table rows. Warm near-white, never pure white. |
| `--color-sage` | `#E7EDE6` | Alternating band, table header fill, step-number discs. |
| `--color-gold` | `#B8905F` | **CTA ONLY.** |
| `--color-gold-700` | `#AA8352` | CTA hover. |
| `--color-moss` | `#3F6E52` | Positive, covered, included. Check icons, the cash-value line. |
| `--color-moss-050` | `#E4EEE6` | Cash-value chart fill. |
| `--color-rule` | `#ECE6DC` | Soft hairline. The only border colour, and it is barely one. |
| `--color-flag` | `#7A5C2E` | Placeholder / pending-review notice text, on `--color-flag-050` `#F7EEDF`. |
| `--color-danger` | `#A32020` | Validation errors. |

### The gold rule (non-negotiable)
Gold appears on call-to-action buttons and on the focus ring over forest backgrounds. Nowhere else.
Not on icons, not on hairlines, not on hover states, not on headline accents, not on the favicon.
If gold appears twice in a viewport and only one of them is a CTA, that is a bug.

### Contrast, measured, not eyeballed
Two pairs the brief implies fail WCAG AA and were corrected at the token level:

| Pair | Ratio | Decision |
|---|---|---|
| Warm Taupe `#8A7968` on ivory | 3.9:1 | Fails for text. Taupe is kept for input borders (needs 3:1, passes at 4.1 on surface), icons, and text at 24px+. Secondary *text* uses `--color-muted` `#6E5F50` at 5.8:1. |
| Deep Forest on Burnished Gold | 4.2:1 | Fails for 16px button labels. The gold is kept exactly as briefed; the label is `--color-forest-950` at 5.6:1 (4.7:1 on the hover shade). White on gold is 2.9:1 and is never used. |

Verified pairs:

| Pair | Ratio | Verdict |
|---|---|---|
| Forest on ivory | 11.5:1 | AAA |
| Ink on ivory / on sage | 9.1:1 / 8.2:1 | AAA |
| Muted on ivory / sage / surface | 5.8 / 5.2 / 6.1 | AA |
| **Forest-950 on gold** (primary CTA) | **5.6:1** | AA |
| White on forest (phone CTA, footer, dark band) | 12.3:1 | AAA |
| White at 80% on forest | 7.8:1 | AAA |
| Moss on ivory / surface | 5.5 / 5.8 | AA |
| Gold ring on forest (focus, non-text) | 4.2:1 | Passes 1.4.11 |
| Flag on flag-050 | 5.4:1 | AA |

### Focus
Default focus ring: 3px forest, 2px offset, radius follows the element. Inputs replace the outline
with a 2px forest border plus a soft forest halo, which is still a solid 3:1 indicator. On forest
surfaces the ring flips to gold. Never `outline: none` without a replacement.

---

## 2. Typography

Self-hosted latin-subset woff2 in `/assets/fonts/`, `font-display: swap`, no Google Fonts request
at runtime: one fewer third party on pages that collect PII.

- **Display / H1 / H2 / card titles / wordmark:** Cormorant Garamond 600. Italic 500 for the
  one emotional line. Cormorant is in the taste-skill's permitted serif pool and is named by the
  brief; it is a different face from Variation 1's Caslon.
- **Body / UI / tables / H3+ :** Montserrat, variable 100 to 900. Body at 400, labels 500, UI 600.
- **Tabular numerals** on every rate table, premium figure, and coverage amount.

Cormorant has a small x-height, so the display ramp sits roughly 12% larger than a Caslon ramp
would for the same optical size.

### Ramp (base 16px)
| Token | Size | Line height | Face |
|---|---|---|---|
| `text-display` | clamp 2.75rem to 4.25rem | 1.05 | Cormorant 600 |
| `text-h1` | clamp 2.5rem to 3.75rem | 1.08 | Cormorant 600 |
| `text-h2` | clamp 2rem to 2.875rem | 1.12 | Cormorant 600 |
| `.text-h3-serif` | 1.75rem | 1.2 | Cormorant 600 (card and panel titles) |
| `text-h3` | 1.375rem | 1.35 | Montserrat 600 |
| `text-h4` | 1.0625rem | 1.4 | Montserrat 600 |
| `text-lead` | 1.1875rem | 1.6 | Montserrat 400 |
| `text-body` | 1rem | 1.7 | Montserrat 400 |
| `text-sm` | 0.875rem | 1.6 | Montserrat 400 |
| `text-micro` | 0.8125rem | 1.5 | Montserrat 500 |
| `.ital-line` | clamp 1.375rem to 1.75rem | 1.25 + 0.25rem reserve | Cormorant italic 500 |

Measure caps at 66ch for body copy, 20ch for display headlines.

### The italic line
One per page, maximum. It carries the emotional register so nothing else has to. Every instance
is checked for descender clearance: `y g j p q` in italic Cormorant need line-height 1.25 and a
bottom reserve, which the class provides.

### Final-expense override
`<html class="fe">` redefines the type tokens **on `main`**: body 18px, nothing inside the page
content below 18px, hierarchy from weight and colour. The page is **Montserrat throughout**; the
serif is used in the H1 only. `.fe main h2` and `.fe main .text-h3-serif` are re-pointed at the
sans face, and the H2 ramp is pulled in slightly because Montserrat is a wide face.

Scoping to `main` keeps the shared header and footer at the sitewide scale. Minimum tap target on
that page is 56px, paragraph measure 58ch, no paragraph over three sentences.

---

## 3. Grid, spacing, shape

### The row rule
A block may be narrow **only if something else occupies the rest of its row.** No section may
leave more than 20% of its content row empty on the right, and no two-column row may differ in
column height by more than 250px.

12 column grid. Container `max-width: 1200px`, gutter 24px, 32px at 1024 and up, declared in px so
the final-expense type bump cannot widen it. Breakpoints tested: **375 / 768 / 1024 / 1440**.

Spacing scale (4px base): `4 8 12 16 24 32 40 48 64 80 96 128`.
Section rhythm: `py-20` mobile, `py-28` at 768, `py-32` at 1024. Bands keep the same rhythm.

### Shape lock (one documented rule, applied everywhere)
| Radius | Token | Applies to |
|---|---|---|
| **24px** | `--radius-card` | Cards, panels, tables, media, the mobile nav panel |
| **16px** | `--radius-ui` | Buttons, inputs, selects, choice chips, accordion items, spoke tiles, logo slots, flags |
| **999px** | `rounded-full` | Progress segments, step-number discs, the nested icon disc inside buttons, the coverage scale |

Nothing else. No `rounded-[2px]`, no mixed radii on one component.

### Surfaces and shadow
No harsh borders. Cards and panels are lifted off the ground with layered, forest-tinted,
low-opacity shadows and a 1px ring at 5% forest for edge definition:

| Token | Value | Where |
|---|---|---|
| `--shadow-soft` | `0 0 0 1px forest/5%, 0 1px 2px forest/4%, 0 6px 16px forest/5%, 0 18px 40px forest/6%` | Every card, table, accordion item |
| `--shadow-lift` | `0 0 0 1px forest/6%, 0 2px 4px forest/5%, 0 14px 28px forest/9%, 0 36px 64px forest/10%` | Hero form panels, hovered interactive cards |

Hovered interactive cards translate 4px up and bloom from soft to lift ("4px card lift with shadow
bloom"). Non-interactive cards do not move.

**One deep-forest band per page.** The footer is chrome and does not count. Inside the page
content, exactly one section may sit on forest: Home uses it for independence and commission
disclosure; the whole-life hub for the final split CTA; the term hub for the carriers strip; the
final-expense hub for the last of its three phone bands. Contact has none.

---

## 4. Motion (MOTION_INTENSITY 4)

Gentle springs. Nothing scroll-linked, no parallax, no mask wipes: those are intensity 5 and up and
were removed from Variation 1's layer, not disabled. No animation library, no scroll listener.

| Pattern | Spec | Applies to |
|---|---|---|
| Section reveal | opacity 0 to 1, translateY 10px to 0, scale .985 to 1, 560ms opacity on `--ease-out`, 640ms transform on `--ease-spring` | Every section |
| Stagger | 60ms per child, capped at 6 | Card rows, spoke grids, path cards |
| Card lift | translateY(-4px) + shadow bloom, 320ms spring | Interactive cards and tiles only |
| Button press | scale(.98) on `:active`, 120ms | Every button |
| Nested icon disc | translateX(3px) on hover inside CTA, 280ms spring | `.btn-cta::after`, `.btn-call svg` |
| Link underline | grows from left, 180ms | Body links |
| Row cascade | 34ms per row, opacity + 6px | Rate and comparison tables |
| Accordion | height via `interpolate-size`, 240ms | FAQ |
| Chart draw-on | `stroke-dashoffset`, 1.4s | Cash-value chart |
| Form step change | 240ms crossfade, focus moves to first field | Term multi-step form |
| Header shrink | 80px to 64px, 240ms spring, IntersectionObserver sentinel | Sticky header |

`--ease-out: cubic-bezier(.22, 1, .36, 1)` and `--ease-spring: cubic-bezier(.34, 1.3, .64, 1)`.
No `linear`, no `ease-in-out`.

### Reduced motion
`prefers-reduced-motion: reduce` collapses everything to opacity at 1ms, removes lift, press, and
disc travel, and forces every reveal visible so no content can be trapped invisible.

### Final-expense exemption
`.fe main` is **fades only**: opacity reveals with no translate and no scale, no card lift, no
button lift, no row cascade, no stagger. Vestibular sensitivity and low vision both rise sharply in
the 60 to 85 band, and the spec calls senior accessibility conversion work on this page.

---

## 5. Component contracts

| Component | Contract |
|---|---|
| `.btn` | 48px min height, 16px radius, Montserrat 600, press scale. |
| `.btn-cta` | Gold fill, forest-950 text, a nested 28px disc at the trailing edge carrying the arrow. The only gold thing. |
| `.btn-call` | Forest fill, white text, the phone icon sits in a translucent disc at the leading edge. `.btn-xl` variant for final expense: 64px, 72px at 768. |
| `.btn-ghost` | Transparent, forest text, 1.5px inset ring at 35% forest. Tertiary only. |
| `.card` | Surface fill, 24px radius, `--shadow-soft`, 28px pad (36px at 768). No border. Add `.card-hover` only when the whole card is a link or a control. |
| `.panel` | `.card` with `--shadow-lift`. Hero form panels and the triage widget. |
| `.tile` | Spoke links. 16px radius, soft shadow, lifts on hover. |
| `.rate-table` | Tabular nums, sage header, soft row hairlines, 24px clipped container, horizontal scroll on mobile. |
| `.field` | Label above, 48px input, taupe border, error line always in the layout and toggled by `visibility` so a late error can never push the submit button out from under the pointer. |
| `.consent` | Ivory tint, 16px radius, 24px checkbox, forest accent. Separate, unchecked, immediately above submit. |
| `.acc` | FAQ item: a soft card per question, plus icon rotates to a cross on open. |
| `.step-num` | 48px sage disc, Cormorant numeral. Replaces the ruled step headers. |
| `.trust-strip` | Muted micro text on a surface strip with soft top and bottom rules, within one viewport of its CTA. |
| `.flag` | Visible placeholder notice: flag-050 fill, 3px inset accent, 16px radius. Renders on the page, not only in comments. |
| `.ital-line` | The one italic serif line. |

Icons: **Lucide only**, inlined as SVG, 1.5px stroke, `aria-hidden="true"`, meaning carried by the
adjacent text. (The soft-skill prefers Phosphor; the spec mandates Lucide, and the spec wins.)

---

## 6. Per-page overrides

Page files in `design-system/pages/` carry the detail. In brief:

**Home.** Triage, not pitch. The only duotone photograph on the site sits in the hero. Three
product paths as three distinct soft cards carrying their own silo's CTA weighting. The forest band
is the independence and commission section.

**Term hub.** Form-weighted. Multi-step form is the hero's right column in a lifted panel, above the
fold at 1024. Rate table rows prefill the form. Forest band: carriers strip.

**Whole-life hub.** Dual CTA at parity: two lifted panels, same width, same height. Section 7b has
identical prominence to 7a. Forest band: final split CTA.

**Final-expense hub.** Phone-first, Montserrat throughout, fades only. Phone CTA above the fold at
display size, repeated after sections 4, 6, and 8 as lifted call panels; the third is the forest
band.

**Contact.** Split layout, designed success state rendered in place, never `alert()`.

---

## 7. Banned

No purple or pink gradients. No neon. No dark mode. No emoji as icons. No section-number eyebrows.
No scroll cues. No centered-everything pages. No Fraunces. No pure black anywhere (`#000` does not
appear in the stylesheet outside print). No glassmorphism: no `backdrop-filter` on any surface. No
gradient text. No harsh 1px borders: the only line colour is `--color-rule` and it sits at
roughly 1.3:1 against the ground. No em-dash anywhere in rendered copy; `tools/build.py` fails
the build if one appears, entity forms included. No invented rates, reviews, carrier names, or
dollar claims.

The Warm Taupe / ivory / gold family is close to the taste-skill's "premium consumer default"
ban list. It is used here because the brief names the exact hex values, which is the documented
override. It is still not permitted to drift: no additional brass, clay, or ochre tints may be
introduced.

**Photography.** Posed joy at the camera is banned. Documentary, no eye contact, hands and
thresholds and kitchen tables. Two rules with no exceptions:

1. **No photograph of a person beside the agent byline.** Bylines use a marked placeholder disc.
2. **No image captioned or positioned to imply the person shown is a customer.**

Eyebrow budget per page: `ceil(sectionCount / 3)`. This build uses none.

---

## 8. Imagery

Same manifest and delivery rules as Variation 1 (`tools/images.py`, AVIF then WebP at three
widths, explicit dimensions, one eager image per page, Unsplash served locally, model releases
tracked in `REPLACE-BEFORE-LAUNCH.md`). What changes:

- **Duotone in the home hero only.** Grayscale plate, forest lifted into the shadows
  (`mix-blend-mode: lighten` under a forest layer), warm cream capped into the highlights
  (`darken` under a cream layer). The blend is isolated to the frame. Product hubs and contact get
  the photograph in natural colour with a 24px radius and no overlay.
- **No text over photography anywhere.** Variation 1's scrimmed independence band is gone; the
  `home-independence` slot was removed from the manifest along with its files.
- Eight images across five pages. No image goes near the triage widget, a rate table, a comparison
  table, the cash-value chart, a FAQ, a spoke grid, or a byline.

---

## 9. Where the skills disagreed, and who won

| Question | high-end-visual-design | ui-ux-pro-max / taste | Spec | Resolution |
|---|---|---|---|---|
| Sticky edge-to-edge header | Banned, wants a floating pill | Allowed | Requires sticky header with shrink | **Spec.** Full-width sticky header on ivory, 80px to 64px. |
| Icon family | Phosphor Light | Any SVG family | Lucide only | **Spec.** Lucide, 1.5px. |
| Radii | `rounded-[2rem]` squircles | One consistent system | Silent | **Brief.** 24 / 16 / full, documented in section 3. |
| Pill CTAs | Yes | Silent | Silent | **Brief.** 16px radius, not pills, so buttons match inputs. |
| Nested "double bezel" surfaces | Everywhere | Cards only where hierarchy is real | Silent | **Soft-skill on surface**, ui-ux on where: panels and the nested icon disc get it; body copy sits on the ground. |
| Eyebrow pills above every H2 | Wanted | Budget of ceil(n/3) | Silent | **Taste.** Zero eyebrows. |
| Serif display | Discouraged by taste | Same | Brief names Cormorant | **Brief.** |
| Three equal product cards | Banned by taste | Same | Requires three paths | **Spec.** Three cards, deliberately not identical: each carries a different CTA weight. |
| `backdrop-filter` on the mobile nav | Wanted | Reduced-transparency caveat | Brief bans glassmorphism | **Brief.** Solid surface. |
