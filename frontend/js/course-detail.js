// course-detail.js - Full page course viewer with progress tracking

let currentLesson = null;
let currentQuiz = [];
let currentProject = null;

async function loadCourseDetail() {
  try {
    const params = new URLSearchParams(window.location.search);
    const courseId = params.get('id');

    if (!courseId) {
      window.location.href = 'elearning.html';
      return;
    }

    const response = await fetch(`/api/lessons/${courseId}`);
    const data = await response.json();
    const lesson = data.data;

    if (!lesson) {
      document.getElementById('courseHeader').innerHTML = '<p>Course not found</p>';
      return;
    }

    currentLesson = lesson;

    const requestedProjectId = params.get('project');
    currentProject = getProjectForLesson(lesson, requestedProjectId);

    const colors = {
      beginner: '#3b82f6',
      intermediate: '#2563eb',
      advanced: '#1e40af'
    };
    const diffColor = colors[lesson.difficulty] || '#2563eb';

    const progress = ProgressStore.load();
    const isCompleted = ProgressStore.isLessonCompleted(lesson.id, progress);
    const quizScore = ProgressStore.getQuizScore(lesson.id, progress);
    const masteryScore = quizScore ? quizScore.score : 0;

    const statusText = isCompleted ? 'Completed' : 'Not completed';
    const statusClass = isCompleted ? 'complete' : 'locked';

    document.getElementById('courseHeader').innerHTML = `
      <div style="background: linear-gradient(135deg, ${diffColor}15 0%, ${diffColor}05 100%); padding: 2rem; border-radius: 12px; border: 2px solid ${diffColor};">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem; gap: 1.5rem; flex-wrap: wrap;">
          <div style="flex: 1; min-width: 260px;">
            <span style="background: ${diffColor}; color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.85rem; font-weight: 700; text-transform: capitalize; display: inline-block; margin-bottom: 1rem;">${lesson.difficulty}</span>
            <h1 style="margin: 0; color: var(--text-primary); font-size: 2.5rem;">${lesson.title}</h1>
            <p style="margin: 0.75rem 0 0 0; color: var(--text-secondary); font-size: 1.1rem;">${lesson.description}</p>
            <div style="margin-top: 1rem; display: flex; gap: 0.75rem; flex-wrap: wrap;">
              <span id="courseStatusChip" class="status-chip ${statusClass}">${statusText}</span>
              <span id="courseMasteryChip" class="status-chip in-progress">Mastery ${masteryScore}%</span>
            </div>
          </div>
          <div style="text-align: right; min-width: 160px;">
            <p style="margin: 0; color: var(--text-secondary); font-size: 1rem;">Time: ${lesson.duration_minutes} minutes</p>
            <p style="margin: 0.5rem 0 0 0; color: var(--text-muted); font-size: 0.9rem;">Subject: ${lesson.subject}</p>
          </div>
        </div>
      </div>
    `;

    let contentHtml = '';

    contentHtml += `
      <div style="grid-column: 1/-1;">
        <h2 style="color: var(--text-primary); margin-bottom: 1.5rem; font-size: 1.8rem;">Lesson Video</h2>
        <div style="background: var(--bg-secondary); border-radius: 12px; overflow: hidden; aspect-ratio: 16/9; display: flex; align-items: center; justify-content: center; box-shadow: 0 8px 24px rgba(0,0,0,0.1);">
          ${lesson.video_url ? `
            <iframe
              width="100%"
              height="100%"
              src="${lesson.video_url.replace(/watch\?v=/, 'embed/')}"
              title="Lesson Video"
              frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
              referrerpolicy="strict-origin-when-cross-origin"
              allowfullscreen>
            </iframe>
          ` : `
            <div style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; background: var(--bg-tertiary);">
              <p style="color: var(--text-muted); font-size: 1.1rem;">No video available for this lesson</p>
            </div>
          `}
        </div>
      </div>
    `;

    if (lesson.content) {
      let processedContent = lesson.content
        .replace(/```python\n([\s\S]*?)\n```/g, '<pre style="background: var(--bg-tertiary); padding: 1rem; border-radius: 8px; overflow-x: auto; margin: 1rem 0;"><code style="font-family: monospace; color: var(--text-primary); font-size: 0.9rem;">$1</code></pre>')
        .replace(/```([\s\S]*?)```/g, '<pre style="background: var(--bg-tertiary); padding: 1rem; border-radius: 8px; overflow-x: auto; margin: 1rem 0;"><code style="font-family: monospace; color: var(--text-primary); font-size: 0.9rem;">$1</code></pre>')
        .replace(/^### (.*?)$/gm, '<h4 style="color: var(--text-secondary); margin-top: 1rem; margin-bottom: 0.5rem; font-size: 1.2rem;">$1</h4>')
        .replace(/^## (.*?)$/gm, '<h3 style="color: var(--text-secondary); margin-top: 1.5rem; margin-bottom: 0.75rem; font-size: 1.4rem;">$1</h3>')
        .replace(/^# (.*?)$/gm, '<h2 style="color: var(--text-primary); margin-top: 2rem; margin-bottom: 1rem; font-size: 1.6rem;">$1</h2>')
        .replace(/\*\*(.*?)\*\*/g, '<strong style="font-weight: 700; color: var(--text-primary);">$1</strong>')
        .replace(/^\* (.*?)$/gm, '<li style="margin-left: 2rem; margin-top: 0.5rem;">$1</li>')
        .replace(/^\- (.*?)$/gm, '<li style="margin-left: 2rem; margin-top: 0.5rem;">$1</li>')
        .split('\n\n')
        .map(para => {
          if (para.includes('<h') || para.includes('<pre') || para.includes('<li')) {
            return para;
          }
          return para.trim() ? '<p style="margin: 1rem 0; color: var(--text-secondary); line-height: 1.7;">' + para + '</p>' : '';
        })
        .join('');

      contentHtml += `
        <div style="grid-column: 1/-1; background: var(--bg-secondary); padding: 2rem; border-radius: 12px; border-left: 5px solid ${diffColor}; font-size: 1.05rem; line-height: 1.8;">
          <div style="color: var(--text-primary);">
            ${processedContent}
          </div>
        </div>
      `;
    }

    if (lesson.information) {
      let infoHtml = '';
      if (typeof lesson.information === 'string') {
        try {
          const infoArray = JSON.parse(lesson.information);
          infoHtml = Array.isArray(infoArray)
            ? infoArray.map(info => `<p style="margin: 0.75rem 0; color: var(--text-secondary);">- ${info}</p>`).join('')
            : lesson.information;
        } catch (e) {
          infoHtml = `<p style="margin: 0; color: var(--text-secondary); line-height: 1.7;">${lesson.information}</p>`;
        }
      } else if (Array.isArray(lesson.information)) {
        infoHtml = lesson.information.map(info => `<p style="margin: 0.75rem 0; color: var(--text-secondary);">- ${info}</p>`).join('');
      }

      contentHtml += `
        <div style="grid-column: 1/-1; background: var(--bg-secondary); padding: 2rem; border-radius: 12px; border-left: 5px solid ${diffColor};">
          <h2 style="color: var(--text-primary); margin-top: 0; margin-bottom: 1rem; font-size: 1.5rem;">Key Information</h2>
          <div style="color: var(--text-secondary);">
            ${infoHtml}
          </div>
        </div>
      `;
    }

    let stepsData = lesson.steps;
    if (typeof stepsData === 'string') {
      try {
        stepsData = JSON.parse(stepsData);
      } catch (e) {
        stepsData = [];
      }
    }

    if (stepsData && stepsData.length > 0) {
      contentHtml += `
        <div style="grid-column: 1/-1;">
          <h2 style="color: var(--text-primary); margin-bottom: 1.5rem; font-size: 1.8rem;">Learning Steps</h2>
          <div style="display: grid; gap: 1rem;">
      `;

      stepsData.forEach((step, idx) => {
        contentHtml += `
          <div style="display: flex; gap: 1.5rem; padding: 1.5rem; background: var(--bg-secondary); border-radius: 8px; align-items: flex-start; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <div style="background: ${diffColor}; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.1rem; flex-shrink: 0;">${idx + 1}</div>
            <p style="color: var(--text-primary); margin: 0; line-height: 1.7; font-size: 1.05rem;">${step}</p>
          </div>
        `;
      });

      contentHtml += `
          </div>
        </div>
      `;
    }

    let quizData = lesson.quiz;
    if (typeof quizData === 'string') {
      try {
        quizData = JSON.parse(quizData);
      } catch (e) {
        quizData = [];
      }
    }

    currentQuiz = Array.isArray(quizData) ? quizData : [];

    if (currentQuiz.length > 0) {
      contentHtml += `
        <div style="grid-column: 1/-1; background: var(--primary-light); padding: 2rem; border-radius: 12px;">
          <h2 style="color: var(--text-primary); margin-top: 0; margin-bottom: 2rem; font-size: 1.8rem;">Knowledge Check Quiz</h2>
          <div id="quizContainer" style="display: flex; flex-direction: column; gap: 2rem;">
      `;

      currentQuiz.forEach((q, idx) => {
        contentHtml += `
          <div data-quiz-question="${idx}" style="background: var(--bg-primary); padding: 1.5rem; border-radius: 8px; border-left: 4px solid ${diffColor};">
            <p style="color: var(--text-primary); font-weight: 700; margin: 0 0 1.25rem 0; font-size: 1.1rem;">Q${idx + 1}: ${q.question}</p>
            <div style="display: flex; flex-direction: column; gap: 0.75rem;">
        `;

        (q.options || []).forEach((opt, optIdx) => {
          contentHtml += `
            <label class="quiz-option">
              <input type="radio" name="q${idx}" value="${optIdx}" style="cursor: pointer; width: 20px; height: 20px; accent-color: ${diffColor};" />
              <span style="color: var(--text-secondary); font-size: 1rem;">${opt}</span>
            </label>
          `;
        });

        contentHtml += `
            </div>
          </div>
        `;
      });

      contentHtml += `
          </div>
          <button id="quizCheckBtn" style="width: 100%; padding: 1rem; background: var(--primary); color: white; border: none; border-radius: 8px; font-weight: 700; cursor: pointer; margin-top: 2rem; font-size: 1.05rem;">Check Answers</button>
          <div id="quizResult" class="quiz-result" style="display: none;"></div>
        </div>
      `;
    }

    if (currentProject) {
      contentHtml += buildProjectSection(currentProject, diffColor);
    }

    contentHtml += `
      <div class="course-progress-card" id="courseProgressCard" style="grid-column: 1/-1;">
        <h3 style="margin-top: 0;">Your Progress</h3>
        <div class="progress-bar">
          <div class="progress-bar-fill" id="courseProgressFill" style="width: ${isCompleted ? 100 : 0}%;"></div>
        </div>
        <div id="courseProgressSummary" style="margin-top: 0.75rem; color: var(--text-secondary);">
          ${isCompleted ? 'Lesson completed. Great work!' : 'Mark this lesson complete when you finish.'}
        </div>
        <div style="display: flex; gap: 1rem; margin-top: 1.25rem; flex-wrap: wrap;">
          <button id="toggleCompleteBtn" class="btn btn-primary" style="flex: 1; min-width: 180px;">${isCompleted ? 'Mark as Incomplete' : 'Mark Lesson Complete'}</button>
          <button id="certificateBtn" class="btn btn-secondary" style="flex: 1; min-width: 180px; display: none;">View Certificate</button>
          <a href="elearning.html" class="btn btn-secondary" style="flex: 1; min-width: 180px; text-align: center;">Browse More Courses</a>
        </div>
      </div>
    `;

    document.getElementById('courseContent').innerHTML = contentHtml;

    const checkBtn = document.getElementById('quizCheckBtn');
    if (checkBtn) {
      checkBtn.addEventListener('click', () => checkQuiz(currentQuiz, lesson.id));
    }

    const completeBtn = document.getElementById('toggleCompleteBtn');
    if (completeBtn) {
      completeBtn.addEventListener('click', () => toggleCompletion(lesson));
    }

    if (currentProject) {
      initProjectForm(currentProject);
    }

    updateCertificateButton(lesson);
  } catch (error) {
    console.error('Error:', error);
    document.getElementById('courseHeader').innerHTML = '<p style="color: var(--error);">Error loading course</p>';
  }
}

function getCorrectIndex(question) {
  if (typeof question.correct !== 'undefined') return question.correct;
  if (typeof question.answer !== 'undefined') return question.answer;
  return -1;
}

function checkQuiz(quizData, lessonId) {
  if (!quizData || quizData.length === 0) return;

  let correct = 0;
  quizData.forEach((q, idx) => {
    const questionEl = document.querySelector(`[data-quiz-question="${idx}"]`);
    if (!questionEl) return;

    const options = questionEl.querySelectorAll('.quiz-option');
    options.forEach(option => option.classList.remove('correct', 'incorrect'));

    const selected = questionEl.querySelector(`input[name="q${idx}"]:checked`);
    const correctIndex = getCorrectIndex(q);

    if (selected) {
      const selectedIndex = parseInt(selected.value, 10);
      if (selectedIndex === correctIndex) {
        correct += 1;
        options[selectedIndex].classList.add('correct');
      } else {
        options[selectedIndex].classList.add('incorrect');
        if (options[correctIndex]) {
          options[correctIndex].classList.add('correct');
        }
      }
    } else if (options[correctIndex]) {
      options[correctIndex].classList.add('correct');
    }
  });

  const percentage = Math.round((correct / quizData.length) * 100);
  ProgressStore.setQuizScore(lessonId, percentage, correct, quizData.length);
  ProgressStore.evaluateBadgesAndCertificates({ lessons: [currentLesson], paths: [] });

  const resultEl = document.getElementById('quizResult');
  if (resultEl) {
    resultEl.style.display = 'block';
    resultEl.innerHTML = `
      <strong>Quiz Result:</strong> ${percentage}% (${correct}/${quizData.length} correct)
      <div style="margin-top: 0.5rem;">Review the highlighted answers and try again anytime.</div>
    `;
  }

  const masteryChip = document.getElementById('courseMasteryChip');
  if (masteryChip) {
    masteryChip.textContent = `Mastery ${percentage}%`;
  }

  updateCertificateButton(currentLesson);
}

function toggleCompletion(lesson) {
  let progress = ProgressStore.load();
  const completed = ProgressStore.isLessonCompleted(lesson.id, progress);

  if (completed) {
    progress = ProgressStore.removeLessonCompletion(lesson.id, progress);
  } else {
    progress = ProgressStore.completeLesson(lesson, progress);
  }

  ProgressStore.evaluateBadgesAndCertificates({ lessons: [lesson], paths: [] });
  updateProgressUI(lesson);
}

function updateProgressUI(lesson) {
  const progress = ProgressStore.load();
  const completed = ProgressStore.isLessonCompleted(lesson.id, progress);

  const fill = document.getElementById('courseProgressFill');
  const summary = document.getElementById('courseProgressSummary');
  const toggleBtn = document.getElementById('toggleCompleteBtn');
  const statusChip = document.getElementById('courseStatusChip');

  if (fill) fill.style.width = completed ? '100%' : '0%';
  if (summary) summary.textContent = completed ? 'Lesson completed. Great work!' : 'Mark this lesson complete when you finish.';
  if (toggleBtn) toggleBtn.textContent = completed ? 'Mark as Incomplete' : 'Mark Lesson Complete';
  if (statusChip) {
    statusChip.textContent = completed ? 'Completed' : 'Not completed';
    statusChip.classList.toggle('complete', completed);
    statusChip.classList.toggle('locked', !completed);
  }

  updateCertificateButton(lesson);
}

function updateCertificateButton(lesson) {
  if (!lesson) return;
  const certBtn = document.getElementById('certificateBtn');
  const certificate = ProgressStore.getCertificateByRef('course', String(lesson.id));

  if (certBtn && certificate) {
    certBtn.style.display = 'inline-flex';
    certBtn.onclick = () => ProgressStore.openCertificate(certificate);
  } else if (certBtn) {
    certBtn.style.display = 'none';
  }
}

function getProjectForLesson(lesson, requestedProjectId) {
  const projects = Array.isArray(window.GuidedProjects) ? window.GuidedProjects : [];
  if (requestedProjectId) {
    const byId = projects.find(item => item.id === requestedProjectId);
    if (byId) {
      return { ...byId, lessonId: String(lesson.id) };
    }
  }
  const byTitle = projects.find(item => item.lessonTitle === lesson.title);
  if (byTitle) {
    return { ...byTitle, lessonId: String(lesson.id) };
  }
  return null;
}

function buildProjectSection(project, accentColor) {
  const steps = Array.isArray(project.steps) ? project.steps : [];
  const deliverables = Array.isArray(project.deliverables) ? project.deliverables : [];
  const skills = Array.isArray(project.skills) ? project.skills : [];

  const stepsHtml = steps.map(step => `<div class="project-step">- ${step}</div>`).join('');
  const deliverablesHtml = deliverables.map(item => `<div class="project-step">- ${item}</div>`).join('');
  const skillsHtml = skills.map(skill => `<span class="project-tag">${skill}</span>`).join('');

  return `
    <div class="project-workspace">
      <div style="display: flex; justify-content: space-between; gap: 1rem; flex-wrap: wrap; align-items: center;">
        <div>
          <div class="project-level">${project.difficulty}</div>
          <h3 style="margin: 0.5rem 0;">Guided Project: ${project.title}</h3>
          <p style="margin: 0; color: var(--text-secondary);">${project.summary}</p>
        </div>
        <span class="status-chip in-progress" style="border-color: ${accentColor}; color: ${accentColor};">Estimated ${project.duration}</span>
      </div>
      <div class="project-tags">${skillsHtml}</div>
      <div class="project-panels">
        <div class="project-panel">
          <h4 style="margin-top: 0;">Project Steps</h4>
          <div class="project-steps">${stepsHtml}</div>
        </div>
        <div class="project-panel">
          <h4 style="margin-top: 0;">Deliverables</h4>
          <div class="project-steps">${deliverablesHtml}</div>
        </div>
        <div class="project-panel project-submit">
          <h4 style="margin-top: 0;">Submit Your Work</h4>
          <label for="projectSubmission" style="font-size: 0.9rem; color: var(--text-secondary);">Project notes, code snippets, or a short write-up.</label>
          <textarea id="projectSubmission" placeholder="Explain your approach, include code samples, or describe your solution."></textarea>
          <div style="margin-top: 0.75rem;">
            <label for="projectRepo" style="font-size: 0.9rem; color: var(--text-secondary);">Optional link (repo or demo)</label>
            <input id="projectRepo" type="text" placeholder="https://..." />
          </div>
          <div class="project-actions">
            <button id="projectSaveDraftBtn" class="btn btn-secondary">Save Draft</button>
            <button id="projectSubmitBtn" class="btn btn-primary">Submit for Feedback</button>
          </div>
          <div id="projectStatus" class="project-status">Submit your project to receive feedback.</div>
          <div id="projectFeedback" class="project-feedback" style="display: none;"></div>
        </div>
      </div>
    </div>
  `;
}

function initProjectForm(project) {
  const submissionEl = document.getElementById('projectSubmission');
  const repoEl = document.getElementById('projectRepo');
  const statusEl = document.getElementById('projectStatus');
  const feedbackEl = document.getElementById('projectFeedback');
  const draftBtn = document.getElementById('projectSaveDraftBtn');
  const submitBtn = document.getElementById('projectSubmitBtn');

  const stored = ProgressStore.getProjectSubmission(project.id);
  if (stored) {
    if (submissionEl) submissionEl.value = stored.notes || '';
    if (repoEl) repoEl.value = stored.repo || '';
    if (stored.feedback && feedbackEl) {
      feedbackEl.style.display = 'block';
      feedbackEl.textContent = stored.feedback;
    }
    if (statusEl) {
      statusEl.textContent = stored.status === 'submitted'
        ? `Submitted on ${new Date(stored.updatedAt).toLocaleDateString()}. Feedback ready.`
        : `Draft saved on ${new Date(stored.updatedAt).toLocaleDateString()}.`;
      statusEl.classList.toggle('success', stored.status === 'submitted');
    }
  }

  if (draftBtn) {
    draftBtn.addEventListener('click', () => saveProjectDraft(project));
  }

  if (submitBtn) {
    submitBtn.addEventListener('click', () => submitProject(project));
  }
}

function saveProjectDraft(project) {
  const submissionEl = document.getElementById('projectSubmission');
  const repoEl = document.getElementById('projectRepo');
  const notes = submissionEl ? submissionEl.value.trim() : '';
  const repo = repoEl ? repoEl.value.trim() : '';

  if (notes.length < 10) {
    updateProjectStatus('Please add at least 10 characters before saving.', 'error');
    return;
  }

  ProgressStore.saveProjectSubmission(project.id, {
    title: project.title,
    lessonId: project.lessonId,
    status: 'draft',
    notes: notes,
    repo: repo,
    feedback: ''
  });

  updateProjectStatus('Draft saved. Keep iterating before you submit.', 'info');
}

async function submitProject(project) {
  const submissionEl = document.getElementById('projectSubmission');
  const repoEl = document.getElementById('projectRepo');
  const notes = submissionEl ? submissionEl.value.trim() : '';
  const repo = repoEl ? repoEl.value.trim() : '';

  if (notes.length < 20) {
    updateProjectStatus('Please provide a more detailed submission (20+ characters).', 'error');
    return;
  }

  updateProjectStatus('Submitting for feedback...', 'info');

  ProgressStore.saveProjectSubmission(project.id, {
    title: project.title,
    lessonId: project.lessonId,
    status: 'submitted',
    notes: notes,
    repo: repo,
    feedback: ''
  });

  try {
    const response = await fetch('/api/project-feedback', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        projectTitle: project.title,
        difficulty: project.difficulty,
        submission: notes,
        repo: repo
      })
    });

    const data = await response.json();
    if (!response.ok || !data.success) {
      throw new Error(data.error || 'Feedback request failed');
    }

    ProgressStore.saveProjectSubmission(project.id, {
      title: project.title,
      lessonId: project.lessonId,
      status: 'submitted',
      notes: notes,
      repo: repo,
      feedback: data.feedback || 'Feedback generated.'
    });

    ProgressStore.evaluateBadgesAndCertificates({ lessons: [currentLesson], paths: [] });
    renderProjectFeedback(data.feedback || '');
    updateProjectStatus('Feedback ready. Review the notes below.', 'success');
  } catch (error) {
    console.error('Project feedback error:', error);
    updateProjectStatus('Unable to generate feedback right now. Please try again later.', 'error');
  }
}

function updateProjectStatus(message, tone) {
  const statusEl = document.getElementById('projectStatus');
  if (!statusEl) return;
  statusEl.textContent = message;
  statusEl.classList.remove('success', 'error');
  if (tone === 'success') statusEl.classList.add('success');
  if (tone === 'error') statusEl.classList.add('error');
}

function renderProjectFeedback(feedback) {
  const feedbackEl = document.getElementById('projectFeedback');
  if (!feedbackEl) return;
  feedbackEl.style.display = 'block';
  feedbackEl.textContent = feedback || 'Feedback generated.';
}

document.addEventListener('DOMContentLoaded', loadCourseDetail);
