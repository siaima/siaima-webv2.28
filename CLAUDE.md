# SIA Innovation Marketing Agency — Website Project

## Project Overview

**Client:** SIA Innovation Marketing Agency (SIA IMA)  
**Goal:** Build a bilingual (Vietnamese + English) marketing agency website — modern, professional, minimalist style with light/dark mode.  
**Market:** Vietnam (primary), Southeast Asia  
**Contact info:** 14 Ngõ Bệ, Tân Bình · 0988 441 630 · sia.agency@siagroupco.com

### About SIA
SIA là công ty thương mại xây dựng cộng đồng, kết nối & khai thác hệ sinh thái doanh nhân, creator, sinh viên tại Việt Nam và quốc tế. Hoạt động qua 3 trụ cột:

- **SIA IMA** — Innovation Marketing (Solutions & Media Production): tư vấn chiến lược, chiến dịch truyền thông tích hợp, Creative Mega Livestream, media production.
- **SIA Event** — Brand Experience: sự kiện doanh nghiệp, hội thảo, workshop, Brand Experience O2O.
- **SIA Hub** — Influencer Marketing · Social Commerce · Creator Ecosystem: KOL/KOC/UGC/Affiliate, KOC Hub community, e-commerce & livestream solutions.

Hành trình brand: **Chiến lược → Truyền thông → Trải nghiệm → Chuyển đổi**

---

## Project Status — v2 (cập nhật 2026-04-24)

Website đã build xong v2 với 15 trang production. So với v1:

**Trang mới bổ sung:**
- `services.html` — hub trung gian 3 trụ cột dịch vụ
- `community.html` — trang Cộng đồng (KOC Hub · Business Network · Next Gen)
- `partnership.html` — form đăng ký đối tác
- `speaker.html` — form đăng ký speaker cho community events
- `event-detail-a.html`, `event-detail-b.html` — template chi tiết sự kiện (2 biến thể)

**Thay đổi trang cũ:**
- `index.html` được tái cấu trúc sang 10 section mới: `hero → services → story → moments → mvv → cases → timeline-intro → timeline → blog → contact` (khác với bảng wireframe v1)
- `about.html` bị gộp vào `index.html`, chỉ còn là stub meta-refresh → đừng thêm nội dung cho nó
- Section "Counter stats" và "Logo wall" **không còn trên index.html v2**; chỉ còn ở `showcase.html` (block clients)

**Assets mới:**
- `assets/images/siamoment/` chứa 5 ảnh sự kiện dùng cho section `moments` và gallery
- `assets/css/components.css` đã mở rộng lên ~113KB với hệ `.form-*`, `.blog-card__*`, `.case-card__*`, `.section--alt/--tight`, `.timeline`, `.faq-*`, `.office-*`, `.community-*`, `.program-card` — **tái sử dụng trước khi tạo class mới**

---

## Reference Files (không edit — chỉ đọc để tham chiếu)

| File | Purpose |
|------|---------|
| `SIA_Marketing_Design_System.html` | Design tokens, typography, components, do/don't rules |
| `sia_wireframe_sitemap_v3.html` | Sitemap + wireframe IA v3 (đã cập nhật theo v2) |
| `chitietsukien-wireframe.html` | Wireframe trang chi tiết sự kiện (tham chiếu khi build event-detail-*) |
| `SIA-innovation-logo.png` / `-black.png` / `-white.png` | Logo gốc ở project root (bản copy đang dùng nằm trong `assets/images/logo/`) |

> **Ghi chú:** Các file `*.py` ở root (`add_html.py`, `fix_*.py`, `update*.py`, `parse*.py`, `check.py`, v.v.) là script dùng một lần để bulk-update nhiều trang HTML cùng lúc trong quá trình build v2. **Không chạy lại** trừ khi chủ động muốn re-run. Khi chỉnh 1–2 trang thì edit trực tiếp file HTML.

---

## Technology Stack

- **HTML5** — semantic markup, no build tools, no framework
- **CSS3** — CSS custom properties (`var(--token)`), no preprocessor
- **GSAP 3** — animations (CDN: `https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js`)
- **GSAP ScrollTrigger** — scroll-driven animations (`gsap/ScrollTrigger.min.js`)
- **Swiper.js** — sliders/carousels (`https://cdn.jsdelivr.net/npm/swiper@11/...`)
- **Alpine.js** — lightweight reactive UI (accordion, dropdown, toggle) (`https://cdn.jsdelivr.net/npm/alpinejs@3/dist/cdn.min.js`)

