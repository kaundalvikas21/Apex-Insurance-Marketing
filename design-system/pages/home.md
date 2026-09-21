# Page override: Home (`/`)
Inherits `design-system/MASTER.md`. Only deviations are listed.

- **Purpose:** get a first-time visitor to a quote or a call in plain language. Links to the three
  hubs, never to spokes. Reframed to the client outline in September 2026.
- **Hero:** `chrome.page_hero(None, ..., banner="home-banner")`. h1, one lead, one CTA with its micro
  line, over the full-bleed client photograph (the page's one eager image; anchored `right 85%`
  because the family sits low in the frame). No breadcrumb, no `.glow`, no product cells, no link
  line. `home-hero` survives only as the OG image.
- **USP strip:** four icon tiles directly beneath the hero CTA. Built by `chrome.usp_strip()`, shared with the three hubs. The icon circle reuses `.step-num`.
  `[X]` placeholders stay visible; nothing here counts up.
- **How it works:** `chrome.steps_section()`, a connected stepper, not `chrome.step()`. An `<ol class="steps">` of three items:
  a filled navy `.steps-node` on a dashed rail (on top from 768px, down the left below it) and a
  cell under each, white, tinted, blue, so the third lands as the destination. Each cell has a
  Lucide icon, a chip that carries no number ("A few minutes", "We do the work", "Your decision"),
  a title and one sentence. The CTA sits in its own `.steps-cta` strip with the no-SSN line.
- **Why us band:** solid navy, no photograph, no scrim. Four raised white-at-8% cells (`.bento-3`),
  not white cards and not glass, so headings stay white. The commission detail lives in the last
  FAQ answer, not here. The hidden reviews slot stays.
- **Coverage types:** three `.bento-2` cells (middle tinted), one sentence and one `.btn-row` hub
  link each, then exactly two buttons: call and quote.
- **Primary CTA repetition:** `/get-a-quote/` sits on three buttons (hero, steps, coverage). Repeated
  primary CTA buttons are the accepted exception to one link per target. Contextual text links are not.
- **Triage quiz:** deliberately not the FAQ's shape, because the two were being read as one. Centred
  heading, one wide `.quiz.panel` (56rem), the form `.progress-track`, and answers as `.triage-opt`
  tiles: icon circle (or a figure for the age question), bold label, one hint line. Three across
  from 768px, icon-left rows below. A pick sets `aria-pressed`, shows a navy ring and a check badge
  for 240ms (0 under reduced motion), then advances. Back link on questions 2 and 3. The result is
  a centred "Your best fit" card. `<noscript>` explains itself instead of showing an empty card.
  This is the page's one centred section.
- **Dialog:** one native `<dialog data-dialog-timed>` for the free policy review, emitted by this
  page only. No form inside it. It never opens while the quiz is on screen or holds focus: the
  quiz sits at the dialog's own 50% scroll trigger.
- **Final CTA:** two hover cards, not a divided row.
- Layout families in order: hero, strip, stepper + CTA strip, navy bento, bento + button pair, form panel
  (triage), accordion, card pair. Eyebrow budget 3, used 0.
