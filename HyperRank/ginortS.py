single = input().strip()

upper = []
lower = []
odd = []
even = []

for i in single:
    if i.isupper():
        upper.append(i)
    elif i.islower():
        lower.append(i)
    elif i.isnumeric() and (int(i) % 2 == 0):
        even.append(i)
    elif i.isnumeric() and (int(i)%2!=0):
        odd.append(i)

#combo = [sorted(lower),sorted(upper),sorted(odd),sorted(even)]
combo = sorted(lower) + sorted(upper) + sorted(odd) + sorted(even)

for x in combo:
    for l in x:
        print(l,end = "")


