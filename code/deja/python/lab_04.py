'''
Lab 04: Credit Caard Validation
16 Mar 23
'''

def credit_card_validator():

    #Convert the input string into a list of ints

    credit_card = input("Enter your credit card number: ")

    credit_card = list(credit_card)

    for x in range(len(credit_card)):
        credit_card[x] = int(credit_card[x])

            

    #Slice off the last digit. That is the check digit.

    check_digit = credit_card.pop(-1)
    print(check_digit)

    #Reverse the digits.

    credit_card.reverse()
    print(credit_card)

    #Double every other element in the reversed list (starting with the first number in the list).
    
    for x in range(len(credit_card)):
        if x % 2 == 0:
            credit_card[x] * 2 
            credit_card[x] = credit_card[x] * 2
            print(credit_card[x])


    #Subtract nine from numbers over nine.

        if credit_card[x] > 9:
            credit_card[x] = credit_card[x] - 9



    #Sum all values.
    total = sum(credit_card)

    #Take the second digit of that sum.
    second_digit = total // 1
    second_digit = second_digit % 10

    #If that matches the check digit, the whole card number is valid.

    if check_digit == second_digit:
        print("true.")
    else:
        print("false.")
