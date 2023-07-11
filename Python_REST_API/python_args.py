
number = "1+5/3+2-5+7/2*2*3/2+2-5*6+0.5"

def multiply(*args):
    total = 1
    for i in args:
        total *= i
    return total

def divison(*args):
    total = 1
    for i in args:
        total *= i
    return total

def apply(*args, operator):
    total = 0
    if operator=="+":
        sum(args)
    if operator =="-":
        total -= args
    if operator =="/":
        return divison(*args)
    elif operator =="*":
        return multiply(*args)
print(apply(1,3,5,7,operator="*"))



