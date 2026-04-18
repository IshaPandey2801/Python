# positional length arguments

def print_numbers(*args): #x it is given by single star
    for numbers in args:
        print(numbers)

print_numbers(1,2,3,4,5,6,"Shreya")  #this all parameters are positional arguments