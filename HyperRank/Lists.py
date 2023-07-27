if __name__ == '__main__':
    N = int(input())
    P = []
    for x in range(N):
        S = input().strip().split(" ")
        if S[0] == "print":
            print(P)
        elif S[0] == "insert":
            P.insert(int(S[1]), int(S[2]))
        elif S[0] == "append":
            P.append(int(S[1]))
        elif S[0] == "remove":
            P.remove(int(S[1]))
        elif S[0] == "sort":
            P.sort()
        elif S[0] == "pop":
            P.pop()
        elif S[0] == "reverse":
            P.reverse()


