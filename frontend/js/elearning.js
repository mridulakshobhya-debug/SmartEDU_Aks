// elearning.js - Course Grid with Search and Filters

let allLessons = [];

async function loadLessons() {
  try {
    const response = await fetch('/api/lessons');
    const data = await response.json();
    allLessons = data.data || data;
    
    console.log('Loaded lessons:', allLessons);
    console.log('Total lessons:', allLessons.length);
    
    const container = document.getElementById('lessonsContainer');
    
    if (!allLessons || allLessons.length === 0) {
      container.innerHTML = `
        <div class="card text-center" style="grid-column: 1/-1;">
          <p style="color: var(--text-muted);">No lessons available yet.</p>
        </div>
      `;
      return;
    }
    
    renderCourses(allLessons);
    
  } catch (error) {
    console.error('Error loading lessons:', error);
    alert('Failed to load lessons. Please try again.');
  }
}

function renderCourses(lessons) {
  const container = document.getElementById('lessonsContainer');
  
  if (!lessons || lessons.length === 0) {
    container.innerHTML = `
      <div class="card text-center" style="grid-column: 1/-1;">
        <p style="color: var(--text-muted);">No courses match your search or filters.</p>
      </div>
    `;
    document.getElementById('resultsCount').textContent = 'No courses found';
    return;
  }
  
  // Update results counter
  document.getElementById('resultsCount').textContent = `Showing ${lessons.length} course${lessons.length !== 1 ? 's' : ''}`;
  
  // Group by subject
  const bySubject = lessons.reduce((acc, lesson) => {
    if (!acc[lesson.subject]) acc[lesson.subject] = [];
    acc[lesson.subject].push(lesson);
    return acc;
  }, {});
  
  console.log('Grouped by subject:', bySubject);
  console.log('Subject groups:', Object.keys(bySubject));
  
  const getDifficultyColor = (diff) => {
    const colors = {
      'beginner': '#10b981',
      'intermediate': '#f59e0b',
      'advanced': '#ef4444'
    };
    return colors[diff.toLowerCase()] || '#1f5cf0';
  };
  
  let html = '';
  Object.entries(bySubject).forEach(([subject, subjectLessons]) => {
    html += `<div style="grid-column: 1/-1; margin-top: 2rem;">
      <h3 style="color: var(--text-primary); margin-bottom: 1.5rem; border-bottom: 2px solid var(--primary); padding-bottom: 0.5rem;">${subject}</h3>
      <div class="grid grid-3">`;
    
    subjectLessons.forEach(lesson => {
      html += `
        <div class="card lesson-card" onclick="window.location.href='course.html?id=${lesson.id}'" style="cursor: pointer;">
          <div style="margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: start;">
            <span class="badge" style="background: ${getDifficultyColor(lesson.difficulty)}; color: white; padding: 0.35rem 0.75rem; border-radius: 999px; font-size: 0.75rem; font-weight: 600; text-transform: capitalize;">
              ${lesson.difficulty}
            </span>
            <span style="font-size: 0.75rem; color: var(--text-muted);">⏱ ${lesson.duration_minutes}m</span>
          </div>
          <h4 style="margin: 0.5rem 0 0.75rem 0; color: var(--text-primary); line-height: 1.4; min-height: 3rem;">${lesson.title}</h4>
          <p style="font-size: 0.875rem; color: var(--text-secondary); margin: 0.75rem 0; flex-grow: 1;">${lesson.description}</p>
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
    
    return matchesSearch && matchesSubject && matchesDifficulty;
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
