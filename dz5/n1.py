def check_password(password):
    if len(password) < 6:      
        return False
    elif password.isalpha():
        return False
    elif password.isdigit():
        return False
    elif password.lower().find("password") >= 0:
        return False
    else:
        return True
    

if __name__ == "__main__":   
    if check_password(input("Введите пароль: ")):
        print("Пароль корректен")
    else:
        print("Пароль не корректен")

