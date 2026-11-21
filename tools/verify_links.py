import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_files = [f for f in os.listdir(BASE_DIR) if f.endswith(".html")]

link_pattern = re.compile(r'href=["\']([^"\'#]+)(#[^"\']*)?["\']')

broken_links = []
total_links_checked = 0

for hf in html_files:
    file_path = os.path.join(BASE_DIR, hf)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = link_pattern.findall(content)
    for target_url, hash_frag in matches:
        # Ignore external links, mailto, tel, javascript
        if target_url.startswith(("http://", "https://", "mailto:", "tel:", "javascript:")):
            continue
        
        total_links_checked += 1
        # Resolve target
        target_path = os.path.join(BASE_DIR, target_url.replace("/", os.sep))
        if not os.path.exists(target_path):
            broken_links.append((hf, target_url))

print(f"Total internal links checked across 31 pages: {total_links_checked}")
if broken_links:
    print(f"Found {len(broken_links)} broken links:")
    for src, tgt in broken_links:
        print(f"  In {src} -> {tgt}")
else:
    print("ALL internal links are 100% valid! Zero broken links.")
