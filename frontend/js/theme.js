// Theme toggle - Light/Dark mode

function initializeTheme() {
  // Check localStorage for saved theme preference
  const savedTheme = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  
  // Use saved theme or system preference
  const theme = savedTheme || (prefersDark ? 'dark' : 'light');
  setTheme(theme);
}

function setTheme(theme) {
  // Set data attribute on html element
  document.documentElement.setAttribute('data-theme', theme);
  
  // Save preference to localStorage
  localStorage.setItem('theme', theme);
  
  // Update icon
  const icon = document.getElementById('themeIcon');
  if (icon) {
    icon.textContent = theme === 'dark' ? '☀️' : '🌙';
  }
}

function toggleTheme() {
  const current = localStorage.getItem('theme') || 'light';
  const newTheme = current === 'dark' ? 'light' : 'dark';
  setTheme(newTheme);
}

// Initialize theme when page loads
document.addEventListener('DOMContentLoaded', initializeTheme);

// Listen for system theme changes
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
  if (!localStorage.getItem('theme')) {
    setTheme(e.matches ? 'dark' : 'light');
  }
});
