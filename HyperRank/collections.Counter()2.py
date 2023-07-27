from collections import Counter
shoe_size = []
price = []
shopping = {}
numba = int(input())
shoes_quan = list(map(int,input().split(" ",numba)))
client = int(input())

sum = 0
shoes_avail = Counter(shoes_quan)

#shoe avail list is there, so using for loop to add one client at a time to deduct the exisiting shoe avail list.
# Only run another loop with amount is greater than 0

for _ in range(client):
    p, v = map(int,input().split())
    shoe_size.append(p)
    price.append(v)
    while shoes_avail[p] > 0:
        sum += v
        shoes_avail[p] -= 1

for i in range(len(shoe_size)):
    shopping[shoe_size[i]] = price[i]


print (shoes_avail)
print (sum)
print(shopping)



