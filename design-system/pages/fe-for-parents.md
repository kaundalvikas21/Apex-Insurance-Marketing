# /final-expense-insurance/for-parents/

Deviations from MASTER.md. Everything not listed here is inherited.

**The only final expense page that does not set `HTML_CLASS = "fe"`.** The senior accessibility
mode exists because the reader is 60 to 85. On this page the reader is the adult child, typically 30
to 55, and the spec says standard type sizes are fine here. So this page keeps the sitewide type
ramp, the ambient glow, `.reveal`, and `data-stagger`. What it does not keep is the register: the
copy stays as calm and unhurried as the rest of the silo, because the subject is still a parent's
death.

**The one CTA exception in the silo: form weighted, not phone first.** `FE.callback_form()` sits in
a `.panel` on the left with the amber submit, and the phone CTA sits beside it as a full-width
`.btn-call` rather than being dropped. Form weighted means the form gets the amber and the panel; it
does not mean the phone disappears. A decision about somebody else's health produces questions a
four-field form cannot take.

**The form uses prefix `fe-parents` and `data-form-name="fe_for_parents_callback"`.** Both must stay
unique to this page: the prefix namespaces every id including the TCPA consent checkbox and the
success panel, and the form name is what makes the GA4 `form_submit` event distinguishable from the
hub's.

**The consent objection is answered in the hero, not in an FAQ.** Second sentence of the lead: your
parent has to know and has to sign, and a policy taken out without them is void. It is the first
thing a reader arriving on this query needs and the one thing on the page that is not negotiable, so
it goes above everything else rather than seventh in an accordion.

**Three rules bento, then two prose sections in a fixed order:** how to actually do it (four steps),
then how to raise it without a row (four `chrome.qa()` pairs). The conversation section is not
padding. For most readers it is the actual blocker, and it is placed after the mechanics because a
reader who does not yet know what they are proposing cannot rehearse proposing it.

**The "have this ready" card is a `.card` inside a light section**, so its `<h3>` needs no
`!text-ink`. If that card is ever moved into a `.band-navy`, it does.
