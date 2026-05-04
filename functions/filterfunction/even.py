lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def even(x):
    return x%2==0
print(list(filter(even, lst)))