def average(array):
    p = set()
    c = 0
    y = 0
    for x in array:
        p.add(x)
    for u in p:
        y = y + u
    #print(y)
    for n in range(len(p)):
        c = c +1
    answer = y/c
    return answer




if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)