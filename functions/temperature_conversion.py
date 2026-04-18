# temperature conversion
def convert(temp, unit):
    """This function converts temperature between celcius and fahrenheit"""
    if unit == 'C':
        return temp * 9/5 + 32 # celcius to fahrenheit
    elif unit == 'F':
        return (temp-32) * 5/9 ## fahrenheit to celcius
    else:
        return None
    
print(convert(45, 'C'))
print(convert(87, 'F'))
    


# if we want to take input from user

# temperature conversion
def convert(temp, unit):
    """This function converts temperature between celsius and fahrenheit"""
    if unit == 'C':
        return temp * 9/5 + 32  # celsius to fahrenheit
    elif unit == 'F':
        return (temp - 32) * 5/9  # fahrenheit to celsius
    else:
        return None

# taking input from user
temp = float(input("Enter temperature: "))
unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()

result = convert(temp, unit)

if result is not None:
    print("Converted temperature:", result)
else:
    print("Invalid unit entered")