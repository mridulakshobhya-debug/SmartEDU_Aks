(function () {
  const STORAGE_VERSION = 1;
  const KEY_PREFIX = 'smartedu_progress';

  function safeParse(value, fallback) {
    try {
      return JSON.parse(value);
    } catch (err) {
      return fallback;
    }
  }

  function getCurrentUser() {
    const stored = safeParse(localStorage.getItem('currentUser'), null);
    if (!stored || !stored.id) {
      return {
        id: 'guest',
        full_name: 'Guest Learner',
        username: 'guest'
      };
    }
    return {
      id: stored.id,
      full_name: stored.full_name || stored.username || 'SmartEDU LMS Learner',
      username: stored.username || 'learner',
      email: stored.email || ''
    };
  }

  function getStorageKey() {
    const user = getCurrentUser();
    return `${KEY_PREFIX}_${user.id}`;
  }

  function normalizeData(data) {
    const normalized = data && typeof data === 'object' ? data : {};
    normalized.version = normalized.version || STORAGE_VERSION;
    normalized.completedLessons = normalized.completedLessons || {};
    normalized.quizScores = normalized.quizScores || {};
    normalized.projectSubmissions = normalized.projectSubmissions || {};
    normalized.certificates = Array.isArray(normalized.certificates) ? normalized.certificates : [];
    normalized.badges = Array.isArray(normalized.badges) ? normalized.badges : [];
    return normalized;
  }

  function load() {
    const stored = localStorage.getItem(getStorageKey());
    return normalizeData(safeParse(stored, {}));
  }

  function save(data) {
    const normalized = normalizeData(data);
    localStorage.setItem(getStorageKey(), JSON.stringify(normalized));
    return normalized;
  }

  function isLessonCompleted(lessonId, data) {
    const progress = data || load();
    return Boolean(progress.completedLessons[String(lessonId)]);
  }

  function completeLesson(lesson, data) {
    const progress = data || load();
    const id = String(lesson.id);
    if (!progress.completedLessons[id]) {
      progress.completedLessons[id] = {
        completedAt: new Date().toISOString(),
        title: lesson.title || 'Lesson',
        subject: lesson.subject || 'General',
        duration_minutes: lesson.duration_minutes || 0
      };
    }
    return save(progress);
  }

  function removeLessonCompletion(lessonId, data) {
    const progress = data || load();
    delete progress.completedLessons[String(lessonId)];
    return save(progress);
  }

  function setQuizScore(lessonId, score, correct, total, data) {
    const progress = data || load();
    const id = String(lessonId);
    const existing = progress.quizScores[id];
    if (!existing || score > existing.score) {
      progress.quizScores[id] = {
        score: score,
        correct: correct,
        total: total,
        takenAt: new Date().toISOString()
      };
    }
    return save(progress);
  }

  function getQuizScore(lessonId, data) {
    const progress = data || load();
    return progress.quizScores[String(lessonId)] || null;
  }

  function saveProjectSubmission(projectId, payload, data) {
    const progress = data || load();
    const id = String(projectId);
    progress.projectSubmissions[id] = {
      id: id,
      title: payload.title || '',
      lessonId: payload.lessonId || '',
      status: payload.status || 'draft',
      notes: payload.notes || '',
      repo: payload.repo || '',
      feedback: payload.feedback || '',
      updatedAt: new Date().toISOString()
    };
    return save(progress);
  }

  function getProjectSubmission(projectId, data) {
    const progress = data || load();
    return progress.projectSubmissions[String(projectId)] || null;
  }

  function awardBadge(badge, data) {
    const progress = data || load();
    const exists = progress.badges.some(item => item.id === badge.id);
    if (!exists) {
      progress.badges.push({
        id: badge.id,
        title: badge.title,
        description: badge.description || '',
        issuedAt: new Date().toISOString()
      });
    }
    return save(progress);
  }

  function awardCertificate(certificate, data) {
    const progress = data || load();
    const exists = progress.certificates.some(item => item.id === certificate.id);
    if (!exists) {
      progress.certificates.push({
        id: certificate.id,
        type: certificate.type,
        title: certificate.title,
        refId: certificate.refId,
        issuedAt: new Date().toISOString()
      });
    }
    return save(progress);
  }

  function getCertificateByRef(type, refId, data) {
    const progress = data || load();
    return progress.certificates.find(item => item.type === type && item.refId === refId) || null;
  }

  function getStats(lessons, data) {
    const progress = data || load();
    const lessonCount = Array.isArray(lessons) ? lessons.length : 0;
    const completedCount = Object.keys(progress.completedLessons).length;
    const completedMinutes = Object.values(progress.completedLessons)
      .reduce((sum, item) => sum + (item.duration_minutes || 0), 0);
    const percent = lessonCount > 0 ? Math.round((completedCount / lessonCount) * 100) : 0;
    return {
      lessonCount,
      completedCount,
      completedMinutes,
      hours: Math.round((completedMinutes / 60) * 10) / 10,
      percent
    };
  }

  function evaluateBadgesAndCertificates(params) {
    const progress = load();
    const lessons = params && params.lessons ? params.lessons : [];
    const paths = params && params.paths ? params.paths : [];

    if (Object.keys(progress.completedLessons).length >= 1) {
      awardBadge({
        id: 'first-lesson',
        title: 'First Lesson',
        description: 'Completed your first lesson.'
      }, progress);
    }

    if (Object.keys(progress.completedLessons).length >= 5) {
      awardBadge({
        id: 'five-lessons',
        title: 'Momentum Builder',
        description: 'Completed 5 lessons.'
      }, progress);
    }

    const hasHighQuiz = Object.values(progress.quizScores).some(item => item.score >= 90);
    if (hasHighQuiz) {
      awardBadge({
        id: 'quiz-ace',
        title: 'Quiz Ace',
        description: 'Scored 90% or higher on a quiz.'
      }, progress);
    }

    const submittedProjects = Object.values(progress.projectSubmissions)
      .filter(item => item.status === 'submitted');
    if (submittedProjects.length >= 1) {
      awardBadge({
        id: 'first-project',
        title: 'Project Builder',
        description: 'Submitted your first guided project.'
      }, progress);
    }
    if (submittedProjects.length >= 3) {
      awardBadge({
        id: 'project-pro',
        title: 'Project Pro',
        description: 'Submitted three guided projects.'
      }, progress);
    }

    // Course certificates
    lessons.forEach(lesson => {
      const quizScore = getQuizScore(lesson.id, progress);
      const completed = isLessonCompleted(lesson.id, progress);
      if (completed && quizScore && quizScore.score >= 70) {
        awardCertificate({
          id: `course-${lesson.id}`,
          type: 'course',
          title: lesson.title,
          refId: String(lesson.id)
        }, progress);
      }
    });

    // Path certificates
    paths.forEach(path => {
      if (!path.lessonIds || path.lessonIds.length === 0) return;
      const completedCount = path.lessonIds.filter(id => isLessonCompleted(id, progress)).length;
      if (completedCount === path.lessonIds.length) {
        awardCertificate({
          id: `path-${path.id}`,
          type: 'path',
          title: path.title,
          refId: path.id
        }, progress);
        awardBadge({
          id: `path-${path.id}`,
          title: `${path.title} Completer`,
          description: 'Finished an entire learning path.'
        }, progress);
      }
    });

    return load();
  }

  function formatDate(value) {
    try {
      const date = new Date(value);
      return date.toLocaleDateString(undefined, {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });
    } catch (err) {
      return '';
    }
  }

  function buildCertificateHtml(certificate) {
    const user = getCurrentUser();
    const issued = formatDate(certificate.issuedAt || new Date().toISOString());
    const title = certificate.title || 'Achievement';
    const typeLabel = certificate.type === 'path' ? 'Learning Path' : 'Course';

    return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>SmartEDU LMS Certificate</title>
  <style>
    body { font-family: 'Space Grotesk', Arial, sans-serif; background: #f5f7fb; padding: 2rem; color: #1a202c; }
    .certificate { background: white; border: 6px solid #1f5cf0; padding: 3rem; border-radius: 16px; text-align: center; max-width: 900px; margin: 0 auto; }
    .seal { width: 80px; height: 80px; border-radius: 50%; background: #1f5cf0; color: white; display: inline-flex; align-items: center; justify-content: center; font-weight: 700; margin-bottom: 1rem; }
    h1 { margin: 0 0 1rem; font-size: 2.5rem; }
    h2 { margin: 0.5rem 0; font-size: 2rem; }
    .subtitle { color: #4a5568; margin-bottom: 2rem; }
    .footer { margin-top: 2.5rem; display: flex; justify-content: space-between; font-size: 0.95rem; color: #4a5568; }
    .highlight { color: #1f5cf0; font-weight: 700; }
  </style>
</head>
<body>
  <div class="certificate">
    <div class="seal">SE</div>
    <h1>Certificate of Completion</h1>
    <p class="subtitle">This certifies that</p>
    <h2>${user.full_name || user.username}</h2>
    <p class="subtitle">has successfully completed the ${typeLabel}</p>
    <h2 class="highlight">${title}</h2>
    <div class="footer">
      <div>Issued by SmartEDU LMS</div>
      <div>${issued}</div>
    </div>
  </div>
  <script>
    window.onload = () => { window.print(); };
  </script>
</body>
</html>`;
  }

  function openCertificate(certificate) {
    const html = buildCertificateHtml(certificate);
    const win = window.open('', '_blank');
    if (!win) return;
    win.document.open();
    win.document.write(html);
    win.document.close();
  }

  window.ProgressStore = {
    load,
    save,
    getCurrentUser,
    isLessonCompleted,
    completeLesson,
    removeLessonCompletion,
    setQuizScore,
    getQuizScore,
    saveProjectSubmission,
    getProjectSubmission,
    awardBadge,
    awardCertificate,
    getCertificateByRef,
    getStats,
    evaluateBadgesAndCertificates,
    openCertificate
  };
})();
