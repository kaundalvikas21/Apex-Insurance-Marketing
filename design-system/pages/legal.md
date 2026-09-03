# Page override: Legal documents (`/legal/privacy/`, `/legal/terms/`, `/legal/disclaimer/`)
Inherits `design-system/MASTER.md`. Only deviations are listed. One doc covers all three: they share a body builder and differ only in content.

- **Built by `chrome.legal_doc(heading, standfirst, sections)`.** `sections` is `[(id, title, body_html)]`; each page module is a list of sections and nothing else.
- **Every section carries an id,** because people arrive at a privacy policy looking for one clause and link to it. `scroll-mt-28` keeps a jumped-to heading clear of the sticky header.
- **Sticky TOC** in three columns (`.sticky-col`), sections in eight at `.measure` (68ch). Numerals in the TOC and the headings are `.tnum`, so a two-digit section does not shift the list.
- **`[PENDING LEGAL REVIEW]` renders as a visible `.flag`,** above the table of contents, not only as a comment. A policy a visitor cannot rely on must not look like one they can. This is the one place the flag outranks the reading experience.
- **Dated `.pill`** under the standfirst carries the last-updated date, using `REVIEW_DATE` until counsel sets a real one.
- **Breadcrumb is two levels** (`Home > Privacy policy`), matching the BreadcrumbList exactly. There is no `/legal/` index page, so an unlinked "Legal" crumb would put `aria-current` on a non-current item and describe a path the schema does not.
- **Sibling tiles close every page.** The three documents cross-link, which is the one correct sideways link between non-silo pages: someone reading the privacy policy is usually looking for the disclaimer.
- **No glow, no photography, no bento.** Legal copy at a readable measure, and nothing competing with it.
- Layout families in order: hero + flag, TOC + sections, tile trio. Eyebrow budget 1, used 0.
