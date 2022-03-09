# Python Tutorial for Beginners 6: Conditionals and Booleans - If, Else, and Elif Statements
# Corey Schafer (YouTube)
# https://youtu.be/DZwmZ8Usvnk?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

language = 'Python'
# language = 'Java'
# language = 'JavaScript'
# language = 'Rust'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')

# and
# or
# not

user = 'Admin'
logged_in = True
# logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

# Object Identity:  is
# Checks for identical in memory, not contents

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))
print(a == b) # Will be True as the values are identical
print(a is b) # Will be False as the locations in memory are not identical

a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
print(a == b) # Will be True as the values are identical
print(a is b) # Will be True as the locations are identical

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
