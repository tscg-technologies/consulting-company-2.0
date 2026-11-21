const fs = require('fs');
const path = require('path');

const baseDir = path.resolve(__dirname, '..');
const htmlFiles = fs.readdirSync(baseDir).filter(f => f.endsWith('.html'));

const linkPattern = /href=["']([^"'#]+)(#[^"']*)?["']/g;

const brokenLinks = [];
let totalLinksChecked = 0;

for (const hf of htmlFiles) {
  const filePath = path.join(baseDir, hf);
  const content = fs.readFileSync(filePath, 'utf8');

  let match;
  while ((match = linkPattern.exec(content)) !== null) {
    const targetUrl = match[1];
    if (
      targetUrl.startsWith('http://') ||
      targetUrl.startsWith('https://') ||
      targetUrl.startsWith('mailto:') ||
      targetUrl.startsWith('tel:') ||
      targetUrl.startsWith('javascript:')
    ) {
      continue;
    }

    totalLinksChecked++;
    const targetPath = path.normalize(path.join(baseDir, targetUrl));
    if (!fs.existsSync(targetPath)) {
      brokenLinks.push({ hf, targetUrl });
    }
  }
}

console.log(`Total internal links checked across ${htmlFiles.length} pages: ${totalLinksChecked}`);
if (brokenLinks.length > 0) {
  console.log(`Found ${brokenLinks.length} broken links:`);
  for (const b of brokenLinks) {
    console.log(`  In ${b.hf} -> ${b.targetUrl}`);
  }
} else {
  console.log('ALL internal links are 100% valid! Zero broken links.');
}
