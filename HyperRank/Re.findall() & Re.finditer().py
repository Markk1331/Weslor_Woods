import re

ans = str(input())
pattern = re.compile(r'(?<=[^aeiou])([aeiou]{2,})[^aeiou]', flags=re.IGNORECASE)

match = list(map(lambda x : x.group(1), re.finditer(pattern, ans)))
if match:
    print(*match,sep="\n")
else:
    print(-1)



