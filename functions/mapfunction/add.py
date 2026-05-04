# map multiple iterables
num1 = [1, 2, 3]
num2 = [4, 5, 6]

added_num = list(map(lambda x, y: x + y, num1, num2))
print(added_num)



# taking input from user
num1 = list(map(int, input("Enter first list: ").split()))
num2 = list(map(int, input("Enter second list: ").split()))

result = list(map(lambda x, y: x + y, num1, num2))
print(result)