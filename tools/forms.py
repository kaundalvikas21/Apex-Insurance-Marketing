# -*- coding: utf-8 -*-
"""Form primitives shared by every quote and contact form on the site.

Split out of the page modules so the compliance-critical parts of a form are
authored once: the hidden source/silo fields, the honeypot, and the TCPA
consent block. Those three are what a reviewer checks, and a copy-pasted copy
is a copy that can drift.

Everything here emits markup that `assets/site.js` already knows how to drive:

    data-ax-form          initForm() binds validation, GA4, and the consent gate
    name="source_url"     filled with window.location.href on load
    name="silo"           filled from the form's data-silo
    name="form_name"      filled from the form's data-form-name
    name="company_website" honeypot, dropped from the payload
    data-consent          the TCPA gate; submission is blocked until checked
    data-success-target   id of the .success panel shown after a good submit

INDENTATION. These helpers are interpolated into hand-indented f-strings, so
every one takes `indent`: the column its block sits at in the caller. The first
line is emitted flush because the call site's own indentation already puts it
there. Get this wrong and the page still renders, it just reads badly in
View Source, which on a YMYL page people do.
"""
import textwrap

from icons import icon

# The error icon that sits in every .field-error line. Was inlined as raw SVG
# 20 times across term.py and final_expense.py before this moved here.
ERR = icon("circle-alert", 16, "shrink-0 mt-px")


def block(html, indent):
    """Re-indent a partial to its call site. First line flush, rest padded."""
    out = textwrap.indent(textwrap.dedent(html).strip("\n"), " " * indent)
    return out[indent:]


def scaffold(extra="", indent=12):
    """Hidden compliance fields plus the honeypot. Required on every form.

    `extra` is any page-specific hidden input, inserted before the honeypot so
    the three compliance fields stay together at the top where they are easy
    to find. The honeypot is positioned off-screen rather than display:none,
    because some bots skip fields that are not rendered.
    """
    extra = ("\n" + textwrap.indent(textwrap.dedent(extra).strip("\n"), "")) if extra.strip() else ""
    return block("""
<input type="hidden" name="source_url" value="">
<input type="hidden" name="silo" value="">
<input type="hidden" name="form_name" value="">%s
<div aria-hidden="true" style="position:absolute;left:-9999px">
  <label>Company website<input type="text" name="company_website" tabindex="-1" autocomplete="off"></label>
</div>
""" % extra, indent)


def consent_block(field_id, brand, indent=12):
    """TCPA consent. Separate, never pre-ticked, immediately above submit.

    The mechanics are enforced in site.js: the box is force-unchecked on load
    (browsers restore checkbox state on back-navigation) and submission is
    blocked with a visible error until it is ticked. The wording is the part
    that still needs counsel.
    """
    return block("""
<!-- TCPA consent. Separate, unchecked, immediately above submit.
     [PENDING LEGAL REVIEW] Wording must be approved by counsel and
     matched to current TCPA one-to-one consent rules before launch. -->
<div class="consent">
  <input type="checkbox" id="%(id)s-consent" name="tcpa_consent" value="yes" data-consent>
  <label class="consent-text" for="%(id)s-consent">
    I agree that %(brand)s may call and text me at the number above about life
    insurance, including with an automatic telephone dialing system or a prerecorded
    voice. I understand this consent is not a condition of purchase and that message
    and data rates may apply.
  </label>
  <p class="field-error">%(err)s<span></span></p>
</div>
""" % {"id": field_id, "brand": brand, "err": ERR}, indent)


# ---------------------------------------------------------------------------
# FIELDS
# Every builder on the site uses these. Two rules shape the markup:
#
#   * The hint and the error share ONE reserved slot under the control
#     (.field-foot). The slot is always in the layout, so the submit button can
#     never move between mousedown and mouseup when a blur validation fires,
#     and a hinted field does not pay for a second line above the input.
#   * row() pairs two fields when the form is wide enough. Pairing, not smaller controls, is how
#     the forms got shorter: targets stay 48px (56px in .fe).
# ---------------------------------------------------------------------------
TRUST = "Goes to one licensed agent. Never sold to anyone else."


def _foot(hint=""):
    tip = ('<p class="field-hint">%s</p>' % hint) if hint else ""
    return '<div class="field-foot">%s<p class="field-error">%s<span></span></p></div>' % (tip, ERR)


