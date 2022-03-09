# Python Tutorial for Beginners 5: Dictionaries - Working with Key-Value Pairs
# Corey Schafer (YouTube)
# https://youtu.be/daefaLgNkw0?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

# Dictionaries use "keys" and "values"

student = {'name': 'Johm', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)
print(student['name'])
print(student.get('phone'))
print(student.get('phone', 'Not Found'))

# Adding a key
student['phone'] = '555-5555'
print(student.get('phone'))
print(student)

# Multiple updates
student.update({'name': 'Jane', 'age': 21, 'gender': 'female'})
print(student)

# Deleting a key
del student['age']
print(student)

# Misc functions
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

# Loops
for key, value in student.items():
    print(key, value)
