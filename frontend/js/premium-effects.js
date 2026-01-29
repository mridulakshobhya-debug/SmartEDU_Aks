// ============================================
// PREMIUM EFFECTS & ANIMATIONS
// ============================================

// Intersection Observer for scroll animations
const createIntersectionObserver = () => {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-in-view');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Observe all animatable elements
  document.querySelectorAll('.card, .premium-card, .testimonial-card, .pricing-card, h2, p').forEach(el => {
    if (!el.classList.contains('animate-in-view')) {
      observer.observe(el);
    }
  });
};

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  createIntersectionObserver();
  createParticleEffect();
  initializeParallax();
  setupScrollAnimations();
});

// ============================================
// PARTICLE EFFECTS
// ============================================

const createParticleEffect = () => {
  const heroSection = document.querySelector('.hero-section');
  if (!heroSection) return;

  // Remove existing particles
  const existingParticles = document.querySelectorAll('.particle');
  existingParticles.forEach(p => p.remove());

  const particlesContainer = document.createElement('div');
  particlesContainer.className = 'hero-particles';
  heroSection.appendChild(particlesContainer);

  // Create 50 particles
  for (let i = 0; i < 50; i++) {
    const particle = document.createElement('div');
    particle.className = 'particle';

    // Random properties
    const size = Math.random() > 0.8 ? 'large' : Math.random() > 0.6 ? 'small' : '';
    const hasGlow = Math.random() > 0.7;
    const x = Math.random() * 100;
    const y = Math.random() * 100;
    const duration = 10 + Math.random() * 15;
    const delay = Math.random() * 2;

    if (size) particle.classList.add(size);
    if (hasGlow) particle.classList.add('glow');
    particle.classList.add('animate-float');

    particle.style.left = x + '%';
    particle.style.top = y + '%';
    particle.style.setProperty('--random-duration', duration + 's');
    particle.style.animation = `floatUp ${duration}s linear ${delay}s infinite`;

    particlesContainer.appendChild(particle);
  }
};

// ============================================
// PARALLAX SCROLL EFFECT
// ============================================

const initializeParallax = () => {
  const parallaxElements = document.querySelectorAll('[data-parallax]');

  if (parallaxElements.length === 0) return;

  window.addEventListener('scroll', () => {
    parallaxElements.forEach(el => {
      const speed = el.getAttribute('data-parallax') || 0.5;
      const yPos = window.scrollY * speed;
      el.style.transform = `translateY(${yPos}px)`;
    });
  });
};

// ============================================
// SCROLL ANIMATIONS
// ============================================

const setupScrollAnimations = () => {
  // Fade in elements on scroll
  const animateOnScroll = () => {
    document.querySelectorAll('.card, .premium-card').forEach((el, index) => {
      const rect = el.getBoundingClientRect();
      const isVisible = rect.top < window.innerHeight && rect.bottom > 0;

      if (isVisible && !el.classList.contains('animated')) {
        el.classList.add('animated');
        el.style.animation = `slideInUp 0.6s ease-out ${index * 0.1}s both`;
      }
    });
  };

  window.addEventListener('scroll', animateOnScroll);
  animateOnScroll(); // Initial check
};

// ============================================
// COUNTER ANIMATION
// ============================================

const animateCounters = () => {
  const counters = document.querySelectorAll('[data-counter]');

  counters.forEach(counter => {
    const target = parseInt(counter.getAttribute('data-counter'));
    const duration = 2000; // 2 seconds
    const increment = target / (duration / 16); // 60fps

    let current = 0;
    const interval = setInterval(() => {
      current += increment;
      if (current >= target) {
        counter.textContent = target;
        clearInterval(interval);
      } else {
        counter.textContent = Math.floor(current);
      }
    }, 16);
  });
};

// ============================================
// FLOATING ELEMENTS
// ============================================

const createFloatingElements = () => {
  const elements = document.querySelectorAll('[data-float]');

  elements.forEach(el => {
    el.style.animation = 'infiniteFloat 4s ease-in-out infinite';
  });
};

// ============================================
// GRADIENT ANIMATIONS
// ============================================

const applyGradientAnimations = () => {
  const elements = document.querySelectorAll('[data-gradient-animate]');

  elements.forEach(el => {
    el.style.backgroundSize = '200% 200%';
    el.style.animation = 'gradientFlow 15s ease infinite';
  });
};

// ============================================
// MOUSE FOLLOW EFFECT
// ============================================

