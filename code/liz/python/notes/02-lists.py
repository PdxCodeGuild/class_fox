'''
Notes: Lists
Mar 8, 2023
'''

animals = ['cat','dog','fox','llama','panda',]

print(animals[1]) # dog
print(animals[4]) # panda
print(animals[-1]) # panda
# print(animals[6]) # ERROR Index out of range
length_of_animals = len(animals) # 5
middle_index_of_animals = length_of_animals // 2 # 5/2 = 2.5, 5//2 = 2
# // rounds down to int
print(animals[middle_index_of_animals]) # fox, new middle dynamically changes
# code should try to avoid hard numbers

# .append method to add a new item to the end list
animals.append('kiwi')
print(animals) # new list has kiwi at new 5 index

# .insert method to add at a specific index
animals.insert(middle_index_of_animals+1,'turtle') # insert is for index before the desired spot
print(animals) # ['cat', 'dog', 'fox', 'turtle', 'llama', 'panda', 'kiwi']

# .pop method to remove last element of the list or at an index
animals.pop() # -1 index for default, meaning last element
print(animals) # ['cat', 'dog', 'fox', 'turtle', 'llama', 'panda']
animals.pop(1) # Remove dog
print(animals) # ['cat', 'fox', 'turtle', 'llama', 'panda']

# .remove method to specific what element should be removed, no index needed
animals.remove('llama') # remove will find and remove existing elements
print(animals) # ['cat', 'fox', 'turtle', 'panda']

# slicing
print(animals[1:3]) # ['fox', 'turtle']
# slice = list[a:b]
# splicing a list will grab indexes a through b
# splice does not include b
print(animals[1:4]) # ['fox', 'turtle', 'panda']
print(animals[1:]) # ['fox', 'turtle', 'panda']
# python assumes end and out of range is not affected
print(animals[:3]) # ['cat', 'fox', 'turtle']
# python assumes beginning if left blank

cool_animals = animals[:] # creates a copy of the original
cool_animals.append('zebra')
print(animals) # will not include zebra, cool animals is a copy

print(animals[::2]) # ['cat', 'turtle']
# goes through the whole list but skips every other

print(animals[::-1]) # ['panda', 'turtle', 'fox', 'cat']
# reverse order list

print(animals[0:4:-1]) # empty
# will never get to end

print(animals[4:0:-1]) # ['panda', 'turtle', 'fox']
# omits the first

# loop over a list
for animal in animals:
    print(animal)
    # animal variable could be anything
    # singular and plural syntax is common


