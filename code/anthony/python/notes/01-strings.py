"""
Notes on strings and string methods
Mar 8, 2023
"""

import random
import string

# A collection of characters between a set of quotes

example_string = "hello world"
example_string = example_string.lower()

# print(example_string)

# String methods

# capitalize - Uppercase the first character
example_string.capitalize()

# title - uppercase first letter of each word
example_string.title()

# upper - uppercase all letters
example_string.upper()

# lower - lowercase all letters
example_string.lower()

# fstring or formatted string
name = "Kara"
greeting = f"{example_string} {name.lower()}"
# print(greeting)

# formatting
total = 1.000000001
# : starts formatting, . decimal point, 2 how many after decimal, f is float
# print(f"${total:.2f}")

# split method
animals = "cat-dog-fish-bird-llama-fox"
list_of_animals = animals.split("-")

# join method
string_of_animals = " ".join(list_of_animals)
# print(string_of_animals)

# replace method
# print(animals.replace("-", " "))

# in keyword

"hello" in "hello world"

# choice = input("Would you like to continue? ")
# if "y" in choice:
#     print("Yay!")


for char in animals:
    print(char)


"""
Lab 01
Author: so and so
Date: Mar 8
"""
