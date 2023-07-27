lst1=[1000, 500, 600, 700, 5000, 90000, 17500]
#Type your answer here.

lst2=list(map(lambda x: x+200, filter(lambda x:True if x<8000 else False,lst1)))
lst3 = [x+200 for x in lst2]
#print(lst3)
print(lst2)
