// elearning.js - Course Grid with Search, Filters, Learning Paths, and Progress

let allLessons = [];
let computedPaths = [];
let guidedProjects = [];
let activePathId = null;
let activePathLessonIds = new Set();

const learningPathsConfig = [
  {
    id: 'path-python',
    title: 'Python Foundations',
    level: 'Beginner',
    description: 'Start from scratch and build confident Python fundamentals for real projects.',
    subjects: ['Python Basics', 'Python'],
    outcomes: ['Variables and data types', 'Control flow', 'Functions and modules', 'OOP basics']
  },
  {
    id: 'path-fullstack',
    title: 'Full-Stack Web Starter',
    level: 'Intermediate',
    description: 'Learn modern web development with HTML, CSS, JavaScript, and web foundations.',
    subjects: ['Web Development', 'JavaScript'],
    outcomes: ['Responsive layouts', 'Core JavaScript', 'Frontend projects']
  },
  {
    id: 'path-ai',
    title: 'AI Explorer',
    level: 'Intermediate',
    description: 'Build AI literacy with machine learning concepts and intelligent systems.',
    subjects: ['Artificial Intelligence', 'Computer Science'],
    outcomes: ['ML basics', 'AI applications', 'Ethics and safety']
  },
  {
    id: 'path-cs',
    title: 'Computer Science Core',
    level: 'Beginner',
    description: 'Master the foundations of CS, algorithms, and problem solving.',
    subjects: ['Computer Science'],
    outcomes: ['Algorithms', 'Data structures', 'Programming fundamentals']
  }
];

const difficultyOrder = {
  beginner: 1,
  intermediate: 2,
  advanced: 3
};

async function loadLessons() {
  try {
    const response = await fetch('/api/lessons');
    const data = await response.json();
    allLessons = data.data || data;

    const container = document.getElementById('lessonsContainer');

    if (!allLessons || allLessons.length === 0) {
      container.innerHTML = `
        <div class="card text-center" style="grid-column: 1/-1;">
          <p style="color: var(--text-muted);">No lessons available yet.</p>
        </div>
      `;
      return;
    }

    computedPaths = buildPaths(allLessons);
    guidedProjects = buildProjects(allLessons);
    ProgressStore.evaluateBadgesAndCertificates({ lessons: allLessons, paths: computedPaths });

    renderPaths(computedPaths);
    renderProjects(guidedProjects);
    updateProgressStats();
    renderCourses(allLessons);
    renderAchievements();
  } catch (error) {
    console.error('Error loading lessons:', error);
    alert('Failed to load lessons. Please try again.');
  }
}

function buildPaths(lessons) {
  return learningPathsConfig.map(path => {
    const lessonList = lessons
      .filter(lesson => path.subjects.includes(lesson.subject))
      .sort((a, b) => {
        const diffA = difficultyOrder[a.difficulty] || 0;
        const diffB = difficultyOrder[b.difficulty] || 0;
        if (diffA !== diffB) return diffA - diffB;
        return a.title.localeCompare(b.title);
      });

    const totalMinutes = lessonList.reduce((sum, lesson) => sum + (lesson.duration_minutes || 0), 0);
    return {
      ...path,
      lessons: lessonList,
      lessonIds: lessonList.map(lesson => String(lesson.id)),
      totalMinutes
    };
  });
}

function buildProjects(lessons) {
  const projects = Array.isArray(window.GuidedProjects) ? window.GuidedProjects : [];
  return projects.map(project => {
    const lesson = lessons.find(item => item.title === project.lessonTitle);
    return {
      ...project,
      lessonId: lesson ? String(lesson.id) : null
    };
  });
}

