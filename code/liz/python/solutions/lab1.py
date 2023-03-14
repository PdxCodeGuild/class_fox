'''
Liz Luu
Lab 1: Number to Phrase
Date: Mar 10, 2023
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10

Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.

Version 2
Handle numbers from 100-999.

Version 3 (optional)
Convert a number to roman numerals.

Version 4 (optional)
Convert a time given in hours and minutes to a phrase.
'''
# Version 1:
def num_to_phrase(num:int):
    '''Turn an integer between 1-99 into an english phrase'''
    # Variables for num digits
    tens_digit = num//10 
    ones_digit = num%10

    # Dictionaries for phrases with digits as keys
    tens_phrases = {
        0:'',
        1:'teen',
        2:'twenty',
        3:'thirty',
        4:'forty',
        5:'fifty',
        6:'sixty',
        7:'seventy',
        8:'eighty',
        9:'ninety'
    }
    ones_phrases = {
        0:'',
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
    }

# this time I made each exception it's own conditional

    if num >= 20: # most numbers will occur here, the rest are exceptions
        print(f'{num} is {tens_phrases[tens_digit]} {ones_phrases[ones_digit]}')
    elif 14 <= num <= 19: # the teens
        print(f'{num} is {ones_phrases[ones_digit]}{tens_phrases[tens_digit]}')
    elif num == 13:
        print(f'{num} is thirteen')
    elif num == 12:
        print(f'{num} is twelve')
    elif num == 11:
        print(f'{num} is eleven')
    elif num == 10:
        print(f'{num} is ten')
    elif num < 10: # the singles
        print(f'{num} is {ones_phrases[ones_digit]}')
    else:
        print(f'{num} is unknown')
    

user_input = input('Enter a number between 1-99: ') # if not an int, will result in error
user_input_num = int(user_input)
if 1 < user_input_num < 100: 
    user_input_num = int(user_input)
    num_to_phrase(user_input_num)
else:
    print('Invalid Number')

# Version 2

def num_to_phrase_v2(num2:int):
    '''Turn an integer between 100-999 into an english phrase'''
    hundreds_digit = num2//100 # New hundreds digit
    tens_digit = (num2%100)//10 # new math to remove the hundreds digit before reusing old math
    ones_digit = num2%10
    hundreds_phrases = {
        0:'',
        1:'one-hundred',
        2:'two-hundred',
        3:'three-hundred',
        4:'four-hundred',
        5:'five-hundred',
        6:'six-hundred',
        7:'seven-hundred',
        8:'eight-hundred',
        9:'nine-hundred',
    }
    tens_phrases = {
        0:'',
        1:'teen',
        2:'twenty',
        3:'thirty',
        4:'forty',
        5:'fifty',
        6:'sixty',
        7:'seventy',
        8:'eighty',
        9:'ninety'
    }
    ones_phrases = {
        0:'',
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
    }
    special_cases = {
        13:'thirteen',
        12:'twelve',
        11:'eleven',
        10:'ten'
    }
    if tens_digit != 1: # if there are no teens or exceptions
        print(f'{num2} is {hundreds_phrases[hundreds_digit]} {tens_phrases[tens_digit]}-{ones_phrases[ones_digit]}')
    elif tens_digit == 1 and ones_digit >= 4: # the teens
        print(f'{num2} is {hundreds_phrases[hundreds_digit]} {ones_phrases[ones_digit]}{tens_phrases[tens_digit]}')
    elif tens_digit == 1 and ones_digit == 3: # 13
        print(f'{num2} is {hundreds_phrases[hundreds_digit]} {special_cases[13]}')
    elif tens_digit == 1 and ones_digit == 2: # 12
        print(f'{num2} is {hundreds_phrases[hundreds_digit]} {special_cases[12]}')
    elif tens_digit == 1 and ones_digit == 1: # 11
        print(f'{num2} is {hundreds_phrases[hundreds_digit]} {special_cases[11]}')
    elif tens_digit == 1 and ones_digit == 0: # 10
        print(f'{num2} is {hundreds_phrases[hundreds_digit]} {special_cases[10]}')
    elif tens_digit == 0: # no tens digit
        print(f'{num2} is {hundreds_phrases[hundreds_digit]} {ones_phrases[ones_digit]}')
    else:
        print(f'{num2} is unknown')

user_inputv2 = input('Enter a number between 100-999: ')
user_input_numv2 = int(user_inputv2)
if 100 <= user_input_numv2 < 1000:
    user_input_numv2 = int(user_inputv2)
    num_to_phrase_v2(user_input_numv2)
else:
    print('Invalid Number')
