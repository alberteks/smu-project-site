import re
from pathlib import Path
 
text = Path('module.md').read_text(encoding='utf-8')
 
# Remove one or more spaces immediately before a footnote marker like [^12]
text = re.sub(r' +(\[\^\d+\])', r'\1', text)
 
Path('module.md').write_text(text, encoding='utf-8')
print("Done!")
