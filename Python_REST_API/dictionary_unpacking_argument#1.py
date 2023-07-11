

def adds(x, y):
    return x + y

browser = {"x":5, "y":-2}
#1 method_1
print(adds(x=browser['a'], y=browser['z']))

#2 method_2
print(adds(**browser))

