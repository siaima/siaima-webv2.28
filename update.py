import re

html_a = open('event-detail-a.html').read()
new_main_a = """
<main>

<div class="container" style="padding-top:14px;padding-bottom:14px;">
  <a href="community.html" class="btn btn--ghost btn--sm">← <span data-lang="vi">Trở lại Sự kiện</span><span data-lang="en" hidden>Back to Events</span></a>
</div>

<!-- ═══════════ HERO ═══════════ -->
<section class="page-hero" id="hero">
  <div class="hero-bg"></div>
  <div class="container">
    <div class="page-hero__inner">
      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:20px;justify-content:center;" data-hero>
        <span class="service-chip" style="background:rgba(250,199,117,.12);color:#FAC775;border:none;">
          <span style="width:6px;height:6px;border-radius:50%;background:currentColor;display:inline-block;margin-right:6px;"></span>
          <span data-lang="vi">Sắp diễn ra</span><span data-lang="en" hidden>Coming soon</span>
        </span>
        <span class="service-chip">12 · 05 · 2026</span>
        <span class="service-chip">Innovation Hub · Hà Nội</span>
        <span class="service-chip" style="color:var(--primary);border-color:var(--primary);">Creator</span>
      </div>

      <h1 class="page-hero__title" data-hero>KOC Hub Workshop #12</h1>
      
      <p class="page-hero__subtitle" data-hero>
        <span data-lang="vi">Workshop training KOC — chủ đề "Storytelling for commerce" với 5 speakers trong ngành. Chi tiết chương trình sẽ sớm được cập nhật.</span>
        <span data-lang="en" hidden>KOC training workshop — "Storytelling for commerce" with 5 industry speakers. Program details coming soon.</span>
      </p>

      <div class="page-hero__actions" data-hero>
        <a href="#form-section" class="btn btn--primary btn--pill btn--lg">
          <span data-lang="vi">Trở thành đối tác / speaker</span>
          <span data-lang="en" hidden>Become a partner / speaker</span>
          <svg class="arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
        </a>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════ NOTICE BANNER ═══════════ -->
<div style="background:var(--color-warning-subtle,#FAEEDA);border-bottom:1px solid #F4C775;padding:14px 0;">
  <div class="container" style="display:flex;gap:12px;align-items:flex-start;font-size:13px;color:#854F0B;">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="flex-shrink:0;margin-top:1px;"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><circle cx="12" cy="16" r=".5" fill="currentColor"/></svg>
    <span data-lang="vi">Sự kiện đang trong giai đoạn lên kế hoạch. Thông tin chi tiết về lịch trình và diễn giả sẽ được cập nhật sớm.</span>
    <span data-lang="en" hidden>This event is in planning stage. Detailed agenda and speaker info will be updated soon.</span>
  </div>
</div>

<!-- ═══════════ ABOUT ═══════════ -->
<section class="section">
  <div class="container" style="max-width:800px; margin: 0 auto;">
    <div class="section-header text-left" style="margin-left: 0;" data-animate>
      <span class="section-eyebrow"><span data-lang="vi">Về sự kiện</span><span data-lang="en" hidden>About</span></span>
      <p class="text-lead mt-4">
        <span data-lang="vi">Workshop chuyên sâu dành cho KOC, content creator và brand marketer muốn nắm vững kỹ năng "Storytelling for commerce" — từ kịch bản đến conversion. Sự kiện quy tụ các speaker thực chiến từ hệ sinh thái TikTok Shop, Shopee và brand side.</span>
        <span data-lang="en" hidden>In-depth workshop for KOCs, content creators and brand marketers mastering "Storytelling for commerce" — from scripting to conversion.</span>
      </p>
    </div>

    <div class="grid grid-3" data-animate>
      <div class="deco-card">
        <div class="text-label mb-2"><span data-lang="vi">Hình thức</span><span data-lang="en" hidden>Format</span></div>
        <div class="text-h4"><span data-lang="vi">Workshop trực tiếp</span><span data-lang="en" hidden>In-person workshop</span></div>
      </div>
      <div class="deco-card">
        <div class="text-label mb-2"><span data-lang="vi">Đối tượng</span><span data-lang="en" hidden>Audience</span></div>
        <div class="text-h4">KOC, Brand, Agency</div>
      </div>
      <div class="deco-card">
        <div class="text-label mb-2"><span data-lang="vi">Quy mô dự kiến</span><span data-lang="en" hidden>Est. capacity</span></div>
        <div class="text-h4">~150 <span data-lang="vi">người</span><span data-lang="en" hidden>people</span></div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════ ORGANIZER ═══════════ -->
<section class="section section--alt">
  <div class="container" style="max-width:800px; margin: 0 auto;" data-animate>
    <span class="section-eyebrow mb-4"><span data-lang="vi">Tổ chức bởi</span><span data-lang="en" hidden>Organised by</span></span>
    <div class="deco-card flex" style="align-items: center; gap: 16px;">
      <div style="width:56px;height:56px;border-radius:12px;background:var(--black);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <img src="assets/images/logo/sia-logo-white.png" alt="SIA" height="28" style="object-fit:contain;">
      </div>
      <div>
        <div class="text-h4">SIA Innovation Marketing Agency</div>
        <div class="text-small mt-2"><span data-lang="vi">Đơn vị tổ chức sự kiện marketing hàng đầu tại Việt Nam</span><span data-lang="en" hidden>Vietnam's leading marketing event organiser</span></div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════ FORM ═══════════ -->
<section class="section" id="form-section">
  <div class="container">
    <div class="section-header" data-animate>
      <span class="section-eyebrow">
        <span data-lang="vi">Tham gia cùng chúng tôi</span>
        <span data-lang="en" hidden>Join us</span>
      </span>
      <h2>
        <span data-lang="vi">Trở thành <em style="color:var(--primary);font-style:italic">đối tác</em> hoặc speaker</span>
        <span data-lang="en" hidden>Become a <em style="color:var(--primary);font-style:italic">partner</em> or speaker</span>
      </h2>
      <p>
        <span data-lang="vi">Điền thông tin bên dưới — đội ngũ SIA sẽ liên hệ trong vòng 2 ngày làm việc.</span>
        <span data-lang="en" hidden>Fill in below — SIA team will respond within 2 business days.</span>
      </p>
    </div>

    <div class="contact-wrap" style="max-width: 800px; margin: 0 auto; display: block;" data-animate x-data="{tab:'sponsor'}">
      
      <!-- Tabs -->
      <div class="service-chips flex-center mb-6">
        <button class="service-chip" :class="{'active': tab==='sponsor'}" @click="tab='sponsor'"><span data-lang="vi">Đối tác tài trợ</span><span data-lang="en" hidden>Sponsor</span></button>
        <button class="service-chip" :class="{'active': tab==='speaker'}" @click="tab='speaker'">Speaker</button>
        <button class="service-chip" :class="{'active': tab==='media'}" @click="tab='media'">Media</button>
      </div>

      <form class="contact-form" style="width: 100%;" onsubmit="return handleFormA(event)">
        <div class="form-row">
          <div class="form-group">
            <label class="form-label"><span data-lang="vi">Họ và tên</span><span data-lang="en" hidden>Full name</span> *</label>
            <input class="form-input" type="text" required placeholder="Nguyễn Văn A">
          </div>
          <div class="form-group">
            <label class="form-label"><span data-lang="vi">Chức vụ</span><span data-lang="en" hidden>Job title</span> *</label>
            <input class="form-input" type="text" required placeholder="Marketing Manager">
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label class="form-label"><span data-lang="vi">Công ty / Thương hiệu</span><span data-lang="en" hidden>Company</span> *</label>
            <input class="form-input" type="text" required placeholder="Tên công ty">
          </div>
          <div class="form-group">
            <label class="form-label">Email *</label>
            <input class="form-input" type="email" required placeholder="name@company.com">
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label class="form-label"><span data-lang="vi">Số điện thoại</span><span data-lang="en" hidden>Phone</span></label>
            <input class="form-input" type="tel" placeholder="0901 234 567">
          </div>
          <div class="form-group">
            <label class="form-label"><span data-lang="vi">Ngân sách dự kiến</span><span data-lang="en" hidden>Budget</span></label>
            <select class="form-input" style="appearance: auto;">
              <option value=""><span data-lang="vi">Chọn mức ngân sách</span></option>
              <option><span data-lang="vi">Dưới 50 triệu</span></option>
              <option>50 – 150 triệu</option>
              <option><span data-lang="vi">Trên 150 triệu</span></option>
            </select>
          </div>
        </div>
        <div class="form-group">
          <label class="form-label"><span data-lang="vi">Mục tiêu & kỳ vọng</span><span data-lang="en" hidden>Goals & expectations</span></label>
          <textarea class="form-textarea" rows="4" placeholder="Chia sẻ ngắn về mục tiêu của bạn khi tham gia sự kiện này..."></textarea>
        </div>
        
        <p class="text-caption mt-4"><span data-lang="vi">Thông tin của bạn được bảo mật và chỉ dùng để liên hệ về sự kiện này.</span><span data-lang="en" hidden>Your info is confidential and used only for this event.</span></p>
        
        <div class="form-actions mt-6">
          <button type="submit" class="btn btn--primary btn--pill btn--lg">
            <span data-lang="vi">Gửi thông tin</span><span data-lang="en" hidden>Submit</span>
            <svg class="arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </button>
        </div>
      </form>
    </div>
  </div>
</section>

</main>
"""
# Replace everything between the first <main> and last </main>
html_a = re.sub(r'<main>.*?</main>', new_main_a, html_a, flags=re.DOTALL)
open('event-detail-a.html', 'w').write(html_a)


