(function () {
  const DOC_TYPE = document.body.getAttribute('data-doc-type'); // "cv" | "cover-letter"
  const grid = document.getElementById('galleryGrid');
  const chipRow = document.getElementById('chipRow');
  const searchInput = document.getElementById('searchInput');
  const emptyState = document.getElementById('emptyState');
  const overlay = document.getElementById('previewOverlay');
  const overlayFrame = document.getElementById('overlayFrame');
  const overlayUseBtn = document.getElementById('overlayUseBtn');
  const overlayClose = document.getElementById('overlayClose');
  const overlayTitle = document.getElementById('overlayTitle');

  const THEME_KEYS = ['signature', 'alt', 'mono'];
  let COMBOS = [];       // every layout x theme combination for this doc type
  let PROFESSIONS = [];  // profession list for this doc type
  let currentProfession = '';
  let themeFilter = 'all'; // 'all' | 'color' | 'mono'

  const filterRow = document.getElementById('themeFilterRow');
  if (filterRow) {
    filterRow.querySelectorAll('[data-filter]').forEach((btn) => {
      btn.addEventListener('click', () => {
        themeFilter = btn.getAttribute('data-filter');
        filterRow.querySelectorAll('[data-filter]').forEach((b) => b.classList.toggle('active', b === btn));
        renderGrid();
      });
    });
  }

  function visibleCombos() {
    if (themeFilter === 'color') return COMBOS.filter((c) => !c.isMono);
    if (themeFilter === 'mono') return COMBOS.filter((c) => c.isMono);
    return COMBOS;
  }

  function buildCombos(layoutsData) {
    const layouts = layoutsData[DOC_TYPE] || [];
    const combos = [];
    layouts.forEach((layout) => {
      THEME_KEYS.forEach((themeKey) => {
        const themeMeta = themeKey === 'mono' ? layoutsData.mono : layout.themes[themeKey];
        if (!themeMeta) return;
        combos.push({
          layoutId: layout.id,
          layoutName: layout.name,
          themeKey,
          themeLabel: themeMeta.label,
          isMono: themeKey === 'mono',
        });
      });
    });
    return combos;
  }

  function sealText(c) {
    return c.isMono ? 'B&W' : c.themeLabel.split(' ')[0];
  }

  function cardHtml(c) {
    return `
      <div class="tpl-card" data-layout="${c.layoutId}" data-theme="${c.themeKey}">
        <div class="tpl-thumb">
          <span class="seal-badge">${sealText(c)}</span>
          <iframe src="render.html?type=${DOC_TYPE}&layout=${c.layoutId}&theme=${c.themeKey}&profession=${currentProfession}&mode=sample" tabindex="-1" aria-hidden="true"></iframe>
        </div>
        <div class="tpl-meta">
          <div class="name">${c.layoutName}</div>
          <div class="tags">${c.themeLabel}</div>
        </div>
      </div>`;
  }

  function scaleThumbs() {
    document.querySelectorAll('.tpl-thumb').forEach((thumb) => {
      const iframe = thumb.querySelector('iframe');
      if (!iframe) return;
      const w = thumb.clientWidth;
      iframe.style.transform = `scale(${w / 850})`;
    });
  }

  function renderGrid() {
    const list = visibleCombos();
    grid.innerHTML = list.map(cardHtml).join('');
    emptyState.style.display = list.length ? 'none' : 'block';
    requestAnimationFrame(scaleThumbs);
    grid.querySelectorAll('.tpl-card').forEach((card, i) => {
      card.addEventListener('click', () => openOverlay(list[i]));
    });
  }

  function buildChips() {
    chipRow.innerHTML = PROFESSIONS
      .map((p) => `<button type="button" class="chip${p.id === currentProfession ? ' active' : ''}" data-p="${p.id}">${p.name}</button>`)
      .join('');
    chipRow.querySelectorAll('.chip').forEach((chip) => {
      chip.addEventListener('click', () => {
        currentProfession = chip.getAttribute('data-p');
        chipRow.querySelectorAll('.chip').forEach((c) => c.classList.toggle('active', c === chip));
        renderGrid();
      });
    });
  }

  function applySearch() {
    const q = (searchInput.value || '').trim().toLowerCase();
    let visible = PROFESSIONS;
    if (q) {
      visible = PROFESSIONS.filter((p) => (p.name + ' ' + (p.tags || []).join(' ')).toLowerCase().includes(q));
    }
    chipRow.innerHTML = visible
      .map((p) => `<button type="button" class="chip${p.id === currentProfession ? ' active' : ''}" data-p="${p.id}">${p.name}</button>`)
      .join('') || '<span class="muted" style="font-size:13px;padding:8px 4px;">No matching job category — showing current templates.</span>';
    chipRow.querySelectorAll('.chip').forEach((chip) => {
      chip.addEventListener('click', () => {
        currentProfession = chip.getAttribute('data-p');
        renderGrid();
        applySearch();
      });
    });
    // if the search narrows to exactly one profession, preview it live
    if (q && visible.length === 1 && visible[0].id !== currentProfession) {
      currentProfession = visible[0].id;
      renderGrid();
    }
  }

  function openOverlay(c) {
    overlayFrame.src = `render.html?type=${DOC_TYPE}&layout=${c.layoutId}&theme=${c.themeKey}&profession=${currentProfession}&mode=sample`;
    overlayUseBtn.href = `create.html?type=${DOC_TYPE}&layout=${c.layoutId}&theme=${c.themeKey}&profession=${currentProfession}`;
    overlayTitle.textContent = `${c.layoutName} — ${c.themeLabel}`;
    overlay.classList.add('open');
    requestAnimationFrame(() => {
      const wrap = overlayFrame.parentElement;
      const scale = wrap.clientWidth / 850;
      overlayFrame.style.transform = `scale(${scale})`;
      wrap.style.height = Math.min(1100 * scale, window.innerHeight * 0.6) + 'px';
    });
  }
  function closeOverlay() {
    overlay.classList.remove('open');
    overlayFrame.src = 'about:blank';
  }
  overlayClose.addEventListener('click', closeOverlay);
  overlay.addEventListener('click', (e) => { if (e.target === overlay) closeOverlay(); });

  searchInput.addEventListener('input', applySearch);
  window.addEventListener('resize', scaleThumbs);

  const presetQ = new URLSearchParams(location.search).get('q');
  if (presetQ) searchInput.value = presetQ;

  Promise.all([
    fetch('data/layouts.json').then((r) => r.json()),
    fetch('data/professions.json').then((r) => r.json()),
  ]).then(([layoutsData, professionsData]) => {
    COMBOS = buildCombos(layoutsData);
    PROFESSIONS = professionsData[DOC_TYPE] || [];
    currentProfession = (PROFESSIONS[0] && PROFESSIONS[0].id) || '';
    buildChips();
    renderGrid();
    if (presetQ) applySearch();
  }).catch(() => {
    grid.innerHTML = '';
    emptyState.style.display = 'block';
  });
})();