function renderPaths(paths) {
  const container = document.getElementById('pathsContainer');
  if (!container) return;

  if (!paths || paths.length === 0) {
    container.innerHTML = '<div class="empty-state">No learning paths available yet.</div>';
    return;
  }

  const progress = ProgressStore.load();

  let html = '';
  paths.forEach(path => {
    const completedCount = path.lessonIds.filter(id => ProgressStore.isLessonCompleted(id, progress)).length;
    const totalLessons = path.lessonIds.length || 1;
    const percent = Math.round((completedCount / totalLessons) * 100);
    const statusClass = percent === 100 ? 'complete' : percent > 0 ? 'in-progress' : 'locked';
    const statusText = percent === 100 ? 'Completed' : percent > 0 ? 'In progress' : 'Not started';
    const durationHours = Math.round((path.totalMinutes / 60) * 10) / 10;
    const modulePreview = path.lessons.slice(0, 4);
    const isActive = activePathId === path.id;

    html += `
      <div class="path-card${isActive ? ' active' : ''}">
        <div class="path-header">
          <div>
            <div class="path-level">${path.level}</div>
            <h4 style="margin: 0.5rem 0 0.75rem 0;">${path.title}</h4>
          </div>
          <span class="status-chip ${statusClass}">${statusText}</span>
        </div>
        <p style="margin: 0.5rem 0 1rem; color: var(--text-secondary);">${path.description}</p>
        <div class="path-meta">
          <span>${path.subjects.join(' | ')}</span>
          <span>${path.lessonIds.length} lessons</span>
          <span>${durationHours}h total</span>
        </div>
        <div class="progress-bar">
          <div class="progress-bar-fill" style="width: ${percent}%;"></div>
        </div>
        <div style="margin-top: 0.75rem; font-size: 0.85rem; color: var(--text-muted);">${completedCount}/${path.lessonIds.length} lessons completed</div>
        <div class="path-modules">
          ${modulePreview.map(lesson => {
            const completed = ProgressStore.isLessonCompleted(lesson.id, progress);
            return `<div class="module-item ${completed ? 'completed' : ''}">
              <span>${completed ? 'Done' : 'Next'}</span>
              <span>${lesson.title}</span>
            </div>`;
          }).join('')}
          ${path.lessons.length > modulePreview.length ? `<div class="module-item">+ ${path.lessons.length - modulePreview.length} more lessons</div>` : ''}
        </div>
        <div class="path-actions">
          <button class="btn btn-primary" onclick="startPath('${path.id}')">${isActive ? 'Active Path' : 'Start Path'}</button>
          <button class="btn btn-secondary" onclick="viewPath('${path.id}')">View Path</button>
        </div>
      </div>
    `;
  });

  container.innerHTML = html;
}

function renderProjects(projects) {
  const container = document.getElementById('projectsContainer');
  if (!container) return;

  if (!projects || projects.length === 0) {
    container.innerHTML = '<div class="empty-state">No guided projects available yet.</div>';
    return;
  }

  const progress = ProgressStore.load();
  let html = '';

  projects.forEach(project => {
    const submission = ProgressStore.getProjectSubmission(project.id, progress);
    const status = submission
      ? (submission.status === 'submitted' ? 'Submitted' : 'Draft saved')
      : 'Not started';
    const statusClass = submission
      ? (submission.status === 'submitted' ? 'complete' : 'in-progress')
      : 'locked';
    const lessonLabel = project.lessonId ? 'Project ready' : 'Lesson not found';

    const skills = Array.isArray(project.skills) ? project.skills : [];
    const steps = Array.isArray(project.steps) ? project.steps : [];

    html += `
      <div class="project-card">
        <div class="project-header">
          <div>
            <div class="project-level">${project.difficulty}</div>
            <h4 class="project-title">${project.title}</h4>
          </div>
          <span class="status-chip ${statusClass}">${status}</span>
        </div>
        <p class="project-summary">${project.summary}</p>
        <div class="project-meta">
          <span>${project.subject}</span>
          <span>${project.duration}</span>
          <span>${lessonLabel}</span>
        </div>
        <div class="project-tags">
          ${skills.slice(0, 2).map(skill => `<span class="project-tag">${skill}</span>`).join('')}
          ${skills.length > 2 ? `<span class="project-tag muted">+${skills.length - 2} more</span>` : ''}
        </div>
        <div class="project-steps">
          ${steps.slice(0, 3).map(step => `<div class="project-step">- ${step}</div>`).join('')}
          ${steps.length > 3 ? `<div class="project-step">+ ${steps.length - 3} more steps</div>` : ''}
        </div>
        <div class="project-actions">
          <button class="btn btn-primary" onclick="startProject('${project.id}')" ${project.lessonId ? '' : 'disabled'}>Start Project</button>
          <button class="btn btn-secondary" onclick="viewProjectDetails('${project.id}')">View Details</button>
        </div>
      </div>
    `;
  });

  container.innerHTML = html;
}