html_b = open('event-detail-b.html').read()
new_main_b = """
<main>

<div class="container" style="padding-top:14px;padding-bottom:14px;">
  <a href="community.html" class="btn btn--ghost btn--sm">← <span data-lang="vi">Trở lại Sự kiện</span><span data-lang="en" hidden>Back to Events</span></a>
</div>

<!-- ═══════════ HERO B ═══════════ -->
<section class="page-hero" id="hero">
  <div class="hero-bg"></div>
  <div class="container">
    <div class="page-hero__inner">
      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:20px;justify-content:center;" data-hero>
        <span class="service-chip" style="background:rgba(29,158,117,.15);color:#5DCAA5;border:none;">
          <span style="width:6px;height:6px;border-radius:50%;background:currentColor;display:inline-block;margin-right:6px;"></span>
          <span data-lang="vi">Đang mở đăng ký</span><span data-lang="en" hidden>Registration open</span>
        </span>
        <span class="service-chip">05 · 05 · 2026</span>
        <span class="service-chip">Studio SIA · Q10, TP.HCM</span>
        <span class="service-chip" style="color:var(--primary);border-color:var(--primary);">E-Commerce</span>
      </div>

      <h1 class="page-hero__title" data-hero>Mega Livestream 5.5</h1>
      
      <p class="page-hero__subtitle" data-hero>
        <span data-lang="vi">Livestream nhãn hàng + creator trên TikTok Shop — flagship campaign Q2/2026. Kết nối 30+ brand và 80+ creator trong 1 ngày.</span>
        <span data-lang="en" hidden>Brand + creator livestream on TikTok Shop — flagship Q2/2026 campaign connecting 30+ brands and 80+ creators.</span>
      </p>

      <div class="grid grid-4 text-center mt-6 mb-8" data-hero>
        <div><div class="text-display" style="color:var(--primary);">300+</div><div class="text-label mt-2"><span data-lang="vi">Khách tham dự</span><span data-lang="en" hidden>Attendees</span></div></div>
        <div><div class="text-display" style="color:var(--primary);">30+</div><div class="text-label mt-2">Brands</div></div>
        <div><div class="text-display" style="color:var(--primary);">80+</div><div class="text-label mt-2">Creators</div></div>
        <div><div class="text-display" style="color:var(--primary);"><span data-lang="vi">Miễn phí</span><span data-lang="en" hidden>Free</span></div><div class="text-label mt-2"><span data-lang="vi">Phí tham dự</span><span data-lang="en" hidden>Entry fee</span></div></div>
      </div>

      <div class="page-hero__actions" data-hero>
        <a href="#form-section" class="btn btn--primary btn--pill btn--lg">
          <span data-lang="vi">Đăng ký tham dự</span><span data-lang="en" hidden>Register now</span>
          <svg class="arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
        </a>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════ ABOUT ═══════════ -->
<section class="section">
  <div class="container" style="max-width:800px; margin: 0 auto;">
    <div class="section-header text-left" style="margin-left: 0;" data-animate>
      <span class="section-eyebrow"><span data-lang="vi">Về sự kiện</span><span data-lang="en" hidden>About</span></span>
      <p class="text-lead mt-4">
        <span data-lang="vi">Mega Livestream 5.5 là sự kiện thương mại điện tử lớn nhất Q2/2026 do SIA tổ chức, kết nối trực tiếp nhãn hàng và creator trong cùng một không gian. Gồm panel thảo luận buổi sáng và session kết nối 1-1 buổi chiều.</span>
        <span data-lang="en" hidden>Mega Livestream 5.5 is SIA's largest Q2/2026 e-commerce event connecting brands and creators. Morning panel + afternoon 1-1 matching session.</span>
      </p>
      <div class="service-chips mt-4">
        <span class="service-chip">TikTok Shop</span>
        <span class="service-chip">Livestream commerce</span>
        <span class="service-chip">Brand × Creator</span>
        <span class="service-chip">Campaign planning</span>
      </div>
    </div>

    <div class="grid grid-3 mt-6" data-animate>
      <div class="deco-card">
        <div class="text-label mb-2"><span data-lang="vi">Thời gian</span><span data-lang="en" hidden>Time</span></div>
        <div class="text-h4">9:00 – 18:00</div>
      </div>
      <div class="deco-card">
        <div class="text-label mb-2"><span data-lang="vi">Phí tham dự</span><span data-lang="en" hidden>Fee</span></div>
        <div class="text-h4 text-primary"><span data-lang="vi">Miễn phí</span><span data-lang="en" hidden>Free</span></div>
      </div>
      <div class="deco-card">
        <div class="text-label mb-2"><span data-lang="vi">Hình thức</span><span data-lang="en" hidden>Format</span></div>
        <div class="text-h4"><span data-lang="vi">Trực tiếp + Livestream</span><span data-lang="en" hidden>In-person + Livestream</span></div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════ SPEAKERS ═══════════ -->
<section class="section section--alt">
  <div class="container" style="max-width:800px; margin: 0 auto;">
    <span class="section-eyebrow mb-6" data-animate><span data-lang="vi">Diễn giả</span><span data-lang="en" hidden>Speakers</span></span>
    
    <div class="grid grid-2 mt-4" data-animate>
      <div class="deco-card flex" style="align-items: center; gap: 16px;">
        <div style="width:56px;height:56px;border-radius:50%;background:var(--bg-surface-2);border:1px solid var(--border-default);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:18px;color:var(--primary);flex-shrink:0;">TN</div>
        <div><div class="text-h4">Trần Ngọc Anh</div><div class="text-small mt-1">Head of Commerce · Brand X</div></div>
      </div>
      <div class="deco-card flex" style="align-items: center; gap: 16px;">
        <div style="width:56px;height:56px;border-radius:50%;background:var(--bg-surface-2);border:1px solid var(--border-default);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:18px;color:var(--primary);flex-shrink:0;">ML</div>
        <div><div class="text-h4">Minh Lê</div><div class="text-small mt-1">TikTok Shop · Partnership Lead</div></div>
      </div>
      <div class="deco-card flex" style="align-items: center; gap: 16px;">
        <div style="width:56px;height:56px;border-radius:50%;background:var(--bg-surface-2);border:1px solid var(--border-default);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:18px;color:var(--primary);flex-shrink:0;">HT</div>
        <div><div class="text-h4">Hà Trương</div><div class="text-small mt-1">Founder · Creator Studio HCM</div></div>
      </div>
      <div class="deco-card flex" style="align-items: center; gap: 16px;">
        <div style="width:56px;height:56px;border-radius:50%;background:var(--bg-surface-2);border:1px solid var(--border-default);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:18px;color:var(--primary);flex-shrink:0;">PD</div>
        <div><div class="text-h4">Phúc Đặng</div><div class="text-small mt-1">CMO · Skincare Brand</div></div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════ SCHEDULE ═══════════ -->
<section class="section">
  <div class="container" style="max-width:800px; margin: 0 auto;">
    <span class="section-eyebrow mb-6" data-animate><span data-lang="vi">Lịch trình</span><span data-lang="en" hidden>Schedule</span></span>
    
    <div class="milestones mt-4" data-animate>
      <div class="milestone">
        <div class="milestone__year">09:00</div>
        <div class="milestone__body">
          <div class="milestone__dot"></div>
          <div class="milestone__title"><span data-lang="vi">Đón tiếp & networking</span><span data-lang="en" hidden>Welcome & networking</span></div>
          <div class="milestone__desc"><span data-lang="vi">Check-in, coffee, kết nối tự do</span><span data-lang="en" hidden>Check-in, coffee, free networking</span></div>
        </div>
      </div>
      <div class="milestone">
        <div class="milestone__year">09:30</div>
        <div class="milestone__body">
          <div class="milestone__dot"></div>
          <div class="milestone__title">Panel: Livestream commerce 2026</div>
          <div class="milestone__desc">4 speakers, moderated Q&A</div>
        </div>
      </div>
      <div class="milestone">
        <div class="milestone__year">13:00</div>
        <div class="milestone__body">
          <div class="milestone__dot"></div>
          <div class="milestone__title">Brand × Creator matching session</div>
          <div class="milestone__desc"><span data-lang="vi">Gặp gỡ 1-1, pitch, ký kết hợp tác</span><span data-lang="en" hidden>1-1 meetings, pitch, partnership signing</span></div>
        </div>
      </div>
      <div class="milestone">
        <div class="milestone__year" style="color:var(--text-secondary);">17:00</div>
        <div class="milestone__body">
          <div class="milestone__dot" style="border-color:var(--border-strong);"></div>
          <div class="milestone__title">Closing & drinks</div>
          <div class="milestone__desc"><span data-lang="vi">Tổng kết, kết nối tự do</span><span data-lang="en" hidden>Wrap-up, free networking</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════ ORGANIZER ═══════════ -->
<section class="section section--alt">
  <div class="container" style="max-width:800px; margin: 0 auto;" data-animate>
    <span class="section-eyebrow mb-4"><span data-lang="vi">Tổ chức bởi</span><span data-lang="en" hidden>Organised by</span></span>
    <div class="deco-card flex" style="align-items: center; gap: 16px;">
      <div style="width:56px;height:56px;border-radius:12px;background:var(--black);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <img src="assets/images/logo/sia-logo-white.png" alt="SIA" height="28" style="object-fit:contain;">
      </div>
      <div>
        <div class="text-h4">SIA Innovation Marketing Agency</div>
        <div class="text-small mt-2"><span data-lang="vi">Đơn vị tổ chức sự kiện marketing hàng đầu tại Việt Nam</span><span data-lang="en" hidden>Vietnam's leading marketing event organiser</span></div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════ FORM B ═══════════ -->
<section class="section" id="form-section">
  <div class="container">
    <div class="section-header" data-animate>
      <span class="section-eyebrow">
        <span data-lang="vi">Đăng ký tham dự</span>
        <span data-lang="en" hidden>Register now</span>
      </span>
      <h2>
        <span data-lang="vi">Giữ <em style="color:var(--primary);font-style:italic">chỗ</em> của bạn</span>
        <span data-lang="en" hidden>Secure your <em style="color:var(--primary);font-style:italic">spot</em></span>
      </h2>
      <p>
        <span data-lang="vi">Chỗ có giới hạn. Xác nhận sẽ được gửi qua email ngay sau khi đăng ký.</span>
        <span data-lang="en" hidden>Spots are limited. Confirmation will be sent via email immediately after registration.</span>
      </p>
    </div>

    <div class="contact-wrap" style="max-width: 800px; margin: 0 auto; display: block;" data-animate>
      <form class="contact-form" style="width: 100%;" onsubmit="return handleFormB(event)">
        <div class="form-row">
          <div class="form-group">
            <label class="form-label"><span data-lang="vi">Họ và tên</span><span data-lang="en" hidden>Full name</span> *</label>
            <input class="form-input" type="text" required placeholder="Nguyễn Văn A">
          </div>
          <div class="form-group">
            <label class="form-label">Email *</label>
            <input class="form-input" type="email" required placeholder="name@email.com">
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label class="form-label"><span data-lang="vi">Số điện thoại</span><span data-lang="en" hidden>Phone</span> *</label>
            <input class="form-input" type="tel" required placeholder="0901 234 567">
          </div>
          <div class="form-group">
            <label class="form-label"><span data-lang="vi">Công ty / Thương hiệu</span><span data-lang="en" hidden>Company</span></label>
            <input class="form-input" type="text" placeholder="(Không bắt buộc)">
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label class="form-label"><span data-lang="vi">Vai trò của bạn</span><span data-lang="en" hidden>Your role</span> *</label>
            <select class="form-input" style="appearance: auto;" required>
              <option value=""><span data-lang="vi">Chọn vai trò</span></option>
              <option>Brand / Marketer</option>
              <option>Creator / KOC</option>
              <option>Agency</option>
              <option>Media</option>
              <option><span data-lang="vi">Khác</span></option>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label"><span data-lang="vi">Bạn biết sự kiện qua</span><span data-lang="en" hidden>How did you hear</span></label>
            <select class="form-input" style="appearance: auto;">
              <option value=""><span data-lang="vi">Chọn nguồn</span></option>
              <option>Facebook / Instagram</option>
              <option>TikTok</option>
              <option><span data-lang="vi">Bạn bè giới thiệu</span></option>
              <option>Email SIA</option>
              <option><span data-lang="vi">Khác</span></option>
            </select>
          </div>
        </div>
        
        <p class="text-caption mt-4"><span data-lang="vi">Thông tin của bạn được bảo mật và chỉ dùng để xác nhận tham dự sự kiện.</span><span data-lang="en" hidden>Your info is used only to confirm attendance.</span></p>
        
        <div class="form-actions mt-6">
          <button type="submit" class="btn btn--primary btn--pill btn--lg">
            <span data-lang="vi">Xác nhận đăng ký</span><span data-lang="en" hidden>Confirm registration</span>
            <svg class="arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </button>
        </div>
      </form>
    </div>
  </div>
</section>

</main>
"""
html_b = re.sub(r'<main>.*?</main>', new_main_b, html_b, flags=re.DOTALL)
open('event-detail-b.html', 'w').write(html_b)

print("Update completed successfully.")
