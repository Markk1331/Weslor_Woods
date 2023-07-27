s = input()
o = list(map(int,input().split(" ")))
t = set()
p = set()
for i in o:
    if i in t:
        p.add(i)
    else:
        t.add(i)
k = t.difference(p)
print(*k)

