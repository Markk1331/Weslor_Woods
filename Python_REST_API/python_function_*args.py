def names(*args):
    real_name = [x for x in args]
    for _ in real_name:
        print(f'{_} is handsome')

names('mark','abc','jacquline','stephen','kwok','on999')