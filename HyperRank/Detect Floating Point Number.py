import re
def numvalidator (num):
    pattern = re.compile(r'(^[+-]?[0-9]*\.[0-9]+([eE][+-][0-9]+)?$)')
    regex = re.match(pattern,num)
    return bool(regex)

n = int(input())
for i in range(n):
    p = str(input())
    print(numvalidator(p))
