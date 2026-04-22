"""Given the length and breadth of rectangle, write a program to find whether the area of 
the rectangle is greater than its perimeter. For example, the area of the rectangle with 
length = 5 and breadth = 4 is greater than its perimeter. """

length = float(input("Enter the length of Rectangle : "))
breadth = float(input("Enter the breadth of Rectangle : "))

area = length * breadth
perimeter = 2*(length+breadth)

if area > perimeter:
    print("Area of rectangle is greater than perimeter.")
elif area < perimeter:
    print("Perimeter of rectangle is greater than area.")
else:
    print("Area and perimeter are equal.")