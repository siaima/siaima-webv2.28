import glob
import re

nav_group_pattern = re.compile(r'<div class="nav-group">.*?</div>\s*</div>', re.DOTALL)

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    is_active = file in ['services.html', 'services-ima.html', 'services-event.html', 'services-hub.html']
    active_class = " active" if is_active else ""
    replacement = f"""<a class="nav-item{active_class}" href="services.html">
    <span data-lang="vi">Dịch vụ</span>
    <span data-lang="en" hidden>Services</span>
  </a>"""
    
    # Wait, the regex `.*?</div>\s*</div>` might capture too much.
    # The nav-group ends with just one </div>. 
    # Let's write a safer regex for nav-group
