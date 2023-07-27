from collections import Counter
l = set()
c = 0
d = Counter()
for i in range(int(input())):
    t = str(input())
    l.add(t)
    d.update({str(t)})
for x in l:
    c = c + 1
print(c)
for key, value in d.items():
    print(value, end = ' ')




