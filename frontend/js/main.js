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
 * Display mode management (mobile / tablet / monitor)
 */
class DisplayModeManager {
  constructor() {
    this.storageKey = 'smartedu_display';
    this.modes = ['mobile', 'tablet', 'monitor'];
    const queryMode = this.getQueryMode();
    this.currentMode = queryMode || this.getSavedMode() || 'monitor';
    this.applyMode(this.currentMode);
    if (queryMode) {
      this.saveMode(queryMode);
    }
  }

  getQueryMode() {
    try {
      const params = new URLSearchParams(window.location.search);
      const mode = params.get('display');
      return this.modes.includes(mode) ? mode : null;
    } catch (error) {
      return null;
    }
  }

  getSavedMode() {
    try {
      const saved = localStorage.getItem(this.storageKey);
      return this.modes.includes(saved) ? saved : null;
    } catch (error) {
      return null;
    }
  }

  saveMode(mode) {
    try {
      localStorage.setItem(this.storageKey, mode);
    } catch (error) {
      // ignore storage failures
    }
  }

  applyMode(mode) {
    if (mode && this.modes.includes(mode)) {
      document.documentElement.setAttribute('data-display', mode);
      if (document.body) {
        document.body.setAttribute('data-display', mode);
      }
      updateDisplayLinks(mode);
      updateDisplayUrl(mode);
    } else {
      document.documentElement.removeAttribute('data-display');
      if (document.body) {
        document.body.removeAttribute('data-display');
      }
    }
  }

  setMode(mode) {
    if (!this.modes.includes(mode)) return;
    this.currentMode = mode;
    this.saveMode(mode);
    this.applyMode(mode);
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

function setDisplayMode(mode) {
  if (window.displayModeManager) {
    window.displayModeManager.setMode(mode);
  } else if (mode) {
    try {
      localStorage.setItem('smartedu_display', mode);
    } catch (error) {
      // ignore
    }
    document.documentElement.setAttribute('data-display', mode);
    if (document.body) {
      document.body.setAttribute('data-display', mode);
    }
    updateDisplayLinks(mode);
    updateDisplayUrl(mode);
  }
}

function updateDisplayUrl(mode) {
  if (!mode) return;
  try {
    const url = new URL(window.location.href);
    url.searchParams.set('display', mode);
    history.replaceState({}, '', `${url.pathname}${url.search}${url.hash}`);
  } catch (error) {
    // ignore URL rewrite issues
  }
}

function updateDisplayLinks(mode) {
  if (!mode) return;
  const links = document.querySelectorAll('a[href]');
  links.forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;
    const lower = href.toLowerCase();
    if (lower.startsWith('#') || lower.startsWith('mailto:') || lower.startsWith('tel:') || lower.startsWith('javascript:')) {
      return;
    }
    if (lower.startsWith('http://') || lower.startsWith('https://') || lower.startsWith('//')) {
      return;
    }

    const hashSplit = href.split('#');
    const base = hashSplit[0];
    const hash = hashSplit.length > 1 ? `#${hashSplit.slice(1).join('#')}` : '';
    const querySplit = base.split('?');
    const path = querySplit[0];
    const queryString = querySplit.length > 1 ? querySplit.slice(1).join('?') : '';

    const params = new URLSearchParams(queryString);
    params.set('display', mode);
    const next = `${path}?${params.toString()}${hash}`;
    link.setAttribute('href', next);
  });
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
 * Mobile navigation (hamburger) for small screens
 */
function initMobileNav() {
  const headers = document.querySelectorAll('header');
  if (!headers.length) return;

  let backdrop = document.getElementById('mobileNavBackdrop');
  if (!backdrop) {
    backdrop = document.createElement('div');
    backdrop.id = 'mobileNavBackdrop';
    backdrop.className = 'mobile-nav-backdrop';
    backdrop.setAttribute('aria-hidden', 'true');
    document.body.appendChild(backdrop);
  }

  const closeAll = () => {
    headers.forEach(h => h.classList.remove('nav-open'));
    document.querySelectorAll('.nav-toggle[aria-expanded="true"]').forEach(btn => {
      btn.setAttribute('aria-expanded', 'false');
    });
    backdrop.classList.remove('show');
  };

  const openFor = (header, toggleButton) => {
    closeAll();
    header.classList.add('nav-open');
    toggleButton.setAttribute('aria-expanded', 'true');
    backdrop.classList.add('show');
  };

  headers.forEach((header, index) => {
    const wrapper = header.querySelector('.header-wrapper');
    const nav = header.querySelector('nav');
    if (!wrapper || !nav) return;

    if (!nav.id) nav.id = `siteNav_${index + 1}`;

    let toggleButton = wrapper.querySelector('.nav-toggle');
    if (!toggleButton) {
      toggleButton = document.createElement('button');
      toggleButton.type = 'button';
      toggleButton.className = 'nav-toggle';
      toggleButton.setAttribute('aria-controls', nav.id);
      toggleButton.setAttribute('aria-expanded', 'false');
      toggleButton.setAttribute('aria-label', 'Toggle navigation menu');
      toggleButton.innerHTML = '<span aria-hidden="true">☰</span><span class="nav-toggle-label">Menu</span>';

      const themeToggle = wrapper.querySelector('.theme-toggle');
      if (themeToggle) {
        wrapper.insertBefore(toggleButton, themeToggle);
      } else {
        wrapper.appendChild(toggleButton);
      }
    }

    header.classList.add('has-mobile-nav');

    toggleButton.addEventListener('click', () => {
      const isOpen = header.classList.contains('nav-open');
      if (isOpen) {
        closeAll();
      } else {
        openFor(header, toggleButton);
      }
    });

    nav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => closeAll());
    });
  });

  backdrop.addEventListener('click', () => closeAll());

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeAll();
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 768) closeAll();
  });
}

