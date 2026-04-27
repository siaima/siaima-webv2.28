import html.parser
import glob

class HTMLValidator(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.line = 0

    def handle_starttag(self, tag, attrs):
        if tag not in ['img', 'br', 'hr', 'input', 'meta', 'link', 'source', 'polyline', 'line', 'circle', 'path', 'rect', 'polygon']:
            self.tags.append(tag)

    def handle_endtag(self, tag):
        if tag not in ['img', 'br', 'hr', 'input', 'meta', 'link', 'source', 'polyline', 'line', 'circle', 'path', 'rect', 'polygon']:
            if not self.tags:
                return
            last_tag = self.tags.pop()
            if last_tag != tag:
                self.tags.append(last_tag)
                for i in range(len(self.tags)-1, -1, -1):
                    if self.tags[i] == tag:
                        self.tags.pop(i)
                        break

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        html_content = f.read()
    v = HTMLValidator()
    v.feed(html_content)
    if v.tags:
        print(f"{file} has unclosed tags at end: {v.tags[-3:]}")
