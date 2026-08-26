# Apex Insurance Marketing, Design System
## Variation 4: "Modern Independent"

**Design read:** editorial agency confidence adapted for YMYL. Oversized Fraunces display headlines
clamped to 7vw, asymmetric splits on a 12 column grid with visible column rules, uppercase
micro-labels with wide tracking, Bone ground, Ink type, one deep navy section per page, Signal
Orange on CTAs and key underlines only. Trust discipline is the mandatory offset for the boldness.

**Dials:** `DESIGN_VARIANCE: 7` · `MOTION_INTENSITY: 5` · `VISUAL_DENSITY: 5`
(final-expense page: `DESIGN_VARIANCE: 3`, `MOTION_INTENSITY: 1`, same tokens).

Single source of truth for the five-page build. `src/input.css` implements every token here; if the
two disagree, this file is wrong and gets updated, not the other way around.

**Skill precedence, as briefed.** ui-ux-pro-max wins on accessibility and trust guidance (focus
rings, 48px targets, cursor states, transitions, high contrast, large type for seniors).
design-taste-frontend wins on layout discipline (eyebrow budget, section-layout variety, hero
economy, the anti-slop bans). The brief's direction wins on layout and typography where the
generator's insurance conservatism disagrees: Fraunces is used despite both skills' generic
"no Fraunces" default because the brief names it, and the trust rail sits inside the hero because
the brief requires licensing, independence, and the carrier strip above the fold on every page.
The compliance spec beats all three.

**Decisions carried from the client conversation, not to be reverted.** Rate and cost cells stay
`$--` with the placeholder banner (no marked sample figures either). Photography is v1's set, used
in fewer, larger frames: six of nine slots placed. The sticky-stack is CSS-native, no GSAP.

---

## 1. Palette

| Token | Hex | Role |
|---|---|---|
| `--color-cream` | `#F2EFE9` | **Bone.** Page ground. (Token name kept; value is Bone.) |
| `--color-ink` | `#16181D` | Text, headlines, footer ground, rules that carry structure. |
| `--color-navy` | `#12224A` | The one deep navy section per page. |
| `--color-navy-700` | `#1C3270` | Navy hover, chart value line. |
| `--color-navy-050` | `#E4E6EE` | Chart fill, media placeholder ground. |
| `--color-slate` | `#4A4F5A` | Body text. |
| `--color-muted` | `#5E6470` | Secondary text. The floor: nothing lighter carries text on bone. |
| `--color-surface` | `#FFFFFF` | Panels, cards, alternate bands, table rows. |
| `--color-gold` | `#E8542E` | **Signal Orange. CTA fill and key underlines ONLY.** (Token name kept so the `.btn-cta` contract and the grep check still work.) |
| `--color-gold-700` | `#B03A1A` | Orange as text or a focus ring on a checked orange-adjacent control. |
| `--color-green` | `#196A4F` | Positive / covered / included states. |
| `--color-rule` | `#D9D4CB` | Hairlines, card borders, column rules. |
| `--color-border-strong` | `#7F7A71` | Form input borders (3:1 per WCAG 1.4.11). |
| `--color-flag` | `#74590F` | Placeholder / pending-review notice text on `--color-flag-050`. |
| `--color-danger` | `#A32020` | Validation errors. |

### The orange rule (non-negotiable)
Signal Orange appears as the fill of `.btn-cta` and `.btn-call`, as the 2px underline on the
active and hovered nav link, and as the `.u-key` underline under one key phrase in a headline
(maximum one per section). Nowhere else. Not on icons, not on hairlines, not on hover states of
non-CTA elements, not as body text. Mechanically checkable:
`grep -o "var(--color-gold)" assets/site.css | wc -l` is 3 (CTA fill, nav underline, key underline).

### Verified contrast pairs (computed, not eyeballed)
| Pair | Ratio | Verdict |
|---|---|---|
| Ink on bone | 15.5:1 | AAA |
| Slate on bone | 7.2:1 | AAA |
| Muted on bone | 5.2:1 | AA |
| **Ink on Signal Orange** (CTA label) | **4.85:1** | AA. The label is Ink, never white. |
| White on Signal Orange | 3.7:1 | **Fails.** Never used. |
| Ink on a darker orange hover fill | 4.2:1 | **Fails.** The fill does not change on hover. |
| Orange on bone (underline, non-text) | 3.2:1 | Passes 1.4.11 |
| Orange on navy (button fill against the band) | 4.2:1 | Passes 1.4.11 |
| Bone on navy | 13.5:1 | AAA |
| Bone on ink (footer) | 15.5:1 | AAA |
| Orange-700 on bone (text) | 5.3:1 | AA |
| Green on bone | 5.7:1 | AA |
| Flag on flag-050 | 6.1:1 | AA |
| Danger on bone | 6.6:1 | AA |
| Border-strong on bone / on white | 3.7:1 / 4.3:1 | Passes 1.4.11 for inputs |

