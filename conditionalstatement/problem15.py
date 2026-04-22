"""Given a point (x, y), write a program to find out if it lies on the X-axis, Y-axis or on the 
origin."""

x = float(input("Enter the value of x : "))
y = float(input("Enter the value of y : "))

if x == 0 and y == 0:
    print("Point lies on origin ")

elif x == 0:
    print("Point lies on y-axis")

elif y == 0:
    print("Point lies on x-axis")

else:
    print("Point doesn't lies on any axis")