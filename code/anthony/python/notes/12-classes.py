
class Fruit:

    def __init__(self):
        self.color = "red"
        self.shape = "round"
        self.name = "apple"
        self.scent = "sweet"

    def grow(self, amount):
        print(f"{self.name} drank {amount} of water, got some sunshine")

    def __str__(self):
        return self.name

    def __eq__(self, fruit):
        if self.name == fruit.name:
            return True
        else:
            return False


new_fruit = Fruit()
other_fruit = Fruit()
banana = Fruit()

other_fruit.name = "kiwi"
other_fruit.color = "green"

banana.name = "banana"
banana.color = "yellow"
banana.shape = "oblong"

# banana.grow("4 cups")
# other_fruit.grow("1 tbsp")
# new_fruit.grow("1 gallon")


pineapple = Fruit()
pineapple.color = "green"
pineapple.name = "pineapple"
pineapple.shape = "oval"

new_fruit.name = "banana"

if new_fruit == banana:
    print("They are the same!")
else:
    print("Nothing happened")