function startProject(projectId) {
  const project = guidedProjects.find(item => item.id === projectId);
  if (!project || !project.lessonId) return;
  window.location.href = `course.html?id=${project.lessonId}&project=${project.id}`;
}

function viewProjectDetails(projectId) {
  const project = guidedProjects.find(item => item.id === projectId);
  if (!project) return;
  const steps = project.steps.map(step => `- ${step}`).join('\n');
  const deliverables = project.deliverables.map(item => `- ${item}`).join('\n');
  alert(`${project.title}\n\nSteps:\n${steps}\n\nDeliverables:\n${deliverables}`);
}

function viewPath(pathId) {
  const path = computedPaths.find(item => item.id === pathId);
  if (!path) return;
  const lessonTitles = path.lessons.map(lesson => `- ${lesson.title}`).join('\n');
  alert(`${path.title}\n\nIncluded lessons:\n${lessonTitles}`);
}

function startPath(pathId) {
  const path = computedPaths.find(item => item.id === pathId);
  if (!path) return;

  if (activePathId === pathId) {
    activePathId = null;
    activePathLessonIds = new Set();
  } else {
    activePathId = pathId;
    activePathLessonIds = new Set(path.lessonIds);
  }

  renderPaths(computedPaths);
  filterCourses();
  document.getElementById('lessonsContainer').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function updateProgressStats() {
  const progress = ProgressStore.load();
  const stats = ProgressStore.getStats(allLessons, progress);

  const percentEl = document.getElementById('progressPercent');
  const certEl = document.getElementById('certCount');
  const badgeEl = document.getElementById('badgeCount');
  const hoursEl = document.getElementById('hoursCount');

  if (percentEl) percentEl.textContent = `${stats.percent}%`;
  if (certEl) certEl.textContent = progress.certificates.length;
  if (badgeEl) badgeEl.textContent = progress.badges.length;
  if (hoursEl) hoursEl.textContent = `${stats.hours}h`;
}

function renderAchievements() {
  const progress = ProgressStore.load();
  const badgesContainer = document.getElementById('badgesContainer');
  const certsContainer = document.getElementById('certificatesContainer');

  if (badgesContainer) {
    if (progress.badges.length === 0) {
      badgesContainer.innerHTML = '<div class="empty-state">Complete lessons to earn your first badge.</div>';
    } else {
      badgesContainer.innerHTML = progress.badges.map(badge => `
        <div class="badge-card">
          <div class="badge-pill">Badge</div>
          <h4 style="margin: 0.75rem 0 0.5rem;">${badge.title}</h4>
          <p style="margin: 0; color: var(--text-secondary);">${badge.description}</p>
          <p style="margin-top: 0.75rem; font-size: 0.85rem; color: var(--text-muted);">Issued ${new Date(badge.issuedAt).toLocaleDateString()}</p>
        </div>
      `).join('');
    }
  }

  if (certsContainer) {
    if (progress.certificates.length === 0) {
      certsContainer.innerHTML = '<div class="empty-state">Complete lessons and pass quizzes to unlock certificates.</div>';
    } else {
      certsContainer.innerHTML = progress.certificates.map(cert => `
        <div class="certificate-card">
          <div class="status-chip in-progress">${cert.type === 'path' ? 'Path Certificate' : 'Course Certificate'}</div>
          <h4 style="margin: 0.75rem 0 0.5rem;">${cert.title}</h4>
          <p style="margin: 0; color: var(--text-secondary);">Issued ${new Date(cert.issuedAt).toLocaleDateString()}</p>
          <div class="certificate-actions">
            <button class="btn btn-primary" onclick="openCertificate('${cert.id}')">View Certificate</button>
          </div>
        </div>
      `).join('');
    }
  }

  window.__smarteduCertificates = progress.certificates;
}

function openCertificate(certId) {
  const certs = window.__smarteduCertificates || [];
  const certificate = certs.find(item => item.id === certId);
  if (certificate) {
    ProgressStore.openCertificate(certificate);
  }
}

function renderCourses(lessons) {
  const container = document.getElementById('lessonsContainer');
  const progress = ProgressStore.load();

  if (!lessons || lessons.length === 0) {
    container.innerHTML = `
      <div class="card text-center" style="grid-column: 1/-1;">
        <p style="color: var(--text-muted);">No courses match your search or filters.</p>
      </div>
    `;
    document.getElementById('resultsCount').textContent = 'No courses found';
    return;
  }

  document.getElementById('resultsCount').textContent = `Showing ${lessons.length} course${lessons.length !== 1 ? 's' : ''}`;

  const bySubject = lessons.reduce((acc, lesson) => {
    if (!acc[lesson.subject]) acc[lesson.subject] = [];
    acc[lesson.subject].push(lesson);
    return acc;
  }, {});

  const getDifficultyColor = (diff) => {
    const colors = {
      beginner: '#3b82f6',
      intermediate: '#2563eb',
      advanced: '#1e40af'
    };
    return colors[diff.toLowerCase()] || '#2563eb';
  };

  let html = '';
  Object.entries(bySubject).forEach(([subject, subjectLessons]) => {
    html += `<div style="grid-column: 1/-1; margin-top: 2rem;">
      <h3 style="color: var(--text-primary); margin-bottom: 1.5rem; border-bottom: 2px solid var(--primary); padding-bottom: 0.5rem;">${subject}</h3>
      <div class="grid grid-3">`;

    subjectLessons.forEach(lesson => {
      const completed = ProgressStore.isLessonCompleted(lesson.id, progress);
      const quizScore = ProgressStore.getQuizScore(lesson.id, progress);
      const statusClass = completed ? 'complete' : 'locked';
      const statusText = completed ? 'Completed' : 'Not started';
      const scoreText = quizScore ? `${quizScore.score}% mastery` : 'No quiz score';

      html += `
        <div class="card lesson-card" onclick="window.location.href='course.html?id=${lesson.id}'" style="cursor: pointer;">
          <div style="margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: start;">
            <span class="badge" style="background: ${getDifficultyColor(lesson.difficulty)}; color: white; padding: 0.35rem 0.75rem; border-radius: 999px; font-size: 0.75rem; font-weight: 600; text-transform: capitalize;">
              ${lesson.difficulty}
            </span>
            <span class="status-chip ${statusClass}">${statusText}</span>
          </div>
          <h4 style="margin: 0.5rem 0 0.75rem 0; color: var(--text-primary); line-height: 1.4; min-height: 3rem;">${lesson.title}</h4>
          <p style="font-size: 0.875rem; color: var(--text-secondary); margin: 0.75rem 0; flex-grow: 1;">${lesson.description}</p>
          <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.8rem; color: var(--text-muted);">
            <span>Time: ${lesson.duration_minutes}m</span>
            <span>${scoreText}</span>
          </div>
          <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid var(--border);">
            <button class="btn btn-primary" style="width: 100%; cursor: pointer;" onmouseover="this.style.opacity='0.8'" onmouseout="this.style.opacity='1'">View Course</button>
          </div>
        </div>
      `;
    });

    html += `</div></div>`;
  });

  container.innerHTML = html;
}

function filterCourses() {
  const searchTerm = document.getElementById('searchInput').value.toLowerCase();
  const subjectFilter = document.getElementById('subjectFilter').value;
  const difficultyFilter = document.getElementById('difficultyFilter').value.toLowerCase();

  let filtered = allLessons.filter(lesson => {
    const matchesSearch =
      lesson.title.toLowerCase().includes(searchTerm) ||
      lesson.description.toLowerCase().includes(searchTerm);

    const matchesSubject = !subjectFilter || lesson.subject === subjectFilter;
    const matchesDifficulty = !difficultyFilter || lesson.difficulty.toLowerCase() === difficultyFilter;
    const matchesPath = activePathLessonIds.size === 0 || activePathLessonIds.has(String(lesson.id));

    return matchesSearch && matchesSubject && matchesDifficulty && matchesPath;
  });

  renderCourses(filtered);
}

function clearFilters() {
  document.getElementById('searchInput').value = '';
  document.getElementById('subjectFilter').value = '';
  document.getElementById('difficultyFilter').value = '';
  renderCourses(allLessons);
}

// Load lessons on page load
document.addEventListener('DOMContentLoaded', loadLessons);
