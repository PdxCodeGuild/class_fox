
"""
Notes: functions
Date: Mar 9, 2023
"""

# Positional arguement
def is_even(num):
    if num % 2 == 0:
        print("is even")
    else:
        print("is odd")
    


# is_even(5) # calling function


# Keyword arguement
def is_even(num, message = "Python is fun!"):
    if num % 2 == 0:
        print("is even")
    else:
        print("is odd")

    print(message)

# is_even(5, "wow")



def sum(a, b):
    result = a + b

    return result

total = sum(5, 7)
if total > 3:
    print("wow")




