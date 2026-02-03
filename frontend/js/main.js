// main.js - SmartEDU LMS Frontend Core Initialization

console.log('🎓 SmartEDU LMS Application Starting...');

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
 * Community gallery slider with progress bar
 */
function initGallerySlider() {
  const track = document.getElementById('galleryTrack');
  const progress = document.getElementById('galleryProgress');
  const shell = document.querySelector('.slideshow-shell');
  if (!track || !progress || !shell) return;

  const updateProgress = () => {
    const maxScroll = track.scrollWidth - track.clientWidth;
    const percent = maxScroll > 0 ? (track.scrollLeft / maxScroll) * 100 : 0;
    progress.style.width = `${percent}%`;
  };

  const step = () => track.clientWidth * 0.85;

  const scrollByStep = (dir) => {
    const maxScroll = track.scrollWidth - track.clientWidth;
    if (maxScroll <= 0) return;
    let next = track.scrollLeft + (dir * step());
    if (next < 0) next = 0;
    if (next > maxScroll) next = maxScroll;
    track.scrollTo({ left: next, behavior: 'smooth' });
  };

  const controls = document.createElement('div');
  controls.className = 'slideshow-controls';
  controls.innerHTML = `
    <button class="slideshow-btn" id="galleryPrev" aria-label="Previous slide">&#8592;</button>
    <button class="slideshow-btn" id="galleryNext" aria-label="Next slide">&#8594;</button>
    <button class="slideshow-btn" id="galleryToggle" aria-label="Pause autoplay">&#10074;&#10074;</button>
  `;
  shell.appendChild(controls);

  const prevBtn = document.getElementById('galleryPrev');
  const nextBtn = document.getElementById('galleryNext');
  const toggleBtn = document.getElementById('galleryToggle');

  let paused = false;

  const updateToggle = () => {
    if (!toggleBtn) return;
    toggleBtn.innerHTML = paused ? '&#9654;' : '&#10074;&#10074;';
  };

  if (prevBtn) prevBtn.addEventListener('click', () => {
    paused = true;
    updateToggle();
    scrollByStep(-1);
  });

  if (nextBtn) nextBtn.addEventListener('click', () => {
    paused = true;
    updateToggle();
    scrollByStep(1);
  });

  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      paused = !paused;
      updateToggle();
    });
  }

  const autoScroll = () => {
    if (paused) return;
    const maxScroll = track.scrollWidth - track.clientWidth;
    if (maxScroll <= 0) return;
    const next = track.scrollLeft + step();
    track.scrollTo({ left: next >= maxScroll ? 0 : next, behavior: 'smooth' });
  };

  let autoTimer = setInterval(autoScroll, 5500);

  track.addEventListener('scroll', () => {
    window.requestAnimationFrame(updateProgress);
  });

  shell.addEventListener('mouseenter', () => {
    paused = true;
    updateToggle();
  });

  shell.addEventListener('mouseleave', () => {
    paused = false;
    updateToggle();
  });

  window.addEventListener('resize', updateProgress);
  updateToggle();
  updateProgress();
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

  // Initialize gallery slider
  initGallerySlider();
  
  console.log('✅ SmartEDU LMS Frontend Fully Initialized');
  console.log('💡 Tip: Press the theme toggle (🌙/☀️) in the header to switch themes');
});

/**
 * Navbar Scroll Effect - Premium Look
 * Adds shadow and styling when user scrolls
 */
function initNavbarScrollEffect() {
  const navbar = document.querySelector('header');
  if (!navbar) return;
  
  window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });
  
  console.log('✅ Navbar Scroll Effect Initialized');
}

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

// Initialize navbar scroll effect when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  initNavbarScrollEffect();
});

