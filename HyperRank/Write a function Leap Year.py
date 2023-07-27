def is_leap(year):
    leap = False
    while 1900 <= year <= 10**5 :
        if int(year) % 4 != 0:
            return leap
        else:
            if int(year) % 100 == 0 and int(year) % 400 != 0:
                leap = False
                return leap
            leap = True
            return leap
        leap = False
year = int(input())
print(is_leap(year))