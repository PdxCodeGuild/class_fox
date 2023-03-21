"""
Date: Mar 16th, 2023
Lab 4: Credit Card Validation
"""

def credit_card_validator():
    """
    Get's card number from user and returns a boolean.
    """
    
 
    card_number = '4556737586899855'

    # 1.Convert the input string into a list of ints
    card_list = list(card_number)
    return card_list
number_list = credit_card_validator()
print(number_list)

credit_card_number = [int(n) for n in number_list]
print(credit_card_number)
    
    # 2.Slice off the last digit. That is the check digit.

check_digit = credit_card_number.pop()
print(credit_card_number)


    # 3.Reverse the digits.
credit_card_number.reverse()
print(credit_card_number)
    
    # 4.Double every other element in the reversed list (starting with the first number in the list)
for n in range(0, len(credit_card_number), 2):
    credit_card_number[n] *= 2
print(credit_card_number)


    # 5.Subtract nine from numbers over nine.
for n in range(len(credit_card_number)):
    if credit_card_number[n] > 9:
        credit_card_number[n] -= 9
print(credit_card_number)

    #  6.Sum all values.
num_list = credit_card_number
total = sum(num_list)
print(total)

    # 7.Take the second digit of that sum.
second_digit = total // 1
second_digit = second_digit % 10
print(second_digit)

    # 8.If that matches the check digit, the whole card number is valid.
if second_digit == check_digit:
    print("valid")
else:
    print("invalid")
