import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

html_files = [f for f in os.listdir(BASE_DIR) if f.endswith(".html")]

placeholders = []
pattern = re.compile(r'<div class="image-placeholder\s+([^"]+)"\s+data-placeholder-filename="([^"]+)"\s+data-dimensions="([^"]+)">.*?<div class="placeholder-dimensions">Target:[^&]*&bull;\s*([^<]+)</div>', re.DOTALL)

for hf in sorted(html_files):
    path = os.path.join(BASE_DIR, hf)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = pattern.findall(content)
    for aspect, filename, dims, label in matches:
        placeholders.append({
            "page": hf,
            "aspect": aspect.strip(),
            "filename": filename.strip(),
            "dimensions": dims.strip(),
            "label": label.strip()
        })

print(f"Total placeholders found: {len(placeholders)}")
for idx, p in enumerate(placeholders, 1):
    print(f"{idx}. [{p['page']}] {p['filename']} ({p['aspect']} - {p['dimensions']}) - {p['label']}")
