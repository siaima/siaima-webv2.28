import re

with open("temp_header.txt", "r", encoding="utf-8") as f:
    header = f.read()
with open("temp_mobile_menu.txt", "r", encoding="utf-8") as f:
    mobile_menu = f.read()

# Make "Cộng đồng" active instead of "Trang chủ"
header = header.replace('<a class="nav-item active" href="index.html">', '<a class="nav-item" href="index.html">')
header = header.replace('<a class="nav-item" href="community.html">', '<a class="nav-item active" href="community.html">')

mobile_menu = mobile_menu.replace('<a class="nav-item active" href="index.html">', '<a class="nav-item" href="index.html">')
mobile_menu = mobile_menu.replace('<a class="nav-item" href="community.html">', '<a class="nav-item active" href="community.html">')

# Get the bottom part of community.html (from gen-stats-grid onwards)
with open("community.html", "r", encoding="utf-8") as f:
    content = f.read()

bottom_part = content[content.find('<div class="gen-stats-grid" data-stagger>'):]

new_content = f"""<!DOCTYPE html>
<html lang="vi" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cộng đồng · SIA Innovation Marketing Agency</title>
  <meta name="description" content="Khám phá hệ sinh thái cộng đồng của SIA: SIA KOC Hub, SIA Business Network và SIA Next Gen.">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Google+Sans+Flex:ital,wdth,wght@0,75..125,100..700;1,75..125,100..700&display=swap" rel="stylesheet">

  <!-- Swiper CSS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">

  <!-- Project CSS -->
  <link rel="stylesheet" href="assets/css/variables.css?v=8">
  <link rel="stylesheet" href="assets/css/base.css?v=8">
  <link rel="stylesheet" href="assets/css/components.css?v=8">
  <link rel="stylesheet" href="assets/css/animations.css?v=8">

  <!-- Alpine.js -->
  <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
  <script>
    (function () {{
      var t = localStorage.getItem('sia-theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
      document.documentElement.setAttribute('data-theme', t);
    }})();
  </script>
</head>
<body>

{header}

{mobile_menu}

<main>

<!-- 01 HERO -->
<section class="page-hero" id="hero">
  <div class="hero-bg"></div>
  <div class="container">
    <div class="page-hero__inner">
      <span class="section-eyebrow" data-hero><span data-lang="vi">Cộng đồng</span><span data-lang="en" hidden>Community</span></span>
      <h1 class="page-hero__title" data-hero>
        <span data-lang="vi">Kết nối để cùng <em style="color:var(--primary);font-style:italic">tăng trưởng</em> bền vững</span>
        <span data-lang="en" hidden>Connecting to <em style="color:var(--primary);font-style:italic">grow</em> sustainably together</span>
      </h1>
      <p class="page-hero__subtitle" data-hero>
        <span data-lang="vi">Hệ sinh thái kết nối Doanh nhân, Creator và Thế hệ trẻ (Sinh viên). Nơi hội tụ những nhà kiến tạo để cùng nhau chia sẻ, học hỏi và tạo ra giá trị mới cho thị trường.</span>
        <span data-lang="en" hidden>An ecosystem connecting Entrepreneurs, Creators, and the Next Generation (Students). A convergence point for creators to share, learn, and create new market value.</span>
      </p>

      <div class="community-stats" data-hero>
        <div class="community-stat">
          <div class="community-stat__num">1.5K<span>+</span></div>
          <div class="community-stat__label">
            <span data-lang="vi">Creators & KOCs</span><span data-lang="en" hidden>Creators & KOCs</span>
          </div>
        </div>
        <div class="community-stat">
          <div class="community-stat__num">50<span>+</span></div>
          <div class="community-stat__label">
            <span data-lang="vi">Chuyên gia & Diễn giả</span><span data-lang="en" hidden>Experts & Speakers</span>
          </div>
        </div>
        <div class="community-stat">
          <div class="community-stat__num">500<span>+</span></div>
          <div class="community-stat__label">
            <span data-lang="vi">Sinh viên & CLB</span><span data-lang="en" hidden>Students & Clubs</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════ 02 3 CỘNG ĐỒNG CHÍNH ═══════════ -->
<section class="section" id="communities">
  <div class="container">
    <div class="section-header" data-animate>
      <h2>
        <span data-lang="vi">Hệ sinh thái <em style="color:var(--primary);font-style:italic">3 mạng lưới</em> kết nối</span>
        <span data-lang="en" hidden>An ecosystem of <em style="color:var(--primary);font-style:italic">3 interconnected</em> networks</span>
      </h2>
    </div>

    <div class="community-grid" data-stagger>
      <!-- SIA KOC Hub -->
      <article class="community-card" data-stagger-item>
        <div class="pillar-card__icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
        </div>
        <h3 class="community-card__title">SIA KOC Hub</h3>
        <p class="community-card__desc">
          <span data-lang="vi">Mạng lưới 1.500+ KOL, KOC và Content Creators. Nơi ươm mầm tài năng, cung cấp campaign đều đặn và giải pháp tăng trưởng thu nhập.</span>
          <span data-lang="en" hidden>Network of 1,500+ KOLs, KOCs, and Content Creators. A place to nurture talent, provide regular campaigns, and solutions for income growth.</span>
        </p>
        <ul class="community-card__list">
          <li>Mega Livestream Campaign</li>
          <li>Affiliate & Social Commerce</li>
          <li>Creator Training Workshops</li>
        </ul>
      </article>

      <!-- SIA Business Network -->
      <article class="community-card" data-stagger-item>
        <div class="pillar-card__icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/></svg>
        </div>
        <h3 class="community-card__title">SIA Business Network</h3>
        <p class="community-card__desc">
          <span data-lang="vi">Cộng đồng dành riêng cho CMO, Brand Managers và Doanh nhân. Cập nhật xu hướng marketing mới nhất và case study thực chiến.</span>
          <span data-lang="en" hidden>Exclusive community for CMOs, Brand Managers, and Entrepreneurs. Stay updated with the latest marketing trends and practical case studies.</span>
        </p>
        <ul class="community-card__list">
          <li>Brand Innovation Forum</li>
          <li>Executive Networking</li>
          <li>Market Insight Reports</li>
        </ul>
      </article>

      <!-- SIA Next Gen -->
      <article class="community-card" data-stagger-item>
        <div class="pillar-card__icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/><path d="M8 14h.01M12 14h.01M16 14h.01M8 18h.01M12 18h.01"/></svg>
        </div>
        <h3 class="community-card__title">SIA Next Gen</h3>
        <p class="community-card__desc">
          <span data-lang="vi">Không gian đồng hành cùng các bạn Sinh viên và Câu lạc bộ Marketing. Định hướng nghề nghiệp và cơ hội thực tập, cọ xát thực tế.</span>
          <span data-lang="en" hidden>A companion space for Students and Marketing Clubs. Career orientation, internship opportunities, and practical exposure.</span>
        </p>
        <ul class="community-card__list">
          <li>University Talkshows</li>
          <li>Marketing Competitions</li>
          <li>Internship Programs</li>
        </ul>
      </article>
    </div>
  </div>
</section>

<!-- ═══════════ NEW SECTION 1: GEN COMMUNITY ═══════════ -->
<section class="section" id="sia-community">
  <div class="container">
    <div class="section-header" data-animate>
      <span class="section-eyebrow">// SIA ECOSYSTEM</span>
      <h2>
        <span data-lang="vi">Cộng đồng <em style="color:var(--primary);font-style:italic">SIA</em></span>
        <span data-lang="en" hidden>SIA <em style="color:var(--primary);font-style:italic">Community</em></span>
      </h2>
      <p>
        <span data-lang="vi">Hệ sinh thái hội tụ 1.500+ Creator, Chuyên gia và Doanh nhân — nơi kiến tạo giá trị, chia sẻ kiến thức và bứt phá doanh thu.</span>
        <span data-lang="en" hidden>An ecosystem of 1,500+ Creators, Experts, and Entrepreneurs — a place to create value, share knowledge, and breakthrough revenue.</span>
      </p>
    </div>

    <div class="gen-timeline" id="community-timeline" data-animate style="scroll-behavior: smooth;">
      <div class="gen-timeline-item" style="border-color:var(--primary);">
        <div class="gen-timeline-dot gen-timeline-dot--live"></div>
        <div class="gen-timeline-date" style="color:var(--primary)">05 · 05 · 2026</div>
        <div class="gen-timeline-title">Mega Livestream 5.5</div>
        <div class="gen-timeline-sub">Studio SIA · Q10</div>
        <div class="gen-timeline-desc">
          <span data-lang="vi">Livestream nhãn hàng + creator trên TikTok Shop — flagship campaign Q2/2026.</span>
          <span data-lang="en" hidden>Brand + creator livestream on TikTok Shop — flagship Q2/2026 campaign.</span>
        </div>
        <a href="#" class="gen-timeline-link">ĐANG DIỄN RA →</a>
      </div>
      <div class="gen-timeline-item">
        <div class="gen-timeline-dot"></div>
        <div class="gen-timeline-date">12 · 05 · 2026</div>
        <div class="gen-timeline-title">KOC Hub Workshop #12</div>
        <div class="gen-timeline-sub">Innovation Hub · HN</div>
        <div class="gen-timeline-desc">
          <span data-lang="vi">Workshop training KOC — chủ đề "Storytelling for commerce" với 5 speakers trong ngành.</span>
          <span data-lang="en" hidden>KOC training — "Storytelling for commerce" with 5 industry speakers.</span>
        </div>
        <a href="#" class="gen-timeline-link">ĐĂNG KÝ NGAY →</a>
      </div>
      <div class="gen-timeline-item">
        <div class="gen-timeline-dot"></div>
        <div class="gen-timeline-date">25 · 05 · 2026</div>
        <div class="gen-timeline-title">Brand Innovation Forum</div>
        <div class="gen-timeline-sub">JW Marriott · HCM</div>
        <div class="gen-timeline-desc">
          <span data-lang="vi">Diễn đàn cho CMO và brand leaders — insight về thị trường, case study và xu hướng 2026.</span>
          <span data-lang="en" hidden>Forum for CMOs and brand leaders — market insights, case studies and 2026 trends.</span>
        </div>
        <a href="#" class="gen-timeline-link">ĐĂNG KÝ NGAY →</a>
      </div>
      <div class="gen-timeline-item">
        <div class="gen-timeline-dot"></div>
        <div class="gen-timeline-date">15 · 07 · 2026</div>
        <div class="gen-timeline-title">Innovation Marketing Summit</div>
        <div class="gen-timeline-sub">GEM Center · HCM</div>
        <div class="gen-timeline-desc">
          <span data-lang="vi">Summit marketing lớn nhất năm của SIA — 2 ngày, 24 diễn giả, 800 khách mời ngành.</span>
          <span data-lang="en" hidden>SIA's biggest marketing summit — 2 days, 24 speakers, 800 industry attendees.</span>
        </div>
        <a href="#" class="gen-timeline-link">ĐẶT CHỖ SỚM →</a>
      </div>
      <div class="gen-timeline-item">
        <div class="gen-timeline-dot"></div>
        <div class="gen-timeline-date">20 · 08 · 2026</div>
        <div class="gen-timeline-title">Next Gen Marketers</div>
        <div class="gen-timeline-sub">RMIT University · HCM</div>
        <div class="gen-timeline-desc">
          <span data-lang="vi">Cuộc thi giải case study marketing quy mô toàn quốc dành cho sinh viên năm 3, 4.</span>
          <span data-lang="en" hidden>National marketing case study competition for junior and senior students.</span>
        </div>
        <a href="#" class="gen-timeline-link">TÌM HIỂU THÊM →</a>
      </div>
    </div>
    <script>
      document.addEventListener('DOMContentLoaded', () => {{
        const tl = document.getElementById('community-timeline');
        if(tl) {{
          setInterval(() => {{
            if(tl.scrollLeft + tl.clientWidth >= tl.scrollWidth - 10) {{
              tl.scrollTo({{ left: 0, behavior: 'smooth' }}); 
            }} else {{
              tl.scrollBy({{ left: 320, behavior: 'smooth' }}); 
            }}
          }}, 3000);
        }}
      }});
    </script>

{bottom_part}
"""

with open("community.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Recovered missing top part!")
