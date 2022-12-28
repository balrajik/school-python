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
    
