/**
 * CONSULTING COMPANY — MAIN SCRIPTS
 * Sticky Header, Mobile Navigation, Multi-Theme Palette Picker, Accessibility, Back to Top
 */

// Immediate Theme Initialization (runs immediately on script load)
(function initThemeEarly() {
  try {
    const savedTheme = localStorage.getItem('consulting_theme') || 'emerald';
    document.documentElement.setAttribute('data-theme', savedTheme);
  } catch (e) {}
})();

document.addEventListener('DOMContentLoaded', () => {
  // 1. Theme Palette Picker Interaction
  const themeSwatches = document.querySelectorAll('.theme-swatch');
  
  const updateActiveThemeUI = (theme) => {
    themeSwatches.forEach(swatch => {
      const isTarget = swatch.getAttribute('data-theme-target') === theme;
      swatch.classList.toggle('active', isTarget);
      swatch.setAttribute('aria-checked', isTarget ? 'true' : 'false');
    });
  };

  const currentTheme = document.documentElement.getAttribute('data-theme') || 'emerald';
  updateActiveThemeUI(currentTheme);

  themeSwatches.forEach(swatch => {
    swatch.addEventListener('click', () => {
      const targetTheme = swatch.getAttribute('data-theme-target');
      if (targetTheme) {
        document.documentElement.setAttribute('data-theme', targetTheme);
        try {
          localStorage.setItem('consulting_theme', targetTheme);
        } catch (e) {}
        updateActiveThemeUI(targetTheme);
      }
    });
  });

  // 2. Sticky Header
  const header = document.querySelector('.site-header');
  const backToTopBtn = document.querySelector('.back-to-top');

  const handleScroll = () => {
    const scrollPos = window.scrollY || document.documentElement.scrollTop;
    
    if (header) {
      if (scrollPos > 30) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }

    if (backToTopBtn) {
      if (scrollPos > 400) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  // 3. Back to Top Click
  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // 4. Mobile Navigation Toggle
  const mobileToggle = document.querySelector('.mobile-toggle');
  const navMenu = document.querySelector('.nav-menu');

  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      const isExpanded = mobileToggle.getAttribute('aria-expanded') === 'true';
      mobileToggle.setAttribute('aria-expanded', !isExpanded);
      navMenu.classList.toggle('open');
      document.body.style.overflow = !isExpanded ? 'hidden' : '';
    });

    // Close when clicking outside
    document.addEventListener('click', (e) => {
      if (!navMenu.contains(e.target) && !mobileToggle.contains(e.target) && navMenu.classList.contains('open')) {
        navMenu.classList.remove('open');
        mobileToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    });

    // Mobile dropdown toggle on touch/click
    const navDropdownItems = document.querySelectorAll('.nav-item.has-dropdown');
    navDropdownItems.forEach(item => {
      const link = item.querySelector('.nav-link');
      if (link && window.innerWidth < 992) {
        link.addEventListener('click', (e) => {
          if (window.innerWidth < 992) {
            e.preventDefault();
            item.classList.toggle('dropdown-open');
          }
        });
      }
    });
  }

  // 5. Keyboard ESC to close menus
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      if (navMenu && navMenu.classList.contains('open')) {
        navMenu.classList.remove('open');
        if (mobileToggle) mobileToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    }
  });

  // 6. Active Navigation Link Highlighting
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link, .dropdown-link');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath) {
      link.classList.add('active');
      const parentDropdown = link.closest('.nav-item.has-dropdown');
      if (parentDropdown) {
        const parentLink = parentDropdown.querySelector('.nav-link');
        if (parentLink) parentLink.classList.add('active');
      }
    }
  });

  // 7. Scroll Reveal Observer
  const revealElements = document.querySelectorAll('.reveal-item');
  if ('IntersectionObserver' in window && revealElements.length > 0) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    revealElements.forEach(el => observer.observe(el));
  } else {
    revealElements.forEach(el => el.classList.add('revealed'));
  }
});