# Placeholders show the expected FORMAT, never a stand-in answer, and the
# label always stays above: a placeholder is gone the moment anyone types.
PLACEHOLDER = {"tel": "(555) 555-5555", "email": "name@example.com"}


def text_field(field_id, name, label, hint="", type="text", autocomplete="",
               validate="", error="", required=True, inputmode="", maxlength="",
               placeholder=None, indent=12):
    attrs = ['class="input"', 'id="%s"' % field_id, 'name="%s"' % name, 'type="%s"' % type]
    if placeholder is None:
        placeholder = "First and last name" if validate == "name" else PLACEHOLDER.get(type, "")
    if placeholder:
        attrs.append('placeholder="%s"' % placeholder)
    if inputmode:
        attrs.append('inputmode="%s"' % inputmode)
    attrs.append('autocomplete="%s"' % (autocomplete or "off"))
    if maxlength:
        attrs.append('maxlength="%s"' % maxlength)
    if required:
        attrs.append("required")
    if validate:
        attrs.append('data-validate="%s"' % validate)
    if error:
        attrs.append('data-error="%s"' % error)
    return block("""
<div class="field">
  <label class="field-label" for="%(id)s">%(label)s</label>
  <input %(attrs)s>
  %(foot)s
</div>
""" % {"id": field_id, "label": label, "attrs": " ".join(attrs), "foot": _foot(hint)}, indent)


def age_field(field_id, senior=False, label="Your age", hint="", indent=12):
    """The one age question, so the range and its message cannot drift apart."""
    rule, low = ("ageSenior", 50) if senior else ("age", 18)
    return text_field(field_id, "age", label, hint=hint, inputmode="numeric", validate=rule,
                      error="Enter an age between %d and 85." % low, maxlength="2",
                      placeholder="e.g. %d" % (67 if senior else 42), indent=indent)


def phone_field(field_id, label="Best number to reach you", hint="", indent=12):
    """site.js formats this as it is typed: (555) 018-0199 is 14 characters."""
    return text_field(field_id, "phone", label, hint=hint, type="tel", autocomplete="tel",
                      inputmode="tel", validate="phone", error="Enter a 10 digit phone number.",
                      maxlength="14", indent=indent)


def select_field(field_id, name, label, options, error="", required=True, hint="", indent=12):
    """`options` is either an HTML string (chrome.state_options()) or
    [(value, label)]. The first entry is always the empty prompt."""
    if not isinstance(options, str):
        options = "".join('    <option value="%s">%s</option>\n' % o for o in options).rstrip("\n")
    req = " required" if required else ""
    err_attr = (' data-error="%s"' % error) if error else ""
    return block("""
<div class="field">
  <label class="field-label" for="%(id)s">%(label)s</label>
  <select class="select" id="%(id)s" name="%(name)s"%(req)s%(err)s>
%(opts)s
  </select>
  %(foot)s
</div>
""" % {"id": field_id, "name": name, "label": label, "req": req,
       "err": err_attr, "opts": options, "foot": _foot(hint)}, indent)


def textarea_field(field_id, name, label, hint="", rows=3, required=False,
                   placeholder="Type your question here", indent=12):
    ph = (' placeholder="%s"' % placeholder) if placeholder else ""
    return block("""
<div class="field">
  <label class="field-label" for="%(id)s">%(label)s</label>
  <textarea class="input" id="%(id)s" name="%(name)s" rows="%(rows)d"%(req)s%(ph)s></textarea>
  %(foot)s
</div>
""" % {"id": field_id, "name": name, "label": label, "rows": rows,
       "req": " required" if required else "", "ph": ph, "foot": _foot(hint)}, indent)


def file_field(field_id, name, label, hint="", accept=".pdf,.jpg,.jpeg,.png,.heic", indent=12):
    """An optional document upload. Always optional: a form that cannot be sent
    without a scan loses everyone who is on a phone away from their papers.
    site.js keeps the File out of the JSON payload (it records has_attachment
    instead), so the CRM wiring has to post multipart to carry the file."""
    return block("""
<div class="field">
  <label class="field-label" for="%(id)s">%(label)s</label>
  <input class="input input-file" id="%(id)s" name="%(name)s" type="file" accept="%(accept)s">
  %(foot)s
</div>
""" % {"id": field_id, "name": name, "label": label, "accept": accept, "foot": _foot(hint)}, indent)


