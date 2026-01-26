// chatbot.js - AI Chatbot Logic
async function ask() {
  const age = document.getElementById('age').value;
  const interest = document.getElementById('interest').value;
  const output = document.getElementById('out');
  
  if (!age || !interest) {
    output.textContent = 'Please fill in both age and interest fields.';
    return;
  }
  
  output.textContent = 'Loading recommendations...';
  
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
    
    output.textContent = typeof data.reply === 'string'
      ? data.reply
      : JSON.stringify(data.reply, null, 2);
      
  } catch (error) {
    console.error('Error:', error);
    output.textContent = 'Error fetching recommendations. Please try again.';
  }
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
