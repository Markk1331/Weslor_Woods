from collections import OrderedDict as OD

dict = OD()
#num = []
#shopping = []
order = int(input())
for _ in range(order):
    wish = input().strip().split()
    #shopping.append(" ".join(wish[0:-1]))
    #num.append(wish[-1])
    goods = " ".join(wish[0:-1])
    cost = int(wish[-1])
    if dict.get(goods):
        dict[goods] += cost
    else:
        dict[goods] = cost

    #for i in range(len(shopping)):
        #dict[shopping[i]] = num[i]
print(dict)