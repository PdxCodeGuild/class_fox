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

# Get user input for each card (3)
# "A,K,6" => ["A", "K", "6"]
hand = input("Enter three cards separated by commas: ")

hand = hand.split(",")

total = 0
for card in hand:
    if card in "JQK":
        total = total + 10
    elif card == "A":
        total = total + 1
    else:
        total = total + int(card)

# Advice the user
# if less than 17 have them hit
if total < 17:
    print("Hit!")
# if between 17 and 21 have them stay
elif total >= 17 and total < 21:
    print("Stay")
# 21 is blackjack
elif total == 21:
    print("Blackjack!")
# over 21 is busted
else:
    print("Busted 😥")

print(f"Total: {total}")


"""
valid_cards = "A2345678910JQK"
if first_card not in valid_cards or second_card not in valid_cards or third_card not in valid_cards:
    print("invalid input")
    exit()

# Have a result for the card totals
if first_card == "Q" or first_card == "J" or first_card == "K":
    first_card = 10
elif first_card == "A":
    first_card = 1
if second_card == "Q" or second_card == "J" or second_card == "K":
    second_card = 10
elif second_card == "A":
    second_card = 1
if third_card == "Q" or third_card == "J" or third_card == "K":
    third_card = 10
elif third_card == "A":
    third_card = 1

result = int(first_card) + int(second_card) + int(third_card)

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
"""
