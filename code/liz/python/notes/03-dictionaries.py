'''
Notes: dictionaries
Date: Mar 9, 2023
'''
shopping_list = {
    'nuts':'1 pound',
    'eggs':'1 carton',
    'potatoes':'1 pound',
    'milk':'1 gallon',
    'tomatoes':'4',
}

# only immutable data types can be keys
# values can be any datatype
# lists and dicts can be values, not keys
# keys are usually strings
# python will try to convert keys into str or int
# 1.0 = 1
# True = 1 or "True"; avoid using boolean True and False as keys
# cannot have identical keys

# for key in shopping_list:
#     # print(key) # prints only keys
#     print(f'{key} - {shopping_list[key]}')

# accessing values in a dictionary
shopping_list['milk'] # 1 gallon

# update value in dictionary
shopping_list.update({'tomatoes':'6'}) # change value of tomatoes key to 6

# or

shopping_list['tomatoes'] = '8' # change value of tomatoes key to 8

# add new item to shopping list
shopping_list.update({'bananas':'1 bunch',}) # also can add new key:value

shopping_list['grapes'] = '1 bunch' # add mew key:value

# shopping_list['cereal'] # if key does not exist, error will occur upon trying to call

# remove key:value pair from dict
del shopping_list['grapes'] # unlike lists and tuples

# check to see if something is a key in the dict
if 'cereal' in shopping_list:
    print(shopping_list['cereal'])
    # won't result in error because the if is FALSE
    # returns a boolean and will not get to printing 

# get all keys in a dict
# print(shopping_list.keys())

# get values in dict
# print(shopping_list.values())
# prints a list called dict_values

# get all keys and values
print(shopping_list.items())
# dict_items([('nuts', '1 pound'), ('eggs', '1 carton'), ('potatoes', '1 pound'), ('milk', '1 gallon'), ('tomatoes', '8'), ('bananas', '1 bunch')])

for key, value in shopping_list.items():
    print(key, value)
    # does not need to loop through the dict twice

# for key in shopping_list:
#     print(f'{key} - {shopping_list[key]}') 