All libraries loaded via CDN — no npm, no bundler.

---

## File Structure (v2 — hiện trạng)

```
/ (project root)
│
│ ─── Trang production ─────────────────────────────────────
├── index.html                     # Trang chủ — 10 sections (xem bảng bên dưới)
├── about.html                     # ⚠️ STUB — chỉ là meta-refresh redirect về index.html
├── services.html                  # Hub tổng quan dịch vụ: 3 trụ cột + principles
├── services-ima.html              # DV: SIA IMA — hero · deliverables · process · pricing
├── services-event.html            # DV: SIA Event — ... + past-events gallery
├── services-hub.html              # DV: SIA Hub — ... + industries selector
├── showcase.html                  # Showcase / Case studies (grid)
├── showcase-detail.html           # Chi tiết case (template: Mega Livestream 5 tỷ)
├── blog.html                      # Blog listing + featured + newsletter form
├── blog-detail.html               # Chi tiết bài viết + related
├── community.html                 # Cộng đồng: KOC Hub · Business Network · Next Gen + sponsors
├── contact.html                   # Form liên hệ + office grid + FAQ (Alpine accordion)
├── partnership.html               # Form đăng ký đối tác
├── speaker.html                   # Form đăng ký Speaker cho community events
├── event-detail-a.html            # Event detail — KOC Hub Workshop #12 (template A)
├── event-detail-b.html            # Event detail — Mega Livestream 5.5 (template B)
│
│ ─── Assets ──────────────────────────────────────────────
├── assets/
│   ├── css/
│   │   ├── variables.css          # Design tokens
│   │   ├── base.css               # Reset, body, dark/light mode
│   │   ├── components.css         # ⚠️ File chính (~113KB, 4300+ dòng) — toàn bộ component
│   │   └── animations.css         # CSS transitions & keyframes
│   ├── js/
│   │   ├── main.js                # GSAP init, ScrollTrigger, page animations
│   │   ├── theme.js               # Dark/light mode toggle & persistence
│   │   └── swiper-init.js         # Swiper instances config
│   └── images/
│       ├── logo/                  # sia-logo.png / -black.png / -white.png
│       ├── siamoment/             # Ảnh sự kiện/moments (5 ảnh, dùng cho hero + gallery)
│       ├── hero/ · cases/ · team/ · clients/   # Placeholder folders (chưa dùng nhiều)
│
│ ─── Reference & wireframes (không edit) ────────────────
├── SIA_Marketing_Design_System.html
├── sia_wireframe_sitemap_v3.html
├── chitietsukien-wireframe.html
│
│ ─── Scripts bulk-update một lần (không chạy lại) ───────
├── add_html.py · add_gen_css.py · update.py · update_community*.py
├── create_partnership.py · fix_*.py · parse*.py · check.py
│
└── CLAUDE.md
```

---

## Design Tokens

Tất cả tokens dưới đây phải được khai báo trong `assets/css/variables.css` rồi dùng qua `var()`.

### Colors — Light mode (`:root`)

```css
:root {
  /* Primary */
  --primary:        #E8502A;
  --primary-light:  #F07A5C;
  --primary-dark:   #C43A1A;

  /* Secondary */
  --secondary:      #2C6E8A;
  --secondary-light:#4A90A8;
  --secondary-dark: #1A4F65;

  /* Neutral */
  --black:      #0D0D0D;
  --gray-700:   #3D3D3D;
  --gray-500:   #6E6E6E;
  --gray-300:   #B8B8B8;
  --gray-100:   #F0F0F0;
  --gray-50:    #F8F8F8;
  --white:      #FFFFFF;
  --warm-gray:  #E8E0D4;
  --surface-1:  #F5F2EE;
  --surface-2:  #EAE4DC;
  --disabled:   #D6D6D6;

  /* Semantic */
  --success: #2A8A4A;
  --warning: #D4A017;
  --error:   #C43A1A;
  --info:    #2C6E8A;

  /* Orange ramp */
  --orange-100: #FFF0EB;
  --orange-200: #FFD4C2;
  --orange-300: #FFB89A;
  --orange-400: #FF9C72;
  --orange-500: #E8502A;
  --orange-600: #C43A1A;
  --orange-700: #9E2D10;
  --orange-800: #7A2008;

  /* Blue ramp */
  --blue-100: #EBF4F8;
  --blue-200: #C2DDE8;
  --blue-300: #9AC6D8;
  --blue-400: #72AEC8;
  --blue-500: #2C6E8A;
  --blue-600: #1A4F65;
  --blue-700: #0E3548;
  --blue-800: #071E2C;

  /* Semantic UI mappings */
  --bg-page:      #FAFAF8;
  --bg-surface:   #FFFFFF;
  --bg-surface-2: #F5F2EE;
  --text-primary:   #0D0D0D;
  --text-secondary: #6E6E6E;
  --text-tertiary:  #B8B8B8;
  --border-default: #F0F0F0;
  --border-strong:  #B8B8B8;

  /* Border radius */
  --radius:    6px;
  --radius-lg: 12px;
  --radius-pill: 100px;
}
```

