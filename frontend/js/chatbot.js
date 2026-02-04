// chatbot.js - AI Chatbot Logic with Table Support
async function ask() {
  const age = document.getElementById('age').value;
  const interest = document.getElementById('interest').value;
  const output = document.getElementById('out');
  
  if (!age || !interest) {
    output.innerHTML = '<p style="color: var(--error);">Please fill in both age and interest fields.</p>';
    return;
  }
  
  output.innerHTML = '<div class="loading">Loading recommendations</div>';
  
  try {
    const response = await fetch('/api/chatbot', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        age: parseInt(age),
        interest: interest
      })
    });
    
    const data = await response.json();
    
    // Render the response, supporting HTML tables
    if (data.reply) {
      output.innerHTML = formatResponse(data.reply);
    } else {
      output.innerHTML = '<p>No recommendations found. Please try again.</p>';
    }
      
  } catch (error) {
    console.error('Error:', error);
    output.innerHTML = '<p style="color: var(--error);">Error fetching recommendations. Please try again.</p>';
  }
}

// Format response, supporting HTML tables
function formatResponse(reply) {
  // If reply contains HTML table markers, render as HTML
  if (typeof reply === 'string' && reply.includes('<table')) {
    return reply;
  }
  
  // Otherwise, escape and wrap in paragraph
  if (typeof reply === 'string') {
    return `<p>${escapeHtml(reply).replace(/\n\n/g, '</p><p>').replace(/\n/g, '<br>')}</p>`;
  }
  
  return `<pre>${JSON.stringify(reply, null, 2)}</pre>`;
}

// Escape HTML special characters
function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

// Allow Enter key to trigger recommendations
document.addEventListener('DOMContentLoaded', () => {
  const interestInput = document.getElementById('interest');
  if (interestInput) {
    interestInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') ask();
    });
  }
});
