const AdminState = {
  lessons: [],
  overview: null,
  quality: []
};

const DRAFT_KEY = 'smartedu_admin_lesson_draft';
const FLAG_KEY = 'smartedu_admin_flags';

function initAdminAuthNav() {
  const nav = document.querySelector('header nav');
  if (!nav) return;

  const findAuthLink = (target) => {
    const links = Array.from(nav.querySelectorAll('a[href]'));
    return links.find(link => {
      const href = link.getAttribute('href');
      if (!href) return false;
      const base = href.split('#')[0].split('?')[0];
      return base.endsWith(target);
    }) || null;
  };

  let login = findAuthLink('login.html');
  if (!login) {
    login = document.createElement('a');
    login.href = 'login.html';
    login.textContent = 'Login';
    nav.appendChild(login);
  }
  login.dataset.auth = 'login';
  login.classList.add('auth-link', 'auth-login');

  let signup = findAuthLink('signup.html');
  if (!signup) {
    signup = document.createElement('a');
    signup.href = 'signup.html';
    signup.textContent = 'Sign Up';
    signup.className = 'btn btn-primary';
    signup.style.padding = '0.5rem 1rem';
    nav.appendChild(signup);
  }
  signup.dataset.auth = 'signup';
  signup.classList.add('auth-link');

  let logout = nav.querySelector('[data-auth="logout"]');
  if (!logout) {
    logout = document.createElement('a');
    logout.href = '#';
    logout.textContent = 'Logout';
    logout.className = 'btn btn-secondary';
    logout.style.padding = '0.5rem 1rem';
    logout.dataset.auth = 'logout';
    nav.appendChild(logout);
  }

  const isAuthed = Boolean(localStorage.getItem('currentUser'));
  nav.querySelectorAll('[data-auth="login"]').forEach(link => link.classList.toggle('auth-hidden', isAuthed));
  nav.querySelectorAll('[data-auth="signup"]').forEach(link => link.classList.toggle('auth-hidden', isAuthed));
  nav.querySelectorAll('[data-auth="logout"]').forEach(link => {
    link.classList.toggle('auth-hidden', !isAuthed);
    if (!link.dataset.bound) {
      link.addEventListener('click', (event) => {
        event.preventDefault();
        localStorage.removeItem('currentUser');
        window.location.href = 'index.html';
      });
      link.dataset.bound = 'true';
    }
  });
}

function enforceAdminAccess() {
  const gate = document.getElementById('adminAccessGate');
  const shell = document.querySelector('.admin-shell');
  const currentUser = localStorage.getItem('currentUser');

  if (!currentUser) {
    if (shell) shell.classList.add('locked');
    if (gate) {
      gate.classList.add('show');
      gate.setAttribute('aria-hidden', 'false');
    }
    return false;
  }

  if (shell) shell.classList.remove('locked');
  if (gate) {
    gate.classList.remove('show');
    gate.setAttribute('aria-hidden', 'true');
  }
  return true;
}

function scrollToSection(id) {
  const target = document.getElementById(id);
  if (target) {
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

async function refreshAdminData() {
  await Promise.all([loadOverview(), loadLessons(), loadQualityQueue()]);
}

async function loadOverview() {
  try {
    const response = await fetch('/api/admin/overview');
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || 'Failed to load overview');

    AdminState.overview = data;
    updateStats(data);
    renderLatestLessons(data.latest_lessons || []);
    renderChart('difficultyChart', data.difficulty_counts || {}, 'Difficulty Mix');
    renderChart('subjectChart', data.subject_counts || {}, 'Subject Coverage');
  } catch (error) {
    console.error(error);
  }
}

async function loadLessons() {
  try {
    const response = await fetch('/api/admin/lessons?limit=200');
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || 'Failed to load lessons');

    AdminState.lessons = data.data || [];
    populateLessonSelect(AdminState.lessons);
  } catch (error) {
    console.error(error);
  }
}

async function loadQualityQueue() {
  try {
    const response = await fetch('/api/admin/quality-check');
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || 'Failed to load quality queue');

    AdminState.quality = data.data || [];
    renderQualityQueue(AdminState.quality);
  } catch (error) {
    console.error(error);
  }
}

function setSeedStatus(message, tone) {
  const status = document.getElementById('seedStatus');
  if (!status) return;
  status.textContent = message;
  status.classList.remove('success', 'error');
  if (tone === 'success') status.classList.add('success');
  if (tone === 'error') status.classList.add('error');
}

async function seedDatabase() {
  const tokenInput = document.getElementById('seedTokenInput');
  const resetToggle = document.getElementById('seedReset');
  const token = tokenInput ? tokenInput.value.trim() : '';

  if (!token) {
    setSeedStatus('Seed token is required.', 'error');
    return;
  }

  const reset = resetToggle ? resetToggle.checked : true;
  setSeedStatus('Seeding database...', 'success');

  try {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 25000);

    const response = await fetch('/api/admin/seed', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Seed-Token': token
      },
      body: JSON.stringify({ reset }),
      signal: controller.signal
    });
    clearTimeout(timeout);
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || 'Seed failed');

    sessionStorage.setItem('smartedu_seed_token', token);
    setSeedStatus('Database seeded successfully.', 'success');
    await refreshAdminData();
  } catch (error) {
    const message = error.name === 'AbortError'
      ? 'Seed timed out. If on Vercel Hobby, seed locally or upgrade plan.'
      : `Seed failed: ${error.message}`;
    setSeedStatus(message, 'error');
  }
}

