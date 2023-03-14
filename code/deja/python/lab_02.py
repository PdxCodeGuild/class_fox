'''
BlackJack Lab 
13 Mar 23
'''

Blackjack = {
    "A" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10
    }

card_1 = input(f"What's your first card? ")
card_2 = input(f"What's your second card? ")
card_3 = input(f"What's your third card? ")
result = (int(Blackjack[card_1] + Blackjack[card_2] + Blackjack[card_3]))

if result < 17:
    print(f"Hit!")
elif result >= 17 and result <= 21:
    print(f"Stay!")
elif result == 21:
    print(f"Blackjack!")
elif result > 21:
    print(f"Already Busted!")

    print(result)
