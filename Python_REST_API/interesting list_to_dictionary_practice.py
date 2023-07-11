def add(number):
    total = 0
    for i in number:
        total += i
    return total

#o = map(int,input().split(" "))

#print(add(o))

print((lambda x,y : x+y) (5,2))

lst = ['a',6,'b',5,'c',10,'d',-10]
dict_llst = {}
for i in range(0,len(lst)-2,1):
    dict_llst[lst[i]] = lst[i+2]






dict_lst = {lst[i]:[lst[i+1]] for i in range(0,len(lst),2)}

print(dict_llst)


