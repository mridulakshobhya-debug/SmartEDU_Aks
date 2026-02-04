// elibrary.js - Book Loading Logic
async function loadBooks() {
  const age = document.getElementById('age').value;
  
  if (!age) {
    alert('Please enter your age');
    return;
  }
  
  try {
    const response = await fetch(`/api/books?age=${age}`);
    const books = await response.json();
    
    const container = document.getElementById('booksContainer');
    
    if (!books || books.length === 0) {
      container.innerHTML = `
        <div class="card text-center" style="grid-column: 1/-1;">
          <p style="color: var(--text-muted);">No books available for your age group.</p>
        </div>
      `;
      return;
    }
    
    container.innerHTML = books.map(book => `
      <div class="card">
        <h3 style="margin-top: 0;">${book.title}</h3>
        <p style="color: var(--text-secondary); margin-bottom: 1rem;"><strong>by</strong> ${book.author}</p>
        <button class="btn btn-outline" onclick="alert('Coming soon!')">Read Book</button>
      </div>
    `).join('');
    
  } catch (error) {
    console.error('Error loading books:', error);
    alert('Failed to load books. Please try again.');
  }
}
