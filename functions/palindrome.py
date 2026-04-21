def is_palindrome(value):
    #convert value into string so that it works with number and string both
    value = str(value)

    reversed_value = [::-1]

    if value == reversed_value:
        return True
    else:
        return False

num = input("Enter value : ")

if is_palindrome(num):
    print("This is palindrome.")
else: 
    print("This is not palindrome.")