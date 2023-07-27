from itertools import groupby

t = input()
s = groupby(t)
for k,v in s:
    o = []
    [o.append(i) for i in v]
    print((len(o),k), end = ' ')
#The print part is tricky with brackets