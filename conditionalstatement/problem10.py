"""Write a program to check whether a triangle is valid or not, when the three angles of 
tringle are entered through keyboard."""

a = float(input("Enter first angle of triangle : "))
b = float(input("Enter second angle of triangle : "))
c = float(input("Enter third angle of triangle : "))

if a > 0 and b > 0 and c > 0 and abs(a + b + c - 180) < 0.0001:
    print("This is a Triangle")
else:
    print("This is not a Triangle")