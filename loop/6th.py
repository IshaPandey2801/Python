"""A for loop is very populary used to iterate through a string, list, tuple, set
or dictionary, as shown below:"""

for char in 'Leopard':
    print(char)
for animal in ['Cat', 'Dog', 'Cow', 'Goat', 'Horse']:
    print(animal)
for flower in ('Rose', 'Lily', 'Lotus'):
    print(flower)
for num in {10, 20, 30, 40}:
    print(num)
for key, value in{'A101' : 'Shreya', 'A102' : 'Isha', 'A103' : 'Divya'}.items():
    print(key, value)