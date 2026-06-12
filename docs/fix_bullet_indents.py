import re
from pathlib import Path

def fix_indentation(text):
    lines = text.split('\n')
    fixed = []
    for line in lines:
        m = re.match(r'^( +)(\* .*)', line)
        if m:
            spaces = len(m.group(1))
            level = spaces // 2
            new_indent = '    ' * level
            fixed.append(new_indent + m.group(2))
        else:
            fixed.append(line)
    return '\n'.join(fixed)

folder = Path('.')
changed = 0
for f in folder.glob('*.md'):
    text = f.read_text(encoding='utf-8')
    if re.search(r'^ +\* ', text, re.MULTILINE):
        new_text = fix_indentation(text)
        if new_text != text:
            f.write_text(new_text, encoding='utf-8')
            changed += 1

print(f"Done! {changed} files updated.")