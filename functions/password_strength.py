
def is_password_strong(password):
    """this is resposible for checking whether password is strong or not"""
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*_()-' for char in password):
        return False
    return True

# calling the function

"""print(is_password_strong("WeakPwd"))
print(is_password_strong("Str0ng_Pwd"))"""

password = input("Enter password : ")
if is_password_strong(password):
    print("Strong password ✅")
else:
    print("Weak password ❌")

print(is_password_strong(password))