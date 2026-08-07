(async function () {
  const type = qs('type', 'cv');
  const layout = qs('layout', '');
  const theme = qs('theme', 'signature');
  const professionParam = qs('profession', '');
  const draftKey = `builderDraft_${type}_${layout}_${theme}`;

  document.body.setAttribute('data-type', type);
  document.getElementById('backLink').href = type === 'cv' ? 'cv.html' : 'cover-letter.html';
  document.getElementById('formTitle').textContent = type === 'cv' ? 'Fill in your CV details' : 'Fill in your cover letter';
  document.getElementById('formSub').textContent = type === 'cv'
    ? "Your information stays on this device until you're ready to download."
    : 'Keep it short — three focused paragraphs read best.';

  // ---- fetch layout metadata (for photo support) and profession presets (for autofill) ----
  let layoutsData = null, professionsData = null;
  try {
    [layoutsData, professionsData] = await Promise.all([
      fetch('data/layouts.json').then((r) => r.json()),
      fetch('data/professions.json').then((r) => r.json()),
    ]);
  } catch (e) { /* fall back to blank form below if this fails */ }

  const layoutMeta = layoutsData && (layoutsData[type] || []).find((l) => l.id === layout);
  const supportsPhoto = type === 'cv' && layoutMeta && layoutMeta.supportsPhoto;
  if (supportsPhoto) document.getElementById('photoField').style.display = '';

  const blank = () => (type === 'cv'
    ? {
        personal: { fullName: '', title: '', phone: '', email: '', location: '', linkedin: '', summary: '', photo: '' },
        education: [{ institution: '', degree: '', course: '', year: '' }],
        experience: [{ company: '', position: '', dates: '', responsibilities: [''] }],
        skills: [], certifications: [], languages: [],
        references: [{ name: '', relation: '', phone: '', email: '' }],
      }
    : {
        personal: { fullName: '', phone: '', email: '', location: '' },
        recipient: { hiringManager: '', company: '', companyAddress: '' },
        date: new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }),
        salutation: 'Dear Hiring Manager,',
        body: [''],
        closing: 'Yours faithfully,',
      });

  let state;
  let prefilled = false;
  try {
    const saved = sessionStorage.getItem(draftKey);
    if (saved) {
      state = JSON.parse(saved);
    } else if (professionParam && professionsData) {
      const list = professionsData[type] || [];
      const entry = list.find((p) => p.id === professionParam);
      if (entry) {
        state = JSON.parse(JSON.stringify(entry.sample)); // deep copy — never mutate the preset
        if (type === 'cv' && state.personal) state.personal.photo = '';
        prefilled = true;
      }
    }
    if (!state) state = blank();
  } catch (e) {
    state = blank();
  }

  function persist() {
    sessionStorage.setItem(draftKey, JSON.stringify(state));
  }
  persist(); // save immediately so a prefilled draft survives a refresh

  if (prefilled) {
    const banner = document.createElement('div');
    banner.className = 'section-block';
    banner.style.cssText = 'background:var(--sage-pale);border-color:var(--sage);display:flex;align-items:center;justify-content:space-between;gap:10px;';
    banner.innerHTML = '<span style="font-size:13px;color:var(--sage-deep);font-weight:700;">Pre-filled with a sample entry for this job — edit any field below.</span>';
    const hero = document.querySelector('.form-hero');
    hero.parentElement.insertBefore(banner, hero.nextSibling);
  }

  // ---- photo upload ----
  if (supportsPhoto) {
    const fileInput = document.getElementById('f_photo');
    const previewWrap = document.getElementById('photoPreviewWrap');
    function drawPhotoPreview() {
      previewWrap.innerHTML = '';
      if (!state.personal.photo) return;
      const row = document.createElement('div');
      row.className = 'photo-preview';
      row.innerHTML = `<img src="${state.personal.photo}" alt=""><button type="button">Remove photo</button>`;
      row.querySelector('button').addEventListener('click', () => {
        state.personal.photo = '';
        fileInput.value = '';
        persist();
        drawPhotoPreview();
      });
      previewWrap.appendChild(row);
    }
    fileInput.addEventListener('change', () => {
      const file = fileInput.files && fileInput.files[0];
      if (!file) return;
      if (file.size > 4 * 1024 * 1024) {
        showToast("That photo is a bit large — try one under 4MB.");
        fileInput.value = '';
        return;
      }
      const reader = new FileReader();
      reader.onload = () => {
        state.personal.photo = reader.result;
        persist();
        drawPhotoPreview();
      };
      reader.readAsDataURL(file);
    });
    drawPhotoPreview();
  }

  function bindSimple(id, path) {
    const el = document.getElementById(id);
    if (!el) return;
    const [a, b] = path.split('.');
    el.value = b ? (state[a] && state[a][b]) || '' : state[a] || '';
    el.addEventListener('input', () => {
      if (b) { state[a] = state[a] || {}; state[a][b] = el.value; }
      else { state[a] = el.value; }
      persist();
    });
  }

  if (type === 'cv') {
    ['fullName', 'title', 'phone', 'email', 'location', 'linkedin', 'summary'].forEach((k) =>
      bindSimple('f_' + k, 'personal.' + k)
    );
  } else {
    ['fullName', 'phone', 'email', 'location'].forEach((k) => bindSimple('f_' + k, 'personal.' + k));
    bindSimple('f_recipientName', 'recipient.hiringManager');
    bindSimple('f_company', 'recipient.company');
    bindSimple('f_companyAddress', 'recipient.companyAddress');
    bindSimple('f_date', 'date');
    bindSimple('f_salutation', 'salutation');
    bindSimple('f_closing', 'closing');
  }

  // ---------- generic repeat-group renderer ----------
  function renderRepeat(containerId, countId, items, fieldsHtml, onInputBind, addDefault) {
    const container = document.getElementById(containerId);
    const countEl = document.getElementById(countId);
    if (countEl) countEl.textContent = items.length;
    container.innerHTML = items
      .map((item, i) => `<div class="repeat-item" data-i="${i}">
          ${items.length > 1 ? '<button type="button" class="repeat-remove" data-remove="' + i + '">✕</button>' : ''}
          ${fieldsHtml(item, i)}
        </div>`)
      .join('');
    container.querySelectorAll('[data-remove]').forEach((btn) => {
      btn.addEventListener('click', () => {
        items.splice(Number(btn.getAttribute('data-remove')), 1);
        persist();
        renderRepeat(containerId, countId, items, fieldsHtml, onInputBind, addDefault);
      });
    });
    onInputBind(container, items);
  }

  // ---- Education ----
  function eduFields(item) {
    return `
      <div class="field"><label>Institution</label><input data-k="institution" value="${esc(item.institution)}" placeholder="e.g. University of Lagos" /></div>
      <div class="field-row">
        <div class="field"><label>Degree</label><input data-k="degree" value="${esc(item.degree)}" placeholder="B.Sc. …" /></div>
        <div class="field"><label>Year</label><input data-k="year" value="${esc(item.year)}" placeholder="2019 – 2023" /></div>
      </div>
      <div class="field"><label>Course / grade</label><input data-k="course" value="${esc(item.course)}" placeholder="Second Class Upper" /></div>`;
  }
  function bindRepeatInputs(container, items) {
    container.querySelectorAll('[data-i]').forEach((row) => {
      const i = Number(row.getAttribute('data-i'));
      row.querySelectorAll('[data-k]').forEach((input) => {
        input.addEventListener('input', () => {
          items[i][input.getAttribute('data-k')] = input.value;
          persist();
        });
      });
    });
  }
  function renderEdu() {
    renderRepeat('eduList', 'eduCount', state.education, eduFields, bindRepeatInputs);
  }

  // ---- Experience ----
  function expFields(item) {
    return `
      <div class="field-row">
        <div class="field"><label>Company</label><input data-k="company" value="${esc(item.company)}" /></div>
        <div class="field"><label>Position</label><input data-k="position" value="${esc(item.position)}" /></div>
      </div>
      <div class="field"><label>Dates</label><input data-k="dates" value="${esc(item.dates)}" placeholder="Jan 2023 – Present" /></div>
      <div class="field"><label>Responsibilities (one per line)</label><textarea data-k="responsibilities">${esc((item.responsibilities || []).join('\n'))}</textarea></div>`;
  }
  function bindExpInputs(container, items) {
    container.querySelectorAll('[data-i]').forEach((row) => {
      const i = Number(row.getAttribute('data-i'));
      row.querySelectorAll('[data-k]').forEach((input) => {
        input.addEventListener('input', () => {
          const k = input.getAttribute('data-k');
          if (k === 'responsibilities') items[i][k] = input.value.split('\n').map((s) => s.trim()).filter(Boolean);
          else items[i][k] = input.value;
          persist();
        });
      });
    });
  }
  function renderExp() {
    renderRepeat('expList', 'expCount', state.experience, expFields, bindExpInputs);
  }

  // ---- References ----
  function refFields(item) {
    return `
      <div class="field-row">
        <div class="field"><label>Name</label><input data-k="name" value="${esc(item.name)}" /></div>
        <div class="field"><label>Relation</label><input data-k="relation" value="${esc(item.relation)}" placeholder="e.g. Manager, Company" /></div>
      </div>
      <div class="field-row">
        <div class="field"><label>Phone</label><input data-k="phone" value="${esc(item.phone)}" /></div>
        <div class="field"><label>Email</label><input data-k="email" value="${esc(item.email)}" /></div>
      </div>`;
  }
  function renderRef() {
    renderRepeat('refList', 'refCount', state.references, refFields, bindRepeatInputs);
  }

  // ---- Cover letter body paragraphs ----
  function bodyFields(item, i) {
    return `<div class="field"><label>Paragraph ${i + 1}</label><textarea data-k="." style="min-height:96px;">${esc(item)}</textarea></div>`;
  }
  function bindBodyInputs(container, items) {
    container.querySelectorAll('[data-i]').forEach((row) => {
      const i = Number(row.getAttribute('data-i'));
      row.querySelectorAll('[data-k]').forEach((input) => {
        input.addEventListener('input', () => { items[i] = input.value; persist(); });
      });
    });
  }
  function renderBody() {
    renderRepeat('bodyList', null, state.body, bodyFields, bindBodyInputs);
  }

  function esc(v) {
    return (v == null ? '' : String(v)).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  if (type === 'cv') {
    renderEdu(); renderExp(); renderRef();
    document.getElementById('addEdu').addEventListener('click', () => {
      state.education.push({ institution: '', degree: '', course: '', year: '' }); persist(); renderEdu();
    });
    document.getElementById('addExp').addEventListener('click', () => {
      state.experience.push({ company: '', position: '', dates: '', responsibilities: [''] }); persist(); renderExp();
    });
    document.getElementById('addRef').addEventListener('click', () => {
      state.references.push({ name: '', relation: '', phone: '', email: '' }); persist(); renderRef();
    });

    // ---- tag inputs ----
    function setupTags(wrapId, inputId, key) {
      const wrap = document.getElementById(wrapId);
      const input = document.getElementById(inputId);
      const addBtn = document.getElementById(inputId.replace('Input', 'AddBtn'));
      function draw() {
        wrap.querySelectorAll('.tag-pill').forEach((p) => p.remove());
        state[key].forEach((tag, i) => {
          const pill = document.createElement('span');
          pill.className = 'tag-pill';
          pill.innerHTML = `${esc(tag)} <button type="button" aria-label="Remove">✕</button>`;
          pill.querySelector('button').addEventListener('click', () => {
            state[key].splice(i, 1); persist(); draw();
          });
          wrap.insertBefore(pill, input);
        });
      }
      function addFromInput() {
        const value = input.value.trim().replace(/,$/, '');
        if (!value) return;
        state[key].push(value);
        input.value = '';
        persist();
        draw();
        input.focus();
      }
      if (addBtn) addBtn.addEventListener('click', addFromInput);
      input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ',') {
          e.preventDefault();
          addFromInput();
        } else if (e.key === 'Backspace' && !input.value && state[key].length) {
          state[key].pop(); persist(); draw();
        }
      });
      draw();
    }
    setupTags('skillsWrap', 'skillsInput', 'skills');
    setupTags('certsWrap', 'certsInput', 'certifications');
    setupTags('langsWrap', 'langsInput', 'languages');
  } else {
    renderBody();
    document.getElementById('addBody').addEventListener('click', () => {
      state.body.push(''); persist(); renderBody();
    });
  }

  document.getElementById('clearBtn').addEventListener('click', () => {
    if (!confirm('Clear everything you\'ve entered on this form?')) return;
    state = blank();
    sessionStorage.removeItem(draftKey);
    location.reload();
  });

  document.getElementById('previewBtn').addEventListener('click', () => {
    persist();
    sessionStorage.setItem('builderData', JSON.stringify(state));
    sessionStorage.setItem('builderMeta', JSON.stringify({ type, layout, theme }));
    location.href = `preview.html?type=${type}&layout=${layout}&theme=${theme}`;
  });
})();
