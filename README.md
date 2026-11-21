# CONSULTING COMPANY — PREMIUM STATIC CORPORATE WEBSITE

A complete, high-performance, professional 31-page static website representing a generic international **CONSULTING COMPANY**. Built with semantic HTML5, modern CSS3, and vanilla JavaScript without external frameworks or backend dependencies. Fully optimized for static hosting on **Hostinger**.

---

## 1. WEBSITE OVERVIEW

- **Brand Identity:** Generic "CONSULTING COMPANY" with an abstract geometric emblem logo.
- **Positioning:** "Clarity for Better Decisions. Strategy for Sustainable Growth."
- **Total Pages:** 31 fully linked, standalone HTML pages.
- **Visual Aesthetic:** High-end international corporate advisory design system with multi-theme color switching:
  - **Default: Prestige Deep Emerald & Champagne Gold** (#0B2821 / #15473B / #1B735D / #C5A880) — inspired by premier global management strategy firms & private advisory.
  - **Option 2: Modern Charcoal & Royal Cobalt** (#0F172A / #1E3A8A / #2563EB / #D97706) — high-contrast enterprise tech advisory palette.
  - **Option 3: Executive Bordeaux & Warm Bronze** (#2B0F1C / #4C1932 / #9B2C59 / #C78D66) — boutique private wealth & M&A advisory aesthetic.
  - **Option 4: Classic Corporate Navy & Gold** (#101D35 / #244B78 / #3979C6 / #B99A5B) — traditional corporate consulting palette.
- **Color Switcher:** Interactive top-bar palette picker with instant zero-flicker live switching and `localStorage` persistence.
- **Interactive Capabilities:**
  - Sticky corporate header with responsive mobile hamburger drawer.
  - Multi-column mega menu for 13 consulting practices.
  - Category filter for illustrative case studies.
  - Instant client-side search & category filtering for thought leadership articles.
  - Accessible multi-item FAQ accordions.
  - Pure CSS analytical dashboards (business performance, cash flow, workforce pipeline, and risk matrix).
  - 6-step multi-step consultation enquiry wizard (`book-consultation.html`) with client-side validation, progress bar, dynamic summary review, and demo confirmation modal.
  - Complete dummy contact details with zero external data transmission.

---

## 2. PROJECT FOLDER STRUCTURE

```
consulting-company/
├── index.html                           # Homepage with hero, services, dashboards & case studies
├── about.html                           # Corporate philosophy, mission, vision & principles
├── services.html                        # Comprehensive directory of all 13 consulting practices
├── business-consulting.html             # Business planning, models, and growth strategy
├── management-consulting.html           # Governance, organizational structure & decision frameworks
├── strategy-consulting.html             # Corporate strategy, market positioning & roadmaps
├── financial-consulting.html            # Financial diagnostics, budgeting & cash flow planning
├── hr-consulting.html                   # Workforce planning, talent retention & performance management
├── marketing-consulting.html            # Brand positioning, acquisition funnels & market research
├── it-consulting.html                   # Enterprise IT architecture, software selection & cloud strategy
├── digital-transformation.html          # Process digitization, workflow automation & change roadmaps
├── operations-consulting.html           # Process optimization, Lean workflow & supply chain
├── startup-consulting.html              # Early-stage validation, unit economics & pitch preparation
├── risk-management.html                 # Enterprise risk identification, 5x5 matrix & BCP planning
├── project-management.html              # PMO delivery governance, WBS scoping & milestone tracking
├── organizational-development.html      # Cultural transformation, team effectiveness & leadership
├── industries.html                      # Sector advisory across 12 commercial industries
├── methodology.html                     # 5-Stage consulting framework (Discover to Support)
├── case-studies.html                    # Filterable gallery of 8 illustrative demonstration case studies
├── case-study-details.html              # Reusable in-depth case study template
├── team.html                            # Generic role-based practice leadership profiles
├── insights.html                        # Thought leadership library with live search & filters
├── article-details.html                 # Editorial article layout with table of contents
├── resources.html                       # Download-style business checklists & template previews
├── pricing.html                         # Three-tier consulting engagement framework & comparison
├── careers.html                         # Illustrative practice openings & frontend application form
├── faq.html                             # Categorized interactive FAQ accordion
├── contact.html                         # Advisory desk contact details & validated enquiry form
├── book-consultation.html               # 6-step interactive consultation planner
├── privacy-policy.html                  # Demonstration privacy policy & data notice
├── terms-and-conditions.html            # Demonstration website terms & conditions
│
├── assets/
│   ├── css/
│   │   ├── style.css                    # Design system, layout, typography, cards & dashboards
│   │   ├── responsive.css               # Media queries (360px, 390px, 768px, 1024px, 1440px, 1920px)
│   │   └── animations.css               # Subtle transitions, scroll reveals & reduced-motion support
│   │
│   ├── js/
│   │   ├── main.js                      # Sticky navigation, mobile toggle, active link detection
│   │   ├── interactions.js              # FAQ accordion, case studies filter & article live search
│   │   └── forms.js                     # 6-step wizard, contact validation & demo notices
│   │
│   ├── images/                          # Destination folder for Google Flow generated WebP images
│   └── icons/                           # Reusable SVG vector assets
│
├── sitemap.xml                          # Complete XML sitemap for search indexing
├── robots.txt                           # Search engine crawling directives
├── IMAGE-GENERATION-GUIDE.md            # Detailed Google Flow prompts for all 67 placeholders
└── README.md                            # Comprehensive technical documentation & run guide
```

---

## 3. TECHNOLOGIES USED

- **Markup:** HTML5 (semantic elements: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`).
- **Styling:** Vanilla CSS3 (custom CSS variables, flexbox, CSS grid, CSS charts, and `@media` queries).
- **Interactivity:** Vanilla ECMAScript 6+ (no external frameworks or dependencies: zero Bootstrap, zero jQuery, zero React).
- **Icons & Graphics:** Pure SVG vector code embedded directly into templates.
- **Typography:** Modern clean system font stack for high performance and zero external font network latency.

---

## 4. HOW TO RUN LOCALLY

Because this website contains zero backend dependencies, you can run it immediately using any local web server or standard browser:

### Option A: Using Python's Built-in HTTP Server
Run this in PowerShell / Terminal:
```bash
python -m http.server 8000
```
Then open your browser to: `http://localhost:8000`

### Option B: Using Node.js `serve` / `http-server`
```bash
npx serve .
```

### Option C: Direct File Opening
You can directly double-click `index.html` to open it in Chrome, Edge, Safari, or Firefox.

---

## 5. HOW TO EDIT PAGE CONTENT

1. Open any `.html` file in your preferred text editor (e.g., VS Code).
2. Locate the main content between `<main id="main-content">` and `</main>`.
3. Modify text, headings, or lists as desired.
4. Save the file and refresh your browser.

---

## 6. HOW TO REPLACE IMAGE PLACEHOLDERS

The website currently uses high-end, responsive CSS/SVG placeholders with explicit aspect ratios (16:9, 4:3, 1:1) and target filenames (e.g., `hero-business-consulting.webp`).

To replace placeholders with genuine images generated via **Google Flow**:
1. Refer to `IMAGE-GENERATION-GUIDE.md` for the exact prompt and dimensions for each of the 67 images.
2. Generate and export each image as a `.webp` file with its designated filename.
3. Save the image to the `assets/images/` folder.
4. Open the respective HTML file, locate the placeholder `div`:
   ```html
   <!-- Before: -->
   <div class="image-placeholder aspect-16-9" data-placeholder-filename="hero-business-consulting.webp" data-dimensions="1920x1080">
     ...
   </div>
   ```
   Replace it with standard responsive image markup:
   ```html
   <!-- After: -->
   <img src="assets/images/hero-business-consulting.webp" alt="Corporate strategic advisory meeting in an executive boardroom" width="1920" height="1080" loading="eager" class="hero-image">
   ```
5. For below-the-fold images, ensure `loading="lazy"` is used to maintain fast initial page load speeds.

---

## 7. HOW TO UPDATE DUMMY CONTACT DETAILS

The website uses consistent dummy contact information:
- **Phone:** `0000000000`
- **Email:** `demo@example.com`
- **Address:** `Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000.`
- **Hours:** `Monday–Saturday: 9:00 AM–6:00 PM`

To update these to real company coordinates:
1. Search and replace across all `.html` files:
   - Replace `0000000000` with your business phone number.
   - Replace `demo@example.com` with your business email.
   - Replace the sample Hyderabad address with your registered office address.
2. Update the contact block in `contact.html` and the multi-column footer in all 31 files.

---

## 8. HOW TO DEPLOY ON HOSTINGER STATIC HOSTING

1. Log into your **Hostinger hPanel**.
2. Navigate to **Websites** &rarr; select your domain &rarr; open **File Manager**.
3. Open the `public_html/` root directory.
4. Upload all files from this project (`index.html`, all other `.html` files, `sitemap.xml`, `robots.txt`, and the `assets/` folder).
5. Ensure `index.html` resides directly in `public_html/` (not inside a nested sub-folder).
6. Enable SSL in Hostinger hPanel for HTTPS security.
7. Your consulting website will immediately be live and globally accessible with blazing fast TTFB.

---

## 9. HOW TO UPDATE SEO METADATA

Every page contains unique Open Graph, canonical, and standard meta tags in its `<head>`:
```html
<title>[Page Title] | CONSULTING COMPANY</title>
<meta name="description" content="[Unique 150-160 character description]">
<link rel="canonical" href="https://yourdomain.com/[page-name].html">
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:url" content="https://yourdomain.com/[page-name].html">
```
When attaching a custom domain:
1. Replace `https://example.com/` in all HTML files, `sitemap.xml`, and `robots.txt` with your live production URL.

---

## 10. HOW TO ADD ADDITIONAL CONSULTING SERVICES

1. Duplicate any existing service page (e.g., `business-consulting.html`) and rename it (e.g., `sustainability-consulting.html`).
2. Update the page title, hero headline, advisory capabilities, and diagram.
3. Open `services.html` and add a new card to the service grid.
4. Open all other `.html` files and add the new link to the `Services` dropdown menu and footer column.
5. Add the new URL to `sitemap.xml`.

---

## 11. HOW TO ADD NEW PAGES

1. Copy the standard page template shell from `about.html`.
2. Insert your custom HTML within `<main id="main-content">`.
3. Ensure the active navigation state class (`active`) is applied to the appropriate menu link.
4. Add the new page link to `sitemap.xml`.

---

## 12. QUALITY ASSURANCE & VERIFICATION SUMMARY

- **All 31 Pages Created:** Verified & present in project root.
- **Zero Framework Bloat:** 100% vanilla HTML5, CSS3, and modern JS.
- **Responsive Across All Viewports:** Verified for 360px, 390px, 768px, 1024px, 1440px, and 1920px.
- **Reduced-Motion Support:** `@media (prefers-reduced-motion: reduce)` implemented.
- **Accessible Navigation:** ARIA attributes, keyboard support (ESC key & focus rings).
- **Form Validation & Privacy:** Client-side validation active; zero data leakage.
- **Image Guide:** Complete `IMAGE-GENERATION-GUIDE.md` with 67 copy-ready prompts.
