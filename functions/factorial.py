def factorial(n):
    # base case
    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)

# user input
num = float(input("Enter the number : "))

if n<0:
    print(f"Factorial of negative is not define.")
else:
    result = factorial(num)
    print(f"Factorial of {num} is {result}")