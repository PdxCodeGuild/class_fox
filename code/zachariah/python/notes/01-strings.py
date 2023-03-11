'''
Notes on strings and string methods
Mar 8, 2023
'''

import random
import string
# A collection of characters between a set of quotes

# "hello' is NOT a string
"hello" # is a string
example_string = "hello"

print(example_string)
# str.capitalize will capitalize the first character
example_string = example_string.capitalize()
print(example_string)
# str.title will upper ALL letters
example_string = example_string.title()
print(example_string)
# str.lower() will lowercase all letters
example_string = example_string.lower()

print(example_string)

NAME = "Zachariah"
# formatted strings 
greeting = f"{example_string} {NAME}"

print(greeting)

# formatting
total = 1
print(f"$                  {total:.2f}         0")

# split method
animals = "cat-dog-fish-bird-llama-fox"

list_of_animals = animals.split('-') # default will split on spaces, but you can insert a character you want to split on
print(list_of_animals)

# join method
string_of_animals = "".join(list_of_animals) #needs to be attached to a string, even a blank one
print(string_of_animals)

# replace method
print(animals.replace("-", " "))

# in keyword
print("hello" in "hello world")

choice = input("would you like to continue? ")
if "y" in choice:
    print("Yay")

for char in animals:
    print(char)

"""
Lab 01
Author: so and so
Date: Mar 8
""" # this is a doc string, typtically used for documentation. you could make it a header et c etc
