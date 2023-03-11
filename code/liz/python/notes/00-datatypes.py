# Python uses objects as data
# Each object has a different datatype
# datatypes do different things
# Datatypes:
# Strings
'''Collection of characters between a pair of quotes \'\"
"abc"
"123"
":("
strings are imutable, variables are mutable
mutable = changable
'''
# Integers
'''
Whole numbers, positive and negative
1_000_000 = 1,000,000 but reads in python
imutable, values of numbers cannot change
'''
# Floats
'''
decimal numbers and fractions, positive or negative
imutable
usage of float or integer is dependent on application
Currency, percentage = floats
counting people = ints
'''
# Booleans
'''
True
False
imutable
'''
# Lists
'''
collection of data points in []
['apple',1,2.4,True,['valid']] - Valid list
mutable - can change values in the list
methods will add, remove, adjust contents of the list
list.pop[] - on the list, remove the last item
'''
# Tuples
'''
collection of data types in ()
example.tuple = ('hello','world',5,False,(4))
imutable, no methods for changing the value
new tuple will need to be assigned new value
ensures data does not change
convert from list to tuple:
phone_brands: list = ["apple","samsung","lg","nokia",]
phone_brands: tuple = tuple(phone_brands) # list becomes tuple
phone_brands: list = list(phone_brands) # tuple becomes list
'''
# Dictionaries
'''
recipe = {
    "elbow noodles": "1 box",
    "cheddar cheese": "1 cup",
}
print(recipe["cheddar cheese"]) # 1 cup
mutable: can add, remove, and change keys and values
'''
# Classes
'''
print(type(recipe)) # <class 'dict'>
every datatype is a class
classes are not mutable after they have been created
but you can change properties of a class
'''
class Person:
    name = 'Bob'
    age = '30'

    def say_hi():
        print('Hello...')

sample_list = []
person = Person()
print(person.age) # 30
# lowercase implies that dataype can me used as a function, not a class



