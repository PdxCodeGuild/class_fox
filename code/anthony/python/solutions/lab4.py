

def credit_card_validator() -> bool:
    """
    Gets card number from user and validates through the following:
    1. Convert the input string into a list of ints
    2. Slice off the last digit.  That is the **check digit**.
    3. Reverse the digits.
    4. Double every other element in the reversed list (starting with the first number in the list).
    5. Subtract nine from numbers over nine.
    6. Sum all values.
    7. Take the second digit of that sum.
    8. If that matches the check digit, the whole card number is valid.
    """
    starting_string = input("Enter card number: ")  # ex. 4556737586899855

    # Convert the input string into a list of ints
    credit_card_number = list(starting_string)
    # credit_card_number = [int(num) for num in starting_string]
    for x in range(len(credit_card_number)):
        credit_card_number[x] = int(credit_card_number[x])

    # Slice off the last digit. That is the check digit.
    check_digit = credit_card_number.pop()

    # Reverse the digits.
    # reversed_card_number = list(reversed(credit_card_number)) # create a new variable in reversed order
    # original_card_number = credit_card_number.copy()
    credit_card_number.reverse()

    # total = 0
    # Double every other element in the reversed list (starting with the first number in the list).
    for x in range(len(credit_card_number)):
        if x % 2 == 0:
            credit_card_number[x] = credit_card_number[x] * 2

        # Subtract nine from numbers over nine.
        if credit_card_number[x] > 9:
            credit_card_number[x] = credit_card_number[x] - 9

        # total = total + credit_card_number[x]

    # Sum all values.
    total = sum(credit_card_number)

    # Take the second digit of that sum.
    second_digit = total // 1
    second_digit = second_digit % 10

    # If that matches the check digit, the whole card number is valid.
    if second_digit == check_digit:
        return True
    else:
        return False


result = credit_card_validator()
print(result)
