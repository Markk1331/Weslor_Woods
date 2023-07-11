lst = [1,3,5,7,9]

#1 way
double = [(lambda x: x*2)(x) for x in lst]
print(double)

#2 way
triple = list(map(lambda x: x*3,lst))
print(triple)

#3 way
def quad (x):
    return x*4
quadruple = list(map(quad,lst))
print(quadruple)