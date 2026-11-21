import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_shared_header(active_nav=""):
    services = [
        ("Business Consulting", "business-consulting.html", "Core strategy and operational planning"),
        ("Management Consulting", "management-consulting.html", "Leadership, governance & organizational alignment"),
        ("Strategy Consulting", "strategy-consulting.html", "Long-term market positioning & growth"),
        ("Financial Consulting", "financial-consulting.html", "Performance analysis & cash planning"),
        ("HR Consulting", "hr-consulting.html", "Workforce structure & talent frameworks"),
        ("Marketing Consulting", "marketing-consulting.html", "Customer segmentation & brand positioning"),
        ("IT Consulting", "it-consulting.html", "Enterprise systems & tech architecture"),
        ("Digital Transformation", "digital-transformation.html", "Process digitization & cloud roadmaps"),
        ("Operations Consulting", "operations-consulting.html", "Process optimization & supply chain"),
        ("Startup Consulting", "startup-consulting.html", "Business model & go-to-market design"),
        ("Risk Management", "risk-management.html", "Operational risk matrices & business continuity"),
        ("Project Management", "project-management.html", "Execution coordination & delivery governance"),
        ("Organizational Development", "organizational-development.html", "Culture, performance & change management"),
    ]

    services_links_html = "\n".join([
        f'            <li><a class="dropdown-link" href="{url}"><span class="dropdown-link-bold">{name}</span><span class="dropdown-link-desc">{desc}</span></a></li>'
        for name, url, desc in services
    ])

    return f'''  <!-- Top Announcement Bar -->
  <div class="top-bar">
    <div class="container top-bar-inner">
      <div class="top-bar-left">
        <span class="top-bar-item">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
          Mon–Sat: 9:00 AM – 6:00 PM
        </span>
        <span class="top-bar-item">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
          <a href="mailto:demo@example.com">demo@example.com</a>
        </span>
        <span class="top-bar-item">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
          0000000000
        </span>
      </div>
      <div class="top-bar-right">
        <!-- Palette Switcher -->
        <div class="theme-palette-picker" role="radiogroup" aria-label="Website Color Palette">
          <span class="theme-picker-label">Palette:</span>
          <button type="button" class="theme-swatch swatch-emerald active" data-theme-target="emerald" title="Prestige Emerald &amp; Champagne Gold (Default)" aria-label="Prestige Emerald Theme" aria-checked="true" role="radio"></button>
          <button type="button" class="theme-swatch swatch-cobalt" data-theme-target="cobalt" title="Modern Charcoal &amp; Royal Cobalt" aria-label="Modern Cobalt Theme" aria-checked="false" role="radio"></button>
          <button type="button" class="theme-swatch swatch-bordeaux" data-theme-target="bordeaux" title="Executive Bordeaux &amp; Warm Bronze" aria-label="Executive Bordeaux Theme" aria-checked="false" role="radio"></button>
          <button type="button" class="theme-swatch swatch-navy" data-theme-target="navy" title="Classic Corporate Navy &amp; Gold" aria-label="Classic Navy Theme" aria-checked="false" role="radio"></button>
        </div>
        <span class="demo-pill">Demonstration Platform &bull; Generic Corporate Model</span>
      </div>
    </div>
  </div>

  <!-- Sticky Header Navigation -->
  <header class="site-header" id="header">
    <div class="container navbar">
      <a href="index.html" class="brand-logo" aria-label="CONSULTING COMPANY Home">
        <div class="logo-symbol">
          <svg width="36" height="36" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect width="40" height="40" rx="8" fill="var(--navy-primary)" />
            <path d="M20 8L32 20L20 32L8 20L20 8Z" stroke="var(--gold-accent)" stroke-width="2" />
            <circle cx="20" cy="20" r="4.5" fill="var(--blue-accent)" />
            <line x1="20" y1="8" x2="20" y2="32" stroke="var(--blue-accent)" stroke-width="1.2" stroke-dasharray="2 2" />
            <line x1="8" y1="20" x2="32" y2="20" stroke="var(--blue-accent)" stroke-width="1.2" stroke-dasharray="2 2" />
          </svg>
        </div>
        <span class="logo-text">CONSULTING COMPANY</span>
      </a>

      <!-- Navigation Menu -->
      <nav aria-label="Main Navigation">
        <ul class="nav-menu">
          <li class="nav-item">
            <a href="index.html" class="nav-link {'active' if active_nav=='home' else ''}">Home</a>
          </li>
          <li class="nav-item">
            <a href="about.html" class="nav-link {'active' if active_nav=='about' else ''}">About</a>
          </li>
          <li class="nav-item has-dropdown">
            <a href="services.html" class="nav-link {'active' if active_nav=='services' else ''}" aria-haspopup="true">
              Services
              <svg class="dropdown-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </a>
            <ul class="dropdown-menu mega-menu" aria-label="Services Submenu">
{services_links_html}
              <li class="mega-menu-footer">
                <span style="font-size: 0.8rem; color: var(--text-secondary);">Comprehensive advisory across enterprise functional domains.</span>
                <a href="services.html" class="btn btn-secondary btn-sm">Explore All Services &rarr;</a>
              </li>
            </ul>
          </li>
          <li class="nav-item">
            <a href="industries.html" class="nav-link {'active' if active_nav=='industries' else ''}">Industries</a>
          </li>
          <li class="nav-item">
            <a href="methodology.html" class="nav-link {'active' if active_nav=='methodology' else ''}">Our Approach</a>
          </li>
          <li class="nav-item">
            <a href="case-studies.html" class="nav-link {'active' if active_nav=='case-studies' else ''}">Case Studies</a>
          </li>
          <li class="nav-item">
            <a href="insights.html" class="nav-link {'active' if active_nav=='insights' else ''}">Insights</a>
          </li>
          <li class="nav-item">
            <a href="contact.html" class="nav-link {'active' if active_nav=='contact' else ''}">Contact</a>
          </li>
          <li class="nav-item nav-menu-cta" style="display: none;">
            <a href="book-consultation.html" class="btn btn-primary btn-full">Book a Consultation</a>
          </li>
        </ul>
      </nav>

      <div class="header-actions">
        <a href="book-consultation.html" class="btn btn-primary">Book a Consultation</a>
        <button class="mobile-toggle" aria-label="Open Mobile Menu" aria-expanded="false">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        </button>
      </div>
    </div>
  </header>'''

