/* Browser-local study controls. No network requests or external dependencies. */
(() => {
  'use strict';
  const $ = (selector, root = document) => root.querySelector(selector);
  const all = (selector, root = document) => [...root.querySelectorAll(selector)];
  const cards = all('.card');
  const key = 'fintech-fieldnotes-v1';
  let state = { done: [], saved: [], notes: {}, theme: 'light', size: 18 };
  let category = 'all';
  let concealed = false;
  let printedDetails = [];
  try {
    const saved = JSON.parse(localStorage.getItem(key) || 'null');
    if (saved && typeof saved === 'object') {
      state.done = Array.isArray(saved.done) ? saved.done.filter(x => typeof x === 'string') : [];
      state.saved = Array.isArray(saved.saved) ? saved.saved.filter(x => typeof x === 'string') : [];
      state.notes = saved.notes && typeof saved.notes === 'object' && !Array.isArray(saved.notes) ? saved.notes : {};
      state.theme = saved.theme === 'dark' ? 'dark' : 'light';
      state.size = Number.isFinite(saved.size) ? Math.min(24, Math.max(16, saved.size)) : 18;
    }
  } catch (_) { $('#storage-warning').hidden = false; }
  const persist = () => {
    try { localStorage.setItem(key, JSON.stringify(state)); }
    catch (_) { $('#storage-warning').hidden = false; }
  };
  const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/đ/g, 'd').replace(/Đ/g, 'D').toLowerCase();
  const searchable = new Map(cards.map(card => [card.id, normalize(card.textContent)]));
  function applyAppearance() {
    document.body.classList.toggle('dark', state.theme === 'dark');
    document.documentElement.style.setProperty('--reading', `${state.size}px`);
    $('#theme').textContent = state.theme === 'dark' ? 'Giao diện sáng' : 'Giao diện tối';
    $('#theme').setAttribute('aria-label', state.theme === 'dark' ? 'Chuyển sang giao diện sáng' : 'Chuyển sang giao diện tối');
    $('#font-down').disabled = state.size <= 16;
    $('#font-up').disabled = state.size >= 24;
  }
  function refreshProgress() {
    const completed = cards.filter(c => state.done.includes(c.id)).length;
    $('#progress').value = completed;
    $('#progress-label').textContent = `${completed}/${cards.length}`;
    cards.forEach(card => {
      const done = state.done.includes(card.id), saved = state.saved.includes(card.id);
      card.classList.toggle('completed', done);
      $('.done-toggle', card).setAttribute('aria-pressed', String(done));
      $('.done-toggle', card).textContent = done ? '✓ Đã luyện' : 'Đánh dấu đã luyện';
      $('.save-toggle', card).setAttribute('aria-pressed', String(saved));
      $('.save-toggle', card).textContent = saved ? '★ Đã lưu' : 'Lưu câu';
    });
  }
  function filterCards() {
    const query = normalize($('#search').value.trim());
    const mode = $('#filter').value;
    let count = 0;
    cards.forEach(card => {
      const matchesCategory = category === 'all' || card.dataset.group === category;
      const matchesQuery = !query || searchable.get(card.id).includes(query);
      const matchesMode = mode === 'all' || (mode === 'priority' && card.dataset.priority === 'true') ||
        (mode === 'saved' && state.saved.includes(card.id)) || (mode === 'done' && state.done.includes(card.id)) ||
        (mode === 'todo' && !state.done.includes(card.id));
      card.hidden = !(matchesCategory && matchesQuery && matchesMode);
      if (!card.hidden) count++;
    });
    $('#result-count').textContent = `${count} / ${cards.length} bài`;
    $('#empty').hidden = count !== 0;
    $('#section-title').textContent = category === 'all' ? 'Tất cả bài luyện' : category;
    all('.nav-item').forEach(button => {
      const active = button.dataset.category === category;
      button.classList.toggle('active', active);
      button.setAttribute('aria-pressed', String(active));
    });
  }
  function selectCategory(value, scroll = true) {
    category = value;
    filterCards();
    if (matchMedia('(max-width:700px)').matches) $('.nav-wrap').open = false;
    if (scroll) $('#library').scrollIntoView({ block: 'start' });
  }
  const showAnswer = (card, visible) => {
    $('.answer', card).hidden = !visible;
    $('.read-toggle', card).textContent = visible ? 'Ẩn script' : 'Hiện script';
    $('.read-toggle', card).setAttribute('aria-expanded', String(visible));
  };
  cards.forEach(card => {
    const note = $('[data-note]', card);
    note.value = typeof state.notes[card.id] === 'string' ? state.notes[card.id] : '';
    note.addEventListener('input', () => { state.notes[card.id] = note.value; persist(); });
    $('.read-toggle', card).addEventListener('click', () => showAnswer(card, $('.answer', card).hidden));
    [['.done-toggle', 'done'], ['.save-toggle', 'saved']].forEach(([selector, name]) => {
      $(selector, card).addEventListener('click', () => {
        state[name] = state[name].includes(card.id) ? state[name].filter(id => id !== card.id) : [...state[name], card.id];
        persist(); refreshProgress(); filterCards();
      });
    });
    $('.start-timer', card).addEventListener('click', event => startTimer(Number(event.currentTarget.dataset.minutes), $('h3', card).textContent));
  });
  all('.nav-item').forEach(button => button.addEventListener('click', () => selectCategory(button.dataset.category)));
  $('#search').addEventListener('input', filterCards);
  $('#filter').addEventListener('change', filterCards);
  $('#clear-filters').addEventListener('click', () => { $('#search').value = ''; $('#filter').value = 'all'; selectCategory('all', false); });
  $('#start-priority').addEventListener('click', () => { $('#search').value = ''; $('#filter').value = 'priority'; selectCategory('all'); });
  $('#open-design').addEventListener('click', () => { $('#search').value = ''; $('#filter').value = 'all'; selectCategory('System design • 40 phút'); showAnswer($('#design-withdrawal'), true); });
  $('#practice').addEventListener('click', () => {
    concealed = !concealed;
    cards.forEach(card => showAnswer(card, !concealed));
    $('#practice').setAttribute('aria-pressed', String(concealed));
    $('#practice').textContent = concealed ? 'Hiện tất cả script' : 'Ẩn tất cả script';
  });
  $('#theme').addEventListener('click', () => { state.theme = state.theme === 'dark' ? 'light' : 'dark'; applyAppearance(); persist(); });
  $('#font-down').addEventListener('click', () => { state.size = Math.max(16, state.size - 1); applyAppearance(); persist(); });
  $('#font-up').addEventListener('click', () => { state.size = Math.min(24, state.size + 1); applyAppearance(); persist(); });
  $('#print').addEventListener('click', () => window.print());
  window.addEventListener('beforeprint', () => {
    printedDetails = all('.card:not([hidden]) .deep-dive, .card:not([hidden]) .workbench').map(el => [el, el.open]);
    printedDetails.forEach(([el]) => { el.open = true; });
  });
  window.addEventListener('afterprint', () => { printedDetails.forEach(([el, wasOpen]) => { el.open = wasOpen; }); });
  let timerHandle = null, timerDeadline = 0, timerRemaining = 0, timerDuration = 0, timerPaused = false;
  function renderTimer() {
    const ms = timerPaused ? timerRemaining : Math.max(0, timerDeadline - Date.now());
    const seconds = Math.ceil(ms / 1000);
    $('#timer-display').textContent = `${String(Math.floor(seconds / 60)).padStart(2, '0')}:${String(seconds % 60).padStart(2, '0')}`;
    if (!timerPaused && ms === 0) {
      clearInterval(timerHandle); timerHandle = null;
      $('#timer').classList.add('finished');
      $('#timer-label').textContent = 'Hết giờ · tự đánh giá và luyện lại';
      $('#timer-pause').disabled = true;
      $('#announcement').textContent = 'Hết thời gian luyện nói. Bạn có thể bấm làm lại.';
    }
  }
  function startTimer(minutes, title) {
    clearInterval(timerHandle);
    timerDuration = minutes * 60 * 1000;
    timerRemaining = timerDuration; timerDeadline = Date.now() + timerDuration; timerPaused = false;
    $('#timer').hidden = false; $('#timer').classList.remove('finished');
    $('#timer-label').textContent = title; $('#timer').dataset.title = title;
    $('#timer-pause').textContent = 'Tạm dừng'; $('#timer-pause').disabled = false;
    $('#announcement').textContent = `Bắt đầu ${minutes} phút luyện nói.`;
    renderTimer(); timerHandle = setInterval(renderTimer, 250);
  }
  $('#timer-pause').addEventListener('click', () => {
    if (!timerPaused) { timerRemaining = Math.max(0, timerDeadline - Date.now()); timerPaused = true; }
    else { timerDeadline = Date.now() + timerRemaining; timerPaused = false; }
    $('#timer-pause').textContent = timerPaused ? 'Tiếp tục' : 'Tạm dừng'; renderTimer();
  });
  $('#timer-reset').addEventListener('click', () => startTimer(timerDuration / 60000, $('#timer').dataset.title));
  $('#timer-close').addEventListener('click', () => { clearInterval(timerHandle); timerHandle = null; $('#timer').hidden = true; });
  function revealHash() {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch (_) { return; }
    const card = document.getElementById(id);
    if (card && card.classList.contains('card')) {
      $('#search').value = ''; $('#filter').value = 'all'; selectCategory('all', false);
      showAnswer(card, true); requestAnimationFrame(() => card.scrollIntoView({ block: 'start' }));
    }
  }
  if (matchMedia('(max-width:700px)').matches) $('.nav-wrap').open = false;
  applyAppearance(); refreshProgress(); filterCards(); revealHash();
  window.addEventListener('hashchange', revealHash);
})();
