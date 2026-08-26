# Page override: Term Life Insurance (/term-life-insurance/)
Inherits design-system/MASTER.md. Only deviations are listed.

- Form-first. The multi-step panel is visually left (5 columns) by CSS `order`; the H1 column
  (6 columns, col-rule) stays first in the DOM. Trust rail with the compact byline spans beneath.
- Who fits / when to look elsewhere is a ruled two-column under a 2px Ink rule, not cards.
- `.reveal` sits on the rate table's scroll container itself, never on a wrapper around it, and
  `.table-scroll` is positioned so the `sr-only` column head cannot widen the page.
- Underwriting timeline drops its photograph; dots are Ink on a white band.
- The one navy section is the no-exam teaser. Carriers section is a static logo row (the marquee
  already lives in the rail; one per page).
- "How to apply" is the sticky-stack with the heading column pinned beside it.
- Layout families in order: split hero + rail / split + ruled pair / selector + card / table /
  timeline split / navy split / logo split / stack / tile grid / split accordion / byline card /
  split + panel.
- Eyebrow budget 4, used 3 (hero, what it costs, three steps).
