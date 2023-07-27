str1="Winter Olympics in 2022 will take place in Beijing China"
#Type your answer here.

lst2=list(filter(lambda x: True if x in ('123456789') else False,str1))
print(lst2)