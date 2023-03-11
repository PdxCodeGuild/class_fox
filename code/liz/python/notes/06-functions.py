'''
Notes: functions
Date: Mar 9, 2023
'''

11 % 2 # 1
10 % 2 # 0
12 % 2 # 0
15 % 2 # 1

# modulus operation to check if even or odd
num = 4
if num % 2 == 0:
    print('even')
else:
    print('odd')

def is_even(num):
    if num % 2 == 0:
        print('even')
    else:
        print('odd')

num = int(input('Num?\n'))
is_even(num)
# is_even() would result in an error
# function must match parameter model in def