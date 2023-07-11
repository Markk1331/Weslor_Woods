import functools

login_credential = {'username': 'markli','password':'Aa123456','user_type':'admin'}




def login_Taycan (func):
    @functools.wraps(func)
    def facial_recognition():
        if login_credential['user_type'] == "admin":
            return func()
        else:
            raise TypeError('UNAUTHORIZED ACCES DENIED')
    return facial_recognition

@login_Taycan
def admin_password():
    return 'Adm1nPassw0rd'

#login_Taycan(admin_password)

#admin_password = login_Taycan(admin_password())

print(admin_password)

