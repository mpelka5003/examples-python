# Python Tutorial for Beginners 8: Functions
# Corey Schafer (YouTube)
# https://youtu.be/9Os0o3wzS_I?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

# Simple function
def hello_func():
    print('Hello Function!')

hello_func()

def hello_func():
    return 'Hello Function'

print(hello_func())
print(hello_func().upper())

# More complex function
def hello_func(greeting, name = 'You'):
    return '{} {}'.format(greeting, name)

print(hello_func('Hi,'))

def hello_func(greeting, name = 'You'):
    return '{} {}'.format(greeting, name)

print(hello_func('Hi,', name = 'Corey'))

# Function to determine number of days in a month
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2017))
print(is_leap(2020))

print(days_in_month(2017, 2))
print(days_in_month(2020, 2))
print(days_in_month(2020, 5))
