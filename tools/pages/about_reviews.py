# -*- coding: utf-8 -*-
"""REVIEWS. Spec P1, shipped in the P0 layer.

The page is built empty and stays empty until real reviews exist. Nothing here
is a sample, a placeholder quote, or an illustrative testimonial, because a
fabricated review is the one thing on an insurance site that is both the
easiest to write and the most expensive to be caught at.

The layout follows the shipped home page slot (home.py, [data-reviews-slot]):
designed, wired, and `hidden` until populated. No AggregateRating is emitted
while the count is zero. An aggregate rating over no reviews is the same
fabrication as an invented quote, expressed in structured data, and it is the
form Google penalises hardest.
"""
from icons import icon
import chrome as C

PATH = "/about/reviews/"
OUT = "about/reviews/index.html"
ACTIVE = PATH
SILO = "site"
TITLE = "Client Reviews | Apex Insurance Marketing"
OG_TITLE = "Client reviews of Apex Insurance Marketing"
DESC = ("Where to find reviews of Apex Insurance Marketing, how we collect them, and why you "
        "will not find an unattributed testimonial anywhere on this site.")

FAQ = [
    ("Why are there no testimonials on this page?",
     "Because we do not have reviews we can attribute yet, and an unattributable testimonial is "
     "indistinguishable from one we wrote ourselves. When there are real ones, they will appear "
     "here with the reviewer's name and the platform they were left on, so you can go and check."),
    ("Will you offer me something in exchange for a review?",
     "No. Paying for or incentivising a review breaches the terms of every major review platform "
     "and, for an insurance agency, risks being treated as an inducement. We will ask, once, "
     "after your policy is issued, and we will take no for an answer."),
    ("Can I leave a review if my application was declined?",
     "Yes, and we would rather you did. A page of only successful outcomes tells a prospective "
     "client nothing about what happens when the answer is difficult."),
]


def schema():
    # Organization + BreadcrumbList only. No AggregateRating, no Review nodes,
    # until there are real reviews to describe. See the module docstring.
    return [C.org_schema(),
            C.breadcrumbs([("Home", "/"), ("About", "/about/"), ("Reviews", None)]),
            C.faq_schema(FAQ)]


