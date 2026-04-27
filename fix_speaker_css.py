import re

with open("assets/css/components.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace .gen-speaker-card properties
old_card = """.gen-speaker-card {
  background: var(--bg-surface-1);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  padding: 24px;
  display: flex;
  gap: 16px;
  align-items: center;
  transition: all 0.2s;
}"""
new_card = """.gen-speaker-card {
  background: var(--bg-surface-1);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  padding: 16px;
  display: flex;
  gap: 12px;
  align-items: flex-start;
  transition: all 0.2s;
}"""
css = css.replace(old_card, new_card)

with open("assets/css/components.css", "w", encoding="utf-8") as f:
    f.write(css)

print("CSS updated")