/**
 * Inject display mode link into nav
 */
function initDisplayModeNav() {
  const headers = document.querySelectorAll('header');
  if (!headers.length) return;

  headers.forEach(header => {
    header.querySelectorAll('nav a[href="display-mode.html"]').forEach(link => link.remove());
    const action = header.querySelector('.display-mode-button');
    if (action) action.remove();
  });
}

/**
 * Display mode page interactions
 */
function initDisplayModePage() {
  const page = document.querySelector('[data-display-page]');
  if (!page) return;

  const cards = page.querySelectorAll('[data-display-select]');
  const status = page.querySelector('[data-display-status]');
  const current = document.documentElement.getAttribute('data-display')
    || (window.displayModeManager && window.displayModeManager.currentMode)
    || (typeof localStorage !== 'undefined' ? localStorage.getItem('smartedu_display') : null)
    || 'monitor';

  const updateActive = (mode) => {
    cards.forEach(card => {
      card.classList.toggle('active', card.dataset.displaySelect === mode);
    });
    if (status) {
      status.textContent = `Current selection: ${mode.charAt(0).toUpperCase() + mode.slice(1)}`;
    }
  };

  updateActive(current);

  cards.forEach(card => {
    const mode = card.dataset.displaySelect;
    card.querySelectorAll('[data-display-button]').forEach(btn => {
      btn.addEventListener('click', () => {
        setDisplayMode(mode);
        updateActive(mode);
      });
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
 * Auth prompt for login/signup
 */
function initAuthPrompt() {
  const currentPath = window.location.pathname.toLowerCase();
  if (currentPath.includes('login.html') || currentPath.includes('signup.html')) {
    return;
  }

  let prompt = document.getElementById('authPrompt');
  if (!prompt) {
    prompt = document.createElement('div');
    prompt.id = 'authPrompt';
    prompt.className = 'auth-prompt';
    prompt.setAttribute('aria-hidden', 'true');
    prompt.innerHTML = `
      <div class="auth-prompt-card" role="dialog" aria-modal="true" aria-labelledby="authPromptTitle">
        <button class="auth-prompt-close" type="button" aria-label="Close" data-auth-close>×</button>
        <h3 id="authPromptTitle">Welcome to SmartEDU LMS</h3>
        <p>Log in or create an account to save progress, access AI tools, and track certificates.</p>
        <div class="auth-prompt-actions">
          <a href="login.html" class="btn btn-primary">Log In</a>
          <a href="signup.html" class="btn btn-outline">Sign Up</a>
        </div>
        <button class="auth-prompt-skip" type="button" data-auth-close>Continue as guest</button>
      </div>
    `;
    document.body.appendChild(prompt);
  }

  const currentUser = localStorage.getItem('currentUser');
  if (currentUser) return;

  if (sessionStorage.getItem('auth_prompt_dismissed') === '1') return;

  prompt.classList.add('show');
  prompt.setAttribute('aria-hidden', 'false');

  const dismiss = () => {
    prompt.classList.remove('show');
    prompt.setAttribute('aria-hidden', 'true');
    sessionStorage.setItem('auth_prompt_dismissed', '1');
  };

  prompt.querySelectorAll('[data-auth-close]').forEach(btn => {
    btn.addEventListener('click', dismiss);
  });

  prompt.addEventListener('click', (event) => {
    if (event.target === prompt) {
      dismiss();
    }
  });
}

/**
 * Navbar auth links (login/signup/logout)
 */
function initAuthNav() {
  const navs = document.querySelectorAll('header nav');
  if (!navs.length) return;

  navs.forEach(nav => {
    const findAuthLink = (target) => {
      const links = Array.from(nav.querySelectorAll('a[href]'));
      return links.find(link => {
        const href = link.getAttribute('href');
        if (!href) return false;
        const base = href.split('#')[0].split('?')[0];
        return base.endsWith(target);
      }) || null;
    };

    let login = findAuthLink('login.html');
    if (!login) {
      login = document.createElement('a');
      login.href = 'login.html';
      login.textContent = 'Login';
      nav.appendChild(login);
    }
    login.dataset.auth = 'login';
    login.classList.add('auth-link', 'auth-login');

    let signup = findAuthLink('signup.html');
    if (!signup) {
      signup = document.createElement('a');
      signup.href = 'signup.html';
      signup.textContent = 'Sign Up';
      signup.className = 'btn btn-primary';
      signup.style.padding = '0.5rem 1rem';
      nav.appendChild(signup);
    }
    signup.dataset.auth = 'signup';
    signup.classList.add('auth-link');

    let logout = nav.querySelector('[data-auth="logout"]');
    if (!logout) {
      logout = document.createElement('a');
      logout.href = '#';
      logout.textContent = 'Logout';
      logout.className = 'btn btn-secondary';
      logout.style.padding = '0.5rem 1rem';
      logout.dataset.auth = 'logout';
      nav.appendChild(logout);
    }
  });

  updateAuthNav();
}

function updateAuthNav() {
  const isAuthed = Boolean(localStorage.getItem('currentUser'));

  document.querySelectorAll('[data-auth="login"]').forEach(link => {
    link.classList.toggle('auth-hidden', isAuthed);
  });

  document.querySelectorAll('[data-auth="signup"]').forEach(link => {
    link.classList.toggle('auth-hidden', isAuthed);
  });

  document.querySelectorAll('[data-auth="logout"]').forEach(link => {
    link.classList.toggle('auth-hidden', !isAuthed);
    if (!link.dataset.bound) {
      link.addEventListener('click', (event) => {
        event.preventDefault();
        localStorage.removeItem('currentUser');
        window.location.href = 'index.html';
      });
      link.dataset.bound = 'true';
    }
  });
}

/**
 * Initialize all systems when DOM is ready
 */
document.addEventListener('DOMContentLoaded', () => {
  // Initialize theme manager
  window.themeManager = new ThemeManager();

  // Initialize display mode manager
  window.displayModeManager = new DisplayModeManager();
  
  // Initialize scroll animator
  new ScrollAnimator();
  
  // Setup smooth scrolling
  setupSmoothScroll();

  // Mobile nav menu
  initMobileNav();

  // Display mode nav link
  initDisplayModeNav();

  // Display mode page
  initDisplayModePage();

  // Initialize gallery slider
  initGallerySlider();

  // Initialize auth prompt
  initAuthPrompt();

  // Initialize auth nav
  initAuthNav();
  
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