def radio_group(group_id, name, legend, options, hint="", error="", indent=12):
    """A .choice-row radio set. site.js validates these as a group, reading the
    error message off the wrapper's data-error, so the wrapper carries it."""
    opts = "".join(
        '    <label class="choice"><input type="radio" name="%s" value="%s" required>'
        '<span>%s</span></label>\n' % (name, v, t) for v, t in options).rstrip("\n")
    return block("""
<div class="field" data-error="%(error)s">
  <span class="field-label" id="%(id)s-label">%(legend)s</span>
  <div class="choice-row" role="group" aria-labelledby="%(id)s-label">
%(opts)s
  </div>
  %(foot)s
</div>
""" % {"id": group_id, "legend": legend, "opts": opts,
       "error": error or "Choose an option.", "foot": _foot(hint)}, indent)


def row(*fields, tight=False):
    """Two fields side by side once the form itself is wide enough (a container
    query, not a viewport one).

    tight=True pairs them from 16rem instead of 26rem, which is the only width
    a phone actually gives a form in a panel (277px at 390). Use it ONLY for
    two short controls: a text or tel input whose value is a few characters.
    Never for a state select (its prompt clips) and never for a radio group
    (.choice has a 6rem min-width, so the pair wraps and the block gets
    taller). .fe is unaffected: its own rule keeps senior forms single column
    below 27.99rem.
    """
    cls = "field-row field-row-tight" if tight else "field-row"
    return '<div class="%s">\n%s\n</div>' % (cls, "\n".join(fields))


def progress(total):
    """Segmented bar plus its live label. Segments are authored for the longest
    path; site.js hides the spare ones once a branch is chosen."""
    segs = "".join('<span class="progress-seg%s" data-progress-seg></span>' % (" is-done" if i == 0 else "")
                   for i in range(total))
    return ('<div class="progress-track" aria-hidden="true">%s</div>\n'
            '<p class="text-micro font-semibold text-muted" data-progress-label aria-live="polite">Step 1</p>'
            % segs)


def step(n, title, body, first=False, owner=""):
    """One step of a [data-steps] form. `title` is read out with the legend and
    shown in the progress label ("Step 1 of 2 · About you"). `owner` is the
    branch value for a [data-step-for] step."""
    own = (' data-step-for="%s" disabled' % owner) if owner else ""
    return ('<fieldset class="step%s mt-5" data-step="%s" data-step-title="%s"%s>\n'
            '<legend class="sr-only">%s</legend>\n%s\n</fieldset>'
            % (" is-active" if first else "", n, title, own, title, body))


def next_button(back=False, label="Continue"):
    if not back:
        return '<button type="button" class="btn btn-cta btn-block" data-step-next>%s</button>' % label
    return ('<div class="flex gap-3"><button type="button" class="btn btn-ghost" data-step-back>Back</button>'
            '<button type="button" class="btn btn-cta grow" data-step-next>%s</button></div>' % label)


def submit_block(label, back=False, note=TRUST):
    """The submit button, the failure line under it, and one trust line. The
    failure line is role="alert": it appears only when submitLead() rejects,
    and site.js turns the button into "Try again" beside it."""
    button = '<button type="submit" class="btn btn-cta %s">%s</button>' % ("grow" if back else "btn-block", label)
    if back:
        button = ('<div class="flex gap-3"><button type="button" class="btn btn-ghost" data-step-back>Back</button>%s</div>'
                  % button)
    return ('%s\n<p class="field-error" data-form-error role="alert">%s<span></span></p>\n'
            '<p class="form-trust">%s%s</p>' % (button, ERR, icon("shield-check", 16, "shrink-0"), note))


def success_panel(panel_id, heading, body_html, cta_html, icon_size=30, indent=8):
    """The designed in-place success state. Never a browser dialog.

    site.js hides the form, reveals this, moves focus to it, and marks it
    role="status" so assistive tech hears it without the page jumping.
    """
    return block("""
<div id="%(id)s" class="success">
  <div class="flex items-start gap-3">
    %(icon)s
    <div>
      <h3 class="text-h3 !font-display !font-semibold">%(heading)s</h3>
%(body)s
      <div class="mt-5">
        %(cta)s
      </div>
    </div>
  </div>
</div>
""" % {"id": panel_id, "heading": heading,
       "icon": icon("circle-check", icon_size, "shrink-0 text-green"),
       "body": textwrap.indent(textwrap.dedent(body_html).strip("\n"), "      "),
       "cta": cta_html}, indent)
