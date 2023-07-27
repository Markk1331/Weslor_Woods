s = list(input())
d = {}

for i in s:
    d[i]= s.count(i)
p = dict(sorted(d.items()))
print(p)
#print(p[0])
q = {}
q = sorted(p.items(), key = lambda x:x[1], reverse = True)
print(q)
print(*q[0])
print(*q[1])
print(*q[2])
