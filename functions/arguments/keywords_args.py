# keyword arguments
# in keywords arguments all the value will be in the form of key value pairs
def print_details(**kwargs): # it is given by double star **
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_details(name = "Shreya", age = 24, country = "India")
