from collections import deque
d = deque()
n = int(input())
for i in range(n):
    x = input().split(" ")
    if x[0] == "append":
        d.append(x[1])
    elif x[0] == "appendleft":
        d.appendleft(x[1])
    elif x[0] == "pop":
        d.pop()
    elif x[0] == "popleft":
        d.popleft()
    elif x[0] == "clear":
        d.clear()
    elif x[0] == "remove":
        d.remove(x[1])
    elif x[0] == "reverse":
        d.reverse()
    elif x[0] == "rotate":
        d.rotate(x[1])
    elif x[0] == "extend":
        d.extend(x[1])
print(" ".join(d))

