"""If three sides of a triangle are entered through the keyboard, write a program to check 
whether the triangle is isosceles, equilateral, scalene or right-angled triangle.
"""
a = float(input("Enter first side of triangle : "))
b = float(input("Enter second side of triangle : "))
c = float(input("Enter third side of triangle : "))

# check if triangle is validate

if a+b>c and b+c>a and c+a>b:
    
    # conditions for equilateral, isoscales, scalene and right-angled triangle

    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or c == a:
        print("Isoscales Triangle")
    else:
        print("Scalene Triangle")

    # check right-angled triangle
    sides = sorted([a, b, c])

    if abs(sides[2]**2 -(sides[0]**2 + sides[1]**2))<0.0001:
        print("Right Angled Triangle")

else:
    print("Invalid Triangle")   