def get_shared_footer():
    return '''  <!-- Corporate Footer -->
  <footer class="site-footer">
    <div class="container footer-grid">
      <!-- Column 1: Brand & Positioning -->
      <div class="footer-brand">
        <a href="index.html" class="brand-logo" style="margin-bottom: 0.75rem;">
          <div class="logo-symbol">
            <svg width="34" height="34" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect width="40" height="40" rx="8" fill="var(--navy-dark)" stroke="var(--blue-secondary)" stroke-width="1.5" />
              <path d="M20 8L32 20L20 32L8 20L20 8Z" stroke="var(--gold-accent)" stroke-width="2" />
              <circle cx="20" cy="20" r="4" fill="var(--blue-accent)" />
            </svg>
          </div>
          <span class="logo-text" style="color: #FFFFFF;">CONSULTING COMPANY</span>
        </a>
        <p>Business consulting and strategic advisory solutions to help organizations make informed decisions and move forward with confidence.</p>
        <div class="demo-disclaimer-tag" style="background: rgba(197, 168, 128, 0.15); border-color: rgba(197, 168, 128, 0.4); color: var(--gold-accent);">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
          Generic Demonstration Identity &bull; Non-Regulated Advisory
        </div>
      </div>

      <!-- Column 2: Consulting Services -->
      <div>
        <h4 class="footer-col-title">Consulting Services</h4>
        <ul class="footer-links">
          <li><a href="business-consulting.html">Business Consulting</a></li>
          <li><a href="strategy-consulting.html">Strategy Consulting</a></li>
          <li><a href="financial-consulting.html">Financial Consulting</a></li>
          <li><a href="hr-consulting.html">HR Consulting</a></li>
          <li><a href="it-consulting.html">IT Consulting</a></li>
          <li><a href="operations-consulting.html">Operations Consulting</a></li>
          <li><a href="services.html">View All 13 Practices &rarr;</a></li>
        </ul>
      </div>

      <!-- Column 3: Corporate & Practice -->
      <div>
        <h4 class="footer-col-title">Organization</h4>
        <ul class="footer-links">
          <li><a href="about.html">About the Firm</a></li>
          <li><a href="industries.html">Industries Served</a></li>
          <li><a href="methodology.html">Our Methodology</a></li>
          <li><a href="case-studies.html">Case Studies</a></li>
          <li><a href="team.html">Consulting Team</a></li>
          <li><a href="insights.html">Insights & Articles</a></li>
          <li><a href="resources.html">Resource Library</a></li>
          <li><a href="pricing.html">Engagement Framework</a></li>
          <li><a href="careers.html">Careers</a></li>
          <li><a href="faq.html">Frequently Asked Questions</a></li>
        </ul>
      </div>

      <!-- Column 4: Demonstration Contact -->
      <div>
        <h4 class="footer-col-title">Demo Advisory Office</h4>
        <div class="footer-contact-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
          <div>
            <span style="display: block; color: #FFF; font-weight: 600;">0000000000</span>
            <span style="font-size: 0.78rem;">Alt: 0000000000</span>
          </div>
        </div>
        <div class="footer-contact-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
          <a href="mailto:demo@example.com">demo@example.com</a>
        </div>
        <div class="footer-contact-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
          <span>Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000.</span>
        </div>
        <div class="footer-contact-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
          <span>Mon–Sat: 9:00 AM – 6:00 PM</span>
        </div>
      </div>
    </div>

    <!-- Footer Bottom Legal -->
    <div class="container footer-bottom">
      <div>&copy; 2026 CONSULTING COMPANY. Generic illustrative website demonstration. All rights reserved.</div>
      <div class="footer-legal-links">
        <a href="privacy-policy.html">Privacy Policy</a>
        <a href="terms-and-conditions.html">Terms & Conditions</a>
        <a href="sitemap.xml">XML Sitemap</a>
      </div>
    </div>
  </footer>

  <!-- Back to Top Button -->
  <button class="back-to-top" aria-label="Back to Top">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="18 15 12 9 6 15"></polyline></svg>
  </button>

  <!-- Core JavaScript Scripts -->
  <script src="assets/js/main.js"></script>
  <script src="assets/js/interactions.js"></script>
  <script src="assets/js/forms.js"></script>'''

