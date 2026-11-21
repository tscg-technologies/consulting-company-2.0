import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_files = [f for f in os.listdir(BASE_DIR) if f.endswith(".html")]

# Regex to match the placeholder div block:
# <div class="image-placeholder aspect-..." data-placeholder-filename="NAME.webp" data-dimensions="...">...</div>
pattern = re.compile(
    r'<div class="image-placeholder\s+([^"]+)"\s+data-placeholder-filename="([^"]+)"\s+data-dimensions="([^"]+)">'
    r'.*?'
    r'<div class="placeholder-dimensions">Target:[^&]*&bull;\s*([^<]+)</div>\s*</div>',
    re.DOTALL
)

total_replaced = 0

for hf in sorted(html_files):
    path = os.path.join(BASE_DIR, hf)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    def replacer(match):
        aspect_class = match.group(1).strip()
        filename = match.group(2).strip()
        dims = match.group(3).strip()
        alt_text = match.group(4).strip()

        # strip extension and use .jpeg as present in assets/images/
        base_name = os.path.splitext(filename)[0]
        real_image = f"assets/images/{base_name}.jpeg"

        # Check if aspect has width/height or style needed
        # We wrap in a responsive image container or clean img tag
        # Notice aspect_class is like "aspect-16-9" or "aspect-1-1"
        return f'<img src="{real_image}" alt="{alt_text}" class="responsive-image {aspect_class}" loading="lazy">'

    new_content, count = pattern.subn(replacer, content)
    if count > 0:
        total_replaced += count
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"[{hf}] Replaced {count} placeholder(s)")

print(f"\nTotal replacements made: {total_replaced}")
