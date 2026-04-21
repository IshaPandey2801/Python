"""If ages of Ram, Shyam and Ajay are input through keyboard. Write a program to determine 
the youngest of three"""

Ram = int(input("Enter age of Ram : "))
Shyam = int(input("Enter age of Shyam : "))
Ajay = int(input("Enter age of Ajay : "))
if Ram < Shyam and Ram < Ajay:
    print("Ram is Younger.")
elif Shyam < Ram and Shyam < Ajay:
    print("Shyam is younger.")
elif Ajay < Ram and Ajay < Shyam:
    print("Ajay is younger.")
else:
    pass