function updateStats(data) {
  const counts = data.counts || {};
  const statLessons = document.getElementById('statLessons');
  const statBooks = document.getElementById('statBooks');
  const statUsers = document.getElementById('statUsers');
  const statDuration = document.getElementById('statDuration');

  if (statLessons) statLessons.textContent = counts.lessons || 0;
  if (statBooks) statBooks.textContent = counts.books || 0;
  if (statUsers) statUsers.textContent = counts.users || 0;
  if (statDuration) statDuration.textContent = `${data.avg_duration || 0} min`;
}

function renderLatestLessons(lessons) {
  const container = document.getElementById('latestLessons');
  if (!container) return;

  if (!lessons || lessons.length === 0) {
    container.innerHTML = '<div class="empty-state">No recent lessons available.</div>';
    return;
  }

  container.innerHTML = lessons.map(lesson => `
    <div class="list-item">
      <div>
        <strong>${lesson.title}</strong>
        <div class="list-meta">${lesson.subject} | ${lesson.difficulty}</div>
      </div>
      <div class="list-right">${lesson.duration_minutes} min</div>
    </div>
  `).join('');
}

function renderChart(targetId, data, label) {
  const container = document.getElementById(targetId);
  if (!container) return;

  const entries = Object.entries(data);
  if (entries.length === 0) {
    container.innerHTML = '<div class="empty-state">No data available.</div>';
    return;
  }

  const total = entries.reduce((sum, item) => sum + item[1], 0) || 1;
  container.innerHTML = entries.map(([key, value]) => {
    const percent = Math.round((value / total) * 100);
    return `
      <div class="bar-row">
        <div class="bar-label">${key}</div>
        <div class="bar-track">
          <div class="bar-fill" style="width: ${percent}%"></div>
        </div>
        <div class="bar-value">${value}</div>
      </div>
    `;
  }).join('');
}

function populateLessonSelect(lessons) {
  const select = document.getElementById('lessonSelect');
  if (!select) return;

  select.innerHTML = lessons.map(lesson => `
    <option value="${lesson.id}">${lesson.title}</option>
  `).join('');

  if (lessons.length > 0) {
    loadLessonForUpdate(lessons[0].id);
    select.addEventListener('change', (event) => loadLessonForUpdate(event.target.value));
  }
}

function loadLessonForUpdate(lessonId) {
  const lesson = AdminState.lessons.find(item => String(item.id) === String(lessonId));
  if (!lesson) return;

  document.getElementById('updateDifficulty').value = (lesson.difficulty || 'beginner').toLowerCase();
  document.getElementById('updateDuration').value = lesson.duration_minutes || 30;
  document.getElementById('updateSubject').value = lesson.subject || '';
  document.getElementById('updateStatus').textContent = 'Editing selected lesson.';
}

