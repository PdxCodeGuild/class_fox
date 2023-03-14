"""
Notes: Lists
Mar 8, 2023
"""

#           -5      -4     -3     -2      -1
animals = ['cat', 'dog', 'fox', 'llama', 'panda']
#           0       1     2       3        4  


# Access elements of a list using it's index
animals[1]

# length of a list
length_of_animals = len(animals) #5
# calculate middle using floor division to avoid floats
middle_index = length_of_animals // 2
# print(animals[middle_index]) #fox

# add element to list
animals.append('kiwi')
print(animals) # ['cat', 'dog', 'fox', 'llama', 'panda', 'kiwi']

# add element to list at a given position
animals.insert(middle_index + 1, 'turtle')
print(animals) # ['cat', 'dog', 'fox', 'turtle', 'llama', 'panda', 'kiwi']

# remove last element
animals.pop()
print(animals) # ['cat', 'dog', 'fox', 'turtle', 'llama', 'panda']

# remove element at a given position
animals.pop(1)
print(animals) # ['cat', 'fox', 'turtle', 'llama', 'panda']

# remove element from list
animals.remove("llama")
print(animals) # ['cat', 'fox', 'turtle', 'panda']

# slicing [start, stop, step]
print(animals[::])

# loop over a list
for animal in animals:
    print(animal)
