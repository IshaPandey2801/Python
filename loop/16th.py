# sum of all even number from 1 to 10

i = 1
sum = 0
while i <= 10:
    if i % 2 == 0:
        sum +=  i
    i = i + 1
print("Sum = ", sum)