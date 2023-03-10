"""
Notes: dictionaries
Date: Mar 9, 2023
"""

shopping_list = {
    "nuts": "1 pound",
    "eggs": "1 carton",
    "potatoes": "1 pound",
    "milk": "1 gallon",
    "tomatoes": "4",
    3: "hooray",
    (2, 3): 5,
    1.1: "floats",
    True: "true"
}

# accessing values in a dictionary
shopping_list['milk']

# update value in dictionary
shopping_list.update({"tomatoes": "6"})
shopping_list["tomatoes"] = "8"

# Add a new key: value pair
shopping_list.update({"bananas": "1 bunch"})
shopping_list["grapes"] = "1 bunch"

# Remove key: value pair
del shopping_list["grapes"]


# if "cereal" in shopping_list:
#     print(shopping_list['cereal'])


# Get all keys from a dictionary
print(shopping_list.keys())

# Get all values from a dictionary
print(shopping_list.values())

# Get all keys and values
print(shopping_list.items())


# print("---------------")
# for key in shopping_list:
#     print(key, shopping_list[key])

print("---------------")
for key, value in shopping_list.items():
    print(key, value)
