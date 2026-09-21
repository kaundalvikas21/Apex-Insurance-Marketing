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
     8. Panel groups
     9. Triage widget
    10. Coverage calculator
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
    var drawer = $('[data-nav-panel]');
    if (!toggle || !drawer || !drawer.showModal) return;

    function close() { if (drawer.open) drawer.close(); }

    toggle.addEventListener('click', function () {
      if (drawer.open) { close(); return; }
      drawer.showModal();                       // focus trap, Escape and backdrop are native
      toggle.setAttribute('aria-expanded', 'true');
    });

    // One handler: the backdrop (a click on the <dialog> itself, outside its
    // inner panel), the close button, and any link, so a same-page anchor does
    // not leave the drawer open over the section it jumped to.
    drawer.addEventListener('click', function (e) {
      if (e.target === drawer || e.target.closest('[data-nav-close], a')) close();
    });

    // Fires for Escape too. Focus goes back to the toggle explicitly: a dialog
    // restores the previously focused element, and Safari never focuses a
    // button on tap, so there would be nothing to restore.
    drawer.addEventListener('close', function () {
      toggle.setAttribute('aria-expanded', 'false');
      toggle.focus({ preventScroll: true });
    });

    // Rotating a tablet or widening the window brings the desktop nav back.
    var wide = window.matchMedia('(min-width: 1024px)');
    var onWide = function () { if (wide.matches) close(); };
    if (wide.addEventListener) wide.addEventListener('change', onWide); else wide.addListener(onWide);
  })();

  // Desktop "Insurance" menu. It is a native <details>, so it opens without
  // this file. This only adds the closing behaviour a menu is expected to have.
  (function navDropdown() {
    var dd = $('[data-nav-dd]');
    if (!dd) return;

    document.addEventListener('click', function (e) {
      if (dd.open && (!dd.contains(e.target) || e.target.closest('.nav-dd-menu a'))) dd.open = false;
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && dd.open) {
        dd.open = false;
        $('summary', dd).focus();
      }
    });
  })();

  /* ------------------------------------------------------------------------
     3b. TIMED DIALOG
     One native <dialog>, opened once per session at the first of 30 seconds
     or half the page scrolled. showModal() supplies the focus trap, Escape,
     and the backdrop. Never in senior mode, and never over an open form.
     --------------------------------------------------------------------- */
  (function timedDialog() {
    var dlg = $('[data-dialog-timed]');
    if (!dlg || !dlg.showModal || document.documentElement.classList.contains('fe')) return;

    var KEY = 'ax_dialog_' + dlg.id;
    try { if (sessionStorage.getItem(KEY)) return; } catch (e) { return; }

    var timer = setTimeout(open, 30000);
    window.addEventListener('scroll', onScroll, { passive: true });

    function onScroll() {
      var max = document.documentElement.scrollHeight - window.innerHeight;
      if (max > 0 && window.scrollY / max >= 0.5) open();
    }

    // Never over the quiz. It sits at about half way down the page, which is
    // also this dialog's scroll trigger, so without this the dialog lands on
    // top of it just as someone arrives. Returning early keeps the scroll
    // listener alive, so the dialog simply waits until they have moved on.
    function quizOnScreen() {
      var quiz = $('[data-triage]');
      if (!quiz) return false;
      var r = quiz.getBoundingClientRect();
      return r.bottom > 0 && r.top < window.innerHeight;
    }

    function open() {
      var busy = document.activeElement && document.activeElement.closest('[data-triage], [data-nav-panel]');
      if (dlg.open || busy || quizOnScreen()) return;
      clearTimeout(timer);
      window.removeEventListener('scroll', onScroll);
      try { sessionStorage.setItem(KEY, '1'); } catch (e) {}
      dlg.showModal();
      track('dialog_open', { dialog: dlg.id });
    }

    dlg.addEventListener('click', function (e) {
      if (e.target === dlg) dlg.close();               // backdrop
      if (e.target.closest('[data-dialog-cta]')) track('dialog_cta', { dialog: dlg.id });
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
    input.classList.remove('is-valid');
    // initForm() gives every error node an id, so this always resolves and a
    // screen reader reads the message when focus lands on the field.
    if (node.id) input.setAttribute('aria-describedby', node.id);
  }

  function clearError(input) {
    var node = errorNode(input);
    input.removeAttribute('aria-invalid');
    input.removeAttribute('aria-describedby');
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
    // A tick for a required answer that passed. An icon, not only a colour.
    input.classList.toggle('is-valid', input.tagName === 'INPUT' && input.hasAttribute('required') && !!value);
    return true;
  }

  // Radio groups validate as a set, not per input.
  function validateRadioGroup(form, name) {
    var group = $$('input[type="radio"][name="' + name + '"]', form);
    if (!group.length || !group[0].hasAttribute('required')) return true;
    var chosen = group.some(function (r) { return r.checked; });
    // .field first: on a multi-step form the fieldset is the whole step, and
    // its first .field-error may belong to a different question.
    var wrap = group[0].closest('.field') || group[0].closest('fieldset');
    var node = wrap && $('.field-error', wrap);
    var set = wrap && ($('[role="group"]', wrap) || wrap);
    if (set) {
      if (chosen) { set.removeAttribute('aria-invalid'); set.removeAttribute('aria-describedby'); }
      else { set.setAttribute('aria-invalid', 'true'); if (node && node.id) set.setAttribute('aria-describedby', node.id); }
    }
    if (node) {
      node.classList.toggle('is-shown', !chosen);
      setMessage(node, chosen ? '' : (wrap.getAttribute('data-error') || 'Choose an option.'));
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

  // One routine for Continue and for Submit. The first problem may be a text
  // control, a radio group (focus its first radio), or the consent box.
  function focusFirstInvalid(scope) {
    var bad = $('[aria-invalid="true"], .consent[data-invalid="true"]', scope);
    if (!bad) return;
    var target = bad.matches('input, select, textarea') ? bad : $('input, select, textarea', bad);
    if (target && target.focus) target.focus();
    else bad.scrollIntoView({ block: 'center', behavior: reduceMotion ? 'auto' : 'smooth' });
  }

  // Per-field messages are read on focus through aria-describedby. This is the
  // one polite summary, so a failed Continue or Submit is not silent.
  function announce(form, scope) {
    var status = $('[data-form-status]', form);
    if (!status) return;
    var n = $$('[aria-invalid="true"], .consent[data-invalid="true"]', scope).length;
    status.textContent = n ? (n === 1 ? '1 answer needs attention.' : n + ' answers need attention.') : '';
  }

  // (555) 018-0199 as it is typed. Only when the caret is at the end, so
  // correcting a digit in the middle is never fought.
  function formatPhone(input) {
    if (input.selectionStart !== input.value.length) return;
    var d = input.value.replace(/\D/g, '').slice(0, 10);
    input.value = d.length > 6 ? '(' + d.slice(0, 3) + ') ' + d.slice(3, 6) + '-' + d.slice(6)
      : d.length > 3 ? '(' + d.slice(0, 3) + ') ' + d.slice(3)
      : d;
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
    // Test hook, like AX_DEBUG: window.AX_FAIL_SUBMIT = true (or "offline")
    // rejects, so the failure state can be seen before a backend exists.
    if (window.AX_FAIL_SUBMIT) {
      return Promise.reject(new Error(window.AX_FAIL_SUBMIT === 'offline' ? 'offline' : 'test failure'));
    }
    console.log('[lead] would POST:', payload);
    return Promise.resolve();
  }

  function initForm(form) {
    var siloValue = form.getAttribute('data-silo') || 'site';
    var formName = form.getAttribute('data-form-name') || 'unnamed_form';
    var submitting = false;
    // One id per form load. A retry after a failure re-sends the same id, so
    // the CRM can drop the duplicate. There is deliberately no automatic
    // retry: a lead POST is not idempotent.
    var submissionId = (window.crypto && crypto.randomUUID) ? crypto.randomUUID()
      : 'ax-' + Date.now().toString(36) + Math.random().toString(36).slice(2, 10);

    $$('.field-error', form).forEach(function (node, i) {
      if (!node.id) node.id = (form.id || formName) + '-err-' + i;
    });
    var status = document.createElement('p');
    status.className = 'sr-only';
    status.setAttribute('aria-live', 'polite');
    status.setAttribute('data-form-status', '');
    form.appendChild(status);

    // Compliance: source URL and silo captured on every submission.
    var src = $('input[name="source_url"]', form);
    var silo = $('input[name="silo"]', form);
    var fname = $('input[name="form_name"]', form);
    if (src) src.value = window.location.href;
    if (silo) silo.value = siloValue;
    if (fname) fname.value = formName;

    // form_start fires once, on first real interaction.
    form.addEventListener('focusin', function (e) {
      // On the form, not in a closure: a rate-table prefill starts it too.
      if (form.axStarted) return;
      if (!e.target.matches('input, select, textarea')) return;
      if (e.target.type === 'hidden') return;
      form.axStarted = true;
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
        var rule = input.getAttribute('data-validate');
        if (rule === 'phone') formatPhone(input);
        else if (rule === 'age' || rule === 'ageSenior') input.value = input.value.replace(/\D/g, '');
        if (input.getAttribute('aria-invalid') === 'true') validateField(input);
        else input.classList.remove('is-valid');
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
      // button.disabled does not stop Enter in another field re-firing submit.
      if (submitting) return;

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

      announce(form, form);
      if (!valid) { focusFirstInvalid(form); return; }

      var payload = {};
      new FormData(form).forEach(function (value, key) {
        if (key === 'company_website') return;
        payload[key] = value;
      });
      payload.submitted_at = new Date().toISOString();
      payload.submission_id = submissionId;

      var button = $('[type="submit"]', form);
      var failure = $('[data-form-error]', form);
      // Child nodes, not textContent: a label with an icon survives the round trip.
      if (button && !button.axLabel) button.axLabel = Array.prototype.slice.call(button.childNodes);

      function setButton(text, busy) {
        if (!button) return;
        button.disabled = busy;
        if (busy) button.setAttribute('aria-busy', 'true'); else button.removeAttribute('aria-busy');
        button.textContent = text;
      }

      submitting = true;
      if (failure) { failure.classList.remove('is-shown'); setMessage(failure, ''); }
      setButton('Sending...', true);

      // A request that never answers must not leave "Sending..." up for ever.
      var timeout = new Promise(function (_, reject) {
        setTimeout(function () { reject(new Error('timeout')); }, 15000);
      });

      Promise.race([submitLead(payload), timeout]).then(function () {
        submitting = false;
        if (button) { button.textContent = ''; button.axLabel.forEach(function (n) { button.appendChild(n); }); }
        track('form_submit', {
          form_name: formName,
          silo: siloValue,
          page_path: window.location.pathname,
          source_url: payload.source_url
        });
        showSuccess(form);
      }).catch(function (err) {
        // Recoverable: say what happened and what to do, keep every answer,
        // and make the button the retry. The role="alert" node announces it.
        submitting = false;
        setButton('Try again', false);
        var offline = (err && err.message === 'offline') || navigator.onLine === false;
        if (failure) {
          setMessage(failure, offline
            ? 'You appear to be offline. Check your connection, then press Try again. Your answers are still here.'
            : 'We could not send that. Your answers are still here: press Try again, or call us and we will take them by phone.');
          failure.classList.add('is-shown');
        }
        track('form_error', { form_name: formName, silo: siloValue, reason: offline ? 'offline' : (err && err.message === 'timeout' ? 'timeout' : 'failed') });
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
        var title = live[index].getAttribute('data-step-title');
        label.textContent = (branchChosen()
          ? 'Step ' + (index + 1) + ' of ' + live.length
          : 'Step ' + (index + 1)) + (title ? ' \u00b7 ' + title : '');
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
        var ok = collect(live[index], form);
        announce(form, live[index]);
        if (!ok) { focusFirstInvalid(live[index]); return; }
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

      // Same flag initForm() uses, so a prefill followed by typing in the form
      // is one form_start, not two.
      if (!form.axStarted) {
        form.axStarted = true;
        track('form_start', {
          form_name: form.getAttribute('data-form-name'),
          silo: form.getAttribute('data-silo'),
          page_path: window.location.pathname,
          trigger: button.getAttribute('data-prefill-trigger') || 'rate_table_prefill'
        });
      }

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
    var head = $('[data-triage-head]', widget);
    var segs = $$('[data-triage-seg]', widget);
    var back = $('[data-triage-back]', widget);
    // One data-score string per answered question. Scores are summed from this
    // at the end, which is what makes Back a pop() rather than a subtraction.
    var picks = [];
    var busy = false;

    function show(step, moveFocus) {
      questions.forEach(function (q, i) { q.hidden = i !== step; });
      results.forEach(function (r) { r.hidden = true; });
      $$('[aria-pressed]', questions[step]).forEach(function (b) { b.setAttribute('aria-pressed', 'false'); });
      if (head) head.hidden = false;
      if (back) back.hidden = step === 0;
      segs.forEach(function (seg, i) { seg.classList.toggle('is-done', i <= step); });
      if (progress) progress.textContent = 'Question ' + (step + 1) + ' of ' + questions.length;
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
      var scores = {};
      picks.forEach(function (pick) {
        pick.split(',').forEach(function (pair) {
          var parts = pair.split(':');
          var key = parts[0].trim();
          scores[key] = (scores[key] || 0) + Number(parts[1]);
        });
      });

      var winner = 'term';
      var best = -1;
      Object.keys(scores).forEach(function (key) {
        if (scores[key] > best) { best = scores[key]; winner = key; }
      });

      questions.forEach(function (q) { q.hidden = true; });
      if (head) head.hidden = true;
      if (back) back.hidden = true;
      results.forEach(function (r) { r.hidden = r.getAttribute('data-triage-result') !== winner; });

      var shown = results.filter(function (r) { return !r.hidden; })[0];
      if (shown) { shown.setAttribute('tabindex', '-1'); shown.focus({ preventScroll: true }); }

      track('triage_complete', { recommended_silo: winner });
    }

    widget.addEventListener('click', function (e) {
      if (busy) return;

      // Every result panel has its own restart button, so this is delegated
      // rather than bound to a single node.
      if (e.target.closest('[data-triage-restart]')) {
        picks = []; show(0, true);
        return;
      }
      if (e.target.closest('[data-triage-back]')) {
        picks.pop(); show(picks.length, true);
        return;
      }

      var choice = e.target.closest('[data-score]');
      if (!choice) return;

      // Show the pick before moving on, so the tap visibly did something.
      choice.setAttribute('aria-pressed', 'true');
      picks.push(choice.getAttribute('data-score'));
      busy = true;
      setTimeout(function () {
        busy = false;
        if (picks.length < questions.length) show(picks.length, true); else finish();
      }, reduceMotion ? 0 : 240);
    });

    show(0, false);
  })();

  /* ------------------------------------------------------------------------
     10. COVERAGE CALCULATOR (term spoke)
     No email gate: every figure is derived and shown in the page, and the
     derivation is the point.

     The markup ships a worked example already filled in, so with JavaScript
     off the page is a complete, readable derivation rather than a column of
     zeros. This takes over from the first edit and deliberately does NOT
     recompute on load, so the authored example and the live one can never
     disagree on first paint.

     Contract, all inside one [data-calc]:
       [data-calc-field="..."]  income | years | debt | children | perchild |
                                existing. Any input or select, read as a number.
       [data-calc-out="..."]    EVERY match is written, so one figure can sit in
                                the table, the headline, and the CTA label.
       [data-calc-cta]          prefill button. Section 7 reads data-prefill at
                                click time, so rewriting the attribute here is
                                the whole bridge into the quote form.
       [data-calc-enough]       shown instead of the CTA when the need is zero.
     --------------------------------------------------------------------- */
  (function calculator() {
    var box = $('[data-calc]');
    if (!box) return;

    // Coverage on the quote form is a <select>. A value that is not one of its
    // options sets the field to "" without complaining, so the recommendation
    // has to land on this ladder. Rounding UP is also what an agent does:
    // buying too little is the more common and more expensive mistake.
    // data-calc-ladder lets a second silo reuse this engine with its own
    // coverage options. Whole life sells from $25,000; term does not.
    var LADDER = (box.getAttribute('data-calc-ladder') ||
                  '100000,250000,500000,750000,1000000,2000000')
                 .split(',').map(Number);
    var fired = false;

    function num(role) {
      var el = $('[data-calc-field="' + role + '"]', box);
      if (!el) return 0;
      // Strip $ and thousands separators: people type "80,000", and parseFloat
      // would read that as 80. NaN > 0 is false, so a blank field reads as 0.
      var n = parseFloat((el.value || '').replace(/[^0-9.]/g, ''));
      return n > 0 ? n : 0;
    }

    function money(n) { return '$' + Math.round(n).toLocaleString('en-US'); }

    function put(role, text) {
      $$('[data-calc-out="' + role + '"]', box).forEach(function (el) {
        el.textContent = text;
      });
    }

    function compute() {
      var perYear = num('income');
      var years = num('years');
      var kids = num('children');
      var perKid = num('perchild');
      var income = perYear * years;
      var debt = num('debt');
      var education = kids * perKid;
      var existing = num('existing');
      var raw = income + debt + education - existing;

      // The raw > 0 guard matters: without it the first rung always matches a
      // negative need, and a household that is already over covered would be
      // told to buy $100,000 instead of seeing the "you have enough" note.
      var rounded = 0;
      if (raw > 0) {
        for (var i = 0; i < LADDER.length; i++) {
          if (LADDER[i] >= raw) { rounded = LADDER[i]; break; }
        }
        // Above the top of the ladder the quote form's own option reads
        // "$2,000,000 or more", so that is the honest answer.
        if (!rounded) rounded = LADDER[LADDER.length - 1];
      }

      put('incomeyear', money(perYear));
      put('years', String(years));
      put('children', String(kids));
      put('perchild', money(perKid));
      put('income', money(income));
      put('debt', money(debt));
      put('education', money(education));
      put('existing', money(existing));
      put('raw', money(raw > 0 ? raw : 0));
      put('rounded', money(rounded));

      var cta = $('[data-calc-cta]', box);
      var enough = $('[data-calc-enough]', box);
      if (cta) {
        cta.hidden = !rounded;
        cta.setAttribute('data-prefill', '{"coverage":"' + rounded + '"}');
      }
      if (enough) enough.hidden = !!rounded;
      return rounded;
    }

    box.addEventListener('input', compute);

    // calculator_complete fires once, on the first finished edit that produces
    // a figure, not on every keystroke. Income, debt, and dependants stay OUT
    // of the dataLayer: the recommendation is the only number the marketing
    // side needs, and the only one here that is not personal financial detail.
    box.addEventListener('change', function () {
      var rounded = compute();
      if (fired || !rounded) return;
      fired = true;
      track('calculator_complete', {
        calculator_name: box.getAttribute('data-calc') || 'unnamed_calculator',
        coverage: rounded,
        silo: document.body.getAttribute('data-silo') || 'site',
        page_path: window.location.pathname
      });
    });
  })();

})();
