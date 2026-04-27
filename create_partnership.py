import re

with open('contact.html', 'r', encoding='utf-8') as f:
    contact_html = f.read()

# Extract header
header_match = re.search(r'(.*?<main>)', contact_html, re.DOTALL)
if not header_match:
    print("Could not find header")
    exit(1)
header = header_match.group(1)
header = header.replace('<title>Liên hệ · SIA Innovation Marketing Agency</title>', '<title>Đăng ký Đối tác · SIA Innovation Marketing Agency</title>')

# Extract footer and scripts
footer_match = re.search(r'(</main>.*)', contact_html, re.DOTALL)
if not footer_match:
    print("Could not find footer")
    exit(1)
footer = footer_match.group(1)

# New Main content
main_content = """
<!-- ═══════════ 01 HERO ═══════════ -->
<section class="page-hero page-hero--contact" id="hero">
  <div class="hero-bg"></div>
  <div class="container">
    <div class="page-hero__inner">
      <div class="hero-eyebrow" data-hero>
        <span class="dot"></span>
        <span data-lang="vi">SIA Partnership 2026</span>
        <span data-lang="en" hidden>SIA Partnership 2026</span>
      </div>

      <h1 class="page-hero__title" data-hero>
        <span data-lang="vi">Đăng ký trở thành <em style="color:var(--primary);font-style:italic">Đối tác</em> của SIA</span>
        <span data-lang="en" hidden>Register to become an SIA <em style="color:var(--primary);font-style:italic">Partner</em></span>
      </h1>

      <p class="page-hero__subtitle" data-hero>
        <span data-lang="vi">Điểm qua các sự kiện gần đây: Hơn 150+ chiến dịch và sự kiện, quy tụ 10.000+ người tham dự cùng 500+ thương hiệu đồng hành. Vui lòng điền form bên dưới để đăng ký trở thành Diễn giả (Speaker), Nhà tài trợ (Sponsor), hoặc Đơn vị triển lãm (Exhibitor).</span>
        <span data-lang="en" hidden>Recent highlights: Over 150+ campaigns and events, gathering 10,000+ attendees and 500+ brands. Please fill out the form below to register as a Speaker, Sponsor, or Exhibitor.</span>
      </p>
    </div>
  </div>
</section>

<!-- ═══════════ 02 FORM ═══════════ -->
<section class="section section--alt" id="registration-form">
  <div class="container" style="max-width: 800px;">
    
    <div style="background: var(--bg-surface); padding: 40px; border-radius: var(--radius-lg); border: 1px solid var(--border-default); box-shadow: var(--shadow-sm);" data-animate>
      <h2 style="margin-bottom: 8px;"><span data-lang="vi">Thông tin đăng ký</span><span data-lang="en" hidden>Registration Info</span></h2>
      <p style="color: var(--text-secondary); margin-bottom: 32px;"><span data-lang="vi">Cảm ơn bạn đã quan tâm đến SIA. Vui lòng điền các thông tin dưới đây, chúng tôi sẽ phản hồi sớm nhất có thể!</span><span data-lang="en" hidden>Thank you for your interest. Please fill out the form below and we will get back to you soon!</span></p>

      <form class="contact-form" onsubmit="return handleContactSubmit(event)">
        <!-- Contact Info -->
        <h3 style="margin-bottom: 16px; font-size: 20px;"><span data-lang="vi">Thông tin liên lạc</span><span data-lang="en" hidden>Contact Info</span></h3>
        <div class="form-row">
          <div class="form-group">
            <label class="form-label">First Name *</label>
            <input class="form-input" type="text" required>
          </div>
          <div class="form-group">
            <label class="form-label">Last Name *</label>
            <input class="form-input" type="text" required>
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label class="form-label">Email Address *</label>
            <input class="form-input" type="email" required>
          </div>
          <div class="form-group">
            <label class="form-label">Phone Number</label>
            <input class="form-input" type="tel">
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">LinkedIn Profile</label>
          <input class="form-input" type="url" placeholder="https://linkedin.com/in/...">
        </div>

        <hr style="border:0; border-top: 1px solid var(--border-default); margin: 32px 0;">

        <!-- Business Info -->
        <h3 style="margin-bottom: 16px; font-size: 20px;"><span data-lang="vi">Thông tin doanh nghiệp</span><span data-lang="en" hidden>Business Info</span></h3>
        <div class="form-row">
          <div class="form-group">
            <label class="form-label">Company Name *</label>
            <input class="form-input" type="text" required>
          </div>
          <div class="form-group">
            <label class="form-label">Job Title *</label>
            <input class="form-input" type="text" required>
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Company Website *</label>
          <input class="form-input" type="url" required placeholder="https://...">
        </div>

        <hr style="border:0; border-top: 1px solid var(--border-default); margin: 32px 0;">

        <!-- Participation Role -->
        <h3 style="margin-bottom: 16px; font-size: 20px;"><span data-lang="vi">Vai trò tham gia</span><span data-lang="en" hidden>Participation Role</span></h3>
        <div class="form-group">
          <label class="form-label">What roles do you want to present:</label>
          <div style="display:flex; flex-direction:column; gap:8px;">
            <label style="display:flex; align-items:center; gap:8px;"><input type="checkbox" name="role" value="speaker"> Speaker</label>
            <label style="display:flex; align-items:center; gap:8px;"><input type="checkbox" name="role" value="exhibitor"> Exhibitor</label>
            <label style="display:flex; align-items:center; gap:8px;"><input type="checkbox" name="role" value="sponsor" checked> Sponsor</label>
          </div>
        </div>
        <p style="font-size:14px; color:var(--text-secondary); margin-bottom:16px;">If you are looking forward to becoming our sponsor, please check our <a href="#" style="color:var(--primary); text-decoration:underline;">Sponsor Deck</a> document for basic information.</p>
        
        <div style="background:var(--bg-surface-2); height: 200px; display:flex; align-items:center; justify-content:center; border-radius:var(--radius); border: 1px dashed var(--border-strong); margin-bottom: 32px;">
          <div style="background: rgba(0,0,0,0.5); color: #fff; padding: 8px 16px; border-radius: 4px; font-size: 14px;">Không có bản xem trước nào (No preview available)</div>
        </div>

        <hr style="border:0; border-top: 1px solid var(--border-default); margin: 32px 0;">

        <!-- Additional Information -->
        <div class="form-group">
          <label class="form-label" style="text-transform: none; letter-spacing: 0; font-size: 14px;">Would you be open to receiving Resumes for Job Applications to your organization/company during our event? *</label>
          <div style="display:flex; flex-direction:column; gap:8px; margin-top:8px;">
            <label style="display:flex; align-items:center; gap:8px;"><input type="radio" name="resumes" value="yes" required> Yes</label>
            <label style="display:flex; align-items:center; gap:8px;"><input type="radio" name="resumes" value="no" required> No</label>
            <label style="display:flex; align-items:center; gap:8px;"><input type="radio" name="resumes" value="discuss_later" required> Discuss Later</label>
          </div>
        </div>

        <div class="form-group" style="margin-top: 24px;">
          <label class="form-label" style="margin-bottom: 0;">Additional Information</label>
          <p style="font-size:12px; color:var(--text-secondary); margin-bottom:8px;">Feel free to leave your additional request here</p>
          <textarea class="form-textarea" rows="4"></textarea>
        </div>

        <div style="margin-top: 24px; border: 1px solid var(--border-default); padding: 12px; border-radius: 4px; display:inline-flex; background:var(--bg-surface);">
          <label style="display:flex; align-items:center; gap:12px; font-size:14px; cursor: pointer;">
            <input type="checkbox" required>
            <span>I'm not a robot</span>
            <img src="https://www.gstatic.com/recaptcha/api2/logo_48.png" height="24" alt="reCAPTCHA">
          </label>
        </div>

        <div class="form-actions" style="margin-top: 32px;">
          <button type="submit" class="btn btn--primary btn--pill btn--lg">
            Submit
            <svg class="arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </button>
          <p class="form-note">
            <span data-lang="vi">Chúng tôi sẽ phản hồi trong 24h làm việc.</span>
            <span data-lang="en" hidden>We'll reply within 24 business hours.</span>
          </p>
        </div>
      </form>

    </div>
  </div>
</section>
"""

with open('partnership.html', 'w', encoding='utf-8') as f:
    f.write(header + main_content + footer)

print("Created partnership.html successfully!")
