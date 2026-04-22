"""Given the coordinates (x, y) of center of a circle and its radius, write a program 
that will determine whether a point lies inside a circle, on the circle or outside the circle. 
(Hint: Use sqrt() and pow() functions"""

"""
Concept

For a circle:

Center = (x, y)
Radius = r

For a point (px, py):

Compute distance from center:

distance= sqrt((px-x)2+(py-y)2)   


Logic
If distance < r → point is inside
If distance == r → point is on the circle
If distance > r → point is outside


"""
import math
# Input center and radius
x = float(input("Enter x-coordinate of center: "))
y = float(input("Enter y-coordinate of center: "))
r = float(input("Enter radius: "))

# Input point
px = float(input("Enter x-coordinate of point: "))
py = float(input("Enter y-coordinate of point: "))

# calculate distance


distance = math.sqrt(pow(px - x, 2) + pow(py - y, 2))

if distance<r:
    print("Point is inside the circle.")
elif distance==r:
    print("Point is on the circle.")
else:
    print("Point is outside the circle.")