async function updateLesson() {
  const select = document.getElementById('lessonSelect');
  if (!select) return;

  const lessonId = select.value;
  const payload = {
    difficulty: document.getElementById('updateDifficulty').value,
    duration_minutes: parseInt(document.getElementById('updateDuration').value, 10) || 30,
    subject: document.getElementById('updateSubject').value.trim()
  };

  try {
    const response = await fetch(`/api/admin/lessons/${lessonId}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || 'Update failed');

    document.getElementById('updateStatus').textContent = 'Lesson updated successfully.';
    await loadLessons();
    await loadOverview();
  } catch (error) {
    document.getElementById('updateStatus').textContent = `Update failed: ${error.message}`;
  }
}

function parseSteps(value) {
  return value.split('\n').map(line => line.trim()).filter(Boolean);
}

function parseQuiz(value) {
  const lines = value.split('\n').map(line => line.trim()).filter(Boolean);
  return lines.map(line => {
    const parts = line.split('|').map(part => part.trim());
    if (parts.length < 3) return null;
    const options = parts[1].split(';').map(opt => opt.trim()).filter(Boolean);
    const correct = parseInt(parts[2], 10);
    return {
      question: parts[0],
      options,
      correct: Number.isNaN(correct) ? 0 : correct
    };
  }).filter(Boolean);
}

function setLessonStatus(message, tone) {
  const status = document.getElementById('lessonFormStatus');
  if (!status) return;
  status.textContent = message;
  status.classList.remove('success', 'error');
  if (tone === 'success') status.classList.add('success');
  if (tone === 'error') status.classList.add('error');
}

function saveLessonDraft() {
  const draft = getLessonFormData();
  localStorage.setItem(DRAFT_KEY, JSON.stringify(draft));
  setLessonStatus('Draft saved locally. You can publish anytime.', 'success');
}

function loadLessonDraft() {
  const raw = localStorage.getItem(DRAFT_KEY);
  if (!raw) return;
  try {
    const draft = JSON.parse(raw);
    document.getElementById('lessonTitle').value = draft.title || '';
    document.getElementById('lessonDescription').value = draft.description || '';
    document.getElementById('lessonSubject').value = draft.subject || '';
    document.getElementById('lessonDifficulty').value = draft.difficulty || 'beginner';
    document.getElementById('lessonDuration').value = draft.duration_minutes || 45;
    document.getElementById('lessonVideo').value = draft.video_url || '';
    document.getElementById('lessonInformation').value = draft.information || '';
    document.getElementById('lessonSteps').value = (draft.steps || []).join('\n');
    document.getElementById('lessonQuiz').value = formatQuizDraft(draft.quiz || []);
    setLessonStatus('Draft loaded. Review and publish when ready.', 'success');
  } catch (error) {
    console.error(error);
  }
}

function formatQuizDraft(quiz) {
  return quiz.map(item => {
    const options = (item.options || []).join(';');
    return `${item.question} | ${options} | ${item.correct}`;
  }).join('\n');
}

function getLessonFormData() {
  return {
    title: document.getElementById('lessonTitle').value.trim(),
    description: document.getElementById('lessonDescription').value.trim(),
    subject: document.getElementById('lessonSubject').value.trim(),
    difficulty: document.getElementById('lessonDifficulty').value,
    duration_minutes: parseInt(document.getElementById('lessonDuration').value, 10) || 45,
    video_url: document.getElementById('lessonVideo').value.trim(),
    information: document.getElementById('lessonInformation').value.trim(),
    steps: parseSteps(document.getElementById('lessonSteps').value),
    quiz: parseQuiz(document.getElementById('lessonQuiz').value)
  };
}

async function handleLessonSubmit(event) {
  event.preventDefault();
  const payload = getLessonFormData();

  if (!payload.title || !payload.description || !payload.subject) {
    setLessonStatus('Please complete title, description, and subject.', 'error');
    return;
  }

  try {
    const response = await fetch('/api/admin/lessons', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || 'Failed to create lesson');

    setLessonStatus('Lesson published successfully.', 'success');
    localStorage.removeItem(DRAFT_KEY);
    document.getElementById('lessonForm').reset();
    await refreshAdminData();
  } catch (error) {
    setLessonStatus(`Publish failed: ${error.message}`, 'error');
  }
}

function addFlag() {
  const input = document.getElementById('flagNote');
  if (!input) return;
  const note = input.value.trim();
  if (!note) return;

  const list = loadFlags();
  list.unshift({ id: Date.now(), note });
  localStorage.setItem(FLAG_KEY, JSON.stringify(list));
  input.value = '';
  renderFlagList(list);
}

function loadFlags() {
  const stored = localStorage.getItem(FLAG_KEY);
  if (!stored) return [];
  try {
    const parsed = JSON.parse(stored);
    return Array.isArray(parsed) ? parsed : [];
  } catch (error) {
    return [];
  }
}

function removeFlag(id) {
  const list = loadFlags().filter(item => item.id !== id);
  localStorage.setItem(FLAG_KEY, JSON.stringify(list));
  renderFlagList(list);
}

function renderFlagList(list) {
  const container = document.getElementById('flagList');
  if (!container) return;

  if (!list || list.length === 0) {
    container.innerHTML = '<div class="empty-state">No manual flags yet.</div>';
    return;
  }

  container.innerHTML = list.map(item => `
    <div class="list-item">
      <div>${item.note}</div>
      <button class="btn btn-secondary" onclick="removeFlag(${item.id})">Resolve</button>
    </div>
  `).join('');
}

function renderQualityQueue(items) {
  const container = document.getElementById('qualityQueue');
  if (!container) return;

  if (!items || items.length === 0) {
    container.innerHTML = '<div class="empty-state">No issues detected. Great job.</div>';
    return;
  }

  container.innerHTML = items.map(item => `
    <div class="list-item">
      <div>
        <strong>${item.title}</strong>
        <div class="list-meta">${item.subject} | ${item.difficulty}</div>
        <div class="issue-list">${item.issues.map(issue => `<span class="issue-pill">${issue}</span>`).join('')}</div>
      </div>
      <div class="list-right">ID ${item.id}</div>
    </div>
  `).join('');
}

document.addEventListener('DOMContentLoaded', () => {
  initAdminAuthNav();
  if (!enforceAdminAccess()) return;

  const form = document.getElementById('lessonForm');
  if (form) form.addEventListener('submit', handleLessonSubmit);

  const seedInput = document.getElementById('seedTokenInput');
  if (seedInput) {
    const saved = sessionStorage.getItem('smartedu_seed_token');
    if (saved) seedInput.value = saved;
  }

  loadLessonDraft();
  renderFlagList(loadFlags());
  refreshAdminData();
});
