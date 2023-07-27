from itertools import product

#x = int(input()).split()
#y = int(input()).strip().split()
x = map(int,input().split())
y = map(int,input().split())

clus = product(x,y)
for i in clus:
    print(i, end = ' ')
