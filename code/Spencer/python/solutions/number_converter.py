"""
Lab 1: Number to Phrase
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

"""

user_input = input("Pick a number between 0-99: ")

numbers = { 
    "1" : "one", "2" : "two", "3" : "three", "4" : "four", "5" : "five", "6" : "six", "7" : "seven", "8" : "eight", "9" : "nine", "10" : "ten",
    "11" : "eleven", "12" : "twelve", "13" : "thirteen", "14" : "fourteen", "15" : "fifteen", "16" : "sixteen", "17" : "seventeen", "18" : "eighteen", "19" : "ninteen",
    "20" : "twenty", "30" : "thirty", "40" : "fourty", "50" : "fifty", "60" : "sixty", "70" : "seventy", "80" :"eighty", "90" : "ninety",
    "100" : "one hundred", "200" : "two hundred", "300" : "three hundred", "400" : "four hundered", "500" : "five hundered", "600" : "six hundered", "700" : "seven hundered", "800" : "eight hundered", "900" : "nine hundered"

    
    }



user_input = int(user_input)

if user_input < 20:
    user_input = str(user_input)
    print(numbers[user_input])

elif user_input > 20 and user_input < 100:
    tens = user_input//10
    ones = user_input%10
    
    tens = tens*10

    ones = str(ones)
    tens = str(tens)
    print(numbers[tens],"-",numbers[ones])

elif user_input > 99:
    hundreds = user_input//100
    tens = user_input//10
    ones = user_input%10
    tens = tens%10
    hundreds = hundreds*100
    tens = tens*10
    ones = str(ones)
    tens = str(tens)
    hundreds = str(hundreds)
    
    print(numbers[hundreds], numbers[tens], numbers[ones])
