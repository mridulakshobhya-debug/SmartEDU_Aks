// main.js - SmartEDU Frontend Core Initialization

console.log('🎓 SmartEDU Application Starting...');

/**
 * Theme Management System
 * Handles light/dark mode switching with local storage persistence
 */
class ThemeManager {
  constructor() {
    this.prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
    this.currentTheme = localStorage.getItem('smartedu_theme') || 
                       (this.prefersDarkMode ? 'dark' : 'light');
    this.init();
  }

  init() {
    this.applyTheme(this.currentTheme);
    this.updateIcon();
    this.setupEventListeners();
    console.log('✅ Theme Manager Initialized - Theme:', this.currentTheme);
  }

  applyTheme(theme) {
    if (theme === 'dark') {
      document.documentElement.setAttribute('data-theme', 'dark');
      localStorage.setItem('smartedu_theme', 'dark');
      this.currentTheme = 'dark';
    } else {
      document.documentElement.removeAttribute('data-theme');
      localStorage.setItem('smartedu_theme', 'light');
      this.currentTheme = 'light';
    }
  }

  toggleTheme() {
    const newTheme = this.currentTheme === 'dark' ? 'light' : 'dark';
    this.applyTheme(newTheme);
    this.updateIcon();
    console.log('🎨 Theme switched to:', newTheme);
  }

  updateIcon() {
    const icon = document.getElementById('themeIcon');
    if (icon) {
      icon.textContent = this.currentTheme === 'dark' ? '☀️' : '🌙';
      // Add smooth rotation animation
      icon.style.transition = 'transform 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
      icon.style.display = 'inline-block';
      icon.style.transform = 'rotate(0deg)';
      
      // Trigger animation
      setTimeout(() => {
        icon.style.transform = 'rotate(180deg)';
      }, 0);
      setTimeout(() => {
        icon.style.transform = 'rotate(360deg)';
      }, 150);
    }
  }

  setupEventListeners() {
    // Watch for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
      if (!localStorage.getItem('smartedu_theme')) {
        this.applyTheme(e.matches ? 'dark' : 'light');
        this.updateIcon();
      }
    });
  }
}

/**
 * Global toggle function (for inline onclick handlers)
 */
function toggleTheme() {
  if (window.themeManager) {
    window.themeManager.toggleTheme();
  }
}

/**
 * Scroll animations for elements
 */
class ScrollAnimator {
  constructor() {
    this.observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    };
    this.observer = new IntersectionObserver((entries) => this.onIntersect(entries), this.observerOptions);
    this.init();
  }

  init() {
    document.addEventListener('DOMContentLoaded', () => {
      document.querySelectorAll('.card').forEach(card => {
        card.style.opacity = '0';
        this.observer.observe(card);
      });
    });
  }

  onIntersect(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animation = 'fadeInUp 0.6s ease-out forwards';
        this.observer.unobserve(entry.target);
      }
    });
  }
}

/**
 * Smooth scroll for anchor links
 */
function setupSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
}

/**
 * Initialize all systems when DOM is ready
 */
document.addEventListener('DOMContentLoaded', () => {
  // Initialize theme manager
  window.themeManager = new ThemeManager();
  
  // Initialize scroll animator
  new ScrollAnimator();
  
  // Setup smooth scrolling
  setupSmoothScroll();
  
  console.log('✅ SmartEDU Frontend Fully Initialized');
  console.log('💡 Tip: Press the theme toggle (🌙/☀️) in the header to switch themes');
});

/**
 * Performance monitoring (optional)
 */
if (window.performance && window.performance.timing) {
  window.addEventListener('load', () => {
    const perfData = window.performance.timing;
    const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
    console.log('📊 Page Load Time:', pageLoadTime + 'ms');
  });
}
