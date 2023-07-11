car = [{'911': 150}, {'Macan': 275}, {'Taycan': 200}, {'718': 535}]

car_dict = {}

for x in car:
    for k,v in x.items():
        car_dict[k]=v

print(car_dict)

car_dictt = {k:v for c in car for k,v in c.items()}

print(car_dictt)