from itertools import combinations
s = int(input())
t = input().split(" ")
k = int(input())
p = list(combinations(t,k))
c = 0
for i in p:
    if "a" in i:
        c = c +1
t = c/(len(p))
print(round(t,4))