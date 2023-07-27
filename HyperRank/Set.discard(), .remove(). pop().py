n = int(input())
s = set(map(int, input().split()))
u = int(input())
c = 0
for x in range(u):
    t = input().strip().split(" ")
    if t[0] == "pop":
        s.pop()
    elif t[0] == "remove":
        s.remove(int(t[1]))
    elif t[0] == "discard":
        s.discard(int(t[1]))
for i in s:
    c = c + i
print(c)
