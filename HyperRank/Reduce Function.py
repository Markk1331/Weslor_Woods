from fractions import Fraction
from functools import reduce

def product(fracs):
    #t = # complete this line with a reduce statement
    t = reduce(lambda numerator,denominator: numerator*denominator,fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    i = int(input())
    for u in range(i):
        fracs.append(Fraction(*map(int,input().split(" "))))
    result = product(fracs)
    print(*result)

