// Tab switching
function switchTab(tabName) {
  const tabs = document.querySelectorAll('.tab-content');
  tabs.forEach(tab => {
    tab.classList.remove('active');
  });
  
  const activeTab = document.getElementById(`${tabName}-tab`);
  if (activeTab) {
    activeTab.classList.add('active');
  }
}

// Worksheet Generator
document.getElementById('worksheetForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const subject = document.getElementById('subject').value;
  const difficulty = document.getElementById('difficulty').value;
  const topic = document.getElementById('topic').value;
  const numQuestions = document.getElementById('numQuestions').value;
  const questionType = document.getElementById('questionType').value;

  // Show loading state
  document.getElementById('loadingState').style.display = 'block';
  document.getElementById('outputArea').style.display = 'none';
  document.getElementById('errorState').style.display = 'none';

  try {
    const response = await fetch('/api/generate-worksheet', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        subject,
        difficulty,
        topic,
        numQuestions: parseInt(numQuestions),
        questionType
      })
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();

    if (data.success) {
      document.getElementById('worksheetContent').innerHTML = data.worksheet;
      document.getElementById('outputArea').style.display = 'block';
      document.getElementById('loadingState').style.display = 'none';
      
      // Store worksheet for download
      window.currentWorksheet = {
        subject,
        difficulty,
        topic,
        content: data.worksheet
      };
    } else {
      throw new Error(data.error || 'Failed to generate worksheet');
    }
  } catch (error) {
    document.getElementById('loadingState').style.display = 'none';
    document.getElementById('errorState').style.display = 'block';
    document.getElementById('errorMessage').textContent = error.message;
  }
});

// File upload handling
const fileInput = document.getElementById('contentFile');
const fileUploadWrapper = document.querySelector('.file-upload-wrapper');
const fileInfo = document.getElementById('fileInfo');

// Drag and drop
fileUploadWrapper.addEventListener('dragover', (e) => {
  e.preventDefault();
  fileUploadWrapper.style.borderColor = 'var(--primary)';
  fileUploadWrapper.style.backgroundColor = 'var(--primary-light)';
});

fileUploadWrapper.addEventListener('dragleave', () => {
  fileUploadWrapper.style.borderColor = 'var(--border)';
  fileUploadWrapper.style.backgroundColor = 'transparent';
});

fileUploadWrapper.addEventListener('drop', (e) => {
  e.preventDefault();
  fileUploadWrapper.style.borderColor = 'var(--border)';
  fileUploadWrapper.style.backgroundColor = 'transparent';
  
  const files = e.dataTransfer.files;
  if (files.length > 0) {
    fileInput.files = files;
    updateFileInfo(files[0]);
  }
});

// Click to upload
fileUploadWrapper.addEventListener('click', () => {
  fileInput.click();
});

fileInput.addEventListener('change', (e) => {
  if (e.target.files.length > 0) {
    updateFileInfo(e.target.files[0]);
  }
});

function updateFileInfo(file) {
  const validTypes = ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 
                      'application/msword', 'text/plain'];
  
  if (!validTypes.includes(file.type)) {
    fileInfo.innerHTML = '❌ Invalid file type. Please upload PDF, DOCX, or TXT.';
    fileInfo.style.color = 'var(--error)';
    fileInput.value = '';
    return;
  }
  
  fileInfo.innerHTML = `✅ ${file.name} (${(file.size / 1024).toFixed(2)} KB)`;
  fileInfo.style.color = 'var(--success)';
}

// Performance calculation
document.getElementById('analysisType').addEventListener('change', (e) => {
  const performanceSection = document.getElementById('performanceSection');
  if (e.target.value === 'assessment') {
    performanceSection.style.display = 'block';
  } else {
    performanceSection.style.display = 'none';
  }
});

document.getElementById('questionsAnswered').addEventListener('input', calculateScore);
document.getElementById('totalQuestions').addEventListener('input', calculateScore);

function calculateScore() {
  const answered = parseInt(document.getElementById('questionsAnswered').value) || 0;
  const total = parseInt(document.getElementById('totalQuestions').value) || 1;
  
  if (total > 0) {
    const percentage = Math.round((answered / total) * 100);
    document.getElementById('scoreDisplay').textContent = `${percentage}% (${answered}/${total})`;
  }
}

