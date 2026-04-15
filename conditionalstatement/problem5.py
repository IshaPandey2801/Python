"""
Suppose there are four  flag variables w, x, y, z. Write a program in python to check in multiple ways
whether one of them is true.
"""


w = 1
x = 0
y = 0
z = 0

## Method 1:
if w == 1 or x == 1 or y == 1 or z ==1:
    print("True")
else:
    print("False")



## Method 2:
if w or x or y or z:
    print("True")

else:
    print("False")



### Method 3:
if any((w, x, y, z)):
    print("True")
else:
    print("False")