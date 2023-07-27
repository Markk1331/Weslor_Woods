s = int(input())
si = set(input().strip().split(" "))
p = int(input())
q = si.union(input().strip().split(" "))
c = 0
for i in q:
    c = c + 1
print(c)
