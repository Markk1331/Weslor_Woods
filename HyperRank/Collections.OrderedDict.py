from collections import OrderedDict
l = int(input())
o = OrderedDict()
for i in range(l):
    t = input().strip().split(" ")
    price = int(t[-1])
    o_list = (" ").join(t[:-1])
    if o.get(o_list):
        o[o_list] += price
    else:
        o[o_list] = price
for keys, values in o.items():
    print(keys, values)





