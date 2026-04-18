# combining positioanl and keyword arguments

def print_details(*args, **kwargs): 
    for val in args:
        print(val)

    for key, value in kwargs.items():
        print(f"{key} : {value}")

"""print_details(1,2,3,name = "Shreya", age = 24, country = "India",4,5,6,"Shreya") 
this will show error because positional arguments cannot be placed after keyword arguments"""

print_details(1,2,3,4,5,6,"Shreya", name = "Shreya", age = 24, country = "India",) 



### return function
def multiply(a, b):
    return a * b

print(multiply(2,4))


def multiply(a, b):
    return a * b, a  ## we can also return multiple parameter from a function

print(multiply(2,4))

