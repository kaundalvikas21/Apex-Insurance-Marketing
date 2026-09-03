# -*- coding: utf-8 -*-
"""Shared body for the /compare/ pages. Template T5.

Compare pages are NEUTRAL (spec s07 rule 3). No silo owns them, so nothing here
leans: the two-path CTA gives both products the same button, the same weight,
and the same amount of room. That neutrality is the whole reason the linking
rules allow a compare page to be the one cross-silo route.

T5's order is fixed by the spec and is not a suggestion:

    breadcrumb -> H1 -> the answer in three sentences -> side-by-side table ->
    worked cost over time -> where A wins / where B wins -> decision checklist
    -> two-path CTA -> FAQ -> byline

The three-sentence answer goes in the hero lead, which is also where the
mandated up-link lives. A reader who bounces after the first paragraph should
still leave with the answer.

# ponytail: one builder for every compare page. compare_term_vs_whole is
# registered in PAGES and unwritten; when it lands it uses this, not a copy.
"""
import chrome as C


def _cells(items):
    """[(eyebrow, title, body_html)] -> bento cells with the mandated variation.
    Two cells (.bento-3) or three (.bento-2), never more: a compare page's
    signature object is the table, and a second dense grid competes with it."""
    span = "bento-3" if len(items) == 2 else "bento-2"
    variants = ["bento-cell-blue", "bento-cell-tint", ""][:len(items)]
    out = ""
    for (eyebrow, title, body), variant in zip(items, variants):
        navy = variant == "bento-cell-blue"
        out += f"""
      <div class="reveal bento-cell {variant} {span}">
        <p class="eyebrow{' text-white/80' if navy else ''}">{eyebrow}</p>
        <h3 class="mt-2 text-h4{' text-white' if navy else ''}">{title}</h3>
        <div class="mt-3 {'text-white/90' if navy else 'text-slate'}">{body}</div>
      </div>"""
    return out


def table(caption, cols, rows, min_width="46rem"):
    """The side-by-side table. `rows` is [(row_header, [cell, ...])]; a row whose
    cell list is empty renders as a full-width group row, which is how the
    simplified variant keeps its section breaks inside the table."""
    heads = "".join('<th scope="col">%s</th>' % c for c in cols)
    body = []
    for head, cells in rows:
        if not cells:
            body.append('<tr><th scope="row" colspan="%d">%s</th></tr>' % (len(cols) + 1, head))
        else:
            body.append('<tr><th scope="row">%s</th>%s</tr>'
                        % (head, "".join("<td>%s</td>" % c for c in cells)))
    return f"""
      <!-- .reveal sits on the scroll container itself, never on a wrapper:
           a transformed wrapper leaks the table's width into the page. -->
      <div class="reveal mt-10 table-scroll table-signature">
        <table class="compare-table" style="min-width:{min_width}">
          <caption class="sr-only">{caption}</caption>
          <thead>
            <tr>
              <th scope="col"><span class="sr-only">What is being compared</span></th>
              {heads}
            </tr>
          </thead>
          <tbody>
            {"".join(body)}
          </tbody>
        </table>
      </div>"""


def checklist(items):
    """The decision checklist. A list of statements the reader can answer about
    their own situation, not a scoring quiz: a quiz would have to invent a
    threshold, and there isn't an honest one."""
    rows = "".join(f"""
        <li class="reveal flex items-start gap-3">
          {C.icon("check", 20, "shrink-0 mt-1 text-green")}
          <span class="text-slate">{t}</span>
        </li>""" for t in items)
    return '<ul class="grid gap-4" data-stagger="40">%s</ul>' % rows


def two_path(heading, intro, paths, note=None):
    """T5's close: one route per product, each into that product's own silo.

    `paths` is exactly two (title, body, href, label). No eyebrow: the card
    already carries an h3 and a labelled button, and a third label for the same
    thing put these pages over the house eyebrow ceiling of three.

    Both buttons are .btn-cta. On a neutral page, giving one of them the amber
    and the other a ghost outline is a recommendation dressed as a layout
    decision, and the reader can tell.
    """
    cards = ""
    for title, body, href, label in paths:
        cards += f"""
      <div class="reveal card flex flex-col">
        <h3 class="text-h4">{title}</h3>
        <p class="mt-3 text-slate">{body}</p>
        <div class="mt-6 lg:mt-auto lg:pt-6">
          <a class="btn btn-cta btn-block" href="{href}">{label}</a>
        </div>
      </div>"""
    return f"""<section class="section band">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">{heading}</h2>
      <p class="reveal mt-5 text-slate">{intro}</p>
    </div>
    <div class="mt-10 grid md:grid-cols-2 gap-4">{cards}
    </div>
    <p class="reveal mt-6 text-sm text-muted">
      Or speak to a licensed agent about both:
      {C.phone_link("compare_two_path", "link-static inline-flex items-center gap-2",
                    C.PHONE_DISPLAY, 18)}. {note or C.HOURS}
    </p>
  </div>
</section>"""


def render(trail, h1, lead, table_heading, table_intro, table_caption, table_cols, table_rows,
           cost_heading, cost_intro, cost_blocks, wins_heading, wins_intro, wins,
           checklist_heading, checklist_intro, checklist_items, paths_heading, paths_intro,
           paths, faq_heading, faq, faq_group, table_min_width="46rem", table_note=None,
           checklist_aside=None, prologue=""):
    """One compare page. Every argument is copy; the order of the sections is
    T5's and is not parameterised."""
    note = ('<p class="reveal mt-4 text-micro text-muted max-w-3xl">%s</p>' % table_note
            ) if table_note else ""
    return f"""{prologue}
{C.page_hero(trail, h1, lead)}


<!-- =====================================================================
     THE SIDE BY SIDE TABLE. The page's signature object, and the reason
     a compare page exists at all: the reader wants the two things in one
     field of view, not two pages of prose about each.
     ================================================================== -->
<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">{table_heading}</h2>
      <p class="reveal mt-5 text-slate">{table_intro}</p>
    </div>
    {table(table_caption, table_cols, table_rows, table_min_width)}
    {note}
  </div>
</section>


{C.prose(cost_heading, cost_blocks, intro=cost_intro, cls="section band")}


<section class="section">
  <div class="container-ax">
    <div class="max-w-2xl">
      <h2 class="reveal text-h2">{wins_heading}</h2>
      <p class="reveal mt-5 text-slate">{wins_intro}</p>
    </div>
    <div class="mt-10 bento" data-stagger="40">{_cells(wins)}
    </div>
  </div>
</section>


{C.prose(checklist_heading, checklist(checklist_items), intro=checklist_intro,
         cls="section band", aside=checklist_aside)}


{two_path(paths_heading, paths_intro, paths)}


{C.faq_section(faq_heading, faq, faq_group)}


{C.byline_section()}
"""
