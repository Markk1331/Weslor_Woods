a = int(input())
for i in range(a):
    x = int(input())
    p = set(map(int,input().split(" ")))
    x = int(input())
    o = set(map(int,input().split(" ")))
    print(bool(p.issubset(o)))