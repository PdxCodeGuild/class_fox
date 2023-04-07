import random


class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __eq__(self, value):
        if self.value == value:
            return True
        else:
            return False


class Deck:
    def __init__(self):

        unshuffled_deck = []
        suits = ["diamonds", "hearts", "clubs", "spades"]
        values = ["A", "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "J", "Q", "K"]
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                unshuffled_deck.append(card)

        self.__cards = unshuffled_deck

    def shuffle(self):
        random.shuffle(self.__cards)
        return self

    def cut(self):
        middle = len(self.__cards) // 2
        # Grab cards starting from 0 up to middle
        first_half = self.__cards[0:middle]
        # Grab cards starting from middle to end
        second_half = self.__cards[middle:]
        self.__cards = second_half + first_half
        return self

    def pull(self):
        return self.__cards.pop()

    def __len__(self):
        return len(self.__cards)