### Focus
Default focus ring: 3px Ink, 2px offset. On navy and on the ink footer the ring flips to bone.
A checked choice chip (ink fill) flips the ring to orange-700. Never `outline: none` without a
replacement.

---

## 2. Typography

Self-hosted latin-subset woff2 in `/assets/fonts/`, `font-display: swap`, both variable, both
under the SIL Open Font License, fetched once from Google Fonts. No third-party request on pages
that collect PII.

- **Display / H1 / H2 / H3 / accordion questions / table column heads:** Fraunces, weight 600
  (700 for the wordmark), `font-variation-settings: "opsz" 144` at display sizes and `48` at
  h3 and below. The heavy optical size is the editorial signal; it is never used below 20px.
- **Body / UI / labels / tables:** Inter Tight (variable 100 to 900).
- **Micro-labels (`.eyebrow`):** Inter Tight 600, 12px, uppercase, 0.14em tracking, Ink. They name
  the topic in plain language and never enumerate.
- **Tabular numerals** on `body`: every figure ends up in a column sooner or later.

### Ramp (base 16px)
| Token | Size | Line height | Face |
|---|---|---|---|
| `text-display` | clamp 2.625rem to 7vw to 5.5rem | 0.98 | Fraunces 600, opsz 144. Home hero only. |
| `text-h1` | clamp 2.5rem to 5.5vw to 4.5rem | 1.02 | Fraunces 600, opsz 144 |
| `text-h2` | clamp 2rem to 3.6vw to 3rem | 1.08 | Fraunces 600, opsz 144 |
| `text-h3` | 1.5rem | 1.25 | Fraunces 600, opsz 48 |
| `text-h4` | 1.125rem | 1.4 | Inter Tight 600 |
| `text-lead` | 1.1875rem | 1.55 | Inter Tight 400 |
| `text-body` | 1rem | 1.6 | Inter Tight 400 |
| `text-sm` | 0.875rem | 1.55 | Inter Tight 400 |
| `text-micro` | 0.8125rem | 1.5 | Inter Tight 500 |

The display clamp stops at 5.5rem (88px) so "who depend on you." holds one line in a 7 column
hero at 1440. Measure caps at 68ch for body, 58ch for lead copy inside stack cards.

### Final-expense override
`<html class="fe">` redefines the type tokens **on `main`**, not on `html`. The editorial display
sizes are pulled back to a calm scale (h1 clamp 2.375rem to 3.125rem, h2 to 2.5rem), body is
19px, lead 22px, and the `sm` and `micro` steps collapse to 18px so nothing on that page renders
below 18px, including the state `<select>`. Fraunces stays for headings, at calm sizes with
normal tracking. Verified in the browser: zero text nodes under 18px inside `main`, at 375 and
1440, outside the native option list.

Scoping to `main` matters. Putting the bump on `html` also scales every rem-based padding and gap
in the shared header, and the nav overflows at 1440.

Also on that page: buttons 56px, inputs and choice chips 56px, accordion summaries 56px, the
consent checkbox 28px, inline text links get a 48px hit area through padding with negative
margins, paragraph max-width 58ch.

---

## 3. Grid and spacing

### The row rule
A block may be narrow **only if something else occupies the rest of its row.** No section may
leave more than 20% of its content row empty on the right, and no two-column row may differ in
column height by more than 250px. Where v4 wants asymmetry it composes the row (7/5, 6/6, 5/7,
4/8) rather than leaving the remainder blank.

12 column grid. Container `max-width: 1200px`, gutter 24px, 32px at 1024 and up. **Declared in
px, not rem**, so the final-expense type bump cannot widen the grid. Breakpoints tested:
**375 / 768 / 1024 / 1440**.

### Asymmetric splits and visible structure
Hero and section splits are deliberately unequal: 7/5 (home hero, term covers), 5/7 (term hero,
form left by CSS order with the H1 first in the DOM), 6/6 at parity only where the spec demands
parity (whole-life dual CTA, suits / does-not-suit), 4/8 (sticky heading beside a stack). The
second column of a split carries `.col-rule`, a 1px `--color-rule` left border at 1024 and up.
Ruled three-column rows use `divide-x`. Section openers use `.rule-ink`, a 2px Ink top rule.
These rules separate content; there are no hairlines as pure decoration.

Spacing scale (4px base): `4 8 12 16 24 32 40 48 64 80 96 128`.
Section rhythm: `py-20` mobile, `py-26` at 768, `py-32` at 1024. Bone and white bands alternate;
navy appears exactly once per page; the footer is Ink so the navy rule stays visibly true.

