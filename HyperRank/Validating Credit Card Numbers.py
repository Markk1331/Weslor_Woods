import re

def validator (creditcard):
    pattern = re.compile(r'(?!.*(\d)(-?\1){3})^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$')
    #pattern = re.compile(r'^(?!.*(\d)(?:\-?\1){3}.*)(?=(?:\d{16})|(?:\d{4}\-\d{4}\-\d{4}\-\d{4}))[456][\d-]{15,18}$')
    regex = re.match(pattern,creditcard)
    if bool(regex):
        return ("Valid")
    else:
        return("Invalid")

p = int(input())
for x in range(p):
    y = input()
    check = validator(y)
    print(check)