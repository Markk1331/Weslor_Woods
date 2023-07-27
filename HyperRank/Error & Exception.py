p = int(input())
for i in range(p):
    try:
        a, b = map(int, input().split(" "))
        print(a//b)
        #print(type(int(t[0])/int(t[1])))
    except BaseException as a:
        print ("Error Code:",a)



