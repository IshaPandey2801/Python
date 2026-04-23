
num = int(input("Enter the number : "))
i = 2 
while i<=num-1:
    if num % i == 0:
        print(num, 'is not a prime')
        break
    i = i + 1
else:
    print(num, 'is prime number')