print("Hey, This is Kamal")

# Multiple variable assignment
x, y = ('abc', 123)

# -----------------------------------------
# Comments
# This is a single line comment
"""
This is a multiline comment
"""
'''
This is also a multiline comment
'''

# Variables are case sensitive and must start with a letter or underscore
x = 123
x = 12.5
x = 'This is a string'
x = True

# Print is used to output data
# Type is used to find out the datatype of a variable
print(type(x))

# Basic Operations
a = 10
b = 20

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

# --------------------------------------------
# String Manipulation
name = 'Kamal Teja'

# Normal 
print("Hi, This is " + name)
# using placeholders and format method
print("Hi, This is {x}".format(x = name))
# F Strings
print(f'Hi, This is {name}')

# String Methods
print(len(name))
print(name.upper())

# ------------------------------------------
# Typecasting
y = int('123')
print(type(y))

# -------------------------------------------
# Conditionals
a = 10
b = 20

if a > b:
    print("a is greater than b") 
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

# <, >, <=, >=, !=, ==

if a < b and a == 10:
    print('a is less than b and is equal to 10')

if not(a<b):
    print("dummy text")

# ----------------------------------------------
# Basic data structures
# List - ordered, changeable, allows duplicate members
test_list = [1, 2, 3, 'kamal']
# Created using constructor
test_list = list((1, 2, 3))

print(type(test_list))

print(test_list[3])
print(len(test_list))

# Add to the list
test_list.append("teja")
print(test_list)

# Remove from the list
test_list.pop(2)
print(test_list)

# Change existing value
test_list[1] = 'test'
print(test_list)

# ------------------------------------------------
# Tuple - ordered, unchangeable, allows duplicate members
test_tuple = (1, 2, 3, 'Kamal')
test_tuple = tuple((1, 2, 3))

print(type(test_tuple))

# Single valued tuple needs a trailing comma
test_list = ['test']
test_tuple = ('test',)

print(test_tuple[0])

test_tuple[0] = 'kamal'

del test_tuple
print(test_tuple)

print(len(test_tuple))

# -------------------------------------------------
# Set - unordered, unindexed, no duplicate members
test_set = {'1', 2, 3}
test_set = set(('1', 2, 3))

print(type(test_set))
print(test_set)

test_set.add('test')
print(test_set)

print('test' in test_set)

test_set.remove('test')
print(test_set)

# Doesnt allow duplicates
print(test_set)
test_set.add(2)
print(test_set)

# ------------------------------------------------------
# Dictionary - unordered, indexed, changeable, no duplicate members
test_dict = {
    "name": "Kamal Teja",
    "age": 21
}
test_dict = dict(name= "Kamal Teja", age= 21)

print(type(test_dict))

test_dict['nickname'] = 'kamal'
print(test_dict)

# Print all keys , values and items
print(test_dict.keys())
print(test_dict.values())
print(test_dict.items())

del(test_dict['nickname'])
print(test_dict)
print(len(test_dict))

# Nested dictionary / list of dictionaries - Similar to JSON
nested_dict = [
    {
        "name": "Kamal Teja",
        "age": 21
    },
    {
        "name": "Test",
        "age": 20
    }
]

print(nested_dict[0]['name'])

# -----------------------------------------------------------
# Advanced Condtionals
a = [1, 2, 3, 'test']
x = 10
y = 10

if 'test' in a:
    print("test is in a") 
elif 'test' not in a:
    print("...")

if x is y:
    print("x is y")
else:
    print("x is not y")

# -----------------------------------------------------------
# Loops
# For
x = [1, 2, 3]
for num in x:
    if num == 2:
        continue
    print(num)

for num in range(len(x)):
    print(x[num])

# While
count = 0
while True:
    print('Hi')
    count += 1
    if(count > 3):
        break

# -----------------------------------------------------------
# Functions
def test(name='Test'):
    print(f'Hi , This is {name}')
    return 'completed'

x = test('Kamal')
print(x)

# ------------------------------------------------------------
# Modules
import random

for i in range(0, 5):
    print(random.random())

for i in range(0, 10):
    print(random.randrange(0, 100))

# pip3 install modulename
# pypi.org is the website to search for python modules

# --------------------------------------------------------------
# Files
# Read from a file
testFile = open('test.txt', 'r')
print(testFile.read())
testFile.close()

# Write to a file
testFile = open('test.txt', 'w')
print(testFile.name)

testFile.write("Hi, This is Kamal")
testFile.close()

# Append to a file
testFile = open('test.txt', 'a')
print(testFile.name)

testFile.write("Hi, This is Kamal")
testFile.close()