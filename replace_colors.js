const fs = require('fs');
const path = require('path');

const directory = '.';

const replacements = [
  // Primary Teal -> Blue (#0344a8 / 3, 68, 168)
  { from: /#0d5c6b/gi, to: '#0344a8' },
  { from: /rgba\(13,\s*92,\s*107/gi, to: 'rgba(3, 68, 168' },
  
  // Teal-2 -> Lighter Blue (#1f5ebc / 31, 94, 188)
  { from: /#0f6f80/gi, to: '#1f5ebc' },
  { from: /rgba\(15,\s*111,\s*128/gi, to: 'rgba(31, 94, 188' },
  { from: /#176f80/gi, to: '#1f5ebc' }, // teal-soft
  { from: /rgba\(23,\s*111,\s*128/gi, to: 'rgba(31, 94, 188' },

  // Teal-3 -> Darker Blue (#02317a / 2, 49, 122)
  { from: /#073d46/gi, to: '#02317a' },
  { from: /rgba\(7,\s*61,\s*70/gi, to: 'rgba(2, 49, 122' },
  { from: /#0a4550/gi, to: '#02317a' }, // teal-dark
  { from: /rgba\(10,\s*69,\s*80/gi, to: 'rgba(2, 49, 122' },

  // Gold -> Orange (#e6871c / 230, 135, 28)
  { from: /#d4a847/gi, to: '#e6871c' },
  { from: /rgba\(212,\s*168,\s*71/gi, to: 'rgba(230, 135, 28' },
  
  // Lighter Gold / Accent texts -> Lighter Orange / Accent texts
  { from: /#f8d57b/gi, to: '#f29835' },
  { from: /#8e6a14/gi, to: '#b36100' },
  { from: /#7b6a35/gi, to: '#b36100' },

  // Navy (Deep bg) -> Deep Blue (#011736 / 1, 23, 54)
  { from: /#0d2433/gi, to: '#011736' },
  { from: /rgba\(13,\s*36,\s*51/gi, to: 'rgba(1, 23, 54' },
  { from: /#091a24/gi, to: '#011026' }, // footer bg
  { from: /#0b1e29/gi, to: '#011026' }, // another footer bg
  { from: /#102d3d/gi, to: '#011e42' }, // gradient stop
  { from: /#112b3b/gi, to: '#011e42' }, // gradient stop

  // Text Colors (Dark Gray-Teal) -> Dark Blue-Gray
  { from: /#16323a/gi, to: '#0f1a2e' },
  { from: /#18313a/gi, to: '#0f1a2e' },
  { from: /#12313a/gi, to: '#0f1a2e' },
  { from: /#23444d/gi, to: '#15243d' },
  { from: /#294850/gi, to: '#1a2d4c' },

  // Muted Text -> Cooler Muted Gray
  { from: /#667b82/gi, to: '#526075' },
  { from: /#637780/gi, to: '#526075' },
  
  // Dark overlay colors for hero bg
  { from: /rgba\(6,\s*34,\s*41/gi, to: 'rgba(2, 18, 41' },
  { from: /rgba\(10,\s*48,\s*57/gi, to: 'rgba(2, 28, 64' },
  { from: /rgba\(7,\s*33,\s*42/gi, to: 'rgba(2, 18, 41' },

  // Green / Whatsapp color -> Provided Green (#74d94f / 116, 217, 79)
  { from: /#25D366/gi, to: '#74d94f' },
  { from: /rgba\(37,\s*211,\s*102/gi, to: 'rgba(116, 217, 79' },
  
  // Adjust generic shadow colors relying on old rgb(6, 49, 58)
  { from: /rgba\(6,\s*49,\s*58/gi, to: 'rgba(2, 25, 64' },
  { from: /rgba\(13,\s*36,\s*51/gi, to: 'rgba(1, 23, 54' }
];

const files = fs.readdirSync(directory).filter(file => file.endsWith('.html'));

files.forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  
  replacements.forEach(r => {
    content = content.replace(r.from, r.to);
  });

  fs.writeFileSync(file, content);
  console.log(`Updated ${file}`);
});