def body():
    return f"""
<section class="pt-6 pb-14 md:pb-16 glow">
  <div class="container-ax">
    {C.crumbs([("Home", "/"), ("About", "/about/"), ("Reviews", None)])}

    <div class="mt-8 max-w-3xl">
      <h1 class="reveal text-h1">Client reviews</h1>
      <p class="reveal mt-5 text-lead text-slate">
        This page is empty on purpose. We have not published a testimonial we cannot attribute to
        a named person on a platform you can go and read for yourself, and we are not going to
        start with the first one.
      </p>
    </div>

    <div class="reveal mt-8 max-w-3xl">
      {C.flag("[REAL ATTRIBUTABLE REVIEWS ONLY - DO NOT FABRICATE] The slots below are designed "
              "and wired but empty. Populate from the agency's Google Business Profile, and add "
              "the AggregateRating schema in schema() only once there is a real rating and a real "
              "count to describe. Never write a sample review into this file, not even a marked "
              "one.", "EMPTY BY DESIGN")}
    </div>

    <!-- AGGREGATE SLOT. Hidden until there is a rating to show. Kept in the
         markup so the integration is a data change, not a design change. -->
    <div class="reveal mt-10 bento" data-stagger="40" data-reviews-aggregate hidden>
      <div class="bento-cell bento-cell-tint bento-2">
        <p class="eyebrow">Average rating</p>
        <span class="stat-value mt-3 block" data-reviews-rating></span>
        <span class="stat-label" data-reviews-source></span>
      </div>
      <div class="bento-cell bento-2">
        <p class="eyebrow">Reviews</p>
        <span class="stat-value mt-3 block" data-reviews-count></span>
        <span class="stat-label">verified, attributable reviews</span>
      </div>
      <div class="bento-cell bento-2">
        <p class="eyebrow">Where</p>
        <p class="mt-3 text-slate" data-reviews-platform></p>
      </div>
    </div>

    <!-- REVIEW LIST. Same construction as the home page slot. -->
    <div class="reveal mt-10 card" data-reviews-slot hidden>
      <h2 class="text-h3 !font-display !font-semibold">What clients say</h2>
      <div class="mt-6 grid gap-4" data-reviews-list></div>
    </div>

    <!-- THE EMPTY STATE, which is what actually renders today. It is a real
         designed state rather than a blank region, because "we have none yet"
         is itself the honest answer to the question this page is asked. -->
    <div class="reveal mt-10 card text-center" data-reviews-empty>
      <div class="mx-auto inline-flex items-center justify-center w-14 h-14 rounded-full bg-navy-050 text-navy">
        {icon("users", 26)}
      </div>
      <h2 class="mt-5 text-h3 !font-display !font-semibold">No published reviews yet</h2>
      <p class="mt-4 text-slate max-w-xl mx-auto">
        When clients leave reviews on our Google Business Profile, they will appear here with the
        reviewer's name and a link to the original, so you can confirm we did not write them.
        Until then, judge us on whether the rest of this site names its sources.
      </p>
      <div class="mt-7 flex flex-wrap justify-center gap-3">
        <a href="/about/agents/" class="btn btn-ghost">See who you would be working with</a>
        {C.phone_link("reviews_empty", "btn btn-call", "Call " + C.PHONE_DISPLAY)}
      </div>
    </div>
  </div>
</section>


<section class="section band">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-start">
      <div class="lg:col-span-5">
        <h2 class="reveal text-h2">How we handle reviews</h2>
        <p class="reveal mt-5 text-slate">
          The rules we hold ourselves to, written down so you can hold us to them.
        </p>
      </div>
      <div class="lg:col-span-6 lg:col-start-7">
        <ul class="grid gap-5">
          {"".join('''<li class="reveal flex items-start gap-3">%s
            <div><p class="font-semibold text-navy">%s</p>
            <p class="mt-1 text-slate">%s</p></div>
          </li>''' % (icon("circle-check", 22, "shrink-0 text-navy mt-1"), h, b) for h, b in [
            ("Attributed or not published",
             "A review appears here with a real first name and the platform it was left on, or it does not appear."),
            ("Collected on a platform we do not control",
             "Reviews are left on the client's own account on a third party platform. We cannot edit, delete, or reorder them there."),
            ("Never bought, never incentivised",
             "No discount, no gift card, no entry into anything. We ask once after a policy is issued."),
            ("The bad ones stay up",
             "We respond to them. We do not ask a platform to remove a review because it is unflattering."),
            ("No aggregate rating without real reviews",
             "The star rating in our search result comes from a real count, or it is absent. It will not be a number we chose."),
          ])}
        </ul>
      </div>
    </div>
  </div>
</section>


{C.faq_section("Questions about reviews", FAQ, "reviews-faq")}


<section class="section band-navy on-navy">
  <div class="container-ax">
    <div class="grid lg:grid-cols-12 gap-8 items-center">
      <div class="lg:col-span-7">
        <h2 class="reveal text-h2 text-white">Judge us on the numbers instead</h2>
        <p class="reveal mt-4 text-white/85 max-w-2xl">
          Ask for a quote and see whether the carrier names and premiums come back on it. That
          tells you more than a testimonial would.
        </p>
      </div>
      <div class="lg:col-span-4 lg:col-start-9 grid gap-3">
        <a href="/get-a-quote/" class="btn btn-cta btn-block">Get a free quote</a>
        {C.phone_link("reviews_footer", "btn btn-ghost btn-block", "Call " + C.PHONE_DISPLAY)}
      </div>
    </div>
  </div>
</section>"""
