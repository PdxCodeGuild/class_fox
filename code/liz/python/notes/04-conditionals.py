'''
Notes: Booleans, Comparison Operators, and Conditionals
Date: Mar 9, 2023
'''

1 < 4 # = Boolean True
4 < 4 # = False

4 == 4 # True
# 4 = 4 is a variable assignment

5 != 4 # True, 5 is not 4

4 != 4 # False

x = 4
y = 4
x is y # True

x = ['something', 'something else']
y = x[:] # copy
x is y # False
x is not y # True
4 is 4 # True, ==

# 'is' checks if 2 objects are the same
# a copy of an object is not the same as it's original, whether or not they have the same value

'something' in x # True
'boo' not in x # True
# check to see if a string is in another string

# and can combine conditionals rather than nest
5 > 2 and 'hello' in 'hello world' # True and True = True
# both sides must be True in and
5 > 7 and 'hello' in 'hello world' # False

5 > 7 or 'hello' in 'hello world' # True
# OR is True as long as one side is True
5 > 7 or 'panda' in 'hello' # False

# not will flip the boolean from True to False or vice versa
not  5 > 7 or 'panda' in 'hello' # True
5 > 7 or not 'panda' in 'hello' # True
# perentheses work as well

# conditional statements are if/then/elif/else

