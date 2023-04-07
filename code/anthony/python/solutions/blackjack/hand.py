"""
In the hand module, implement methods that:

Hand class with a collection of cards from a deck.

Add a card to a hand
Score a hand
"""

from deck import Deck, Card


class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        cards_to_print = []
        for card in self.cards:
            cards_to_print.append(str(card))
        return f"{cards_to_print}"

    def add_card(self, card):
        self.cards.append(card)

    def score(self):
        total = 0
        for card in self.cards:
            if card == "J" or card == "Q" or card == "K":
                total += 10
            elif card == "A":
                if total < 11:
                    total += 11
                else:
                    total += 1
            else:
                total += int(card.value)

        return total
