import os

css_content = """

/* ==========================================================================
   GEN COMMUNITY SECTIONS (SIA THEME)
   ========================================================================== */

/* ── TIMELINE ── */
.gen-timeline {
  display: flex;
  gap: 24px;
  overflow-x: auto;
  padding-bottom: 24px;
  position: relative;
  -webkit-overflow-scrolling: touch;
  margin-top: 40px;
}
.gen-timeline::-webkit-scrollbar {
  height: 4px;
}
.gen-timeline::-webkit-scrollbar-track {
  background: var(--bg-surface-1);
}
.gen-timeline::-webkit-scrollbar-thumb {
  background: var(--border-default);
  border-radius: 4px;
}

.gen-timeline::before {
  content: '';
  position: absolute;
  top: 15px; /* aligns with dots */
  left: 0;
  right: 0;
  height: 2px;
  background: var(--border-default);
  z-index: 0;
}

.gen-timeline-item {
  min-width: 260px;
  flex: 1;
  position: relative;
  z-index: 1;
  background: var(--bg-surface-1);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  padding: 24px;
  margin-top: 30px; /* space for dot */
}

.gen-timeline-dot {
  position: absolute;
  top: -36px;
  left: 24px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--primary);
  border: 2px solid var(--bg-default);
}
.gen-timeline-dot--live {
  background: var(--semantic-success, #2A8A4A);
  box-shadow: 0 0 0 4px rgba(42, 138, 74, 0.2);
}

.gen-timeline-date {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: var(--primary);
  text-transform: uppercase;
  margin-bottom: 8px;
}

.gen-timeline-title {
  font-size: 16px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 4px;
}

.gen-timeline-sub {
  font-size: 12px;
  color: var(--text-secondary);
  margin-bottom: 12px;
}

.gen-timeline-desc {
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.5;
  margin-bottom: 16px;
}

.gen-timeline-link {
  font-size: 11px;
  font-weight: 700;
  color: var(--secondary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

/* ── STATS GRID ── */
.gen-stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  margin: 48px 0;
}
@media (max-width: 1024px) {
  .gen-stats-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
  .gen-stats-grid { grid-template-columns: 1fr; }
}

.gen-stat-card {
  background: var(--bg-surface-1);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  padding: 32px 24px;
}
.gen-stat-val {
  font-family: var(--font-display);
  font-size: 40px;
  font-weight: 800;
  color: var(--primary);
  line-height: 1;
  margin-bottom: 8px;
  letter-spacing: -0.02em;
}
.gen-stat-title {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text-primary);
  margin-bottom: 8px;
}
.gen-stat-desc {
  font-size: 12px;
  color: var(--text-secondary);
  line-height: 1.5;
}

/* ── HORIZONTAL BAR CHARTS ── */
.gen-chart-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  margin-bottom: 48px;
}
@media (max-width: 900px) {
  .gen-chart-container { grid-template-columns: 1fr; gap: 32px; }
}

.gen-chart-card {
  background: var(--bg-surface-1);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  padding: 32px;
}
.gen-chart-header {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--secondary);
  margin-bottom: 24px;
}

.gen-bar-row {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 16px;
}
.gen-bar-label {
  width: 140px;
  font-size: 12px;
  font-weight: 500;
  color: var(--text-primary);
  flex-shrink: 0;
}
.gen-bar-track {
  flex: 1;
  height: 24px;
  background: var(--bg-surface-2);
  border-radius: 4px;
  position: relative;
  overflow: hidden;
}
.gen-bar-fill {
  height: 100%;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 8px;
  font-size: 10px;
  font-weight: 700;
  color: white;
}
.gen-chart-note {
  font-size: 11px;
  color: var(--text-secondary);
  font-style: italic;
  margin-top: 24px;
  line-height: 1.5;
}

/* ── LOGO CATEGORIES ── */
.gen-logo-section {
  text-align: center;
  margin-top: 64px;
}
.gen-logo-title {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--primary);
  margin-bottom: 32px;
}

.gen-logo-category {
  margin-bottom: 40px;
}
.gen-logo-category-title {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text-secondary);
  margin-bottom: 16px;
}
.gen-logo-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 16px;
}
.gen-logo-item {
  background: var(--bg-surface-1);
  border: 1px solid var(--border-default);
  border-radius: var(--radius);
  padding: 12px 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 120px;
  height: 50px;
  font-size: 14px;
  font-weight: 600;
  color: var(--text-primary);
  transition: all 0.2s;
}
.gen-logo-item:hover {
  border-color: var(--primary);
  transform: translateY(-2px);
}
.gen-logo-item img {
  max-height: 24px;
  max-width: 100%;
  opacity: 0.8;
}

/* ── TABS (Why Attend) ── */
.gen-tabs {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding-bottom: 8px;
  margin-bottom: 40px;
  -webkit-overflow-scrolling: touch;
}
.gen-tabs::-webkit-scrollbar { display: none; }

.gen-tab-btn {
  background: transparent;
  border: 1px solid var(--border-default);
  border-radius: 100px;
  padding: 10px 20px;
  font-size: 13px;
  font-weight: 600;
  color: var(--text-secondary);
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 8px;
}
.gen-tab-btn:hover {
  background: var(--bg-surface-2);
  color: var(--text-primary);
}
.gen-tab-btn.active {
  background: var(--primary);
  color: white;
  border-color: var(--primary);
}

.gen-tab-content {
  display: grid;
  grid-template-columns: 1fr 380px;
  gap: 64px;
}
@media (max-width: 900px) {
  .gen-tab-content { grid-template-columns: 1fr; gap: 40px; }
}

.gen-tab-left h3 {
  font-family: var(--font-display);
  font-size: 40px;
  font-weight: 800;
  line-height: 1.1;
  color: var(--text-primary);
  margin-bottom: 16px;
  letter-spacing: -0.02em;
}
.gen-tab-left p {
  font-size: 16px;
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: 40px;
  max-width: 600px;
}
.gen-tab-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 16px;
}

/* ── CHECKLIST BOX ── */
.gen-checklist-box {
  background: var(--bg-surface-1);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  padding: 32px;
}
.gen-checklist-title {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--secondary);
  margin-bottom: 24px;
}
.gen-check-item {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
  font-size: 14px;
  font-weight: 500;
  color: var(--text-primary);
}
.gen-check-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  background: var(--bg-surface-2);
  border-radius: 4px;
  color: var(--primary);
}

/* ── SPEAKER GRID ── */
.gen-speaker-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 40px;
  flex-wrap: wrap;
  gap: 20px;
}
.gen-speaker-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}
@media (max-width: 1024px) {
  .gen-speaker-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
  .gen-speaker-grid { grid-template-columns: 1fr; }
}

.gen-speaker-card {
  background: var(--bg-surface-1);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  padding: 24px;
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
}

"""
with open('assets/css/components.css', 'a', encoding='utf-8') as f:
    f.write(css_content)

print("CSS appended to components.css")
