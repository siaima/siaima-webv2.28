import re

with open("community.html", "r", encoding="utf-8") as f:
    content = f.read()

# Match from </script> down to <div class="gen-stats-grid" data-stagger>
pattern = re.compile(r'(</script>).*?(<div class="gen-stats-grid" data-stagger>)', re.DOTALL)

def replacer(match):
    # Ensure we only remove the garbage if it contains "SEP 2023" or similar old data
    inner = match.group(0)
    if "SEP 2023" in inner or "GenAI Summit" in inner:
        return match.group(1) + '\n\n    ' + match.group(2)
    return inner

new_content = pattern.sub(replacer, content)

with open("community.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Timeline garbage fixed.")
