"""
Version 1
The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

Jackalopes are reproductive from ages 4-8 and die at age 10.
Gestation is instantaneous. Each gestation produces two offspring.
Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
With these conditions in mind, we can represent our population as a list of ints.

Version 2
Now let's give the jackalopes distinct sexes and extend their gestation period to one year.
We can represent each jackalope with a dictionary, thus our population will be a list of dictionaries.
A jackalope will have the following properties:

name
age
sex
whether they're pregnant
Jackalopes can only mate with those immediately around them.
Every generation Jackalopes are randomly shuffled.
"""

import random


def random_name():
    vowels = "aeiouy"
    not_vowels = "bcdfghjklmnqrstvwxz"
    name = random.choice(not_vowels) + random.choice(vowels) + \
        random.choice(not_vowels) + random.choice(vowels)
    return name


def random_sex():
    sex = random.choice(["female", "male"])
    return sex

# Start with list to represent our population


jackalopes = [{"name": "jill", "age": 0, "sex": "female", "is_pregnant": False},
              {"name": "jack", "age": 0, "sex": "male", "is_pregnant": False}]

# Need a year tracker (counter)
year_tracker = 0
# while population length less than 1000
population = len(jackalopes)
while 0 < population < 1000:
    print("Population", population)
    # Increase each jackalopes age by 1
    for x in range(len(jackalopes)):
        jackalopes[x]["age"] = jackalopes[x]["age"] + 1

        # for loop to add new jackalopes to population
        if jackalopes[x]["is_pregnant"] == True:
            jackalopes.insert(0, {"name": random_name(), "age": 0,
                              "sex": random_sex(), "is_pregnant": False})
            jackalopes.insert(0, {"name": random_name(), "age": 0,
                              "sex": random_sex(), "is_pregnant": False})
            jackalopes[x]["is_pregnant"] = False

        # if pair of jackalopes is between 4-8:
        if jackalopes[x]["age"] in range(4, 9):
            if jackalopes[x]["sex"] == "female":
                if x != len(jackalopes) - 1:
                    if jackalopes[x - 1]["sex"] == "male" or jackalopes[x + 1] == "male":
                        jackalopes[x]["is_pregnant"] = True
                elif jackalopes[x - 1]["sex"] == "male":
                    jackalopes[x]["is_pregnant"] = True

        # remove jackalopes when they reach 10 years old
    index = 0
    while index < len(jackalopes):
        if (jackalopes[index]['age'] > 10):
            jackalopes.pop(index)
        else:
            index += 1

    random.shuffle(jackalopes)

    # print(jackalopes)
    population = len(jackalopes)
    year_tracker += 1


for jackalope in jackalopes:
    print(
        f"{jackalope['name']}\t{jackalope['age']}\t{jackalope['sex']}\t{jackalope['is_pregnant']}")

print(
    f"It took {year_tracker} years to reach a population of {len(jackalopes)}")
# ["L", "C", "R"]
# jackalopes[x - 1] jackalopes[x] jackalopes[x + 1]


chess_board = [
    ["black", "white", "black", "white", "black", "white", "black", "white"],  # 0
    ["white", "black", "white", "black", "white", "black", "white", "black"],  # 1
    ["black", "white", "black", "white", "black", "white", "black", "white"],  # 2
    ["white", "black", "white", "black", "white", "black", "white", "black"],  # 3
    ["black", "white", "black", "white", "black", "white", "black", "white"],  # 4
    ["white", "black", "white", "black", "white", "black", "white", "black"],  # 5
    ["black", "white", "black", "white", "black", "white", "black", "white"],  # 6
    ["white", "black", "white", "black", "white", "black", "white", "black"],  # 7
    #   0        1        2        3        4        5        6       7
]


chess_board[1][0]

person = {
    "name": "dave",
    "fav_foods": ["pizza", "burgers", "fries", "tacos"]
}

person["fav_foods"][0]
