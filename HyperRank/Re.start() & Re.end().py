import re

S = str(input())
K = str(input())

regex = re.compile(f'(?={K})')
match = re.finditer(regex,S)

if re.search(regex,S):
    for i in match:
        print((i.start(),i.end()+len(K)-1))
else:
    print((-1,-1))
