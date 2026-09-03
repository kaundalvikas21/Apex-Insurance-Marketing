# /term-life-insurance/no-medical-exam/

Deviations from MASTER.md. Everything not listed here is inherited.

**Treated as near-money, not as a standard T4.** The spec's per-silo note puts the form and the
phone at equal weight on this page and asks for a denser CTA rhythm than an informational page
would carry. The visitor has usually already decided to buy and is looking for a reason not to be
examined, which is the highest intent state in this silo.

**Three asks instead of one.** Hero (amber anchor button plus a navy call button), a phone-first
`inline_cta` at mid page, and the form section itself. That is the only page in the P2 layer with
more than one CTA block.

**The form is on the page.** `term.quote_form()` is reused with its own `form_id`, `form_name`, and
id prefix (`tnx`), the same pattern `/term-life-insurance/rates/` uses. Two reasons:

- Three separate links to `/term-life-insurance/quotes/` would break spec s07 rule 4. The hero
  button and the mid-page CTA therefore point at `#quote` on this page, and the spoke module keeps
  the one canonical link to the quotes page.
- An objection page that answers the objection and then sends the reader elsewhere to act on it
  throws away the intent it just earned.

**`#who-qualifies` is a contract.** The term hub's no-exam banner deep-links to it. It sits on the
three-routes section. `check.py` strips fragments when it crawls links, so nothing will catch this
if the id is removed: see REPLACE-BEFORE-LAUNCH.md section 6.

**Compliance.** Nothing on the page promises approval. The "what same day actually means" section
states that same day means a same-day decision, not always an approval and not always a yes, and
that coverage starts when the policy is in force rather than at approval.
