"""
Each player receives at least 3 chips. Players take it in turn to roll three
six-sided dice, each of which is marked with "L", "C", "R" on one side, and
a single dot on the three remaining sides. For each "L" or "R" thrown, the
player must pass one chip to the player to his left or right, respectively.
A "C" indicates a chip to the center (pot). A dot has no effect.

If a player has fewer than three chips left, he/she is still in the game but
his number of chips is the number of dice he/she rolls on his/her turn, rather
than rolling all three. When a player has zero chips, he/she passes the dice on
his turn, but may receive chips from others and take his next turn accordingly.
The winner is the last player with chips left. He/she does not roll the dice, and
wins the center pot. If he/she chooses to play another round, he/she does not roll
3, he/she keeps his pot and plays with that.

When the program starts, it should ask for the names of the players, until the user
enters 'done'. Then it should run the simulation, tell the user who won, and ask the
player whether they'd like to play again.
"""
import random
from typing import Literal
import os


class Dice:
    def __init__(self):
        self.sides = ["L", "C", "R", "·", "·", "·"]

    def roll(self) -> Literal["L", "C", "R", "·"]:
        return random.choice(self.sides)

    def __str__(self):
        return ", ".join(self.sides)


class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips

    def dice_to_roll(self):
        """At most, roll three dice. If fewer than three chips remaining, roll that many dice"""
        if self.chips >= 3:
            return 3
        else:
            return self.chips

    def pass_chips(self, other_player):
        self.chips -= 1
        other_player.chips += 1

    def __str__(self):
        return f"{self.name} has {self.chips} chip(s)."


# Get player names from user
players: list[Player] = []
while True:
    player_name = input("Enter player name or 'done': ")

    if player_name == "done":
        break
    else:
        players.append(Player(player_name, 3))

pot = Player("pot", 0)
dice = Dice()

winner = False

while winner == False:
    print("\n----------------------\n")
    os.system('clear')
    for index, player in enumerate(players):
        if player.chips + pot.chips == len(players) * 3:
            print(f"Winner is {player.name} with {player.chips} chips!")
            winner = True
            break

        print(f"It is {player.name}'s turn. With {player.chips} chips.")
        left = players[index - 1]
        right = players[(index + 1) % len(players)]

        for x in range(player.dice_to_roll()):
            roll = dice.roll()
            print(f"{player.name} rolled '{roll}'")
            if roll == "C":
                player.pass_chips(pot)
                print(f"\tPassing chip to {pot.name}")
            elif roll == "L":
                player.pass_chips(left)
                print(f"\tPassing chip to {left.name}")
            elif roll == "R":
                player.pass_chips(right)
                print(f"\tPassing chip to {right.name}")
