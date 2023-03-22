"""Lab 3: Pick6
Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

a ticket costs $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000
One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

Steps
Generate a list of 6 random numbers representing the winning tickets
Start your balance at 0
Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance
Version 2
The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
"""

# Generate a list of 6 random numbers representing the winning tickets
import random

winning_ticket = random.sample(range(0,100), 6)
#print(winning_ticket)

# Start your balance at 0
balance = 0
matches = 0

# Loop 100,000 times, for each loop:

for ticket in range(0, 100000):


# Generate a list of 6 random numbers representing the ticket
    random_ticket = random.sample(range(0,100), 6)

# Subtract 2 from your balance (you bought a ticket)
    balance = balance -2
    
# Find how many numbers match

    number_of_matches = 0
    for x in range(6):
        if random_ticket[x] == winning_ticket[x]:
            #print("We found a match!")
            number_of_matches = number_of_matches + 1 
            matches = matches + 1
        #print(number_of_matches)
    """
    the loop is how you simpliefied these if statements


    if random_ticket[0] == winning_ticket[0]:
        balance = balance + 4
    if random_ticket[1] == winning_ticket[1]:
        balance = balance + 7
    if random_ticket[2] == winning_ticket[2]:
        balance = balance + 100
    if random_ticket[3] == winning_ticket[3]:
        balance = balance + 50000
    if random_ticket[4] == winning_ticket[4]:
        balance = balance + 1000000
    if random_ticket[5] == winning_ticket[5]:
    balance = balance + 25000000
    """
    

# Add to your balance the winnings from your matches

    if number_of_matches == 1:
        balance = balance + 4
    elif number_of_matches == 2:
        balance = balance + 7
    elif number_of_matches == 3:
        balance = balance + 100
    elif number_of_matches == 4:
        balance = balance + 50000
    elif number_of_matches == 5:
        balance = balance + 1000000
    elif number_of_matches == 6:
        balance = balance + 25000000


# After the loop, print the final balance
print(f"You had {matches} number of matches")
print(f"Your balance is: ${balance}")

#ROI
earnings = 200000 + balance
roi = balance/200000
print(f"your return on investments is {roi * 100}%")
print("Your expenses are $-200,000")
print(f"You Earned ${earnings}")