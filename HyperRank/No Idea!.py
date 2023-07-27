n, m = map(int,input().split(" "))
index = list(map(int,input().strip().split(" ")))
c = 0

a = set(map(int,input().split(" ")))
b = set(map(int,input().split(" ")))
for x in index:
    if x in a:
        c = c + 1
    elif x in b:
        c = c -1
print(c)

