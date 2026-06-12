import re
from pathlib import Path
 
text = Path('index.md').read_text(encoding='utf-8')
 
# Remove one or more spaces immediately before a footnote marker like [^12]
text = re.sub(r' +(\[\^\d+\])', r'\1', text)
 
Path('index.md').write_text(text, encoding='utf-8')
print("Done!")
