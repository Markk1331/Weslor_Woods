from itertools import permutations

p, v = input().split()
ko = list(permutations(p,int(v)))
#print(ko)
ko.sort()
[print("".join(i)) for i in ko]

