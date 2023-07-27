s, v = map(int,input().split( ))
p = list()
for i in range(v):
    p.append(list(map(float,input().split( ))))
    result = list(map(list,zip(*p)))
    #Displaying in list,  each for-loop "p" value is seperated and inserted into list ordering in turn
    print(result)
for o in range(len(result)):
    #range(len()) = assign each index from the list to the fixed amount of loop variable in turn
    print(float(sum(result[o])/v))