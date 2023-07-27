import string
abc = string.ascii_lowercase
p = []
s = int(input())
for i in range(s):
    t = "-".join(abc[i:s])
    #print(t)
    p.append((t[::-1]+t[1:]).center(4*s-3,"-"))
print(p)
print('\n'.join(p[:0:-1]+p))