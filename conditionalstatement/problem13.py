"""Given three points (x1, y1), (x2, y2) and (x3, y3), write a program to check if all 
the three points fall on one straight line."""

"""Logic of this code:
Concept (very important)

Three points lie on a straight line if their slopes are equal

Condition:
(y2-y1)/(x2-x1) = (y3-y2)/(x3-x2)

Problem with slope method
If x2 - x1 = 0 → division error 
So better to avoid division

Best method (cross multiplication)

Use:

(y2-y1)(x3-x2)=(y3-y2)(x2-x1)
"""

x1 = float(input("Enter the value of x1 : "))
y1 = float(input("Enter the value of y1 : "))

x2 = float(input("Enter the value of x2 : "))
y2 = float(input("Enter the value of y2 : "))

x3 = float(input("Enter the value of x3 : "))
y3 = float(input("Enter the value of y3 : "))

if (y2-y1) * (x2-x1) == (y3-y2) * (x3-x2):
    print("Points lies on a straigth line.")
else:
    print("Points doesn't lies on a straigth line.")