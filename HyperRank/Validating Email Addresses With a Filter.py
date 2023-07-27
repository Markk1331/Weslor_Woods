import re

def fun(s):
    # return True if s is a valid email, else return False
    #pattern = r'[A-Za-z0-9-_]+@[A-Za-z0-9]+\.[A-Z|a-z]{,3}'
    pattern = re.compile(r'\b^[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,3}$\b')
    if re.fullmatch(pattern, s):
        return s


def filter_mail(emails):
    return list(filter(fun,emails))

emails = []
i = int(input())
for x in range(i):
    emails.append(input())
email = filter_mail(emails)
email.sort()
print(email)