import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, "images")
html_files = [f for f in os.listdir(BASE_DIR) if f.endswith(".html")]

pattern = re.compile(r'data-placeholder-filename="([^"]+)"')
placeholders = set()
for hf in html_files:
    with open(os.path.join(BASE_DIR, hf), "r", encoding="utf-8") as f:
        content = f.read()
    for m in pattern.findall(content):
        placeholders.add(os.path.splitext(m)[0])

print(f"Total unique placeholder bases: {len(placeholders)}")
print(f"Total available images: {len(images)}")
missing = [p for p in placeholders if p not in images]
print(f"Missing: {len(missing)} -> {missing}")
