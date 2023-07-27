def wrapper(f):
    def fun(l):
        s = "+91 "
        w=[]
        for i in l:
            if len(i) == 10:
                w.append(s+i)
            if len(i) == 11:
                w.append(s+i[1:])
            if len(i) == 12:
                w.append(s+i[2:])
        for x in w:
            w = sorted(w)
        print (w)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)