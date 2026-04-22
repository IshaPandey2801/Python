"""If the three sides of a triangle are entered through the keyboard, write a program 
to check whether the triangle is valid or not. The triangle is valid if the sum of two 
sides is greater than the largest of the three sides."""

a = float(input("Enter first side of triangle : "))
b = float(input("Enter second side of triangle : "))
c = float(input("Enter third side of triangle : "))

if a + b > c and b + c > a and c + a > b:
    print("Triangle is valid")
else:
    print("Invalid Triangle")