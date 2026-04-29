"""
Write a program that prints numbers from 1 to 10 using an infinte loop. All numbers should 
get printed in same line.
"""
# number will print in same line
i = 1
while 1:
    print(i, end=' ')
    i = i + 1
    if i > 10:
        break