const createMouseFollowEffect = () => {
  const cursor = document.createElement('div');
  cursor.className = 'cursor-follower';
  cursor.style.cssText = `
    position: fixed;
    width: 20px;
    height: 20px;
    background: radial-gradient(circle, rgba(31, 92, 240, 0.5), transparent);
    border-radius: 50%;
    pointer-events: none;
    z-index: 999;
    display: none;
  `;
  document.body.appendChild(cursor);

  let mouseX = 0;
  let mouseY = 0;
  let cursorX = 0;
  let cursorY = 0;

  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    cursor.style.display = 'block';

    // Smooth follow effect
    const delay = 0.2;
    cursorX += (mouseX - cursorX) * delay;
    cursorY += (mouseY - cursorY) * delay;

    cursor.style.left = cursorX - 10 + 'px';
    cursor.style.top = cursorY - 10 + 'px';
  });

  document.addEventListener('mouseleave', () => {
    cursor.style.display = 'none';
  });
};

// ============================================
// RIPPLE EFFECT ON BUTTONS
// ============================================

const addRippleEffect = () => {
  document.querySelectorAll('.btn, button').forEach(button => {
    button.addEventListener('click', function(e) {
      const ripple = document.createElement('span');
      const rect = this.getBoundingClientRect();
      const size = Math.max(rect.width, rect.height);
      const x = e.clientX - rect.left - size / 2;
      const y = e.clientY - rect.top - size / 2;

      ripple.style.cssText = `
        position: absolute;
        width: ${size}px;
        height: ${size}px;
        background: rgba(255, 255, 255, 0.5);
        border-radius: 50%;
        left: ${x}px;
        top: ${y}px;
        pointer-events: none;
        animation: ripple 0.6s ease-out;
      `;

      if (!this.style.position || this.style.position === 'static') {
        this.style.position = 'relative';
      }

      this.appendChild(ripple);
      setTimeout(() => ripple.remove(), 600);
    });
  });
};

// Add ripple animation keyframes
const style = document.createElement('style');
style.textContent = `
  @keyframes ripple {
    to {
      transform: scale(4);
      opacity: 0;
    }
  }
`;
document.head.appendChild(style);

// ============================================
// LAZY LOAD IMAGES WITH BLUR ANIMATION
// ============================================

const setupLazyLoading = () => {
  const images = document.querySelectorAll('img[data-src]');

  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.getAttribute('data-src');
        img.classList.add('loaded');
        observer.unobserve(img);
      }
    });
  });

  images.forEach(img => imageObserver.observe(img));
};

// ============================================
// TEXT REVEAL ANIMATION
// ============================================

const createTextRevealAnimation = () => {
  const revealElements = document.querySelectorAll('[data-text-reveal]');

  revealElements.forEach(el => {
    const text = el.textContent;
    el.innerHTML = '';
    
    text.split('').forEach((char, index) => {
      const span = document.createElement('span');
      span.textContent = char;
      span.style.animation = `textSlide 0.6s ease-out ${index * 0.05}s both`;
      el.appendChild(span);
    });
  });
};

// ============================================
// TYPEWRITER EFFECT
// ============================================

const createTypewriterEffect = () => {
  const elements = document.querySelectorAll('[data-typewriter]');

  elements.forEach(el => {
    const text = el.textContent;
    el.textContent = '';
    let index = 0;

    const type = () => {
      if (index < text.length) {
        el.textContent += text[index];
        index++;
        setTimeout(type, 50);
      }
    };

    type();
  });
};

// ============================================
// SCROLL PROGRESS BAR
// ============================================

const createScrollProgressBar = () => {
  const progressBar = document.createElement('div');
  progressBar.style.cssText = `
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    background: linear-gradient(90deg, #1f5cf0, #6c5ce7);
    z-index: 1000;
    animation: gradientFlow 3s ease infinite;
  `;
  document.body.appendChild(progressBar);

  window.addEventListener('scroll', () => {
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrolled = (window.scrollY / scrollHeight) * 100;
    progressBar.style.width = scrolled + '%';
  });
};

// ============================================
// ANIMATE NUMBERS
// ============================================

const animateNumber = (element, target, duration = 2000) => {
  const start = 0;
  const increment = target / (duration / 16);
  let current = start;

  const counter = setInterval(() => {
    current += increment;
    if (current >= target) {
      element.textContent = target;
      clearInterval(counter);
    } else {
      element.textContent = Math.floor(current);
    }
  }, 16);
};

// ============================================
// INITIALIZE ALL EFFECTS
// ============================================

document.addEventListener('DOMContentLoaded', () => {
  // Initialize all effects
  setTimeout(() => {
    createFloatingElements();
    applyGradientAnimations();
    createMouseFollowEffect();
    addRippleEffect();
    setupLazyLoading();
    createTextRevealAnimation();
    createTypewriterEffect();
    createScrollProgressBar();
  }, 100);
});

// Reinitialize on window resize
window.addEventListener('resize', () => {
  // Reinitialize particles on resize
  if (window.innerWidth > 768) {
    createParticleEffect();
  }
});
