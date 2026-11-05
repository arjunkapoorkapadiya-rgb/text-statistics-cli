"""Summarize a UTF-8 text file as JSON."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re

p = argparse.ArgumentParser(description=__doc__)
p.add_argument("file", type=Path)
p.add_argument("--top", type=int, default=10)
a = p.parse_args()

if not 1 <= a.top <= 100:
    p.error("--top must be between 1 and 100")

try:
    text = a.file.read_text(encoding="utf-8-sig")
except (OSError, UnicodeError) as error:
    p.exit(2, f"Cannot read text: {error}\n")

words = re.findall(r"[^\W_]+(?:['’][^\W_]+)*", text.casefold())
print(json.dumps({
    "characters": len(text),
    "lines": len(text.splitlines()),
    "words": len(words),
    "unique_words": len(set(words)),
    "top_words": Counter(words).most_common(a.top)
}, ensure_ascii=False, indent=2))