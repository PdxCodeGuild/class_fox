"""
    # Lab 1: Number to Phrase

    Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

    Hint: you can use modulus to extract the ones and tens digit.

    ```python
    x = 67
    tens_digit = x//10
    ones_digit = x%10
    ```
    Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.

    ## Version 2

    Handle numbers from 100-999.

    ## Version 3 (optional)

    Convert a number to roman numerals.

    ## Version 4 (optional)

    Convert a time given in hours and minutes to a phrase.
"""
import string

# okay here we go, number to phraser!

# Version 1
print("Version 1")
# the next three dictionaries are my way of determining what numbers to return
teens_digit = {10 : 'ten',
            11 : 'eleven',
            12 : 'twelve',
            13 : 'thirteen',
            14 : 'fourteen',
            15 : 'fifteen',
            16 : 'sixteen',
            17 : 'seventeen',
            18 : 'eighteen',
            19 : 'ninteen',
            }

single_digits = {1 : 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            0: 'zero'}

ones_digits = {1 : '-one',
            2: '-two',
            3: '-three',
            4: '-four',
            5: '-five',
            6: '-six',
            7: '-seven',
            8: '-eight',
            9: '-nine',
            0: ''}

tens_digits = {2 : 'twenty',
            3 : 'thirty',
            4 : 'forty',
            5 : 'fifty',
            6 : 'sixty',
            7 : 'seventy',
            8 : 'eighty',
            9 : 'ninty',
            0 : ''}

hundo_digits = {1 : 'one-hundred ',
                2 : 'two-hundred ',
                3 : 'three-hundred ',
                4 : 'four-hundred ',
                5 : 'five-hundred ',
                6 : 'six-hundred ',
                7 : 'seven-hundred ',
                8 : 'eight-hundred ',
                9 : 'nine-hundred ',
                0 : '',
                '' : ''}



numbers_needing_conversion = 'yes' # this will setup a loop for my code

while 'y' in numbers_needing_conversion:
    usernumber = input("Gimmie an integer between 0 and 100:\n")
    usernumber = int(usernumber)
# this is the code that will allow the person running it to enter a number


# this block will help determine which dictionary to look from
    if usernumber < 10:
        print(single_digits[usernumber])
    elif usernumber >= 10 and usernumber < 20:
        print(teens_digit[usernumber])
    elif usernumber > 99:
        print("I can only do BETWEEN 0 and 100, not more, not less")
    else: print(tens_digits[usernumber//10] + ones_digits[usernumber%10])
    numbers_needing_conversion = input("Do you have more numbers to convert, yes or no: \n")



print("\nSayanarya bucko!\n \n \n")

# Version 2
print("Version 2\n")
hundos_needing_conversion = 'yes'

while 'y' in hundos_needing_conversion: #this should loop it
    usernumber = input("Gimmie an integer between 100 and 999:\n")
    usernumber = int(usernumber)
    h = usernumber//100
    t = (usernumber-(100*int(h)))//10
    o = usernumber%10


    if usernumber < 10:
        print(single_digits[o])
    elif usernumber >= 10 and usernumber < 20:
        print(teens_digit[o])
    elif usernumber < 19:
        print(tens_digits[t] + ones_digits[o])
    elif usernumber > 99 and usernumber <= 999:
        if t == 1:
            print(hundo_digits[h] + teens_digit[int(usernumber)-int(100*int(h))])
        else:
            print(hundo_digits[h] + tens_digits[t] + ones_digits[o])
    else:
        print("reread the prompt plz")
    hundos_needing_conversion = input("Do you have more numbers to convert, yes or no: \n")


print("\nSee ya dude bro!")