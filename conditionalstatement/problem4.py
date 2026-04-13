"""
A comapny insures its drivers in the following cases:
- if the driver is married.
- if the driver is unmarried, male & above 30 years of age.
- if the driver is unmarried, female & above 25 years of age.

In all the other cases. the driver is not insured. If the marital status, sex and 
age of the driver are the inputs, write a program to determine whether the driver 
should be insured or not.
"""

ms=input("Enter the marital status : ")
sex = input("Enter sex : ")
age = int(input("Enter age : "))

if(ms == 'married') or (ms == 'unmarried' and sex == 'male' and age > 30)\
 or (sex == 'female' and age > 25):
    print("insured")

else:
    print("Not Insured")