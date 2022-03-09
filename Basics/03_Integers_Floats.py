# Python Tutorial for Beginners 3: Integers and Floats - Working with Numeric Data
# Corey Schafer (YouTube)
# https://youtu.be/khKv-8q7YmY?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

# Integers are whole numbers
num = 3
print(type(num))

# Floats have decimal positions
num = 3.14
print(type(num))

# Arithmetic Operators:
# Addition:       3 + 2
print(3 + 2)

# Subtraction:    3 - 2
print(3 - 2)

# Multiplication: 3 * 2
print(3 * 2)

# Division:       3 / 2
print(3 / 2)

# Floor Division: 3 // 2
print(3 // 2)

# Exponent:       3 ** 2
print(3 ** 2)

# Modulus:        3 % 2
# Can be used to check for even/odd number. 0 = Even, 1 = Odd
print(2 % 2)
print(3 % 2)
print(4 % 2)
print(5 % 2)

# Incrementing numbers
num = 1
num += 1
print(num)

# Absolute values
print(abs(-3))

# Rounding numbers
print(round(3.756))
print(round(3.756, 1))
print(round(3.756, 2))

# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

num_1 = 3
num_2 = 2

print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

# Converting strings to integers
num_1 = '100'
num_2 = '200'
print(num_1 + num_2)

num_1 = '100'
num_2 = '200'
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)
