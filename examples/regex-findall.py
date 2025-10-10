import re

txt = "The quick brown fox"
pattern = r"brown"

search = re.findall(pattern, txt)

if search:
    print("Pattern found")
else:
    print("Pattern not found")