b = input("Enter binary number : ")

i = 0

for digit in b:
    i = i * 2 + int(digit)
print("Decimal value : ", i)