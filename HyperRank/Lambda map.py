cube = lambda x: x**3


def fibonacci(n):

    k = 0

    #0,1,1,2,3,5,8,13
    #n[0] = first_term = 0
    #n[1] = second_term = 1
    #n[2]= first_term + second_term
    #n[3] = second_term + n[2]
    #n[4] = n[2] + n[3}
    #n[i] = n[x-2] + n[x-1]
    g = []
    if n == 0:
        return g
    else:
        for x in range(n):
            b = [0,1]
            #for u in range(x,1):
                #b.append(0)
                #for t in range(x+1,2,):
                    #b.append(1)
            for a in range(n-2):
                k = b[-2] + b[-1]
                b.append(k)
            return list(b[0:n])


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
