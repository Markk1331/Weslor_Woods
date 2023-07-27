y = set(map(int,input().split(" ")))
t = int(input())
superset = True
for i in range(t):
    r = set(map(int,input().split(" ")))
    if not y.issuperset(r):
        superset = False
print(superset)



