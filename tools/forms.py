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
# The built pages hand-wrap their own field markup, which is why these are not
# retrofitted there: the labels, hints, autocomplete tokens, and validators are
# per-question content rather than duplication. New pages use these.
# ---------------------------------------------------------------------------
def text_field(field_id, name, label, hint="", type="text", autocomplete="",
               validate="", error="", required=True, inputmode="", indent=12):
    attrs = ['class="input"', 'id="%s"' % field_id, 'name="%s"' % name, 'type="%s"' % type]
    if inputmode:
        attrs.append('inputmode="%s"' % inputmode)
    attrs.append('autocomplete="%s"' % (autocomplete or "off"))
    if required:
        attrs.append("required")
    if validate:
        attrs.append('data-validate="%s"' % validate)
    if error:
        attrs.append('data-error="%s"' % error)
    hint_html = ('\n    <span class="field-hint block font-normal">%s</span>' % hint) if hint else ""
    return block("""
<div class="field">
  <label class="field-label" for="%(id)s">%(label)s%(hint)s
  </label>
  <input %(attrs)s>
  <p class="field-error">%(err)s<span></span></p>
</div>
""" % {"id": field_id, "label": label, "hint": hint_html,
       "attrs": " ".join(attrs), "err": ERR}, indent) if hint else block("""
<div class="field">
  <label class="field-label" for="%(id)s">%(label)s</label>
  <input %(attrs)s>
  <p class="field-error">%(err)s<span></span></p>
</div>
""" % {"id": field_id, "label": label, "attrs": " ".join(attrs), "err": ERR}, indent)


def select_field(field_id, name, label, options, error="", required=True, indent=12):
    """`options` is either an HTML string (chrome.state_options()) or
    [(value, label)]. The first entry is always the empty prompt."""
    if not isinstance(options, str):
        options = "".join('    <option value="%s">%s</option>\n' % o for o in options).rstrip("\n")
    req = " required" if required else ""
    err_attr = ('\n          data-error="%s"' % error) if error else ""
    return block("""
<div class="field">
  <label class="field-label" for="%(id)s">%(label)s</label>
  <select class="select" id="%(id)s" name="%(name)s"%(req)s%(err)s>
%(opts)s
  </select>
  <p class="field-error">%(errico)s<span></span></p>
</div>
""" % {"id": field_id, "name": name, "label": label, "req": req,
       "err": err_attr, "opts": options, "errico": ERR}, indent)


def radio_group(group_id, name, legend, options, hint="", error="", indent=12):
    """A .choice-row radio set. site.js validates these as a group, reading the
    error message off the wrapper's data-error, so the wrapper carries it."""
    opts = "".join(
        '    <label class="choice"><input type="radio" name="%s" value="%s" required>'
        '<span>%s</span></label>\n' % (name, v, t) for v, t in options).rstrip("\n")
    hint_html = ('\n    <span class="field-hint block font-normal">%s</span>' % hint) if hint else ""
    return block("""
<div class="field" data-error="%(error)s">
  <span class="field-label" id="%(id)s-label">%(legend)s%(hint)s
  </span>
  <div class="choice-row" role="group" aria-labelledby="%(id)s-label">
%(opts)s
  </div>
  <p class="field-error">%(err)s<span></span></p>
</div>
""" % {"id": group_id, "legend": legend, "hint": hint_html, "opts": opts,
       "error": error or "Choose an option.", "err": ERR}, indent)


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
