# Python Tutorial for Beginners 7: Loops and Iterations - For/While Loops
# Corey Schafer (YouTube)
# https://youtu.be/6iF8Xb7Z3wQ?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

# break statement
for num in nums:
    if num ==3:
        print('Found It!')
        break
    print(num)

# continue statement
for num in nums:
    if num ==3:
        print('Found It!')
        continue
    print(num)

# Nested loops
for num in nums:
    for letter in 'abc':
        print(num, letter)

# Loop ranges
for r in range(1, 11):
    print(r)

# While loops
x = 0

while x < 10:
    print(x)
    x += 1

x = 0

while True:
    if x == 5:
        break
    print(x)
    x += 1
