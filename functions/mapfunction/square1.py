# lambda function with map
numbers = [1, 2, 3, 4, 5]

print(list(map(lambda x: x*x, numbers)))


# by taking input from users
numbers = input("Enter the numbers: "). split()

numbers= list(map(int, numbers))

print(list(map(lambda x: x*x, numbers)))