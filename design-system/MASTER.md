# Apex Insurance Marketing — Design System
## Variation 1: "Institutional Trust"

**Design read:** trust-first consumer insurance hub for three distinct age cohorts, Swiss /
institutional language, leaning toward Tailwind v4 tokens + Libre Caslon Text display + Inter UI,
with reveal-only motion.

**Dials:** `DESIGN_VARIANCE: 4` · `MOTION_INTENSITY: 3` · `VISUAL_DENSITY: 5`

Single source of truth for the five-page build. `src/input.css` implements every token here; if the
two disagree, this file is wrong and gets updated, not the other way around.

---

## 1. Palette

| Token | Hex | Role |
|---|---|---|
| `--color-navy` | `#0A2540` | Primary. Headlines, header, footer, phone CTA fill. |
| `--color-navy-700` | `#173F63` | Navy hover, secondary navy surfaces. |
| `--color-navy-050` | `#EAF0F6` | Tinted band background, table header fill. |
| `--color-slate` | `#425466` | Body text. |
| `--color-muted` | `#5A6B80` | Secondary text, captions, table sub-labels. |
| `--color-cream` | `#F6F9FC` | Page ground (warm white). |
| `--color-surface` | `#FFFFFF` | Cards, form panels, table rows. |
| `--color-gold` | `#C9A227` | **CTA ONLY.** |
| `--color-gold-700` | `#B08E1E` | CTA hover. |
| `--color-green` | `#1F7A5C` | Positive / covered / included states. |
| `--color-rule` | `#DFE6EE` | Decorative hairlines, card borders. |
| `--color-border-strong` | `#7B8CA0` | Form input borders (needs 3:1 per WCAG 1.4.11). |
| `--color-flag` | `#8A6D1F` | Placeholder / pending-review notice text. |

### The gold rule (non-negotiable)
Gold appears on call-to-action buttons and on the focus ring over navy backgrounds. Nowhere else.
Not on icons, not on hairlines, not on hover states of non-CTA elements, not on headline accents.
If gold appears twice in a viewport and only one of them is a CTA, that is a bug.

### Verified contrast pairs
| Pair | Ratio | Verdict |
|---|---|---|
| Navy on cream | 14.8:1 | AAA |
| Slate on cream | 7.4:1 | AAA |
| Muted on cream | 5.2:1 | AA |
| **Navy on gold** (primary CTA) | **6.5:1** | AA, AAA at large |
| Navy on gold-700 (CTA hover) | 5.0:1 | AA |
| White on navy (phone CTA) | 15.6:1 | AAA |
| Green on cream | 5.0:1 | AA |
| Border-strong on cream | 3.3:1 | Passes 1.4.11 for inputs |

Primary CTA is **navy text on gold fill**, never white on gold (that pair is 2.4:1 and fails).

### Focus
Default focus ring: 3px navy, 2px offset. On navy surfaces the ring flips to gold (6.5:1 against
navy). Never `outline: none` without a replacement.

---

## 2. Typography

Self-hosted latin-subset woff2 in `/assets/fonts/`, `font-display: swap`. No Google Fonts request:
one fewer third party on pages that collect PII, and one fewer render-blocking origin.

- **Display / H1 / H2:** Libre Caslon Text (400, 700). Chosen over Fraunces deliberately: Fraunces
  is the current AI-default serif and reads as templated. Caslon reads as legal, institutional,
  and old, which is exactly the register an insurance agency wants.
- **Body / UI / tables:** Inter (variable 100 to 900).
- **Tabular numerals** (`font-variant-numeric: tabular-nums`) on every rate table, every premium
  figure, every coverage amount. Non-negotiable: columns of money must align.

### Ramp (base 16px)
| Token | Size | Line height | Face |
|---|---|---|---|
| `text-display` | clamp 2.5rem to 3.75rem | 1.05 | Caslon 700 |
| `text-h1` | clamp 2.25rem to 3.25rem | 1.1 | Caslon 700 |
| `text-h2` | clamp 1.75rem to 2.5rem | 1.15 | Caslon 700 |
| `text-h3` | 1.375rem | 1.3 | Inter 600 |
| `text-h4` | 1.125rem | 1.4 | Inter 600 |
| `text-lead` | 1.1875rem | 1.6 | Inter 400 |
| `text-body` | 1rem | 1.65 | Inter 400 |
| `text-sm` | 0.875rem | 1.55 | Inter 400 |
| `text-micro` | 0.8125rem | 1.5 | Inter 500 |

Measure caps at 68ch for body copy, 34ch for display headlines.

### Final-expense override
`<html class="fe">` redefines the type tokens **on `main`**, not on `html`. Inside the page content
the ramp moves up a notch: body 18px, lead 21px, h3 24px, and the `sm` and `micro` steps collapse
into the body size so nothing on that page renders below 18px. Hierarchy there comes from weight
and colour, not from shrinking the type.

Scoping to `main` matters. Putting the bump on `html` also scales every rem-based padding and gap
in the shared header, and the nav overflows at 1440. The header and footer stay at the sitewide
scale on every page, including this one.

