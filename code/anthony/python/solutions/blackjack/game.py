"""
In the game module, implement top-level functions that:

Start a new game of Blackjack, or Quit
Bust if the score is over 21
Loop through game
"""

from deck import Deck, Card
from hand import Hand

deck = Deck()
deck.shuffle().cut().pull()

player = Hand()
dealer = Hand()

for x in range(2):
    player.add_card(deck.pull())
    dealer.add_card(deck.pull())

print(f"Dealers hand: {dealer}")
print(f"Dealers score: {dealer.score()}")

while True:
    print(f"Your hand: {player}")
    print(f"Current score: {player.score()}")
    if player.score() >= 21:
        break
    hit = input("Would you like another card? y/n: ")
    if hit == "y":
        player.add_card(deck.pull())
    else:
        break

while True:
    if dealer.score() < 16:
        card = deck.pull()
        dealer.add_card(card)
        print(f"Dealer drew: {card}")
        print(f"Dealer score: {dealer.score()}")
    else:
        break

if dealer.score() == 21:
    print("Dealer wins")
elif player.score() > 21:
    print("Dealer wins")
elif dealer.score() > player.score():
    print("Dealer wins")
elif dealer.score() == player.score():
    print("Dealer wins")
elif dealer.score() < player.score():
    print("You win")
