import re

with open("community.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Icons
# Find <div class="community-card__icon" style="..."> and replace with <div class="pillar-card__icon">
html = re.sub(r'<div class="community-card__icon"[^>]*>', r'<div class="pillar-card__icon">', html)


# 2. Remove old partners section
html = re.sub(r'<!-- ═══════════ 04 LOGO WALL THEO NHÓM ═══════════ -->\s*<section class="section" id="partners">.*?</section>', '', html, flags=re.DOTALL)


# 3. Remove old events section
html = re.sub(r'<!-- ═══════════ 03 TIMELINE SỰ KIỆN ═══════════ -->\s*<section class="section section--tight section--alt" id="events">.*?</section>', '', html, flags=re.DOTALL)


# 4. Rewrite GenAI Community to SIA Community
new_gen_community_header = """<!-- ═══════════ NEW SECTION 1: GEN COMMUNITY ═══════════ -->
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
    </div>"""
html = re.sub(r'<!-- ═══════════ NEW SECTION 1: GEN COMMUNITY ═══════════ -->\s*<section class="section" id="gen-community">\s*<div class="container">\s*<div class="section-header" data-animate>.*?</div>', new_gen_community_header, html, flags=re.DOTALL)

# 4.1 Timeline replacement
new_timeline = """
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
      document.addEventListener('DOMContentLoaded', () => {
        const tl = document.getElementById('community-timeline');
        if(tl) {
          setInterval(() => {
            if(tl.scrollLeft + tl.clientWidth >= tl.scrollWidth - 10) {
              tl.scrollTo({ left: 0, behavior: 'smooth' }); // reset to start
            } else {
              tl.scrollBy({ left: 320, behavior: 'smooth' }); // scroll one card
            }
          }, 3000);
        }
      });
    </script>"""
html = re.sub(r'<div class="gen-timeline" data-animate>.*?</div>', new_timeline, html, flags=re.DOTALL)

# 4.2 Stats replacement
new_stats = """
    <div class="gen-stats-grid" data-stagger>
      <div class="gen-stat-card" data-stagger-item>
        <div class="gen-stat-val">1.500+</div>
        <div class="gen-stat-title">CREATORS & KOCs</div>
        <div class="gen-stat-desc">
          <span data-lang="vi">Tham gia mạng lưới Affiliate & Social Commerce</span>
          <span data-lang="en" hidden>Active in Affiliate & Social Commerce network</span>
        </div>
      </div>
      <div class="gen-stat-card" data-stagger-item>
        <div class="gen-stat-val">50+</div>
        <div class="gen-stat-title">CHUYÊN GIA & DIỄN GIẢ</div>
        <div class="gen-stat-desc">
          <span data-lang="vi">Đồng hành trong các diễn đàn & workshop</span>
          <span data-lang="en" hidden>Partners in forums & workshops</span>
        </div>
      </div>
      <div class="gen-stat-card" data-stagger-item>
        <div class="gen-stat-val">30+</div>
        <div class="gen-stat-title">TRƯỜNG ĐẠI HỌC</div>
        <div class="gen-stat-desc" style="margin-top:8px;">
          <span data-lang="vi">Kết nối qua các CLB Marketing sinh viên</span>
          <span data-lang="en" hidden>Connected via Student Marketing Clubs</span>
        </div>
      </div>
      <div class="gen-stat-card" data-stagger-item>
        <div class="gen-stat-val">500+</div>
        <div class="gen-stat-title">THƯƠNG HIỆU</div>
        <div class="gen-stat-desc" style="margin-top:8px;">
          <span data-lang="vi">Đã hợp tác & triển khai chiến dịch cùng SIA</span>
          <span data-lang="en" hidden>Partnered & launched campaigns with SIA</span>
        </div>
      </div>
    </div>"""
html = re.sub(r'<div class="gen-stats-grid" data-stagger>.*?</div>\s*(?=<div class="gen-chart-container")', new_stats, html, flags=re.DOTALL)

# 4.3 Charts replacement
new_charts = """
    <div class="gen-chart-container" data-animate>
      <!-- ROLE CHART -->
      <div class="gen-chart-card">
        <div class="gen-chart-header">
          <span data-lang="vi">PHÂN BỔ THEO VAI TRÒ</span>
          <span data-lang="en" hidden>COMMUNITY BY ROLE</span>
        </div>
        
        <div class="gen-bar-row">
          <div class="gen-bar-label">Creators / KOCs</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 45%; background:var(--primary);">45%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">Students & Next Gen</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 25%; background:var(--secondary-light);">25%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">Marketers & Managers</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 15%; background:var(--secondary);">15%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">Founders & C-Level</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 10%; background:var(--primary-dark);">10%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">Others</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 5%; background:var(--border-strong); color:var(--text-secondary);">5%</div></div>
        </div>
        
        <div class="gen-chart-note">
          <span data-lang="vi">* Dữ liệu ước tính dựa trên tương tác các chiến dịch và sự kiện cộng đồng của SIA.</span>
          <span data-lang="en" hidden>* Estimated data based on SIA's campaigns and community event interactions.</span>
        </div>
      </div>

      <!-- SECTOR CHART -->
      <div class="gen-chart-card">
        <div class="gen-chart-header">
          <span data-lang="vi">LĨNH VỰC HOẠT ĐỘNG CHÍNH</span>
          <span data-lang="en" hidden>KEY ACTIVE SECTORS</span>
        </div>
        
        <div class="gen-bar-row">
          <div class="gen-bar-label">FMCG & Beauty</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 40%; background:var(--primary);">40%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">Tech & Electronics</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 25%; background:var(--secondary-light);">25%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">E-commerce Platforms</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 20%; background:var(--secondary);">20%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">F&B & Lifestyle</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 10%; background:var(--primary-dark);">10%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">Others</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 5%; background:var(--border-strong); color:var(--text-secondary);">5%</div></div>
        </div>
        
        <div class="gen-chart-note">
          <span data-lang="vi">* Cơ cấu lĩnh vực của đối tác và nhãn hàng đồng hành cùng SIA.</span>
          <span data-lang="en" hidden>* Sector breakdown of SIA's partners and partner brands.</span>
        </div>
      </div>
    </div>"""
html = re.sub(r'<div class="gen-chart-container" data-animate>.*?</div>\s*(?=<!-- LOGO CATEGORIES -->)', new_charts, html, flags=re.DOTALL)

# 4.4 Logos replacement
new_logos = """
    <!-- LOGO CATEGORIES -->
    <div class="gen-logo-section" data-animate>
      <div class="gen-logo-title">
        <span data-lang="vi">ĐỐI TÁC ĐỒNG HÀNH & NỀN TẢNG</span>
        <span data-lang="en" hidden>PARTNERS & PLATFORMS</span>
      </div>
      
      <div class="gen-logo-category">
        <div class="gen-logo-category-title">BRANDS & PLATFORMS</div>
        <div class="gen-logo-grid">
          <div class="gen-logo-item">Shopee</div>
          <div class="gen-logo-item">TikTok Shop</div>
          <div class="gen-logo-item">L'Oréal</div>
          <div class="gen-logo-item">Unilever</div>
          <div class="gen-logo-item">Samsung</div>
          <div class="gen-logo-item">Meta</div>
        </div>
      </div>

      <div class="gen-logo-category">
        <div class="gen-logo-category-title">CREATOR AGENCIES & MCNS</div>
        <div class="gen-logo-grid">
          <div class="gen-logo-item">Metub</div>
          <div class="gen-logo-item">Schannel</div>
          <div class="gen-logo-item">MCV Network</div>
          <div class="gen-logo-item">WebTV Asia</div>
          <div class="gen-logo-item">Yeah1</div>
          <div class="gen-logo-item">Vulcan</div>
        </div>
      </div>

      <div class="gen-logo-category">
        <div class="gen-logo-category-title">UNIVERSITIES & CLUBS</div>
        <div class="gen-logo-grid">
          <div class="gen-logo-item">RMIT University</div>
          <div class="gen-logo-item">UEH</div>
          <div class="gen-logo-item">FTU</div>
          <div class="gen-logo-item">HUTECH</div>
          <div class="gen-logo-item">Margroup</div>
          <div class="gen-logo-item">MarC</div>
        </div>
      </div>
    </div>"""
html = re.sub(r'<!-- LOGO CATEGORIES -->\s*<div class="gen-logo-section" data-animate>.*?</div>\s*</div>\s*</section>', new_logos + '\n  </div>\n</section>', html, flags=re.DOTALL)

with open("community.html", "w", encoding="utf-8") as f:
    f.write(html)

print("community.html sections 1-4 updated.")
