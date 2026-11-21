const fs = require('fs');
const path = require('path');

const baseDir = path.resolve(__dirname, '..');
const htmlFiles = fs.readdirSync(baseDir).filter(f => f.endsWith('.html'));

const pattern = /<div class="image-placeholder\s+([^"]+)"\s+data-placeholder-filename="([^"]+)"\s+data-dimensions="([^"]+)">[\s\S]*?<div class="placeholder-dimensions">Target:[^&]*&bull;\s*([^<]+)<\/div>\s*<\/div>/g;

let totalReplaced = 0;
let fileDetails = [];
let missingFiles = [];

for (const hf of htmlFiles.sort()) {
  const filePath = path.join(baseDir, hf);
  const content = fs.readFileSync(filePath, 'utf8');

  let fileReplacements = 0;
  const newContent = content.replace(pattern, (match, aspectClass, filename, dims, altText) => {
    aspectClass = aspectClass.trim();
    filename = filename.trim();
    dims = dims.trim();
    altText = altText.trim().replace(/"/g, '&quot;');

    const baseName = path.parse(filename).name;
    const realImage = `assets/images/${baseName}.jpeg`;
    const fullDiskPath = path.join(baseDir, 'assets', 'images', `${baseName}.jpeg`);

    if (!fs.existsSync(fullDiskPath)) {
      missingFiles.push({ hf, realImage, fullDiskPath });
    }

    const [width, height] = dims.split('x');
    const isHero = baseName.includes('hero');
    const loadingAttr = isHero ? 'loading="eager" fetchpriority="high"' : 'loading="lazy"';

    fileReplacements++;
    totalReplaced++;

    return `<img src="${realImage}" alt="${altText}" class="responsive-image ${aspectClass}" width="${width}" height="${height}" ${loadingAttr}>`;
  });

  if (fileReplacements > 0) {
    fs.writeFileSync(filePath, newContent, 'utf8');
    fileDetails.push({ file: hf, count: fileReplacements });
  }
}

console.log('Total placeholder replacements completed:', totalReplaced);
console.log('Files updated:', fileDetails.length);
fileDetails.forEach(d => console.log(`  [${d.file}]: replaced ${d.count} placeholder(s)`));

if (missingFiles.length > 0) {
  console.error('\nWARNING: Missing files on disk:');
  missingFiles.forEach(m => console.error(`  ${m.hf}: ${m.realImage}`));
} else {
  console.log('\nSUCCESS: All replaced image paths exist on disk in assets/images/!');
}
