"""
Given a number n we wish to do the following:

If n is positive - print n*n, set a flag to true
if n is negative - print n*n*n, set a flag to true
if n is 0 - do nothing
"""

n = int(input("Enter a number : "))

if n>0:
    flag = True
    print(n*n)

elif n<0:
    flag = True
    print(n*n*n)

else:
    pass

"""
What is pass?
pass is a do-nothing statement
It's used when Python expects a block, but you don't want to execute anything.
"""