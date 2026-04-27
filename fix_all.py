import glob
import re

# FIX 4 & FIX 5: Remove dropdown from nav & Fix footer contact
# We will do this across all HTML files
dropdown_pattern = re.compile(r'<div class="nav-dropdown(?:\s+nav-dropdown--active)?"[^>]*>.*?</div>\s*</div>', re.DOTALL)
footer_address_pattern = re.compile(r'<li>14 Ngõ Bệ, Tân Bình</li>')

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix 4: Dropdown
    is_active = file in ['services.html', 'services-ima.html', 'services-event.html', 'services-hub.html']
    active_class = " active" if is_active else ""
    replacement = f"""<a class="nav-item{active_class}" href="services.html">
        <span data-lang="vi">Dịch vụ</span>
        <span data-lang="en" hidden>Services</span>
      </a>"""
    content = dropdown_pattern.sub(replacement, content)
    
    # Fix 5: Footer address (Make it consistent with other links)
    content = footer_address_pattern.sub(r'<li><a href="https://maps.google.com/?q=14+Ngõ+Bệ,+Tân+Bình" target="_blank" rel="noopener">14 Ngõ Bệ, Tân Bình</a></li>', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# FIX 1: blog.html duplicate menu
with open("blog.html", "r", encoding="utf-8") as f:
    blog_content = f.read()

# We need to remove the stray lines 118-128
# The pattern starts after </div> of mobile-menu
stray_pattern = re.compile(r'(<div class="mobile-menu" id="mobileMenu">.*?</div>)\s*<a class="nav-item" href="services-ima\.html">SIA IMA</a>.*?</div>', re.DOTALL)
blog_content = stray_pattern.sub(r'\1', blog_content)
with open("blog.html", "w", encoding="utf-8") as f:
    f.write(blog_content)


# FIX 2: Remove milestones from index.html
with open("index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

# Find and remove the section with id="milestones"
milestone_pattern = re.compile(r'<!-- ═══════════ 04 MILESTONES ═══════════ -->.*?<section class="section" id="milestones">.*?</section>', re.DOTALL)
idx_content = milestone_pattern.sub('', idx_content)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx_content)


# FIX 3: Blog tags on one row
# Add CSS for .filter-chips to components.css
css_addition = """
/* Fix .filter-chips layout */
.filter-chips {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
  gap: 12px;
  -webkit-overflow-scrolling: touch;
  padding-bottom: 8px;
  justify-content: flex-start;
}
.filter-chips::-webkit-scrollbar {
  display: none;
}
@media (min-width: 768px) {
  .filter-chips {
    justify-content: center;
  }
}
"""
with open("assets/css/components.css", "a", encoding="utf-8") as f:
    f.write(css_addition)

print("All fixes applied successfully.")
