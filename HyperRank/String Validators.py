def combo_test(n):
    print(any(k.isalnum()for k in n))
    print(any(k.isalpha() for k in n))
    print(any(k.isdigit() for k in n))
    print(any(k.islower() for k in n))
    print(any(k.isupper() for k in n))



if __name__ == '__main__':
    s = input()
    combo_test(s)