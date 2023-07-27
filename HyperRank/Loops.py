import math
if __name__ == '__main__':
    n = int(input())
    i = 0
    while 1<= n <= 20 :
        if i > n - 1:
            break
        print(i**2)
        i = i + 1  