Also on that page: minimum tap target rises to 56px, paragraph max-width drops to 58ch, and no
paragraph runs past three sentences.

---

## 3. Grid and spacing

Swiss 12 column. Container `max-width: 1200px`, gutter 24px, 32px at 1024 and up. **Declared in
px, not rem**, so the final-expense type bump cannot widen the grid: every page shares one grid.
Breakpoints tested: **375 / 768 / 1024 / 1440**.

Spacing scale (4px base): `4 8 12 16 24 32 40 48 64 80 96 128`.
Section rhythm: `py-20` mobile, `py-28` at 768, `py-32` at 1024. Band sections (tinted) keep the
same rhythm so the page reads as one grid, not stacked blocks.

Hairline rules at 1px `--color-rule` carry the Swiss structure. Cards use a 1px rule plus white
fill, never a drop shadow, except the two elevated form panels (hero forms) which get a single
soft shadow to lift them off the band.

Corner radius: **one system.** `2px` on everything (inputs, buttons, cards, tables). The near-square
corner is the institutional signal. No `rounded-full` anywhere except the step-progress dots.

---

## 4. Motion (MOTION_INTENSITY 3)

| Pattern | Spec |
|---|---|
| Section reveal | opacity 0 to 1 + translateY 12px to 0, 480ms `cubic-bezier(.22,1,.36,1)` |
| Stagger | 60ms per child, capped at 6 children |
| Link underline | grows from left, 180ms ease-out |
| CTA hover | translateY(-2px) + shadow, 180ms |
| Accordion | native `<details>`, 200ms on the panel |
| Form step change | 240ms crossfade, focus moves to the first field of the new step |

Trigger with `IntersectionObserver` only. No `scroll` listeners anywhere in the codebase.

`prefers-reduced-motion: reduce` collapses everything to opacity-only at 1ms, and reveals are
forced visible so no content can be trapped invisible.

**Final-expense page:** reveal is opacity-only with no translate, no stagger, and no CTA lift.
Motion on a page built for 60 to 85 year olds is a liability, not a delight.

---

## 5. Component contracts

| Component | Contract |
|---|---|
| `.btn-cta` | Gold fill, navy text, 600 weight, min-height 48px, 2px radius. The only gold thing. |
| `.btn-call` | Navy fill, white text, phone icon, min-height 48px. Large variant 64px for final expense. |
| `.btn-ghost` | Transparent, navy text, 1px navy rule. Tertiary only ("Request an illustration"). |
| `.card` | White fill, 1px rule, 2px radius, 24px pad. No shadow. |
| `.rate-table` | Tabular nums, navy-050 header, hairline row rules, horizontal scroll container on mobile with a visible affordance. |
| `.field` | Label above input, 48px input, border-strong, error text below wired via `aria-describedby`. The error line is **always in the layout** and only toggles `visibility`: if it appeared on demand it would push the button beneath it down between mousedown and mouseup, and the click would land on nothing. |
| `.trust-strip` | Hairline top and bottom, muted micro text, sits within one viewport of its CTA. |
| `.flag` | Visible placeholder notice. Left rule in `--color-flag`, flag-colored micro text. Renders on the page, not only in comments. |

Icons: **Lucide only**, inlined as SVG, 1.5px stroke, 20px or 24px, `aria-hidden="true"` with the
meaning carried by adjacent text.

---

## 6. Per-page overrides

**Home.** Triage, not pitch. Three product paths each carry its own silo's CTA weighting, so the
three cards are deliberately *not* visually identical: term gets a gold form CTA, whole life gets a
gold CTA plus a navy phone CTA, final expense gets the navy phone CTA at larger size. Layout
families alternate (split, band, grid, two-column, split) so no two adjacent sections repeat.

**Term hub.** Form-weighted. Multi-step form is the hero's right column, elevated panel, above the
fold at 1024. Phone is present in the sticky header only. Rate table rows prefill the form.

**Whole-life hub.** Dual CTA at genuine parity: same height, same width band, same optical mass.
Gold on the form CTA, solid navy on the phone CTA. Parity is by weight, not by both being gold.
Section 7b ("who this does not suit") gets identical prominence to 7a, side by side at 1024, and is
the strongest E-E-A-T signal on the page.

**Final-expense hub.** Phone-first. See the type override in section 2. Phone CTA above the fold at
display size, repeated after sections 4, 6, and 8. Rate table rows carry *call* buttons, not quote
buttons. Reveal-only motion.

**Contact.** Split layout, designed success state rendered in place, never `alert()`.

---

## 7. Banned

No purple or pink gradients. No neon. No dark mode. No emoji as icons. No section-number eyebrows
(`01 / Coverage`). No scroll cues. No centered-everything pages. No Fraunces. No drop shadows on
content cards. No `rounded-2xl` soft-SaaS corners. No stock-photo smiling families as decoration.
No em-dash anywhere in rendered copy: use a comma, a colon, a period, or a middot separator.
`tools/build.py` fails the build if one appears, entity forms included.
No invented rates, reviews, carrier names, or dollar claims.

Eyebrow budget per page: `ceil(sectionCount / 3)`.
