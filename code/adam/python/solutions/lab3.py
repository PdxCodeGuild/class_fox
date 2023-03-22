"""
Adam
Lab 3: Pick 6
Date: Mar 15, 2023
"""

# Generate a list of 6 random numbers representing the winning tickets
import random
winner = []
num = 6
for x in range(6):
    winner.append(random.randint(1,99))
    winning_ticket = winner
print(f"Winning tickets are {winning_ticket}")

# Start your balance at 0
balance = 0

    


# Loop 100,000 times, for each loop:
entry = 0
for x in range(100_000):
    
    if entry == 100_000:
        break



# Generate a list of 6 random numbers representing the ticket
    ticket = []
    num = 6
    for x in range(6):
     ticket.append(random.randint(1,99))
    print(f"your ticket is {ticket}")

# Subtract 2 from your balance (you bought a ticket)
    balance = balance - 2

 # Find how many numbers match
    matches = 0
    
    for x in range(6):
        if ticket[x] == winning_ticket[x]:
            print("We found a match!")
            matches = matches + 1

    print(f"{matches} total matches")



# Add to your balance the winnings from your matches
    if matches == 1:
     earnings = balance + 4
    elif matches == 2:
     earnings = balance + 7
    elif matches == 3:
     earnings = balance + 100
    elif matches == 4:
     earnings = balance + 50_000
    elif matches == 5:
     earnings = balance + 1_000_000
    elif matches == 6:
      earnings = balance + 25_000_000


# After the loop, print the final balance
print(f"Final balance {earnings}")

# Version 2
ROI = (earnings - balance)/balance
print(f"Your return on investment is {ROI}")
