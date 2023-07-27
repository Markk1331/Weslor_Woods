def combo_test(n):
    l = list(n)
    a = b = c = d = e = False
    for i in l:
        if i.isalnum():
            a = True
            break
        if i.isalpha():
            b = True
            break
        if i.isdigit():
            c = True
        if i.islower():
            d = True
        if i.isupper():
            e = True
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


if __name__ == '__main__':
    s = input()
    combo_test(s)