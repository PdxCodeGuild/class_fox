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

number_to_phrase = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

# Get number from user
raw_number = int(input("Enter a number from 0-9999: "))  # 23


if raw_number < 0:
    print("Invalid input.")
elif raw_number == 0:
    print("zero")
elif raw_number <= 20:
    print(number_to_phrase[raw_number])
elif raw_number <= 99:
    tens_digit = raw_number // 10
    tens_digit = tens_digit * 10
    ones_digit = raw_number % 10

    print(number_to_phrase[tens_digit] + " " + number_to_phrase[ones_digit])
    # print(f"{number_to_phrase[tens_digit]} {number_to_phrase[ones_digit]}")
elif raw_number <= 999:

    hundreds_digit = raw_number // 100

    # 123
    tens_digit = raw_number // 10  # 12
    tens_digit = tens_digit % 10  # 2
    tens_digit = tens_digit * 10  # 20

    ones_digit = raw_number % 10

    print(number_to_phrase[hundreds_digit] + " hundred and " +
          number_to_phrase[tens_digit] + " " + number_to_phrase[ones_digit])

elif raw_number <= 9999:
    # 1234
    thousands_digit = raw_number // 1000  # 1
    hundreds_digit = raw_number // 100  # 12
    hundreds_digit = hundreds_digit % 10  # 2
    tens_digit = raw_number // 10  # 123
    tens_digit = tens_digit % 10  # 3
    tens_digit = tens_digit * 10  # 30
    ones_digit = raw_number % 10  # 4

    print(number_to_phrase[thousands_digit] + " thousand " + number_to_phrase[hundreds_digit] + " hundred and " +
          number_to_phrase[tens_digit] + " " + number_to_phrase[ones_digit])

else:
    print("Not yet implemented")
