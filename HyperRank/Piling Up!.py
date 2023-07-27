t = int(input())
for i in range(t):
    y = int(input())
    t = list(map(int,input().split(" ")))
    stack=[]
    for u in range(y):
        if t[0]>=t[-1]:
            stack += [t.pop(0)]
        else:
            stack += [t.pop(-1)]
    print(stack)
    if stack == sorted(stack, reverse = True):
        print("Yes")
    else:
        print("No")
    print(sorted(stack, reverse = True))

