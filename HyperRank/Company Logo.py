from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

s = OrderedCounter(sorted(input()))
[print(*i) for i in s.most_common(3)]
