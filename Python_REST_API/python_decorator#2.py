#method 0
def self_multiply(num):
    return num * num

def times_ten(num):
    return num * 10


def num1 ():
    return 10

def num2 ():
    return 2


print(self_multiply(times_ten(num2())))

#method 1


def square (func):
    x = func()
    def self_times():
        return x ** 2
    return self_times

def area (func):
    def formula():
        x = func()
        return x**2 * 3.14
    return formula

@square
@area
def num3():
    return 3

print(num3())


#method 2
def add(x):
    def subtract (y):
        return y - 2*x
    x = x +10
    return subtract


adder = add(20)
print(adder(5))



