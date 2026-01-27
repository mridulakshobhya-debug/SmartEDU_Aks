// course-detail.js - Full page course viewer

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
    
    console.log('Lesson data:', lesson);
    
    if (!lesson) {
      document.getElementById('courseHeader').innerHTML = '<p>Course not found</p>';
      return;
    }
    
    const colors = {
      'beginner': '#10b981',
      'intermediate': '#f59e0b',
      'advanced': '#ef4444'
    };
    const diffColor = colors[lesson.difficulty] || '#1f5cf0';
    
    // Render header
    document.getElementById('courseHeader').innerHTML = `
      <div style="background: linear-gradient(135deg, ${diffColor}15 0%, ${diffColor}05 100%); padding: 2rem; border-radius: 12px; border: 2px solid ${diffColor};">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
          <div>
            <span style="background: ${diffColor}; color: white; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.85rem; font-weight: 700; text-transform: capitalize; display: inline-block; margin-bottom: 1rem;">${lesson.difficulty}</span>
            <h1 style="margin: 0; color: var(--text-primary); font-size: 2.5rem;">${lesson.title}</h1>
            <p style="margin: 0.75rem 0 0 0; color: var(--text-secondary); font-size: 1.1rem;">${lesson.description}</p>
          </div>
          <div style="text-align: right;">
            <p style="margin: 0; color: var(--text-secondary); font-size: 1rem;">⏱ ${lesson.duration_minutes} minutes</p>
            <p style="margin: 0.5rem 0 0 0; color: var(--text-muted); font-size: 0.9rem;">Subject: ${lesson.subject}</p>
          </div>
        </div>
      </div>
    `;
    
    // Render content
    let contentHtml = '';
    
    // Video section
    contentHtml += `
      <div style="grid-column: 1/-1;">
        <h2 style="color: var(--text-primary); margin-bottom: 1.5rem; font-size: 1.8rem;">📹 Lesson Video</h2>
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
    
    // Main Content section with markdown-like rendering
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
    
    // Information section
    if (lesson.information) {
      let infoHtml = '';
      if (typeof lesson.information === 'string') {
        // If it's a JSON string, try to parse it
        try {
          const infoArray = JSON.parse(lesson.information);
          infoHtml = Array.isArray(infoArray) 
            ? infoArray.map(info => `<p style="margin: 0.75rem 0; color: var(--text-secondary);">✓ ${info}</p>`).join('')
            : lesson.information;
        } catch (e) {
          // If not JSON, treat as plain text
          infoHtml = `<p style="margin: 0; color: var(--text-secondary); line-height: 1.7;">${lesson.information}</p>`;
        }
      } else if (Array.isArray(lesson.information)) {
        infoHtml = lesson.information.map(info => `<p style="margin: 0.75rem 0; color: var(--text-secondary);">✓ ${info}</p>`).join('');
      }
      
      contentHtml += `
        <div style="grid-column: 1/-1; background: var(--bg-secondary); padding: 2rem; border-radius: 12px; border-left: 5px solid ${diffColor};">
          <h2 style="color: var(--text-primary); margin-top: 0; margin-bottom: 1rem; font-size: 1.5rem;">💡 Key Information</h2>
          <div style="color: var(--text-secondary);">
            ${infoHtml}
          </div>
        </div>
      `;
    }
    
    // Learning Steps section
    let stepsData = lesson.steps;
    
    // Parse steps if it's a JSON string
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
          <h2 style="color: var(--text-primary); margin-bottom: 1.5rem; font-size: 1.8rem;">📋 Learning Steps</h2>
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
    
    // Quiz section
    let quizData = lesson.quiz;
    
    // Parse quiz if it's a JSON string
    if (typeof quizData === 'string') {
      try {
        quizData = JSON.parse(quizData);
      } catch (e) {
        quizData = [];
      }
    }
    
    if (quizData && quizData.length > 0) {
      contentHtml += `
        <div style="grid-column: 1/-1; background: var(--primary-light); padding: 2rem; border-radius: 12px;">
          <h2 style="color: var(--text-primary); margin-top: 0; margin-bottom: 2rem; font-size: 1.8rem;">🎯 Knowledge Check Quiz</h2>
          <div id="quizContainer" style="display: flex; flex-direction: column; gap: 2rem;">
      `;
      
      quizData.forEach((q, idx) => {
        contentHtml += `
          <div style="background: var(--bg-primary); padding: 1.5rem; border-radius: 8px; border-left: 4px solid ${diffColor};">
            <p style="color: var(--text-primary); font-weight: 700; margin: 0 0 1.25rem 0; font-size: 1.1rem;">Q${idx + 1}: ${q.question}</p>
            <div style="display: flex; flex-direction: column; gap: 0.75rem;">
        `;
        
        (q.options || []).forEach((opt, optIdx) => {
          contentHtml += `
            <label style="display: flex; align-items: center; cursor: pointer; gap: 1rem; padding: 0.75rem; border-radius: 6px; transition: background 0.2s;">
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
          <button onclick="checkQuiz(${JSON.stringify(quizData).replace(/"/g, '&quot;')})" style="width: 100%; padding: 1rem; background: var(--primary); color: white; border: none; border-radius: 8px; font-weight: 700; cursor: pointer; margin-top: 2rem; font-size: 1.05rem;">Check Answers</button>
        </div>
      `;
    }
    
    // Action buttons
    contentHtml += `
      <div style="grid-column: 1/-1; display: flex; gap: 1rem; margin-top: 2rem;">
        <button class="btn btn-primary" style="flex: 1; padding: 1rem; font-size: 1.05rem;">Start Learning Course</button>
        <a href="elearning.html" class="btn btn-secondary" style="flex: 1; padding: 1rem; font-size: 1.05rem; text-align: center; text-decoration: none;">Browse More Courses</a>
      </div>
    `;
    
    document.getElementById('courseContent').innerHTML = contentHtml;
    
  } catch (error) {
    console.error('Error:', error);
    document.getElementById('courseHeader').innerHTML = '<p style="color: var(--error);">Error loading course</p>';
  }
}

function checkQuiz(quizData) {
  let correct = 0;
  quizData.forEach((q, idx) => {
    const selected = document.querySelector(`input[name="q${idx}"]:checked`);
    if (selected && parseInt(selected.value) === q.correct) {
      correct++;
    }
  });
  
  const percentage = Math.round((correct / quizData.length) * 100);
  const message = percentage >= 80 ? '🎉 Excellent!' : percentage >= 60 ? '👍 Good job!' : '📚 Keep studying!';
  alert(`${message}\n\nYou scored ${percentage}% (${correct}/${quizData.length} correct)\n\nGreat effort! Review the material and try again to improve your score.`);
}

document.addEventListener('DOMContentLoaded', loadCourseDetail);
