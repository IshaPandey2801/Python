# print odd number between 1 to 5
i = 1
sum = 0
while i<=5:
    if i % 2 != 0:
        sum = sum + i
    i = i + 1
print(sum)