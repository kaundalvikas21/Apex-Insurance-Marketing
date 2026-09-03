# /whole-life-insurance/is-it-worth-it/

Deviations from MASTER.md. Everything not listed here is inherited.

**The softest CTA on the site.** No amber, no form, no `chrome.inline_cta()`, and no button
hierarchy. The single ask is a text link inside a card near the end, and it offers a document ("we
will put a term quote and a whole life illustration next to each other") rather than a call. The
spec says this page earns trust and links and is not a sales page; the layout has to agree with the
copy or the copy is not credible.

**The byline is placed directly under the hero**, using `chrome.byline_section(cls="section-tight")`,
and the page does not carry a second one at the foot. This is the only page on the site that moves
it. The argument being made is "here is the case against the thing we sell", and who is making that
argument is part of the argument. Burying the named agent at the foot of a page whose whole value is
disclosure would be the wrong call.

**"Who whole life is not for" comes before "who it genuinely is for".** Four failure cases as
numbered `chrome.step()` rows, then three fit cases as a bento. Reversing the order turns the page
into a sales page with a balanced headline, which is the exact failure mode the spec is warning
about. The four negative cases must also stay longer than the three positive ones.

**The conflict of interest is disclosed in the hero**, in the last sentence of the lead: "we sell
the product, which is a conflict of interest you should hold in mind while reading it." Do not move
it lower or soften it. It is the sentence that makes the rest of the page worth reading.

**No cost figure, no multiple, no rate of return anywhere.** The page says the cost gap is "a large
multiple, not a small markup" and then explicitly refuses to print one, because any figure chosen
would be doing the arguing. The two `$--` rate pages are linked instead. This is not an oversight
waiting on rate cards: even with rate cards loaded, this page states the shape and links the
numbers.

**"What the critics get right" is longer than "what the critics get wrong".** Deliberate. The
concessions are real concessions, including the one about front-loaded commissions applying to this
agency, and must not be trimmed to restore symmetry.

**The six checks use `compare.checklist()`**, the T5 helper, rather than a bespoke list. One of the
six asks the reader to demand the agent's compensation on the policy. That check stays.
