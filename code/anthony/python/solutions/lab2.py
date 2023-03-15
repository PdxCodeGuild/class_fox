"""
Anthony
Lab2 Blackjack Advice
Mar 13 2023

Lab 2: Blackjack Advice
Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
Print out the current total point value and the advice.

What's your first card? Q
What's your second card? 2
What's your third card? 3
15 Hit

What's your first card? K
What's your second card? 5
What's your third card? 5
20 Stay

What's your first card? Q
What's your second card? J
What's your third card? A
21 Blackjack!
"""

# Create dictionary for card values
blackjack = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}

# Get user input for each card (3)
first_card = input("Enter your first card: ")  # "Q"
second_card = input("Enter your second card: ")  # 4
third_card = input("Enter your third card: ")  # 7

if first_card in blackjack and second_card in blackjack and third_card in blackjack:
    # Have a result for the card totals
    result = blackjack[first_card] + \
        blackjack[second_card] + blackjack[third_card]

    # Advice the user
    # if less than 17 have them hit
    if result < 17:
        print("Hit!")
    # if between 17 and 21 have them stay
    elif result >= 17 and result < 21:
        print("Stay")
    # 21 is blackjack
    elif result == 21:
        print("Blackjack!")
    # over 21 is busted
    else:
        print("Busted 😥")

    print(f"Total: {result}")
else:
    print("Invalid input")
