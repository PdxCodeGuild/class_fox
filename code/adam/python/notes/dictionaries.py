"""
Notes: dictionaries
Date: March 9th, 2023
"""

# only immutable datatypes can be in dictionaries
shopping_lists = {
"nuts": "1 pound",
"eggs": "1 carton",
"potatoes": "1 pound",
"milk": "1 gallon",
"tomatoes": "4",
3: "hooray",
(2, 3): 5,
1.1: "floats",
True: 'true' # dont use conditionals as key:value pairs
}

# accessing values in a dictionary
shopping_lists["milk"]

# update value in dictionary
shopping_lists.update({"tomatoes": "6"})
shopping_lists["tomatoes"] = "8"

# add a new key:value pair
shopping_lists.update({"bananas": "1 bunch"})
shopping_lists["grapes"] = "1 bunch"

# remove key: value pair
del shopping_lists["grapes"]


# if "cereal" in shopping_lists:
#     print(shopping_lists['cereal'])

# for key in shopping_lists:
#     print(key, shopping_lists[key])

# dictionary method
print(shopping_lists.keys()) # get all keys in dict

print(shopping_lists.values()) # get all values in dict

print(shopping_lists.items()) # get all keys and values

print("------------")
for key in shopping_lists:
    print(key, shopping_lists[key])

print("------------")
for key, value in shopping_lists.items:
    print(key, value)

