import html.parser
import sys

class HTMLValidator(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.line = 0

    def handle_starttag(self, tag, attrs):
        if tag not in ['img', 'br', 'hr', 'input', 'meta', 'link', 'source', 'polyline', 'line', 'circle', 'path', 'rect', 'polygon']:
            self.tags.append((tag, self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag not in ['img', 'br', 'hr', 'input', 'meta', 'link', 'source', 'polyline', 'line', 'circle', 'path', 'rect', 'polygon']:
            if not self.tags:
                print(f"Error: unmatched end tag </{tag}> at line {self.getpos()[0]}")
                return
            last_tag, line = self.tags.pop()
            if last_tag != tag:
                print(f"Error: expected </{last_tag}> but got </{tag}> at line {self.getpos()[0]}")
                self.tags.append((last_tag, line)) # put it back
                # Pop until we find it
                for i in range(len(self.tags)-1, -1, -1):
                    if self.tags[i][0] == tag:
                        self.tags.pop(i)
                        break

with open("community.html", "r", encoding="utf-8") as f:
    html_content = f.read()

v = HTMLValidator()
v.feed(html_content)
if v.tags:
    print(f"Unclosed tags at end: {v.tags}")
else:
    print("All tags matched!")
