import numpy as np
k = []
n,m = map(int,(input().split(" ")))
for x in range(n):
    p = list(map(float,(input().split(" ", m))))
    k.append(p)
#print(k)
print(np.mean(k,axis=1))
print(np.var(k,axis=0))
print(round(np.std(k,axis=None),11))



    #for __ in range(p):

    #my_array = np.array.mean(p,)



