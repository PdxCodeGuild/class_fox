"""Lab 2: Blackjack Advice
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



first_card = input(" What is your first card? ")
second_card = input(" What is your second card? ")
third_card = input("What is your third card?: ")


if first_card == "Q" or first_card == "K" or first_card == "J":
    first_card = 10
elif first_card == "A":
    first_card = 1
if second_card == "J" or second_card == "Q" or second_card == "K":
    second_card = 10
elif second_card == "A":
    second_card = 1
if third_card == "J" or third_card == "Q" or third_card == "K":
    third_card = 10
elif third_card == "A":
    third_card = 1

total = int(first_card) + int(second_card) + int(third_card)

if total < 17:
    print("hit")
elif total > 17 and total < 21:
    print("stay")
elif total == 21:
    print("Black jack!")
else:
    print("Already Busted")


print(total)