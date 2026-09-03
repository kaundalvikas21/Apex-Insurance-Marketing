/* ==========================================================================
   Apex Insurance Marketing — site behavior
   Vanilla, no dependencies, one file. Progressive enhancement throughout:
   every page is readable and every link works with this file blocked.

   Contents
     1. Analytics (GA4 dataLayer)
     2. Sticky header shrink
     3. Mobile navigation
     4. Scroll reveal
     5. Form validation, TCPA gate, success state
     6. Multi-step forms
     7. Rate-table prefill
     8. Triage widget
   ========================================================================== */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }

  /* ------------------------------------------------------------------------
     1. ANALYTICS
     Guarded so the site works with no GA4 property installed. Swap the
     dataLayer push for gtag() if you move off GTM.
     --------------------------------------------------------------------- */
  window.dataLayer = window.dataLayer || [];

  function track(eventName, params) {
    var payload = { event: eventName };
    for (var k in params) { if (Object.prototype.hasOwnProperty.call(params, k)) payload[k] = params[k]; }
    window.dataLayer.push(payload);
    if (window.AX_DEBUG) console.log('[ga4]', eventName, payload);
  }

  // Exposed so the (future) calculator spokes can fire calculator_complete.
  window.axTrack = track;

  // call_click: delegated, catches every tel: link on the page including
  // ones injected later.
  document.addEventListener('click', function (e) {
    var link = e.target.closest && e.target.closest('a[href^="tel:"]');
    if (!link) return;
    track('call_click', {
      phone_number: link.getAttribute('href').replace('tel:', ''),
      link_location: link.getAttribute('data-cta-location') || 'unspecified',
      silo: document.body.getAttribute('data-silo') || 'site',
      page_path: window.location.pathname
    });
  });

  /* ------------------------------------------------------------------------
     2. STICKY HEADER SHRINK
     IntersectionObserver on a 1px sentinel. No scroll listener anywhere.
     --------------------------------------------------------------------- */
  (function stickyHeader() {
    var header = $('[data-header]');
    var sentinel = $('[data-header-sentinel]');
    if (!header || !sentinel || !('IntersectionObserver' in window)) return;

    new IntersectionObserver(function (entries) {
      header.classList.toggle('is-stuck', !entries[0].isIntersecting);
    }, { threshold: 0 }).observe(sentinel);
  })();

  /* ------------------------------------------------------------------------
     3. MOBILE NAVIGATION
     --------------------------------------------------------------------- */
  (function mobileNav() {
    var toggle = $('[data-nav-toggle]');
    var panel = $('[data-nav-panel]');
    if (!toggle || !panel) return;

    function setOpen(open) {
      toggle.setAttribute('aria-expanded', String(open));
      panel.hidden = !open;
    }

    toggle.addEventListener('click', function () {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        toggle.focus();
      }
    });

    // Close when a nav link is followed, so the panel is not left open on
    // same-page anchors.
    panel.addEventListener('click', function (e) {
      if (e.target.closest('a')) setOpen(false);
    });
  })();

  /* ------------------------------------------------------------------------
     4. SCROLL REVEAL
     Reduced motion and missing IO both fall through to "everything visible".
     --------------------------------------------------------------------- */
  (function reveal() {
    var items = $$('.reveal');
    if (!items.length) return;

    if (reduceMotion || !('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('is-in'); });
      return;
    }

    // Stagger children of a [data-stagger] container, capped at 6 so a long
    // list never waits half a second for its last item.
    // data-stagger="40" sets the step in ms; bento grids use 40, lists 60.
    $$('[data-stagger]').forEach(function (group) {
      var step = parseInt(group.getAttribute('data-stagger'), 10) || 60;
      $$('.reveal', group).forEach(function (el, i) {
        el.style.setProperty('--reveal-delay', Math.min(i, 5) * step + 'ms');
      });
    });

    // Count-up. The final figure is already in the HTML, so with JS off, in
    // print, under reduced motion, and on the final-expense page (html.fe)
    // the number simply sits there. Only spec figures carry data-count.
    var senior = document.documentElement.classList.contains('fe');
    function countUp(el) {
      var end = parseFloat(el.getAttribute('data-count'));
      if (senior || isNaN(end)) return;
      var pre = el.getAttribute('data-count-prefix') || '';
      var suf = el.getAttribute('data-count-suffix') || '';
      var t0 = null;
      function frame(t) {
        if (t0 === null) t0 = t;
        var p = Math.min((t - t0) / 900, 1);
        p = 1 - Math.pow(1 - p, 3);
        el.textContent = pre + Math.round(end * p).toLocaleString('en-US') + suf;
        if (p < 1) requestAnimationFrame(frame);
      }
      requestAnimationFrame(frame);
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in');
        if (entry.target.hasAttribute('data-count')) countUp(entry.target);
        $$('[data-count]', entry.target).forEach(countUp);
        io.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });

    items.forEach(function (el) { io.observe(el); });
  })();

  /* ------------------------------------------------------------------------
     4b. TABLE ROW CASCADE
     Rate and comparison tables build a row at a time. The class is added here
     rather than in the HTML so the tables are fully opaque with JS off, which
     matters more on a page of premiums than the animation does.
     --------------------------------------------------------------------- */
  (function rowCascade() {
    var tables = $$('.rate-table tbody, .compare-table tbody');
    if (!tables.length) return;

    var senior = document.documentElement.classList.contains('fe');
    if (senior || reduceMotion || !('IntersectionObserver' in window)) return;

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        $$('tr', entry.target).forEach(function (row, i) {
          row.style.setProperty('--row-delay', Math.min(i, 9) * 34 + 'ms');
          row.classList.add('is-in');
        });
        io.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.08 });

    tables.forEach(function (body) {
      if (body.hidden) return;
      $$('tr', body).forEach(function (row) { row.classList.add('reveal-row'); });
      io.observe(body);
    });
  })();

  /* ------------------------------------------------------------------------
     5. FORMS
     Every form: hidden source_url + silo + form_name, inline validation on
     blur, TCPA gate, GA4 form_start / form_submit, designed success state.

     >>> WIRE TO CRM ENDPOINT HERE <<<
     submitLead() is the single integration point. Replace the body with a
     fetch() to your CRM or lead-post URL and keep the returned promise.
     --------------------------------------------------------------------- */

  var VALIDATORS = {
    email: {
      test: function (v) { return /^[^\s@]+@[^\s@]+\.[a-z]{2,}$/i.test(v); },
      message: 'Enter a valid email address.'
    },
    phone: {
      test: function (v) { return v.replace(/\D/g, '').length === 10; },
      message: 'Enter a 10 digit US phone number.'
    },
    age: {
      test: function (v) { return /^\d{1,3}$/.test(v) && +v >= 18 && +v <= 85; },
      message: 'Enter an age between 18 and 85.'
    },
    ageSenior: {
      test: function (v) { return /^\d{1,3}$/.test(v) && +v >= 50 && +v <= 85; },
      message: 'Enter an age between 50 and 85.'
    },
    name: {
      test: function (v) { return v.trim().length >= 2; },
      message: 'Enter your name.'
    }
  };

  function fieldWrapper(input) {
    return input.closest('.field') || input.closest('.choice-row') || input.parentNode;
  }

  function errorNode(input) {
    var wrap = input.closest('.field') || input.closest('fieldset') || input.parentNode;
    return $('.field-error', wrap);
  }

  function setMessage(node, message) {
    // The error node holds an icon plus a <span>. Write into the span so the
    // icon is not wiped out by textContent.
    var slot = node.querySelector('span') || node;
    slot.textContent = message;
  }

  function showError(input, message) {
    var node = errorNode(input);
    input.setAttribute('aria-invalid', 'true');
    if (!node) return;
    setMessage(node, message);
    node.classList.add('is-shown');
    if (node.id) input.setAttribute('aria-describedby', node.id);
  }

  function clearError(input) {
    var node = errorNode(input);
    input.removeAttribute('aria-invalid');
    if (!node) return;
    node.classList.remove('is-shown');
    setMessage(node, '');
  }

  function validateField(input) {
    var value = (input.value || '').trim();
    var rule = input.getAttribute('data-validate');

    if (input.hasAttribute('required') && !value) {
      showError(input, input.getAttribute('data-error') || 'This field is required.');
      return false;
    }
    if (value && rule && VALIDATORS[rule] && !VALIDATORS[rule].test(value)) {
      showError(input, input.getAttribute('data-error') || VALIDATORS[rule].message);
      return false;
    }
    clearError(input);
    return true;
  }

  // Radio groups validate as a set, not per input.
  function validateRadioGroup(form, name) {
    var group = $$('input[type="radio"][name="' + name + '"]', form);
    if (!group.length || !group[0].hasAttribute('required')) return true;
    var chosen = group.some(function (r) { return r.checked; });
    var wrap = group[0].closest('fieldset') || group[0].closest('.field');
    var node = wrap && $('.field-error', wrap);
    if (node) {
      node.classList.toggle('is-shown', !chosen);
      if (!chosen) setMessage(node, wrap.getAttribute('data-error') || 'Choose an option.');
    }
    return chosen;
  }

  function collect(scope, form) {
    var inputs = $$('input, select, textarea', scope);
    var radioNames = {};
    var ok = true;

    inputs.forEach(function (input) {
      // :disabled, not .disabled. The IDL property reflects only the element's
      // own attribute, so a control inside <fieldset disabled> reports false
      // and would be validated even though the browser will never submit it.
      // The pseudo-class matches the computed state, which is what we mean.
      if (input.type === 'hidden' || input.matches(':disabled')) return;
      if (input.type === 'checkbox') return;          // consent handled separately
      if (input.type === 'radio') { radioNames[input.name] = true; return; }
      if (!validateField(input)) ok = false;
    });

    Object.keys(radioNames).forEach(function (name) {
      if (!validateRadioGroup(form, name)) ok = false;
    });

    return ok;
  }

  function firstInvalid(scope) {
    return $('[aria-invalid="true"]', scope) || $('.field-error.is-shown', scope);
  }

  /* >>> WIRE TO CRM ENDPOINT HERE <<< */
  function submitLead(payload) {
    // No backend in this build. The payload below is exactly what the CRM
    // needs to receive. Replace with:
    //   return fetch('/api/leads', {
    //     method: 'POST',
    //     headers: { 'Content-Type': 'application/json' },
    //     body: JSON.stringify(payload)
    //   }).then(function (r) { if (!r.ok) throw new Error(r.status); });
    console.log('[lead] would POST:', payload);
    return Promise.resolve();
  }

  function initForm(form) {
    var siloValue = form.getAttribute('data-silo') || 'site';
    var formName = form.getAttribute('data-form-name') || 'unnamed_form';
    var started = false;

    // Compliance: source URL and silo captured on every submission.
    var src = $('input[name="source_url"]', form);
    var silo = $('input[name="silo"]', form);
    var fname = $('input[name="form_name"]', form);
    if (src) src.value = window.location.href;
    if (silo) silo.value = siloValue;
    if (fname) fname.value = formName;

    // form_start fires once, on first real interaction.
    form.addEventListener('focusin', function (e) {
      if (started) return;
      if (!e.target.matches('input, select, textarea')) return;
      if (e.target.type === 'hidden') return;
      started = true;
      track('form_start', { form_name: formName, silo: siloValue, page_path: window.location.pathname });
    });

    // Validate on blur, then live-correct once the field has been flagged.
    $$('input, select, textarea', form).forEach(function (input) {
      if (input.type === 'hidden' || input.type === 'checkbox' || input.type === 'radio') return;
      input.addEventListener('blur', function (e) {
        // Stepping back is a retreat, not a mistake. Validating here would
        // flag fields the visitor has not finished with yet.
        var to = e.relatedTarget;
        if (to && to.closest && to.closest('[data-step-back]')) return;
        validateField(input);
      });
      input.addEventListener('input', function () {
        if (input.getAttribute('aria-invalid') === 'true') validateField(input);
      });
    });

    $$('input[type="radio"]', form).forEach(function (radio) {
      radio.addEventListener('change', function () { validateRadioGroup(form, radio.name); });
    });

    // Consent gate. Never pre-ticked, never bundled with another statement.
    var consent = $('[data-consent]', form);
    if (consent) {
      consent.checked = false; // defensive: browsers restore checkbox state on back-nav
      consent.addEventListener('change', function () {
        if (consent.checked) {
          var box = consent.closest('.consent');
          if (box) box.removeAttribute('data-invalid');
          var node = box && $('.field-error', box);
          if (node) { node.classList.remove('is-shown'); setMessage(node, ''); }
        }
      });
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      // Honeypot. Bots fill hidden text inputs; humans never see this one.
      var trap = $('input[name="company_website"]', form);
      if (trap && trap.value) return;

      var valid = collect(form, form);

      if (consent && !consent.checked) {
        valid = false;
        var box = consent.closest('.consent');
        if (box) {
          box.setAttribute('data-invalid', 'true');
          var node = $('.field-error', box);
          if (node) {
            setMessage(node, 'Please check the box so a licensed agent can contact you.');
            node.classList.add('is-shown');
          }
        }
      }

      if (!valid) {
        var bad = firstInvalid(form);
        if (bad) {
          var focusTarget = bad.matches('input, select, textarea') ? bad : $('input, select', bad.closest('.field, .consent, fieldset') || form);
          if (focusTarget && focusTarget.focus) focusTarget.focus();
          else bad.scrollIntoView({ block: 'center', behavior: reduceMotion ? 'auto' : 'smooth' });
        }
        return;
      }

      var payload = {};
      new FormData(form).forEach(function (value, key) {
        if (key === 'company_website') return;
        payload[key] = value;
      });
      payload.submitted_at = new Date().toISOString();

      var button = $('[type="submit"]', form);
      var originalLabel = button ? button.textContent : '';
      if (button) { button.disabled = true; button.textContent = 'Sending...'; }

      submitLead(payload).then(function () {
        track('form_submit', {
          form_name: formName,
          silo: siloValue,
          page_path: window.location.pathname,
          source_url: payload.source_url
        });
        showSuccess(form);
      }).catch(function () {
        if (button) { button.disabled = false; button.textContent = originalLabel; }
        var node = $('[data-form-error]', form);
        if (node) {
          setMessage(node, 'Something went wrong sending your request. Please call us and we will take your details over the phone.');
          node.classList.add('is-shown');
        }
      });
    });
  }

  function showSuccess(form) {
    var panel = document.getElementById(form.getAttribute('data-success-target'));
    if (!panel) { form.reset(); return; }

    form.hidden = true;
    panel.classList.add('is-shown');
    panel.setAttribute('tabindex', '-1');
    panel.focus();

    // Announce to assistive tech without stealing the visual scroll position.
    panel.setAttribute('role', 'status');
    panel.setAttribute('aria-live', 'polite');
  }

  $$('[data-ax-form]').forEach(initForm);

  /* ------------------------------------------------------------------------
     6. MULTI-STEP FORMS (term hub hero)
     Each step gates on its own fields. Focus follows the step so keyboard
     and screen-reader users are never left behind at the top of the form.
     --------------------------------------------------------------------- */
  $$('[data-steps]').forEach(function (form) {
    var allSteps = $$('[data-step]', form);
    var segments = $$('[data-progress-seg]', form);
    var label = $('[data-progress-label]', form);
    var branchInputs = $$('[data-step-branch]', form);
    if (allSteps.length < 2) return;

    var index = 0;

    // A branching form (the master quote page) holds the steps for all three
    // products at once and disables the branches that do not apply. A disabled
    // <fieldset> is the native tool for exactly this: collect() already skips
    // disabled inputs and FormData already drops them, so neither validation
    // nor the submitted payload has to know that branches exist.
    function steps() {
      return allSteps.filter(function (step) { return !step.disabled; });
    }

    function selectBranch(value) {
      allSteps.forEach(function (step) {
        var owner = step.getAttribute('data-step-for');
        if (owner) step.disabled = owner !== value;
      });
    }

    function branchChosen() {
      return !branchInputs.length || branchInputs.some(function (r) { return r.checked; });
    }

    function render(focusFirst) {
      var live = steps();
      if (index > live.length - 1) index = live.length - 1;

      allSteps.forEach(function (step) { step.classList.remove('is-active'); });
      live.forEach(function (step, i) { step.classList.toggle('is-active', i === index); });
      segments.forEach(function (seg, i) {
        // Segments are authored for the longest branch. Once a product is
        // picked, a shorter branch hides the spare ones rather than showing
        // progress against a total that does not apply. Before that the full
        // set stays visible, so the bar does not visibly grow on first choice.
        seg.hidden = branchChosen() && i >= live.length;
        seg.classList.toggle('is-done', i <= index);
      });
      // Before a product is picked the total is genuinely not known yet, so the
      // label does not invent one.
      if (label) {
        label.textContent = branchChosen()
          ? 'Step ' + (index + 1) + ' of ' + live.length
          : 'Step ' + (index + 1);
      }

      if (focusFirst) {
        // preventScroll: the visitor clicked Continue inside the form, so the
        // form is already in view. Letting focus() scroll yanks the page and
        // moves the Back button out from under the pointer.
        var target = $('input:not([type="hidden"]), select', live[index]);
        if (target) target.focus({ preventScroll: true });
      }
    }

    // Picking a product re-derives the step list underneath the current step.
    form.addEventListener('change', function (e) {
      if (!e.target.matches('[data-step-branch]')) return;
      selectBranch(e.target.value);
      render(false);
    });

    form.addEventListener('click', function (e) {
      var next = e.target.closest('[data-step-next]');
      var back = e.target.closest('[data-step-back]');

      if (next) {
        e.preventDefault();
        var live = steps();
        if (!collect(live[index], form)) {
          var bad = firstInvalid(live[index]);
          if (bad && bad.focus) bad.focus();
          return;
        }
        if (index < live.length - 1) { index++; render(true); }
      }

      if (back) {
        e.preventDefault();
        if (index > 0) { index--; render(true); }
      }
    });

    // Enter should advance a step, not submit from step 1.
    form.addEventListener('keydown', function (e) {
      if (e.key !== 'Enter') return;
      if (e.target.tagName === 'TEXTAREA') return;
      var live = steps();
      if (index === live.length - 1) return;
      e.preventDefault();
      var nextBtn = $('[data-step-next]', live[index]);
      if (nextBtn) nextBtn.click();
    });

    // Jump to the first step that still has an empty required field. Used
    // after a rate-table prefill.
    form.axGoToFirstGap = function () {
      var live = steps();
      for (var i = 0; i < live.length; i++) {
        var empty = $$('input[required], select[required]', live[i]).some(function (el) {
          if (el.type === 'radio') {
            return !$$('input[name="' + el.name + '"]', form).some(function (r) { return r.checked; });
          }
          return !el.value;
        });
        if (empty) { index = i; render(true); return; }
      }
      index = live.length - 1;
      render(true);
    };

    // Honour a branch the browser restored on back-navigation, and otherwise
    // start with every branch disabled so only the shared steps are live.
    if (branchInputs.length) {
      var preset = branchInputs.filter(function (r) { return r.checked; })[0];
      selectBranch(preset ? preset.value : null);
    }

    render(false);
  });

  /* ------------------------------------------------------------------------
     7. RATE-TABLE PREFILL
     A row button writes its own numbers into the quote form and moves the
     user to the first thing we still need from them.
     --------------------------------------------------------------------- */
  $$('[data-prefill]').forEach(function (button) {
    button.addEventListener('click', function () {
      var form = document.getElementById(button.getAttribute('data-prefill-target'));
      if (!form) return;

      var values;
      try { values = JSON.parse(button.getAttribute('data-prefill')); }
      catch (err) { return; }

      // Merge in whatever the rate table's own toggles are currently set to,
      // so "quote this row" carries the term length, sex, and tobacco status
      // the visitor was actually looking at.
      var panels = button.closest('[data-panels]');
      if (panels) {
        $$('input[type="radio"]:checked[data-prefill-name]', panels).forEach(function (radio) {
          values[radio.getAttribute('data-prefill-name')] = radio.value;
        });
      }

      Object.keys(values).forEach(function (name) {
        var field = form.elements[name];
        if (!field) return;
        if (field.length && field[0] && field[0].type === 'radio') {
          Array.prototype.forEach.call(field, function (radio) {
            radio.checked = (radio.value === String(values[name]));
          });
        } else {
          field.value = values[name];
        }
      });

      track('form_start', {
        form_name: form.getAttribute('data-form-name'),
        silo: form.getAttribute('data-silo'),
        trigger: 'rate_table_prefill'
      });

      // Some prefill buttons also change what the visitor is asking for
      // (a full illustration rather than a quote). Reveal the note that says so.
      var reveal = button.getAttribute('data-prefill-reveal');
      if (reveal) {
        $$('[data-prefill-note]', form.parentNode).forEach(function (n) { n.hidden = true; });
        var note = document.getElementById(reveal);
        if (note) note.hidden = false;
      }

      form.scrollIntoView({ block: 'start', behavior: reduceMotion ? 'auto' : 'smooth' });
      if (typeof form.axGoToFirstGap === 'function') form.axGoToFirstGap();
    });
  });

  /* ------------------------------------------------------------------------
     8. PANEL GROUPS
     One radio group shows one panel. Used by the final-expense rate table
     (male / female) and the term-length selector. Every panel is present in
     the HTML, so the content is complete for crawlers and with JS off; this
     only hides the ones that are not selected.
     --------------------------------------------------------------------- */
  $$('[data-panels]').forEach(function (group) {
    var panels = $$('[data-panel]', group);

    function apply() {
      var chosen = $$('input[type="radio"]:checked', group).map(function (r) { return r.value; });
      panels.forEach(function (panel) {
        panel.hidden = chosen.indexOf(panel.getAttribute('data-panel')) === -1;
      });

      // Caption reflects every dimension currently selected, so a printed or
      // screenshotted table is never ambiguous about what it is showing.
      var caption = $('[data-panel-caption]', group);
      if (!caption) return;
      var labels = $$('input[type="radio"]:checked', group).map(function (r) {
        var el = r.closest('label');
        return el ? el.textContent.trim().toLowerCase() : r.value;
      });
      caption.textContent = 'Showing ' + labels.join(', ') + '.';
    }

    group.addEventListener('change', function (e) {
      if (e.target.matches('input[type="radio"]')) apply();
    });
    apply();
  });

  /* ------------------------------------------------------------------------
     9. TRIAGE WIDGET (home)
     Three questions, no email wall, routes to a hub. Scores are declared in
     markup as data-score="term:3,whole:1" so the copy and the logic stay in
     the same place.
     --------------------------------------------------------------------- */
  (function triage() {
    var widget = $('[data-triage]');
    if (!widget) return;

    var questions = $$('[data-triage-q]', widget);
    var results = $$('[data-triage-result]', widget);
    var progress = $('[data-triage-progress]', widget);
    var scores = {};
    var at = 0;

    function show(step, moveFocus) {
      questions.forEach(function (q, i) { q.hidden = i !== step; });
      results.forEach(function (r) { r.hidden = true; });
      if (progress) {
        progress.hidden = false;
        progress.textContent = 'Question ' + (step + 1) + ' of ' + questions.length;
      }
      // Focus follows the question so keyboard and screen reader users hear the
      // new one. Not on first paint, which would ring the heading on page load.
      if (!moveFocus) return;
      var heading = $('[data-triage-heading]', questions[step]);
      if (heading) {
        heading.setAttribute('tabindex', '-1');
        heading.focus({ preventScroll: true });
      }
    }

    function finish() {
      var winner = 'term';
      var best = -1;
      Object.keys(scores).forEach(function (key) {
        if (scores[key] > best) { best = scores[key]; winner = key; }
      });

      questions.forEach(function (q) { q.hidden = true; });
      if (progress) progress.hidden = true;
      results.forEach(function (r) { r.hidden = r.getAttribute('data-triage-result') !== winner; });

      var shown = results.filter(function (r) { return !r.hidden; })[0];
      if (shown) { shown.setAttribute('tabindex', '-1'); shown.focus({ preventScroll: true }); }

      track('triage_complete', { recommended_silo: winner });
    }

    widget.addEventListener('click', function (e) {
      // Every result panel has its own restart button, so this is delegated
      // rather than bound to a single node.
      if (e.target.closest('[data-triage-restart]')) {
        scores = {}; at = 0; show(0, true);
        return;
      }

      var choice = e.target.closest('[data-score]');
      if (!choice) return;

      choice.getAttribute('data-score').split(',').forEach(function (pair) {
        var parts = pair.split(':');
        var key = parts[0].trim();
        scores[key] = (scores[key] || 0) + Number(parts[1]);
      });

      at++;
      if (at < questions.length) show(at, true); else finish();
    });

    show(0, false);
  })();

})();
