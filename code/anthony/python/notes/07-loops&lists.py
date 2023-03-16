
"""
numbers = []

for x in range(9):
    numbers.append(x + 1)

for x in range(1, 10):
    numbers.append(x)

print(numbers)
"""

"""
numbers = []

for x in range(50):
    if x % 2 == 0:
        numbers.append(x)


for x in range(len(numbers)):
    if numbers[x] > 9:
        tens_digit = numbers[x] // 10
        ones_digit = numbers[x] % 10
        numbers[x] = tens_digit + ones_digit

print(numbers)
"""

pets = ["cat", "fish", "dog", "bird"]
four_legged_animals = ["cat", "llama", "dog", "horse"]


number_of_matches = 0

for x in range(4):
    if pets[x] == four_legged_animals[x]:
        print("We found a match!")
        number_of_matches = number_of_matches + 1


print(f"{number_of_matches} total matches")


if number_of_matches == 1:
    pass
    # add 4 to balance
elif number_of_matches == 2:
    pass
    # add 7 to balance
