"""Ramanujan number is the smallest number that can be expressed as the sum of two cubes in two different ways. 
Write a program to print such numbers to the reasonable limit.
"""


limit = 5000

for num in range(1, limit + 1):
    pairs = []

    for i in range(1, int(num ** (1 / 3)) + 2):
        for j in range(i, int(num ** (1 / 3)) + 2):

            if i**3 + j**3 == num:
                pairs.append((i, j))

    if len(pairs) >= 2:
        print(f"{num} = ", end="")

        for k in range(len(pairs)):
            a, b = pairs[k]
            print(f"{a}³ + {b}³", end="")

            if k != len(pairs) - 1:
                print(" = ", end="")

        print()