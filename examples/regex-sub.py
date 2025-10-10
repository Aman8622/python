import re

txt = "The quick brown fox"
pattern = r"brown"
substitute = "orange"

res = re.sub(pattern, substitute, txt)
print(res)