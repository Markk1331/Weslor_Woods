from itertools import product
k, m = list(map(int,input().split()))
l = list()
for i in range(k):
    l.append(list(map(int,input().split()))[1:])

num = lambda x:x**2

li = list()
for j in l:
    li.append(list(map(num,j)))

mar = list()
for h in list(product(*li)):
    mar.append(sum(h)%m)

print(max(mar))
print(mar)




