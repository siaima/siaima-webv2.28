import os
import re

html_to_inject = """
<!-- ═══════════ NEW SECTION 1: GEN COMMUNITY ═══════════ -->
<section class="section" id="gen-community">
  <div class="container">
    <div class="section-header" data-animate>
      <span class="section-eyebrow">// COMMUNITY</span>
      <h2>
        The GenAI <em style="color:var(--primary);font-style:italic">Community</em>
      </h2>
      <p>Built across 5 GenAI Summits since 2023. 79,000+ members across Silicon Valley's AI ecosystem.</p>
    </div>

    <div class="gen-timeline" data-animate>
      <div class="gen-timeline-item">
        <div class="gen-timeline-dot"></div>
        <div class="gen-timeline-date">SEP 2023</div>
        <div class="gen-timeline-title">GenAI Summit 2023</div>
        <div class="gen-timeline-sub">Santa Clara · 1 day</div>
        <div class="gen-timeline-desc">Aravind Srinivas | Perplexity, Co-F...<br>Arvind Jain | Glean, Founder & CEO</div>
        <a href="#" class="gen-timeline-link">VIEW EVENT SITE →</a>
      </div>
      <div class="gen-timeline-item">
        <div class="gen-timeline-dot"></div>
        <div class="gen-timeline-date">MAY 2024</div>
        <div class="gen-timeline-title">GenAI Summit 2024 SF</div>
        <div class="gen-timeline-sub">Palace of Fine Arts, SF · 3 days</div>
        <div class="gen-timeline-desc">Denis Yarats | Perplexity, Co-Foun...<br>Arvind Jain | Glean, Founder & CEO</div>
        <a href="#" class="gen-timeline-link">VIEW EVENT SITE →</a>
      </div>
      <div class="gen-timeline-item">
        <div class="gen-timeline-dot"></div>
        <div class="gen-timeline-date">NOV 2024</div>
        <div class="gen-timeline-title">GenAI Summit 2024 SC</div>
        <div class="gen-timeline-sub">Santa Clara · 3 days</div>
        <div class="gen-timeline-desc">Lip-Bu Tan | Intel, CEO<br>Vanessa Larco | Ex-NEA, Partner<br>Arvind Jain | Glean, Founder & CEO</div>
        <a href="#" class="gen-timeline-link">VIEW EVENT SITE →</a>
      </div>
      <div class="gen-timeline-item">
        <div class="gen-timeline-dot"></div>
        <div class="gen-timeline-date">JUL 2025</div>
        <div class="gen-timeline-title">GenAI Summit 2025</div>
        <div class="gen-timeline-sub">Santa Clara · 5 days</div>
        <div class="gen-timeline-desc">Jason Wei | Ex-OpenAI<br>Ed Oates | Oracle, Co-Founder<br>Tuhin Srivastava | Baseten, Co-Fou...<br>Arvind Jain | Glean, Founder & CEO</div>
        <a href="#" class="gen-timeline-link">VIEW EVENT SITE →</a>
      </div>
      <div class="gen-timeline-item">
        <div class="gen-timeline-dot"></div>
        <div class="gen-timeline-date">APR 2026</div>
        <div class="gen-timeline-title">GenAI Summit Paris 2026</div>
        <div class="gen-timeline-sub">STATION F, Paris · 1 day</div>
        <div class="gen-timeline-desc">Carol S. Scott | Microsoft<br>Michelle Lau | Alibaba<br>Barbara Grabiwoda | Publicis Grou...<br>Philippe Limantour | Microsoft<br>Thalie Farinaud | L'Oréal</div>
        <a href="#" class="gen-timeline-link">VIEW EVENT SITE →</a>
      </div>
      <div class="gen-timeline-item" style="border-color:var(--primary);">
        <div class="gen-timeline-dot gen-timeline-dot--live"></div>
        <div class="gen-timeline-date" style="color:var(--semantic-success)">JUL 18-19, 2026</div>
        <div class="gen-timeline-title">GenAI Summit 2026 SF</div>
        <div class="gen-timeline-sub">Palace of Fine Arts, SF · 2 days</div>
        <div class="gen-timeline-desc" style="color:var(--semantic-success); font-weight:600; font-size:11px; letter-spacing:0.1em; text-transform:uppercase;">● NOW BUILDING</div>
      </div>
    </div>

    <div class="gen-stats-grid" data-stagger>
      <div class="gen-stat-card" data-stagger-item>
        <div class="gen-stat-val">79,000+</div>
        <div class="gen-stat-title">COMMUNITY MEMBERS</div>
        <div class="gen-stat-desc">Verified community across AI, venture, enterprise, and academia</div>
      </div>
      <div class="gen-stat-card" data-stagger-item>
        <div class="gen-stat-val">40%+</div>
        <div class="gen-stat-title">FOUNDERS, EXECUTIVES & BUILDERS</div>
        <div class="gen-stat-desc">High-intent operators across startups, research, and enterprise</div>
      </div>
      <div class="gen-stat-card" data-stagger-item>
        <div class="gen-stat-val">30+</div>
        <div class="gen-stat-title">TOP UNIVERSITIES REPRESENTED</div>
        <div class="gen-stat-desc" style="margin-top:8px;">
          <img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Stanford_University_seal_2003.svg" height="20" style="margin-right:4px;">
          <img src="https://upload.wikimedia.org/wikipedia/commons/a/a1/Seal_of_University_of_California%2C_Berkeley.svg" height="20" style="margin-right:4px;">
        </div>
      </div>
      <div class="gen-stat-card" data-stagger-item>
        <div class="gen-stat-val">40+</div>
        <div class="gen-stat-title">FORTUNE 500 COMPANIES REPRESENTED</div>
        <div class="gen-stat-desc" style="margin-top:8px;">
          <span style="font-size:18px; font-weight:600;">G a ⊞</span>
        </div>
      </div>
    </div>

    <div class="gen-chart-container" data-animate>
      <!-- ROLE CHART -->
      <div class="gen-chart-card">
        <div class="gen-chart-header">COMMUNITY BY ROLE</div>
        
        <div class="gen-bar-row">
          <div class="gen-bar-label">Founders & CEOs</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 80%; background:var(--secondary);">21.1%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">C-Suite & Operators</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 55%; background:var(--primary-light);">14.8%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">Engineers & Builders</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 50%; background:var(--secondary-light);">14.5%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">VCs & Investors</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 45%; background:var(--semantic-success);">12.3%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">Managers & Leads</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 40%; background:var(--secondary);">10.9%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">Students & Academics</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 20%; background:var(--primary);">5%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">Researchers</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 15%; background:var(--primary-light);">4.2%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">Enterprise Leaders</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 10%; background:var(--semantic-success);">3.1%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">Other Roles</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 50%; background:var(--border-default); color:var(--text-secondary);">14.1%</div></div>
        </div>
        
        <div class="gen-chart-note">
          * Based on 79,366 community members with identified professional titles.<br>
          Display mix combines identified roles, summit attendee patterns, and broader ecosystem weighting.
        </div>
      </div>

      <!-- SECTOR CHART -->
      <div class="gen-chart-card">
        <div class="gen-chart-header">COMMUNITY BY SECTOR</div>
        
        <div class="gen-bar-row">
          <div class="gen-bar-label">Big Tech</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 90%; background:var(--secondary);">30%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">AI Companies</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 75%; background:var(--primary-light);">24%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">Venture & Investment</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 60%; background:var(--primary);">20%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">Enterprise & Fortune 500</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 50%; background:var(--semantic-success);">16%</div></div>
        </div>
        <div class="gen-bar-row">
          <div class="gen-bar-label">Universities & Research</div>
          <div class="gen-bar-track"><div class="gen-bar-fill" style="width: 30%; background:var(--secondary-light);">10%</div></div>
        </div>
        
        <div class="gen-chart-note">
          * Based on company and professional background data from 79,366 community members.<br>
          Sector distribution estimated from member company affiliations and role information across our community ecosystem.
        </div>
      </div>
    </div>

    <!-- LOGO CATEGORIES -->
    <div class="gen-logo-section" data-animate>
      <div class="gen-logo-title">COMMUNITY MEMBERS FROM</div>
      
      <div class="gen-logo-category">
        <div class="gen-logo-category-title">BIG TECH</div>
        <div class="gen-logo-grid">
          <div class="gen-logo-item">G Google</div>
          <div class="gen-logo-item">a Amazon</div>
          <div class="gen-logo-item">NVIDIA</div>
          <div class="gen-logo-item">Microsoft</div>
          <div class="gen-logo-item">Meta</div>
          <div class="gen-logo-item">Apple</div>
          <div class="gen-logo-item">Adobe</div>
          <div class="gen-logo-item">Salesforce</div>
          <div class="gen-logo-item">Oracle</div>
        </div>
      </div>

      <div class="gen-logo-category">
        <div class="gen-logo-category-title">AI COMPANIES</div>
        <div class="gen-logo-grid">
          <div class="gen-logo-item">OpenAI</div>
          <div class="gen-logo-item">Anthropic</div>
          <div class="gen-logo-item">Perplexity</div>
          <div class="gen-logo-item">Glean</div>
          <div class="gen-logo-item">Together AI</div>
          <div class="gen-logo-item">Pinecone</div>
        </div>
      </div>

      <div class="gen-logo-category">
        <div class="gen-logo-category-title">VC FIRMS</div>
        <div class="gen-logo-grid">
          <div class="gen-logo-item">Accel</div>
          <div class="gen-logo-item">a16z</div>
          <div class="gen-logo-item">NEA</div>
          <div class="gen-logo-item">Bessemer</div>
          <div class="gen-logo-item">IVP</div>
          <div class="gen-logo-item">Bain Capital</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════ NEW SECTION 2: WHY ATTEND & SPEAKERS ═══════════ -->
<section class="section section--alt" id="gen-why-attend">
  <div class="container">
    <div class="section-header" data-animate>
      <span class="section-eyebrow">// WHY ATTEND</span>
      <h2>
        Why Come to <em style="color:var(--primary);font-style:italic">GenAI Summit</em>
      </h2>
      <p>Whether you write checks, ship models, or deploy at scale — there's a reason this is the one AI event you can't miss.</p>
    </div>

    <!-- TABS -->
    <div x-data="{ tab: 'tech' }" data-animate>
      <div class="gen-tabs">
        <button class="gen-tab-btn" :class="{ 'active': tab === 'vcs' }" @click="tab = 'vcs'">VCs & Investors</button>
        <button class="gen-tab-btn" :class="{ 'active': tab === 'founders' }" @click="tab = 'founders'">Founders & Startups</button>
        <button class="gen-tab-btn" :class="{ 'active': tab === 'enterprise' }" @click="tab = 'enterprise'">Enterprise & Sponsors</button>
        <button class="gen-tab-btn" :class="{ 'active': tab === 'students' }" @click="tab = 'students'">Students & Academics</button>
        <button class="gen-tab-btn" :class="{ 'active': tab === 'tech' }" @click="tab = 'tech'">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>
          Tech Enthusiasts
        </button>
        <button class="gen-tab-btn" :class="{ 'active': tab === 'bigtech' }" @click="tab = 'bigtech'">Big Tech & AI Teams</button>
      </div>

      <div class="gen-tab-content">
        <!-- LEFT CONTENT -->
        <div class="gen-tab-left">
          <div style="font-size:16px; font-weight:700; color:var(--primary); margin-bottom:16px; display:flex; align-items:center; gap:8px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>
            Tech Enthusiasts
          </div>
          <h3>See the future before it ships.</h3>
          <p>Join 79,000+ community members across 5 editions. Live demos, open-source showcases, and keynotes from the people building frontier AI.</p>
          
          <div class="gen-tab-stats">
            <div class="gen-stat-card" style="padding: 24px;">
              <div class="gen-stat-val" style="font-size:24px;">79,000+</div>
              <div class="gen-stat-title" style="font-size:9px;">COMMUNITY MEMBERS</div>
            </div>
            <div class="gen-stat-card" style="padding: 24px;">
              <div class="gen-stat-val" style="font-size:24px;">5</div>
              <div class="gen-stat-title" style="font-size:9px;">EDITIONS SINCE 2023</div>
            </div>
            <div class="gen-stat-card" style="padding: 24px;">
              <div class="gen-stat-val" style="font-size:24px;">1,100+</div>
              <div class="gen-stat-title" style="font-size:9px;">ENGINEERS & DEVELOPERS</div>
            </div>
          </div>
        </div>

        <!-- RIGHT CONTENT -->
        <div class="gen-tab-right">
          <div class="gen-checklist-box">
            <div class="gen-checklist-title">BUILT BY THE COMMUNITY</div>
            <div class="gen-check-item">
              <div class="gen-check-icon">✓</div> OpenAI
            </div>
            <div class="gen-check-item">
              <div class="gen-check-icon">✓</div> Meta
            </div>
            <div class="gen-check-item">
              <div class="gen-check-icon">✓</div> Google
            </div>
            <div class="gen-check-item">
              <div class="gen-check-icon">✓</div> Anthropic
            </div>
            <div class="gen-check-item">
              <div class="gen-check-icon">✓</div> NVIDIA
            </div>
            <div class="gen-check-item">
              <div class="gen-check-icon">✓</div> Perplexity
            </div>
            <div style="font-size:11px; color:var(--text-secondary); margin-top:32px;">+ 79,000 members across 5 editions</div>
          </div>
        </div>
      </div>
    </div>

    <!-- SPEAKERS -->
    <div style="margin-top:80px;" data-animate>
      <div class="gen-speaker-header">
        <div>
          <span class="section-eyebrow">// WHO'S ON STAGE</span>
          <h2 style="font-size:40px; margin-bottom:8px;">
            World-Class <em style="color:var(--primary);font-style:italic">Speakers</em>
            <span style="font-size:12px; font-weight:600; font-style:normal; font-family:var(--font-body); letter-spacing:0.1em; color:var(--text-secondary); border:1px solid var(--border-default); padding:4px 12px; border-radius:100px; margin-left:12px; vertical-align:middle;">PAST SPEAKERS</span>
          </h2>
          <p style="font-size:14px; max-width:500px;">400+ speakers from OpenAI, Google, Meta, Microsoft, and the most ambitious AI startups.</p>
        </div>
        <div>
          <a href="#" class="btn btn--outline btn--pill btn--sm">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right:4px; vertical-align:text-bottom;"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg>
            Speak at the Summit →
          </a>
        </div>
      </div>

      <div class="section-label" style="margin-bottom:16px;">KEYNOTES</div>
      <div class="gen-speaker-grid" style="margin-bottom:32px;">
        <div class="gen-speaker-card">
          <img src="https://i.pravatar.cc/150?u=1" class="gen-speaker-avatar" alt="Jason Wei">
          <div class="gen-speaker-info">
            <div class="gen-speaker-name">Jason Wei</div>
            <div class="gen-speaker-title">Member of Technical Staff</div>
            <div class="gen-speaker-company">OpenAI</div>
            <div class="gen-speaker-tag">CoT & O3 Architect</div>
          </div>
        </div>
        <div class="gen-speaker-card">
          <img src="https://i.pravatar.cc/150?u=2" class="gen-speaker-avatar" alt="Arvind Jain">
          <div class="gen-speaker-info">
            <div class="gen-speaker-name">Arvind Jain</div>
            <div class="gen-speaker-title">Founder & CEO</div>
            <div class="gen-speaker-company">Glean</div>
            <div class="gen-speaker-tag">$7.2B Valuation</div>
          </div>
        </div>
        <div class="gen-speaker-card">
          <img src="https://i.pravatar.cc/150?u=3" class="gen-speaker-avatar" alt="Shannon McClenaghan">
          <div class="gen-speaker-info">
            <div class="gen-speaker-name">Shannon McClenaghan</div>
            <div class="gen-speaker-title">CEO</div>
            <div class="gen-speaker-company">StartX</div>
            <div class="gen-speaker-tag">$40B Portfolio</div>
          </div>
        </div>
      </div>

      <div class="section-label" style="margin-bottom:16px;">FEATURED SPEAKERS</div>
      <div class="gen-speaker-grid">
        <div class="gen-speaker-card">
          <img src="https://i.pravatar.cc/150?u=4" class="gen-speaker-avatar" alt="Rob Ferguson">
          <div class="gen-speaker-info">
            <div class="gen-speaker-name">Rob Ferguson</div>
            <div class="gen-speaker-title">Head of AI for Startups</div>
            <div class="gen-speaker-company">Microsoft</div>
            <div class="gen-speaker-tag">Startup Growth</div>
          </div>
        </div>
        <div class="gen-speaker-card">
          <img src="https://i.pravatar.cc/150?u=5" class="gen-speaker-avatar" alt="Ed Oates">
          <div class="gen-speaker-info">
            <div class="gen-speaker-name">Ed Oates</div>
            <div class="gen-speaker-title">Co-Founder</div>
            <div class="gen-speaker-company">Oracle</div>
            <div class="gen-speaker-tag">3rd Largest Software Co.</div>
          </div>
        </div>
        <div class="gen-speaker-card">
          <img src="https://i.pravatar.cc/150?u=6" class="gen-speaker-avatar" alt="Deon Nicholas">
          <div class="gen-speaker-info">
            <div class="gen-speaker-name">Deon Nicholas</div>
            <div class="gen-speaker-title">Founder</div>
            <div class="gen-speaker-company">Forethought</div>
            <div class="gen-speaker-tag">$100M+ Raised</div>
          </div>
        </div>
      </div>
      
      <div style="margin-top:24px;">
        <a href="#" style="font-size:12px; font-weight:600; color:var(--text-secondary); text-decoration:none;">> Show 1 more speakers</a>
      </div>
    </div>
  </div>
</section>
"""

with open('community.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert before <!-- ═══════════ 04 LOGO WALL THEO NHÓM ═══════════ -->
target_comment = "<!-- ═══════════ 04 LOGO WALL THEO NHÓM ═══════════ -->"
content = content.replace(target_comment, html_to_inject + "\n\n" + target_comment)

with open('community.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML injected into community.html")
