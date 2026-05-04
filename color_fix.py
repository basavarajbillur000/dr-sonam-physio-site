import os
import re

files = ['index.html', 'about.html', 'services.html', 'contact.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace :root block for index.html
    root_pattern_index = re.compile(r':root\s*\{.*?\--container:\s*1180px;\s*\}', re.DOTALL)
    new_root_index = """:root {
      --teal: #0050A0;
      --teal-2: #7ED321;
      --teal-3: #061C30;
      --warm: #FFFFFF;
      --gold: #7ED321;
      --navy: #061C30;
      --text: #061C30;
      --muted: #0050A0;
      --white: #FFFFFF;
      --card: #FFFFFF;
      --shadow: 0 12px 40px rgba(6, 28, 48, 0.08);
      --radius: 22px;
      --container: 1180px;
    }"""
    content = root_pattern_index.sub(new_root_index, content)

    # 1b. Replace :root block for other files (with .3s ease)
    root_pattern_others = re.compile(r':root\s*\{.*?\--transition:all \.3s ease;\s*\}', re.DOTALL)
    new_root_others = """:root{
      --teal:#0050A0;
      --teal-dark:#061C30;
      --teal-soft:#7ED321;
      --cream:#FFFFFF;
      --gold:#7ED321;
      --navy:#061C30;
      --text:#061C30;
      --muted:#0050A0;
      --white:#ffffff;
      --border:rgba(0,80,160,0.12);
      --shadow:0 18px 50px rgba(6,28,48,.1);
      --shadow-lg:0 24px 60px rgba(6,28,48,.15);
      --radius:22px;
      --transition:all .3s ease;
    }"""
    content = root_pattern_others.sub(new_root_others, content)
    
    # 1c. Replace :root block for other files (with .35s ease)
    root_pattern_services = re.compile(r':root\s*\{.*?\--transition:all \.35s ease;\s*\}', re.DOTALL)
    new_root_services = """:root{
      --teal:#0050A0;
      --teal-dark:#061C30;
      --teal-soft:#7ED321;
      --cream:#FFFFFF;
      --gold:#7ED321;
      --navy:#061C30;
      --text:#061C30;
      --muted:#0050A0;
      --white:#ffffff;
      --border:rgba(0,80,160,0.12);
      --shadow:0 18px 50px rgba(6,28,48,.1);
      --shadow-lg:0 24px 60px rgba(6,28,48,.15);
      --radius:22px;
      --transition:all .35s ease;
    }"""
    content = root_pattern_services.sub(new_root_services, content)

    # 2. Fix body background in index.html
    content = re.sub(r'background:\s*linear-gradient\(180deg,\s*#fffefc\s*0%,\s*#f9f7f4\s*100%\);', 'background: var(--white);', content)
    
    # 3. Replace all random hardcoded rgba and hex colors to strictly stick to the 4 colors
    
    # Old Teal (13,92,107) -> Primary Blue (0,80,160)
    content = re.sub(r'rgba\(13,\s*92,\s*107', 'rgba(0, 80, 160', content)
    content = re.sub(r'rgba\(15,\s*111,\s*128', 'rgba(0, 80, 160', content)
    
    # Old Dark Navy -> Dark Blue (6,28,48)
    content = re.sub(r'rgba\(6,\s*49,\s*58', 'rgba(6, 28, 48', content)
    content = re.sub(r'rgba\(10,\s*36,\s*51', 'rgba(6, 28, 48', content)
    content = re.sub(r'rgba\(13,\s*36,\s*51', 'rgba(6, 28, 48', content)
    content = re.sub(r'rgba\(6,\s*34,\s*41', 'rgba(6, 28, 48', content)
    
    # Old Gold (212,168,71) -> Green (126,211,33)
    content = re.sub(r'rgba\(212,\s*168,\s*71', 'rgba(126, 211, 33', content)
    
    # Hex Replacements
    content = re.sub(r'#f8d57b', 'var(--teal-2)', content, flags=re.IGNORECASE)
    content = re.sub(r'#25D366', 'var(--teal-2)', content, flags=re.IGNORECASE)
    content = re.sub(r'#091a24', 'var(--navy)', content, flags=re.IGNORECASE)
    content = re.sub(r'#0b1e29', 'var(--navy)', content, flags=re.IGNORECASE)
    content = re.sub(r'#0d2433', 'var(--navy)', content, flags=re.IGNORECASE)
    content = re.sub(r'#102d3d', 'var(--navy)', content, flags=re.IGNORECASE)
    
    # Fix gradients with hardcoded colors
    content = re.sub(r'linear-gradient\(120deg,\s*rgba\(.*?\),\s*rgba\(.*?\),\s*rgba\(.*?\)\)', 'linear-gradient(120deg, rgba(6,28,48,0.92), rgba(0,80,160,0.75))', content)

    # about.html hero gradient:
    content = re.sub(r'linear-gradient\(120deg,\s*rgba\(7,33,42,\.82\),\s*rgba\(13,92,107,\.6\)\)', 'linear-gradient(120deg, rgba(6,28,48,0.92), rgba(0,80,160,0.75))', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Colors fixed.")
