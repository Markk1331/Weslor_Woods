from itertools import combinations

s, v = input().split()
v = int(v)
for i in range(1,v+1):
    t = list(combinations(sorted(s),i))
    [print(("").join(x)) for x in t]