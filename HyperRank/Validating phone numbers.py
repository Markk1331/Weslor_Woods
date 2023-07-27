import re
s = int(input())

for _ in range(s):
    n = str(input())
    regex = re.compile(r'^[789]\d{9}$')
    match = re.match(regex,n)
    if bool(match):
        print("YES")
    else:
        print("NO")