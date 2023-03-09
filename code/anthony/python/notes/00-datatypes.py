import random

# Datatypes

# Strings
"abc"
'123'
"""a1b2c3"""
'''🦊'''

# Strings are immutable,
# in order to update the value of a variable,
# we must create a new string
pie = "apple"
pie = "peach"

# Integers
1
-4
1000
1_000_000

# Integers are also immutable

age = 30
age = 31

# Floats
1.5
2.4
-0.3
4.0

# floats also immutable

# Booleans
True
False
# immutable

# Lists - mutable
example_list = ["apple", 1, 2.4, True, []]
example_list.pop()  # removes last item

# Tuples - immutable
example_tuple = ("hello", "world", 5, False)
example_tuple = ("hello", 5)

# convert from list to tuple
phone_brands = ["apple", "samsung", "lg", "nokia"]
phone_brands = tuple(phone_brands)

# convert back to list
phone_brands = list(phone_brands)

# Dictionaries
recipe = {
    "elbow noodles": "1 box",
    "Cheddar Cheese": "1 cup"
}

# print(recipe["Cheddar Cheese"])

# Classes
print(type(recipe))


class Person:
    name = "Bob"
    age = 30

    def say_hi():
        print("Hello")


sample_list = []

person = Person()

person.age
