/* Thai Local – free draft request form.
   Submissions go to Supabase table public.thailocal_draft_requests with country='TH' (insert-only for the public key via RLS).
   The publishable key below is safe to expose: anon can INSERT rows into this one table and cannot read anything. */
(function () {
  var SUPABASE_URL = 'https://ivleheagpnenoaevpcjv.supabase.co';
  var SUPABASE_KEY = 'sb_publishable_zAv6QQS0k1tFsjyNJk2S0Q_YUC4K_gi';
  var ENDPOINT = SUPABASE_URL + '/rest/v1/thailocal_draft_requests';
  var WA = 'https://wa.me/66656495277';

  var form = document.getElementById('draftForm');
  if (!form) return;
  var btn = document.getElementById('submitBtn');
  var errBox = document.getElementById('formError');
  var thanks = document.getElementById('thanks');

  function val(id) { return (form.elements[id].value || '').trim(); }
  function setInvalid(id, bad) {
    var f = form.elements[id].closest('.field');
    if (f) f.classList.toggle('invalid', !!bad);
    return !bad;
  }
  function normUrl(u) {
    if (!u) return u;
    if (!/^https?:\/\//i.test(u)) u = 'https://' + u.replace(/^\/+/, '');
    return u;
  }
  function validate() {
    var fb = val('fb_url'), shop = val('shop_name'), contact = val('contact'), email = val('email');
    var fbOk = fb.length >= 5 && fb.length <= 500 && (/facebook|fb\.(com|me|watch)/i.test(fb) || /^(https?:\/\/)?[^\s]+\.[^\s]+/i.test(fb)) && !/\s/.test(fb);
    var ok = true;
    ok = setInvalid('fb_url', !fbOk) && ok;
    ok = setInvalid('shop_name', shop.length < 1 || shop.length > 200) && ok;
    ok = setInvalid('contact', contact.replace(/[\s\-]/g, '').length < 3 || contact.length > 200) && ok;
    ok = setInvalid('email', email && (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) || email.length > 254)) && ok;
    return ok;
  }
  ['fb_url', 'shop_name', 'contact', 'email'].forEach(function (id) {
    form.elements[id].addEventListener('input', function () {
      var f = this.closest('.field');
      if (f && f.classList.contains('invalid')) validate();
    });
  });

  function showThanks() {
    form.hidden = true;
    thanks.hidden = false;
    thanks.focus();
    thanks.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  function showError(payload) {
    var msg = 'ส่งไม่สำเร็จ กรุณาลองอีกครั้ง หรือส่งข้อมูลทาง WhatsApp<br><span lang="en">Sorry, that didn\'t send. Please try again, or send your details on WhatsApp.</span>';
    var text = 'สวัสดีครับ ขอเว็บตัวอย่างฟรี / Free draft request\n' +
      'Facebook: ' + payload.fb_url + '\nShop: ' + payload.shop_name + '\nContact: ' + payload.contact +
      (payload.email ? '\nEmail: ' + payload.email : '') + '\nCity: ' + (payload.city || '');
    errBox.innerHTML = msg + '<br><a href="' + WA + '?text=' + encodeURIComponent(text) + '" target="_blank" rel="noopener">WhatsApp 065 649 5277 →</a>';
    errBox.hidden = false;
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    errBox.hidden = true;
    if (!validate()) {
      var first = form.querySelector('.field.invalid input');
      if (first) first.focus();
      return;
    }
    // honeypot filled = bot: pretend success, send nothing
    if (val('website')) { showThanks(); return; }

    var payload = {
      fb_url: normUrl(val('fb_url')).slice(0, 500),
      shop_name: val('shop_name').slice(0, 200),
      contact: val('contact').slice(0, 200),
      email: val('email') || null,
      city: val('city').slice(0, 100) || null,
      country: 'TH',
      user_agent: (navigator.userAgent || '').slice(0, 500)
    };

    btn.disabled = true;
    var label = btn.innerHTML;
    btn.innerHTML = 'กำลังส่ง… <small lang="en">Sending…</small>';

    fetch(ENDPOINT, {
      method: 'POST',
      headers: {
        'apikey': SUPABASE_KEY,
        'Content-Type': 'application/json',
        'Prefer': 'return=minimal'
      },
      body: JSON.stringify(payload)
    }).then(function (res) {
      if (res.status === 201 || res.ok) { showThanks(); }
      else { throw new Error('HTTP ' + res.status); }
    }).catch(function () {
      showError(payload);
    }).then(function () {
      btn.disabled = false;
      btn.innerHTML = label;
    });
  });
})();
