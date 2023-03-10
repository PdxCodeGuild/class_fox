"""
Notes: functions
Date: Mar 9, 2023
"""


def is_even(num):
    if num % 2 == 0:
        print("is even")
    else:
        print("is odd")


is_even(112)


def is_even(num, message):
    if num % 2 == 0:
        print("is even")
    else:
        print("is odd")

    print(message)


is_even(112, "Hello World")


def is_even(num, message="Python is fun!", color="blue"):
    if num % 2 == 0:
        print("is even")
    else:
        print("is odd")

    print(message)


is_even(112, "red", "wow")


def sum(a, b):
    return a + b


total = sum(5, 7)
if total > 3:
    print("wow")
