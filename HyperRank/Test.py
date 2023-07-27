str1="Winter Olympics in 2022 will take place in Beijing China"

lst=list(filter(lambda x: True if x.lower() in ('aeiou') else False,str1))



print(lst)