### Colors — Dark mode (`[data-theme="dark"]`)

```css
[data-theme="dark"] {
  --bg-page:      #0D0D0D;
  --bg-surface:   #1A1A1A;
  --bg-surface-2: #242424;
  --text-primary:   #F0F0F0;
  --text-secondary: #B8B8B8;
  --text-tertiary:  #6E6E6E;
  --border-default: #2A2A2A;
  --border-strong:  #3D3D3D;
  --primary:        #F07A5C;   /* Lighten primary for dark bg contrast */
  --primary-light:  #FF9A7A;
  --primary-dark:   #E8502A;
  --warm-gray:      #2A2520;
  --surface-1:      #1E1C1A;
  --surface-2:      #242220;
}
```

### Typography

Font duy nhất: **Google Sans Flex** (variable font, CDN Google Fonts).

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Google+Sans+Flex:ital,wdth,wght@0,75..125,100..700;1,75..125,100..700&display=swap" rel="stylesheet">
```

| Token CSS | Size | Weight | Line-height | Letter-spacing | Usage |
|-----------|------|--------|-------------|----------------|-------|
| `--text-display` | 72px | 800 | 1.0 | -0.04em | Hero heading chính |
| `--text-h1` | 56px | 700 | 1.05 | -0.03em | Page title, section hero |
| `--text-h2` | 40px | 700 | 1.1 | -0.02em | Section heading |
| `--text-h3` | 32px | 600 | 1.2 | -0.01em | Sub-section, card title |
| `--text-h4` | 24px | 600 | 1.25 | 0 | Card heading |
| `--body-l` | 18px | 400 | 1.6 | 0 | Lead paragraph |
| `--body-m` | 16px | 400 | 1.6 | 0 | Body text mặc định |
| `--body-s` | 14px | 400 | 1.65 | 0 | Secondary body |
| `--caption` | 12px | 400 | 1.4 | 0 | Caption, meta, timestamp |
| `--label` | 11px | 700 | 1.0 | +0.08em | Nav items, tags (uppercase) |

**Responsive type (dùng clamp hoặc media queries):**
| Role | Mobile | Tablet | Desktop | Wide |
|------|--------|--------|---------|------|
| Display | 40px | 56px | 72px | 80px |
| H1 | 30px | 40px | 56px | 60px |
| H2 | 22px | 30px | 40px | 44px |
| H3 | 18px | 22px | 28px | 28px |
| Body | 14px | 14px | 16px | 16px |

### Spacing System (base 4px)

| Token | Value | Usage |
|-------|-------|-------|
| `--space-1` | 4px | 2xs |
| `--space-2` | 8px | xs |
| `--space-3` | 12px | sm |
| `--space-4` | 16px | md |
| `--space-6` | 24px | lg |
| `--space-8` | 32px | xl |
| `--space-12` | 48px | 2xl |
| `--space-16` | 64px | 3xl |
| `--space-24` | 96px | 4xl |
| `--space-32` | 128px | 5xl |
| `--section-pad` | 96px desktop / 64px tablet / 48px mobile | Section vertical padding |

### Grid System

| Breakpoint | Columns | Gutter | Margin | Max width |
|------------|---------|--------|--------|-----------|
| Mobile (<768px) | 4 | 16px | 16px | 100% |
| Tablet (768–1023px) | 8 | 24px | 32px | 100% |
| Desktop (1024–1439px) | 12 | 32px | 64px | 1320px |
| Wide (1440px+) | 12 | 32px | 120px | 1440px |

Nav height: 60px desktop / 48px mobile.

---

## Logo Usage Rules

| Nền | Logo variant |
|-----|-------------|
| Nền trắng / sáng (light mode) | `sia-logo.png` (màu cam) |
| Nền tối / dark mode | `sia-logo-white.png` (trắng) |
| Nền màu cam (primary bg) | `sia-logo-white.png` (trắng) |
| Nền xám trung tính | `sia-logo-black.png` (đen) |

Logo phải được bọc trong thẻ `<a href="/">` với `aria-label="SIA Innovation Marketing Agency"`.  
Kích thước tối thiểu: height 32px. Đừng distort tỷ lệ.

---

## Dark / Light Mode

### Implementation

Dùng `data-theme` attribute trên thẻ `<html>`:

```html
<html lang="vi" data-theme="light">
```

Toggle bằng `theme.js`:

```js
// theme.js
const root = document.documentElement;
const stored = localStorage.getItem('sia-theme') || 'light';
root.setAttribute('data-theme', stored);