Corner radius: **one system.** `2px` on everything. The near-square corner is the editorial and
institutional signal at once. Nothing is `rounded-full`.

Shadows: none on content. The hero form panels carry `--shadow-panel`; stack cards carry a soft
upward shadow so the deck reads as layered. The stuck header is the one translucent surface, with
`@supports not (backdrop-filter)` and `prefers-reduced-transparency` fallbacks.

---

## 4. Motion (MOTION_INTENSITY 5)

CSS keyframes, one IntersectionObserver reveal, and CSS scroll-driven animations behind
`@supports`. No animation library, no scroll listener, no GSAP.

| Pattern | Spec | Applies to |
|---|---|---|
| Kinetic line reveal | authored `.line` spans, translateY .35em + opacity, 600ms, 90ms stagger, on load | Home hero H1 only |
| Section reveal | opacity 0 to 1 + translateY 12px to 0, 480ms `cubic-bezier(.22,1,.36,1)` | Headings, blocks |
| Stagger | `data-stagger="<ms>"` per child (40 to 80ms), capped at 6 | Path cards, spoke grid, ruled rows |
| Sticky stack | `position: sticky` deck, each card a notch lower; card i scales to .94 and dims (`filter: brightness(.9)`, not opacity) on card i+1's view timeline, `entry 0% to 100%` | Home "how we work", term "how to apply" |
| Marquee | 40s linear translateX(-50%) over a duplicated track, paused on hover and focus, Pause button with `aria-pressed` | Carrier strip in the trust rail, one per page |
| Magnetic CTA | `translate` follows the pointer up to 6px, springs back, fine pointers only | Header CTA, hero primary CTA, final CTA |
| Row cascade | 34ms per row, opacity + translateY 6px | Rate and comparison tables |
| Sticky column | `position: sticky` on the heading column | Stacks, underwriting timeline |
| Nav underline | 2px orange grows from left, 180ms | Nav links |
| CTA hover | translateY(-2px) + orange-tinted shadow, fill unchanged | Buttons |
| Accordion | height via `interpolate-size: allow-keywords`, 240ms, icon rotates 45deg | FAQ |
| Chart draw-on | `stroke-dashoffset`, 1.4s | Cash-value chart |
| Form step change | 240ms crossfade, focus moves to the first field | Term multi-step form |

**Why the stack dims with brightness, not opacity.** The cards overlap; a translucent card shows
the card beneath it. **Why card i animates on card i+1's timeline.** A stuck element's own view
timeline stalls; the card arriving underneath is the one still moving. The timeline names are
inline so the `animation` shorthand cannot reset them.

**Deliberately absent.** Parallax and mask wipes (v1). Count-ups (v3): every figure is a
placeholder. Scroll-progress bars and scroll cues (section 7 bans). Pinned scrub sequences
beyond the stack. GSAP: the taste-skill skeleton was rebuilt in CSS because the site ships zero
dependencies and makes no runtime request off-domain.

### Reduced motion
`prefers-reduced-motion: reduce` collapses everything to opacity at 1ms: no kinetic reveal, the
stack becomes a plain list, the marquee becomes a static wrapped row with its Pause button and
duplicate group hidden, the magnetic pull is off, every reveal is forced visible.

### Final-expense exemption
`.fe main` opts out of every pattern above except the opacity reveal: no kinetic headline, no
stack (plain list), static carrier row, no magnetic pull, no row cascade, no CTA lift, no sticky
column. Fades only.

This is an accessibility decision, not a stylistic one. Vestibular sensitivity and low vision both
rise sharply in the 60 to 85 band this page is built for, and the spec calls senior accessibility
conversion work here.

---

## 5. Component contracts

