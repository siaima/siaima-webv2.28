import glob
import re

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    is_active = file in ['services.html', 'services-ima.html', 'services-event.html', 'services-hub.html']
    active_class = " active" if is_active else ""
    replacement = f"""<a class="nav-item{active_class}" href="services.html"><span data-lang="vi">Dịch vụ</span><span data-lang="en" hidden>Services</span></a>"""
    
    # Use a tight regex to only capture the nav-group for services
    pattern = re.compile(r'<div class="nav-group">\s*<div class="nav-group__label">.*?</div>\s*<a[^>]*href="services.html"[^>]*>.*?</a>\s*<a[^>]*href="services-ima.html"[^>]*>.*?</a>\s*<a[^>]*href="services-event.html"[^>]*>.*?</a>\s*<a[^>]*href="services-hub.html"[^>]*>.*?</a>\s*</div>', re.DOTALL)
    
    new_content = pattern.sub(replacement, content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Mobile nav updated")
