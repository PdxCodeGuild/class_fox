"""Lab 4: Credit Card Validation
Let's write a function credit_card_validator which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list (starting with the first number in the list).
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
Here is a valid credit card number to test with: 4556737586899855

For example, the worked out steps would be:

4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
True Valid!"""
credit_card_number = [4,5,5,6,7,3,7,5,8,6,8,9,9,8,5,5]

#def credit_card_validator():

# Convert the input string into a list of ints
    
# Slice off the last digit. That is the check digit.
check_digit = credit_card_number.pop()
# Reverse the digits.
credit_card_number.reverse()

# Double every other element in the reversed list (starting with the first number in the list).
for num in range(len(credit_card_number)):
    if num % 2 == 0:
        credit_card_number[num] = credit_card_number[num] * 2

# Subtract nine from numbers over nine.
    if credit_card_number[num] > 9:
        credit_card_number[num] = credit_card_number[num] - 9
#print(credit_card_number)

# Sum all values.

credit_card_number = sum(credit_card_number)

    
# Take the second digit of that sum.

credit_card_number = credit_card_number % 10

# If that matches the check digit, the whole card number is valid
if credit_card_number == check_digit:
    print("The credit card number is valid")