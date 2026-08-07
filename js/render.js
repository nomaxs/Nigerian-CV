/* =========================================================
   render.js — tiny, dependency-free data-binding engine
   used to turn a template.html + a data object into a
   filled-in CV / cover letter. Same engine powers the
   gallery thumbnails (sample data), the live preview
   (user data) and the PDF export — so a template only has
   to be written once.

   Binding vocabulary used inside each templates/.../template.html:
     data-field="a.b.c"   -> element.textContent = value at path
     data-field-html="a"  -> value written as HTML (line breaks -> <br>)
     data-list="a.b"      -> element holds one <template>; cloned once
                             per item in the array at that path
     data-field="."       -> (inside a data-list clone) the item itself
                             is a string/primitive
     data-if="a.b"        -> element removed from the DOM if the value
                             at that path is empty / falsy / empty array
     data-field-img="a.b" -> sets the element's src attribute from that
                             path (used for an uploaded photo); the
                             element is removed entirely if the value is
                             empty, so photo-less CVs never show a broken
                             image icon
   ========================================================= */

(function (global) {
  function getPath(obj, path) {
    if (!path || path === '.') return obj;
    return path.split('.').reduce((acc, key) => (acc == null ? undefined : acc[key]), obj);
  }

  function textToHtml(str) {
    const div = document.createElement('div');
    div.textContent = str == null ? '' : String(str);
    return div.innerHTML.replace(/\n/g, '<br>');
  }

  function isEmpty(val) {
    if (val == null) return true;
    if (Array.isArray(val)) return val.length === 0;
    if (typeof val === 'string') return val.trim() === '';
    return false;
  }

  function bindScope(root, data) {
    // 1. data-if — prune empty sections first
    root.querySelectorAll('[data-if]').forEach((el) => {
      const path = el.getAttribute('data-if');
      if (isEmpty(getPath(data, path))) el.remove();
    });

    // 2. data-list — repeatable blocks
    root.querySelectorAll('[data-list]').forEach((container) => {
      const path = container.getAttribute('data-list');
      const items = getPath(data, path);
      const tpl = container.querySelector('template');
      if (!tpl) return;
      if (!Array.isArray(items) || items.length === 0) {
        container.remove();
        return;
      }
      items.forEach((item) => {
        const node = tpl.content.cloneNode(true);
        const frag = document.createElement('div');
        frag.appendChild(node);
        bindScope(frag, item);
        // append the clone's children directly, skip the wrapper div
        while (frag.firstChild) container.insertBefore(frag.firstChild, tpl);
      });
    });

    // 3. data-field / data-field-html — leaf values. Skip anything that
    //    now lives inside a nested data-list, since that subtree was
    //    already bound (against its own item) by the recursive call above.
    const insideNestedList = (el) => {
      const listAncestor = el.closest('[data-list]');
      return listAncestor && root.contains(listAncestor);
    };
    root.querySelectorAll('[data-field]').forEach((el) => {
      if (insideNestedList(el)) return;
      const path = el.getAttribute('data-field');
      const val = getPath(data, path);
      el.textContent = val == null || val === '' ? el.getAttribute('data-fallback') || '' : val;
    });
    root.querySelectorAll('[data-field-html]').forEach((el) => {
      if (insideNestedList(el)) return;
      const path = el.getAttribute('data-field-html');
      const val = getPath(data, path);
      el.innerHTML = isEmpty(val) ? (el.getAttribute('data-fallback') || '') : textToHtml(val);
    });

    // 4. data-field-img — photo elements; removed entirely if empty so a
    //    photo-less profile never shows a broken image icon
    root.querySelectorAll('[data-field-img]').forEach((el) => {
      if (insideNestedList(el)) return;
      const path = el.getAttribute('data-field-img');
      const val = getPath(data, path);
      if (isEmpty(val)) {
        el.remove();
      } else {
        el.setAttribute('src', val);
      }
    });
  }

  function renderInto(rootEl, data) {
    bindScope(rootEl, data);
  }

  global.TemplateEngine = { renderInto, getPath, isEmpty };
})(window);
