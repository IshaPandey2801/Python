# Count how many numbers between 1–100 are prime
count = 0

for num in range(2, 101):
    i = 2
    while i * i <= num:
        if num % i == 0:
            break
        i += 1
    else:
        print(num)
        count += 1

print("Total:", count)