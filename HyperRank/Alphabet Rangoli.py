import string
alpha = string.ascii_lowercase
k = int(input())
L = []
for i in range(k):
    t = "-".join(alpha[i:k])
#print(t)
    L.append((t[::-1]+t[1:]).center(4*k-3,"-"))
#print(s)
print('\n'.join(L[:0:-1]+L))
#print(L)