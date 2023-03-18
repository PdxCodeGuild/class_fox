# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance
# Version 2
# The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
# """

import random

def pick6():
    ticket = []

    for x in range(6):
        ticket.append(random.randint(1, 99))
    return ticket

winning_ticket = pick6()

print(winning_ticket)

balance = 0 

for ticket in range(0, 100_000):
    ticket = pick6()
    balance = balance - 2 

    number_of_matches = 0
    for x in range(6):
        if ticket[x] == winning_ticket[x]:
            #print("We found a match!")
            number_of_matches = number_of_matches + 1 

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

print(f"You have earned ${balance}")

