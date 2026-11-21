import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_files = [f for f in os.listdir(BASE_DIR) if f.endswith(".html")]

img_pattern = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']')

all_images = []
missing_images = []

for hf in sorted(html_files):
    path = os.path.join(BASE_DIR, hf)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = img_pattern.findall(content)
    for src in matches:
        all_images.append((hf, src))
        # Resolve path relative to BASE_DIR
        resolved = os.path.normpath(os.path.join(BASE_DIR, src))
        if not os.path.exists(resolved):
            missing_images.append((hf, src, resolved))

print(f"Total HTML files checked: {len(html_files)}")
print(f"Total <img> tags found: {len(all_images)}")
print(f"Missing images: {len(missing_images)}")

if missing_images:
    for hf, src, resolved in missing_images:
        print(f"  [MISSING] in {hf}: {src}")
else:
    print("ALL <img> tags resolve to existing physical files on disk!")
