"""
Notes: Booleans, Comparison, and Conditionals
Date: Mar 9, 2023
"""

1 < 4  # True
4 < 4  # False
5 > 1  # True
2 > 6  # False
4 <= 4  # True

4 == 4  # True
5 != 4  # True
4 != 4  # False

x = ["something", "something else"]
y = x[:]

# is checks if two objects are the same, not their values
x is y  # False
x is not y  # True
"something" in x  # True
"blueberry" not in x  # True


5 > 2 and "hello" in "hello world"  # True
5 > 7 and "hello" in "hello world"  # False
5 > 7 or "hello" in "hello world"  # True
5 > 7 or "panda" in "hello world"  # False
not (5 > 7) or "panda" in "hello world"  # True


user_input = "yes"
monkey = True

if "hello":
    print("hello")
elif monkey and "y" in user_input:
    print("That is the correct word")
elif "n" in user_input and not monkey:
    print("go away")
else:
    print("incorrect")


3 < 5 < 10  # True
3 < 5 and 5 < 10  # True

5 == 5 == 5  # True
(5 == 5) == 5  # False
True == 5

4 == "4"  # False
4 == 4.0  # True
