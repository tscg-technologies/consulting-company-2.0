const fs = require('fs');
const path = require('path');

const baseDir = path.resolve(__dirname, '..');
const htmlFiles = fs.readdirSync(baseDir).filter(f => f.endsWith('.html'));

const imgPattern = /<img[^>]+src=["']([^"']+)["']/g;

const allImages = [];
const missingImages = [];

for (const hf of htmlFiles.sort()) {
  const filePath = path.join(baseDir, hf);
  const content = fs.readFileSync(filePath, 'utf8');

  let match;
  while ((match = imgPattern.exec(content)) !== null) {
    const src = match[1];
    allImages.push({ hf, src });
    const resolved = path.normalize(path.join(baseDir, src));
    if (!fs.existsSync(resolved)) {
      missingImages.push({ hf, src, resolved });
    }
  }
}

console.log(`Total HTML files checked: ${htmlFiles.length}`);
console.log(`Total <img> tags found: ${allImages.length}`);
console.log(`Missing images: ${missingImages.length}`);

if (missingImages.length > 0) {
  for (const item of missingImages) {
    console.error(`  [MISSING] in ${item.hf}: ${item.src} -> ${item.resolved}`);
  }
  process.exit(1);
} else {
  console.log('ALL <img> tags resolve to existing physical files on disk!');
}
