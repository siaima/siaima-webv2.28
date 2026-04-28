document.addEventListener('DOMContentLoaded', function () {
  // ===== Header scroll effect =====
  const header = document.querySelector('.site-header');
  if (header) {
    const onScroll = () => {
      if (window.scrollY > 40) header.classList.add('scrolled');
      else header.classList.remove('scrolled');
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // ===== Mobile menu toggle =====
  const mobileToggle = document.querySelector('.mobile-toggle');
  const mobileMenu = document.querySelector('.mobile-menu');
  if (mobileToggle && mobileMenu) {
    mobileToggle.addEventListener('click', () => {
      const open = mobileMenu.classList.toggle('open');
      mobileToggle.setAttribute('aria-expanded', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
    mobileMenu.querySelectorAll('a, .nav-item').forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
        mobileToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
  }

  // ===== GSAP animations =====
  if (typeof gsap === 'undefined') return;
  gsap.registerPlugin(ScrollTrigger);

  gsap.defaults({ ease: 'power2.out', duration: 0.7 });

  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReduced) {
    gsap.globalTimeline.timeScale(2.5);
    document.querySelectorAll('[data-animate]').forEach(el => (el.style.opacity = 1));
    return;
  }

  // ===== Hero entrance =====
  const heroItems = document.querySelectorAll('.hero-inner [data-hero]');
  if (heroItems.length) {
    gsap.from(heroItems, {
      y: 30, opacity: 0, duration: 0.8, stagger: 0.12, delay: 0.1
    });
  }

  // ===== Scroll-triggered fade-in for every section =====
  gsap.utils.toArray('[data-animate]').forEach(el => {
    const delay = parseFloat(el.dataset.delay || 0);
    gsap.fromTo(el,
      { y: 40, opacity: 0 },
      {
        y: 0, opacity: 1, duration: 0.7, delay,
        scrollTrigger: {
          trigger: el,
          start: 'top 85%',
          toggleActions: 'play none none none'
        }
      }
    );
  });

  // ===== Staggered grid items =====
  gsap.utils.toArray('[data-stagger]').forEach(container => {
    const items = container.querySelectorAll('[data-stagger-item]');
    if (!items.length) return;
    gsap.fromTo(items,
      { y: 40, opacity: 0 },
      {
        y: 0, opacity: 1, duration: 0.7, stagger: 0.08,
        scrollTrigger: {
          trigger: container,
          start: 'top 82%',
          toggleActions: 'play none none none'
        }
      }
    );
  });

  // ===== Counter animation =====
  // data-target (number) · data-prefix · data-suffix · data-decimals (default 0)
  gsap.utils.toArray('.counter').forEach(el => {
    const target = parseFloat(el.dataset.target || 0);
    const suffix = el.dataset.suffix || '';
    const prefix = el.dataset.prefix || '';
    const decimals = parseInt(el.dataset.decimals || 0);
    const obj = { val: 0 };
    gsap.to(obj, {
      val: target, duration: 1.8, ease: 'power1.out',
      scrollTrigger: { trigger: el, start: 'top 85%' },
      onUpdate() {
        const v = decimals > 0
          ? obj.val.toFixed(decimals)
          : Math.round(obj.val).toLocaleString('en-US');
        el.textContent = prefix + v + suffix;
      }
    });
  });

  // ===== Parallax on hero bg =====
  const heroBg = document.querySelector('.hero-bg');
  if (heroBg) {
    gsap.to(heroBg, {
      y: 100, ease: 'none',
      scrollTrigger: { trigger: '.section-hero', start: 'top top', end: 'bottom top', scrub: true }
    });
  }

  // ===== Hover spotlight glow (cursor-following) =====
  const GLOW_SELECTOR = [
    // Cards
    '.pillar-card', '.stat-card', '.case-card', '.blog-card', '.team-card',
    '.mvv-card', '.culture-card', '.service-hero__kpi-card', '.deliverable-card',
    '.pricing-card', '.case-meta-card', '.psr-card', '.industry-card',
    '.community-card', '.speaker-form-card', '.principle-card',
    '.gen-stat-card', '.gen-chart-card', '.gen-speaker-card', '.gen-timeline-item',
    '.gen-logo-item', '.audience-card', '.value-card',
    '.hero-stat', '.faq-item',
    // Interactive
    '.btn', '.nav-link', '.nav-item',
    '.form-input', '.form-select', '.form-textarea', '.form-tab',
    '.moments-thumb'
  ].join(', ');
  document.querySelectorAll(GLOW_SELECTOR).forEach(el => el.classList.add('glow'));
  document.addEventListener('pointermove', (e) => {
    const el = e.target.closest('.glow');
    if (!el) return;
    const r = el.getBoundingClientRect();
    el.style.setProperty('--mx', (e.clientX - r.left) + 'px');
    el.style.setProperty('--my', (e.clientY - r.top) + 'px');
  }, { passive: true });

  // ===== Smooth anchor scroll =====
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', (e) => {
      const id = a.getAttribute('href');
      if (id.length <= 1) return;
      const target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      const navH = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--nav-height')) || 72;
      const top = target.getBoundingClientRect().top + window.pageYOffset - navH - 16;
      window.scrollTo({ top, behavior: 'smooth' });
    });
  });
});
