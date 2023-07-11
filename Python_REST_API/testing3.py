x = 5 , 11

#print(type(x))

y = {'kel' : 5, 'Geo' : 7 }

for i in y.values():
    print(i)
#print(type(y.values()))

def add (x):
    y = sum(x)
    return(y)

o = map(int,input().split(" "))

print(add(o))