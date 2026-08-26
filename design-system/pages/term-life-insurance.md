# Page override: Term Life Insurance hub (`/term-life-insurance/`)
Inherits `design-system/MASTER.md`. Only deviations are listed.

- **CTA weighting:** form first. The three-step form is the hero's right `.panel`, above the fold
  at 1024. Phone lives in the sticky header.
- **Hero:** `.glow`. h1, lead, four check facts, "what happens after you submit".
- **What it covers:** split with the `term-home` photograph (glow), then a three-cell bento led by
  a `.bento-cell-blue` coverage-range stat (`$2,000,000`, counts up) beside the "fits" and "look
  elsewhere" cells.
- **Term lengths:** four segmented choices rendered as stat cells in a `.bento` (`10 / 15 / 20 /
  30`, count-up). The checked cell fills navy. They still drive `[data-panels="term-lengths"]`.
- **Rates:** `.table-signature`. Toggles above (7fr 4fr 4fr), `$--` cells by decision, `[PLACEHOLDER]`
  flag above, dated `.pill` beneath. `.reveal` sits on the scroll container, never on a wrapper
  around it (a transformed wrapper leaks the table's width into the page until it reveals).
- **No-exam teaser:** navy band. **Carriers:** white strip directly after it.
- **How to apply:** `chrome.step()` trio.
- Layout families in order: hero + panel, strip, split + bento, selector + card, table, timeline,
  navy band, strip, step trio, tile grid, accordion, byline, split + panel. Eyebrow budget 4, used 1.
