t = int(input())
y = set(input().strip().split(" "))
u = int(input())
i = set(input().strip().split(" "))

q = y.difference(i)
c = 0
for i in q:
    c = c+1
print(c)