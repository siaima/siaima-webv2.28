import re

with open("community.html", "r", encoding="utf-8") as f:
    html = f.read()

new_why_attend = """<!-- ═══════════ NEW SECTION 2: WHY ATTEND & SPEAKERS ═══════════ -->
<section class="section section--alt" id="gen-why-attend">
  <div class="container">
    <div class="section-header" data-animate>
      <span class="section-eyebrow">// VÌ SAO CHỌN SIA</span>
      <h2>
        <span data-lang="vi">Tại sao nên đồng hành cùng <em style="color:var(--primary);font-style:italic">mạng lưới SIA</em></span>
        <span data-lang="en" hidden>Why partner with <em style="color:var(--primary);font-style:italic">SIA Network</em></span>
      </h2>
      <p>
        <span data-lang="vi">Dù bạn là một Creator đang tìm định hướng, một Brand Manager cần tối ưu chuyển đổi, hay Sinh viên muốn học hỏi thực chiến.</span>
        <span data-lang="en" hidden>Whether you are a Creator seeking direction, a Brand Manager optimizing conversion, or a Student wanting practical knowledge.</span>
      </p>
    </div>

    <!-- TABS -->
    <div x-data="{ tab: 'creators' }" data-animate>
      <div class="gen-tabs">
        <button class="gen-tab-btn" :class="{ 'active': tab === 'creators' }" @click="tab = 'creators'">Creators & KOCs</button>
        <button class="gen-tab-btn" :class="{ 'active': tab === 'brands' }" @click="tab = 'brands'">Brands & Platforms</button>
        <button class="gen-tab-btn" :class="{ 'active': tab === 'students' }" @click="tab = 'students'">Students & Next Gen</button>
        <button class="gen-tab-btn" :class="{ 'active': tab === 'experts' }" @click="tab = 'experts'">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>
          Chuyên gia
        </button>
      </div>

      <div class="gen-tab-content">
        <!-- LEFT CONTENT -->
        <div class="gen-tab-left">
          <div style="font-size:16px; font-weight:700; color:var(--primary); margin-bottom:16px; display:flex; align-items:center; gap:8px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>
            <span x-show="tab === 'creators'">Creators & KOCs</span>
            <span x-show="tab === 'brands'">Brands & Platforms</span>
            <span x-show="tab === 'students'">Students & Next Gen</span>
            <span x-show="tab === 'experts'">Chuyên gia</span>
          </div>
          
          <h3 x-show="tab === 'creators'">Bứt phá thu nhập với Social Commerce.</h3>
          <p x-show="tab === 'creators'">Trở thành một phần của KOC Hub với 1.500+ creators. Nhận booking đều đặn, tham gia Mega Livestream và được đào tạo kỹ năng thực chiến.</p>

          <h3 x-show="tab === 'brands'" style="display:none;">Tối ưu hóa chuyển đổi qua chiến dịch tích hợp.</h3>
          <p x-show="tab === 'brands'" style="display:none;">Kết nối với mạng lưới creator đa dạng và hệ sinh thái sự kiện của SIA. Triển khai các chiến dịch Mega Livestream mang lại GMV đột phá.</p>

          <h3 x-show="tab === 'students'" style="display:none;">Khởi đầu sự nghiệp Marketing vững chắc.</h3>
          <p x-show="tab === 'students'" style="display:none;">Tham gia giải case study toàn quốc, học hỏi từ CMOs hàng đầu và cơ hội thực tập trực tiếp tại các dự án lớn của SIA.</p>

          <h3 x-show="tab === 'experts'" style="display:none;">Chia sẻ tầm nhìn, dẫn dắt thế hệ mới.</h3>
          <p x-show="tab === 'experts'" style="display:none;">Đóng góp tiếng nói trong các diễn đàn Brand Innovation, chia sẻ case study tại các sự kiện ngành quy mô lớn với hàng nghìn người tham dự.</p>

          
          <div class="gen-tab-stats">
            <div class="gen-stat-card" style="padding: 24px;">
              <div class="gen-stat-val" style="font-size:24px;">150+</div>
              <div class="gen-stat-title" style="font-size:9px;">CHIẾN DỊCH / NĂM</div>
            </div>
            <div class="gen-stat-card" style="padding: 24px;">
              <div class="gen-stat-val" style="font-size:24px;">50B+</div>
              <div class="gen-stat-title" style="font-size:9px;">VND GMV LIVESTREAM</div>
            </div>
            <div class="gen-stat-card" style="padding: 24px;">
              <div class="gen-stat-val" style="font-size:24px;">10+</div>
              <div class="gen-stat-title" style="font-size:9px;">SỰ KIỆN QUY MÔ LỚN</div>
            </div>
          </div>
        </div>

        <!-- RIGHT CONTENT -->
        <div class="gen-tab-right">
          <div class="gen-checklist-box">
            <div class="gen-checklist-title">HỆ SINH THÁI ĐỐI TÁC</div>
            <div class="gen-check-item">
              <div class="gen-check-icon">✓</div> TikTok Shop
            </div>
            <div class="gen-check-item">
              <div class="gen-check-icon">✓</div> Shopee
            </div>
            <div class="gen-check-item">
              <div class="gen-check-icon">✓</div> Meta
            </div>
            <div class="gen-check-item">
              <div class="gen-check-icon">✓</div> L'Oréal
            </div>
            <div class="gen-check-item">
              <div class="gen-check-icon">✓</div> Unilever
            </div>
            <div class="gen-check-item">
              <div class="gen-check-icon">✓</div> Samsung
            </div>
            <div style="font-size:11px; color:var(--text-secondary); margin-top:32px;">+ Cùng hơn 500 thương hiệu hàng đầu.</div>
          </div>
        </div>
      </div>
    </div>

    <!-- SPEAKERS -->
    <div style="margin-top:80px;" data-animate>
      <div class="gen-speaker-header">
        <div>
          <span class="section-eyebrow">// CHUYÊN GIA ĐỒNG HÀNH</span>
          <h2 style="font-size:40px; margin-bottom:8px;">
            <span data-lang="vi">Gặp gỡ <em style="color:var(--primary);font-style:italic">Chuyên gia</em> & Diễn giả</span>
            <span data-lang="en" hidden>Meet our <em style="color:var(--primary);font-style:italic">Experts</em> & Speakers</span>
            <span style="font-size:12px; font-weight:600; font-style:normal; font-family:var(--font-body); letter-spacing:0.1em; color:var(--text-secondary); border:1px solid var(--border-default); padding:4px 12px; border-radius:100px; margin-left:12px; vertical-align:middle;">SIA NETWORK</span>
          </h2>
          <p style="font-size:14px; max-width:500px;">
            <span data-lang="vi">Hơn 50+ chuyên gia đến từ các nền tảng, agency và tập đoàn đa quốc gia đã chia sẻ kiến thức tại mạng lưới SIA.</span>
            <span data-lang="en" hidden>Over 50+ experts from platforms, agencies, and multinational corporations have shared knowledge across the SIA network.</span>
          </p>
        </div>
        <div>
          <a href="#" class="btn btn--outline btn--pill btn--sm">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right:4px; vertical-align:text-bottom;"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg>
            <span data-lang="vi">Trở thành Diễn giả →</span>
            <span data-lang="en" hidden>Become a Speaker →</span>
          </a>
        </div>
      </div>

      <div class="section-label" style="margin-bottom:16px;">
        <span data-lang="vi">DIỄN GIẢ TIÊU BIỂU</span>
        <span data-lang="en" hidden>FEATURED SPEAKERS</span>
      </div>
      <div class="gen-speaker-grid" style="margin-bottom:32px;">
        <!-- HÀNG 1 -->
        <div class="gen-speaker-card">
          <img src="https://i.pravatar.cc/150?u=12" class="gen-speaker-avatar" alt="Speaker 1">
          <div class="gen-speaker-info">
            <div class="gen-speaker-name">Nguyen Van A</div>
            <div class="gen-speaker-title">Marketing Director</div>
            <div class="gen-speaker-company">Unilever</div>
            <div class="gen-speaker-tag">Brand Strategy</div>
          </div>
        </div>
        <div class="gen-speaker-card">
          <img src="https://i.pravatar.cc/150?u=22" class="gen-speaker-avatar" alt="Speaker 2">
          <div class="gen-speaker-info">
            <div class="gen-speaker-name">Tran Thi B</div>
            <div class="gen-speaker-title">Head of Social Commerce</div>
            <div class="gen-speaker-company">TikTok Shop</div>
            <div class="gen-speaker-tag">Livestream Growth</div>
          </div>
        </div>
        <div class="gen-speaker-card">
          <img src="https://i.pravatar.cc/150?u=33" class="gen-speaker-avatar" alt="Speaker 3">
          <div class="gen-speaker-info">
            <div class="gen-speaker-name">Le Van C</div>
            <div class="gen-speaker-title">Founder & CEO</div>
            <div class="gen-speaker-company">Schannel</div>
            <div class="gen-speaker-tag">Creator Economy</div>
          </div>
        </div>
        
        <!-- HÀNG 2 -->
        <div class="gen-speaker-card">
          <img src="https://i.pravatar.cc/150?u=44" class="gen-speaker-avatar" alt="Speaker 4">
          <div class="gen-speaker-info">
            <div class="gen-speaker-name">Pham Thi D</div>
            <div class="gen-speaker-title">Creative Director</div>
            <div class="gen-speaker-company">Ogilvy</div>
            <div class="gen-speaker-tag">Integrated Campaign</div>
          </div>
        </div>
        <div class="gen-speaker-card">
          <img src="https://i.pravatar.cc/150?u=55" class="gen-speaker-avatar" alt="Speaker 5">
          <div class="gen-speaker-info">
            <div class="gen-speaker-name">Hoang Van E</div>
            <div class="gen-speaker-title">E-commerce Head</div>
            <div class="gen-speaker-company">Shopee</div>
            <div class="gen-speaker-tag">Mega Sales</div>
          </div>
        </div>
        <div class="gen-speaker-card">
          <img src="https://i.pravatar.cc/150?u=66" class="gen-speaker-avatar" alt="Speaker 6">
          <div class="gen-speaker-info">
            <div class="gen-speaker-name">Vo Thi F</div>
            <div class="gen-speaker-title">CMO</div>
            <div class="gen-speaker-company">L'Oréal</div>
            <div class="gen-speaker-tag">Beauty Marketing</div>
          </div>
        </div>

        <!-- HÀNG 3 -->
        <div class="gen-speaker-card">
          <img src="https://i.pravatar.cc/150?u=77" class="gen-speaker-avatar" alt="Speaker 7">
          <div class="gen-speaker-info">
            <div class="gen-speaker-name">Vu Van G</div>
            <div class="gen-speaker-title">Partner</div>
            <div class="gen-speaker-company">Metub Network</div>
            <div class="gen-speaker-tag">MCN Strategy</div>
          </div>
        </div>
        <div class="gen-speaker-card">
          <img src="https://i.pravatar.cc/150?u=88" class="gen-speaker-avatar" alt="Speaker 8">
          <div class="gen-speaker-info">
            <div class="gen-speaker-name">Truong Thi H</div>
            <div class="gen-speaker-title">Head of Marketing</div>
            <div class="gen-speaker-company">Samsung</div>
            <div class="gen-speaker-tag">Tech Branding</div>
          </div>
        </div>
        <div class="gen-speaker-card">
          <img src="https://i.pravatar.cc/150?u=99" class="gen-speaker-avatar" alt="Speaker 9">
          <div class="gen-speaker-info">
            <div class="gen-speaker-name">Dang Van I</div>
            <div class="gen-speaker-title">Director</div>
            <div class="gen-speaker-company">WebTV Asia</div>
            <div class="gen-speaker-tag">Content Production</div>
          </div>
        </div>

        <!-- HÀNG 4 -->
        <div class="gen-speaker-card">
          <img src="https://i.pravatar.cc/150?u=101" class="gen-speaker-avatar" alt="Speaker 10">
          <div class="gen-speaker-info">
            <div class="gen-speaker-name">Dinh Thi K</div>
            <div class="gen-speaker-title">Agency Lead</div>
            <div class="gen-speaker-company">Meta</div>
            <div class="gen-speaker-tag">Social Strategy</div>
          </div>
        </div>
        <div class="gen-speaker-card">
          <img src="https://i.pravatar.cc/150?u=111" class="gen-speaker-avatar" alt="Speaker 11">
          <div class="gen-speaker-info">
            <div class="gen-speaker-name">Ngo Van L</div>
            <div class="gen-speaker-title">Lecturer</div>
            <div class="gen-speaker-company">RMIT University</div>
            <div class="gen-speaker-tag">Academic Research</div>
          </div>
        </div>
        <div class="gen-speaker-card">
          <img src="https://i.pravatar.cc/150?u=121" class="gen-speaker-avatar" alt="Speaker 12">
          <div class="gen-speaker-info">
            <div class="gen-speaker-name">Bui Thi M</div>
            <div class="gen-speaker-title">Managing Director</div>
            <div class="gen-speaker-company">Yeah1</div>
            <div class="gen-speaker-tag">Media Ecosystem</div>
          </div>
        </div>
      </div>
      
    </div>
  </div>
</section>"""
html = re.sub(r'<!-- ═══════════ NEW SECTION 2: WHY ATTEND & SPEAKERS ═══════════ -->.*?</section>', new_why_attend, html, flags=re.DOTALL)

with open("community.html", "w", encoding="utf-8") as f:
    f.write(html)

print("community.html section 5 updated.")
