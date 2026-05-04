# applying filter function with dictionary
# filter() to check if the age is greater than 18 

people = [
    { 'name': 'Shreya','age': 14,},
    { 'name': 'Isha','age': 25,},
    { 'name': 'Katrina','age': 32,},
]

greater_than_eighteen=list(filter(lambda person: person['age']>18, people))
print(greater_than_eighteen)