function toggleTheme() {
  const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
  root.setAttribute('data-theme', next);
  localStorage.setItem('sia-theme', next);
  // Swap logo src
  document.querySelectorAll('.logo-img').forEach(img => {
    img.src = next === 'dark' ? '/assets/images/logo/sia-logo-white.png' : '/assets/images/logo/sia-logo.png';
  });
}
```

CSS dark mode overrides dùng `[data-theme="dark"] { ... }` trong `variables.css`.

CSS transition mượt khi đổi theme:
```css
*, *::before, *::after {
  transition: background-color 0.2s ease, color 0.15s ease, border-color 0.15s ease;
}
```

---

## Animation Guidelines

### GSAP Setup (mọi trang đều cần)

```js
// main.js
gsap.registerPlugin(ScrollTrigger);

// Default ease
gsap.defaults({ ease: "power2.out", duration: 0.6 });

// Respect reduced motion
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (prefersReduced) gsap.globalTimeline.timeScale(0);
```

### Scroll-triggered fade-in (pattern chuẩn)

```js
gsap.utils.toArray('[data-animate]').forEach(el => {
  gsap.from(el, {
    scrollTrigger: { trigger: el, start: 'top 85%', toggleActions: 'play none none none' },
    y: 40, opacity: 0, duration: 0.7
  });
});
```

Thêm `data-animate` vào bất kỳ element nào cần fade-in khi scroll.

### Counter animation (stats section)

```js
gsap.utils.toArray('.counter').forEach(el => {
  const target = +el.dataset.target;
  gsap.from({ val: 0 }, {
    scrollTrigger: { trigger: el, start: 'top 80%' },
    val: target, duration: 1.5, ease: 'power1.out',
    onUpdate() { el.textContent = Math.round(this.targets()[0].val) + (el.dataset.suffix || ''); }
  });
});
```

### Horizontal scroll timeline

Dùng GSAP horizontal scroll pin cho "Timeline sự kiện" section:
```js
const timeline = document.querySelector('.event-timeline-track');
if (timeline) {
  gsap.to(timeline, {
    x: () => -(timeline.scrollWidth - window.innerWidth),
    ease: 'none',
    scrollTrigger: { trigger: '.event-timeline', pin: true, scrub: 1, end: () => '+=' + timeline.scrollWidth }
  });
}
```

### Swiper config mặc định

```js
// swiper-init.js
// Logo wall
new Swiper('.logo-wall-swiper', {
  loop: true, speed: 3000, autoplay: { delay: 0, disableOnInteraction: false },
  slidesPerView: 'auto', spaceBetween: 40,
  allowTouchMove: false, freeMode: true
});

// Case study cards
new Swiper('.cases-swiper', {
  slidesPerView: 1.2, spaceBetween: 16,
  breakpoints: { 768: { slidesPerView: 2.2 }, 1024: { slidesPerView: 3, spaceBetween: 24 } },
  pagination: { el: '.swiper-pagination', clickable: true }
});
```

---

## Pages & Components

> **Trạng thái v2:** Toàn bộ các trang đã được build xong. Khi chỉnh sửa: tôn trọng header/footer chung, design tokens trong `variables.css`, và hệ component trong `components.css`.

### Shared Header/Nav (mọi trang)

```html
<header class="site-header" x-data="{ mobileOpen: false, scrolled: false }"
        @scroll.window="scrolled = (window.scrollY > 40)">
  <nav class="nav-container" :class="{ 'nav-scrolled': scrolled }">
    <a href="/" class="nav-logo" aria-label="SIA Innovation Marketing Agency">
      <img class="logo-img" src="/assets/images/logo/sia-logo.png" height="36" alt="SIA">
    </a>
    <!-- Nav items, CTA, theme toggle, lang switch -->
    <button class="theme-toggle" onclick="toggleTheme()" aria-label="Toggle theme">☀/☾</button>
    <div class="lang-switch">
      <button onclick="setLang('vi')" class="lang-btn" :class="{ active: lang === 'vi' }">VI</button>
      <button onclick="setLang('en')" class="lang-btn" :class="{ active: lang === 'en' }">EN</button>
    </div>
  </nav>
