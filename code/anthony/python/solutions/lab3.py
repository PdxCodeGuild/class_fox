"""
Anthony
Lab3 Pick 6
Mar 16 2023
"""


"""
- a ticket costs $2
- if 1 number matches, you win $4
- if 2 numbers match, you win $7
- if 3 numbers match, you win $100
- if 4 numbers match, you win $50,000
- if 5 numbers match, you win $1,000,000
- if 6 numbers match, you win $25,000,000
"""




import random
def pick6():
    ticket = []

    for x in range(6):
        ticket.append(random.randint(1, 99))

    return ticket


def calculate_winnings(matches):
    if matches == 1:
        return 4
    elif matches == 2:
        return 7
    elif matches == 3:
        return 100
    elif matches == 4:
        return 50_000
    elif matches == 5:
        return 1_000_000
    elif matches == 6:
        return 25_000_000

    return 0


def get_number_of_matches(ticket, winning_ticket):
    matches = 0
    for x in range(6):
        if ticket[x] == winning_ticket[x]:
            matches = matches + 1

    return matches


# 1. Generate a list of 6 random numbers representing the winning tickets
winning_ticket = pick6()

# 2. Start your balance at 0
balance = 0

# 2. Loop 100,000 times, for each loop:
for ticket in range(0, 100_000):

    # 3. Generate a list of 6 random numbers representing the ticket
    ticket = pick6()

    # 4. Subtract 2 from your balance (you bought a ticket)
    balance = balance - 2

    # 5. Find how many numbers match
    matches = get_number_of_matches(ticket, winning_ticket)

    # 6. Add to your balance the winnings from your matches
    balance = balance + calculate_winnings(matches)

# 7. After the loop, print the final balance
print(f"You have earned ${balance}")

# 8 Calculate your ROI (Return on investment)
roi = balance / 200_000
print(f"Your ROI is: {roi * 100}%")
