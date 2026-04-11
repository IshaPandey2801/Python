"""
Percentage marks obtain by student are input through the keyboard. The student gets a division 
as per the following rules:

Percentage above or equal to 60- First Division
Percentage between 50 and 59- Second Division
Percentage between 40 and 49- Third Division
Percentage less than 40- Fail
"""

per = float(input("Enter your percentage : "))

if per>=60:
    print("First Division")
elif per>=50:
    print("Second Division")
elif per>=40:
    print("Third Division")
else:
    print("Fail")
    