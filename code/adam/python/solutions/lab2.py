"""
Adam
Lab2: Blackjack advice
Mar 13, 2023
"""

# Dictionary of blackjack card values
blackjack = {"A": 1,
"J": 10,
"Q": 10,
"K": 10,
"2": 2,
"3": 3,
"4": 4,
"5": 5,
"6": 6,
"7": 7,
"8": 8,
"9": 9,
"10": 10
}

# User input of blackjack
first_card = (input("What's your first card: "))
second_card = (input("What's your second card: "))
third_card = (input("What's your third card: "))

# Total amount of cards adding up all 3 card values
total = blackjack[first_card] + blackjack[second_card] + blackjack[third_card]
# if statement giving the user advice(Hit, Stay, Blackjack)
if total == 21:
    print("21 Blackjack!")
elif total < 15:
    print(f"{total} Hit")
elif total > 17 and total < 21:
    print(f"{total} Stay")
else:
    print("Over 21, already busted!")
