import collections
from collections import Counter
sum = 0

num_shoe = int(input())

stocks = collections.Counter(map(int, input().split()))
customers = int(input())
for x in range(customers):
    size, price = map(int, input().split())
    if stocks[size]:
        sum = sum + price
        stocks[size] = stocks[size] - 1
print(sum)
