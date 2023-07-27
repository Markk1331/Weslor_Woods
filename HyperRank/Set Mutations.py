p = int(input())
l = set(map(int,input().split()))
o = int(input())
for i in range(o):
    u = input().split()
    j = set(map(int,input().split()))
    if u[0] == "intersection_update":
        l.intersection_update(j)
    if u[0] == "update":
        l.update(j)
    if u[0] == "symmetric_difference_update":
        l.symmetric_difference_update(j)
    if u[0] == "difference_update":
        l.difference_update(j)
c = 0
for i in l:
    c = c + int(i)
print(c)
