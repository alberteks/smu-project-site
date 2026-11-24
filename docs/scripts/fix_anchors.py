import re
from pathlib import Path

text = Path('module.md').read_text(encoding='utf-8')

# Remove {#anchor} tags from headings
# e.g. "# Purpose {#purpose}" -> "# Purpose"
text = re.sub(r'\s*\{#[^}]+\}', '', text)

Path('module.md').write_text(text, encoding='utf-8')
print("Done!")