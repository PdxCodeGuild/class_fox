'''
Number To Phrase
13 Mar 23
'''
#convert user numerical input into words

number = {
    0: " ",
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
    20: "tweenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

phrase = int(input("Enter a number from 1 to 999: "))


if phrase < 0:
    print("Input not included.")
elif phrase == 0:
    print("zero")

elif phrase <= 20:
    print(number[phrase])

elif phrase <= 99:
    tens = phrase // 10
    tens = tens * 10
    ones = phrase % 10
    print(number[tens] + " " + number[ones])

elif phrase <= 999:
    hundreds = phrase // 100
    tens = phrase // 10 
    tens = tens % 10  
    tens = tens * 10  
    ones = phrase % 10

    print(number[hundreds] + " hundred and " +
        number[tens] + " " + number[ones])
   