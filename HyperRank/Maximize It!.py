from itertools import product
p,o = map(int,input().split())
q = list()
for i in range(p):
    u = list(map(int,input().split()))
    max = u[0]
    for x in u:
        if x > max:
            max = x
    q.append(max)
print(q)
t = 0
for m in q:
    t = t + m**2
j = t % o
print(int(j))