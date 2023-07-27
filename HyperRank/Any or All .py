z = int(input())
x = input().split()
lst = list()
for i in x:
    lst.append(int(i)>0)
lis = list()
if all(lst):
    for i in x:
        lis.append(i == i[::-1])
print(any(lis))