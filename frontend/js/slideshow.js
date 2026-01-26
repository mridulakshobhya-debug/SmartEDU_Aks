// slideshow.js - Advanced Image Slideshow with Swipe Animations

class HeroSlideshow {
  constructor() {
    this.currentSlide = 0;
    this.touchStartX = 0;
    this.touchEndX = 0;
    this.isTransitioning = false;
    this.slides = [
      {
        image: '/images/businessman-using-laptop-while-sitting-with-young-coworkers-conference-table-coworking-office.jpg',
        fallbackColor: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
      },
      {
        image: '/images/creative-group-working-startup-using-laptops.jpg',
        fallbackColor: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)'
      },
      {
        image: '/images/modern-equipped-computer-lab (1).jpg',
        fallbackColor: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)'
      },
      {
        image: '/images/multiethnic-designers-sitting-together-working-laptops-coworking-space.jpg',
        fallbackColor: 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)'
      },
      {
        image: '/images/people-analyzing-checking-finance-graphs-office.jpg',
        fallbackColor: 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)'
      }
    ];
    this.autoPlayInterval = null;
    this.init();
  }

  init() {
    this.createSlides();
    this.createIndicators();
    this.startAutoPlay();
    this.setupEventListeners();
  }

  createSlides() {
    const container = document.getElementById('heroBackground');
    if (!container) return;

    this.slides.forEach((slide, index) => {
      const slideElement = document.createElement('div');
      slideElement.className = 'hero-slide';
      if (index === 0) slideElement.classList.add('active');

      // Try to load image, fallback to gradient
      slideElement.style.backgroundImage = `url('${slide.image}')`;
      slideElement.style.backgroundColor = slide.fallbackColor;
      slideElement.style.backgroundBlendMode = 'overlay';

      container.appendChild(slideElement);
    });
  }

  createIndicators() {
    const container = document.getElementById('slideIndicators');
    if (!container) return;

    this.slides.forEach((_, index) => {
      const dot = document.createElement('div');
      dot.className = 'slide-dot';
      if (index === 0) dot.classList.add('active');
      dot.addEventListener('click', () => this.goToSlide(index));
      container.appendChild(dot);
    });
  }

  showSlide(index, direction = 'next') {
    if (this.isTransitioning) return;
    
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.slide-dot');

    // Add transition class based on direction
    slides.forEach((slide, i) => {
      slide.classList.remove('active', 'slide-out-left', 'slide-out-right', 'slide-in-left', 'slide-in-right');
      
      if (i === this.currentSlide) {
        // Outgoing slide
        if (direction === 'next') {
          slide.classList.add('slide-out-left');
        } else {
          slide.classList.add('slide-out-right');
        }
      }
      
      if (i === index) {
        // Incoming slide
        if (direction === 'next') {
          slide.classList.add('slide-in-right');
        } else {
          slide.classList.add('slide-in-left');
        }
        slide.classList.add('active');
      }
    });

    dots.forEach((dot, i) => {
      dot.classList.remove('active');
      if (i === index) {
        dot.classList.add('active');
      }
    });

    this.currentSlide = index;
    this.isTransitioning = true;
    
    setTimeout(() => {
      this.isTransitioning = false;
    }, 1000);
  }

  nextSlide() {
    const next = (this.currentSlide + 1) % this.slides.length;
    this.showSlide(next, 'next');
  }

  prevSlide() {
    const prev = (this.currentSlide - 1 + this.slides.length) % this.slides.length;
    this.showSlide(prev, 'prev');
  }

  goToSlide(index) {
    const direction = index > this.currentSlide ? 'next' : 'prev';
    this.showSlide(index, direction);
    this.resetAutoPlay();
  }

  startAutoPlay() {
    this.autoPlayInterval = setInterval(() => {
      this.nextSlide();
    }, 6500);
  }

  resetAutoPlay() {
    clearInterval(this.autoPlayInterval);
    this.startAutoPlay();
  }

  setupEventListeners() {
    const heroSection = document.querySelector('.hero-section');
    if (!heroSection) return;

    // Pause on hover
    heroSection.addEventListener('mouseenter', () => {
      clearInterval(this.autoPlayInterval);
    });

    heroSection.addEventListener('mouseleave', () => {
      this.startAutoPlay();
    });

    // Touch/Swipe support
    heroSection.addEventListener('touchstart', (e) => {
      this.touchStartX = e.changedTouches[0].screenX;
    }, false);

    heroSection.addEventListener('touchend', (e) => {
      this.touchEndX = e.changedTouches[0].screenX;
      this.handleSwipe();
    }, false);

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') {
        this.prevSlide();
        this.resetAutoPlay();
      }
      if (e.key === 'ArrowRight') {
        this.nextSlide();
        this.resetAutoPlay();
      }
    });

    // Mouse drag support
    let isMouseDown = false;
    heroSection.addEventListener('mousedown', (e) => {
      isMouseDown = true;
      this.touchStartX = e.clientX;
    });

    heroSection.addEventListener('mousemove', (e) => {
      if (!isMouseDown) return;
    });

    heroSection.addEventListener('mouseup', (e) => {
      if (!isMouseDown) return;
      isMouseDown = false;
      this.touchEndX = e.clientX;
      this.handleSwipe();
    });

    heroSection.addEventListener('mouseleave', () => {
      isMouseDown = false;
    });
  }

  handleSwipe() {
    const swipeThreshold = 50;
    const diff = this.touchStartX - this.touchEndX;

    if (Math.abs(diff) < swipeThreshold) return;

    if (diff > 0) {
      // Swiped left - show next slide
      this.nextSlide();
    } else {
      // Swiped right - show previous slide
      this.prevSlide();
    }

    this.resetAutoPlay();
  }
}

// Initialize slideshow when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  new HeroSlideshow();
});