// Content Analyzer
document.getElementById('analyzerForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const analysisType = document.getElementById('analysisType').value;
  const analysisLevel = document.getElementById('analysisLevel').value;
  const contentFile = document.getElementById('contentFile').files[0];
  const contentText = document.getElementById('contentInput').value;

  let contentToAnalyze = contentText;
  let fileName = null;

  // If file is selected, we need to handle it differently
  if (contentFile) {
    // Show loading state
    document.getElementById('analyzerLoadingState').style.display = 'block';
    document.getElementById('analyzerOutputArea').style.display = 'none';
    document.getElementById('analyzerErrorState').style.display = 'none';

    try {
      // Create FormData for file upload
      const formData = new FormData();
      formData.append('file', contentFile);
      formData.append('analysisType', analysisType);
      formData.append('detailLevel', analysisLevel);
      
      // Add performance data if assessment
      if (analysisType === 'assessment') {
        const answered = document.getElementById('questionsAnswered').value;
        const total = document.getElementById('totalQuestions').value;
        if (answered && total) {
          formData.append('questionsAnswered', parseInt(answered));
          formData.append('totalQuestions', parseInt(total));
        }
      }

      const response = await fetch('/api/analyze-content', {
        method: 'POST',
        body: formData
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();

      if (data.success) {
        const analysisContent = document.getElementById('analysisContent');
        analysisContent.innerHTML = formatAnalysisOutput(data.analysis);
        document.getElementById('analyzerOutputArea').style.display = 'block';
        document.getElementById('analyzerLoadingState').style.display = 'none';
        
        // Store analysis for copying
        window.currentAnalysis = data.analysis;
      } else {
        throw new Error(data.error || 'Failed to analyze content');
      }
    } catch (error) {
      document.getElementById('analyzerLoadingState').style.display = 'none';
      document.getElementById('analyzerErrorState').style.display = 'block';
      document.getElementById('analyzerErrorMessage').textContent = error.message;
    }
  } else if (contentToAnalyze) {
    // Text content analysis (original flow)
    document.getElementById('analyzerLoadingState').style.display = 'block';
    document.getElementById('analyzerOutputArea').style.display = 'none';
    document.getElementById('analyzerErrorState').style.display = 'none';

    try {
      const requestBody = {
        analysisType,
        content: contentToAnalyze,
        detailLevel: analysisLevel
      };

      // Add performance data if assessment
      if (analysisType === 'assessment') {
        const answered = document.getElementById('questionsAnswered').value;
        const total = document.getElementById('totalQuestions').value;
        if (answered && total) {
          requestBody.questionsAnswered = parseInt(answered);
          requestBody.totalQuestions = parseInt(total);
        }
      }

      const response = await fetch('/api/analyze-content', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();

      if (data.success) {
        const analysisContent = document.getElementById('analysisContent');
        analysisContent.innerHTML = formatAnalysisOutput(data.analysis);
        document.getElementById('analyzerOutputArea').style.display = 'block';
        document.getElementById('analyzerLoadingState').style.display = 'none';
        
        // Store analysis for copying
        window.currentAnalysis = data.analysis;
      } else {
        throw new Error(data.error || 'Failed to analyze content');
      }
    } catch (error) {
      document.getElementById('analyzerLoadingState').style.display = 'none';
      document.getElementById('analyzerErrorState').style.display = 'block';
      document.getElementById('analyzerErrorMessage').textContent = error.message;
    }
  } else {
    alert('Please either upload a file or paste content to analyze.');
  }
});

// Format analysis output to readable HTML
function formatAnalysisOutput(text) {
  // Basic formatting for analysis output
  let html = text
    .replace(/##\s(.+)/g, '<h3 style="color: var(--primary); margin-top: 1.5rem; margin-bottom: 1rem;">$1</h3>')
    .replace(/###\s(.+)/g, '<h4 style="color: var(--text-primary); margin-top: 1rem; margin-bottom: 0.5rem;">$1</h4>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\n\n+/g, '</p><p>')
    .replace(/\n/g, '<br>');
  
  return `<p>${html}</p>`;
}

// Download worksheet as HTML file
function downloadWorksheet() {
  if (!window.currentWorksheet) return;

  const { subject, difficulty, topic, content } = window.currentWorksheet;
  
  const htmlContent = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>${subject} Worksheet - ${difficulty}</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
    h1 { color: #1f5cf0; border-bottom: 3px solid #1f5cf0; padding-bottom: 10px; }
    h2 { color: #333; margin-top: 20px; }
    .header { background: #f0f5ff; padding: 15px; border-radius: 8px; margin-bottom: 20px; }
    .question { margin: 20px 0; padding: 15px; background: #f9f9f9; border-left: 4px solid #1f5cf0; }
    .footer { margin-top: 40px; text-align: center; color: #666; font-size: 12px; }
  </style>
</head>
<body>
  <div class="header">
    <h1>${subject} Worksheet</h1>
    <p><strong>Difficulty Level:</strong> ${difficulty}</p>
    ${topic ? `<p><strong>Topic:</strong> ${topic}</p>` : ''}
    <p><strong>Generated:</strong> ${new Date().toLocaleDateString()}</p>
  </div>
  
  ${content}
  
  <div class="footer">
    <p>Generated by SmartEDU AI Worksheet Generator</p>
  </div>
</body>
</html>
  `;

  const blob = new Blob([htmlContent], { type: 'text/html' });
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `${subject}-${difficulty}-worksheet-${Date.now()}.html`;
  document.body.appendChild(a);
  a.click();
  window.URL.revokeObjectURL(url);
  document.body.removeChild(a);
}

// Copy analysis to clipboard
function copyAnalysis() {
  if (!window.currentAnalysis) return;

  const text = window.currentAnalysis;
  navigator.clipboard.writeText(text).then(() => {
    // Show success message
    const button = event.target;
    const originalText = button.textContent;
    button.textContent = '✅ Copied!';
    setTimeout(() => {
      button.textContent = originalText;
    }, 2000);
  }).catch(err => {
    alert('Failed to copy: ' + err.message);
  });
}
