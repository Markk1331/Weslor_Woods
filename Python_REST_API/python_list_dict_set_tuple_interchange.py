list = [1,2,3,4,5]
tuple = (1,2,3,4,5)
set = {1,2,3,4,5}

tuple_inside_list = [(1,2,3),(4,5,6)]

dictionary_inside_list = [{'b':1,'b':2,'c':3,'d':4,'e':5}]

#method sorted = turn into list

I_phone = {'name':'Apple', 'price':50}
new_lst = []


#containing a dictionary into a list
for i in I_phone.items():
    new_lst.append(i)
print(new_lst)

#putting a set into a list
lst2 = []
p = [(1,2),(3,4),(5,6),(7,8),(9,10)]
for i in p:
    lst2.append(i)
print(lst2)

#containing a list into dictionary
lss = ['a',1,'b',2,'c',3,'d',4,'e',5,'f',6]
new_dict = {lss[i]:lss[i+1] for i in range(0,len(lss),2)}

snew_dict = sorted(new_dict.items(),reverse = True)

print(snew_dict)

#changing List[{dictionary}] into dictionary
car = [{'911': 150}, {'Macan': 275}, {'Taycan': 200}, {'718': 535}]
car_dict = {}

#long way
for x in car:
    for k,v in x.items():
        car_dict[k]=v
print(car_dict)
#short way
car_dictt = {k:v for c in car for k,v in c.items()}
print(car_dictt)