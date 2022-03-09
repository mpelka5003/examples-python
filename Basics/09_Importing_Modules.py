# Python Tutorial for Beginners 9: Importing Modules and Exploring The Standard Library
# Corey Schafer (YouTube)
# https://youtu.be/CqvZ3vGoGs0?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

# First option
import my_module

courses = ['History', 'Math', 'Physics', 'CompSci']

index = my_module.find_index(courses, "Math")
print(index)

#Second option
import my_module as mod

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mod.find_index(courses, "Math")
print(index)

# Third option
from my_module import find_index

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, "Math")
print(index)

# Finding module directories
import sys
print(sys.path)

# Importing modules from the Standard Library
import random
courses = ['History', 'Math', 'Physics', 'CompSci']
random_course = random.choice(courses)
print(random_course)

import math
rads = math.radians(90)
print(rads)

import datetime

today = datetime.date.today()
print(today)

import os
print(os.getcwd())
print(os.__file__)
