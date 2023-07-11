info = [("bob", 3005), ("Rolf", 1536), ("Kay",9016)]

user_info = {x[0]:x[1] for x in info}

user_info["apple"] = 7891

username_in = input().lower().strip(" ")
password_in = int(input().lower())

if username_in in user_info.keys():
    print(f'{username_in} is correct')
    if password_in in user_info.values():
        print("Logined")
    else:
        print("password not matched")
else:
    print("not matched id")

