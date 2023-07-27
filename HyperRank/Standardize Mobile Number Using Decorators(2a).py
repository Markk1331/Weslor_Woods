def wrapper(f):
    def fun(l):
        ten_digits = [i[-10:-5] + " " + i[-5:] for i in l]
            #ten_digits = i[-10:-5] + " " + i[-5:]
        #for x in ten_digits:
            #phone_num = "+91 " + x
        phone_num = ["+91 " + x for x in ten_digits]
        return f(phone_num)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

