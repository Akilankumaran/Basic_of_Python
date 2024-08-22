def Validate():
    s_username = "EMC"
    s_password = "123"
    a = input("uname: ")
    b = input("Password: ")
    if (s_username == a and s_password == b):
        return True
    else:
        return False
Trust = Validate()
print(Trust)
