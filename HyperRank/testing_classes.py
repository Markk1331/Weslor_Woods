class myfunc:
    def power(x, y):
        return (x ** y)

    def __str__(self):
        return ("This class will consist of mathematical operations. We only have one function named power currently.")


ans1 = myfunc.power(5, 6)
ans2 = myfunc()
print(ans1)
print(ans2)