</header>
```

### index.html — Sections thực tế (v2)

Thứ tự section hiện tại trên trang chủ (section id / class trong HTML):

| # | id | Section | Notes |
|---|-----|---------|-------|
| 1 | — | Header/Nav | Sticky, transparent → solid khi scroll |
| 2 | `hero` | `.section-hero` — Hero banner | Tagline, CTA, GSAP entrance |
| 3 | `services` | `.section` — 3 trụ cột | IMA · Event · Hub — icon + mô tả + link |
| 4 | `story` | `.section` — Câu chuyện SIA | Narrative về hành trình thương hiệu |
| 5 | `moments` | `.section` — Khoảnh khắc (SIA Moments) | Ảnh trong `assets/images/siamoment/` |
| 6 | `mvv` | `.section section--alt` — Mission · Vision · Values | Block nền khác (alt) |
| 7 | `cases` | `.section` — Case study nổi bật | Grid / Swiper case cards |
| 8 | `timeline-intro` | `.section section--tight` — Dẫn dắt timeline | Spacing gọn hơn (tight) |
| 9 | `timeline` | `.event-timeline` — Timeline sự kiện | GSAP horizontal scroll + dot status |
| 10 | `blog` | `.section` — Blog / Insight | 3 card mới nhất |
| 11 | `contact` | `.section section--alt` — Form liên hệ ngắn | Tên · Email · SĐT · Nhu cầu |
| 12 | — | Footer | Social, info, nav links |

> **Lưu ý:** Các section "Counter animation" (stats) và "Logo khách hàng" (logo wall) có mô tả pattern trong phần Animation Guidelines ở trên, nhưng **không còn xuất hiện trên index.html v2**. Counter/logo wall chỉ dùng ở các trang con (ví dụ `showcase.html` — block `.clients`) hoặc khi được yêu cầu thêm lại.

### Các trang con — Section map

| Trang | Sections chính (id) | Đặc điểm riêng |
|-------|---------------------|----------------|
| `services.html` | hero · pillars · principles | Hub trung gian dẫn về 3 trang services-* |
| `services-ima.html` | hero · deliverables · process · pricing | Pricing table component |
| `services-event.html` | hero · deliverables · process · pricing · past-events | Gallery sự kiện đã tổ chức |
| `services-hub.html` | hero · deliverables · industries · process · pricing | Industry selector / vertical cards |
| `showcase.html` | hero · cases · clients | Case grid + logo wall |
| `showcase-detail.html` | hero · intro · metrics · psr · body · gallery · related | KPI dashboard + media gallery (Swiper) |
| `blog.html` | hero · featured · articles · newsletter | Featured card + newsletter form |
| `blog-detail.html` | hero · body · related | Article + related posts |
| `community.html` | hero · sia-community · gen-why-attend · sponsors | Các chương trình: KOC Hub · Business Network · Next Gen |
| `contact.html` | hero · contact-form · office · faq | Form (Alpine) + office grid + FAQ accordion |
| `partnership.html` | hero · registration-form | Form đăng ký đối tác |
| `speaker.html` | form `speaker-form` (form-only) | Form đăng ký speaker — trang nhỏ nhất |
| `event-detail-a.html` | hero · form-section | Template A — KOC Hub Workshop #12 |
| `event-detail-b.html` | hero · form-section | Template B — Mega Livestream 5.5 |
| `about.html` | — | ⚠️ Stub — meta-refresh về index.html |

### Forms (quan trọng cho v2)

v2 có nhiều form đăng ký khác nhau — tất cả dùng **cùng hệ class `.form-*`** trong `components.css`:

- `.form-grid`, `.form-group`, `.form-field-group` — layout
- `.form-input`, `.form-select`, `.form-textarea`, `.form-label`, `.form-note` — field
- `.form-tab`, `.form-consent` — tab chuyển loại form + checkbox đồng ý
- FAQ accordion ở `contact.html` dùng Alpine `x-data` + `x-collapse` (không dùng `<details>`)

Khi thêm form mới: **tái sử dụng class hiện có**, đừng tạo class mới cùng mục đích.

### Components đã xây sẵn trong `components.css`

File này ~113KB / 4300+ dòng, đã có đầy đủ:
- `.blog-card__*` (media, title, excerpt, footer, category, metadata)
- `.case-card__*` (body, description, kpis, link)
- `.section-hero`, `.section-header`, `.section-eyebrow`, `.section--alt`, `.section--tight`
- `.timeline` (event timeline component)
- `.newsletter__form`
- `.faq-*` (FAQ accordion)
- `.office-grid`, `.office-card`
- `.community-*`, `.program-card`

**Trước khi tạo component mới, luôn grep `components.css` xem đã có chưa.**

---

## Bilingual (VI / EN)

Dùng `data-lang` attribute pattern trên text nodes:

```html
<p>
  <span data-lang="vi">Khám phá dịch vụ</span>
  <span data-lang="en" hidden>Explore Services</span>
