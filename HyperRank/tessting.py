lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
#Type your answer here.

lst2=list(map(lambda x:abs(x),filter(lambda x:True if x<0 else False,lst1)))

print(lst2)