| Component | Contract |
|---|---|
| `.btn-cta` | Orange fill, **Ink** label, 600 weight, min-height 48px, 2px radius. Hover lifts, never recolours. |
| `.btn-call` | Same fill and label as `.btn-cta` (a phone CTA is a CTA; one accent). `.btn-xl` 64/72px on final expense. |
| `.btn-ghost` | Transparent, Ink text, 1.5px Ink rule; inverts on navy and the footer. Tertiary only. |
| `.btn-row` | Table-row action, 40px, 1px Ink rule, inverts on hover. 48px on final expense. |
| `.eyebrow` | Uppercase micro-label, 0.14em tracking, Ink. Budget `ceil(sections / 3)` per page, hero counts. |
| `.u-key` | One orange underline under one key phrase in a headline. Max one per section. |
| `.rail` | Trust rail: 2px Ink top rule, licensing line + NPN, independence statement, years, compact byline (hubs), carrier marquee. Sits directly under the hero CTA on every page, inside the first viewport. |
| `.marquee` | Duplicated `.marquee-group` track, `aria-hidden` copy, Pause button, `.marquee-static` for the senior page. One per page. |
| `.stack` / `.stack-card` | Sticky deck, `--stack-i` offset, 58svh min-height at 768+, inline view timelines. Never carries `.reveal` itself. |
| `.step-num` | 40px ruled square with a Fraunces numeral. Flat step rows. |
| `.card` | White fill, 1px rule, 2px radius, 24px pad. No shadow. |
| `.panel` | The hero form panels. White, 1px rule, `--shadow-panel`. |
| `.tile` | Spoke link: bone on white, 1px rule, hover to Ink rule and arrow shift. |
| `.rate-table` | `border-collapse: separate`, one rule per row boundary, bone header with a 2px Ink rule, sticky first column under 768px. Lives in a **positioned** `.table-scroll` so its `sr-only` heads cannot widen the page. |
| `.compare-table` | Fraunces column heads, bone row heads, one rule per boundary. Final-expense version uses `rowgroup` label rows to stay at three columns. |
| `.field` | Label above input, 48px input, border-strong, error line always in the layout, toggling `visibility` only. |
| `.acc` | Fraunces 20px question, 2px Ink rule above the first item, hairline between items, plus icon rotates. |
| `.site-header` | Bone, 1px rule, 76px, shrinks to 60px and goes translucent when stuck. |
| `.site-footer` | Ink ground, bone text. |
| `.flag` | Visible placeholder notice. Renders on the page, not only in comments. |

Icons: **Lucide only**, inlined as SVG, 1.5px stroke, 18 to 26px, `aria-hidden="true"` with the
meaning carried by adjacent text.

---

## 6. Per-page overrides

See `design-system/pages/*.md` for the full per-page notes. In brief: home is triage with the
kinetic headline, the only one; term is form-first with the form visually left; whole life keeps
the two panels at parity and the suits / does-not-suit pair at equal weight; final expense drops
every editorial device to a calm 19px single register; contact is a 5/7 split with the licence
statement as its navy section.

---

## 7. Banned

No purple or pink gradients. No neon. No dark mode. No emoji as icons. No section-number eyebrows
(`01 / Coverage`): the stack numerals are content inside a card, not eyebrows. No version labels.
No decoration strips. No scroll cues. No centered-everything pages. No hairline grids as
decoration; every rule separates two things. No `border-top` plus `border-bottom` on the same
table row. No orange outside the three rules in section 1. No white text on orange. No opacity on
overlapping stack cards. No `.reveal` on a scroll container's wrapper or on a stack card. No
Fraunces below 20px. No marquee on the final-expense page. No second marquee on any page.
No em-dash anywhere in rendered copy: use a comma, a colon, a period, or a middot separator.
`tools/build.py` fails the build if one appears, entity forms included.
No invented rates, reviews, carrier names, or dollar claims.

**Photography.** Posed joy at the camera is banned. The two rules with no exceptions:

1. **No photograph of a person beside the agent byline.** Presenting a stranger as
   "[Agent Name], Licensed Agent" fabricates a person, the same failure as an invented testimonial.
2. **No image captioned or positioned to imply the person shown is a customer.**

Eyebrow budget per page: `ceil(sectionCount / 3)`.

---

## 8. Imagery

### Art direction
Documentary, no eye contact with the camera. Hands, backs, thresholds, kitchen tables, a window,
a porch. If a frame could carry the caption "happy family enjoys peace of mind," it is the wrong
frame. Photographs are atmospheric; none evidences anything, so none may be positioned to suggest
it does: no photo beside a testimonial, a rate, a claim statistic, or the agent byline.

### Sourcing and licensing
Unsplash, downloaded and served locally. Nothing hotlinks at runtime. The Unsplash Licence does
**not** convey a model release, so identifiable people must be cleared or replaced before launch.
`assets/img/CREDITS.md` records every file; `REPLACE-BEFORE-LAUNCH.md` tracks the swap. The
manifest lives in `tools/images.py`; `python3 tools/images.py --fetch` is idempotent.

### Delivery
`<picture>` with AVIF then WebP then `<img>`, three widths, explicit `width` and `height`,
`sizes` matched to the real column, exactly one `loading="eager"` + `fetchpriority="high"` per
page (the LCP candidate), `alt=""` when decorative. Every frame carries a 1px 12% Ink plate edge.

### Placement
Six placements across five pages, fewer and larger than v1: home hero (eager), term covers,
whole-life permanence, final-expense hero and final section, contact left column. No text over
photography anywhere. No image near the triage widget, any table, the chart, the FAQ, the spoke
grids, or any byline.
