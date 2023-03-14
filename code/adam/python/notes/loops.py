"""
Notes: Loops
Date: Mar 9, 2023
"""

# For
fruits = ["pear", "apple", "pineapple", "tomatoes"]

for fruit in fruits:
    if "p" in fruit:
        print(f"{fruit} is delicious")

for num in range(0, 5):    
    print(num)

# print(list(range(5)))
print("------------")

# While
counter = 0
while counter < 5:
    print(counter)
    counter += 1

print("-----------")
# continue
counter = 0
while counter < 5:
    counter += 1
    if counter == 2 :
        break
    print(counter)


print("------------")
# else
counter = 0
while counter < 5:
    counter += 1
    print(counter)
    if(counter == 3):
        break
else:
    print("The loop has completed")

# else on a for loop
for num in range(0, 5):
    print(num)
else:
    print("this also works!")