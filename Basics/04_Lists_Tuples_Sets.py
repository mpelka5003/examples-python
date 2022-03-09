# Python Tutorial for Beginners 4: Lists, Tuples, and Sets
# Corey Schafer (YouTube)
# https://youtu.be/W8KRzm-HUcc?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

# LISTS
courses = ['History', 'Math', "Physics", 'CompSci']

print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses.index('CompSci'))

# -1 will always be the last item
print(courses[-1])

# Slicing
print(courses[0:2])
print(courses[:2])
print(courses[2:])

# Adding values to the list
courses.append('Art')
print(courses)
courses.insert(0,'English')
print(courses)

courses_2 = ['Calc', 'Spanish']
courses.extend(courses_2)
print(courses)

# Removing values to the list
courses.remove('Math')
print(courses)

popped = courses.pop()
print(popped)
print(courses)

# Sorting the list
courses.reverse()
print(courses)

courses.sort()
print(courses)

nums = [1, 5, 2, 4, 3]
nums.sort()
print(nums)

courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums)

# The above alters the list
# Here how you can sort and not alter

sorted_courses = sorted(courses)
print(sorted_courses)

# Misc list functions

print(min(nums))
print(max(nums))
print(sum(nums))
print('Math' in courses)
print('Art' in courses)

for course in courses:
    print(course)
for index, course in enumerate(courses):
    print(index, course)

course_str = ', '.join(courses)
print(course_str)

# TUPLES
# Similar to Lists but cannot be modified
# Use () instead of []

tuple_1 = ('History', 'Math', "Physics", 'CompSci')
print(tuple_1)

# SETS
# Unordered with no duplicates
# Use {} instead of [] or ()

cs_courses = {'History', 'Math', "Physics", 'CompSci'}
# Will have a different order with each execution
print(cs_courses)
print('Math' in cs_courses)

cs_courses_2 = {'History', 'Math', "Physics", 'CompSci', 'Math'}
# Will have a different order with each execution
print(cs_courses_2)

# What values are common or unique to multiple sets
art_courses = {'History', 'Math', "Art", 'Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))

print(cs_courses.union(art_courses))

# Creating empty lists, tuples and sets
empty_list = list()
empty_tuple = tuple()
empty_set = set() # Note the use of () rather than {}
 