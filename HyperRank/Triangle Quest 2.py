for i in range(1,int(input())+1):
    print(*list(range(1,i+1))+list(range(i-1,0,-1)))
    #mathmatical formula
    print(((10 ** i - 1) // 9) ** 2)
