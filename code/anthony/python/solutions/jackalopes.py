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
Jackalopes can only mate with those immediately around them. Every generation Jackalopes are randomly shuffled.

"""

# Start with list to represent our population

jackalopes = [0, 0]

# Need a year tracker (counter)
year_tracker = 0
# while population length less than 1000
population = len(jackalopes)
while population < 1000:
    # Increase each jackalopes age by 1
    for x in range(0, len(jackalopes), 1):
        jackalopes[x] = jackalopes[x] + 1

        # if pair of jackalopes is between 4-8:
        if jackalopes[x] in range(4, 9):
            # for loop to add new jackalopes to population
            jackalopes.insert(0, 0)

        # remove jackalopes when they reach 10 years old
        if jackalopes[x] > 10:
            jackalopes.pop(x)
    # print(jackalopes)
    population = len(jackalopes)
    year_tracker += 1

print(year_tracker)
