def check_password(pw):
    has_number = False
    has_upper = False
    has_symbol = False

    for c in pw:
        if c.isdigit():
            has_number = True
        if c.isupper():
            has_upper = True
        if  not c.isalnum():
            has_symbol = True
    if len(pw) >= 8 and has_number and has_upper and has_symbol:
        return "PASSWORD OK"
    else: 
        return "PASSWORD NOT OK"

password = input("Enter your PASSWORD: ")
result = check_password(password)
print(result)