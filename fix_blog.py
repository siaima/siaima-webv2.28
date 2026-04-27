import re

with open("blog.html", "r", encoding="utf-8") as f:
    content = f.read()

correct_mobile_menu = """
<div class="mobile-menu" id="mobileMenu">
  <a class="nav-item" href="index.html"><span data-lang="vi">Về SIA IMA</span><span data-lang="en" hidden>About SIA</span></a>
  <div class="nav-group">
    <div class="nav-group__label"><span data-lang="vi">Dịch vụ</span><span data-lang="en" hidden>Services</span></div>
    <a class="nav-item" href="services.html"><span data-lang="vi">Tổng quan dịch vụ</span><span data-lang="en" hidden>Services Overview</span></a>
    <a class="nav-item" href="services-ima.html">SIA IMA</a>
    <a class="nav-item" href="services-event.html">SIA Event</a>
    <a class="nav-item" href="services-hub.html">SIA Hub</a>
  </div>
  <a class="nav-item" href="community.html"><span data-lang="vi">Cộng đồng</span><span data-lang="en" hidden>Community</span></a>
  <a class="nav-item" href="showcase.html">Showcase</a>
  <a class="nav-item active" href="blog.html">Blog</a>
  <a class="nav-item" href="contact.html"><span data-lang="vi">Liên hệ</span><span data-lang="en" hidden>Contact</span></a>
  <div class="mobile-actions">
    <a href="contact.html" class="btn btn--primary btn--pill btn--lg"><span data-lang="vi">Liên hệ ngay</span><span data-lang="en" hidden>Contact us</span></a>
  </div>
</div>
"""

# Replace everything from <div class="mobile-menu" id="mobileMenu"> up to right before <main x-data=...
pattern = re.compile(r'<div class="mobile-menu" id="mobileMenu">.*?(?=<main)', re.DOTALL)
new_content = pattern.sub(correct_mobile_menu + '\n', content)

with open("blog.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("blog.html mobile menu fixed.")
