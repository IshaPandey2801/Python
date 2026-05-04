# filter function with lambda function]
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

greater_than_five=list(filter(lambda x: x>5, numbers))
print(greater_than_five)