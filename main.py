from pathlib import Path

text = Path("thankful_draft2.txt").read_text(encoding="utf-8")
print(text)
