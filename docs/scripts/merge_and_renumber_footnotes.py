import re
from pathlib import Path

text = Path('module.md').read_text(encoding='utf-8')

# Pairs to merge: (keep, remove) -- all refs to "remove" become "keep", and
# "remove"'s definition is dropped entirely.
merge_pairs = [
    (7, 11),
    (12, 13),
    (17, 22),
    (33, 34),
]

lines = text.split('\n')

removed_numbers = set(remove for _, remove in merge_pairs)

# 1. Drop definition lines for the "remove" footnotes
new_lines = []
for line in lines:
    m = re.match(r'^\[\^(\d+)\]:', line)
    if m and int(m.group(1)) in removed_numbers:
        continue
    new_lines.append(line)
text = '\n'.join(new_lines)

# 2. Replace all references to "remove" with "keep" (do this for all pairs first,
#    before any renumbering, using temporary unique placeholders to avoid collisions)
for keep, remove in merge_pairs:
    text = re.sub(rf'\[\^{remove}\]', f'[^{keep}]', text)

# 3. Determine the new sequential numbering.
#    Find all footnote numbers still present (from definitions, which are authoritative)
remaining_numbers = sorted(
    int(m.group(1)) for m in re.finditer(r'^\[\^(\d+)\]:', text, re.MULTILINE)
)

# Build old -> new mapping (sequential 1..N)
old_to_new = {old: i + 1 for i, old in enumerate(remaining_numbers)}

# 4. Apply renumbering to both references and definitions.
# To avoid collisions during substitution (e.g. 5->4 then later 4->3 double-shifting),
# use a placeholder pattern first.
for old, new in old_to_new.items():
    if old != new:
        text = re.sub(rf'\[\^{old}\]', f'[^__TMP{new}__]', text)

text = re.sub(r'\[\^__TMP(\d+)__\]', r'[^\1]', text)

Path('module.md').write_text(text, encoding='utf-8')

print("Merged pairs:", merge_pairs)
print("Old -> New mapping (only changed):")
for old, new in old_to_new.items():
    if old != new:
        print(f"  {old} -> {new}")
print("Done!")