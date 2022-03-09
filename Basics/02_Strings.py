# Python Tutorial for Beginners 2: Strings
# Corey Schafer (YouTube)
# https://youtu.be/k9TUPpGqYTo?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

message_1 = 'Hello World'
message_2 = '''Thank God
It's Friday!'''

print(message_1)
print(message_1.lower())
print(message_1.upper())

print(message_2)

# Prints the length of the string
print(len(message_1))

# This is called slicing
print(message_1[0])
print(message_1[10])
print(message_1[0:5])
print(message_1[:5])
print(message_1[6:])

# Counting occurrence of an element in the string
print(message_1.count('l'))
print(message_1.find('World'))

# Replacing part of a string
new_message_1 = message_1.replace('World', 'Universe')
print(new_message_1)

# String formatting
greeting = 'Hello'
name = 'Matthew'
message_3 = greeting + ', ' + name +'. Welcome!'
print(message_3)

message_3 = '{}, {}. Welcome!'.format(greeting, name)
print(message_3)
