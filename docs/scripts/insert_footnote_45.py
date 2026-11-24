import re
from pathlib import Path
 
text = Path('module.md').read_text(encoding='utf-8')
 
NEW_NUM = 45
NEW_TITLE = "To the Contrary | 25,000 Teens, 3 Years: Groundbreaking Social Media and Mental Health Study"
NEW_FILE = "to-the-contrary-25000-teens-3-years.md"
 
# 1. Shift all existing footnote numbers >= NEW_NUM up by 1 (both refs and definitions)
# Find max existing number first
existing_numbers = sorted(
    int(m.group(1)) for m in re.finditer(r'\[\^(\d+)\]', text)
)
max_num = max(existing_numbers)
 
# Shift from highest to lowest to avoid collisions
for old in range(max_num, NEW_NUM - 1, -1):
    text = re.sub(rf'\[\^{old}\]', f'[^{old + 1}]', text)
 
# 2. Insert the new footnote definition in the correct sorted position
lines = text.split('\n')
new_def_line = f"[^{NEW_NUM}]: [{NEW_TITLE}]({NEW_FILE})"
 
inserted = False
for i, line in enumerate(lines):
    m = re.match(r'^\[\^(\d+)\]:', line)
    if m and int(m.group(1)) > NEW_NUM:
        lines.insert(i, new_def_line)
        inserted = True
        break
 
if not inserted:
    # No higher-numbered definition found, append at end
    lines.append(new_def_line)
 
text = '\n'.join(lines)
 
Path('module.md').write_text(text, encoding='utf-8')
print(f"Inserted [^{NEW_NUM}] and shifted {max_num - NEW_NUM + 1} existing footnotes up by 1.")
print("Remember to manually add [^45] references where this new source should be cited!")
