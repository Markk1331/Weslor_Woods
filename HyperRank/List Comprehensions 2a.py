if __name__ == '__main__':
    x = int(input("Insert X: "))
    y = int(input("Insert Y: "))
    z = int(input("Insert Z: "))
    n = int(input("Insert N: "))
    ans = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print (ans)