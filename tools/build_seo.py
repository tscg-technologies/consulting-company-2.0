import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# All 31 HTML files in alphabetical or logical order
ALL_PAGES = [
    "index.html",
    "about.html",
    "services.html",
    "business-consulting.html",
    "management-consulting.html",
    "strategy-consulting.html",
    "financial-consulting.html",
    "hr-consulting.html",
    "marketing-consulting.html",
    "it-consulting.html",
    "digital-transformation.html",
    "operations-consulting.html",
    "startup-consulting.html",
    "risk-management.html",
    "project-management.html",
    "organizational-development.html",
    "industries.html",
    "methodology.html",
    "case-studies.html",
    "case-study-details.html",
    "team.html",
    "insights.html",
    "article-details.html",
    "resources.html",
    "pricing.html",
    "careers.html",
    "faq.html",
    "contact.html",
    "book-consultation.html",
    "privacy-policy.html",
    "terms-and-conditions.html"
]

def generate_sitemap():
    base_url = "https://example.com"
    urls = []
    for page in ALL_PAGES:
        priority = "1.0" if page == "index.html" else ("0.9" if "services" in page or "consulting" in page else "0.8")
        urls.append(f"""  <url>
    <loc>{base_url}/{page}</loc>
    <lastmod>2026-11-05</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>""")
    
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>"""

    with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    print("sitemap.xml created.")

def generate_robots():
    robots = """# Robots.txt for Generic CONSULTING COMPANY Website
User-agent: *
Allow: /

Sitemap: https://example.com/sitemap.xml
"""
    with open(os.path.join(BASE_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)
    print("robots.txt created.")

generate_sitemap()
generate_robots()