</p>
```

```js
function setLang(lang) {
  localStorage.setItem('sia-lang', lang);
  document.querySelectorAll('[data-lang]').forEach(el => {
    el.hidden = el.dataset.lang !== lang;
  });
}
const savedLang = localStorage.getItem('sia-lang') || 'vi';
setLang(savedLang);
```

---

## Coding Conventions

### HTML
- Semantic tags: `<header>`, `<main>`, `<section>`, `<article>`, `<footer>`, `<nav>`
- Mỗi section có `id` theo slug: `id="hero"`, `id="why-sia"`, `id="timeline"`
- `lang` attribute: `<html lang="vi">` mặc định

### CSS — BEM-lite naming
- Block: `.section-hero`, `.card-case`, `.nav-primary`
- Element: `.card-case__title`, `.card-case__meta`
- Modifier: `.btn--outline`, `.card--featured`
- Chỉ dùng class, không dùng id cho styling
- CSS load order: `variables.css` → `base.css` → `components.css` → `animations.css` → page-specific inline `<style>`

### JS
- Không dùng jQuery
- Mọi DOM query đặt sau `DOMContentLoaded`
- GSAP animation trong `main.js`, theme logic trong `theme.js`, Swiper trong `swiper-init.js`

### Do / Don't (từ design system)
- **DO**: Button radius 6px (không bo tròn hoàn toàn, trừ CTA pill `border-radius: 100px`)
- **DO**: Dùng `var(--primary)` cho tất cả interactive elements
- **DON'T**: Không mix 2 màu accent cùng cấp
- **DON'T**: Không dùng font ngoài Google Sans Flex
- **DON'T**: Không border-radius > 12px trên card lớn
- **DON'T**: Không shadow quá đậm trên nền sáng

---

## CDN Links (copy vào mọi file HTML)

```html
<!-- Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Google+Sans+Flex:ital,wdth,wght@0,75..125,100..700;1,75..125,100..700&display=swap" rel="stylesheet">

<!-- Swiper CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">

<!-- Alpine.js (defer) -->
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>

<!-- GSAP + ScrollTrigger (before </body>) -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/ScrollTrigger.min.js"></script>
<!-- Swiper JS -->
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>

<!-- Project scripts -->
<script src="/assets/js/theme.js"></script>
<script src="/assets/js/swiper-init.js"></script>
<script src="/assets/js/main.js"></script>
```

---

## HTML Page Template

```html
<!DOCTYPE html>
<html lang="vi" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SIA Innovation Marketing Agency</title>
  <meta name="description" content="...">
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Google+Sans+Flex:ital,wdth,wght@0,75..125,100..700;1,75..125,100..700&display=swap" rel="stylesheet">
  <!-- Swiper CSS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">
  <!-- Project CSS -->
  <link rel="stylesheet" href="/assets/css/variables.css">
  <link rel="stylesheet" href="/assets/css/base.css">
  <link rel="stylesheet" href="/assets/css/components.css">
  <link rel="stylesheet" href="/assets/css/animations.css">
  <!-- Alpine.js -->
  <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>
<body>
  <!-- HEADER -->
  <header class="site-header">...</header>

  <!-- MAIN -->
  <main>
    <!-- page sections here -->
  </main>

  <!-- FOOTER -->
  <footer class="site-footer">...</footer>

  <!-- Scripts -->
  <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/ScrollTrigger.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
  <script src="/assets/js/theme.js"></script>
  <script src="/assets/js/swiper-init.js"></script>
  <script src="/assets/js/main.js"></script>
</body>
</html>
```
