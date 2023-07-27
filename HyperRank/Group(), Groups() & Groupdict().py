import re

k = []

#consecutive = re.compile(r'(?!.*(\d)\1{3,}).*$')
n = str(input())
for i in re.finditer(r'([a-zA-Z0-9])\1',n):
    k.append(i.group(1))

if not k:
    print(-1)
else:
    print(k[0])



