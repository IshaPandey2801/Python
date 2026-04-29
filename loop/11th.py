"""
Write a program that receives 3 sets of value of p, n and r and calculate the simple intrest 
for each..
"""

i = 1
while i<=3:
    p = float(input("Enter the value of p : "))
    n = int(input("Enter the value of n : "))
    r = float(input("Enter the value of r : "))
    si = (p * n * r)/100
    print("Simple Intrest = Rs. " + str(si))
    i = i + 1