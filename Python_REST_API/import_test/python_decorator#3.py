import functools
Pycharm_login = {'username': 'chanpigpig','user_type':'admin'}


def secured_login(user_type):

    def credential_check(func):
        @functools.wraps(func)
        def login_info(*args,**kwargs):

            if args:
                for i in args :
                    if i == 'markli':
                        return('No password needed. Welcome Boss')

            elif kwargs:
                for k,v in kwargs.items():
                    if v == 'guest':
                        return('guess password will last for 30 days after login')

            else:

                if Pycharm_login['user_type'] == user_type:
                    return func(*args,**kwargs)
                else:
                    return (f'Invalid Access of {user_type} due to incorrect access ')

        return login_info

    return credential_check


@secured_login('admin')
def system_password():
    return 'Adm1nPassw0rd'

@secured_login('user')
def user_password():
    return 'Aa123456'



print(system_password('markli'))
print(user_password(name='guest'))
print(system_password())
#print(user_password())