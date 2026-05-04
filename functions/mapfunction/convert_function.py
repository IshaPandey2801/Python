# map() to convert list of strings to integers
# use map to convert string to integers

str_number = ['1', '2', '3']
int_number = list(map(int, str_number))

print(int_number)


# second conversion
word = ['apple', 'banana', 'orange']
upper_word = list(map(str.upper, word)) # convert lower case into uppercase
print(upper_word)