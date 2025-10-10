import re

txt = "apple,samsung,xiaomi,blackberry"
pattern = r","

res = re.split(pattern, txt)

print(res)

for i in res:
    print(i)