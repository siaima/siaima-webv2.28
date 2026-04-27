import re

with open("assets/css/components.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace .gen-speaker-card to .gen-speaker-tag
old_css = """
.gen-speaker-card {
  background: var(--bg-surface-1);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  padding: 16px;
  display: flex;
  gap: 12px;
  align-items: flex-start;
  transition: all 0.2s;
}
.gen-speaker-card:hover {
  transform: translateY(-4px);
  border-color: var(--primary);
  box-shadow: 0 12px 24px rgba(0,0,0,0.05);
}
.gen-speaker-avatar {
  width: 72px;
  height: 72px;
  border-radius: var(--radius);
  object-fit: cover;
  background: var(--bg-surface-2);
  flex-shrink: 0;
}
.gen-speaker-info {
  flex: 1;
}
.gen-speaker-name {
  font-size: 16px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 4px;
}
.gen-speaker-title {
  font-size: 12px;
  color: var(--text-secondary);
  margin-bottom: 2px;
}
.gen-speaker-company {
  font-size: 12px;
  font-weight: 600;
  color: var(--secondary);
  margin-bottom: 8px;
}
.gen-speaker-tag {
  display: inline-block;
  font-size: 10px;
  font-weight: 600;
  padding: 4px 8px;
  background: var(--bg-surface-2);
  border-radius: 4px;
  color: var(--text-secondary);
}"""

new_css = """
.gen-speaker-card {
  background: var(--bg-surface-1);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  padding: 20px;
  display: flex;
  gap: 16px;
  align-items: center;
  transition: all 0.2s;
}
.gen-speaker-card:hover {
  transform: translateY(-4px);
  border-color: var(--primary);
  box-shadow: 0 12px 24px rgba(0,0,0,0.05);
}
.gen-speaker-avatar {
  width: 96px;
  height: 96px;
  border-radius: var(--radius-md);
  object-fit: cover;
  background: var(--bg-surface-2);
  flex-shrink: 0;
  border: 1px solid var(--border-default);
  padding: 2px;
}
.gen-speaker-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.gen-speaker-name {
  font-size: 16px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 2px;
}
.gen-speaker-title {
  font-size: 12px;
  color: var(--text-secondary);
  margin-bottom: 2px;
}
.gen-speaker-company {
  font-size: 12px;
  font-weight: 600;
  color: var(--secondary);
  margin-bottom: 12px;
}
.gen-speaker-tag {
  display: inline-flex;
  align-items: center;
  font-size: 10px;
  font-weight: 600;
  padding: 4px 10px;
  background: transparent;
  border: 1px solid var(--border-strong);
  border-radius: 100px;
  color: var(--text-primary);
  width: fit-content;
}"""

if old_css.strip() in css:
    css = css.replace(old_css.strip(), new_css.strip())
    with open("assets/css/components.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("CSS updated successfully")
else:
    print("Old CSS block not found! Trying regex.")
    