def get_page_shell(title, description, canonical_url, active_nav, body_content):
    header = get_shared_header(active_nav)
    footer = get_shared_footer()
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | CONSULTING COMPANY</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://example.com/{canonical_url}">

  <!-- Open Graph Metadata -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title} | CONSULTING COMPANY">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="https://example.com/{canonical_url}">
  <meta property="og:site_name" content="CONSULTING COMPANY">

  <!-- Immediate Theme Initialization (Prevents color flash) -->
  <script>
    (function(){{
      try {{
        var t = localStorage.getItem('consulting_theme') || 'emerald';
        document.documentElement.setAttribute('data-theme', t);
      }} catch(e){{}}
    }})();
  </script>

  <!-- Core Stylesheets -->
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="stylesheet" href="assets/css/responsive.css">
  <link rel="stylesheet" href="assets/css/animations.css">
</head>
<body>
{header}

<main id="main-content">
{body_content}
</main>

{footer}
</body>
</html>'''

def make_placeholder(filename, aspect="aspect-16-9", dimensions="1920x1080", label="Corporate Business Strategy"):
    return f'''<div class="image-placeholder {aspect}" data-placeholder-filename="{filename}" data-dimensions="{dimensions}">
  <div class="placeholder-grid-pattern"></div>
  <span class="placeholder-badge">Image Placeholder &bull; Google Flow Ready</span>
  <svg class="placeholder-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
    <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
    <circle cx="8.5" cy="8.5" r="1.5"></circle>
    <polyline points="21 15 16 10 5 21"></polyline>
  </svg>
  <div class="placeholder-filename">{filename}</div>
  <div class="placeholder-dimensions">Target: {dimensions} &bull; {label}</div>
</div>'''

print("Updated build_helpers with multi-theme architecture.")
