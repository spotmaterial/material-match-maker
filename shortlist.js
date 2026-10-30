/* Shortlist + navigation shared by every matchmaker page (index, material, innovation, search, shortlist).
   - Shortlist lives in this browser (localStorage; falls back to memory if storage is blocked) as a list of
     codes; card details come from the read-only function match_items(p_codes).
   - Adds a small bar at the top right: "Your matches" (back to the swipe results, when there are some) and
     "Shortlist (n)".
   - On material.html / innovation.html: a "Save to shortlist" button under the name, and on innovation pages
     "Visit company website" / "Ask about samples" (both open the company's site; no emails are stored). */
(function () {
  const SUPABASE = 'https://bjkkqawalpuvsubnbodt.supabase.co';
  const KEY = 'sb_publishable_ZZN2JFwNHFbBLLjh2DE3cg_4t1YvQ7m';
  const LS = 'spot_match_shortlist';
  let mem = [];
  const read = () => { try { return JSON.parse(localStorage.getItem(LS) || '[]'); } catch (e) { return mem; } };
  const write = (a) => { mem = a; try { localStorage.setItem(LS, JSON.stringify(a)); } catch (e) { /* memory only */ } fire(); };
  const listeners = [];
  const fire = () => { listeners.forEach((f) => { try { f(read()); } catch (e) {} }); paintBar(); };
  async function rpc(fn, body) {
    const r = await fetch(`${SUPABASE}/rest/v1/rpc/${fn}`, { method: 'POST', headers: { apikey: KEY, 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
    if (!r.ok) throw new Error(r.statusText); return r.json();
  }
  const S = window.Shortlist = {
    codes: () => read(),
    has: (code) => read().includes(code),
    add: (code) => { const a = read(); if (!a.includes(code)) { a.unshift(code); write(a); } },
    remove: (code) => write(read().filter((c) => c !== code)),
    toggle: (code) => (S.has(code) ? S.remove(code) : S.add(code), S.has(code)),
    set: (codes) => write([...new Set(codes)]),
    onChange: (f) => listeners.push(f),
    items: (codes) => codes.length ? rpc('match_items', { p_codes: codes }) : Promise.resolve([]),
    img: (it) => !it || !it.image ? '' : it.image_kind === 'storage' ? `${SUPABASE}/storage/v1/object/public/images/${it.image}` : it.image,
    page: (it) => (it.kind === 'innovation' ? 'innovation.html' : 'material.html') + '?code=' + encodeURIComponent(it.code),
    hasMatches: () => { try { return !!sessionStorage.getItem('spot_match_state'); } catch (e) { return false; } },
  };
  window.addEventListener('storage', (e) => { if (e.key === LS) fire(); });

  // ---- top bar
  const css = document.createElement('style');
  css.textContent = `
  .sl-bar { position: fixed; top: 10px; right: 12px; z-index: 50; display: flex; gap: 8px; font: 14px/1.2 Inter, system-ui, sans-serif; }
  .sl-bar a { background: #fff; color: #111; border: 1px solid #d9d6cf; border-radius: 999px; padding: 7px 13px; text-decoration: none; box-shadow: 0 1px 4px rgba(0,0,0,.06); white-space: nowrap; }
  .sl-bar a.on { background: #111; color: #fff; border-color: #111; }
  .sl-save { display: inline-flex; align-items: center; gap: 6px; margin: 10px 8px 0 0; padding: 9px 15px; border-radius: 999px; border: 1px solid #111; background: #fff; color: #111; font: inherit; font-size: 16px; cursor: pointer; text-decoration: none; }
  .sl-save.saved, .sl-save.dark { background: #111; color: #fff; }
  @media print { .sl-bar { display: none; } }`;
  document.head.appendChild(css);
  const bar = document.createElement('div'); bar.className = 'sl-bar';
  function paintBar() {
    const n = read().length, here = location.pathname.split('/').pop() || 'index.html';
    const back = here !== 'index.html' && S.hasMatches() ? '<a href="index.html#results">← Your matches</a>' : '';
    bar.innerHTML = back + `<a href="shortlist.html" class="${n ? 'on' : ''}" title="Your shortlist">♡ Shortlist${n ? ` (${n})` : ''}</a>`;
  }
  const mount = () => { const z = parseFloat(getComputedStyle(document.documentElement).zoom) || 1; if (z < 1) bar.style.zoom = String(1 / z);
    document.body.appendChild(bar); paintBar(); detailButtons(); };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount); else mount();

  // ---- material / innovation pages: save + contact buttons once the record has loaded
  function detailButtons() {
    const content = document.getElementById('content'), name = document.getElementById('name');
    const code = new URLSearchParams(location.search).get('code');
    if (!content || !name || !code) return;
    const isInn = /innovation\.html$/.test(location.pathname) || code.startsWith('INN-');
    const add = async () => {
      if (content.hidden || document.getElementById('slActions')) return;
      const box = document.createElement('div'); box.id = 'slActions';
      const save = document.createElement('button'); save.type = 'button'; save.className = 'sl-save';
      const paint = () => { const on = S.has(code); save.classList.toggle('saved', on); save.textContent = on ? '♥ Saved to shortlist' : '♡ Save to shortlist'; };
      save.onclick = () => { S.toggle(code); paint(); }; S.onChange(paint); paint(); box.appendChild(save);
      name.insertAdjacentElement('afterend', box);
      if (isInn) {
        try {
          const [it] = await S.items([code]);
          if (it && it.company_url) box.insertAdjacentHTML('beforeend',
            `<a class="sl-save dark" href="${it.company_url.replace(/"/g, '&quot;')}" target="_blank" rel="noopener">Visit company website ↗</a>` +
            `<a class="sl-save" href="${it.company_url.replace(/"/g, '&quot;')}" target="_blank" rel="noopener" title="Opens the company's website; look for contact or sample requests there">Ask about samples ↗</a>`);
        } catch (e) { /* buttons are optional */ }
      }
    };
    new MutationObserver(add).observe(content, { attributes: true, attributeFilter: ['hidden'] }); add();
  }
})();
